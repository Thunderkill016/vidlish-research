---
id: FEAT-READ-001
title: Adaptive reading progression engine
status: research-backed-candidate
research_question: RQ-013
---

# Feature research spec — Adaptive reading progression engine

## Learner problem

Near-A0 learners can get trapped between two bad extremes:

- isolated sentence/translation exercises that never become real reading;
- authentic connected text that is so difficult the learner must translate line by line.

Reading support can also hide what the learner can actually do independently.

## Target capability

Understand increasingly long connected English text with adequate fluency and progressively less support, then transfer that ability to unseen text.

## Research basis

- `SYN-READ-001`
- `CLM-READ-001` through `CLM-READ-016`
- `PRN-149` through `PRN-164`
- `FEAT-VOC-001`
- `FEAT-GRM-001`
- `FEAT-SCF-001`
- `FEAT-TRN-001`
- `FEAT-REV-001`

## Reading stages

```ts
type ReadingStage =
  | "message"
  | "microtext"
  | "graded-short"
  | "sustained-easy"
  | "authentic";
```

### Message
One or two short propositions with known/high-readiness language.

### Microtext
Several connected sentences requiring reference/coherence across sentence boundaries.

### Graded short
Short connected text with controlled lexical/construction load and a small tolerable unknown set.

### Sustained easy
Longer easy/graded reading optimized for flow, volume and meaning rather than constant testing.

### Authentic
Increasingly real-world text selected by learner × text readiness, not by one CEFR badge.

## Text readiness

```ts
type ReadingReadiness = {
  estimatedLexicalCoverage: number;
  estimatedConstructionCoverage: number;
  unknownCriticalItems: string[];
  topicFamiliarity?: number;
  textLength: number;
  discourseComplexity?: number;
  supportBudget?: number;
};
```

No one field is a hard universal unlock threshold.

## Attempt model

```ts
type ReadingAttempt = {
  userId: string;
  textId: string;
  stage: ReadingStage;
  firstSeen: boolean;
  exposureIndex: number;
  audioUsed: boolean;
  glossCount: number;
  translationCount: number;
  rereadCount: number;
  readingMs: number;
  gistCorrect?: boolean;
  detailCorrect?: boolean;
  constructionProbeCorrect?: boolean;
  lexicalProbeCorrect?: boolean;
};
```

## Evidence states

At minimum distinguish:

```text
independent_first_read
independent_reread
read_with_gloss
read_with_translation
read_while_listening
repeated_reading
```

Do not collapse them into one `reading_correct` boolean.

## Default interaction

```text
1. show connected text at current readiness
2. learner reads independently first
3. capture meaning evidence
4. if blocked, expose smallest useful gloss/support
5. preserve reading flow
6. optional reread if pedagogically useful
7. later use unseen parallel text with less/no support
```

## Gloss behavior

Default:

- no persistent full translation;
- tap word/chunk for bounded help;
- distinguish noncritical unknowns from message-critical unknowns;
- do not auto-create every looked-up item as a review card;
- record support provenance.

## Audio behavior

Audio can be:

- optional learner support;
- scheduled for orthography↔sound mapping;
- used in a fluency/repeated-reading task;
- used as accessibility support.

Audio should not be permanently attached as the only way a learner reads a text.

After audio-assisted reading, probe a new text without audio before inferring independent reading growth.

## Reading-flow rule

Do not interrupt every sentence with a quiz.

For sustained/graded reading, sample evidence sparsely enough to preserve connected comprehension.

Candidate pattern:

```text
read short section
→ one gist/meaning checkpoint
→ continue
→ optional detail/transfer probe after meaningful boundary
```

Exact sampling frequency is experimental.

## Fluency behavior

Track rate only with comprehension and support context.

Bad metric:

```text
WPM ↑ = reading mastery ↑
```

Better evidence bundle:

```text
reading time
+ comprehension
+ rereads
+ support use
+ text readiness
+ unseen transfer
```

## Repeated reading

Use selectively when:

- word access is slow despite known vocabulary;
- construction parsing is accurate but laborious;
- learner needs orthography↔sound fluency;
- a short text is worth consolidating.

Do not force repeated reading of every text.

After repeated practice, test unfamiliar parallel text to estimate transfer.

## Strategy prompts

Strategy instruction should be failure-contingent and stage-aware.

Near-A0 examples:

```text
"Read the whole sentence before opening the word help."
"This unknown word is not needed for the main idea—keep going."
"Read the previous sentence again: who does 'he' refer to?"
```

Later stages can include purpose setting, structure, inference, questioning, skimming/scanning.

Do not front-load a taxonomy of reading strategies.

## Progress UI

Good:

```text
Short messages — independent
Connected 3–4 sentence texts — usually independent
Longer graded texts — uses 2–3 word helps
Reading rate — improving at stable comprehension
```

Avoid:

```text
Reading level: 74%
```

without a validated model explaining what that percentage means.

## Falsification

This feature is weakened if:

- sentence-only practice transfers equally well to connected unseen reading at lower cost;
- graded/easy text produces no advantage in retention or sustained comprehension;
- audio support does not fade or independent reading does not improve;
- gloss use becomes the dominant activity;
- reading-rate gains fail to transfer to unseen text;
- readiness estimates do not predict reading success;
- extensive-reading engagement produces volume but no measurable reading improvement.

## Experiment

See `EXP-013`.
