---
id: FEAT-MOT-001
title: Useful-return and recovery orchestrator
status: research-backed-candidate
research_question: RQ-018
synthesis: SYN-MOT-001
experiment: EXP-018
---

# FEAT-MOT-001 — Useful-return and recovery orchestrator

## Learner problem

An English product fails if learners do not return often enough to retrieve, review and transfer what they learned. But it also fails if it maximizes streaks, XP and screen time while learners do not retain usable English.

Nếp therefore needs a return system whose unit of value is **useful learning**, not app activity.

## Core invariant

```text
engagement metric
≠
learning evidence
```

No return, streak, XP event, notification click, session duration or badge can directly set a capability to mastered.

## Target outcome

The learner returns often enough to receive appropriately spaced learning opportunities and, after returns and breaks, continues generating independent, changed-context and delayed evidence efficiently.

## Inputs

```ts
type ReturnOrchestratorInput = {
  learnerId: string;
  now: string;

  evidenceState: EvidenceState;
  reviewState: ReviewState;
  curriculumState: CurriculumState;

  lastUsefulLearningAt?: string;
  recentSessions: SessionTrace[];
  reminderPreferences: ReminderPreferences;
  reminderHistory: ReminderEvent[];

  continuityPreference?: "off" | "daily" | "weekly";
  breakState: "active" | "short_break" | "returning" | "extended_break";
};
```

## Useful return contract

```ts
type UsefulReturnEvent = {
  sessionId: string;
  returnedAt: string;
  meaningfulAttemptCount: number;
  evidenceIds: string[];
  minutes: number;
  reviewDebtBefore?: number;
  reviewDebtAfter?: number;
};
```

Candidate rule:

```ts
const usefulReturn =
  meaningfulAttemptCount > 0 &&
  evidenceIds.length > 0;
```

Exact qualifying evidence belongs to `EXP-018`.

Examples that may qualify:
- delayed meaning recall;
- changed-context listening comprehension;
- controlled production without visible answer;
- pronunciation attempt with valid evidence gate;
- review retrieval;
- short transfer probe.

Examples that do not qualify by themselves:
- opening Today;
- watching an animation;
- collecting XP;
- reading a motivational quote;
- tapping “streak saved”;
- passively replaying material with no interpretable task.

## Objective stack

### Primary learning metric

```text
delayed changed-context capability gain
──────────────────────────────────────
learning minutes
```

### Co-primary product metric

```text
useful-return probability
```

at relevant horizons, e.g. D1 / D7 / D30 or individualized intervals.

### Recovery metric

```text
P(useful return within window | prior break)
```

### Guardrails
- delayed learning quality;
- independent evidence proportion;
- session abandonment;
- notification disable / ignore rate;
- learner pressure/annoyance samples;
- trivial streak-saving sessions;
- review debt;
- task difficulty collapse.

## Separate telemetry domains

```ts
type EngagementTelemetry = {
  appOpens: number;
  sessions: number;
  minutes: number;
  streak?: number;
  xp?: number;
  notificationOpens: number;
};

type LearningTelemetry = {
  independentAttempts: number;
  changedContextAttempts: number;
  delayedAttempts: number;
  evidenceGain: number;
  capabilityGain: number;
};
```

Never combine these into an opaque “engagement/mastery score.”

## Progress experience

The default progress surface should foreground capabilities and evidence.

Example:

```text
ORDER A DRINK

✓ Understand a simple changed café request
✓ Say “I'd like...” without a model
△ Handle a follow-up question after a delay

Next useful step: one short follow-up exchange
```

Secondary analytics may show:
- practice days;
- time;
- XP;
- completed sessions.

But those must not visually overpower capability evidence.

## Competence support

The engine should select actions likely to be challenging enough to matter but feasible enough to produce a credible success signal.

```text
too easy
→ trivial activity / fake competence

appropriate
→ evidence-producing success or diagnostic failure

too hard
→ repeated failure / friction / avoidance
```

Reuse readiness and support policies from other Nếp engines.

## Autonomy support

Learner-controlled settings should include where feasible:
- reminder on/off;
- preferred study window;
- continuity display on/off;
- some scenario choice;
- pause today / resume later;
- ask for explanation/support.

Do not ask the learner to manually plan the entire curriculum.

## Gamification adapter

Gamification should consume learning events rather than create learning truth.

```ts
function awardCelebration(event: EvidenceEvent) {
  // cosmetic/motivational output only
  // cannot mutate mastery state
}
```

Candidate reward triggers:
- first independent retrieval;
- first changed-context success;
- delayed retention success;
- completed useful-return week;
- recovered after a break.

Avoid rewarding only volume if it invites low-value repetition.

## Streak adapter

If enabled:

```ts
type ContinuityState = {
  mode: "daily" | "weekly";
  qualifyingUsefulReturns: string[];
  currentRun: number;
  graceAvailable?: boolean;
};
```

### Streak eligibility

A qualifying event should require a useful return, not an app open.

Candidate:

```text
at least one valid evidence-producing action
```

### Streak label

Use language like:

```text
Practice continuity
```

not:

```text
Mastery streak
English level streak
```

### Broken continuity

Never erase learning progress.

```text
continuity run resets/repairs
≠
capability evidence resets
```

Candidate grace/repair policies are experimental.

## Detect token sessions

A risk signal:

```ts
type TokenSessionRisk = {
  sessionSeconds: number;
  evidenceProduced: boolean;
  repeatedLowestDifficulty: boolean;
  streakWasNearDeadline: boolean;
};
```

