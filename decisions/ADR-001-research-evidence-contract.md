# ADR-001 — Research evidence contract

**Status:** accepted  
**Date:** 2026-08-25

## Context

Vidlish/Nếp already had research mixed into product documents. As the system grows, agents can easily copy a statement into product requirements without preserving its evidence strength, scope or uncertainty.

## Decision

Maintain a dedicated research repository with stable IDs linking:

```text
sources → claims → syntheses → principles → features → experiments
```

The application codebase consumes stable research IDs and concise decisions instead of duplicating full literature notes.

## Consequences

Positive:

- easier agent retrieval;
- explicit uncertainty;
- auditable product rationale;
- research can evolve without rewriting implementation history.

Costs:

- extra maintenance;
- IDs/indexes need validation;
- product docs must avoid stale copied summaries.

## Guardrail

A product feature may be built for UX/business reasons with evidence level `E`, but it must not be represented as research-backed until the evidence record supports that claim.
