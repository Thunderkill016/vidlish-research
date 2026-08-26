# Nếp v1 — Implementation slices

**Status:** build handoff  
**Purpose:** turn the integrated research architecture into an order of implementation that produces a usable product early without building all 21 research areas at once.

## Build principle

Do not build feature-by-feature in research order.

Build **vertical learning slices** that exercise the shared runtime:

```text
content
→ task
→ support
→ attempt
→ evidence
→ next decision
```

A vertical slice is only useful when a real learner can complete it end-to-end and the system stores interpretable evidence.

## Slice 0 — Runtime invariants and fixtures

Before polished UI, encode the rules most likely to be accidentally violated.

### Required

- stable IDs for capability, target, task spec and policy versions;
- evidence-event schema;
- support-event schema;
- independent-attempt flag;
- novelty/trained/changed-context field;
- scorer provenance;
- `NOT_OBSERVED` distinct from weak/failure;
- decision-reason logging.

### Test fixtures

Create automated fixtures for at least:

1. visible answer before response → cannot emit independent recall;
2. post-reveal retry → original failed attempt remains;
3. exact repeated item → cannot emit transfer by default;
4. no delayed interval → cannot emit retention;
5. transcript visible before answer → cannot emit unsupported listening comprehension;
6. untested speaking → stays not observed;
7. ASR confidence alone → cannot emit pronunciation mastery;
8. session completion → cannot emit language evidence by itself.

### Done when

The code can reject invalid evidence creation before a real course exists.

## Slice 1 — Domain skeleton + one deterministic capability

Use one tiny capability to prove the runtime.

Candidate:

```text
CAP-IDENTITY-001
Can say their name and understand a simple "What's your name?" prompt.
```

Build:

- capability definition;
- minimal targets;
- one listening input;
- one meaning check;
- one independent spoken/text fallback retrieval task;
- support event;
- one changed-context parallel variant;
- evidence viewer/debug trace.

No AI required.

### Done when

A developer can inspect one session and answer:

```text
why this task
what support appeared
what learner attempted
what evidence was emitted
what changed in learner state
```

## Slice 2 — Capability graph + first content set

Add a small set, not a whole A1 course.

Candidate eight-capability product slice:

1. greet and say name;
2. understand/respond to a bounded wellbeing greeting;
3. ask for one familiar item;
4. order a drink + answer size choice;
5. understand a simple price;
6. say a basic need/problem;
7. ask for repetition/clarification;
8. understand/respond to one short everyday message.

For each capability author:

- can-do;
- scenarios;
- prerequisites;
- vocabulary/chunks;
- construction targets;
- listening targets;
- pronunciation risk targets when relevant;
- first exposure;
- independent retrieval;
- changed-context family;
- review hook.

### Done when

Curriculum can choose among multiple capabilities rather than following a hard-coded lesson number.

## Slice 3 — Progressive onboarding / placement

Implement `FEAT-ONB-001` against only the content regions v1 actually supports.

### Minimum

- prior exposure question(s);
- audio availability/setup;
- written recognition anchor;
- aural recognition anchor;
- short listening meaning anchor;
- small construction/meaning anchor;
- low-support retrieval anchor where feasible;
- provisional route decision;
- missing constructs list;
- route uncertainty;
- first-session recalibration.

Do not claim full CEFR placement.

### Done when

True beginners reach a learnable first task and stronger entrants skip obvious known material without a long exam.

## Slice 4 — Session planner + adaptive support

Add state-driven session assembly.

### Planner must select

- capability;
- primary bottleneck;
- primary modality;
- task sequence;
- support policy;
- evidence expectations;
- estimated session burden.

### First support controllers

- Vietnamese meaning support;
- image/context support;
- replay;
- partial cue;
- answer reveal after attempt.

Caption/transcript policies can be added later with video/listening expansion.

### Done when

Two learners with different evidence can receive different next tasks/support for the same capability.

## Slice 5 — Review + transfer loop

Implement `FEAT-REV-001` and `FEAT-TRN-001` early. Without them, Nếp cannot verify "nhớ lâu" or "dùng được".

### Required

- review candidate state;
- due opportunity ranking;
- attempt-before-reveal review;
- parallel-item pool;
- changed-context tagging;
- delayed probe support;
- backlog compression after absence.

### Done when

A target can move through:

```text
learned today
→ retrieved later
→ changed context
→ delayed evidence
```

without one boolean `mastered` field.

## Slice 6 — Guided speaking + intelligibility repair

