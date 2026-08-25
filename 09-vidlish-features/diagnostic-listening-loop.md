---
id: FEAT-LIS-001
title: Diagnostic listening loop
status: candidate-core
research_question: RQ-003
---

# Feature research spec — Diagnostic listening loop

## Learner problem

A failed listening-comprehension question does not reveal whether the learner failed to hear/segment the speech, access the spoken word's meaning, or construct the message. Replaying the same audio or immediately revealing text can hide the real failure.

## Target capability

Help a near-A0 learner build reliable spoken-form access and short-message comprehension while storing evidence that identifies what the learner could do without transcript/answer support.

## Research basis

- `SYN-LIS-002`
- `CLM-LIS-001` through `CLM-LIS-010`
- `PRN-023` through `PRN-030`
- RQ-001 lexical evidence model
- RQ-002 scaffold provenance model

## Interaction model

```text
short audio
  ↓
independent meaning attempt
  ↓
correct? ─ yes → store message evidence → continue / later transfer
  │
  no / uncertain
  ↓
critical decoding probe
  ↓
┌────────────────────┬─────────────────────┐
│ signal/segmentation│ form recognized     │
│ problem            │ but meaning failed  │
└─────────┬──────────┴──────────┬──────────┘
          ↓                     ↓
 sound-form teaching       meaning/context teaching
          └──────────┬──────────┘
                     ↓
              transcript/reveal
                     ↓
             replay + linkage
                     ↓
              no-text retry
                     ↓
             later parallel audio
```

The diagnostic classifier begins as deterministic task evidence, not an AI diagnosis.

## Minimum evidence events

```text
listening_attempt
  target_id
  utterance_id
  task_type
  input_modality = audio
  speaker_id
  source_type
  listen_index
  replay_count_before_attempt
  transcript_visible
  caption_visible
  support_level
  response
  correctness
  latency
  evidence_type
```

Potential `evidence_type` values:

```text
speech_form_discrimination
aural_word_recognition
segmentation
aural_form_meaning
message_comprehension
listening_transfer
```

## Stage-0 task constraints

- Use short utterances containing mostly known language plus the intended target.
- First scored meaning probe is audio-only except non-answer-bearing context support.
- A decoding diagnostic focuses only on the critical portion, not full-sentence dictation by default.
- If transcription is used, spelling tolerance must match the construct being measured.
- Transcript/caption can appear after evidence capture for teaching and sound-text mapping.
- Retry removes answer-bearing support.
- Transfer uses a parallel utterance and preferably a different speaker once the item is ready.

## Failure interpretation

Examples:

```text
meaning wrong + target not recognized from speech
→ likely decoding/access gap

meaning wrong + target recognized + target meaning unknown
→ lexical meaning gap

critical words recognized + meanings known + message wrong
→ parsing/message construction gap
```

These are **working diagnostic hypotheses**, not claims about hidden mental states. Store observed task results; derive the hypothesis separately.

## Risks

- Too many micro-probes make listening feel like a laboratory test.
- Word-choice probes may allow guessing.
- Dictation can accidentally become a spelling test.
- A single speaker can overfit the learner to one voice.
- Excessive replay can make an item artificially easy.
- Transcript reveal can dominate attention if shown too early.
- Failure may have multiple causes; deterministic branches can oversimplify.

## Falsification

The feature weakens if, compared with a simpler comprehension-only loop, it:

- does not improve delayed unseen listening;
- adds substantial time/friction without predictive value;
- misclassifies failure pathways often enough to give unhelpful remediation;
- produces gains only on trained utterances/speakers.

## Learning metrics

- delayed audio-only message comprehension;
- aural recognition of known targets in new utterances;
- performance with a new speaker;
- reduction in transcript/replay support needed;
- changed-context listening transfer;
- retained listening gains per minute.

## Engagement metrics — separate

- completion;
- replay count;
- diagnostic branch rate;
- transcript reveal rate;
- task time;
- abandonment.
