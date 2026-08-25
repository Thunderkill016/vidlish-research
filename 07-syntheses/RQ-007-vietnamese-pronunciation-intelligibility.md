---
id: SYN-PRN-001
title: Intelligibility-first pronunciation priorities for Vietnamese-speaking Nếp learners
status: initial-synthesis
research_question: RQ-007
last_verified: 2026-08-25
---

# RQ-007 — Intelligibility-first pronunciation priorities

## Decision summary

Nếp should **not** teach pronunciation as a tour through the IPA and should not optimize for native-like accent ratings.

For a Vietnamese-speaking learner near A0, pronunciation work should be selected from the intersection of:

```text
Vietnamese population prior
        ×
learner's observed pronunciation pattern
        ×
communicative / functional load
        ×
actual listener consequence
        ×
prerequisite + practice cost
        ↓
next pronunciation target
```

The first goal is **preserve enough phonological information for the intended word/message to survive**. Ease/naturalness can improve after that. Accent reduction is not a mastery dimension.

## Constructs Nếp must keep separate

```text
intelligibility
= was the intended word/message actually understood?

comprehensibility
= how much effort did understanding require?

accentedness
= how different did the speech sound from a chosen native norm?
```

These dimensions are related but not interchangeable (`SRC-0063`, `SRC-0064`).

**Nếp product target:** primarily intelligibility, secondarily comprehensibility where it is useful and measurable. Never treat accentedness as failure by itself.

## Candidate priority tiers

These are **product priority tiers**, not universal stages of human phonological acquisition.

### Tier I — preserve word shape and grammatical information

Highest candidate priority for Vietnamese-speaking beginners:

1. audible, contrast-preserving English word-final consonants when their loss changes the lexical item;
2. word-final consonant clusters where deletion removes important information;
3. especially high-risk morphology-bearing `/s,z/` environments currently supported by direct Vietnamese naturalistic evidence;
4. avoidance of syllable restructuring that deletes or inserts material enough to change recognition.

Why:

- direct Vietnamese syllable-structure evidence (`SRC-0070`);
- repeated Vietnamese-English observations of final/cluster loss (`SRC-0072`, `SRC-0074`);
- recent naturalistic `/s,z/` evidence (`SRC-0073`).

Important nuance: **coda preservation does not mean native allophonic perfection**. For example, Nếp should not force audible final-stop release simply because one prestige accent does it in some contexts. The target is adequate word/message identification.

### Tier II — preserve lexical contrasts and lexical access

Candidate priorities:

- learner-specific **high-functional-load consonant contrasts**;
- learner-specific high-value vowel contrasts;
- lexical stress when the deviation changes vowel quality, syllable realization or word recognition;
- vowel duration/quality when the learner collapses a contrast used in his or her target vocabulary.

General functional-load evidence supports this prioritization logic (`SRC-0066`), while Vietnamese vowel/stress evidence supplies candidate risk families (`SRC-0068`, `SRC-0069`, `SRC-0074`).

Nếp must not hard-code “Vietnamese learners need phoneme X” without an individual diagnostic.

### Tier III — reduce listener effort and improve message organization

Candidate targets after basic word-form stability:

- sentence focus / prominence on communicatively important information;
- chunk/thought-group boundaries;
- timing and reduction patterns where they make words easier to locate;
- speaking rate and pause placement when they materially raise listener effort.

This tier is motivated by general comprehensibility evidence (`SRC-0063`) and Vietnamese prosody/listening work (`SRC-0069`, `SRC-0075`).

Nếp should not train a caricatured “stress-timed rhythm” as an accent badge.

### Tier IV — interactional prosody and optional refinement

Candidate later targets:

- question/statement tunes when they alter pragmatic interpretation;
- contrastive focus;
- repair/confirmation prosody;
- finer accent features requested by the learner.

Vietnamese L1 transfer into English intonation exists (`SRC-0076`), but RQ-007 does not show that native-like question tunes are a first-order A0 intelligibility requirement.

## What should NOT automatically be early curriculum

```text
all 44-ish English phonemes in IPA order
all minimal pairs equally
/θ/ and /ð/ just because they sound non-native
perfect aspiration
perfect rhoticity/non-rhoticity
native-like schwa in every context
native-like stop release
accent elimination
intonation imitation for its own sake
```

Any of those may become useful for an individual learner, but only when communicative value + learner evidence justify the cost.

## Pronunciation target model

Nếp needs explicit target metadata rather than a flat list of sounds.

```yaml
PronunciationTarget:
  id: PRON_TARGET_...
  feature_family: coda | cluster | consonant_contrast | vowel_contrast | lexical_stress | focus | timing | intonation
  target_relation: "word-final /s,z/ presence"
  communicative_function: "preserve plural/3SG/lexical contrast"
  vietnamese_prior: high | moderate | unknown
  functional_load: high | moderate | low | unknown
  prerequisite_targets: []
  dialect_scope: universal_candidate | northern_candidate | southern_candidate | unknown
  evidence_ids: []
  accepted_variation: []
  forbidden_inference: "native-likeness"
```

