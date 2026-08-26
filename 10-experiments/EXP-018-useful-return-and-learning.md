---
id: EXP-018
title: Useful return, recovery and learning-quality experiment
status: candidate
research_question: RQ-018
feature: FEAT-MOT-001
---

# EXP-018 — Useful return, recovery and learning quality

## Question

Which return-support policy increases sustained **useful return** and delayed changed-context English learning for Vietnamese adults near A0/A1 without creating streak-saving behavior, excessive pressure or lower learning quality?

## Why this experiment exists

A product can easily win the wrong metric:

```text
DAU ↑
streak ↑
minutes ↑
```

while:

```text
delayed recall = flat
transfer = flat
learning efficiency ↓
```

RQ-018 therefore tests product retention and learning in the same experiment.

## Population

Initial target:
- Vietnamese-speaking adults;
- near A0 / early A1 according to Nếp entry evidence;
- self-directed/mobile-friendly learning context;
- enough onboarding data to select comparable initial capabilities.

Exact inclusion/exclusion criteria and sample size must be preregistered before launch.

## Design

Prefer randomized assignment with capability/evidence baselines.

Candidate 4-arm design:

### A — Minimal neutral support
- capability-based Today queue;
- no visible streak;
- minimal neutral reminder policy;
- ordinary progress evidence.

Purpose: low-mechanic baseline.

### B — Daily streak baseline
- daily visible streak;
- standard daily reminder;
- conventional streak celebration;
- no special break-recovery system beyond ordinary queue.

Purpose: test a common engagement design directly rather than assuming its value.

### C — Capability progress + self-regulation
- no punitive streak;
- capability/evidence progress foregrounded;
- learner selects preferred practice window/rhythm;
- lightweight weekly goal;
- adaptive reminder within preferences.

Purpose: test competence/autonomy/progress support without streak pressure.

### D — Recovery-first adaptive return
Includes C plus:
- optional soft continuity / weekly consistency;
- missed-session grace rather than failure framing;
- explicit break states;
- overdue review compression;
- smallest-valid-action re-entry;
- reminder frequency reduction after repeated ignore;
- recovery copy after absence.

Purpose: test the full `FEAT-MOT-001` candidate policy.

## Learning content control

Across conditions:
- same curriculum graph;
- same eligible capability pool;
- same domain learning engines;
- same review theory;
- same evidence rules;
- comparable task difficulty/readiness policies.

Do not let condition B receive easier content merely because a streak mechanic exists.

## Duration

Candidate minimum:

```text
4–8 weeks active study
+
post-period delayed probes
```

Reason: a one-session experiment can measure motivation reaction but cannot meaningfully test return/recovery dynamics.

Exact duration requires power analysis and operational feasibility.

## Primary outcomes

### P1 — delayed changed-context learning efficiency

```text
delayed changed-context evidence gain
────────────────────────────────────
learning minutes
```

This prevents a high-retention arm from winning simply by consuming more learner time.

### P2 — useful-return rate

At preregistered horizons:

```text
P(useful return by next expected opportunity)
P(useful return in 7 days)
P(useful return in 30 days)
```

A useful return requires meaningful evidence-producing learning action according to the experiment contract.

### P3 — break recovery

For learners who experience a preregistered absence window:

```text
P(useful return within X days after break)
```

and:

```text
quality of first post-break evidence
```

## Learning-quality outcomes

Report separately:
- independent recall;
- changed-context comprehension/use;
- delayed evidence;
- support dependence;
- review retention;
- first-pass listening where relevant;
- capability completion based on evidence.

Do not collapse everything into one posttest if the construct is multi-dimensional.

## Engagement outcomes

Secondary:
- app returns;
- useful returns;
- session count;
- learner minutes;
- continuity/streak length where applicable;
- notification opens;
- notification → useful-return conversion;
- voluntary retries.

These cannot override a learning-quality failure.

## Token-session detector

A key adversarial outcome.

Candidate token session:

```text
session near streak deadline
+
very short duration
+
lowest-available challenge / repeated trivial task
+
no meaningful evidence gain
```

Measure:

```text
token sessions / active learner
```

and compare especially B vs C/D.

The exact classifier must be preregistered and validated before interpretation.

## Break definitions

