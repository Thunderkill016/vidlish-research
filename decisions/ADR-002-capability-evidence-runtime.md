# ADR-002 — Capability/evidence runtime is the product source of truth

**Status:** accepted  
**Date:** 2026-08-26

## Context

Research cycles `RQ-001`–`RQ-021` repeatedly require Nếp to distinguish comprehension, recall, support dependence, transfer, retention, modality and task conditions. A fixed unit sequence, one CEFR level or one mastery percentage cannot preserve these distinctions well enough for adaptive decisions.

## Decision

Nếp runtime decisions will be based on:

```text
capability graph
+
decomposable learner evidence
+
versioned decision policies
```

The authoritative runtime path is:

```text
learner evidence
→ learner state
→ capability/curriculum decision
→ task/support contract
→ learner attempt
→ new evidence
```

The Curriculum Engine decides **what next**. Domain Learning Engines decide **how the relevant task works**. The Evidence Engine decides **what the attempt is allowed to support**.

The application may expose CEFR mappings, progress summaries or simple labels for communication, but these cannot replace the capability/evidence model as the internal decision source.

## Rejected alternatives

### Fixed textbook/unit progression

Rejected because learners can have uneven prior knowledge and modality-specific bottlenecks.

### One global mastery score

Rejected because it hides evidence provenance and encourages invalid substitution between constructs.

### LLM-selected curriculum without explicit state/contracts

Rejected because decisions become difficult to validate, reproduce and audit.

## Consequences

Positive:

- supports adaptive routing;
- preserves uncertainty;
- lets evidence from different modalities coexist;
- makes experiments/version changes interpretable;
- implementation can explain why a task was selected.

Costs:

- richer data model;
- more explicit task authoring;
- state policies require versioning;
- product UI must simplify without corrupting underlying distinctions.

## Guardrails

- completion cannot create mastery;
- support provenance is part of evidence;
- unobserved cannot become weak by default;
- no global level is required for every next-task decision;
- raw evidence remains auditable beneath derived snapshots.

## Linked research

- `SYN-SYS-001`
- `FEAT-CUR-001`
- `FEAT-A0-001`
- `FEAT-ONB-001`
- `FEAT-REV-001`
- `FEAT-TRN-001`
- `PRN-277`–`PRN-292`
