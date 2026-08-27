# Research Map

**Current phase:** P14 — curriculum derivation + validation design  
**Decision:** `ADR-005`  
**Meta-audit:** `META-001`  
**Evidence protocol:** `00-foundations/EVIDENCE_GRADING_PROTOCOL.md`  
**Method:** `07-syntheses/SYN-METHOD-001-nep-method-v0.md`  
**Method audit:** `06-evidence/SYN-METHOD-001-audit.md`  
**Validation contract:** `00-foundations/NEP_METHOD_VALIDATION_CONTRACT.md`

## 1. Research objective

Derive an evidence-backed English-learning method for Vietnamese-speaking adults beginning near zero / Pre-A1, then derive curriculum and product behavior from that method.

Required order:

```text
research coverage
→ competing evidence
→ Nếp Method
→ curriculum
→ target-population validation
→ product
→ implementation
```

The existing Vidlish application is a **legacy prototype**, not a pedagogical source of truth.

## 2. P12/P13 status

P12 meta-foundation RQ-022–RQ-028 is closed to the documented initial-synthesis level.

P13 `SYN-METHOD-001` has passed the V0 traceability audit and is accepted as the **provisional pedagogical source of truth for curriculum derivation and validation design**.

This means:

```text
research is sufficient to derive/test a method
≠
integrated Nếp efficacy is proven
```

The Method remains falsifiable and target-population validation may narrow, modify or reject parts of it.

## 3. Coverage status

| Track | Current state | Next dependency |
| --- | --- | --- |
| Foundational SLA / ISLA | RQ-022 integrated into Method | target validation only when decision-critical |
| Vocabulary / formulaic language | RQ-001 + RQ-027 integrated | curriculum content contract |
| Listening | RQ-003 + RQ-009/010/011 integrated | curriculum/task derivation |
| Retrieval / spacing / retention | RQ-004 integrated with RQ-024 boundaries | validation slices |
| Speaking / output | RQ-006 + RQ-024/025 integrated | curriculum/task derivation |
| Pronunciation | RQ-007 + RQ-019 integrated | learner-specific diagnostic/content derivation |
| Reading | RQ-013 integrated | curriculum derivation |
| Writing | RQ-014 + validity/feedback integrated | curriculum derivation |
| Interaction / pragmatics | RQ-015 + RQ-025/027 integrated | curriculum derivation |
| Fluency / automaticity | RQ-016 + RQ-022 integrated | later-stage curriculum derivation |
| Grammar / constructions | RQ-012 + RQ-022/025/027 integrated | curriculum content contract |
| Corrective feedback | RQ-025 integrated | slice-level policy validation |
| Curriculum / sequencing | RQ-017 is historical/provisional | **P14 resynthesis from Method** |
| Needs / target language use | RQ-023 method contract available | **V1 direct target-needs confirmation** |
| Assessment / learner-state inference | RQ-024 integrated | V2+ validation data |
| Individual differences / affect / SRL | RQ-026 integrated | only evidence-backed reversible adaptations |
| Vietnamese L1 / multilingual support | RQ-002 + RQ-019 integrated | slice-level support policy |
| AI / ASR / TTS | RQ-008 + RQ-020 subordinated to validity | product stage after curriculum need is known |
| Motivation / sustained participation | RQ-018 + RQ-026 | product stage; never overrides learning outcomes |
| Placement / onboarding | RQ-021 bounded by Method/RQ-024 | after first curriculum capabilities exist |
| Research methodology / evidence synthesis | RQ-028 active protocol | ongoing governance |

## 4. Completed research cycles

Completion below means an initial synthesis/evidence module exists. It does not mean the intervention is proven for Nếp.

| RQ | Topic | Status |
| --- | --- | --- |
| RQ-001 | independent evidence of word/chunk knowledge | complete |
| RQ-002 | Vietnamese scaffolding | complete |
| RQ-003 | listening perception vs comprehension | complete |
| RQ-004 | retrieval / spacing / review | complete |
| RQ-005 | changed-context transfer | complete |
| RQ-006 | controlled speaking near A0 | complete |
| RQ-007 | pronunciation / intelligibility | complete |
| RQ-008 | ASR evidence validity | complete |
| RQ-009 | authentic-video readiness | complete |
| RQ-010 | adaptive caption/support | complete |
| RQ-011 | temporal repair / auto-pause | complete |
| RQ-012 | grammar / constructions | complete |
| RQ-013 | reading progression | complete |
| RQ-014 | writing progression | complete |
| RQ-015 | interaction / pragmatics | complete |
| RQ-016 | fluency / automaticity | complete |
| RQ-017 | integrated curriculum sequencing | **provisional historical synthesis; superseded as build plan** |
| RQ-018 | useful return / product behavior | complete |
| RQ-019 | Vietnamese-specific calibration | complete |
| RQ-020 | AI / TTS / LLM reliability | complete |
| RQ-021 | cold-start placement | complete |
| RQ-022 | competing SLA mechanisms / theories | meta-foundation complete |
| RQ-023 | target needs / capability selection | meta-foundation complete; `EXP-023` planned |
| RQ-024 | assessment validity / learner-state inference | meta-foundation complete; `EXP-024` planned |
| RQ-025 | corrective feedback / self-repair | meta-foundation complete; `EXP-025` planned |
| RQ-026 | individual differences / affect / SRL | meta-foundation complete; `EXP-026` planned |
| RQ-027 | corpus-informed content selection | meta-foundation complete; `EXP-027` planned |
| RQ-028 | evidence grading / contradiction / update protocol | meta-foundation complete; `EXP-028` audit planned |

