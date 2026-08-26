---
id: EXP-017
title: Capability-centered integrated curriculum sequencing
status: proposed
research_question: RQ-017
---

# EXP-017 — Capability-centered integrated curriculum sequencing

## Primary question

Which curriculum assembly policy produces the best **delayed changed-context capability gain per learning minute** for Vietnamese-speaking Nếp learners near A0/A1 while preserving diagnostic clarity and avoiding unnecessary overload?

## Why this experiment exists

A curriculum can appear comprehensive while failing to produce usable English.

Possible failure modes:
- isolated skill silos do not transfer into real use;
- all-skills lessons overload beginners;
- integrated tasks hide which component actually failed;
- support creates task success but no independent ability;
- fixed sequences waste time on already-known prerequisites;
- adaptive systems become so complex that they outperform nothing simpler.

`EXP-017` tests the orchestrator rather than assuming integration itself is beneficial.

## Population

Vietnamese-speaking adults near A0/A1.

Capture baseline evidence for:
- high-frequency vocabulary/chunks;
- basic construction knowledge;
- listening comprehension/perception;
- guided speaking;
- basic reading/writing where available;
- support dependence;
- changed-context transfer;
- delayed review history.

Do not require complete evidence in all modalities before enrollment; sparse state is part of the real product problem.

## Capability set

Use a small practical initial bank, for example:
- state name/basic identity;
- say where one lives/is from;
- request one familiar item;
- answer a simple either/or choice;
- understand and state a simple price/number;
- say a simple preference;
- ask for repetition;
- signal non-understanding;
- send one short practical message.

The final capability order is itself experimental.

## Curriculum policies

### A — All-skills lesson template benchmark

Every selected capability is taught through a fixed template containing most major modes/components in one session.

Example:

```text
vocabulary
→ listening
→ grammar
→ pronunciation
→ speaking
→ reading
→ writing
→ quiz
```

Purpose:
- benchmark the common intuition that comprehensiveness means including everything every time.

Risk predicted by RQ-017:
- unnecessary load;
- weak diagnostics;
- low-value modality work.

### B — Skill-silo benchmark

Learners progress through largely separate skill blocks.

Example:

```text
listening block
speaking block
reading block
writing block
```

Content can share vocabulary, but sequencing is driven mainly by skill rather than a common capability.

Purpose:
- test whether integration actually adds learning value beyond organized single-skill practice.

### C — Capability-centered primary-bottleneck policy

```text
choose useful capability
→ inspect prerequisites
→ choose one primary bottleneck
→ assemble smallest meaningful task
→ use bounded support
→ changed-context probe
→ persist component evidence
```

Only supporting modalities needed for the current bottleneck are included.

### D — Capability-centered adaptive spiral policy

Condition C plus:
- rolling Four-Strands audit;
- modality-starvation monitoring;
- repeated capability encounters across different modes;
- adaptive complexity increments;
- delayed continuation in another modality where useful;
- evidence-based capability merging.

This is the fullest version of `FEAT-CUR-001`.

## Optional embedded factorials

Where sample size permits, independently test selected policy choices rather than bundling everything into C/D.

### Task-first vs model-first

Task-first:

```text
bounded attempt
→ diagnose
→ targeted learning
→ retry
```

Model-first:

```text
processable model/input
→ target work
→ attempt
```

Hypothesis:
- task-first may provide better diagnosis when prerequisites are mostly known;
- model-first may reduce unproductive failure for truly novel near-A0 targets.

Do not assume one universal winner.

### Fixed vs readiness-adaptive complexity

Fixed:
- predetermined simple-to-complex sequence.

Adaptive:
- next complexity dimension chosen from learner evidence.

### Fixed vs rolling strand balance

Fixed:
- approximate planned proportions over curriculum.

Rolling:
- detect underrepresented strands/modalities and select suitable ready capabilities to rebalance.

## Shared content controls

Across policies, match as closely as possible:
- target capability set;
- high-frequency language inventory;
- total learning time;
- access to audio/text assets;
- review opportunities;
- device conditions.

Differences should come from assembly/sequencing, not one group simply receiving more English.

## Capability transfer assessment

Training example:

```text
Order water in café A.
```

Changed-content probe:

```text
Order tea in café A.
```

Changed-context probe:

```text
Ask for a charger at a service desk.
```

Higher transfer probe:

```text
Use the same request function with a new partner/prompt realization.
```

Novel content must remain within prerequisite fairness; transfer should not secretly test unknown vocabulary.

## Delayed assessment

At one or more delayed points:
- no exact training item;
- reduced/no scaffold on first attempt;
- changed surface wording;
- changed lexical content within readiness;
- changed voice/partner where relevant;
- same underlying capability.

Store both capability success and component evidence.

## Primary outcome

```text
delayed changed-context capability gain
──────────────────────────────────────
learning minutes
```

Capability gain requires task success plus the modality-specific quality criteria defined by the underlying engine.

## Secondary learning outcomes

- unsupported first-attempt success;
- delayed retention;
- changed-content transfer;
- changed-modality transfer where intended;
- support reduction;
- time to first independent capability evidence;
- prerequisite violations;
- component mastery/transfer evidence;
- fluency only where the target was already ready for fluency practice.

