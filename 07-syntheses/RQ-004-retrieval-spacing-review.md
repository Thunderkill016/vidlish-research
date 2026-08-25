---
id: SYN-REV-001
title: Retrieval and spacing policy for the Nếp review engine
status: initial-synthesis
research_question: RQ-004
last_verified: 2026-08-25
---

# RQ-004 — Retrieval, spacing and efficient review

## Decision summary

Nếp should use **attempt-before-reveal retrieval plus adaptive spaced review**, but should not become a flashcard scheduler with language-learning claims attached afterward.

The review system has two separate jobs:

```text
MEMORY SCHEDULER
When is another attempt likely to be useful?

LANGUAGE EVIDENCE ENGINE
What task should be attempted, and what does success actually prove?
```

FSRS or another memory model can help with the first. RQ-001/RQ-003/RQ-005 determine the second.

## Core review loop

```text
initial learning / successful low-support attempt
                ↓
        create review candidate
                ↓
     scheduler proposes due time
                ↓
          item becomes due
                ↓
 evidence engine selects needed task
                ↓
      attempt before answer reveal
                ↓
      ┌─────────┴─────────┐
      ↓                   ↓
independent success      failure
      ↓                   ↓
update evidence       corrective feedback
      ↓                   ↓
update scheduler      relearning / retry
      └─────────┬─────────┘
                ↓
          next useful due time
```

## What the evidence supports

### 1. Space practice across time

`SRC-0003` provides the strongest L2 synthesis in this cycle: spacing improves second-language learning on average, and longer spacing tends to matter more when retention is measured after a delay.

**Product consequence:** Nếp should preserve delayed review even when same-session accuracy looks excellent.

### 2. No magic relative-spacing schedule

The meta-analysis found equal and expanding spacing statistically equivalent overall (`SRC-0003`). Individual L2 studies can favor expanding spacing in particular designs (`SRC-0037`), but that does not justify a universal rule.

**Product consequence:** never encode `1-3-7-14` or “always expand intervals” as a scientific truth. A fixed schedule can be a fallback or experiment baseline, not the knowledge model.

### 3. More retrieval is not free

Within-session repeated retrieval can raise raw retention (`SRC-0004`), but time-normalized efficiency changes the picture.

**Product consequence:** stop overdrilling an item merely to make a mastery meter look safe. The review engine should optimize delayed unsupported performance per minute and move on when the marginal value is low.

### 4. Retrieval task must match the target capability

Recognition, receptive recall and productive recall do not produce identical learning outcomes (`SRC-0038`, plus RQ-001).

For example:

```text
Goal: recognize spoken "borrow"
→ audio recognition / form-meaning task

Goal: retrieve English from meaning
→ productive recall

Goal: use "borrow" in a new request
→ changed-context production task
```

A single generic card cannot be interpreted as all three.

### 5. Retrieval must be difficult enough to retrieve, not impossible

General retrieval-practice synthesis shows robust benefits relative to restudy, but retrieval success matters (`SRC-0040`). Desirable difficulty is not a license to repeatedly test content before the learner has any usable representation.

**Product consequence:** first establish enough access for a meaningful attempt. After failure, teach/correct and retry rather than repeatedly recording hopeless failures.

### 6. Attempt first; feedback can follow promptly

RQ-001 already requires attempt-before-reveal. `SRC-0039` does not support a universal advantage for delaying feedback in L2 vocabulary learning.

**Product consequence:** Nếp can reveal corrective feedback immediately after the scored attempt unless another task-specific reason requires delay. The important boundary is **before vs after the attempt**, not a ritual number of seconds.

### 7. Scheduler state is not mastery

The MaiMemo scheduling work (`SRC-0042`, `SRC-0043`) shows that large-scale review histories can support useful memory prediction and schedule optimization. FSRS (`SRC-0044`) is an engineering implementation in this family.

