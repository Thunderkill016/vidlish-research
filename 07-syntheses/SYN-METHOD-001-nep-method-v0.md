# SYN-METHOD-001 — Nếp Method v0

**Status:** initial evidence-backed method synthesis; not yet efficacy-validated as an integrated system  
**Date:** 2026-08-27  
**Scope:** Vietnamese-speaking adults beginning near zero / Pre-A1  
**Evidence governance:** `00-foundations/EVIDENCE_GRADING_PROTOCOL.md`  
**Foundation:** RQ-001–RQ-028, with P12 meta-foundation RQ-022–RQ-028 taking precedence when earlier integrations conflict

---

## 0. What this document is

This is the first attempt to state **the language-learning method itself** after the research-first reset.

It is not:

- a website specification;
- a screen flow;
- a database model;
- a curriculum unit list;
- a CEFR syllabus;
- an AI-agent architecture;
- a claim that the integrated Nếp system has already been proven effective.

The intended chain is:

```text
research
→ Nếp Method
→ curriculum
→ target-population validation
→ product
→ implementation
```

The old Vidlish application is not an input to this method except as negative design history.

---

# 1. Target learner and target-language-use scope

## 1.1 Initial target learner

Nếp v0 is designed first for:

```text
Vietnamese-speaking adult
+
near zero / Pre-A1 English ability
+
limited usable English despite possible prior school exposure
+
primarily self-directed learning
+
constrained time
+
wants English for real communication / study / work / life
```

This is a **design scope**, not a claim that all Vietnamese adults share one profile.

Relevant evidence from RQ-023 and RQ-026 shows heterogeneous goals, confidence, time constraints and target domains. Published Vietnamese needs studies are not sufficiently representative to declare one universal first task list (`CLM-NEED-007`–`016`).

Therefore:

```text
TARGET POPULATION
≠
ONE FIXED NEEDS PROFILE
```

## 1.2 Target-language-use architecture

RQ-023 supports using **target tasks/capabilities** as the primary needs-analysis unit (`CLM-NEED-001`–`005`; `EVA-MTH-001`).

Provisional architecture:

```text
portable cross-domain capabilities
        ↓
learner-specific target situations
        ↓
domain branches
```

Examples of capability families may eventually include:

- understand a short request/message;
- ask for clarification/repetition;
- provide simple relevant information;
- respond to a follow-up;
- read a practical message;
- write a practical message;
- manage misunderstanding;

but **the exact first capability inventory is not fixed by this method**. It requires `EXP-023` / direct target-needs work.

---

# 2. What “usable English ability” means

Nếp does not define English ability as:

```text
number of lessons completed
number of grammar points covered
vocabulary list percentage
XP / streak
AI score
CEFR label alone
```

The central unit is a **capability to process and/or produce meaning under specified conditions**.

## 2.1 Evidence levels are conditions, not psychological stages

From RQ-024 (`CLM-VAL-001`–`019`; `EVA-MTH-002`):

```text
TASK-BOUND OBSERVATION
        ↓
GENERALIZATION CANDIDATE
        ↓
CURRENT INDEPENDENT CAPABILITY

MEDIATED / EMERGING CAPABILITY
kept separate

DELAYED-RETENTION EVIDENCE
requires time

CHANGED-CONTEXT TRANSFER
requires meaningful novelty
```

These describe **what the evidence justifies**, not universal stages inside the learner's brain.

## 2.2 Three useful capability claims

### Current independent capability

The learner can perform the target behavior without answer-bearing support under representative conditions.

### Portable capability

The learner can perform under a meaningful change in cue, exemplar, context, interlocutor, content or task demand (`CLM-TRN-001`; `EVA-MTH-005`).

### Durable capability

The learner can perform after an explicit delay relevant to the intended use/retention horizon (`CLM-VAL-012`, `CLM-REV-001`; `EVA-MTH-004`).

A learner does not need to reach all three before learning continues. The system must simply avoid calling one of them another.

---

# 3. The Nếp learning model

## 3.1 Compact learner-facing formulation

