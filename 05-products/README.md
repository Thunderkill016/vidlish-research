# Product decision layer

`05-products/` contains implementation-facing product synthesis and benchmark notes.

This directory does **not** replace the application repository. It translates stable research decisions into contracts that the application can consume.

## Nếp v1 integrated handoff

Start here:

1. [`nep-v1-executable-product-spec.md`](./nep-v1-executable-product-spec.md) — learner journey, surfaces, content model, runtime behavior and v1 scope.
2. [`nep-v1-runtime-architecture.md`](./nep-v1-runtime-architecture.md) — logical services, ownership boundaries, task/scorer/support contracts and observability.
3. [`nep-v1-learner-model-evidence-contract.md`](./nep-v1-learner-model-evidence-contract.md) — authoritative evidence semantics and derived learner state.
4. [`nep-v1-build-slices.md`](./nep-v1-build-slices.md) — implementation order from invariant fixtures to the first end-to-end learning loop and later modules.

Integrated research synthesis:

- [`../07-syntheses/SYN-SYS-001-nep-v1-integrated-learning-system.md`](../07-syntheses/SYN-SYS-001-nep-v1-integrated-learning-system.md)

Durable decisions:

- [`../decisions/ADR-001-research-evidence-contract.md`](../decisions/ADR-001-research-evidence-contract.md)
- [`../decisions/ADR-002-capability-evidence-runtime.md`](../decisions/ADR-002-capability-evidence-runtime.md)
- [`../decisions/ADR-003-progressive-placement-bootstrap.md`](../decisions/ADR-003-progressive-placement-bootstrap.md)
- [`../decisions/ADR-004-ai-is-mediated-not-authoritative.md`](../decisions/ADR-004-ai-is-mediated-not-authoritative.md)

## Benchmark material

- [`benchmark-rules.md`](./benchmark-rules.md) — rules for using product benchmarks without treating competitor behavior as efficacy evidence.

## Boundary

Research/product decision docs may define:

- what claim a feature is allowed to make;
- data/evidence semantics;
- engine responsibilities;
- product guardrails;
- experiment parameters;
- implementation acceptance criteria.

The application repository owns:

- framework/library choices;
- concrete database schema and migrations;
- API implementation;
- UI components;
- deployment/runtime infrastructure;
- production feature flags;
- final code architecture within the constraints of the accepted ADRs.
