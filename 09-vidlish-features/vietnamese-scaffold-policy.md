---
id: FEAT-SCF-001
title: Adaptive Vietnamese scaffold policy
status: candidate-core
research_question: RQ-002
---

# Feature research spec — Adaptive Vietnamese scaffold policy

## Learner problem

A near-A0 Vietnamese learner may not have enough English to understand instructions,
definitions or new input without help. But if Vietnamese answers are always visible, Nếp
cannot tell whether the learner understood English or merely read the support.

## Target capability

Help the learner enter and continue an English task while progressively collecting evidence
that the same task can later be completed with less or no answer-bearing Vietnamese support.

## Research basis

- `SYN-SCF-001`
- `CLM-SCF-001` through `CLM-SCF-009`
- `PRN-016` through `PRN-021`
- RQ-001 task-sensitive evidence model (`SYN-VOC-002`, `FEAT-VOC-001`)

## Proposed interaction model

```text
task begins
  ↓
is this a scored independent attempt?
  ├─ yes → hide answer-bearing Vietnamese
  └─ no  → allow baseline task/instruction scaffold
  ↓
learner attempts / requests help / fails
  ↓
reveal smallest next scaffold level
  ↓
record support_type + support_level + trigger
  ↓
feedback
  ↓
later retry with lower support
```

## Scaffold levels

| Level | Meaning | Examples |
| --- | --- | --- |
| S0 | independent | English target + allowed non-answer context only |
| S1 | perceptual/context support | replay, image, scene cue |
| S2 | Vietnamese instruction/context hint | task instruction; scenario clarification |
| S3 | Vietnamese micro-gloss | one word/chunk meaning |
| S4 | partial meaning support | paraphrase or partial translation |
| S5 | answer-bearing rescue | full translation / explicit answer |

Levels are an initial product taxonomy, not a scientific universal scale.

## Required attempt data

```text
attempt_id
learner_id
target_id
task_type
input_modality

support_level_at_attempt
support_types[]
support_trigger:
  default | learner_request | failure | system_adaptation

answer
correctness
latency

independent:
  true | false

occurred_at
```

`independent=true` is only allowed when no answer-bearing support for the tested construct
was visible.

## Initial behavior rules

- Vietnamese UI instruction can be default for Stage 0 when it prevents task confusion.
- Answer-bearing Vietnamese meaning is hidden for an independent comprehension/recall
  probe.
- After failure or explicit help request, show the smallest relevant scaffold.
- Full translation is later rescue, not the default state of every lesson.
- Success after support remains useful learning evidence but cannot be silently stored as
  unsupported success.
- Repeated unsupported success makes the relevant scaffold less likely to auto-appear.
- Repeated failure can increase support, but does not lower the task's historical evidence
  integrity.

## Risks

- Too little support: user cannot even understand what to do.
- Too much support: learner reads Vietnamese instead of processing English.
- Frequent reveal interactions create UI friction.
- Learner may optimize for fast reveal instead of attempting.
- A support hierarchy that works for text may fail for listening.
- Automatically suppressing support may frustrate the learner.
- Vietnamese translations can flatten polysemy/pragmatic nuance.

## Falsification

The proposed policy weakens if progressive support:

- yields worse delayed English performance than a simpler always-on policy;
- causes materially higher abandonment without later-learning benefit;
- adds task time without improving unsupported later performance;
- produces no useful predictive relation between support level and later ability.

## Learning metrics

- next-day unsupported comprehension/recall;
- changed-context performance;
- probability of later success conditional on support level;
- amount of support needed over time for the same capability;
- retained targets per minute of learning.

## Engagement / usability metrics

Keep separate from learning:

- hint request rate;
- full-translation reveal rate;
- task abandonment;
- session duration;
- confusion/help events.

## Not yet decided

- exact support suppression threshold;
- whether support is learner-requested, automatically adaptive, or hybrid;
- whether S1/S2 order differs by modality;
- exact delay windows;
- whether the same scaffold ladder should apply after Stage 0.