The evidence converges most defensibly on this compact cycle:

```text
HIỂU NGHĨA / CHỨC NĂNG
        ↓
TỰ TRUY XUẤT / THỰC HIỆN
        ↓
NHẬN PHẢN HỒI + TỰ SỬA
        ↓
DÙNG TRONG BIẾN THỂ
        ↓
GẶP LẠI / TRUY XUẤT LẠI QUA THỜI GIAN
        ↓
NGÀY CÀNG ĐỘC LẬP + HIỆU QUẢ
```

Short label:

> **Hiểu → Tự lấy ra → Dùng → Sửa → Biến đổi → Giữ**

This is not a mandatory six-screen lesson template.

A target may enter the loop at different points; the loop may span days or weeks; not every target requires every mechanism in every session.

## 3.2 Why this is not one branded SLA theory

RQ-022 found no defensible basis for:

```text
input alone
explicit instruction alone
output alone
conversation alone
frequency alone
practice alone
```

as the complete method (`CLM-SLA-017`; `EVA-SLA-002`).

Nếp v0 is therefore **outcome- and bottleneck-sensitive** rather than loyal to a school of thought.

---

# 4. Core Method Constraints

These are the strongest method-level constraints currently justified. Confidence refers to the **scope stated here**, not to exact implementation details.

## M1 — Begin from meaning/capability, not language inventory

**Rule:** new teaching should be anchored to a meaningful interpretation, function or target capability rather than introduced merely because a grammar/vocabulary list says it is next.

Why:

- RQ-023: target tasks are more actionable than decontextualized skill/topic labels (`CLM-NEED-003`);
- RQ-022: meaningful input and form–meaning/function processing are necessary parts of learning;
- RQ-027: content inclusion and teaching order are separate (`CLM-CONT-025`; `EVA-MTH-017`).

Does **not** mean grammar explanation is forbidden.

Confidence: **moderate-high as a method constraint; exact first capabilities remain provisional.**

---

## M2 — Meaningful input is necessary, but input alone is not the full method

Learners need comprehensible/processable examples of the language in use.

But when the desired outcome is productive or interactive performance, comprehension exposure alone must not be assumed to create that ability (`CLM-SLA-004`–`007`, `CLM-SPK-002`; `EVA-MTH-008`).

Therefore:

```text
input-rich
≠ input-only
```

Confidence: **moderate-high for complementarity; dosage is unresolved.**

---

## M3 — Make form ↔ meaning/function processing necessary when it matters

For vocabulary, grammar/constructions, chunks and pragmatic routines, learners should not merely see a form; tasks should require them to connect it to relevant meaning/function.

RQ-012/RQ-022 show that structured interpretation can directly target problematic form–meaning processing and that visual salience alone is insufficient (`CLM-GRM-004`–`006`; `EVA-MTH-009`).

Use explicit explanation when it solves a real barrier such as:

- confusing form–meaning contrast;
- low salience;
- L1-tuned attention;
- opaque construction/chunk;
- feedback that otherwise cannot be interpreted.

Do not default to:

```text
rule
→ rule quiz
→ mastered
```

Confidence: **moderate.**

`CTR-SLA-001` remains open/bounded around explicit instruction versus spontaneous/implicit ability.

---

## M4 — Practice must elicit the capability being learned

A target skill requires actual practice in that response/processing mode.

Examples:

```text
typing ≠ speaking
reading text ≠ listening
recognition ≠ productive recall
reading model aloud ≠ independent spoken retrieval
revising AI-written text ≠ independent writing
```

Supported by RQ-024 (`CLM-VAL-008`), RQ-006 (`CLM-SPK-002`, `010`), vocabulary evidence and skill-specific syntheses.

This is one of Nếp v0's highest-confidence constraints because it is primarily a construct-validity boundary.

Confidence: **high.**

---

## M5 — Retrieval/performance comes before answer reveal when independent retrieval is the target

When the learning goal is to retrieve or generate language, the learner should normally attempt before seeing the full target answer.

