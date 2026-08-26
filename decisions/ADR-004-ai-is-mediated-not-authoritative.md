# ADR-004 — AI is a mediated service, not the learning authority

**Status:** accepted  
**Date:** 2026-08-26

## Context

Nếp can benefit from LLMs, ASR and TTS for generation, feedback, conversation, transcription and synthetic input. But `RQ-008`, `RQ-014`, `RQ-015` and `RQ-020` show that model/provider outputs have task- and population-specific validity limits, can drift after updates, and can create false evidence when used as a holistic authority.

## Decision

All AI components operate through explicit **role policies** and a reliability gateway.

```text
AI proposes / renders / observes
→ policy + validators + provenance
→ learner task or feedback
→ learner behavior
→ Evidence Engine decides what can be claimed
```

AI may:

- generate candidate examples/distractors/variants;
- rephrase hints within constraints;
- act as a bounded conversation partner;
- render TTS input;
- provide ASR observations/transcripts where validated;
- assist scoring where the scorer policy explicitly permits it.

AI may not, by default:

- assign one holistic English level that directly drives the learner model;
- convert ASR confidence into pronunciation mastery;
- mark a capability mastered from subjective conversational impression;
- silently rewrite evidence after feedback;
- expose arbitrary learner data to third parties;
- bypass deterministic constraints because generated content appears plausible.

## Required provenance

Any AI output that affects learner-facing content, feedback or evidence must be attributable to:

```text
role
provider
model/version
prompt/policy version
validators
fallback/abstention behavior
```

Where raw prompt/model versions are not stable provider concepts, Nếp still records the application-side policy/version that generated the call.

## Rejected alternatives

### LLM as central tutor/controller

Rejected because it combines curriculum selection, content generation, feedback and assessment into one opaque authority that is difficult to validate or reproduce.

### Vendor score as direct learner truth

Rejected because vendor metrics do not automatically validate the exact learner population, task or product claim.

### Avoid AI entirely

Rejected because AI can lower authoring cost and improve adaptive mediation when bounded by the research/evidence architecture.

## Consequences

Positive:

- AI providers can be swapped;
- high-risk decisions remain auditable;
- generated content can improve without making the learner model model-dependent;
- failures can fall back to deterministic/editorial paths.

Costs:

- gateway/policy infrastructure;
- regression suites;
- validator maintenance;
- more abstention/fallback cases than a naive AI-first architecture.

## Guardrails

- high-value scorers must be allowed to abstain;
- model/provider changes that affect evidence require revalidation/regression testing;
- raw audio/transcript retention is separate from derived evidence retention;
- AI cost/latency never substitutes for learning-benefit validation;
- optional AI/video services must not make the core A0 loop unavailable when they fail.

## Linked research

- `FEAT-AIG-001`
- `FEAT-ASR-001`
- `FEAT-SPK-001`
- `FEAT-INT-001`
- `FEAT-WRI-001`
- `SYN-SYS-001`
