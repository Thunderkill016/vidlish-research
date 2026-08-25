---
id: SYN-ASR-001
title: Validity boundaries for ASR and automated pronunciation scoring in Nếp
status: initial-synthesis
research_question: RQ-008
last_verified: 2026-08-25
---

# RQ-008 — What can ASR score reliably for Vietnamese-speaking Nếp learners?

## Decision summary

Nếp should **use ASR, but not believe ASR**.

ASR is useful as a cheap, immediate sensor in pronunciation practice. It is not, by itself, a validated pronunciation judge, human-intelligibility simulator or mastery engine.

The product contract is:

```text
speech
  ↓
ASR / acoustic / pronunciation detector
  ↓
machine signal
  ↓
validity gate
  ├── validated for this feature + population + task? → supporting evidence / feedback
  └── not validated or uncertain?                  → no mastery claim
  ↓
human-listener outcome + transfer evidence
```

This is especially important for Vietnamese learners because current systems show non-uniform error across L1 backgrounds and Vietnamese-accented English is among the higher-error groups in several recent benchmarks (`SRC-0082`, `SRC-0083`).

## The central construct error to avoid

### ASR asks

> What word sequence is most likely given this audio and the model's learned language prior?

### Pronunciation assessment asks

> Which aspects of this learner's speech threaten intelligibility or deserve feedback?

These objectives overlap, but they are not the same (`SRC-0079`, `SRC-0080`). A strong ASR system is explicitly trained to be robust to accent, noise and variation. Therefore it may correctly recover an intended word even when the pronunciation differs substantially from the target model.

So this inference is invalid:

```text
ASR transcribed the intended sentence
→ pronunciation is correct
```

and so is this one:

```text
ASR failed
→ learner pronounced it wrong
```

## What ASR can currently do for Nếp

### 1. Candidate machine-intelligibility signal

For constrained speech with a known or bounded target, transcript agreement can tell us whether **this ASR model** recovered the intended lexical content.

Useful fields:

```text
expected_text_or_intent
asr_text
alignment
insertions
substitutions
deletions
model_confidence_if_available
```

This is useful for triage and practice, not human-intelligibility mastery. ASR/human agreement varies by speaker and task (`SRC-0078`).

### 2. Candidate error localization

Where the learner is expected to say a known word/chunk, alignment and repeated machine errors can identify places worth checking.

Example:

```text
expected: likes
ASR across attempts: like / lights / like
```

This can trigger a **diagnostic probe** for final `/s/`; it cannot conclude that `/s/` is absent without feature-specific evidence.

### 3. Practice feedback

ASR-based pronunciation practice has an overall positive learning effect in the literature, especially when feedback is explicit (`SRC-0077`). That supports using the technology to create attempts, noticing and correction loops.

Learning benefit does **not** validate every machine score generated inside the loop.

### 4. Input to a feature-specific detector

ASR/SSL representations, forced alignment, GOP-like measures, acoustic measurements and dedicated pronunciation models can contribute to feature-level detection (`SRC-0080`).

But each target requires validation. A `/s,z/`-ending detector and a lexical-stress detector are different measurement instruments.

## What ASR cannot currently certify for Nếp

Without target-population validation, do not use ordinary ASR or vendor aggregate scores to certify:

```text
pronunciation mastery
human intelligibility
comprehensibility
native-likeness / accentedness
phoneme correctness
lexical stress correctness
rhythm
intonation
transfer to unseen speech
```

## Why WER/MER is not a pronunciation score

WER/MER measures how a recognizer's text differs from a reference. That is useful for evaluating transcription systems.

It is not a stable pronunciation-quality scale.

Recent evidence (`SRC-0084`) shows a key paradox: very accurate systems can produce near-zero transcription errors while correlating weakly with human pronunciation judgments. The system has become good at **recovering the word despite pronunciation variation**.

Therefore:

```text
lower WER
≠ linearly better pronunciation
```

## Vietnamese-specific risk

Two recent sources matter directly:

- Whisper evaluation across diverse English accents found Vietnamese and Thai among the highest-error variants and tone-language backgrounds with elevated error (`SRC-0082`).
- A 2026 multi-system L2-ARCTIC benchmark found Vietnamese speakers had notably higher error across five current ASR systems (`SRC-0083`).

Prior Vietnamese case evidence using Otter also showed that machine transcription and human-listener intelligibility can diverge (`SRC-0072`).

Nếp must interpret this as an **instrument validity problem**, not a learner deficit.

## Machine evidence classes

Nếp should assign machine outputs to one of four classes.

### `machine_observation`

Raw facts:

```text
ASR output
confidence
alignment
latency
acoustic features
model metadata
```

No educational interpretation yet.

### `machine_candidate`

A pattern suggests a possible issue:

```text
repeated final token deletion
low-confidence region
expected/observed mismatch
```

May trigger a diagnostic probe.

### `validated_machine_evidence`

The detector has been calibrated for:

```text
feature
population
speech task
recording conditions
reference / label procedure
model version
```

It may contribute to learner evidence inside its validated scope.

### `human_outcome_evidence`

A human listener actually identifies the intended word/message or rates effort under a defined protocol.

This remains the strongest criterion for Nếp's intelligibility-first pronunciation claims.

## Validation matrix

Every automated signal should declare:

| Dimension | Required question |
| --- | --- |
| Construct | What exactly is being measured? |
| Population | Was Vietnamese L1 represented? Which region/proficiency? |
| Task | isolated word, read sentence, guided production, spontaneous speech? |
| Context | known text or open response? |
| Audio | clean mic, phone mic, traffic/noise? |
| Human criterion | transcription, meaning choice, expert feature label, scalar rating? |
| Error | false correction and missed-error rates? |
| Fairness | do errors differ by speaker subgroup? |
| Version | provider/model/config/scoring-rule version? |
| Generalization | does it work on first-seen items/speakers? |

If these are unknown, Nếp should not present a precise educational score.

## Product policy for near-A0

```text
ASR says likely OK
        ↓
allow practice flow to continue
but do not mark pronunciation mastered from ASR alone

ASR says likely problem
        ↓
check recording quality / retry
        ↓
feature-specific diagnostic if available
        ↓
small corrective feedback
        ↓
new production attempt

ASR and feature detector disagree
        ↓
uncertain
        ↓
no punitive score / no mastery gate
```

## Relationship to FEAT-PRN-001

`FEAT-PRN-001` chooses **what pronunciation target matters**.

`FEAT-ASR-001` decides **whether a machine is allowed to judge that target, and how much evidential weight its output receives**.

```text
Intelligibility-first target selector
             ↓
pronunciation task
             ↓
ASR / detector
             ↓
ASR Evidence Gate
             ↓
Evidence Engine
```

## What the literature does not establish

RQ-008 does not establish:

- a universal best ASR provider for Nếp;
- a safe confidence threshold;
- that Whisper large-v3 is the best pronunciation sensor just because it transcribes well;
- that one global pronunciation API score is valid for Vietnamese near-A0;
- a minimum human-machine correlation sufficient for mastery;
- a safe false-positive rate for corrective feedback;
- generalization from read speech to guided/spontaneous speech;
- reliable automated scoring of all suprasegmental features.

Those become `EXP-008` product-validation questions.

## Product conclusion

The correct Nếp architecture is **not**:

```text
microphone
→ ASR
→ score 87/100
→ mastery
```

It is:

```text
microphone
→ machine observation
→ calibrated validity gate
→ bounded feedback / diagnostic
→ independent attempt
→ human-relevant outcome evidence
→ mastery inference
```