If many sessions preserve continuity without producing useful evidence, the streak design is gaming the learner/product rather than helping learning.

## Break-state detection

Do not infer psychology from absence alone.

Candidate operational states:

```text
ACTIVE
recent useful practice

SHORT_BREAK
missed expected practice window(s), evidence still mostly current

RETURNING
first useful session after a break

EXTENDED_BREAK
enough time has passed that selected evidence should be re-probed
```

Exact day counts are not hard-coded scientific truths.

## Recovery planner

```ts
type RecoveryPlan = {
  staleEvidenceSample: string[];
  firstAction: LearningAction;
  compressedReviewSet: string[];
  deferredReviewSet: string[];
  newContentAllowed: boolean;
};
```

Candidate algorithm:

```text
1. preserve history
2. identify high-value / uncertain evidence
3. sample rather than replay every overdue review
4. choose a small feasible first action
5. update state from actual performance
6. rebuild queue
7. re-enter normal curriculum
```

## Overdue queue compression

Never present every missed review as debt that must be paid in chronological order.

Possible policy:

```text
47 overdue targets
↓
select representative/high-value/high-uncertainty probes
↓
8 sampled probes
↓
re-estimate retained state
↓
rebuild next queue
```

Reuse `FEAT-REV-001` scheduling logic; RQ-018 governs UX/return behavior, not memory scheduling theory.

## Minimum useful session

The orchestrator should always be able to request a short action for low-time states.

Candidate classes:

```text
30–120 sec: one retrieval/probe
2–5 min: compact review cluster
normal: full learning loop
```

These durations are product hypotheses, not validated thresholds.

Crucially:

```text
short + valid evidence
>
long + passive activity
```

## Reminder policy

```ts
type ReminderPreferences = {
  enabled: boolean;
  preferredWindows: string[];
  maxPerWeek?: number;
  quietHours?: string;
};

type ReminderEvent = {
  sentAt: string;
  openedAt?: string;
  usefulReturnAt?: string;
  ignored: boolean;
  messagePolicyId: string;
};
```

Candidate adaptive behavior:
- respect opt-out immediately;
- prefer learner-selected windows;
- lower cadence after repeated ignored notifications;
- avoid escalating guilt language;
- after breaks, invite the smallest useful action;
- separate reminder-open success from learning success.

## Copy principles

Prefer:

```text
A 2-minute review is ready. Continue from where you are.
```

or:

```text
Your progress is still here. Check what you still remember.
```

Avoid default coercive framing:

```text
Don't ruin your streak!
You're falling behind!
You failed yesterday!
```

Exact copy effects must be tested.

## Lightweight self-regulation

### Goal

```text
This week: handle a simple café order without a model.
```

### Plan

```text
Preferred rhythm: 4 short useful sessions this week.
```

### Monitor

```text
2/3 capability evidences currently demonstrated.
```

### Reflect

Occasionally ask one low-friction question when informative:

```text
What made today's practice harder?
- time
- task too hard
- audio hard to hear
- not interested
- other
```

Do not survey every session.

## Interaction with FEAT-CUR-001

`FEAT-MOT-001` answers:

```text
How do we get the learner into a useful next learning action?
```

`FEAT-CUR-001` answers:

```text
What capability/action should be next educationally?
```

The return orchestrator must not override curriculum prerequisites merely to produce a fun/easy session.

## Interaction with FEAT-REV-001

Review provides due/uncertain targets.
Return orchestration determines how much work is feasible now and how to present/recover it.

## Interaction with Evidence Engine

Only domain learning engines create learning evidence.

```text
FEAT-MOT-001
→ requests action
→ learner attempts
→ domain engine evaluates
→ Evidence Engine stores
→ FEAT-MOT-001 receives outcome summary
```

It cannot create evidence from a retention event.

## Progress state example

```ts
type UsefulReturnState = {
  lastUsefulLearningAt?: string;
  usefulReturns7d: number;
  usefulReturns30d: number;

  breakState: "active" | "short_break" | "returning" | "extended_break";
  reviewLoad: number;

  independentEvidenceGain7d: number;
  delayedEvidenceGain30d: number;

  continuity?: ContinuityState;
  reminderPreferences: ReminderPreferences;

  ignoredReminderStreak: number;
  tokenSessionRisk: number;
  abandonmentRisk: number;
};
```

## User-facing progress rule

Do not display a universal composite such as:

```text
Motivation 78/100
Engagement 92/100
```

unless a validated user benefit emerges.

Prefer actionable facts:

```text
You practiced meaningfully 3 times this week.
Two capabilities still held up on delayed checks.
One listening target needs another review.
```

## Failure modes

### Engagement worship
Product team celebrates DAU while delayed learning is flat.

### Streak gaming
Learners repeatedly choose trivial tasks near midnight.

### Notification addiction
More pushes increase opens but not useful returns and drive opt-outs.

### Punitive debt
Returning learners face a huge overdue queue and leave again.

### Fake competence
XP/celebrations tell learners they are improving despite weak independent evidence.

### Autonomy overload
Too many choices force near-A0 learners to design their own curriculum.

### Easy-mode retention
System avoids meaningful difficulty because harder tasks reduce session completion.

## Falsification

Weaken, redesign or remove a retention mechanic if it:
- increases app opens but not useful returns;
- increases useful returns but not delayed learning;
- reduces delayed gain per minute;
- produces token sessions;
- increases notification opt-out or reported pressure materially;
- causes learners to avoid useful challenge;
- makes return after a break less likely;
- performs no better than a simpler neutral reminder/progress system.

## Experiment

See `EXP-018`.
