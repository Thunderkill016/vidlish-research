# Research Map

**Current phase:** meta-foundation before `SYN-METHOD-001`  
**Decision:** `ADR-005`  
**Audit:** `META-001`

## 1. Research objective

Derive an evidence-backed English-learning method for Vietnamese-speaking adults beginning near zero / Pre-A1, then specify curriculum and product behavior from that method.

Required order:

```text
research coverage
→ competing evidence
→ Nếp Method
→ curriculum
→ product
→ implementation
```

The existing Vidlish application is a legacy prototype, not a pedagogical source of truth.

## 2. Coverage tracks

| Track | Core question | Current state | Next dependency |
| --- | --- | --- | --- |
| R01 Foundational SLA / ISLA | What mechanisms and instructional theories best explain adult L2 development? | **RQ-022 initial synthesis complete** | revisit after RQ-024/026/028 if validity/moderator evidence changes integration |
| R02 Vocabulary & formulaic language | What should be learned, how, and what counts as lexical knowledge? | RQ-001 strong on evidence-of-knowing; **content selection incomplete** | RQ-027 |
| R03 Listening | How should perception, lexical access, segmentation and comprehension progress? | RQ-003 + video support work complete at initial synthesis level | integrate after RQ-024 |
| R04 Retrieval, spacing & longitudinal retention | How should retrieval/review improve delayed retention efficiently? | RQ-004 initial synthesis complete | later target validation |
| R05 Speaking/output | How should bounded production become flexible speech? | RQ-006 initial synthesis complete | RQ-024, RQ-025 |
| R06 Pronunciation | What improves intelligibility/comprehensibility? | RQ-007 + Vietnamese calibration initial syntheses complete | later target validation |
| R07 Reading | How does supported decoding/comprehension become independent connected reading? | RQ-013 initial synthesis complete | integrate after RQ-024/027 |
| R08 Writing | How does controlled writing become independent useful writing? | RQ-014 initial synthesis complete | RQ-024, RQ-025 |
| R09 Interaction & pragmatics | How should learners manage contingent turns, repair and appropriateness? | RQ-015 initial synthesis complete | RQ-025 |
| R10 Fluency & automaticity | How does accurate/meaningful language become efficient without confusing repetition with general fluency? | RQ-016 initial synthesis complete | RQ-024 |
| R11 Grammar / constructions / form | How should form, meaning and use develop? | RQ-012 + RQ-022 foundational comparison complete at initial synthesis level | RQ-025/027 |
| R12 Corrective feedback | What feedback type/timing/focus helps which learner/feature/task? | **critical gap — fragmented across skills** | RQ-025 |
| R13 Curriculum / tasks / sequencing | What capabilities, task progression and course balance should define the curriculum? | RQ-017 provisional integration | **needs/content foundation missing** RQ-023/027 |
| R14 Needs analysis / target language use | What English does the target learner actually need to do? | **critical gap** | RQ-023 |
| R15 Assessment / diagnosis / inference | What task observations justify what learner-state claims? | RQ-005 transfer work only; **critical validity gap** | RQ-024 |
| R16 Individual differences / affect / SRL | Which learner differences justify adaptation? | product-return RQ-018 only; **major SLA gap** | RQ-026 |
| R17 Vietnamese L1 / multilingual support | How should Vietnamese/L1 evidence guide support without stereotyping? | RQ-002 + RQ-019 initial syntheses complete | integrate with RQ-026/027 |
| R18 Technology / AI / ASR / TTS | Where does technology improve learning and where are its judgments invalid? | RQ-008 + RQ-020 initial syntheses complete | subordinate to method |
| R19 Authentic/video-mediated input | When and how can authentic audiovisual material support learning? | RQ-009/010/011 initial syntheses complete | lower priority than P12 foundations |
| R20 Motivation / sustained participation | How should language motivation, anxiety, autonomy and product return interact? | RQ-018 covers product behavior; **L2 affect incomplete** | RQ-026 |
| R21 Placement / onboarding | How should the initial learner model be bootstrapped? | RQ-021 initial synthesis complete | RQ-024 validity work |
| R22 Research methodology / evidence synthesis | How should evidence quality, directness, contradiction and revision be represented? | **critical gap** | RQ-028 |

