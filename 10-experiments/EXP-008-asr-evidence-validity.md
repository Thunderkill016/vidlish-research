---
id: EXP-008
title: Validate automated speech evidence for Vietnamese near-A0 learners
status: proposed
research_question: RQ-008
---

# EXP-008 — Which machine speech signals are safe enough to use?

## Question

For Vietnamese-speaking adults near A0 / early A1, which ASR or pronunciation signals predict human-relevant pronunciation outcomes well enough to support feedback, and which are too noisy or biased to use beyond observation?

## Primary hypotheses

1. Raw transcript correctness/WER will not be a sufficiently calibrated pronunciation-quality measure.
2. Human-machine agreement will vary by task and learner.
3. Vietnamese speaker subgroups will show different error profiles across systems.
4. Feature-specific detectors can be useful for narrowly defined targets if calibrated on Vietnamese learner data.
5. Machine feedback should improve delayed first-seen human listener outcomes to justify its product complexity.

## Participants

Target initial calibration sample:

- Vietnamese L1 adults;
- near-A0 / early A1 operational boundary pre-registered;
- record Northern/Central/Southern variety where self-reported;
- record speaking/English learning history;
- recruit enough speakers to estimate between-speaker variation rather than treating utterances as independent people.

Do not use accent strength as an exclusion criterion.

## Speech task matrix

Each participant contributes multiple task families:

```text
A. isolated known word
B. known chunk / short read sentence
C. bounded guided production with hidden model
D. changed-context first-seen production
E. short semi-spontaneous response when level permits
```

Include both clean and realistic phone-recording conditions. Do not make noisy audio a pronunciation error.

## Candidate target families

Draw from `FEAT-PRN-001`, especially:

```text
word-final consonant presence
word-final clusters
morphological /s,z/
learner-specific high-value consonant contrasts
learner-specific vowel contrasts
lexical stress + vowel realization
simple focus/timing
```

Not every learner needs every target.

## Human criterion data

Use at least two distinct labels where feasible.

### Objective intelligibility

- orthographic word/chunk transcription;
- intended message/picture selection;
- minimal contrast identification.

### Feature annotation

Trained raters label only pre-specified features, for example:

```text
final /s,z/ present enough to preserve target?
contrast A/B maintained?
primary stress realization acceptable for word recognition?
```

### Comprehensibility

A separate listener-effort rating where task length supports it.

Never collapse these into one gold score.

## Machine systems

Benchmark at least:

- one current high-capability general ASR model;
- one second independent ASR provider/model if budget permits;
- any dedicated pronunciation API considered for production;
- Nếp feature-specific detector prototypes.

Freeze and log exact versions/configurations for the experiment.

## Machine outputs to retain

```text
transcript
WER/MER/alignment
confidence/token probability if available
n-best alternatives if available
feature detector scores
forced-alignment output if used
latency/cost
failure/empty transcript
```

## Analyses

### A. Human-ASR intelligibility agreement

For each system/task/speaker:

```text
ASR target recovery
vs
human target recovery
```

Report calibration and within-speaker variation, not just one global correlation.

### B. Pronunciation-quality proxy validity

Test whether:

```text
WER/MER
confidence
transcript distance
vendor pronunciation score
```

predict human intelligibility, comprehensibility and feature labels separately.

### C. Feature detector validity

For each target family calculate:

```text
precision
recall
false-positive rate
false-negative rate
calibration
```

False correction rate is especially important because unnecessary pronunciation correction can redirect learner behavior.

### D. Subgroup robustness

Estimate errors by:

```text
Vietnamese regional variety
proficiency band
task family
speech style
audio condition
```

Explore other variables only when sample size supports interpretation.

### E. Generalization

Train/calibrate on one set of lexical items and speakers; test on first-seen items and held-out speakers.

A detector that memorizes prompts is not valid pronunciation evidence.

## Product-use tiers to calibrate

Do not pre-commit exact thresholds. Determine whether each signal qualifies for:

```text
Tier 0  raw logging only
Tier 1  learner-facing neutral transcript / retry
Tier 2  candidate diagnostic trigger
Tier 3  bounded feature-specific corrective feedback
Tier 4  supporting learner evidence
```

`Tier 4` still must not become sole mastery evidence.

## Learning-value arm

Validity alone is not enough. Randomize or counterbalance:

```text
A. record + listen/compare
B. ASR transcript feedback
C. validated feature-specific feedback
```

Then test delayed, first-seen human listener understanding.

Primary product metric:

```text
delayed first-seen listener-understanding gain
───────────────────────────────────────────
learner time + correction count + system cost
```

## Safety / fairness rule

If a system produces systematically higher false-correction rates for a Vietnamese subgroup, Nếp must narrow or disable the affected automated judgment until recalibrated.

## Success criteria

Before shipping consequential automated correction, evidence must show:

- the construct is clearly defined;
- feature/task/population scope is explicit;
- human criterion agreement is practically useful;
- false corrective feedback is sufficiently rare for the intended interaction;
- held-out speakers/items retain performance;
- subgroup behavior is characterized;
- delayed learner outcomes beat a simpler feedback baseline.

Exact numerical cutoffs are pre-registered during experiment design, not invented after seeing results.

## Failure interpretation

A failed detector does not mean pronunciation technology is useless. It means the product should fall back to lower-evidence uses such as recording, replay, comparison, neutral transcript assistance or human review.
