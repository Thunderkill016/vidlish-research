---
id: SYN-MOT-001
title: Useful return, motivation and recovery without engagement worship
status: initial-synthesis
research_question: RQ-018
last_verified: 2026-08-26
---

# RQ-018 — Useful return, motivation and recovery

## Decision summary

Nếp should optimize for **sustained useful learning**, not maximum app use.

The intended chain is:

```text
learner-valued reason
+ achievable next action
+ truthful competence feedback
+ enough autonomy
↓
useful return
↓
meaningful learning / retrieval / review
↓
independent evidence
↓
delayed changed-context evidence
↓
visible real progress
↓
next useful return
```

The system must explicitly reject:

```text
streak / XP / minutes / opens
→ mastery
```

## Product objective hierarchy

### Level 1 — educational outcome

```text
delayed changed-context capability gain
```

This remains the strongest target.

### Level 2 — learning efficiency

```text
delayed changed-context capability gain
──────────────────────────────────────
learner minutes
```

### Level 3 — useful return

A return that reaches an interpretable learning action:

```text
return
+
meaningful learning / retrieval / review / transfer attempt
+
evidence stored
```

### Level 4 — participation telemetry

Examples:
- app open;
- session count;
- DAU / WAU;
- streak length;
- XP;
- content viewed;
- time spent;
- notification click.

These are useful for diagnosing product behavior but are not educational outcomes.

## Motivation quality

L2 meta-analytic evidence (`SRC-0183`, `SRC-0184`) supports distinguishing more autonomous motivation from controlled motivation.

Nếp should strengthen three conditions where possible:

### Competence
The learner experiences:

```text
I can do something today that I could not reliably do before.
```

Competence feedback should come from real evidence:
- fewer supports;
- independent retrieval;
- changed-context success;
- delayed success;
- improved first-pass listening;
- successful interaction.

### Autonomy
The learner has meaningful but bounded control:
- preferred learning times;
- reminder settings;
- some scenario choice;
- pause/resume choice;
- explanation/help request;
- optional gamification settings where feasible.

Autonomy does not mean dumping the whole curriculum decision on a beginner.

### Relatedness
Potential supports include:
- supportive tutor/coach voice;
- interaction with people/AI where pedagogically valid;
- optional social accountability;
- shared goals.

The evidence does not justify making a social network a core requirement.

## Competence must be truthful

A progress system that says:

```text
You are amazing — +500 XP!
```

while the learner still cannot understand or retrieve the target can produce activity without useful competence information.

Prefer:

```text
Yesterday: needed Vietnamese meaning + model
Today: understood the new request without translation
Next: retrieve the response without a model
```

The progress UI should answer:

```text
What can I now do?
What evidence supports that?
What is the next obstacle?
```

## Progress monitoring

`SRC-0192` supports progress monitoring as a general self-regulation tool.

For Nếp, the monitored variable should be close to the learner's goal.

Candidate progress hierarchy:

```text
CAPABILITY
  Can order a simple drink

EVIDENCE
  ✓ understand changed café requests
  ✓ retrieve "I'd like..." without model
  △ delayed interaction evidence incomplete

NEXT
  answer one follow-up question
```

Activity telemetry can remain in secondary views.

## Self-regulated learning without turning Nếp into homework administration

RQ-018 adopts a lightweight cycle:

```text
FORETHOUGHT
choose realistic target / routine
↓
PERFORMANCE
learn + monitor support/friction
↓
REFLECTION
show what changed and what still fails
↓
ADAPT
schedule next useful action
```

The learner should not have to create elaborate study plans.

The app can do most orchestration while exposing enough choice and rationale to preserve agency.

## Gamification policy

Gamification is permitted only as a **support layer**.

Allowed candidate functions:
- celebrate real evidence milestones;
- make repetition less dull;
- make progress visible;
- add optional collection/achievement goals;
- support cooperative or self-comparison challenges.

Not allowed as evidence:

```text
XP ↑
→ word known
```

```text
badge earned
→ speaking mastered
```

```text
leaderboard rank ↑
→ English improved
```

### Leaderboards

Because social comparison can damage perceived competence for low-ranked learners, absolute public rankings should not be the default beginner experience.

Safer candidates to test:
- compare with own prior evidence;
- cooperative goals;
- opt-in friend groups;
- capability milestones rather than raw minutes/XP.

## Streak policy

Streaks are behavior mechanisms, not learning models.

If Nếp uses a streak, it should represent something like:

```text
consecutive periods with useful practice
```

not:

```text
consecutive days of English mastery
```

### The streak problem

`SRC-0191` shows that a highlighted streak can become a goal itself.

That gives two goals:

```text
Goal A: improve English
Goal B: keep streak alive
```

If B wins, the learner may choose a trivial action only to protect the streak.

Candidate anti-gaming rule:

```text
open app
+ tap easy item
+ no interpretable evidence
≠ useful-learning continuity
```

Exact qualifying criteria remain experimental.

## Missed day / broken streak

Do not use:

```text
You failed.
87-day streak lost.
Start at day 1.
```

Candidate handling:

```text
You missed some practice.
Your learning progress is still here.
Here is the smallest useful next step.
```