After reveal, the same performance can still be useful learning/rehearsal, but it is not evidence that the answer was independently available before reveal.

Vocabulary/retrieval evidence supports retrieval for retention, with task alignment important (`CLM-VOC-007`, `CLM-REV-004`, `CLM-REV-006`; `EVA-MTH-003`).

Exception:

- the target is initial comprehension/exposure, not retrieval;
- the learner genuinely lacks enough knowledge for a productive attempt;
- support is intentionally being used to build mediated/emerging capability.

Confidence: **moderate-high for the evidence boundary; exact difficulty/support threshold unresolved.**

---

## M6 — Feedback should produce repair/learning, not just judgment

Corrective feedback is beneficial on average (`CLM-CF-001`) but no one feedback type wins everywhere.

Candidate policy from RQ-025:

```text
preserve original attempt
↓
identify target / consequence / likely repair readiness
↓
smallest useful feedback
↓
bounded self-repair when feasible
↓
escalate if learner cannot repair
↓
record post-feedback response separately
```

`CTR-CF-001` keeps prompts-vs-recasts disagreement explicit.

Immediate corrected output is not evidence that the learner possessed the capability before feedback. Later independent performance is required when the claim concerns learning (`CLM-CF-018`; `EVA-MTH-015`).

Confidence: **high that feedback can help and later independent evidence matters; low/moderate for exact escalation/timing policy.**

---

## M7 — Repetition must become variation

Repeating a task/item can improve performance and fluency, but same-task improvement is not transfer.

Nếp should move from supported/familiar performance toward **meaningful variation** appropriate to learner readiness:

```text
same target
→ changed exemplar
→ changed cue/context
→ changed communicative detail
→ changed interlocutor/task demand where relevant
```

Do not maximize variation immediately: RQ-005 shows contextual variability can add processing cost and may be less useful for lower-proficiency learners.

Confidence: **high for repetition ≠ transfer; moderate for progression/dose.**

---

## M8 — Revisit over time; immediate success is not retention

Spacing and retrieval improve delayed L2 retention relative to massed practice on average (`CLM-REV-001`; `EVA-MTH-004`).

Therefore useful language should reappear across time.

But:

```text
scheduler prediction
≠ mastery
```

and no universal interval/repetition count is established for Nếp.

Review should be driven by the intended capability and evidence condition, not merely by a generic flashcard state.

Confidence: **high for spaced revisit direction; low for exact scheduler policy.**

---

## M9 — Support is allowed; provenance is mandatory

Support can accelerate learning and reveal emerging capability.

For Vietnamese near-A0 learners, L1/Vietnamese support is legitimate. L1 gloss/meaning support has meaningful evidence, often with larger relative benefits for lower proficiency (`CLM-SCF-002`; `EVA-MTH-006`).

Possible support includes:

- Vietnamese gloss/explanation;
- model/example;
- caption/transcript;
- replay;
- planning;
- partial cue;
- slowed/segmented repair;
- explicit rule/pattern help.

But every support changes the evidence condition (`CLM-VAL-009`, `010`).

Thus:

```text
success with support
≠ same claim as independent success
```

Support should fade according to observed learner performance and task goal, not a fixed CEFR/vocabulary/date threshold.

Confidence: **high for provenance distinction; moderate for L1 usefulness; exact fading policy unresolved.**

---

## M10 — Content selection is multi-criteria; sequencing is a separate problem

The beginner inventory must include at least:

```text
lexeme / sense
multiword unit / collocation
construction / form–function pattern
pragmatic / interaction routine
```

Candidate selection uses:

```text
target-task value
+ portable utility
+ frequency
+ range / dispersion
+ corpus/modality/register fit
+ multiword/construction value
+ coverage contribution
+ learning cost / Vietnamese-L1 prior
+ generative/prerequisite value
+ individual learner gap
```

(`CLM-CONT-024`; `EVA-CONT-002`)

No one weighted formula is validated yet.

Forbidden shortcut:

```text
top 3000 words / EVP A1 / grammar profile
→ teaching order
```

