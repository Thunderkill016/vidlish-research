# META-001 — Research coverage and validity audit before Nếp Method

**Status:** meta-audit complete; foundation gaps open  
**Date:** 2026-08-27  
**Scope:** `RQ-001`–`RQ-021`, repository research architecture, and field-coverage comparison against contemporary ISLA/SLA/ELT reference domains.  
**Important:** this is a research-program audit. It does not create new learner-efficacy claims.

## 1. Why this audit was necessary

The repository accumulated 21 focused research cycles and then integrated them into `SYN-SYS-001` and Nếp v1 product handoff documents.

That sequence created a legitimate concern:

```text
many well-researched local decisions
        ↓
can look like
        ↓
a fully validated global teaching method
```

but the implication does not follow automatically.

The audit therefore asks four questions:

1. **Coverage:** have the major scientific/pedagogical domains needed for a complete teaching system actually been researched?
2. **Validity:** does the current evidence architecture support the strength of learner inferences the product wants to make?
3. **Controversy:** were competing schools/theories compared, or were compatible-looking pieces blended too early?
4. **Readiness:** is the current integrated product synthesis mature enough to become the source of truth for a new implementation?

## 2. Audit method

### Repository review

The audit reviewed:

- `RESEARCH_MAP.md`;
- `AGENTS.md` and evidence-handling rules;
- `00-foundations/`;
- source digests `RQ-001`–`RQ-021`;
- syntheses `RQ-001`–`RQ-021`;
- `SYN-SYS-001`;
- the human-readable evidence matrix;
- machine-readable claim/principle/source architecture;
- feature specs and experiment plans;
- validation script behavior;
- provisional product handoff documents.

### External field-mapping scan

A discovery scan reviewed 50 search results across five workstreams:

1. comprehensive instructed-SLA field maps;
2. individual differences / affect / self-regulation;
3. curriculum / needs / TBLT / form-focused instruction;
4. assessment validity / diagnostic assessment;
5. vocabulary / corpus-informed content selection.

The scan used contemporary handbooks, systematic reviews, meta-analyses and methodological syntheses to identify **missing research domains**, not to import claims without source-level extraction.

High-signal anchors included:

- Loewen, *Introduction to Instructed Second Language Acquisition* (3rd ed., 2025), DOI `10.4324/9781003355212`;
- *The Routledge Handbook of Instructed Second Language Acquisition*;
- *The Cambridge Handbook of Language Learning*;
- *The Cambridge Handbook of Corrective Feedback in Second Language Learning and Teaching*;
- *The Routledge Handbook of Second Language Acquisition and Input Processing*;
- Kang, Sok & Han, 2019, 35-year form-focused instruction meta-analysis, DOI `10.1177/1362168818776671`;
- Norris & Ortega, 2000, L2 instruction meta-analysis, DOI `10.1111/0023-8333.00136`;
- Bryfonski & McKay, TBLT implementation meta-analysis, DOI `10.1177/1362168817744389`;
- expanded Evidence-Centered Design for learning/assessment systems, DOI `10.3389/fpsyg.2019.00853`;
- current corpus/vocabulary curriculum syntheses by Nation, Webb, Dang and related work.

This scan is not a replacement for the new RQs below.

## 3. Executive conclusion

The current repository is **substantially better than an intuition-driven product plan**, but it is **not yet a comprehensive evidence base from which a final teaching method should be declared**.

The central finding is structural:

> **The repository is strongest at feature-level pedagogical questions and weakest at the foundational layer that should decide how those features fit together.**

The clearest evidence is that the current foundational learning model is explicitly marked `seeded` and calls itself a product hypothesis, while downstream work already defines a full adaptive learning architecture.

Therefore:

```text
RQ-001…RQ-021
= valuable evidence modules

SYN-SYS-001
= plausible integration hypothesis

Nếp Method
≠ established yet
```

## 4. What is strong and should be preserved

### 4.1 Research governance

The strongest part of the repository is its epistemic discipline:

