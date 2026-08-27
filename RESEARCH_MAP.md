# Research Map

**Current phase:** P13 — `SYN-METHOD-001` method synthesis  
**Decision:** `ADR-005`  
**Audit:** `META-001`  
**Evidence protocol:** `00-foundations/EVIDENCE_GRADING_PROTOCOL.md`

## 1. Research objective

Derive an evidence-backed English-learning method for Vietnamese-speaking adults beginning near zero / Pre-A1, then derive curriculum and product behavior from that method.

Required order:

```text
research coverage
→ competing evidence
→ Nếp Method
→ curriculum
→ product
→ implementation
```

The existing Vidlish application is a **legacy prototype**, not a pedagogical source of truth.

## 2. Coverage status after P12

| Track | Current state | Next dependency |
| --- | --- | --- |
| Foundational SLA / ISLA | RQ-022 initial meta-foundation synthesis complete | `SYN-METHOD-001` |
| Vocabulary / formulaic language | RQ-001 evidence-of-knowing + RQ-027 content selection | method integration + target validation |
| Listening | RQ-003 + RQ-009/010/011 initial syntheses; inference bounded by RQ-024 | method integration |
| Retrieval / spacing / retention | RQ-004 initial synthesis; retention claims bounded by RQ-024 | method integration + target validation |
| Speaking / output | RQ-006; validity RQ-024; feedback RQ-025 | method integration |
| Pronunciation | RQ-007 + RQ-019 | method integration + target validation |
| Reading | RQ-013 + content selection RQ-027 | method integration |
| Writing | RQ-014; scorer validity RQ-024; feedback RQ-025 | method integration |
| Interaction / pragmatics | RQ-015; feedback RQ-025; routines RQ-027 | method integration |
| Fluency / automaticity | RQ-016 + RQ-022 | method integration |
| Grammar / constructions | RQ-012 + RQ-022 + RQ-025 + RQ-027 | method integration |
| Corrective feedback | RQ-025 initial meta-foundation synthesis complete | method integration + EXP-025 |
| Curriculum / sequencing | RQ-017 **provisional**; RQ-023/RQ-027 now supply missing needs/content foundations | resynthesize only after method |
| Needs / target language use | RQ-023 initial meta-foundation synthesis complete | method + EXP-023 |
| Assessment / learner-state inference | RQ-024 initial meta-foundation synthesis complete | method + EXP-024 |
| Individual differences / affect / SRL | RQ-026 initial meta-foundation synthesis complete | method + EXP-026 |
| Vietnamese L1 / multilingual support | RQ-002 + RQ-019 | method/content integration |
| AI / ASR / TTS | RQ-008 + RQ-020; subordinated to validity | subordinate to method |
| Motivation / sustained participation | RQ-018 + RQ-026 | subordinate to learning outcomes |
| Placement / onboarding | RQ-021; interpretation bounded by RQ-024 | after method/curriculum |
| Research methodology / evidence synthesis | **RQ-028 initial protocol complete** | apply during `SYN-METHOD-001` |

Full field checklist: `00-foundations/ISLA_FIELD_COVERAGE_FRAMEWORK.md`.

## 3. Completed focused cycles

All cycles are evidence modules. Completion means an **initial synthesis exists**, not that the intervention/product rule is proven for Nếp.

| RQ | Topic | Status |
| --- | --- | --- |
| RQ-001 | independent evidence of word/chunk knowledge | initial synthesis complete |
| RQ-002 | Vietnamese scaffolding | initial synthesis complete |
| RQ-003 | listening perception vs comprehension | initial synthesis complete |
| RQ-004 | retrieval / spacing / review | initial synthesis complete |
| RQ-005 | changed-context transfer | initial synthesis complete |
| RQ-006 | controlled speaking near A0 | initial synthesis complete |
| RQ-007 | pronunciation / intelligibility | initial synthesis complete |
| RQ-008 | ASR evidence validity | initial synthesis complete |
| RQ-009 | authentic-video readiness | initial synthesis complete |
| RQ-010 | adaptive caption/support | initial synthesis complete |
| RQ-011 | temporal repair / auto-pause | initial synthesis complete |
| RQ-012 | grammar / constructions | initial synthesis complete |
| RQ-013 | reading progression | initial synthesis complete |
| RQ-014 | writing progression | initial synthesis complete |
| RQ-015 | interaction / pragmatics | initial synthesis complete |
| RQ-016 | fluency / automaticity | initial synthesis complete |
| RQ-017 | integrated curriculum sequencing | **provisional; must be resynthesized after method** |
| RQ-018 | useful return / product behavior | initial synthesis complete |
| RQ-019 | Vietnamese-specific calibration | initial synthesis complete |
| RQ-020 | AI / TTS / LLM reliability | initial synthesis complete |
| RQ-021 | cold-start placement | initial synthesis complete |
| RQ-022 | competing SLA mechanisms / theories | **initial meta-foundation synthesis complete** (`CLM-SLA-001`–`019`) |
| RQ-023 | target needs / capability selection | **initial meta-foundation synthesis complete** (`CLM-NEED-001`–`016`); `EXP-023` planned |
| RQ-024 | assessment validity / learner-state inference | **initial meta-foundation synthesis complete** (`CLM-VAL-001`–`020`); `EXP-024` planned |
| RQ-025 | corrective feedback / self-repair | **initial meta-foundation synthesis complete** (`CLM-CF-001`–`019`); `EXP-025` planned |
| RQ-026 | individual differences / affect / SRL | **initial meta-foundation synthesis complete** (`CLM-ID-001`–`020`); `EXP-026` planned |
| RQ-027 | corpus-informed content selection | **initial meta-foundation synthesis complete** (`CLM-CONT-001`–`026`); `EXP-027` planned |
| RQ-028 | evidence grading / contradiction / update protocol | **initial meta-foundation synthesis complete** (`CLM-META-001`–`022`); `EXP-028` audit planned |

