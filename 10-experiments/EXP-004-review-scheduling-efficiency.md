---
id: EXP-004
title: Calibrate adaptive review scheduling efficiency
status: proposed
research_question: RQ-004
---

# EXP-004 — Adaptive scheduling vs a simple fixed schedule

## Question

For Vietnamese-speaking near-A0 adults, does adaptive memory scheduling improve **delayed unsupported English performance per review minute** enough to justify its complexity?

## Design

Assign comparable newly learned targets within learner to two scheduling policies while keeping teaching content and review task family matched.

### A — simple fixed schedule

Use a transparent fixed schedule chosen before the experiment (for example a short sequence of day-scale intervals). It is a baseline, not a claim that the sequence is optimal.

### B — adaptive scheduler

Use the current pinned scheduler adapter (initial candidate: FSRS) from the same first valid independent retrieval.

Both conditions:

- use attempt-before-reveal;
- use the same evidence-aware task selector;
- record support provenance;
- impose comparable session workload limits;
- do not expose algorithm names to the learner.

## Primary outcomes

At pre-registered delayed checkpoints, without answer-bearing support:

- target recall appropriate to the learned capability;
- aural recognition for sampled spoken targets;
- retained targets per cumulative review minute.

## Secondary outcomes

- total review attempts;
- review backlog;
- failure rate when due;
- learner return rate for due reviews;
- support/relearning events;
- sampled changed-context performance;
- curriculum progress displaced by review workload.

## Scheduler calibration sub-study

For adaptive items, compare candidate desired-retention/workload settings only after enough review data exist. Do not change both scheduling algorithm and desired-retention target in the same primary comparison unless the design explicitly models the interaction.

## Grade-mapping validation

Initial mapping uses independent incorrect → `Again`, independent correct → `Good`.

Before enabling `Hard/Easy`, test whether candidate signals such as latency, confidence or partial errors actually predict later recall after controlling for correctness and support.

## Decision rule

Prefer the simplest policy that achieves the best useful delayed performance at acceptable workload.

Adaptive scheduling should not ship merely because it predicts card recall more accurately in an external benchmark. It must improve Nếp's own language-learning objective or materially reduce review cost.

## Pre-register

- definition of near-A0;
- target sampling and difficulty balance;
- fixed-schedule baseline;
- pinned scheduler/version/parameters;
- delayed evaluation horizon;
- primary capability probe;
- workload cap;
- minimum worthwhile learning/time improvement;
- missing-review handling;
- stopping/exclusion rules.