But the scheduler estimates something like probability of recalling a memory item. It does not observe whether the learner:

- recognized the item in connected speech;
- produced it independently;
- understood it in a message;
- used it in a changed situation;
- retained that other capability.

**Product consequence:** `retrievability`, `stability`, `difficulty`, `due_at` and `mastery/evidence` must never be one object.

### 8. Retrieval can help transfer, but does not certify it

The transfer meta-analysis (`SRC-0041`) finds positive but conditional transfer effects.

**Product consequence:** spaced retrieval is part of the learning mechanism, while `transferred` still requires an actual changed-context probe. This boundary becomes the focus of RQ-005.

## Proposed Nếp architecture

### A. Language evidence state

Owned by the learning/evidence engine:

```text
target_evidence
  learner_id
  target_id
  modality
  evidence_type
  support_level
  task_type
  correctness
  latency
  context_id
  occurred_at
```

### B. Memory scheduling state

Owned by the review scheduler:

```text
review_memory
  learner_id
  target_id
  review_lane
  scheduler_model
  scheduler_version
  due_at
  stability?
  difficulty?
  retrievability?
  last_scheduler_grade
  updated_at
```

The scheduler fields are implementation-specific and nullable. Language evidence is the durable product truth.

### C. Review lane

At minimum, Nếp should be able to distinguish review demand such as:

```text
meaning_recall
spoken_form_access
productive_form_recall
changed_context_use
```

This does **not** require four independent FSRS cards for every word on day one. The task selector can choose the cheapest useful lane from accumulated evidence. The exact data architecture remains an implementation decision.

## Initial scheduler-adapter policy

Nếp should not show learners four Anki-like self-rating buttons by default.

Initial candidate mapping:

```text
independent failure
→ scheduler failure / Again

independent correct attempt
→ scheduler success / Good

answer-bearing hint or reveal required
→ learning/relearning event; not independent success

Hard / Easy
→ leave unused until product data justifies a reliable mapping
```

This mapping is **not** a research fact. It is intentionally conservative so the scheduler cannot turn scaffolded success into strong memory evidence.

## Due-item selection

When several items are due, priority should combine:

1. scheduler urgency;
2. curriculum importance/frequency;
3. weak evidence lane;
4. recent failure/support dependence;
5. session workload budget.

Scheduler urgency alone should not dominate all product decisions.

## Workload and desired retention

Higher target retention generally implies more reviews. The correct product objective is not “maximum retention at any cost.”

Nếp should optimize something closer to:

```text
useful delayed capability gained
────────────────────────────────
review minutes + friction + backlog
```

The exact tradeoff requires `EXP-004`.

## What this changes in Nếp

### `/review`

Should become an adaptive task queue, not a flashcard deck.

A review session can mix:

```text
🔊 spoken recognition
→ meaning recall
→ short production
→ occasional changed-context probe
```

based on what evidence is missing.

### `/progress`

May show durable capability evidence, but should not display FSRS stability as “English mastery.”

### `/start`

A successful new-item retrieval can create the first review candidate. Mere exposure/completion should not.

## Current answer to RQ-004

Use adaptive spaced retrieval, but keep the following invariants:

1. attempt before answer reveal;
2. enough initial learning to permit meaningful retrieval;
3. delayed review instead of massed repetition;
4. no magic interval sequence;
5. no universal expanding-spacing doctrine;
6. task selection tied to language evidence;
7. scheduler state separate from mastery;
8. optimize retained/transferable capability per learner minute;
9. calibrate exact workload and scheduler policy in Nếp itself.

## Open questions handed forward

- RQ-005: which changed-context probe is cheap and valid enough to run repeatedly?
- How should different evidence lanes share or split scheduling state?
- When should a failed due item reappear inside the same session?
- What desired-retention/workload target is acceptable for real Nếp users?
- Does FSRS outperform a simple fixed schedule on Nếp's actual language tasks at matched workload?