All `EXP-*` files are plans unless a corresponding result artifact exists.

## 5. `SYN-METHOD-001 — Nếp Method v0` ✅ V0

The Method defines:

1. target learner and target-language-use scope;
2. usable ability as capability under stated conditions;
3. twelve core method constraints;
4. skill-specific boundaries for vocabulary, listening, speaking, pronunciation, grammar, reading, writing, interaction and fluency;
5. content-selection versus sequencing rules;
6. support/L1 and feedback contracts;
7. learner-state inference boundaries;
8. evidence-backed personalization limits;
9. rejected universal claims;
10. unresolved validation questions;
11. falsification and target-validation direction.

Compact learning direction:

```text
understand meaning/function
→ retrieve / actually perform
→ feedback + repair
→ use with meaningful variation
→ revisit across time
→ become more independent and efficient
```

This is an orchestration model, **not a mandatory six-screen lesson template**.

## 6. Method audit result

V0 passed:

- Method scope is separate from product/implementation;
- method `CLM-*`, `EVA-*`, `CTR-*` references are now CI-validated;
- promoted core claims have strategic multidimensional appraisal;
- decision-critical controversies remain explicit;
- integrated efficacy is not overclaimed;
- construct boundaries are preserved.

See `06-evidence/SYN-METHOD-001-audit.md`.

### Method lock

From P14 forward:

```text
SYN-METHOD-001
= pedagogical parent

legacy Vidlish / SYN-SYS-001 / old product specs
= historical hypotheses only
```

A material Method change must follow `NEP_METHOD_VALIDATION_CONTRACT.md` and may be driven by positive, null or negative target learner data.

## 7. P14 — Curriculum derivation ← CURRENT

The next artifact must be a **curriculum contract**, not a full course inventory.

It must define at least:

### 7.1 Capability model

For every curriculum capability:

```text
real purpose / target task
required input/output modality
success condition
likely sub-capabilities
candidate language resources
prerequisites that are actually necessary
independent evidence task
changed-context evidence task
retention requirement when relevant
```

### 7.2 Content-entry rule

An item may enter curriculum because of a defensible combination of:

```text
target-task value
portable utility
frequency + dispersion
modality/register fit
formulaic/construction/pragmatic value
coverage contribution
learning cost / Vietnamese-L1 prior
generative/prerequisite value
learner gap evidence
```

No single list or corpus rank decides inclusion/order.

### 7.3 Sequencing rule

Selection asks:

> Is this worth learning?

Sequencing asks:

> Is this useful and learnable next for this learner/capability?

Sequence must consider current evidence, real prerequisites, processing load, support, prior exposure, review/transfer needs and target modality.

### 7.4 Task contract

A curriculum task must name the observable behavior it actually elicits and the inference it is allowed to support.

### 7.5 No full A1 build yet

P14 explicitly forbids jumping to:

```text
30 units
hundreds of lessons
full CEFR A1 path
```

before first capability slices pass V2–V5 validation.

## 8. V1 — Direct target-needs confirmation

`RQ-023` established the method, but not the exact first capability list.

Before fixing a broad beginner sequence, collect direct evidence from intended use.

For the owner-first phase, the owner's target situations can seed a **personal initial branch**, but they must not be relabeled a universal Vietnamese-near-A0 curriculum.

For broader release, use a mixed-method target-needs study with intended learners and relevant domain insiders as defined by `EXP-023`.

## 9. V2 — First construct-faithful slices

After the curriculum contract, select only a very small number of high-value capabilities and implement them end-to-end.

Each slice must preserve:

```text
target capability
→ understandable input/examples
→ necessary form↔meaning/function processing
→ target-modality attempt
→ feedback/repair
→ useful variation
→ spaced/delayed probe when relevant
→ changed-context probe
→ conservative evidence update
```

Mechanisms may be skipped/reordered when justified; the inference boundaries may not be faked.

## 10. V3–V6 validation path

```text
V3 owner dogfood / instrumentation sanity
↓
V4 Vietnamese near-A0 pilot
↓
V5 compare against credible simpler baseline(s)
↓
V6 replicate across capabilities / learners / time
```

Primary educational criterion when relevant:

```text
independent
+ delayed
+ changed-context
+ capability-relevant performance
──────────────────────────────────
learning time
```

See `00-foundations/NEP_METHOD_VALIDATION_CONTRACT.md`.

## 11. Active high-confidence guardrails

- CEFR is descriptive, not a teaching algorithm.
- engagement/completion/streaks are not learning evidence.
- scheduler state is not mastery.
- recognition is not productive recall.
- supported success is not unsupported success.
- first-seen differs from replayed/repeated performance.
- same-task repetition is not transfer.
- immediate success is not delayed retention.
- a skill claim requires a task that elicits that skill.
- broader claims require broader/more representative evidence.
- high reliability does not by itself validate real-world extrapolation.
- motivation/WTC/confidence/anxiety are not mastery.
- VARK/preference matching is not evidence-based method assignment.
- aptitude/working memory are not permanent ceilings.
- frequency/coverage/CEFR inventory is not teaching order.
- Vietnamese population evidence is a prior, not an individual diagnosis.
- strong accent is not synonymous with low intelligibility.
- AI/ASR/TTS outputs do not automatically justify learner-state claims.
- experiments remain hypotheses until results exist.

## 12. Research stop rule

Do not restart broad literature collection merely because more papers exist.

Open new research only when curriculum/validation identifies a **decision-critical unresolved claim** capable of changing the Method or curriculum contract.

Otherwise:

```text
derive
→ test
→ collect target evidence
→ revise
```

instead of researching indefinitely.
