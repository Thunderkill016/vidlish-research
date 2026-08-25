---
id: SYN-SPK-001
title: Controlled speaking progression for near-A0 Nếp learners
status: initial-synthesis
research_question: RQ-006
last_verified: 2026-08-25
---

# RQ-006 — Controlled speaking before free conversation

## Decision summary

Nếp should begin speaking **early but narrowly**.

Near-A0 learners should not be held in silent comprehension-only mode until they are “ready,” and they also should not be thrown directly into open AI conversation. The evidence supports a middle path:

```text
understand a useful message
        ↓
hear / inspect a usable chunk
        ↓
rehearse if needed
        ↓
retrieve a short utterance without the answer visible
        ↓
recombine it in a bounded changed context
        ↓
respond to a standardized conversational turn
        ↓
repeat with less support
        ↓
show it again on an unseen parallel speaking task
```

Speaking practice and speaking evidence must remain distinct.

## Why this fits near A0

The CEFR Pre-A1 profile (`SRC-0001`) is deliberately narrow: short phrases, basic personal information, simple questions/answers, formulaic expressions and gesture-supported interaction. It is not a profile of sustained spontaneous conversation.

At the same time, production-practice evidence (`SRC-0054`) indicates that productive ability benefits from productive practice. Waiting for comprehension alone to turn into fluent production is therefore not a sufficient product strategy.

Nếp should make the learner **say useful English before free conversation becomes feasible**, but keep the production demand inside what the learner can actually formulate.

## Speaking task ladder

The following ladder is product taxonomy, not a universal acquisition sequence.

### `SP0` — rehearsal only

Examples:

```text
listen → repeat
shadow a short chunk
read a visible phrase aloud
```

Useful for articulation, familiarization and reducing first-attempt load.

**Evidence interpretation:** rehearsal. It does **not** establish independent oral retrieval because the model is available.

### `SP1` — bounded oral completion

Example:

```text
Audio/context: "I want water."
Later cue: "I ___ water."
Learner says: "want"
```

Or a meaning/picture cue that requires one target chunk.

**Evidence:** controlled oral target retrieval, provided the answer was not visible.

### `SP2` — full short-utterance retrieval

Example:

```text
[picture: water + intention cue]
Learner says:
"I want water."
```

The phrase must be retrieved, not read.

**Evidence:** bounded independent utterance production in the trained capability family.

### `SP3` — controlled recombination

Example:

```text
learned:
I want water.

new known slot:
tea

learner:
I want tea.
```

This connects RQ-006 to `FEAT-TRN-001`: the learner is producing language in a changed but controlled context.

**Evidence:** controlled productive transfer when the probe is unseen and non-target language is known.

### `SP4` — guided one-turn interaction

A standardized interlocutor asks a known/parallel question:

```text
Interlocutor: "What do you want?"
Learner: "I want tea."
```

Or:

```text
"What's your name?"
"Where do you live?"
```

**Evidence:** guided turn response. This is more interactional than monologic retrieval but still bounded.

### `SP5` — bounded multi-turn role-play / information gap

Example:

```text
café scenario
2–4 turns
known communicative functions
known surrounding vocabulary
standardized interlocutor behavior
```

Learner may need to request, answer, confirm or repair.

**Evidence:** interactional task evidence such as successful turn response, request completion, meaning negotiation or repair. `SRC-0059` supports standardized interactive tasks as a viable way to measure interactional subskills.

### `SP6` — open interaction

Learner has much more freedom over message and form.

This is a later/sample task, not the default near-A0 mastery gate. It adds lexical choice, grammar, discourse management, pronunciation, planning and interaction demands at once.

## Preparation is allowed during learning, but must have provenance

Planning can improve oral production (`SRC-0055`, `SRC-0056`). Therefore Nếp may deliberately prepare learners before an oral attempt.

Candidate support progression:

```text
full model
→ partial phrase / chunk bank
→ keywords / picture / intention
→ no answer-bearing language
```

However:

```text
visible full script while speaking
= supported rehearsal

script hidden before response
= possible independent production evidence
```

A planning phase and an independent attempt can occur in the same lesson; they simply cannot be interpreted as the same evidence condition.

## Task complexity should grow by one meaningful burden at a time

`SRC-0057` shows that novice performance responds to task sequencing and guided vocabulary planning, with trade-offs when complexity rises.

For Nếp, increase one major demand at a time where possible:

```text
same target + new object
before
same target + new scenario + new speaker + new grammar + open response
```

