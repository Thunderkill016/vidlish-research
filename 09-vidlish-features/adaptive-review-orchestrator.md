---
id: FEAT-REV-001
title: Adaptive review orchestrator
status: candidate-core
research_question: RQ-004
---

# Feature research spec — Adaptive review orchestrator

## Learner problem

A beginner needs delayed retrieval to retain language, but a generic flashcard scheduler can over-review easy material, test the wrong capability, or turn scheduler predictions into fake mastery claims.

## Target capability

Bring back the right target at a useful time, choose a review task that tests the evidence Nếp actually needs, and keep review workload low enough that the learner can continue the curriculum.

## Research basis

- `SYN-REV-001`
- `CLM-REV-001` through `CLM-REV-010`
- `PRN-031` through `PRN-039`
- RQ-001 lexical evidence model
- RQ-002 support provenance
- RQ-003 aural evidence model

## Architecture

```text
Evidence Engine
     │
     ├── independent attempt evidence
     │
     ▼
Review Candidate Service
     │
     ▼
Scheduler Adapter ─── FSRS / simple fallback
     │
     ▼
Due Queue
     │
     ▼
Task Selector
     │
     ▼
Review attempt
     │
     ├──→ Evidence Engine
     └──→ Scheduler Adapter
```

Scheduler and evidence remain separate modules.

## Required scheduling state

```text
review_memory
  learner_id
  target_id
  review_lane
  scheduler_model
  scheduler_version
  scheduler_params_version?
  due_at
  stability?
  difficulty?
  retrievability?
  last_grade?
  last_review_at?
```

No field above is allowed to mean `mastered`.

## Required review-attempt state

Reuse the canonical attempt/evidence data from RQ-001/RQ-003 and include:

```text
review_id
scheduled_due_at
actual_review_at
review_lane
scheduler_model
scheduler_version

attempt_before_reveal
support_level
support_types[]
correctness
latency

scheduler_grade_derived
scheduler_grade_rule_version
```

The raw attempt must remain available even if the scheduling algorithm changes later.

## Review lanes

Candidate lanes:

- `meaning_recall`
- `spoken_form_access`
- `productive_form_recall`
- `changed_context_use`

Lane names are product taxonomy, not claims of independent cognitive systems.

## Task-selection rules

1. Pick the weakest important evidence that is due and cheap enough for the current session.
2. Prefer recall over recognition when the desired capability requires recall.
3. Use audio-only tasks when refreshing aural evidence.
4. Do not schedule a changed-context task on every review; use it when transfer evidence is due/needed.
5. Never let one easy recognition answer refresh all evidence lanes.

## Initial FSRS adapter

FSRS is an implementation candidate, not a product truth.

Conservative initial mapping:

```text
independent incorrect → Again
independent correct   → Good
hint/reveal needed    → no successful scheduler grade; enter relearning
Hard/Easy             → unused initially
```

The adapter must be versioned so later experiments can change this mapping without corrupting historical evidence.

## Cold start

When the learner does not have enough review history:

- use FSRS default parameters or a simple conservative schedule behind the same adapter;
- do not pretend personalization exists before enough data are available;
- preserve all raw attempts so future parameter optimization can use them.

## Backlog behavior

When due items exceed the session budget:

1. prioritize high-value/high-risk items;
2. avoid showing dozens of overdue cards as learner failure;
3. carry remaining due items forward;
4. record backlog separately from learner capability.

## UX behavior

Learner sees:

```text
Ôn hôm nay · ~6 phút
```

not:

```text
FSRS stability 18.4 days
Retrievability 0.893
```

Those model values are internal diagnostics.

After a failure:

```text
attempt
→ concise correction
→ one useful retry if appropriate
→ continue
```

Do not trap the learner in unlimited same-session repetitions.

## Risks

- review backlog crowds out new language;
- easy recognition tasks inflate scheduler success;
- mapping latency/confidence to Hard/Easy becomes arbitrary;
- per-lane cards multiply review load;
- scheduler upgrades change intervals unexpectedly;
- optimization on engagement may reduce true delayed retention.

## Falsification

This feature is not justified if an adaptive scheduler plus evidence-aware task selection fails to improve delayed unsupported capability per review minute compared with a simpler schedule.

## Learning metrics

Primary:

- delayed unsupported recall;
- aural recognition where relevant;
- changed-context performance where sampled;
- retained targets per review minute.

Guardrails:

- review minutes/day;
- backlog size/age;
- support dependence;
- repeated-failure rate;
- abandonment during review.
