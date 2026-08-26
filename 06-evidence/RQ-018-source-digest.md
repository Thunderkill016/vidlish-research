---
id: EVD-RQ-018
title: RQ-018 source digest — motivation, useful return, streaks and recovery
status: initial-digest
last_verified: 2026-08-26
---

# RQ-018 source digest

## Research question

Which product/session behaviors increase **useful return and sustained practice** for near-A0 adults without substituting engagement metrics for delayed learning outcomes?

## 1. Motivation quality matters more than raw motivation quantity

### SRC-0183 — Alamer, Robat, Shirvan & Ryan (2025)
A multilevel meta-analysis of self-determination-theory motivation and L2 learning. Intrinsic and identified regulation, and their broader autonomous-motivation factor, were positively associated with L2 achievement. Controlled motivation was not equivalently associated with achievement. Autonomous motivation was also associated with lower language anxiety.

**Nếp implication:** support reasons the learner personally values, plus real competence and agency. Do not assume a larger reward or stronger pressure creates better language learning.

**Limit:** these are associations across studies, not proof that a specific app feature causes achievement.

### SRC-0184 — Al-Hoorie et al. (2022)
Systematic review of 111 empirical L2 studies using self-determination theory over roughly three decades. It confirms a substantial L2 evidence base while also exposing uneven use of SDT mini-theories, constructs and measures.

**Nếp implication:** SDT is useful as a design lens, not a plug-and-play algorithm.

### SRC-0185 / SRC-0186 — general education meta-analyses
Across large education samples, self-determined motivation is associated with adaptive outcomes, and competence, autonomy and relatedness support are important antecedents. Bureau et al. found competence particularly strong as a predictor of self-determined motivation.

**Nếp implication:** a learner should be able to see truthful evidence that they are becoming capable. Fake progress can undermine the very mechanism the product needs.

### SRC-0187 — SDT intervention meta-analysis
Across 36 educational interventions, SDT-based interventions showed benefits for perceived autonomy and competence and some benefits for intrinsic motivation. Relatedness effects were less consistent.

**Nếp implication:** need-support can be designed, but exact mobile-language UX still requires direct validation.

## 2. Engagement is not learning

RQ-018 keeps four outcomes separate:

```text
motivation
engagement / use
persistence / return
learning / retained capability
```

They can influence each other, but none is a valid proxy for all others.

A learner can:
- open the app every day and learn little;
- do one tiny XP-saving activity with no independent retrieval;
- spend a long time because the task is confusing;
- temporarily stop using the app while retaining prior learning;
- return after a break and continue successfully.

Therefore:

```text
DAU ↑
≠
English ability ↑
```

and:

```text
streak ↑
≠
retention ↑
```

## 3. Gamification is a support layer, not a curriculum or evidence model

### SRC-0188 — Sailer & Homner (2020)
Meta-analysis found small positive average effects of gamification on cognitive, motivational and behavioral learning outcomes, with substantial heterogeneity. Motivational and behavioral effects were less stable in stricter methodological subsets.

### SRC-0189 — Li, Hew & Du (2024)
Meta-analysis/systematic review found a small overall effect on intrinsic motivation. Gamification affected autonomy and relatedness more strongly than perceived competence in the included data. The review also describes risks from controlling rewards and unfavorable leaderboard comparison.

### SRC-0190 — Luo (2023), foreign-language learning
Systematic review of 21 empirical FLL studies found mixed positive, null and negative findings, with measurement and design weaknesses common.

**Nếp decision:** XP, badges, streaks, levels and celebrations may be tested as optional motivational supports. They cannot define mastery and cannot be accepted merely because they increase clicks or time-on-task.

## 4. Streaks are behaviorally powerful and therefore need guardrails

### SRC-0191 — Silverman & Barasch (2023; online 2022)
Across seven studies, highlighted intact streaks increased subsequent engagement relative to broken streaks. Importantly, the streak representation itself mattered even when past behavior was held constant. Maintaining the streak became a goal in its own right. Allowing a broken streak to be repaired attenuated the negative post-break effect.

