---
id: FEAT-A0-001
title: A0 learning loop
status: candidate-core
---

# Feature research spec — A0 learning loop

## Learner problem

A learner near A0 has too little language to benefit from open conversation or difficult authentic media, but passive exposure alone does not provide useful evidence of learning.

## Target capability

Understand one small message, retrieve/use part of it with reduced support, handle a changed context, and return after a delay.

## Research basis

- `SYN-FND-001` initial learning model.
- `SYN-LIS-001` listening model.
- `SYN-VOC-001` retrieval + spacing.
- `SYN-TRN-001` changed-context transfer policy.
- `FEAT-TRN-001` graduated transfer probes.
- `PRN-001` through `PRN-005`, plus `PRN-040` through `PRN-049` for transfer interpretation.

## Proposed behavior

```text
1. learner sees/hears a bounded context
2. learner attempts meaning
3. support reveals only as needed
4. one useful target is noticed
5. learner retrieves target without full model
6. learner handles an unseen, bounded changed-context variant
7. system stores evidence by dimension
8. item returns later based on scheduling + evidence
```

## Risks

- Too much task switching can overload a true beginner.
- “Changed context” may accidentally test puzzle-solving, unknown non-target language or interface novelty rather than transfer.
- Support may fade too quickly or too slowly.
- Review volume may become burdensome.

## Falsification

The feature assumption weakens if real target learners cannot understand the flow, show no delayed gain over a simpler comparison, or abandon sessions due to friction.

## Learning metrics

- comprehension accuracy on unseen parallel item;
- unsupported recall rate;
- changed-context performance;
- delayed retention.

## Engagement metrics (separate)

- first-session completion;
- time-on-task;
- return for due review;
- voluntary continuation.