`functional_load` and `vietnamese_prior` are priors, not learner state.

## Learner-specific priority engine

```text
candidate target pool
      ↓
Vietnamese prior risk
      ↓
learner diagnostic evidence
      ↓
Does this deviation preserve intended word/message?
      ↓
communicative-cost estimate
      ↓
teachability + current curriculum relevance
      ↓
rank next pronunciation work
```

A simple first candidate scoring model can be:

```text
priority =
  learner_error_probability
× communicative_cost
× curriculum_relevance
× evidence_confidence
÷ expected_practice_cost
```

Do **not** ship this formula as psychometric truth. It is an engineering hypothesis to calibrate through `EXP-007`.

## Integrating pronunciation with the speaking ladder

Pronunciation is not a separate mini-course that suspends communication.

Use `FEAT-SPK-001` contexts:

```text
SP0 rehearsal
    ↓ pronunciation noticing/perception if needed
SP1 bounded oral retrieval
    ↓ target-focused production evidence
SP2 short utterance
    ↓ word/message intelligibility
SP3 changed slot/context
    ↓ pronunciation transfer
SP4-SP5 guided interaction
    ↓ listener success / repair if needed
```

Example target: final `/s/` in `likes`

```text
1. learner understands "He likes tea."
2. notices contrast: like / likes
3. hears which message was said
4. produces "likes" in a bounded phrase
5. produces first-seen parallel: "She likes coffee."
6. listener identifies intended sentence/person-number relation
7. later delayed production with no model
```

This links perception, production, transfer and retention without turning the session into phonetics theory.

## Pronunciation evidence model

Do not store only:

```text
pronunciation_score = 82
```

Store provenance:

```text
PronunciationAttempt
  learner_id
  target_feature_id
  speech_task_id
  speaking_level
  first_seen
  target_text_or_intent
  feature_family
  scoring_method
  scoring_rule_version
  listener_background_if_human
  support_level
  model_visible_at_response
  attempt_before_feedback
  feature_realized_candidate
  intended_word_identified
  intended_message_understood
  comprehensibility_rating_optional
  repair_needed
  repair_success
  occurred_at
```

Important:

```text
feature_realized_candidate = true
≠ message intelligible

message intelligible once
≠ pronunciation target mastered

accentedness high
≠ communication failure
```

## Perception is useful but does not need to gate every production

Vietnamese vowel/stress research shows perception and production can use different cue systems (`SRC-0069`, `SRC-0074`). Pronunciation instruction can include perception tasks, but RQ-007 does not establish a universal `perception first → production later` law.

Use perception when it helps diagnose or form a contrast; then obtain production and listener-outcome evidence when production is the goal.

## Listener sampling policy

A pronunciation system for international English cannot validate itself against a single listener population.

Initial validation should include at least:

- Vietnamese English users who share the learner L1;
- non-Vietnamese proficient English users;
- where feasible, listeners with different degrees of Vietnamese-accent familiarity.

Listener background must be logged (`SRC-0071`, `SRC-0072`).

## Regional Vietnamese variation

Northern, Central and Southern Vietnamese phonologies differ. RQ-007 therefore provides **population priors**, never rules such as:

> “Vietnamese speakers always omit X.”

Nếp should ask the learner's own speech to confirm the target before allocating meaningful practice time.

## Feedback policy

After an independent attempt:

```text
listener/task success?
  ├─ yes → do not correct merely to erase accent
  └─ no / high-risk feature failure
       ↓
     smallest useful cue
       ↓
     retry without full model if plausible
       ↓
     explicit model/articulation support if still needed
       ↓
     supported rehearsal
       ↓
     later independent attempt
```

Corrections should target **communication-relevant deviations**, not every detectable phonetic departure.

## Relationship to RQ-008 / ASR

RQ-007 defines **what Nếp wishes to measure**. It does not prove that ASR can measure it.

Until RQ-008:

- ASR transcription can be exploratory telemetry, not ground truth;
- no opaque 0–100 pronunciation score;
- no feature mastery decision from vendor confidence alone;
- no accent penalty;
- human/listener outcome must anchor `EXP-007` validity.

## Falsification

The synthesis should be revised if Nếp data show that:

- the proposed Tier I targets do not predict listener understanding in Vietnamese near-A0 speech;
- a generic broad pronunciation curriculum yields equal/better listener gains per minute;
- functional-load priors add no predictive value after individual learner data;
- target prioritization varies so strongly by Vietnamese region/listener group that one common prior is misleading;
- listener-based measures cannot be made reliable enough for practical validation.

## Bottom line

Nếp should teach pronunciation **where sound carries useful information and communication is actually at risk**.

```text
not: "How native do you sound?"

but:
"Did the listener get the word/message?"
"Which sound pattern caused the failure?"
"Can you fix that pattern in a new utterance later?"
```
