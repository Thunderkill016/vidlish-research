# Collected Research Corpus

This directory connects the externally collected Nếp research corpus to the repository's existing evidence system.

## What is committed here

- source manifests with SHA-256 hashes for every major collected asset currently accounted for;
- aggregate market-demand and product-feedback outputs;
- robustness/sensitivity/model-selection summaries;
- PDF/source audit metadata and curriculum-evidence layer mapping;
- Google-material discovery summaries;
- integrated reports and methodology/limits.

## What is intentionally not committed to this public repository

1. **Raw Facebook/social corpus** — the source files may contain names, URLs, comments, and other user-generated metadata. The public repo stores provenance hashes and derived aggregate evidence instead.
2. **Third-party books/PDF binaries or extracted full text** — redistribution rights were not established. The public repo stores audit metadata, source identity, hashes, and derived research conclusions instead.
3. **Large processed bundles that embed the above raw materials** — these stay out of the public Git history.

This is deliberate: `source_manifest.*` accounts for the raw corpus without pretending that a public Git repository is an appropriate storage location for every source artifact. If the repository is moved to a private/restricted setup with appropriate rights, those raw assets can be attached under a separate `restricted/` storage policy.

## Evidence layers

```text
raw sources (restricted/local)
    ↓
normalized / audited evidence
    ↓
derived aggregate research (this directory)
    ↓
claims / syntheses / principles (existing Nếp Research structure)
    ↓
method → curriculum → product experiments
```

## Bundle contents

`bundles/nep-public-derived-corpus.zip` contains 28 public-safe files organized as:

- `derived/market/`
- `derived/catalog/`
- `derived/pdf/`
- `manifests/`
- `reports/`

See `manifests/source_manifest.csv` for every major raw/source asset currently accounted for, including files intentionally withheld from the public repository.
