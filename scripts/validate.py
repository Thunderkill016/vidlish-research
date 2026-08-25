#!/usr/bin/env python3
"""Integrity checks for Vidlish Research machine-readable indexes and cycle fragments."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
BASE_FILES = ["sources.json", "claims.json", "principles.json", "features.json"]
FRAGMENT_FILES = sorted(p.name for p in DATA.glob("*-rq*.json"))
FILES = BASE_FILES + FRAGMENT_FILES

errors = []
objects = {}
collections = {"sources": [], "claims": [], "principles": [], "features": []}

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
for filename, payload in objects.items():
    for key, value in payload.items():
        if key == "schema_version" or not isinstance(value, list):
            continue
        for item in value:
            item_id = item.get("id")
            if not item_id:
                errors.append(f"{filename}: item missing id")
                continue
            if item_id in ids:
                errors.append(f"duplicate id {item_id}: {ids[item_id]} and {filename}")
            ids[item_id] = filename

for claim in collections["claims"]:
    for ref in claim.get("source_ids", []):
        if ref not in ids:
            errors.append(f"{claim['id']}: missing source reference {ref}")

for principle in collections["principles"]:
    for ref in principle.get("claim_ids", []):
        if ref not in ids:
            errors.append(f"{principle['id']}: missing claim reference {ref}")

for feature in collections["features"]:
    for ref in feature.get("principle_ids", []):
        if ref not in ids:
            errors.append(f"{feature['id']}: missing principle reference {ref}")
    rel_path = feature.get("path")
    if rel_path and not (ROOT / rel_path).exists():
        errors.append(f"{feature['id']}: missing feature spec path {rel_path}")

if errors:
    print("Validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"OK: validated {len(ids)} stable IDs across {len(FILES)} registry files")
