---
id: EXP-009
title: Validate authentic-video readiness gating
status: proposed
research_question: RQ-009
---

# EXP-009 — Can a learner × clip gate predict useful authentic-video learning?

## Question

Can Nếp predict which first-seen authentic video windows Vietnamese near-A0 / early-A1 learners can understand and learn from using clip-specific lexical, speech and visual features plus learner evidence better than simple global vocabulary-size or CEFR rules?

## Core hypotheses

1. Learner-specific **aural lexical coverage** predicts audio-based comprehension better than global vocabulary-size level alone.
2. Adding speech-load and visual-grounding features improves prediction beyond lexical coverage alone.
3. A gate using clip windows produces more successful audio-led attempts per minute than a rule that unlocks whole videos by global level.
4. Content comprehension with strong imagery/captions will overestimate independent listening readiness unless audio-based probes are separated.

## Participants

Initial product-validation population:

- Vietnamese L1 adults;
- operational near-A0 through early A1 range defined before recruitment;
- record region, age, English-learning history and device/audio conditions;
- do not exclude learners because authentic video is currently difficult.

## Materials

Create a bank of short authentic windows sampled from several source families:

```text
single-speaker everyday explanation
two-person everyday dialogue
café / shopping / transport interaction
simple demonstration / how-to
vlog / talking head
short documentary
simple interview
```

Avoid using copyright-restricted source text as research artifacts beyond metadata/derived features.

Each window should have validated transcript and annotations for:

```text
lexical profile
critical content words
speech rate
speaker count
turn density
overlap/noise
connected-speech risk
visual grounding
topic tags
```

## Learner baseline

Measure:

```text
text vocabulary evidence
aural word/chunk recognition
aural form-meaning access
short listening comprehension
support history
```

Use the same evidence model as RQ-001/RQ-003 rather than a standalone vocabulary-size test only.

## Readiness models to compare

### A — global vocabulary-size gate

Example baseline:

```text
below threshold → locked
above threshold → available
```

Pre-register the threshold; do not tune it after outcomes are seen.

### B — clip lexical-coverage gate

Uses only learner × clip estimated aural lexical coverage.

### C — multimodal readiness gate

Uses:

```text
aural lexical coverage
critical unknowns
speech rate
speaker/turn complexity
noise/overlap
visual grounding
topic familiarity proxy
```

### D — evidence-adaptive gate

Model C plus learner's prior first-seen video/listening outcomes.

This tests whether personalization after real attempts adds meaningful value.

## Attempt protocol

For each sampled window:

```text
first attempt
video/audio available
no answer-bearing caption
        ↓
probe 1: gist/message
probe 2: audio-dependent detail
probe 3: optional visual-dependent item
        ↓
record confidence / effort
        ↓
then allow scaffold
        ↓
English caption or bounded Vietnamese support
        ↓
replay
```

Do not allow support to rewrite the first-attempt evidence.

## Primary outcome

Prediction of **first-seen audio-based comprehension** at the individual learner × window level.

Candidate metrics:

```text
AUROC / AUPRC for success classification
Brier score / calibration error
false-ready rate
false-locked rate
```

For product safety, false-ready matters: repeatedly serving hopeless clips wastes time and trains subtitle dependence.

But false-locked also matters because over-conservative gating can prevent useful authentic exposure.

## Learning-efficiency outcome

After matched training, test unseen parallel windows.

Primary efficiency metric:

```text
delayed first-seen audio comprehension gain
───────────────────────────────────────
authentic-video learning minutes
```

Secondary:

```text
new-word/chunk retention
caption-support reduction
replay demand
subjective effort
completion
```

Completion is not a learning outcome.

## Threshold calibration

Do not begin by declaring 80/90/95/98% correct.

Instead pre-register candidate bands informed by the literature and estimate for the target population:

- probability of first-attempt gist success;
- probability of audio-detail success;
- support needed;
- delayed transfer.

The result may be different thresholds for:

```text
V1 scaffolded exposure
V2 audio-led learning
V3 independent authentic windows
```

## Ablations

To determine what is worth engineering, compare model performance with features removed:

```text
- visual grounding
- speech rate
- critical unknown weighting
- topic familiarity
- prior learner video evidence
```

If a feature does not improve held-out prediction enough to justify complexity, remove it.

## Generalization tests

Hold out:

```text
learners
source creators
speakers
topics
genres
```

A readiness model that only memorizes one channel/creator is not useful.

## Falsification

`FEAT-VID-002` needs revision if:

- clip-specific gating does not beat simple global-level gating;
- lexical coverage alone performs as well as the multimodal model;
- visual-grounding ratings do not generalize;
- false-ready rates remain high for Vietnamese near-A0;
- learner adaptation adds no held-out predictive value;
- supported clips do not produce better delayed audio transfer per minute.
