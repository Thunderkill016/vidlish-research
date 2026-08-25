---
id: FEAT-SPK-001
title: Guided speaking ladder
status: candidate-core
research_question: RQ-006
---

# Feature research spec — Guided speaking ladder

## Learner problem

Near-A0 learners need actual speaking practice to build productive skill, but open conversation creates too many simultaneous demands and can make failure uninterpretable. At the other extreme, listen-and-repeat activities can look like speaking progress while never requiring independent retrieval.

## Target capability

Move the learner from short supported oral rehearsal to independent short utterances, controlled recombination and bounded interaction, while recording exactly what support and task demands were present.

## Research basis

- `SYN-SPK-001`
- `CLM-SPK-001` through `CLM-SPK-012`
- `PRN-050` through `PRN-061`
- RQ-001 vocabulary/chunk evidence
- RQ-002 scaffold provenance
- RQ-004 review timing
- RQ-005 transfer probes

## Architecture

```text
Learner Evidence
      │
      ├── target meaning/form known?
      ├── oral access evidence?
      ├── transfer evidence?
      └── support history
      ↓
Speaking Task Selector
      │
      ├── choose SP level
      ├── choose support
      ├── enforce prerequisite/novelty budget
      └── choose practice vs evidence mode
      ↓
Preparation / Rehearsal (optional)
      ↓
Independent Attempt
      ↓
Feedback / Self-repair
      ↓
Evidence Engine
      │
      ├── speaking attempt evidence
      └── scheduler update when relevant
      ↓
Later unseen speaking transfer probe
```

## Task levels

```text
SP0 rehearsal
SP1 bounded oral completion
SP2 full short-utterance retrieval
SP3 controlled recombination
SP4 guided one-turn interaction
SP5 bounded multi-turn role-play / information gap
SP6 open interaction (later / sampled)
```

The level is product metadata, not a CEFR equivalence.

## Hard evidence rules

1. `SP0` never counts as independent oral production.
2. If the full answer/model is visible at response time, label the attempt supported/rehearsal.
3. Independent speaking evidence requires `attempt_before_feedback = true`.
4. Record all answer-bearing support used before/during the response.
5. A corrected repetition after model reveal does not overwrite the failed independent attempt.
6. Repeating an exact task can update trained-context speaking evidence but does not create fresh transfer evidence.
7. A production claim requires an oral production response, not recognition alone.
8. A guided-interaction claim requires an actual contingent turn, not a monologue read from a script.
9. Do not use a global ASR/pronunciation score as a mastery gate before RQ-007/RQ-008 validation.

## Preparation support

Candidate support types:

```text
full_model_audio
full_model_text
chunk_bank
keyword_plan
picture_cue
meaning_cue
L1_intention_cue
interlocutor_preview
```

The task selector can deliberately use richer support during acquisition and fade it before independent evidence.

## Example lesson progression

Target:

```text
I want ___
```

Flow:

```text
1. understand "I want water."
2. SP0 repeat once if oral form is new
3. hide model
4. SP2: picture water → "I want water."
5. feedback / repair
6. SP3: picture tea → "I want tea."
7. later SP4:
   "What do you want?"
   → "I want tea."
8. delayed unseen parallel probe
```

Not every target needs every level in one session.

## Standardized interlocutor

For `SP4`/`SP5`, use a bounded state machine rather than unrestricted AI by default.

Example:

```text
state 1: ask expected question
state 2: accept task-success variants
state 3a: natural next turn
state 3b: clarification/repair prompt if needed
state 4: close interaction
```

Benefits:

- consistent task demand across learners;
- lower scoring ambiguity;
- known language coverage;
- easier experiment replication;
- interaction still requires a contingent learner response.

Generative AI may later realize surface variants only within a validated task contract.

## Feedback behavior

Initial policy:

```text
attempt
→ interpret target/task success
→ if repairable: one concise prompt
→ learner self-repair
→ if still unsuccessful: reveal/correct
→ rehearsal retry
```

Feedback never deletes the original attempt record.

## Attempt data

```text
speaking_attempt
  learner_id
  task_id
  speaking_level
  target_ids[]
  transfer_probe_id?
  task_first_seen

  planning_mode
  support_level
  support_types[]
  model_visible_at_response

  attempt_before_feedback
  repair_prompt_count
  model_revealed

  task_success?
  target_success?
  response_latency_ms?
  response_duration_ms?
  scorer_type
  scoring_rule_version
  scoring_confidence?

  occurred_at
```

Audio/transcript storage is a separate product/privacy decision; the evidence model must not require indefinite raw-audio retention.

## Evidence labels

Candidate task evidence:

```text
oral_target_recall
short_utterance_production
controlled_recombination
guided_turn_response
interaction_task_success
interaction_repair
speaking_transfer
```

Do not collapse these into one boolean.

## Task selector rules

1. If oral form has never been practiced, allow one brief SP0 rehearsal before retrieval.
2. If independent retrieval is weak, use SP1/SP2 rather than open interaction.
3. If short production is stable, introduce SP3 with known slot substitutions.
4. Open SP4 only when the question/context language is already comprehensible.
5. Open SP5 only when the learner can handle the component turns with acceptable support.
6. Sample SP6 later; do not require it for every lexical target.
7. Use RQ-004 review state to bring speaking tasks back after delay.
8. Use RQ-005 novelty rules for unseen speaking transfer.

## Scoring boundary before RQ-008

Production can be practiced before automated scoring is fully valid.

For research experiments and high-stakes evidence:

- prefer human/independent scoring or tightly constrained validated response sets;
- blind scorers to experimental condition where feasible;
- preserve scoring-rule versions;
- measure inter-rater agreement when human ratings are used.

An ASR transcript may help the interface, but an ASR mismatch alone is not learner failure until RQ-008 establishes its reliability for the target population/task.

## UX constraints

The learner should not see academic labels such as `SP3` or `controlled recombination`.

The experience should feel like:

```text
Hear it
→ Say it yourself
→ Change one thing
→ Answer someone
→ Try it later without help
```

Avoid a speaking screen dominated by scores, waveforms or “AI pronunciation 87/100” before those measurements are validated.

## Falsification

This feature should be simplified or rejected if `EXP-006` shows that:

- controlled oral retrieval adds no useful delayed production benefit over rehearsal/input;
- guided interaction adds burden without improving later unseen speaking;
- the ladder causes excessive failure/abandonment near A0;
- scoring reliability is too poor to interpret progression;
- task-level gains do not carry to unseen parallel production.

## Learning metric

Primary candidate:

```text
delayed unseen speaking-task success
per speaking-practice minute
```

Secondary:

- independent short-utterance retrieval;
- guided-turn success;
- changed-context productive success;
- support required;
- repair success;
- delayed retention.

## Engagement metric

- speaking task completion;
- voluntary retry rate;
- abandonment after speaking prompt;
- time spent waiting/recording;
- return for delayed speaking review.

Engagement does not substitute for speaking evidence.