- source ≠ claim ≠ synthesis ≠ product implication;
- no invented evidence;
- uncertainty and population limits must be recorded;
- CEFR is descriptive, not a teaching algorithm;
- engagement is not mastery;
- AI is not evidence authority by default;
- stable IDs and traceable links are required.

This is an unusually good foundation for AI-assisted research and must remain.

### 4.2 Support/evidence provenance

The repository repeatedly protects distinctions such as:

```text
first-seen success
≠ repeated success

supported success
≠ unsupported success

recognition
≠ productive recall

trained-item success
≠ changed-context success

immediate success
≠ delayed retention
```

These distinctions are defensible and highly valuable even if their exact thresholds remain unvalidated.

### 4.3 Delayed and changed-context evaluation

The insistence that a learning policy should eventually be evaluated on delayed, unseen/parallel or changed-context performance is one of the strongest cross-RQ ideas in the repository.

It protects the product from optimizing only same-session exercise scores.

### 4.4 Vietnamese evidence as prior, not stereotype

`RQ-019` correctly prevents population-level Vietnamese findings from becoming deterministic learner labels.

The general structure:

```text
population prior
→ cheap probe
→ individual evidence
→ confirm / override
```

should survive the meta-foundation phase.

### 4.5 Technology is subordinate to pedagogy

ASR, TTS, LLMs, captions and video are treated as tools whose validity depends on the task and inference. This is preferable to making a technology category itself the learning method.

### 4.6 Intelligibility-first pronunciation

The pronunciation track correctly resists native-accent imitation as the default objective and keeps communicative consequence central.

## 5. Critical gap 1 — foundational SLA comparison was never completed

### Current state

`R01 Second-language acquisition` remains `seeded`.

The foundational learning model itself says:

```text
status: seeded
```

and calls its loop a **current product hypothesis**.

Yet the repository later synthesizes an evidence-driven capability architecture around that loop.

### Why this matters

Contemporary instructed-SLA reference works do not converge on one single mechanism. Major instruction-relevant perspectives include, among others:

- Interaction Approach;
- Input Processing / Processing Instruction;
- Skill Acquisition Theory;
- Sociocultural Theory;
- usage-based/construction approaches;
- explicit/implicit and intentional/incidental learning research;
- noticing/attention/depth-of-processing accounts;
- form-focused instruction.

These perspectives overlap but also make different predictions about what instruction should do.

The repo has pieces of many of them in downstream RQs but has **never performed a direct foundational comparison**.

### Risk

Without this comparison, `SYN-SYS-001` can accidentally be an attractive blend of compatible-sounding ideas rather than a synthesis that survived competing explanations.

### Required action

Open `RQ-022 — Foundational SLA mechanisms and competing instructional theories`.

## 6. Critical gap 2 — assessment/inference validity is much thinner than the Evidence Engine implies

### Current state

The repository has excellent vocabulary around:

- understood;
- recalled;
- transferred;
- retained;
- support provenance;
- first-seen/changed-context/delayed conditions.

But `R08 Assessment` is primarily represented by `RQ-005` on transfer.

There is no comprehensive research cycle on:

- construct validity;
- reliability/generalizability;
- task-to-construct inference;
- scorer/rater effects;
- classification error;
- diagnostic assessment design;
- formative vs proficiency inference;
- validity consequences of using a score/state for routing.

### Why this matters

Language-assessment research treats validity as an argument about **the interpretation and use of observations**, not as a property obtained by giving a task a sensible name.

A realistic task can still measure the wrong construct. A diagnostic classification can still be unreliable. A speaking task can be contaminated by reading, memory, topic knowledge, planning or scorer error.

### Risk

The current `Evidence Engine` is conceptually careful but could still make unvalidated learner-state inferences with high confidence.

### Required action

Open `RQ-024 — Language-assessment validity and learner-state inference`.

This RQ must test whether the current four cross-cutting evidence labels are adequate product categories, what they may legitimately imply, and how confidence/generalization should work.

## 7. Critical gap 3 — no dedicated target-needs/content-selection foundation

### Current state