The study set included language-learning-app contexts, which makes the behavioral mechanism especially relevant to Nếp.

But the inference boundary is strict:

```text
streak evidence
→ repeated behavior
```

not:

```text
streak evidence
→ vocabulary retained
→ listening improved
→ speaking transferred
```

A streak may help a learner return. It may also create a second product goal — “do not lose the streak” — that competes with the real goal of improving English.

## 5. Progress monitoring is stronger when the monitored thing matches the real goal

### SRC-0192 — Harkin et al. (2016)
Meta-analysis of 138 randomized studies found that interventions increasing goal-progress monitoring also improved goal attainment on average.

**Nếp implication:** progress feedback is worth using, but it should monitor evidence-linked capabilities whenever possible:

```text
Can understand this changed café request on first listen
Can retrieve "I'd like..." without a model
Can still do it after delay
```

rather than mainly:

```text
Level 12
4,380 XP
32 minutes today
```

The latter may describe activity, not progress toward English capability.

## 6. Self-regulation can be product infrastructure

### SRC-0193 — Xu et al. (2023)
Meta-analysis of self-regulated-learning interventions in online/blended education found positive effects on academic achievement.

Relevant SRL functions for Nếp include:
- choosing a realistic goal;
- planning when/how to study;
- monitoring progress;
- deciding when help is needed;
- reflecting on what worked;
- adjusting future study.

Nếp should scaffold these lightly. A beginner English app should not turn into a project-management tool.

## 7. Dropout is multi-causal; absence is not always final

### SRC-0194 — Rahmani, Groot & Rahmani (2024)
Systematic review of 110 online-higher-education studies identified interacting learner, course, technology, motivational and support factors. The review also notes definitional problems when temporary absence is treated as dropout.

### SRC-0195 — Badali et al. (2022)
Systematic review of 50 MOOC publications found multiple motivational pathways to retention, with satisfaction, self-regulation, performance, engagement and participation acting as related mechanisms.

**Nếp implication:** there is no single retention hack. A missed week can result from workload, product friction, task mismatch or changed life circumstances rather than lack of motivation.

Product state should distinguish:

```text
active
short break
returning
extended break
```

instead of:

```text
active / churned
```

## 8. Proposed construct: useful return

A **return** is product behavior.

A **useful return** is a return that reaches at least one meaningful learning action and stores interpretable evidence.

Candidate:

```text
app/session return
+
meaningful learning/retrieval/review/transfer attempt
+
evidence stored
=
useful return
```

A stronger outcome remains downstream learning:

```text
delayed changed-context capability gain
──────────────────────────────────────
learner minutes
```

Useful return is an intermediate product metric, not the final educational outcome.

## 9. Recovery is part of retention design

A punitive re-entry flow can create unnecessary friction:

```text
You lost your 87-day streak
42 reviews overdue
Start again
```

Candidate Nếp recovery:

```text
BREAK
↓
preserve prior evidence
↓
re-estimate what is actually due
↓
compress backlog
↓
offer one small meaningful action
↓
restore successful momentum
↓
resume normal curriculum gradually
```

This is a product hypothesis supported indirectly by streak/dropout/self-regulation evidence and must be tested in `EXP-018`.

## 10. What RQ-018 does NOT establish

The literature does not establish for Vietnamese near-A0 adults:
- ideal session duration;
- whether daily study is better than flexible weekly consistency for this product;
- ideal reminder time or frequency;
- whether Nếp should show a streak at all;
- how many grace days are useful;
- whether streak repair helps learning rather than only engagement;
- best reward type;
- whether a capability progress bar motivates better than XP;
- how much learner choice is helpful before it becomes decision burden;
- exact reactivation policy after 3, 7, 14 or more absent days;
- the acceptable trade-off between higher return and lower learning quality.

These are `EXP-018` parameters.
