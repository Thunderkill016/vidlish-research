# ADR-003 — Placement bootstraps the learner model; it does not define a permanent level

**Status:** accepted  
**Date:** 2026-08-26

## Context

A new learner needs a useful starting point, but a comprehensive placement battery creates friction and still cannot eliminate uncertainty. Self-assessment alone is too weak for important placement decisions, while testing every modality before learning delays first value.

`RQ-021` supports a progressive approach: short anchors, targeted frontier probes, a provisional route, then rapid recalibration from real learning evidence.

## Decision

Nếp will use placement as a **cold-start bootstrap**.

```text
prior
→ common anchors
→ targeted adaptive probes
→ provisional route
→ first real learning task
→ rapid recalibration
```

Placement creates provisional learner-state estimates and route recommendations only.

Rules:

- self-report is a routing prior, not direct ability evidence;
- untested constructs remain unknown;
- low-end/near-A0 item coverage is required;
- productive probes are conditional rather than mandatory blockers;
- uncertainty near a route boundary can trigger another probe or conservative fallback;
- early normal learning evidence can override placement quickly;
- CEFR mapping, if shown, is downstream reporting rather than the runtime source of truth.

## Rejected alternatives

### Long mandatory four-skill placement before first lesson

Rejected as the default because it spends learner time to resolve uncertainty that can often be resolved during learning.

### Self-report-only placement

Rejected because direct productive/placement studies show meaningful mismatch between perceived and observed performance.

### No placement; always start at lesson one

Rejected because stronger entrants would waste time and uneven prior knowledge would be ignored.

## Consequences

Positive:

- faster time to first useful learning;
- preserves uncertainty honestly;
- allows modality asymmetry;
- placement errors can self-correct quickly;
- first sessions become part of calibration rather than waiting for a perfect pre-test.

Costs:

- needs explicit correction/recalibration logic;
- first-session tasks must be evidentially useful;
- exact anchor/stop thresholds require product calibration;
- stronger QA needed for true-beginner floor coverage.

## Guardrails

- placement evidence cannot directly create `retained`;
- unknown cannot be written as weak;
- one modality cannot silently stand in for another;
- route correction is logged and used to improve placement;
- maximum onboarding burden is a versioned policy parameter.

## Linked research

- `SYN-PLC-001`
- `FEAT-ONB-001`
- `EXP-021`
- `PRN-277`–`PRN-292`