Do not use one universal definition without sensitivity analysis.

Candidate operational windows:
- short break: missed 2–3 expected opportunities;
- medium break: ~7 days without useful learning;
- extended break: ≥14 days without useful learning.

Use both expectation-relative and calendar-time analyses where feasible.

## Recovery outcomes

After a break measure:
- re-entry session start;
- first useful action completion;
- first post-break independent evidence;
- re-abandonment within same session;
- time to next useful return;
- review backlog presented vs actually needed;
- delayed learning after recovery.

## Reminder outcomes

For each reminder:

```text
sent
opened
session_started
useful_return
learning_evidence
```

Compare conversion funnels.

A reminder policy that increases opens but not useful return has not shown educational value.

## Pressure / autonomy guardrails

Sample brief measures rather than asking every session.

Candidate items:
- “I felt pressured to open Nếp even when I did not want to.”
- “I could fit Nếp around my life.”
- “The progress shown felt like real English progress.”
- “I wanted to continue because the learning felt useful.”

Also track:
- reminder opt-out;
- notification disable;
- continuity feature disable;
- uninstall where observable/ethical;
- negative feedback.

## Competence guardrail

Compare perceived capability progress with actual evidence progress.

Potential miscalibration:

```text
perceived progress ↑↑
actual delayed evidence ↔
```

This would indicate motivational inflation rather than truthful competence support.

## Hypotheses

### H1
Capability/evidence progress with lightweight autonomy support (C/D) will produce at least comparable useful return to a daily streak baseline while improving the alignment between perceived progress and actual learning evidence.

### H2
Recovery-first policy D will improve useful re-entry after breaks relative to A/B, particularly by reducing first-return abandonment and backlog friction.

### H3
Daily streak condition B will produce more continuity-preserving sessions than A, but may also produce more token sessions.

### H4
No arm should be considered superior unless delayed changed-context learning efficiency is non-inferior at minimum and preferably superior.

These are product hypotheses, not claims established by the literature.

## Decision rule framework

### Promote D toward product default if
- useful-return rate improves materially;
- break recovery improves materially;
- delayed changed-context gain/minute is non-inferior or better;
- no material rise in pressure/annoyance;
- token-session rate is low;
- reminder opt-out is acceptable.

### Keep simpler C if
D adds complexity but produces no meaningful improvement in recovery or learning.

### Keep or use streak only selectively if
B improves useful return without:
- token-session inflation;
- worse break recovery;
- worse learning efficiency;
- excessive pressure;
- distorted progress perception.

### Remove or demote streak if
it mostly improves raw returns/opens while learning and recovery do not improve.

## Analysis plan requirements

Preregister:
- sample size / power;
- randomization unit;
- proficiency criteria;
- expected-study-opportunity definition;
- useful-return definition;
- token-session classifier;
- break windows;
- reminder policies;
- delayed-probe timing;
- minimum non-inferiority learning margin;
- missing-data treatment;
- attrition analysis;
- multiple-comparison policy;
- subgroup tests, if any.

## Important subgroups

Only analyze if powered/predeclared:
- learner-chosen daily vs flexible rhythm;
- high vs low initial self-regulation;
- work/time constraint levels;
- initial motivation quality;
- true near-A0 vs early-A1;
- notification enabled vs disabled.

Avoid post-hoc personalization stories from underpowered slices.

## Instrumentation contract

Minimum events:

```text
session_opened
learning_action_started
learning_action_completed
evidence_created
useful_return_completed
reminder_sent
reminder_opened
continuity_qualified
continuity_broken
continuity_repaired
break_state_entered
recovery_plan_created
recovery_action_completed
```

Every event needs policy/version identifiers so later changes remain analyzable.

## Falsification

`FEAT-MOT-001` is too complex or wrong if:
- simpler neutral support has equal learning and return;
- adaptive reminders do not outperform learner-set static reminders;
- recovery compression harms retention by skipping valuable review;
- capability progress does not help useful return;
- streak/grace policy dominates recovery-first design without learning harm;
- useful-return definition fails to predict downstream delayed learning;
- pressure/annoyance costs exceed retention benefit.

## Core experiment principle

```text
Retention is valuable
only when it repeatedly brings the learner
back into evidence-producing learning.
```
