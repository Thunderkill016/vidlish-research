---
id: FEAT-VOC-001
title: Vocabulary evidence model
status: research-backed-candidate
research_question: RQ-001
---

# Feature research spec — Vocabulary evidence model

## Learner problem

A learner can recognize a word without being able to retrieve or use it, can succeed immediately and forget later, and can know the written form without reliably recognizing the spoken form. A single `known` flag hides these differences and can make Nếp advance too early or review the wrong thing.

## Target capability

Maintain enough task-grounded evidence to choose the next learning action honestly without demanding unrealistic total mastery of every lexical aspect.

## Research basis

- `SYN-VOC-002`
- `CLM-VOC-002` through `CLM-VOC-011`
- `PRN-011` through `PRN-015`

## Core rule

**Store attempts; derive state.** Do not store an irreversible mastery truth from one successful task.

## Proposed attempt contract

```text
learner_lexical_attempt
  user_id
  target_id
  target_kind            single_word | chunk
  construct              meaning_recognition | form_recognition |
                         meaning_recall | form_recall |
                         controlled_use
  input_mode             audio | text | image | context
  response_mode          choice | arrange | text | speech
  support_level          0..N
  answer_was_visible     boolean
  context_relation       same | parallel | changed
  correct                 boolean / bounded rubric result
  latency_ms              optional
  attempted_at
  delay_from_learning_ms  optional
```

The exact database naming can change. The research requirement is that the information needed to interpret the attempt is preserved.

## Derived learner view

```text
introduced
recognized
retrievable
usable
retained
```

These labels are conveniences for product logic. They are calculated from attempt history and can lose confidence after failures or long gaps.

## Inference boundaries

| Task result | May support | Must not silently claim |
| --- | --- | --- |
| multiple-choice meaning | recognition | recall / production |
| answer revealed then repeated | imitation/correction | independent recall |
| first-letter cloze | scaffolded form recall | uncued form recall |
| same-sentence retry | corrected same-context performance | transfer |
| changed parallel context | controlled transfer/use | spontaneous conversation ability |
| later answer-hidden probe | delayed evidence for that construct | permanent mastery |

## Words and chunks

Single words and multiword chunks are both lexical targets. For chunks, the engine records whether the full phrase was supplied by the learner or whether part of it was exposed as a cue.

## Aural vs written evidence

A listening-first A0 curriculum must not infer aural recognition from written translation tasks. The target may have separate evidence for spoken-form recognition and written-form recognition even when both contribute to one broader lexical state.

## UX consequences

- The learner does not see a complicated diagnostic dashboard during each lesson.
- The engine chooses the smallest task needed to resolve uncertainty.
- A recognition success can move the lesson forward while scheduling a later recall attempt.
- Failure after prior success is normal evidence, not a broken streak/mastery state.
- "Learned" copy should be avoided unless the UI clearly says what was demonstrated.

## Risks

- Too many evidence dimensions can create excessive testing.
- A rigid state machine can become another fake mastery system.
- Speech and spelling rubrics can confound lexical knowledge with pronunciation/orthography.
- Changed-context tasks can accidentally require grammar that the learner has not learned.

## Falsification / calibration

The model should be simplified if several stored distinctions fail to improve prediction of later performance or next-task selection. It should be expanded only when a new distinction changes useful product decisions.

## Learning metrics

- delayed recall by earlier evidence type;
- changed-context success by support level;
- false-positive rate: targets marked strong that fail quickly later;
- false-negative burden: unnecessary reviews of targets that remain robust;
- time spent measuring vs time spent learning.