`RQ-017` asks how to integrate a curriculum and explicitly admits that the exact first capability set is unknown.

But there is no dedicated research cycle asking:

> What English capabilities and language content are actually highest-value for the target learner?

### Missing evidence families

- general/adult learner needs analysis;
- target-situation analysis;
- task-based needs analysis;
- triangulated learner/expert/real-language evidence;
- corpus-informed language demand;
- frequency/range/dispersion;
- spoken/written register differences;
- formulaic-sequence utility;
- learnability and prerequisite value.

### Why this matters

A pedagogically excellent learning loop can still waste time if it teaches low-value language.

`what to teach` and `how to teach` are separate research questions.

### Required actions

Open:

- `RQ-023 — Target needs and capability selection`;
- `RQ-027 — Corpus-informed beginner language/content selection`.

## 8. Critical gap 4 — individual differences are underrepresented

### Current state

The motivation track (`RQ-018`) focuses mainly on useful return, streaks, recovery and product behavior.

That is valuable but it does not cover the broader instructed-SLA individual-differences domain.

### Missing/under-covered constructs

- language-learning anxiety;
- willingness to communicate;
- self-efficacy;
- autonomous vs controlled motivation;
- self-regulated learning;
- language aptitude;
- working memory / cognitive resources;
- prior literacy/education;
- accessibility/neurodiversity limits.

### Why this matters

Meta-analytic work shows that these variables can relate to achievement, participation, treatment response and persistence, often with meaningful moderators.

A system that claims to adapt instruction should know **which adaptations are evidence-backed** and which are personalization theater.

### Required action

Open `RQ-026 — Individual differences, affect and self-regulated learning`.

## 9. Critical gap 5 — corrective feedback lacks a cross-skill synthesis

### Current state

Feedback appears inside speaking, grammar, writing and AI cycles, but there is no foundational corrective-feedback track.

### Missing comparisons

- explicit correction vs recast;
- prompts/self-repair;
- metalinguistic feedback;
- oral vs written feedback;
- focused vs unfocused feedback;
- immediate vs delayed timing;
- feedback intensity;
- proficiency, aptitude, feature and task moderators;
- learning vs same-task correction.

### Why this matters

Corrective feedback is one of the largest evidence domains in instructed SLA and directly affects almost every interactive learning task Nếp might build.

### Required action

Open `RQ-025 — Corrective feedback and self-repair policy`.

## 10. Critical gap 6 — explicit/implicit and intentional/incidental learning were never synthesized at method level

The current repo pragmatically uses both explicit and implicit mechanisms, but it has not yet answered:

- what explicit instruction is especially good at;
- what outcome measures may favor explicit instruction;
- what implicit/incidental learning can reasonably accomplish under limited exposure;
- when explicit knowledge can support later proceduralized performance;
- when explanation creates knowledge about English rather than usable English;
- how deliberate vocabulary/chunk learning should interact with incidental exposure.

This belongs inside `RQ-022` rather than being resolved implicitly by product design.

## 11. Critical gap 7 — research-quality grading is too compressed

### Current state

Claims use an `A–E` evidence label.

The scheme is helpful but currently mixes several different questions:

- Was the study/methodology strong?
- Is the evidence directly about the target learner?
- Is the outcome construct the same one Nếp cares about?
- Is the finding replicated/consistent?
- Does a classroom/lab result transfer to a self-study product?

### Example problem

A high-quality meta-analysis can be methodologically strong while having low directness to Vietnamese adults near A0.

Calling that simply `A` can encourage later agents to overread confidence.

### Required action

Open `RQ-028 — Evidence grading, contradiction and update protocol` as a methodology RQ.

Future claims should retain compact confidence but add separate axes such as:

```text
methodological_quality
population_directness
construct_directness
replication_consistency
product_transfer_directness
```

## 12. Critical gap 8 — contradictions are not first-class data

The evidence matrix often records accepted/rejected universal claims, which is useful.

However there is no systematic registry for:

```text
position A
vs
position B

supporting evidence
measurement differences
moderators
current synthesis
```

