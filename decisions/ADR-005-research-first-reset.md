# ADR-005 — Research-first reset

**Status:** accepted  
**Date:** 2026-08-27

## Context

`RQ-001`–`RQ-021` produced useful feature-level evidence and an integrated Nếp v1 design. `META-001` found that several foundational research domains are still incomplete, including competing SLA theories, target needs/content selection, assessment validity, corrective feedback and individual differences.

The existing Vidlish application is an earlier prototype. Its implementation can provide engineering lessons, but it is not evidence that its curriculum or learning design is effective.

## Decision

Use this source-of-truth order:

```text
verified research
→ competing-evidence synthesis
→ Nếp Method
→ curriculum specification
→ product specification
→ implementation
```

`SYN-SYS-001` and the current Nếp v1 product handoff remain useful, but their status is provisional until the meta-foundation gate is closed.

## Consequences

Before accepting a new implementation plan:

- complete the P12 meta-foundation research defined by `META-001`;
- do not expand curriculum merely to increase framework/grammar/list coverage;
- do not treat software tests, feature completeness or internally consistent AI rationale as evidence of learning efficacy;
- keep product-specific assumptions falsifiable;
- use the old application only selectively for reusable engineering infrastructure after method/product contracts are settled.

Research prototypes are still allowed when their purpose is to test an explicit hypothesis.

## Exit condition

The reset ends when `SYN-METHOD-001 — Nếp Method v0` is accepted against the gates in `00-foundations/ISLA_FIELD_COVERAGE_FRAMEWORK.md`.