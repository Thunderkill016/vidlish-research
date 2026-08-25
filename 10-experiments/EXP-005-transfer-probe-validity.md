---
id: EXP-005
title: Calibrate cheap changed-context transfer probes
status: proposed
research_question: RQ-005
---

# EXP-005 — Which transfer probe predicts useful later language at acceptable cost?

## Question

For Vietnamese-speaking near-A0 adults, what is the cheapest changed-context probe that predicts later unsupported performance on unseen language better than an exact-context retest?

## Core design

After comparable initial learning, assign matched targets within learner to different probe families.

### A — exact-context retest (`T0`)

```text
same/near-identical cue and response requirement
```

This is the retention baseline, not a transfer condition.

### B — minimal near-transfer probe (`T1`)

```text
one controlled dimension changes
non-target language remains known
```

Example: same construction with a known new object/referent.

### C — parallel-context probe (`T2`)

```text
new situation/surface exemplar
same target communicative relation
known surrounding language
```

### Optional D — controlled productive probe

For targets with enough prerequisites, require short independent production in a new bounded context.

Do not include open conversation as the default first experiment; scoring and construct contamination are too large.

## Delayed criterion

After a pre-registered delay, test all conditions on **new probes not used during training or the earlier probe**.

Use at least two criterion families when feasible:

1. unseen comprehension/selection in a new parallel context;
2. short controlled production for a stratified subset of targets.

For listening targets, include a new speaker/audio exemplar.

## Primary analysis

Compare how well each early probe predicts later criterion success after accounting for:

- prior target knowledge;
- initial training success;
- support level;
- target difficulty;
- probe time.

Primary product metric:

```text
incremental prediction of later unseen success
────────────────────────────────────────────
probe seconds + learner friction
```

A T1 probe can win even if T2 is marginally more predictive, if T1 captures almost the same signal at much lower cost.

## Secondary questions

- Does T0 accuracy substantially overestimate T1/T2 performance?
- Does T2 create excessive failure for the near-A0 subgroup?
- Does productive T1/T2 predict later production better than receptive transfer probes?
- Which novelty dimensions are most informative without creating unrelated difficulty?
- How much does a transfer probe itself improve later learning (testing effect), rather than merely measure it?

## Probe validity checks

For each item, expert/content review should verify:

- target relation preserved;
- changed dimensions correctly labeled;
- no answer leakage;
- non-target vocabulary/grammar within learner evidence;
- plausible distractors;
- one intended interpretation;
- scoring rule aligned to capability.

## Reuse contamination rule

Once a learner sees a probe, set:

```text
probe_first_seen = false
```

for future attempts. It may become a review/training item, but never again counts as the learner's first unseen transfer demonstration.

## Decision rule

Adopt the least burdensome probe family that adds meaningful prediction of later unseen performance over a same-context retention retest.

Do not ship a “transfer score” if:

- exact-context and transfer probes are not empirically distinguishable;
- probe difficulty is dominated by unrelated vocabulary/grammar;
- scoring reliability is poor;
- repeated testing burden crowds out learning.

## Pre-register

- near-A0 inclusion criteria;
- target families and prerequisites;
- exact novelty dimensions for T1/T2;
- delay interval;
- criterion tasks;
- scoring rules;
- support policy;
- minimum worthwhile predictive improvement;
- maximum acceptable probe-time cost;
- missing-session handling;
- exclusion/stopping rules.