All `EXP-*` artifacts are experiment/research-study **plans** unless a corresponding result artifact exists.

## 4. P12 closure decision

P12 is **closed to the documented initial-synthesis level** required to begin method synthesis.

This means:

- major SLA mechanisms have been compared rather than selecting one branded method;
- target needs have a methodological contract;
- learner-state inference has a validity framework;
- corrective-feedback boundaries have been synthesized;
- individual-difference/personalization limits are explicit;
- content selection has needs + corpus + learnability constraints;
- evidence quality/directness and contradictions now have first-class representation.

It does **not** mean:

```text
Nếp is proven effective
or
all earlier claims are high confidence
or
all target-population experiments are complete
```

RQ-028 specifically requires strategic reappraisal of claims promoted into the core method.

## 5. RQ-028 evidence-governance result ✅

High-impact claims can now receive an `EVA-*` appraisal across:

```text
methodological_quality
population_directness
construct_directness
replication_consistency
product_transfer_directness
```

Credible disagreements are stored as `CTR-*` records containing competing positions, boundary conditions, current bounded resolution and revision triggers.

The legacy `A–E` claim level remains a retrieval shorthand; it is no longer sufficient on its own for a high-confidence Nếp Method rule.

Artifacts:

- `00-foundations/EVIDENCE_GRADING_PROTOCOL.md`
- `06-evidence/RQ-028-source-digest.md`
- `07-syntheses/RQ-028-evidence-grading-contradiction-update.md`
- `10-experiments/EXP-028-evidence-protocol-audit.md`
- `data/sources-rq028.json`
- `data/claims-rq028.json`
- `data/evidence-assessments-rq028.json`
- `data/controversies-rq028.json`
- updated `scripts/validate.py`

## 6. P13 — `SYN-METHOD-001 — Nếp Method v0` ← CURRENT

The method synthesis must define:

1. target learner and target-language-use domain;
2. what usable English ability means;
3. minimum learning conditions supported by converging evidence;
4. where conditions change by skill/learner/linguistic feature;
5. content-selection rules;
6. task/support/feedback rules;
7. assessment and inference rules;
8. justified personalization boundaries;
9. what remains uncertain/optional;
10. explicitly rejected universal claims;
11. falsification and target-learner validation plan.

### Promotion rule

A core high-confidence method statement must pass:

```text
verified sources
+ atomic supporting claims
+ RQ-024 construct/inference check
+ EVA appraisal
+ CTR contradiction check where relevant
+ explicit boundary/directness statement
+ falsification/validation path
```

Statements that do not pass may still appear as provisional constraints or validation hypotheses.

**No UI, database schema, route, framework choice or app architecture belongs in the core method.**

## 7. After method synthesis

```text
SYN-METHOD-001
→ curriculum specification
→ direct target-population validation
→ product specification
→ new implementation
```

Current `05-products/` files and `SYN-SYS-001` remain **pre-meta-foundation hypotheses/design history**. They may be mined selectively only after the method/curriculum contract says what the product needs.

## 8. Active high-confidence guardrails

- CEFR is descriptive, not a teaching algorithm.
- engagement/completion/streaks are not learning evidence.
- scheduler state is not mastery.
- recognition is not productive recall.
- supported success is not unsupported success.
- supported performance may still be mediated/emerging evidence if provenance is retained.
- first-seen performance differs from replayed/repeated performance.
- exact-task repetition is not transfer.
- immediate success is not delayed retention.
- a skill claim requires a task that elicits that skill.
- broader claims require broader/more representative evidence.
- high reliability does not by itself validate real-world extrapolation.
- motivation, WTC, confidence and anxiety are not mastery.
- preference is not evidence that preference-matched teaching improves learning.
- stable traits must not become fixed ceilings.
- corpus frequency/coverage is evidence for content selection, not teaching order.
- Vietnamese population evidence is a prior, not an individual diagnosis.
- strong accent is not synonymous with low intelligibility.
- AI/ASR/TTS outputs do not automatically justify learner-state claims.
- human agreement is not sufficient to prove an automated judgment construct-valid or unbiased.
- experiments remain hypotheses until results exist.

## 9. Research stop rule during P13

Do not reopen broad literature collection merely because more papers exist.

Open new research only when method synthesis identifies a **decision-critical unresolved claim** whose uncertainty could materially change the method.

Otherwise:

```text
synthesize
→ expose uncertainty
→ define target validation
```

instead of researching indefinitely.
