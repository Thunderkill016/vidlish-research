# Product decision layer

`05-products/` contains product hypotheses, benchmark notes and implementation-facing artifacts derived from research.

## Current status — provisional, not build authority

`META-001` identified foundational research gaps after the first 21 RQs were integrated. Therefore the existing Nếp v1 documents in this directory are **pre-meta-foundation design artifacts**.

They are useful because they show how `RQ-001`–`RQ-021` could fit into one product, but they must not be interpreted as:

- the final Nếp Method;
- an empirically validated curriculum;
- instructions to begin a new implementation;
- evidence that the legacy Vidlish product teaches effectively.

Current source-of-truth order:

```text
research
→ competing-evidence synthesis
→ SYN-METHOD-001
→ curriculum specification
→ product specification
→ implementation
```

See first:

- [`../00-foundations/ISLA_FIELD_COVERAGE_FRAMEWORK.md`](../00-foundations/ISLA_FIELD_COVERAGE_FRAMEWORK.md)
- [`../07-syntheses/META-001-research-coverage-validity-audit.md`](../07-syntheses/META-001-research-coverage-validity-audit.md)
- [`../decisions/ADR-005-research-first-reset.md`](../decisions/ADR-005-research-first-reset.md)

## Pre-meta-foundation Nếp v1 handoff

Retain for design history and hypotheses:

1. [`nep-v1-executable-product-spec.md`](./nep-v1-executable-product-spec.md) — provisional learner journey, surfaces, content model and v1 scope.
2. [`nep-v1-runtime-architecture.md`](./nep-v1-runtime-architecture.md) — provisional engine/service decomposition.
3. [`nep-v1-learner-model-evidence-contract.md`](./nep-v1-learner-model-evidence-contract.md) — careful evidence semantics that must be re-evaluated through `RQ-024` assessment-validity work.
4. [`nep-v1-build-slices.md`](./nep-v1-build-slices.md) — **paused** implementation ordering; do not execute as the current project plan.

Integrated pre-meta-foundation synthesis:

- [`../07-syntheses/SYN-SYS-001-nep-v1-integrated-learning-system.md`](../07-syntheses/SYN-SYS-001-nep-v1-integrated-learning-system.md)

Earlier durable decisions that remain useful as hypotheses/guardrails unless superseded:

- [`../decisions/ADR-001-research-evidence-contract.md`](../decisions/ADR-001-research-evidence-contract.md)
- [`../decisions/ADR-002-capability-evidence-runtime.md`](../decisions/ADR-002-capability-evidence-runtime.md)
- [`../decisions/ADR-003-progressive-placement-bootstrap.md`](../decisions/ADR-003-progressive-placement-bootstrap.md)
- [`../decisions/ADR-004-ai-is-mediated-not-authoritative.md`](../decisions/ADR-004-ai-is-mediated-not-authoritative.md)

Research-first reset:

- [`../decisions/ADR-005-research-first-reset.md`](../decisions/ADR-005-research-first-reset.md)

## Benchmark material

- [`benchmark-rules.md`](./benchmark-rules.md) — competitor behavior may inspire hypotheses but is never efficacy evidence by default.

## Boundary

Until `SYN-METHOD-001` is accepted, product documents may explore:

- candidate learner flows;
- data/evidence semantics;
- possible engine responsibilities;
- product guardrails;
- experiment parameters;
- technical feasibility.

They may **not** settle unresolved pedagogy by architecture choice.

A future application repository will own framework/library choices, database/API/UI/deployment implementation and concrete runtime architecture only after the research-derived method and curriculum contracts are established.