## Diagnostic-quality outcome

For failed integrated tasks, compare the orchestrator's inferred bottleneck with subsequent targeted probes.

Example:

```text
system predicts: listening perception failure
```

Then targeted diagnostic may reveal:
- sound form not recognized;
- word meaning unknown;
- interaction question misunderstood;
- learner understood but could not produce response.

Measure:

```text
bottleneck prediction precision/recall
```

A coherent integrated UX is not enough if the system diagnoses failure incorrectly.

## Overload outcome

Operationalize overload behaviorally rather than relying only on self-report.

Candidate signals:
- multiple simultaneous unknown targets;
- abrupt failure across otherwise-known components;
- large support escalation;
- abandonment;
- unusually long latency without useful progress;
- post-task report of excessive difficulty;
- quality collapse after multiple complexity dimensions increase together.

Use self-reported effort/frustration as secondary evidence.

## Skill/modality starvation

For each learner and rolling window track:
- listening meaningful opportunities;
- speaking opportunities;
- reading opportunities;
- writing opportunities;
- interaction opportunities;
- Four-Strands minutes/opportunities.

Flag starvation only when:
- a mode has been absent for a meaningful horizon;
- the learner has ready capabilities that could productively use it.

Do not force a modality merely to satisfy a quota.

## Complexity increment test

Compare gains after changes such as:
- one new lexical item;
- reduced support;
- one extra proposition;
- one extra turn;
- changed voice;
- changed context;
- longer input;
- combined dimensions.

Estimate which increments produce:

```text
useful challenge
without
quality collapse
```

The product should learn empirical transition probabilities rather than use one global difficulty ladder forever.

## Planning/scaffold dose

Record:
- scenario preview;
- model viewed/heard;
- planning seconds;
- word-bank use;
- sentence-frame use;
- Vietnamese support;
- rehearsal count;
- replay/transcript use;
- partner rescue.

Compare later unsupported performance conditional on prior support.

The best support is not the support that maximizes immediate completion; it is the one that improves later independent use per minute.

## Spiral benefit test

For capabilities encountered across several modes, compare:

```text
same total practice concentrated in one modality
```

versus:

```text
practice revisited across relevant modalities/contexts
```

Primary criterion remains later capability transfer, not exposure count.

## Capability merge test

Before a combined scenario, estimate independent evidence for component capabilities.

Example:

```text
request item
+ understand size choice
+ ask for repetition
```

Combined café transaction succeeds/fails.

Analyze whether merge readiness predicted integrated performance.

If not, revise prerequisite graph or interaction complexity model.

## Curriculum balance audit

For each policy report rolling distributions of:
- meaning-focused input;
- meaning-focused output;
- language-focused learning;
- fluency development.

Do not score policies better merely for being closer to 25% each.

Instead ask whether balance predicts:
- delayed capability gains;
- fewer modality gaps;
- better transfer;
- reasonable learning cost.

## Learner choice sub-study

When multiple equally ready capabilities exist:
- system-selected scenario;
- learner-selected scenario from safe candidates.

Compare:
- learning gain;
- completion;
- voluntary return;
- transfer;
- whether chosen topics cause systematic curriculum gaps.

Engagement can influence selection but cannot override learning outcomes.

## AI content controls

If AI generates task variants:
- keep target capability and prerequisite constraints fixed;
- log model/version/prompt policy where operationally available;
- validate target language against curriculum schema;
- reject variants with undeclared lexical/construction novelty;
- do not let AI decide mastery.

## Analysis by learner state

Test moderators such as:
- true A0 vs emerging A1;
- stronger listening vs stronger reading profile;
- high vs low support dependence;
- high vs low prior vocabulary coverage;
- learner who prefers/avoids production;
- device/input constraints.

A policy can be adaptive by subgroup rather than globally best.

## Cost outcome

Track:
- authoring/generation complexity;
- computation/API cost if relevant;
- learner minutes;
- number of diagnostic probes;
- content rejection rate;
- orchestration latency.

If D produces negligible learning improvement over C but much higher system cost, prefer C.

## Falsification criteria

`FEAT-CUR-001` is weakened or simplified if:
- capability-centered policies do not beat a simpler skill-silo or fixed curriculum on delayed changed-context capability gain per minute;
- all-skills lessons do not actually create measurable overload or learning inefficiency;
- the one-primary-bottleneck heuristic frequently misses the true cause of failure;
- support provenance fails to predict later independent ability;
- rolling Four-Strands balancing adds low-value activities with no transfer benefit;
- simple-to-complex progression is worse than adaptive/non-monotonic sequencing for meaningful learner groups;
- spiral cross-modal revisiting adds time without improving relevant transfer;
- prerequisite graphs predict integrated-task success poorly;
- learner choice improves engagement but harms learning or creates persistent coverage gaps;
- task-first/model-first effects do not justify adaptive routing;
- a much simpler fixed sequence achieves equivalent delayed learning at lower product complexity.

## Adoption rule

Adopt the **simplest** curriculum assembly policy that reliably improves delayed changed-context capability performance per learning minute while keeping diagnostic error, support dependence and overload within acceptable bounds.

Comprehensive coverage is a constraint on curriculum health, not a reason to sacrifice learning efficiency or evidence quality.
