# Research Map

**Current phase:** meta-foundation before `SYN-METHOD-001`  
**Decision:** `ADR-005`  
**Audit:** `META-001`

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

## 2. Coverage status

| Track | Current state | Next dependency |
| --- | --- | --- |
| Foundational SLA / ISLA | RQ-022 initial meta-foundation synthesis complete | revisit after RQ-028 |
| Vocabulary / formulaic language | RQ-001 evidence-of-knowing + **RQ-027 content selection** | method integration + target validation |
| Listening | RQ-003 + RQ-009/010/011 initial syntheses; inference bounded by RQ-024 | method integration |
| Retrieval / spacing / retention | RQ-004 initial synthesis; retention claims bounded by RQ-024 | target validation |
| Speaking / output | RQ-006 initial synthesis; validity RQ-024; feedback RQ-025 | method integration |
| Pronunciation | RQ-007 + RQ-019 initial syntheses | target validation |
| Reading | RQ-013 initial synthesis; content selection RQ-027 | method integration |
| Writing | RQ-014 initial synthesis; scorer validity RQ-024; feedback RQ-025 | method integration |
| Interaction / pragmatics | RQ-015 initial synthesis; feedback RQ-025; routines RQ-027 | method integration |
| Fluency / automaticity | RQ-016 + RQ-022 initial synthesis | method integration |
| Grammar / constructions | RQ-012 + RQ-022; feedback RQ-025; content selection RQ-027 | method integration |
| Corrective feedback | RQ-025 initial meta-foundation synthesis complete | EXP-025 + method integration |
| Curriculum / sequencing | RQ-017 is **provisional**; RQ-023 target needs + RQ-027 content contract now available | resynthesize after RQ-028 |
| Needs / target language use | RQ-023 initial meta-foundation synthesis complete | EXP-023 + curriculum validation |
| Assessment / learner-state inference | RQ-024 initial meta-foundation synthesis complete | EXP-024 + method integration |
| Individual differences / affect / SRL | RQ-026 initial meta-foundation synthesis complete | EXP-026 + method integration |
| Vietnamese L1 / multilingual support | RQ-002 + RQ-019 initial syntheses | integrate with method/content |
| AI / ASR / TTS | RQ-008 + RQ-020; subordinated to RQ-024 validity | subordinate to method |
| Motivation / sustained participation | RQ-018 + RQ-026 cover product return and key L2 affect/ID boundaries | EXP-026 |
| Placement / onboarding | RQ-021; interpretation bounded by RQ-024 | target validation |
| Research methodology / evidence synthesis | **only remaining P12 foundation gap** | **RQ-028** |

Full field checklist: `00-foundations/ISLA_FIELD_COVERAGE_FRAMEWORK.md`.

## 3. Completed focused cycles

All items below are useful evidence modules. They are **not collectively a final Nếp Method**.

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
| RQ-017 | integrated curriculum sequencing | **provisional; revisit after P12** |
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

All `EXP-*` artifacts are experiment/research-study **plans** unless a corresponding result artifact exists.

## 4. P12 meta-foundation results so far

### RQ-022 — SLA mechanisms ✅

No single exclusive mechanism is sufficient as a complete adult instructed-L2 method. Current convergence supports complementary roles for meaningful input, form–meaning processing, targeted explicit help, production/practice for productive outcomes, interaction/feedback for contingent communication, rich exemplars, deliberate + incidental learning, automatization practice and mediated support kept distinct from independent performance.

### RQ-023 — Target needs ✅

Curriculum priority must come from target learners, target situations/tasks, importance/frequency/difficulty/training need and authentic target discourse—not CEFR order, textbook topics, grammar inventory or owner/AI intuition.

Provisional architecture:

```text
portable cross-domain capability core
↓
learner target situations
↓
domain branches
```

Exact first capabilities remain provisional pending direct target-population work.

### RQ-024 — Assessment validity ✅

Learner state is an inference from evidence under known conditions, not a property read directly from one answer.

Current evidence taxonomy:

```text
task-bound observation
→ generalization candidate
→ independent current capability

mediated/emerging capability   [separate]

delayed-retention evidence    [requires time]
changed-context transfer       [requires meaningful novelty]
```

These are epistemic evidence categories, not psychological acquisition stages.

### RQ-025 — Corrective feedback ✅

Corrective feedback is beneficial on average, but no single type/timing is universally best. Candidate policy:

```text
preserve original attempt
↓
judge target/error consequence + repair readiness
↓
smallest useful feedback
↓
bounded self-repair when feasible
↓
escalate information if repair is not feasible
↓
store post-feedback response separately
↓
later independent/delayed/changed-context evidence
```

Immediate repair is a learning event, not retroactive proof of original mastery.

### RQ-026 — Individual differences / affect / SRL ✅

Learner differences matter, but a difference only justifies personalization when the chain is defensible:

```text
valid learner variable
→ plausible mechanism
→ treatment-relevant difference
→ reversible adaptation
→ better relevant outcome
```

Key results:

- anxiety, WTC and self-efficacy are meaningful but task/context-sensitive;
- motivation/participation remain separate from language mastery;
- SRL can be taught rather than treated as a fixed learner quality;
- aptitude and working memory predict some outcomes but do not justify permanent ability ceilings;
- trait-based routing requires learner × treatment evidence;
- VARK/learning-style matching is rejected as a default;
- prior literacy/schooling must be represented separately from English proficiency;
- neurotype-specific foreign-language intervention evidence is too sparse for inferred diagnosis/routing;
- accessibility should start from declared needs and observable barriers.

### RQ-027 — Corpus-informed content selection ✅

Content selection and teaching order are separate decisions.

The content prior should combine:

```text
target-task value
+ portable general utility
+ frequency
+ range / dispersion
+ corpus / modality / register fit
+ multiword / construction / pragmatic value
+ coverage contribution
+ learning cost / Vietnamese-L1 prior
+ generative / prerequisite value
+ individual learner gap evidence
```

The curriculum must represent more than single words and grammar labels:

```text
lexeme / sense
multiword unit / collocation
construction / form–function pattern
pragmatic / interaction routine
```

No published word list, CEFR profile, vocabulary-size threshold or corpus rank is allowed to become the teaching order by itself.

Artifacts:
- `06-evidence/RQ-027-source-digest.md`
- `07-syntheses/RQ-027-corpus-informed-content-selection.md`
- `10-experiments/EXP-027-content-selection-policy.md`
- `data/sources-rq027.json`
- `data/claims-rq027.json`

## 5. Remaining P12 blocker

### RQ-028 — Evidence grading, contradiction and update protocol ← NEXT / FINAL P12 BLOCKER

**Question**  
How should the knowledge base separately grade methodological quality and directness, represent competing/null findings and boundary conditions, and revise earlier syntheses when stronger/newer evidence appears?

Required axes should include at least:

```text
methodological_quality
population_directness
construct_directness
replication_consistency
product_transfer_directness
```

Required behavior:

- distinguish study quality from relevance/directness;
- preserve null/negative evidence;
- represent contradictions/controversies as first-class records;
- encode population/task/treatment/outcome boundary conditions;
- avoid vote-counting studies as equally informative;
- support superseding/revising claims without deleting history;
- detect when a product principle rests on low-directness evidence;
- trigger resynthesis when stronger or more direct evidence changes confidence.

## 6. P13 — `SYN-METHOD-001` gate

Only after RQ-028 is closed to a documented satisfactory level.

`SYN-METHOD-001 — Nếp Method v0` must define:

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

**No UI, database schema, routes or app architecture in the core method.**

## 7. After method synthesis

```text
SYN-METHOD-001
→ curriculum specification
→ target-population validation
→ product specification
→ new implementation
```

Current `05-products/` files and `SYN-SYS-001` are retained as **pre-meta-foundation hypotheses/design history** and may be mined selectively, not executed as the current build plan.

## 8. Active high-confidence guardrails

- CEFR is descriptive, not a teaching algorithm.
- engagement/completion/streaks are not learning evidence.
- a scheduler state is not mastery.
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

## 9. Research stop condition

The goal is not to read every document ever published.

Research is sufficient for `SYN-METHOD-001` when:

1. every important domain in `ISLA_FIELD_COVERAGE_FRAMEWORK.md` is covered or explicitly scoped out;
2. important competing theories have been compared;
3. target needs and content selection have an evidence basis;
4. core learner-state inferences have a validity argument;
5. feedback and individual-difference boundaries are specified;
6. evidence directness to Vietnamese near-A0 is explicit;
7. contradictions/evidence quality are represented systematically;
8. unresolved product choices are labeled validation questions rather than scientific facts.