Confidence: **moderate for multi-criteria direction; low for weights/exact first inventory.**

---

## M11 — Learner state is inferred conservatively and remains uncertain

Every learner-state update should conceptually preserve:

```text
what behavior occurred?
under what task?
what support/exposure?
how was it evaluated?
what claim is being made?
how far may it generalize?
```

A single correct response directly supports that response, not broad mastery (`CLM-VAL-003`; `EVA-MTH-002`).

The cost of false inference determines how much evidence is required (`CLM-VAL-019`).

Confidence: **high as an assessment/inference rule.**

---

## M12 — Personalize from actionable evidence, not learner stereotypes

Personalization requires:

```text
valid learner variable
→ plausible mechanism
→ treatment-relevant difference
→ reversible adaptation
→ better outcome
```

A main-effect correlation with achievement is insufficient for treatment assignment (`CLM-ID-017`; `EVA-MTH-016`).

Therefore:

- no VARK/learning-style routing;
- aptitude/working memory are not fixed ceilings;
- anxiety/WTC/self-efficacy can inform support/participation decisions but are not mastery;
- declared constraints/accessibility needs should be respected;
- prior literacy/schooling remains separate from English proficiency;
- Vietnamese population findings are priors, not diagnoses.

Confidence: **high as a boundary against unjustified personalization; specific adaptive policies remain experimental.**

---

# 5. Skill-specific method constraints

The core cycle is shared, but skills are not interchangeable.

## 5.1 Vocabulary and formulaic language

Goal is not a binary `known` flag.

Distinguish at minimum:

- form recognition/access;
- meaning/function;
- productive retrieval when needed;
- multiword/chunk knowledge;
- contextual use;
- delayed availability.

Deliberate establishment is efficient for high-value beginner content, but later contextual encounters/retrieval are needed (`CLM-SLA-014`, `015`, `CLM-VOC-007`).

Chunks are first-class learning units; knowing component words does not prove chunk retrieval.

---

## 5.2 Listening

Listening requires both lower-level access and message construction.

Potential bottlenecks include:

```text
sound discrimination / decoding
spoken-word access
segmentation / chunking
parsing / construction interpretation
gist/detail/discourse meaning
```

Written knowledge does not imply aural access (`CLM-LIS-003`). Decoding-focused instruction can help (`CLM-LIS-004`; `EVA-MTH-007`).

Assessment must distinguish:

```text
first-seen audio-only
replayed
caption/transcript-supported
segmented/slowed repair
```

Do not default to continuous auto-pause or always-on captions; these are support/repair options from RQ-010/011, not the listening curriculum.

---

## 5.3 Speaking

Near-A0 speaking can legitimately begin with short formulaic/bounded production; broad free conversation is not the entry requirement (`CLM-SPK-001`, `009`).

But productive capability requires **actual oral production** (`CLM-SPK-002`; `EVA-MTH-008`).

A defensible progression moves from support/rehearsal toward:

```text
short independent retrieval
→ recombination
→ contingent one-turn use
→ bounded multi-turn interaction
→ broader interaction later
```

Exact unlock thresholds remain unvalidated.

---

## 5.4 Pronunciation

Primary outcome:

```text
intelligibility
+ comprehensibility
+ communicatively consequential distinctions
```

not native-accent imitation (`CLM-PRN-001`; `EVA-MTH-010`).

Vietnamese evidence can prioritize probes for coda/cluster, information-bearing final sounds, stress/timing and relevant contrasts, but individual evidence must confirm the problem.

ASR/vendor scores are not pronunciation truth unless separately validated for population/task/construct.

---

## 5.5 Grammar / constructions

Teach grammar as **form ↔ meaning/function/use**, not as rule inventory coverage.

Use:

- meaningful exemplars;
- structured interpretation where the cue must be processed;
- concise explicit help where useful;
- productive practice when productive use is desired;
- varied exemplars/recombination;
- feedback/repair.

RQ-012 shows different relative advantages for receptive versus productive grammar outcomes (`CLM-GRM-004`; `EVA-MTH-009`).

