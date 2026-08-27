#!/usr/bin/env python3
"""Integrity checks for Vidlish Research machine-readable indexes and core method references."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
BASE_FILES = ["sources.json", "claims.json", "principles.json", "features.json"]
FRAGMENT_FILES = sorted(p.name for p in DATA.glob("*-rq*.json"))
FILES = BASE_FILES + FRAGMENT_FILES

errors = []
objects = {}
collections = {
    "sources": [],
    "claims": [],
    "principles": [],
    "features": [],
    "evidence_assessments": [],
    "controversies": [],
}

for filename in FILES:
    path = DATA / filename
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        objects[filename] = payload
    except Exception as exc:
        errors.append(f"{filename}: invalid JSON: {exc}")
        continue
    for key in collections:
        value = payload.get(key, [])
        if value is not None and not isinstance(value, list):
            errors.append(f"{filename}: {key} must be a list")
            continue
        collections[key].extend(value or [])

ids = {}
collection_ids = {key: set() for key in collections}
for filename, payload in objects.items():
    for key, value in payload.items():
        if key == "schema_version" or not isinstance(value, list):
            continue
        for item in value:
            if not isinstance(item, dict):
                errors.append(f"{filename}: list item in {key} must be an object")
                continue
            item_id = item.get("id")
            if not item_id:
                errors.append(f"{filename}: item missing id")
                continue
            if item_id in ids:
                errors.append(f"duplicate id {item_id}: {ids[item_id]} and {filename}")
            ids[item_id] = filename
            if key in collection_ids:
                collection_ids[key].add(item_id)

for claim in collections["claims"]:
    for ref in claim.get("source_ids", []):
        if ref not in collection_ids["sources"]:
            errors.append(f"{claim['id']}: missing/invalid source reference {ref}")

for principle in collections["principles"]:
    for ref in principle.get("claim_ids", []):
        if ref not in collection_ids["claims"]:
            errors.append(f"{principle['id']}: missing/invalid claim reference {ref}")

for feature in collections["features"]:
    for ref in feature.get("principle_ids", []):
        if ref not in collection_ids["principles"]:
            errors.append(f"{feature['id']}: missing/invalid principle reference {ref}")
    rel_path = feature.get("path")
    if rel_path and not (ROOT / rel_path).exists():
        errors.append(f"{feature['id']}: missing feature spec path {rel_path}")

allowed_appraisal_values = {"high", "moderate", "low", "unclear"}
for assessment in collections["evidence_assessments"]:
    assessment_id = assessment.get("id", "<unknown-EVA>")
    claim_ref = assessment.get("claim_id")
    if claim_ref not in collection_ids["claims"]:
        errors.append(f"{assessment_id}: missing/invalid claim reference {claim_ref}")
    for ref in assessment.get("source_ids", []):
        if ref not in collection_ids["sources"]:
            errors.append(f"{assessment_id}: missing/invalid source reference {ref}")
    for axis in (
        "methodological_quality",
        "population_directness",
        "construct_directness",
        "replication_consistency",
        "product_transfer_directness",
    ):
        value = assessment.get(axis)
        if value not in allowed_appraisal_values:
            errors.append(
                f"{assessment_id}: {axis} must be one of {sorted(allowed_appraisal_values)}, got {value!r}"
            )
    if not assessment.get("rationale"):
        errors.append(f"{assessment_id}: rationale is required")

allowed_controversy_statuses = {
    "open",
    "open-moderated",
    "open-bounded",
    "provisionally-resolved",
    "superseded",
}
for controversy in collections["controversies"]:
    controversy_id = controversy.get("id", "<unknown-CTR>")
    status = controversy.get("status")
    if status not in allowed_controversy_statuses:
        errors.append(
            f"{controversy_id}: status must be one of {sorted(allowed_controversy_statuses)}, got {status!r}"
        )
    claim_refs = controversy.get("claim_ids", [])
    if not claim_refs:
        errors.append(f"{controversy_id}: at least one claim_id is required")
    for ref in claim_refs:
        if ref not in collection_ids["claims"]:
            errors.append(f"{controversy_id}: missing/invalid claim reference {ref}")
    for ref in controversy.get("source_ids", []):
        if ref not in collection_ids["sources"]:
            errors.append(f"{controversy_id}: missing/invalid source reference {ref}")
    if len(controversy.get("competing_positions", [])) < 2:
        errors.append(f"{controversy_id}: at least two competing_positions are required")
    if not controversy.get("boundary_conditions"):
        errors.append(f"{controversy_id}: boundary_conditions are required")
    if not controversy.get("current_resolution"):
        errors.append(f"{controversy_id}: current_resolution is required")
    if not controversy.get("would_change_if"):
        errors.append(f"{controversy_id}: would_change_if is required")

# Core method citations are part of the executable research contract. A typo or
# stale CLM/EVA/CTR reference should fail CI instead of silently degrading traceability.
method_path = ROOT / "07-syntheses" / "SYN-METHOD-001-nep-method-v0.md"
if method_path.exists():
    method_text = method_path.read_text(encoding="utf-8")
    method_refs = set(
        re.findall(r"\b(?:CLM|EVA|CTR)-[A-Z0-9]+(?:-[A-Z0-9]+)+\b", method_text)
    )
    for ref in sorted(method_refs):
        if ref not in ids:
            errors.append(f"{method_path.relative_to(ROOT)}: missing method evidence reference {ref}")
else:
    errors.append("missing core method file 07-syntheses/SYN-METHOD-001-nep-method-v0.md")

if errors:
    print("Validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(
    "OK: validated "
    f"{len(ids)} stable IDs across {len(FILES)} registry files "
    f"({len(collections['evidence_assessments'])} EVA, "
    f"{len(collections['controversies'])} CTR)"
)
