---
id: SYN-LIS-002
title: Separate perception, decoding and meaning evidence in short listening tasks
status: initial-synthesis
research_question: RQ-003
last_verified: 2026-08-25
---

# RQ-003 — Perception vs comprehension in Nếp listening

## Decision summary

Nếp should not represent listening with one boolean such as `understood_audio = true`.

For short beginner audio, the system should distinguish at least:

```text
PERCEIVE / DECODE
Can the learner recover useful spoken forms from the signal?

MEANING
Can the learner map those forms and context to the intended message?
```

The two interact, but research does not justify treating them as the same performance (`SRC-0032`, `SRC-0033`, `SRC-0034`).

## Why this matters for a true beginner

A learner may know `want` on a flashcard and still hear something else in `I want it` because spoken language contains reduction, linking, weak forms, varying talkers and time pressure. Diagnostic work has repeatedly found that orthographically known language can remain difficult in speech (`SRC-0030`, `SRC-0031`, `SRC-0036`).

If Nếp sees only:

```text
🔊 "I want it."
Question: What does it mean?
learner: wrong
```

it cannot know whether the learner:

1. failed to hear/segment `want`;
2. heard `want` but did not retrieve its meaning;
3. recognized the words but failed to combine the message;
4. knew the message but misunderstood the question/UI.

The next teaching action should differ for each case.

## What the evidence supports

### 1. Signal-level decoding deserves direct practice

The decoding-training review/meta-analysis (`SRC-0026`) found a medium pooled advantage for decoding instruction. Recent phonetic-training meta-analysis also shows that perception can improve, retain and generalize with targeted high-variability practice (`SRC-0029`).

**Product consequence:** Nếp needs explicit short tasks for speech perception/word recognition; merely exposing learners to longer audio and asking comprehension questions is insufficient as a diagnostic curriculum.

### 2. Spoken-word knowledge is modality-specific enough to measure

Recognition of high-frequency words from speech predicts listening performance (`SRC-0032`). More recent phonological-vocabulary research shows that fast contextual access to spoken vocabulary is strongly related to listening proficiency and that learners may possess written form-meaning knowledge without equally available spoken access (`SRC-0031`).

**Product consequence:** RQ-001's lexical evidence model needs aural evidence. `can_read(want)` cannot silently become `can_recognize_in_speech(want)`.

### 3. Decoding and comprehension must remain connected but separate

Leonard (`SRC-0033`) found a strong relation between decoding accuracy and comprehension, yet some good message comprehension occurred without near-perfect word decoding. Listening assessment research also treats input decoding, lexical search, parsing and meaning/discourse construction as distinguishable processing levels (`SRC-0034`).

**Product consequence:** do not require word-perfect transcription before marking a simple message understood. Conversely, a guessed meaning does not prove that the learner actually decoded the target form.

### 4. Bottom-up work should feed meaning, not become the whole course

General listening instruction (`SRC-0027`) and listening-strategy instruction (`SRC-0028`) have positive synthesized effects. In one low-proficiency intervention, combining bottom-up and metacognitive work outperformed either no training or metacognitive work alone (`SRC-0035`).

**Product consequence:** the session should return from a decoding diagnosis to message meaning and later transfer. Nếp should not become an endless dictation/phoneme-drill app.

### 5. Written transcript is support, not independent listening evidence

Showing the transcript changes the available information and therefore changes what the task can demonstrate. This follows from listening-assessment validity (`SRC-0034`) and the support-provenance rules from RQ-001/RQ-002.

**Product consequence:** for an independent aural probe, answer-bearing transcript/captions are hidden until after the scored attempt. They can then be excellent teaching support.

### 6. Dictation is useful but must be interpreted narrowly

Dictation/partial transcription appears frequently in decoding research (`SRC-0026`, `SRC-0032`, `SRC-0033`), but it requires a written response. A strict spelling score therefore risks mixing speech perception with orthographic production.

**Product consequence:** near A0, Nếp can use lower-writing-burden diagnostic alternatives:

- choose which known word/chunk was heard;
- arrange a tiny set of known word tiles;
- mark a boundary between words/chunks;
- lenient partial transcription when spelling is not the target;
- contrast two audio forms after an error.

If spelling is scored, label that extra construct explicitly.

## Proposed Nếp listening evidence model

Do not force these into one global score.

| Evidence | Example probe | What it supports |
| --- | --- | --- |
| `speech_form_discrimination` | which of two forms was heard? | low-level perceptual contrast |
| `aural_word_recognition` | select known target heard in a short utterance | spoken-form access |
| `segmentation` | identify word/chunk boundary or reconstruct known sequence | continuous-speech decoding |
| `aural_form_meaning` | hear target/message → choose meaning | spoken form → meaning |
| `message_comprehension` | hear short utterance → act/choose intended meaning | proposition/message understanding |
| `listening_transfer` | new speaker/new parallel utterance → understand without transcript | stronger generalized listening evidence |

## Default diagnostic loop for Stage 0

```text
1. play one short, bounded English utterance
2. independent meaning attempt, no transcript
3. if correct → optionally sample decoding only when needed; continue
4. if wrong/uncertain → run a tiny decoding probe on the critical known language
5. classify likely failure: signal/segmentation vs lexical meaning vs message construction
6. teach the smallest missing piece
7. reveal transcript only after the independent aural evidence is captured
8. replay while linking sound ↔ form ↔ meaning
9. retry without transcript
10. later test a parallel utterance / another speaker
```

This is a candidate product loop, not a validated diagnostic algorithm. `EXP-003` must test whether the extra diagnosis actually improves later listening enough to justify its time and complexity.

## Replay policy

Replay count itself is support metadata. Research in this cycle does not establish one universal number of listens.

Nếp should record:

```text
listen_index
replay_count_before_answer
speaker_id / voice characteristics
speech_rate / source
transcript_visible
caption_visible
support_level
```

A correct response on listen 1 and a correct response after five replays are both useful, but they are not identical evidence.

## What we should not conclude

- "If the learner knows the written word, they can hear it."
- "If they transcribe every word, they understood the message."
- "If they guessed the message, they decoded the target words."
- "Perfect word recognition is necessary for every successful comprehension event."
- "Phoneme training alone is a complete listening curriculum."
- "Metacognitive strategies alone solve beginner decoding problems."
- "Two replays / 90% / 95% is the universal A0 threshold."

## Product decisions unlocked

1. add modality-specific aural evidence to the learner model;
2. make transcript/caption visibility explicit support provenance;
3. split listening tasks into decoding and message-comprehension probes;
4. add a failure-diagnosis branch rather than repeating the same quiz;
5. use connected-speech and multi-talker variants for later transfer;
6. avoid spelling-heavy dictation as the only beginner decoding instrument;
7. evaluate the diagnostic loop against a simpler comprehension-only condition.
