---
id: EXP-007
title: Validate intelligibility-first pronunciation priorities
status: proposed
research_question: RQ-007
---

# EXP-007 — Does intelligibility-first target selection beat generic pronunciation practice?

## Question

For Vietnamese-speaking adults near A0, does a pronunciation curriculum selected by **learner-specific communication risk** improve delayed human listener understanding of first-seen utterances more per practice minute than a generic broad/native-model pronunciation sequence?

## Core hypothesis

A learner should spend scarce pronunciation time on features that repeatedly threaten word/message identity, not on every nonnative feature.

## Participants

Initial target population:

- Vietnamese L1 adults;
- near-A0 / early A1 operational inclusion boundary defined before recruitment;
- record Vietnamese regional variety and learning history;
- stratify or at least report Northern/Central/Southern representation;
- exclude no learner merely because they have a strong accent.

## Baseline diagnostics

Before treatment, sample short controlled and bounded communicative speech containing candidate families:

```text
word-final consonant presence
word-final clusters
morphological /s,z/
high-value consonant contrasts
high-value vowel contrasts
multisyllabic word stress + vowel realization
simple sentence focus/timing
```

Do not assume each learner needs each target.

A human-validated diagnostic panel should label:

- intended word/message;
- whether listeners identified it;
- candidate pronunciation feature(s) implicated in failure;
- listener background;
- task/support provenance.

## Treatment conditions

Use either randomized target families within learner or a cluster/crossover design that avoids obvious contamination.

### A — generic broad pronunciation sequence

Equal-duration practice drawn from a conventional pronunciation inventory without learner-specific communicative-risk prioritization.

Possible content mix:

```text
segment drills
minimal pairs
word stress
intonation
```

Keep instruction competent; the comparison should not be a deliberately weak control.

### B — intelligibility-priority sequence

Select only targets where the ranker has evidence:

```text
Vietnamese prior
× learner observed risk
× functional / information value
× curriculum relevance
```

Typical early candidates may include coda/cluster preservation, morphology-bearing `/s,z/`, learner-specific high-value contrasts, or stress-vowel errors that caused lexical confusion.

### Optional C — learner-specific but accent-accuracy optimized

If sample size permits, compare communication-risk ranking against a learner-specific ranking that targets the largest acoustic/native-model deviation regardless of communication cost.

This isolates the value of **intelligibility-first** rather than personalization alone.

## Practice sequence

Within each target family:

```text
perception/contrast check if needed
→ bounded production
→ model hidden
→ short utterance
→ changed-context utterance
→ delayed recheck
```

Use `FEAT-SPK-001` and `FEAT-TRN-001` provenance rules.

## Primary delayed criterion

After a pre-registered delay, collect **first-seen** utterances that contain the same capability but different lexical/situational exemplars.

Human listeners complete objective understanding tasks where feasible:

- orthographic word/phrase transcription;
- picture/message selection;
- forced-choice intended meaning when free transcription would add spelling confounds;
- short communicative follow-up showing whether the intended distinction was received.

Primary metric:

```text
gain in first-seen listener understanding
───────────────────────────────────────
pronunciation-practice minutes
```

## Listener panel

Because intelligibility is listener-dependent, pre-register at least two listener strata:

1. Vietnamese English users;
2. non-Vietnamese proficient English users.

Where feasible, stratify non-Vietnamese listeners by familiarity with Vietnamese-accented English.

Do not make “native speaker” status the only validity anchor.

## Secondary outcomes

- listener effort/comprehensibility ratings;
- target-specific feature realization under a transparent human/acoustic rubric;
- communication breakdown rate;
- successful repair after one clarification request;
- same-item vs first-seen transfer gap;
- retention at a longer checkpoint;
- target-specific practice burden;
- learner abandonment/frustration;
- consistency across Vietnamese regional varieties;
- consistency across listener strata.

## Critical analysis

Test whether the priority rank predicts listener outcome beyond:

- baseline general proficiency;
- target lexical knowledge;
- speaking task level;
- sentence/context predictability;
- support level;
- speech rate;
- listener background;
- target frequency.

## Feature-specific validation

### Coda / cluster

Test whether preserving the candidate final element materially raises intended word/message identification, not merely expert pronunciation ratings.

### `/s,z/`

Separate:

```text
lexical final /s,z/
vs
morphological /s,z/

single coda
vs
cluster context
```

This mirrors the risk structure in `SRC-0073`.

### Lexical stress

Separate harmless prominence displacement from stress errors accompanied by vowel/syllable distortion. The latter is the stronger risk hypothesis from `SRC-0067`.

### High-functional-load contrasts

Do not assume a published general FL table perfectly predicts this population. Test whether FL adds predictive value to learner error frequency and lexical frequency.

## Scoring policy before RQ-008

ASR may be logged **only as exploratory comparison data**.

Primary validity must come from human/listener outcomes or a tightly constrained scoring method independently validated against them.

Prohibited primary outcomes:

```text
vendor pronunciation score
generic ASR confidence
accent similarity to native reference
```

## Decision rules

Adopt intelligibility-priority target selection if it produces a practically meaningful improvement in delayed first-seen listener understanding per learner minute without unacceptable burden.

Downgrade or remove a candidate priority if:

- frequent “errors” do not reduce listener understanding;
- correcting them improves native-likeness but not intelligibility/comprehensibility;
- another target family yields substantially larger listener gains per minute;
- effects occur only for one narrow listener group and do not fit the product communication goal.

## Pre-register

- near-A0 operational definition;
- Vietnamese regional/demographic reporting plan;
- candidate target inventory;
- target-priority algorithm version;
- training dose/time accounting;
- first-seen item construction rules;
- delay intervals;
- listener strata and minimum English proficiency;
- listener task and scoring rubric;
- inter-rater/retest reliability procedure;
- minimum worthwhile intelligibility gain;
- missing-data/exclusion rules;
- ASR exploratory-analysis plan if included.
