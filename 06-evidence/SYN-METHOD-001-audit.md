# Audit — SYN-METHOD-001 Nếp Method v0

**Audit date:** 2026-08-27  
**Audited artifact:** `07-syntheses/SYN-METHOD-001-nep-method-v0.md`  
**Evidence governance:** `00-foundations/EVIDENCE_GRADING_PROTOCOL.md`  
**Validation governance:** `00-foundations/NEP_METHOD_VALIDATION_CONTRACT.md`

## Decision

`SYN-METHOD-001` passes the **V0 research-traceability gate** and is accepted as the **provisional pedagogical source of truth for curriculum derivation and validation design**.

This decision does not assert that the integrated method is efficacy-validated or optimal.

## Audit checks

### 1. Scope separation — PASS

The method explicitly excludes UI, routes, database schema, framework choice, app architecture and the legacy Vidlish implementation.

The chain remains:

```text
research
→ method
→ curriculum
→ target validation
→ product
→ implementation
```

### 2. Method-reference integrity — PASS

`scripts/validate.py` now scans full `CLM-*`, `EVA-*` and `CTR-*` references appearing in `SYN-METHOD-001` and fails CI when a referenced record does not exist.

GitHub Actions passed after this rule was added.

### 3. Strategic evidence appraisal — PASS WITH DIRECTNESS LIMITS

Core promoted claims have dedicated `EVA-MTH-*` appraisals in addition to the older A–E shorthand.

The audit deliberately preserves cases such as:

```text
methodological quality = high
population directness = low
product-transfer directness = low/moderate
```

Therefore a strong literature base does not silently become a claim of direct validation for Vietnamese near-A0 self-study.

### 4. Contradiction handling — PASS

Decision-relevant controversies remain explicit rather than being erased by synthesis:

- `CTR-SLA-001` — explicit instruction vs spontaneous/implicit ability;
- `CTR-CF-001` — prompts vs recasts/supplied correction;
- `CTR-CONT-001` — lexical coverage thresholds vs continuous/modality-dependent comprehension.

The Method uses bounded resolutions, not universal winners.

### 5. Integrated-efficacy overclaim — PASS

The method repeatedly states that:

```text
supported components
≠
proven integrated method
```

It does not claim that Nếp is scientifically proven to be the optimal way to learn English.

### 6. Construct-validity boundaries — PASS

The method preserves the distinctions most likely to be corrupted during implementation:

```text
recognition ≠ productive recall
typing ≠ speaking
reading ≠ listening
supported ≠ independent
immediate ≠ retained
same-task repetition ≠ transfer
AI score ≠ learner truth
engagement ≠ learning
```

These boundaries are suitable to become curriculum/task acceptance criteria.

## Statements that remain deliberately provisional

No material overclaim required removing the method draft, but the following must not be converted into fixed product constants without direct evidence:

1. the exact first target capability inventory;
2. the exact orchestration/order/dose of the generic learning cycle;
3. content-selection weights and sequencing weights;
4. support-fading thresholds;
5. feedback escalation/timing policy;
6. review intervals and desired-retention targets;
7. speaking/interaction unlock thresholds;
8. pronunciation target order;
9. AI/ASR/TTS scorer thresholds;
10. individual-difference treatment routing;
11. the course-level balance among input, output, focused learning and fluency work;
12. integrated Nếp efficacy relative to simpler credible baselines.

## Important interpretation note

Statements such as `input-rich`, `meaning/capability first`, `target-modality practice`, `feedback/repair`, `variation`, and `spaced revisit` are **method constraints/directions at the scope stated in the synthesis**.

They are not evidence for one compulsory lesson template such as:

```text
screen 1 input
→ screen 2 grammar
→ screen 3 speaking
→ screen 4 feedback
→ screen 5 transfer
```

A curriculum may skip, reorder or revisit mechanisms when the target capability and learner evidence justify it, while preserving the core inference boundaries.

## Lock rule

From this audit forward:

- curriculum work must cite `SYN-METHOD-001` as its pedagogical parent;
- the old `SYN-SYS-001` and `05-products/` specifications cannot override the Method;
- implementation convenience cannot silently alter a Method constraint;
- material changes to the Method require evidence/target results and must follow `NEP_METHOD_VALIDATION_CONTRACT.md` change control;
- null/negative learner results are allowed to narrow or overturn the current Method.

## Next gate

The research repo may now enter curriculum derivation, but **not full-product implementation**.

Required sequence:

```text
SYN-METHOD-001
→ direct target-needs confirmation / first capability selection
→ curriculum contract
→ a very small number of construct-faithful learning slices
→ dogfood
→ Vietnamese near-A0 pilot
→ comparative delayed + changed-context validation
→ revise
```

This audit closes P13 at the **provisional method-source-of-truth** level, not at the efficacy-validation level.