Do not infer communicative grammar ability from rule explanation, judgment or fill-in-the-blank success (`CLM-GRM-015`).

---

## 5.6 Reading

Connected-text reading depends on written-word access, vocabulary/constructions and language comprehension (`CLM-READ-001`–`003`).

Easy/level-attuned extensive reading has positive evidence (`CLM-READ-006`; `EVA-MTH-011`).

Audio/gloss support is allowed, but supported understanding is not independent reading.

Independent reading evidence requires unfamiliar/self-paced text when the claim concerns portable reading (`CLM-READ-015`).

---

## 5.7 Writing

Writing capability requires learner-generated text appropriate to the target purpose.

Planning and feedback can help; AI/model text can support learning after provenance is preserved.

But:

```text
polished assisted text
≠ independent writing evidence
```

and improvement revising a treated text does not establish transfer (`CLM-WRI-005`; `EVA-MTH-012`).

Later new-task writing is needed for broader claims.

---

## 5.8 Interaction / pragmatics

Interaction is co-constructed and contingent (`CLM-INT-001`–`005`; `EVA-MTH-013`).

Valid interactive practice eventually needs:

- partner response contingent on learner meaning;
- turn management;
- understanding of preceding turn;
- clarification/repair when needed;
- pragmatic fit;
- shared-goal progress.

A clarification request can be successful interaction, not failure.

AI can provide practice but success with an accommodating AI partner does not establish transfer to unfamiliar humans.

---

## 5.9 Fluency / automaticity

Fluency is not raw speed.

Across modalities the safe principle is:

```text
efficiency improves
+
meaning/accuracy/intelligibility preserved
+
performance survives changed task/context
+
when claimed durable, survives delay
```

(`CLM-FLU-015`; `EVA-MTH-014`)

Repeated-task speed-up can be useful practice evidence, but it cannot be called portable fluency by itself.

---

# 6. Course-level balance

Nếp should be **comprehensive over time**, not all-skills-in-every-lesson.

The curriculum should eventually create adequate opportunities for:

```text
meaning-focused input
meaning-focused output
focused language learning where useful
fluency/automatization of known language
```

while also satisfying the capability/task model above.

This balance is a course-level heuristic, not a fixed 25/25/25/25 quota and not a mandate to touch every modality every day.

The provisional RQ-017 curriculum orchestrator must be resynthesized from this method rather than inherited unchanged.

---

# 7. How a target moves through learning

## 7.1 Generic target cycle

```text
1. TARGET CAPABILITY / MEANING
        ↓
2. UNDERSTANDABLE EXEMPLARS
        ↓
3. NECESSARY FORM ↔ MEANING/FUNCTION PROCESSING
        ↓
4. OPTIONAL EXPLICIT/L1 SUPPORT
   only when it solves a barrier
        ↓
5. TARGET-MODALITY RETRIEVAL / PERFORMANCE
        ↓
6. FEEDBACK + BOUNDED REPAIR
        ↓
7. REPEATED PRACTICE WITH INCREASING VARIATION
        ↓
8. CONTEXTUAL INPUT / INTERACTION / USE
        ↓
9. SPACED REVISIT
        ↓
10. INDEPENDENT DELAYED / CHANGED-CONTEXT EVIDENCE
```

This is an **orchestration model**, not a fixed screen sequence.

## 7.2 Skip logic is legitimate

If the learner already demonstrates capability under valid conditions:

```text
do not force instruction for coverage
```

If the learner fails only one bottleneck:

```text
repair the bottleneck
≠ restart the whole lesson
```

If support makes performance possible:

```text
store mediated/emerging evidence
→ teach
→ later re-probe independently
```

---

# 8. Content and sequencing contract

## 8.1 Selection asks “worth learning?”

Use RQ-023 + RQ-027 dimensions.

## 8.2 Sequencing asks “what is learnable/useful next?”

Sequence should depend on:

- target capability value;
- learner's current evidence;
- prerequisite language actually required;
- processing burden;
- support available;
- prior target exposure;
- need for review/transfer;
- desired modality/outcome.