Implement the smallest useful subset of:

- `FEAT-SPK-001`;
- `FEAT-PRN-001`;
- `FEAT-ASR-001` if machine support is used.

### Start with

```text
rehearsal
→ model-hidden short utterance
→ one-slot recombination
→ guided one-turn response
```

Pronunciation work only triggers on relevant target risks.

ASR is optional for the first version; deterministic/manual constrained scoring is preferable to pretending an unvalidated score is authoritative.

### Done when

The system preserves rehearsal versus independent speaking and can attach pronunciation repair without turning the session into a phoneme course.

## Slice 7 — Meaning-linked constructions

Integrate `FEAT-GRM-001` into the first capability set.

Do not create a separate grammar-tab dependency.

### Required

- construction ID;
- form/meaning/use examples;
- interpretation evidence;
- model-hidden production opportunity;
- changed lexical slot/context;
- Vietnamese explanation support where useful.

### Done when

Grammar knowledge can influence capability readiness without grammar quiz score becoming the course progression source.

## Slice 8 — Recovery + useful return

Implement the smallest useful subset of `FEAT-MOT-001`.

### Required

- last useful learning timestamp;
- return/recovery state;
- overdue queue compression;
- smallest valid re-entry task;
- immediate learner-state recalibration;
- behavior metrics separated from learning metrics.

Notifications/streaks are optional experiments, not core architecture requirements.

### Done when

Returning after a break leads to one useful action rather than punishment/backlog dumping.

## Slice 9 — Reading, writing and bounded interaction

Expand the same capabilities with:

- `FEAT-READ-001`;
- `FEAT-WRI-001`;
- `FEAT-INT-001`.

Add only when prerequisite language makes the tasks meaningful.

Candidate examples:

```text
read a tiny menu/message related to known café language
write one short practical reply
handle a 2–3 turn bounded transaction
ask for clarification after a controlled breakdown
```

### Done when

New modalities attach to existing capability/evidence state rather than creating separate course silos.

## Slice 10 — Fluency consolidation

Integrate `FEAT-FLU-001` only after enough stable language exists.

### Required

- readiness rule;
- repeated-practice limit;
- quality-collapse backoff;
- changed-content check;
- delayed fluency/automaticity evidence sample.

### Done when

Faster performance is treated as consolidation evidence under known conditions, not a global speaking score.

## Slice 11 — Authentic video module

Integrate only after core learning works.

Uses:

- `FEAT-VID-002` readiness;
- `FEAT-VID-001` support controller;
- `FEAT-VID-003` temporal repair.

Video clips become scenario/input assets within capability units.

They do not create a second video curriculum.

### Done when

A clip is selected because learner × clip readiness is adequate, and caption/replay use remains visible to the Evidence Engine.

## AI integration order

AI should be introduced role by role, not as one giant tutor.

Candidate order:

1. internal content-candidate generation with human/deterministic review;
2. low-risk hint rephrasing;
3. constrained TTS with provenance;
4. bounded conversation-partner turns;
5. scoring assistance only after slice-level validation.

Every step goes through `ADR-004` / `FEAT-AIG-001`.

## Cross-slice quality gates

Before expanding to the next major slice, verify:

### Evidence integrity

- no invalid independent evidence;
- support events stored;
- scorer versions stored;
- unknown preserved;
- route decision reasons stored.

### Learning integrity

- target learners understand task instructions;
- first attempts are feasible;
- delayed/changed-context opportunities exist;
- obvious confounds are identified.

### Product integrity

- mobile flow works;
- session can terminate gracefully;
- optional AI outage does not destroy core path;
- instrumentation distinguishes learning from engagement.

## What not to build first

Do not start Nếp v1 implementation with:

- hundreds of hand-authored lessons;
- a giant dashboard;
- a Duolingo-style XP economy;
- unrestricted voice chat;
- authentic YouTube ingestion pipeline;
- advanced CEFR level calculation;
- leaderboards;
- detailed avatar/pet systems;
- comprehensive AI agent orchestration.

Those can consume months while the core learning/evidence loop remains unproven.

## First implementation milestone

The first meaningful milestone is **not** "A1 course complete."

It is:

```text
one target learner
→ short placement bootstrap
→ correctly routed capability
→ meaningful input
→ active attempt
→ support if needed
→ independent retrieval
→ changed-context use
→ stored evidence
→ later review
→ next decision changes from evidence
```

Once that loop is reliable, expanding content becomes leverage rather than rework.