Use the learner model to keep surrounding vocabulary/constructions within demonstrated capability.

## Repeat to proceduralize; vary to generalize

Task repetition can improve oral performance (`SRC-0058`). Nếp should use this for practice:

```text
attempt
→ feedback
→ repair / model if needed
→ repeat
→ reduced support
```

But exact repetition creates a familiar task. It is not evidence that the learner can speak in a new situation.

Therefore:

```text
same-task repetition
= practice / trained-context improvement

unseen parallel speaking probe
= candidate transfer evidence
```

RQ-004 schedules when to revisit; RQ-005 determines when the changed speaking task qualifies as transfer.

## Feedback policy

Oral corrective feedback can improve L2 development (`SRC-0060`). Initial Nếp policy:

```text
independent attempt
      ↓
acceptable for target/task?
   ↙             ↘
 yes             no
  ↓               ↓
continue      short repair prompt
                  ↓
             self-repair?
             ↙       ↘
           yes       no
            ↓         ↓
        continue   model/explanation
                       ↓
                  rehearsal retry
```

Rules:

1. Do not interrupt before the learner has produced enough to interpret the intended attempt.
2. Prefer a bounded self-repair opportunity when the form is plausibly retrievable.
3. Do not loop prompts indefinitely; reveal/correct when needed.
4. A corrected repetition after model reveal is practice evidence, not independent success.
5. Feedback policy should be versioned and experimentally calibrated.

## What counts as speaking evidence

Store task evidence rather than a single `speaking_score`.

Candidate evidence labels:

```text
oral_target_recall
short_utterance_production
controlled_recombination
guided_turn_response
interaction_task_success
interaction_repair
speaking_transfer
```

These labels describe what was elicited. They are not claims of independent cognitive faculties.

## What does NOT count as the same thing

```text
listen + repeat
≠ independent recall

read visible sentence aloud
≠ independent utterance production

one memorized role-play
≠ interactional flexibility

fast speech
≠ communicative success

ASR confidence
≠ validated speaking proficiency
```

## Speaking measurement before RQ-007/RQ-008

RQ-006 cannot validate pronunciation scoring or ASR scoring.

Until those cycles are complete:

- retain enough task metadata to interpret attempts;
- store audio only under an explicit product/privacy policy;
- use human-reviewed scoring in experiments when validity matters;
- use automated transcripts/scores only as provisional practice aids, not mastery truth;
- do not expose a global `87/100 speaking` score as scientific evidence.

## Proposed data separation

### Speaking task definition

```text
speaking_task
  task_id
  level              # SP0..SP6
  target_ids[]
  communicative_goal
  expected_response_family[]
  allowed_variants[]
  prerequisite_ids[]
  interlocutor_script_id?
  planned_support_options[]
  transfer_family_id?
```

### Speaking attempt evidence

```text
speaking_attempt
  learner_id
  task_id
  target_ids[]
  speaking_level
  task_first_seen

  planning_mode
  support_level
  support_types[]
  model_visible_at_response
  attempt_before_feedback

  task_success?
  target_success?
  response_latency_ms?
  response_duration_ms?
  self_repair_count?

  scorer_type
  scoring_rule_version
  scoring_confidence?
  audio_ref?              # product/privacy policy required
  occurred_at
```

No field above is allowed to mean global speaking mastery.

## Product behavior

A learner with strong comprehension but weak production might receive:

```text
Today
  input + meaning success
      ↓
SP1 oral completion
      ↓
SP2 short utterance
      ↓
feedback + one repeat
```

A learner already retrieving independently might skip rehearsal and move to:

```text
SP3 changed slot
→ SP4 one-turn Q&A
→ later SP5 bounded role-play
```

The engine therefore adapts **support and task demand**, not merely lesson difficulty.

## Claims we should not make yet

Do not claim that:

- this ladder is the universal order of speaking acquisition;
- `SP5` equals CEFR A1;
- a speech-recognition transcript is a valid pronunciation/grammar score;
- formulaic production proves generative grammar;
- task repetition proves transfer;
- every target needs open speaking practice;
- the learner should receive corrective feedback on every error.

## Research-to-product contract

RQ-006 supports:

```text
CLM-SPK-001..012
        ↓
PRN-050..061
        ↓
FEAT-SPK-001
        ↓
EXP-006
```

The next research dependencies are:

- `RQ-007`: which pronunciation targets matter for intelligibility for Vietnamese L1 learners;
- `RQ-008`: what ASR can score reliably enough to use in this ladder.