A traditional syllabus position is not a prerequisite by itself.

## 8.3 Near-A0 load rule

For a beginner task, most supporting language should be already accessible or deliberately scaffolded so the learner can focus on the intended new bottleneck.

This is a **candidate curriculum constraint** rather than a validated percentage rule.

Do not set a universal `knownWords >= X%` threshold yet.

---

# 9. Feedback contract

Feedback should answer one of these jobs:

```text
make learner notice mismatch
clarify meaning/function
provide missing form/model
elicit self-repair
improve intelligibility
improve task/pragmatic effectiveness
support revision
```

It should not exist merely to maximize the number of red errors shown.

Prioritize when an error:

- blocks or materially changes meaning;
- prevents task completion/repair;
- affects a current target;
- recurs enough to justify attention;
- represents a useful form–meaning/function mapping;
- harms intelligibility/comprehensibility.

Exact global correction density is unresolved.

---

# 10. Support and Vietnamese/L1 contract

Vietnamese is a legitimate learning resource.

Use L1 when it improves efficiency/clarity for the target learning job, for example:

- rapid semantic establishment;
- concise explanation of difficult contrast;
- rescue after comprehension failure;
- metacognitive/strategy instruction;
- task instructions when English instructions add irrelevant load.

Do not use L1 support to fabricate independent English evidence.

Fading rule:

```text
successful supported processing
→ reduced support when feasible
→ independent probe later
```

not:

```text
A1 reached
→ Vietnamese banned
```

---

# 11. Personalization contract

Default adaptation hierarchy:

```text
1. observed language evidence
2. observed task/support response
3. learner-declared goals/constraints/accessibility needs
4. validated population/L1 prior
5. stable trait measure only when treatment interaction is defensible
```

All nonessential adaptations should be reversible.

A personalization feature must be evaluated against a simpler policy; complexity is not value.

---

# 12. What Nếp Method v0 explicitly rejects

The evidence is strong enough to reject these as universal method claims:

1. **Comprehensible input alone is sufficient for optimal adult learning.**
2. **Explicit grammar rules should always come first.**
3. **Grammar rules should never be taught.**
4. **Learners should wait to speak until they have a large vocabulary.**
5. **Speaking more, regardless of task quality, automatically means learning more.**
6. **A native-like accent is the pronunciation goal.**
7. **One CEFR/grammar/vocabulary inventory defines the teaching sequence.**
8. **The top N frequent words are the curriculum.**
9. **98% lexical coverage is a universal gate for all comprehension modalities.**
10. **Recognition proves productive knowledge.**
11. **Supported success proves independent mastery.**
12. **Immediate success proves retention.**
13. **Repeated-task success proves transfer.**
14. **One correct item proves stable capability.**
15. **One feedback type is universally best.**
16. **One spacing/repetition schedule is universally best.**
17. **VARK/learning-style matching is evidence-based personalization.**
18. **Aptitude or working memory should set a permanent learner ceiling.**
19. **Vietnamese learner research can diagnose every Vietnamese individual.**
20. **ASR/LLM/TTS output is automatically valid learner evidence.**
21. **Streak, completion, XP or time-on-app are evidence of English mastery.**

---

# 13. What remains unresolved

The research does **not** yet determine:

- exact first capability list;
- exact first vocabulary/chunk/construction/routine inventory;
- optimal ratio of input/output/focus/fluency;
- exact lesson/session length;
- exact review intervals/desired retention;
- exact support-fading thresholds;
- exact grammar explanation timing/dose;
- exact speaking unlock stages;
- exact correction type/timing/escalation for each error;
- exact pronunciation target order;
- exact text/video readiness thresholds;
- exact individual-difference adaptation rules;
- exact automated scoring thresholds;
- exact curriculum sequencing weights;
- whether the integrated Nếp Method outperforms simpler alternatives.

These must stay visible as validation questions.

---

# 14. Falsification and target validation

## 14.1 The method itself is a hypothesis bundle