For the full field checklist see `00-foundations/ISLA_FIELD_COVERAGE_FRAMEWORK.md`.

## 3. Completed focused cycles — useful but not collectively a final method

| RQ | Topic | Status |
| --- | --- | --- |
| RQ-001 | independent evidence of word/chunk knowledge | initial synthesis complete |
| RQ-002 | Vietnamese scaffolding | initial synthesis complete |
| RQ-003 | listening perception vs comprehension | initial synthesis complete |
| RQ-004 | retrieval / spacing / review | initial synthesis complete |
| RQ-005 | changed-context transfer | initial synthesis complete |
| RQ-006 | controlled speaking near A0 | initial synthesis complete |
| RQ-007 | Vietnamese pronunciation / intelligibility | initial synthesis complete |
| RQ-008 | ASR evidence validity | initial synthesis complete |
| RQ-009 | authentic-video readiness | initial synthesis complete |
| RQ-010 | adaptive caption/support | initial synthesis complete |
| RQ-011 | temporal repair / auto-pause | initial synthesis complete |
| RQ-012 | grammar / constructions | initial synthesis complete |
| RQ-013 | reading progression | initial synthesis complete |
| RQ-014 | writing progression | initial synthesis complete |
| RQ-015 | interaction / pragmatics | initial synthesis complete |
| RQ-016 | fluency / automaticity | initial synthesis complete |
| RQ-017 | integrated curriculum sequencing | **provisional; must be revisited after P12** |
| RQ-018 | useful return / product behavior | initial synthesis complete; does not cover full L2 affect/ID domain |
| RQ-019 | Vietnamese-specific calibration | initial synthesis complete |
| RQ-020 | AI/TTS/LLM reliability | initial synthesis complete |
| RQ-021 | cold-start placement | initial synthesis complete; validity work pending RQ-024 |
| RQ-022 | foundational SLA mechanisms / competing theories | **initial meta-foundation synthesis complete** (`CLM-FND-001`–`019`) |

All `EXP-001`–`EXP-021` are experiment **plans** unless/until corresponding result artifacts exist.

## 4. P12 — Meta-foundation blocker before Nếp Method or new build

### RQ-022 — Foundational SLA mechanisms and competing instructional theories ✅ initial synthesis

**Question**  
Which learning mechanisms and instructional theories have the strongest converging evidence for adult instructed L2 development, which predictions conflict, and what does each imply for Vietnamese near-A0 self-study?

**Result:** no single exclusive theory/mechanism is sufficient as a complete method. Current convergence supports complementary roles for meaningful input, form–meaning processing, targeted explicit help, production/practice for productive outcomes, interaction/feedback for contingent communication, rich exemplars, deliberate + incidental learning, automatization practice, and mediated support kept distinct from independent performance.

Artifacts:

- `06-evidence/RQ-022-source-digest.md`
- `07-syntheses/RQ-022-foundational-sla-mechanisms.md`
- `data/sources-rq022.json`
- `data/claims-rq022.json`

No `PRN-*`, feature or product policy was created because RQ-022 is a foundation synthesis.

### RQ-023 — Target needs and capability selection ← NEXT

**Question**  
What real-world English tasks/capabilities are highest-value for the target population, and how should current needs, target situations, learner goals and general-English portability determine the first curriculum?

Must use triangulated needs analysis rather than one owner/AI intuition.

### RQ-024 — Language-assessment validity and learner-state inference

**Question**  
What observations under what task/support/scorer conditions justify what learner-state inference, with what uncertainty, reliability and generalizability?

Must revisit:

- `understood`;
- `recalled`;
- `transferred`;
- `retained`;
- modality-specific claims;
- support contamination;
- diagnostic classification;
- changed-context generalization;
- automated/human scoring.

### RQ-025 — Corrective feedback and self-repair policy

**Question**  
Which corrective-feedback type, explicitness, timing, focus and repair opportunity best serve which construct, learner, linguistic feature and task?

