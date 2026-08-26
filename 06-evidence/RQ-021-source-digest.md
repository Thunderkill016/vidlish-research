# RQ-021 source digest — cold-start placement and learner-model bootstrap

**Evidence ID:** `EVD-RQ-021`  
**Question:** How should Nếp place a new learner quickly enough to start learning, while keeping the decision valid for Vietnamese adults near A0/A1?

## Scope

This pass retained 12 sources spanning:

- English/language placement validity;
- computerized adaptive and multistage testing;
- classification accuracy and cut-score uncertainty;
- self-assessment for placement;
- formative/diagnostic placement;
- adaptive-test learner experience;
- embedded/stealth assessment.

The strongest direct evidence concerns institutional placement and adaptive testing. Evidence for true near-A0 Vietnamese adults in mobile self-study onboarding remains thin, so exact timings and thresholds remain product experiments.

## Retained evidence

| Source | Population / method | High-signal result | Product limitation |
| --- | --- | --- | --- |
| `SRC-0223` | English CAT; 3,224 calibration + 7,254 operational administrations | adaptive estimates can be reliable/valid; reasonable precision required more than 15 items in that system; low-end precision suffered when the bank lacked informative items | old system; personnel/University contexts; not Nếp thresholds |
| `SRC-0224` | ACTFL APPT listening placement validation | adaptive placement can efficiently establish a floor/ceiling and correlate with other placement evidence | university Spanish; listening only in the validation study |
| `SRC-0225` | real-data simulation on English reading classification | CAT can improve classification, but multiple simultaneous cut points reduce classification performance; content coverage remains a validity concern | reading subtest; not a complete learner model |
| `SRC-0226` | systematic review/meta-analysis of CAT motivation/anxiety | CAT is not automatically more motivating or less anxiety-inducing; easier adaptive variants showed some psychological benefit | not language-specific overall |
| `SRC-0227` | 92 intensive-English learners; ACTFL can-do self-assessment vs placement performance | self-assessment was internally coherent but only moderately related to productive placement scores; not sufficient as sole placement evidence | productive skills and IEP context |
| `SRC-0228` | multilingual SELF placement/diagnostic system | semi-adaptive placement can report uneven skill profiles and be extended into diagnostic feedback | institutional system; broader/longer than mobile onboarding |
| `SRC-0229` | local English/French placement redesign with objective + self-directed elements | placement should support a local learning progression; self-directed judgments need concrete task information and triangulation | pilot context; not near-A0 mobile learning |
| `SRC-0230` | methodological/empirical stealth-assessment work | embedded evidence requires explicit competency, evidence and task models; logs alone are not valid assessment | broad education technology, not English placement |
| `SRC-0231` | L2 Chinese reading stealth assessment | embedded learner interactions can support validated proficiency estimates when designed around explicit evidence models | children, Chinese reading, not adult English |
| `SRC-0232` | 286 participants, adaptive vs fixed test | adaptive testing improved precision; learner experience did not automatically improve; starting easier/explaining adaptivity may help | non-language fluid-reasoning test |
| `SRC-0233` | multidimensional English CAT post-hoc simulation | MCAT can reduce test length substantially while preserving precision; stopping rule and content balancing matter | simulation based on an English proficiency item pool |
| `SRC-0234` | 2,201 learners, web-based language placement validation | reliability alone is insufficient; placement-use validity should include whether the resulting decisions are appropriate | Spanish university placement, 100-item fixed test |

## Convergence

### 1. Placement is a decision problem, not a label problem

A placement result is useful when it selects a suitable next learning context. The relevant question for Nếp is therefore:

```text
What should this learner encounter next?
```

not:

```text
What single CEFR label can we assign as early as possible?
```

This matters because Nếp does not need certification precision at cold start. It needs to avoid wasting time on already-known material while also avoiding a starting point so hard that the learner cannot understand or retrieve anything.

### 2. Adaptive does not mean “three questions = truth”

Adaptive methods can reduce wasted items, but evidence repeatedly shows that precision depends on:

- the quality and range of the item bank;
- the initial estimate/prior;
- item selection;
- construct/content balancing;
- stopping rules;
- the number and location of decision boundaries.

A very short test can be useful for coarse routing. That is not the same as a validated comprehensive proficiency estimate.

### 3. Near-A0 needs its own low-end item bank

`SRC-0223` is especially important: precision deteriorated at the lowest ability range partly because the bank lacked informative items there.

For Nếp this means a generic A1–C1 placement bank is structurally wrong for the target population. The system needs tasks that distinguish among states such as:

```text
no usable English evidence yet
recognizes a few written words
recognizes familiar spoken words
understands simple chunks with context
can retrieve a small amount without support
can produce a basic controlled response
```

### 4. Multiple dimensions should not be collapsed prematurely

Language profiles can be uneven. A learner might recognize written vocabulary but fail to recover the same targets from speech, or understand a phrase but be unable to retrieve it.

A single overall score can therefore hide the exact information Nếp needs to choose the next task.

### 5. Self-assessment is useful context, not ground truth

Self-report can be cheap and learner-friendly. It can help set a prior and capture history/goals. But direct studies show that even a well-designed can-do instrument is not a safe substitute for actual productive performance.

So:

```text
“I think I am A2”
```

may alter what Nếp probes first, but must never make Nếp skip direct evidence.

### 6. Placement should keep learning after the test

Embedded-assessment research provides a stronger product pattern than a one-shot entrance exam:

```text
short cold-start bootstrap
→ begin real learning
→ collect validated task evidence
→ update learner profile quickly
→ repair any bad initial placement
```

This is not “secret scoring.” The learner can be told plainly that Nếp is continually adjusting difficulty based on what they demonstrate.

## What is rejected

- “Three adaptive questions can accurately tell Nếp the learner’s English level.” — rejected as a general scientific claim.
- “Self-declared CEFR is enough for placement.” — rejected.
- “One grammar/vocabulary score can stand in for speaking/listening/writing.” — rejected.
- “A reliable test is automatically a valid placement system.” — rejected.
- “Adaptive testing is automatically more pleasant for learners.” — rejected.
- “Every learner must complete all four skills before receiving any learning value.” — rejected as a product rule.
- “Initial placement proves mastery.” — rejected.
- “Clicks, latency or completion can be interpreted as language ability without an evidence model.” — rejected.

## Evidence gap that matters most

No retained study directly answers the Nếp target condition:

> Vietnamese-speaking adults at true A0/low A1, on mobile, completing a very short cold-start sequence whose success is judged by downstream learning efficiency rather than certificate-level classification accuracy.

Therefore `EXP-021` must validate the **decision consequences** of the onboarding system, not merely correlation with a longer test.