The individual constraints are evidence-backed to different degrees.

The **integrated method** is not yet directly tested.

Nếp must therefore be willing to discover:

```text
some component adds no value
some sequence is inefficient
some support creates dependence
some personalization adds noise
some construct is measured badly
```

## 14.2 First target-population validation

Before scaling a full curriculum, test a small set of high-value capabilities with Vietnamese near-A0 adults.

At minimum compare:

```text
Nếp method slice
vs
simpler credible baseline(s)
```

Match learning time where possible.

Primary educational outcome:

```text
independent
+ delayed
+ changed-context
+ capability-relevant performance
──────────────────────────────────
learning time
```

Secondary outcomes:

- immediate learning;
- support dependence;
- error/repair profile;
- abandonment/effort;
- learner confidence/WTC (separate from mastery);
- false mastery decisions;
- time to useful capability.

## 14.3 Dogfooding is useful but insufficient

The owner using Nếp personally can reveal:

- UX problems;
- implementation bugs;
- confusing feedback;
- obvious curriculum problems;
- longitudinal evidence behavior.

But one learner cannot establish efficacy or population-level rules.

---

# 15. Evidence confidence summary

## High-confidence method boundaries

Current strongest items include:

- skill claims require tasks that elicit the skill;
- broader capability claims need broader/more representative evidence;
- support/retry/delay/transfer conditions change evidence meaning;
- immediate success is not retention;
- same-task repetition is not transfer;
- native-likeness is not the same as pronunciation intelligibility;
- frequency/CEFR coverage is not a teaching order;
- learner stereotypes/learning styles do not justify method assignment;
- AI/human agreement alone does not validate a scorer;
- engagement is not learning evidence.

## Moderate-confidence integrated learning direction

```text
meaningful input / exemplars
+
form ↔ meaning/function processing
+
targeted explicit/L1 support when useful
+
target-modality retrieval/performance
+
feedback/repair
+
repeated + varied practice
+
spaced revisit
+
contextual use / interaction where relevant
```

The components are supported; **their exact orchestration for Nếp is not yet proven** (`EVA-SLA-002`).

## Low/direct-validation-needed areas

- exact target capability set;
- content-selection weights;
- adaptive sequencing algorithm;
- support fading;
- feedback escalation;
- personalized treatment routing;
- AI/TTS/ASR use in high-stakes learner-state updates;
- the integrated method's efficacy versus strong baselines.

---

# 16. Nếp Method v0 in one paragraph

> **Nếp teaches useful English capabilities rather than checklist coverage. Learners meet understandable, relevant language and are helped to process how form expresses meaning/function; concise explicit or Vietnamese support is used when it removes a real barrier. When the target is retrieval, speaking, writing or interaction, learners must actually attempt that behavior before answer-bearing help can count as independent evidence. Feedback should create repair and learning, practice should progress from successful retrieval toward useful variation, and important language should be revisited across time. Support, retries and AI judgments keep their provenance. Progress is inferred conservatively from the behavior actually elicited, with changed-context and delayed performance used when claims concern transfer or durable ability. Content comes from target needs plus representative usage/corpus evidence, not CEFR/frequency order alone, and personalization is allowed only when learner evidence or validated treatment interactions justify it.**

---

# 17. Decision

`SYN-METHOD-001` is suitable as **Nếp Method v0 for curriculum derivation and empirical validation**, subject to the confidence/boundary labels above.

It is not suitable for the claim:

> “Nếp has been scientifically proven to be the optimal way to learn English.”

The defensible claim is:

> **Nếp Method v0 is a constrained instructional synthesis built from current SLA/ISLA, needs-analysis, assessment, feedback, corpus/content, individual-difference and skill-specific evidence. Its core inference boundaries are relatively strong; its target-population orchestration and efficacy remain to be tested directly.**

Next step:

```text
Nếp Method v0
→ derive curriculum contract
→ select first target capabilities/content
→ build small validation slices
→ test with target learners
→ revise method/curriculum
→ only then specify the full product
```