Must compare oral/written feedback, recasts, prompts, explicit/metalinguistic feedback, self-repair, focused/unfocused and immediate/delayed policies.

### RQ-026 — Individual differences, affect and self-regulated learning

**Question**  
Which learner differences materially affect learning/participation, and which adaptations are justified rather than personalization theater?

Must cover at minimum:

- language-learning anxiety;
- willingness to communicate;
- self-efficacy;
- autonomous/controlled motivation;
- self-regulated learning / metacognition;
- aptitude;
- working-memory/cognitive-resource evidence;
- prior literacy/education;
- accessibility/neurodiversity only to the level evidence supports.

### RQ-027 — Corpus-informed beginner language/content selection

**Question**  
Which words, chunks, constructions, functions and pragmatic routines should be prioritized by combining target needs with real-language frequency/range/dispersion/coverage, formulaicity, learnability and prerequisite value?

This RQ decides **what English is worth spending learning time on**. It must not turn a wordlist, grammar profile or corpus ranking into a teaching order by itself.

### RQ-028 — Evidence grading, contradiction and update protocol

**Question**  
How should the knowledge base separately grade methodological quality and directness, represent competing/null findings and boundary conditions, and revise earlier syntheses when stronger/newer evidence appears?

Required output should add explicit axes such as:

```text
methodological_quality
population_directness
construct_directness
replication_consistency
product_transfer_directness
```

and a first-class controversy/contradiction representation.

## 5. P13 — Method synthesis gate

Only after P12 is closed to a documented satisfactory level:

### SYN-METHOD-001 — Nếp Method v0

Must define:

1. target learner and target-language-use domain;
2. what usable English ability means;
3. minimum learning conditions supported by converging evidence;
4. where conditions change by learner/skill/linguistic feature;
5. content-selection rules;
6. task/support/feedback rules;
7. assessment and inference rules;
8. what remains uncertain/optional;
9. explicitly rejected universal claims;
10. falsification and target-learner validation plan.

**No UI, database schema, routes or app architecture in the core method.**

## 6. P14 — Curriculum specification

After `SYN-METHOD-001`:

- define first target capability set from RQ-023;
- define vocabulary/chunk/construction content from RQ-027;
- define prerequisite relationships;
- define task families and skill/modal progression from the method;
- define assessment probes and confidence from RQ-024;
- define feedback from RQ-025;
- define learner adaptations from RQ-026;
- define target-population validation before scale.

## 7. P15 — Product specification and implementation

Only after the curriculum contract exists:

```text
Nếp Method
→ curriculum
→ product UX/runtime
→ implementation
```

The current files in `05-products/` and `SYN-SYS-001` are retained as pre-meta-foundation hypotheses/design history and may be mined selectively, not executed as the present plan.

## 8. Current high-confidence guardrails that remain active

These are not the full Nếp Method, but they are strong enough to keep as research guardrails while P12 proceeds:

- CEFR is descriptive, not a teaching algorithm.
- engagement/completion/streaks are not learning evidence.
- a scheduler state is not language mastery.
- recognition is not productive recall.
- supported success is not unsupported success.
- first-seen performance differs from repeated/replayed performance.
- exact-task repetition is not transfer.
- immediate success is not delayed retention.
- a skill claim requires a task that actually elicits that skill.
- Vietnamese population evidence is a prior, not an individual diagnosis.
- strong accent is not synonymous with low intelligibility.
- AI/ASR/TTS outputs do not automatically justify learner-state claims.
- experiments remain hypotheses until results exist.

## 9. Research stop condition

The goal is **not** to research forever or literally read every document ever published.

Research becomes sufficient for `SYN-METHOD-001` when:

1. every field domain in `ISLA_FIELD_COVERAGE_FRAMEWORK.md` is covered or explicitly scoped out;
2. the important competing theories have been compared;
3. target needs/content selection have an evidence basis;
4. core learner-state inferences have a validity argument;
5. evidence directness to Vietnamese near-A0 is explicit;
6. unresolved product-specific choices are labeled as validation questions rather than scientific facts.

That is the gate between a research program and an endlessly expanding literature collection.