If a continuity mechanic is retained, candidates include:
- grace windows;
- streak repair;
- weekly consistency rather than perfect daily continuity;
- personal target such as 4 useful sessions/week;
- separate “practice continuity” from capability progress.

`EXP-018` decides whether any of these create better learning, not merely higher retention.

## Multiple-lives learner model

A learner should be able to cycle through:

```text
ACTIVE
↓
SHORT_BREAK
↓
RETURNING
↓
ACTIVE
```

or:

```text
ACTIVE
↓
EXTENDED_BREAK
↓
REASSESS
↓
RETURNING
```

A break must not delete:
- attempt history;
- retained evidence;
- capability history;
- learner preferences.

But stale evidence should be re-probed where relevant.

## Re-entry after a break

The worst return experience is a punishment wall:

```text
47 overdue reviews
6 unfinished lessons
streak = 0
```

Candidate recovery policy:

1. Estimate what evidence has become stale.
2. Do not replay every missed scheduled review.
3. Sample high-value / uncertain targets.
4. Offer one short action with a high probability of meaningful success.
5. Use results to rebuild the review queue.
6. Resume curriculum progressively.

This connects RQ-018 to:
- `FEAT-REV-001` review scheduling;
- `FEAT-CUR-001` curriculum orchestration;
- `FEAT-VOC-001` and other evidence engines.

## Reminder policy

Reminders are cues, not proof of motivation.

Candidate properties:
- user can turn them off;
- learner can choose preferred window;
- copy focuses on the next useful action rather than guilt;
- repeated ignore events reduce frequency or trigger preference reset;
- after a break, reminder copy emphasizes easy re-entry;
- notification click and useful-return completion are recorded separately.

Example distinction:

```text
notification_sent
notification_opened
session_started
useful_action_completed
learning_evidence_created
```

Do not optimize only `notification_opened`.

## Session size

RQ-018 does not justify one scientific session length.

The system should support at least two product states:

### Minimum useful session
When time/energy is constrained:
- one valid retrieval/review/transfer action;
- small enough to complete;
- not fake progress.

### Normal learning session
Enough time for a fuller learning loop.

A 90-second session can be educationally useful if it contains valid retrieval; a 20-minute session can be useless if it is passive clicking.

## Friction and workload

Return failure can come from:
- too much overdue work;
- tasks above readiness;
- repetitive low-value practice;
- slow UI;
- unclear instructions;
- excessive notifications;
- emotional pressure from streak loss;
- life constraints.

Therefore the learner model should record friction signals rather than interpreting every absence as low motivation.

Candidate signals:

```ts
type ReturnFriction = {
  abandonedSessions: number;
  ignoredReminders: number;
  repeatedHelpRequests: number;
  overdueQueueSize: number;
  taskFailureBurst: number;
  supportEscalation: number;
  optionalPressureRating?: number;
};
```

## Useful-return state

```ts
type LearningReturnState = {
  lastUsefulLearningAt?: string;
  daysSinceUsefulLearning: number;
  breakState: "active" | "short_break" | "returning" | "extended_break";

  currentReviewLoad: number;
  recentIndependentEvidenceGain: number;
  recentDelayedEvidenceGain: number;

  learnerPreferredWindow?: string;
  reminderEnabled: boolean;
  reminderResponseHistory: ReminderResponse[];

  friction: ReturnFriction;
};
```

This state must not contain:

```text
motivation = low
```

as a confident inference merely because the learner missed sessions.

## Core orchestration rule

```text
What is the smallest next action
that is feasible now
and still creates useful learning evidence?
```

The answer may be:
- delayed retrieval of one important chunk;
- one short first-pass listening probe;
- one changed-context response;
- a short review sample after a break;
- a normal new-learning session if readiness/time allows.

## Product decision

Create `FEAT-MOT-001` — **Useful-return and recovery orchestrator**.

It should:
- keep learning outcomes above engagement outcomes;
- calculate useful return separately from app return;
- expose truthful capability progress;
- support competence/autonomy without fake praise;
- treat gamification as optional/supportive;
- treat streaks only as continuity signals;
- provide grace/recovery rather than punishment;
- preserve multiple-lives re-entry;
- compress overdue queues after absence;
- use lightweight goal/self-monitoring support;
- adapt reminder cadence from learner control and response history;
- log engagement and learning metrics separately.

## Strong falsification condition

If an engagement feature increases:

```text
DAU / streak / session count
```

but does not improve, or worsens:

```text
delayed changed-context capability gain per learner minute
```

then it must not be justified as an educational feature.

It may still be a business/entertainment feature, but that distinction must be explicit.

## Open assumptions

- minimum evidence required for a return to count as useful;
- ideal session length distribution;
- reminder cadence and timing;
- reminder suppression after ignored prompts;
- whether Nếp should show a streak;
- daily versus weekly continuity;
- grace/repair rules;
- capability-progress UI;
- reward type and frequency;
- social/leaderboard policy;
- break-state thresholds;
- overdue review compression algorithm;
- easiest valid re-entry task;
- amount of learner choice;
- short self-reflection frequency;
- acceptable engagement-learning trade-offs.

All remain `EXP-018` variables.