This matters because several apparent contradictions in SLA disappear when outcome measure, proficiency, target form or instructional context is considered.

Required controversy syntheses include:

1. input/comprehension emphasis vs output/practice emphasis;
2. explicit vs implicit instruction;
3. focus on form vs focus on forms;
4. Processing Instruction vs production-based instruction;
5. explicit feedback vs recasts;
6. TBLT vs task-supported/structured instruction;
7. chunk/formulaic learning vs early grammatical abstraction;
8. authentic vs graded input;
9. L1 support vs L2-only;
10. repetition/stabilization vs contextual variability;
11. independent psychometric assessment vs mediated/dynamic assessment.

`RQ-028` should define how the knowledge base represents this disagreement.

## 13. Critical gap 9 — experiments exist only as plans

The repository contains `EXP-001` through `EXP-021`, but there is not yet a corresponding result layer showing target learners actually ran those experiments.

Therefore statements such as:

```text
feature is research-backed candidate
```

must not become:

```text
Nếp has proven the feature works
```

The experiment designs are assets. They are **unexecuted hypotheses** until learner data exists.

## 14. Critical gap 10 — the integrated product synthesis is premature as an implementation authority

`SYN-SYS-001` is internally coherent and should not be deleted.

But after this audit its correct status is:

```text
provisional pre-meta-foundation integration hypothesis
```

not:

```text
final Nếp Method / build authority
```

Likewise, the Nếp v1 product handoff documents should be retained as design history/hypotheses while the meta-foundation RQs remain open.

## 15. Coverage scorecard

This scorecard measures **research-program maturity**, not scientific truth or product efficacy.

| Domain | Current maturity | Audit judgment |
| --- | --- | --- |
| Research governance / provenance | strong | preserve |
| Vocabulary knowledge/evidence | strong | method evidence good; content-selection gap remains |
| Listening diagnostics | strong-moderate | good local coverage |
| Retrieval/spacing | strong | keep; exact scheduler still empirical |
| Transfer framing | strong conceptually | assessment validation still required |
| Speaking progression | moderate-strong | local evidence good; broader theory/assessment links pending |
| Pronunciation/intelligibility | strong-moderate | Vietnamese directness still limited |
| ASR/AI reliability | strong as guardrail | technology policy, not efficacy evidence |
| Video/caption/pause | moderate | useful but lower priority than foundation gaps |
| Grammar/constructions | moderate-strong | needs explicit theory comparison in RQ-022 |
| Reading | moderate | skill track exists but foundations should deepen |
| Writing | moderate | skill track exists; feedback/generalization needs RQ-025/024 |
| Interaction/pragmatics | moderate-strong | good local synthesis; foundational interaction theory still fragmented |
| Fluency/automaticity | moderate-strong | transfer criterion is good; theoretical integration pending |
| Curriculum sequencing | moderate | **premature because needs/content foundation missing** |
| Product motivation/recovery | moderate | does not replace L2 affect/ID research |
| Vietnamese calibration | moderate | right epistemic shape; more target data needed |
| Placement | moderate | routing concept good; psychometric validity pending |
| Foundational SLA theories | **weak / seeded** | critical gap |
| Needs analysis / target capabilities | **weak / missing** | critical gap |
| Assessment validity/reliability | **weak** | critical gap |
| Individual differences / affect / SRL | **weak** | critical gap |
| Corrective feedback as general domain | **weak** | critical gap |
| Corpus-informed content selection | **weak-moderate** | critical gap |
| Research contradiction/update methodology | **weak / missing** | critical gap |
| Target-learner efficacy results | **none yet** | cannot claim efficacy |

## 16. New research sequence

Do not expand product features before this sequence is closed enough to support a method synthesis.

### P12 — Meta-foundation gate

#### RQ-022 — Foundational SLA mechanisms and competing instructional theories

**Question:** Which learning mechanisms and instructional theories have the strongest converging evidence for adult instructed L2 development, which predictions conflict, and what does each imply for a near-A0 self-study system?

Must cover at minimum:

- input/comprehension;
- interaction;
- output;
- noticing/attention/depth of processing;
- explicit/implicit;
- intentional/incidental;
- Input Processing / Processing Instruction;
- Skill Acquisition Theory;
- usage-based/construction learning;
- Sociocultural Theory;
- form-focused instruction.

#### RQ-023 — Target needs and capability selection

**Question:** What real-world English tasks/capabilities are most valuable for the target population, and how should learner needs, target-situation evidence and general-English goals define the first curriculum?

#### RQ-024 — Assessment validity and learner-state inference

**Question:** What observations under which task/scorer/support conditions justify what learner-state inference, with what uncertainty and generalizability?

#### RQ-025 — Corrective feedback and self-repair

**Question:** Which feedback type, explicitness, timing, focus and repair opportunity best serve which construct, learner, feature and task?

#### RQ-026 — Individual differences, affect and SRL

**Question:** Which learner differences meaningfully moderate instruction or participation, and which adaptations are justified for a self-study system?

#### RQ-027 — Corpus-informed beginner content selection

**Question:** Which words, chunks, constructions and pragmatic routines should be prioritized using target needs plus frequency/range/dispersion/coverage/learnability/formulaicity evidence?

#### RQ-028 — Evidence grading, contradiction and update protocol

**Question:** How should Nếp grade methodological quality/directness/consistency, represent contradictory evidence, and revise prior syntheses when stronger/newer evidence appears?

### P13 — Method synthesis gate

Only after P12:

#### SYN-METHOD-001 — Nếp Method v0

This synthesis should contain only:

1. target learner and target-use definition;
2. learning goals / constructs;
3. minimum set of supported learning conditions;
4. conditions/moderators where method changes;
5. content-selection rules;
6. assessment/inference rules;
7. what is optional/uncertain;
8. explicit rejected methods/claims;
9. falsification conditions;
10. target-learner validation plan.

No product UI, database, app route or engineering architecture belongs in the core method itself.

## 17. Candidate convergence already visible — not yet the final method

Across the existing repo plus the field-mapping scan, several themes appear repeatedly enough to remain high-priority candidates:

```text
meaningful/comprehensible input
+ attention to useful language form
+ actual retrieval/production when production is the goal
+ interaction/contingency when interaction is the goal
+ corrective feedback/self-repair appropriate to task
+ spaced revisiting
+ increasing contextual/task variation
+ substantial exposure to high-value language
+ fluency practice on sufficiently known material
+ diagnostic evidence that changes the next instruction
```

But this is intentionally **not** labeled Nếp Method yet.

The meta-foundation work must determine:

- relative emphasis;
- ordering;
- dosage;
- beginner exceptions;
- outcome-specific differences;
- learner moderators;
- which parts are mechanisms versus curriculum heuristics.

## 18. What should stop now

Until P12 is complete enough:

- do not add more A1/A2 course units because a grammar/profile gap exists;
- do not build another learning engine simply because a skill has no feature;
- do not treat `SYN-SYS-001` as implementation authority;
- do not claim Nếp has a scientifically optimized method;
- do not use the legacy Vidlish application as evidence for pedagogy;
- do not turn an `EXP-*` design into a product rule before results exist.

## 19. What can continue safely

- source verification;
- meta-foundation RQs;
- evidence-quality/contradiction infrastructure;
- target-needs research;
- corpus/usage analysis;
- construct/assessment validation design;
- small research prototypes used only to test an explicit hypothesis;
- recruitment/planning for target-learner validation.

## 20. Decision

The research program is **not discarded**. Most RQ-001–RQ-021 artifacts remain useful.

The decision is to change their role:

```text
before META-001:
RQ modules → integrated product → build

after META-001:
RQ modules
+ missing meta-foundations
+ contradiction/validity audit
→ Nếp Method
→ curriculum specification
→ product specification
→ new implementation
```

This reset is necessary precisely because the project is AI-assisted: the research system must prevent a plausible, internally consistent AI synthesis from becoming pedagogy merely because it is well written.