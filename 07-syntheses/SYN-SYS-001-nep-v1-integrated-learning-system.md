# SYN-SYS-001 — Nếp v1 integrated learning system

**Status:** integrated product synthesis  
**Date:** 2026-08-26  
**Scope:** integrates `RQ-001` through `RQ-021`; does not create new scientific claims.

## Question

What single product architecture is justified by the completed research cycles, and how should the parts interact without collapsing distinct kinds of learning evidence into one score?

## Synthesis

Nếp should be an **evidence-driven adaptive capability system**, not a linear course, a CEFR textbook, a video player with exercises, an SRS deck, or an unrestricted AI tutor.

The learner-facing experience should stay simple:

```text
start at a sensible place
→ understand one useful thing
→ retrieve/use it
→ handle a small change
→ return later
→ expand the capability
```

Underneath, the product must preserve several distinctions that the learner does not need to see directly:

```text
placement prior
≠ observed learning evidence
≠ supported success
≠ independent recall
≠ changed-context transfer
≠ delayed retention
≠ engagement
```

The integrated system therefore has three authoritative layers:

```text
Curriculum Engine
→ what capability should be worked on next?

Learning Engine
→ what task/support sequence should be used now?

Evidence Engine
→ what did the learner actually demonstrate under what conditions?
```

AI, ASR, TTS, video, captions, Vietnamese explanations, streaks and recommendations are supporting services around these three layers. They are not authoritative mastery engines.

## Product source of truth

The source of truth is a **capability graph plus decomposable learner evidence**.

Do not make any of the following the primary source of truth:

- one CEFR level;
- unit number;
- lesson completion;
- XP;
- streak length;
- SRS due state;
- AI confidence;
- ASR confidence;
- time spent;
- a single `mastery = 0.84` field.

A capability is a practical communicative outcome such as:

```text
Can order one familiar drink and answer a simple size question.
```

Its current learner state is inferred from evidence such as:

```text
listening meaning understood with no transcript
spoken chunk recalled without visible model
pronunciation understood by listener
one-turn response contingent on partner question
changed-context version succeeded
same capability retained after delay
```

## Runtime architecture

```text
                        ┌───────────────────────┐
                        │  Placement bootstrap  │
                        │    FEAT-ONB-001       │
                        └───────────┬───────────┘
                                    │ provisional state
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         LEARNER MODEL                               │
│ capability evidence · target evidence · support history · unknowns │
└───────────────────────────────┬─────────────────────────────────────┘
                                │
                                ▼
                    ┌─────────────────────────┐
                    │ Curriculum Orchestrator │
                    │      FEAT-CUR-001       │
                    └────────────┬────────────┘
                                 │ unit contract
                                 ▼
                    ┌─────────────────────────┐
                    │     Session Planner     │
                    │ bottleneck + task + UX  │
                    └────────────┬────────────┘
                                 │
        ┌────────────────────────┼────────────────────────┐
        ▼                        ▼                        ▼
  input/meaning            language focus             output/use
 listening/read      vocab/chunks/grammar/pron     speaking/write
        │                        │                    interaction
        └────────────────────────┼────────────────────────┘
                                 ▼
                       support controllers
             Vietnamese · replay · captions · planning
                                 │
                                 ▼
                         independent attempt
                                 │
                                 ▼
                         Evidence Engine
                                 │
                  ┌──────────────┴──────────────┐
                  ▼                             ▼
             Review engine                 Transfer probes
             FEAT-REV-001                  FEAT-TRN-001
                  │                             │
                  └──────────────┬──────────────┘
                                 ▼
                         learner model update
                                 │
                                 ▼
                           next decision
```

## Responsibilities by research cycle

### Initial learner state

`RQ-021` / `FEAT-ONB-001`

- collect only useful priors;
- run a short common anchor set;
- adaptively probe uncertain frontiers;
- keep untested constructs `unknown`;
- choose a conservative next-learning region;
- recalibrate from the first real sessions.

### Vocabulary/chunks and retrieval

`RQ-001`, `RQ-004`, `RQ-005`

- distinguish recognition, comprehension, retrieval, transfer and delayed retention;
- attempt before reveal when retrieval is the target;
- use changed contexts rather than exact-item repetition as transfer evidence;
- schedule review from learner evidence rather than treating schedule as mastery.

### Vietnamese support

`RQ-002`, `RQ-019`

- Vietnamese is a scaffold, not the task;
- support strength is recorded;
- L1-population priors may select diagnostic opportunities but cannot define an individual learner;
- learner evidence overrides Vietnamese-L1 priors quickly.

### Listening

`RQ-003`, `RQ-009`, `RQ-010`, `RQ-011`

- separate sound recognition from message comprehension;
- use replay/caption/transcript support diagnostically;
- authentic video requires readiness rather than being the universal starting medium;
- temporal repair should target a bottleneck instead of fragmenting all listening by default.

### Speaking, pronunciation and interaction

`RQ-006`, `RQ-007`, `RQ-008`, `RQ-015`

- begin meaningful speaking near A0 in bounded tasks;
- distinguish rehearsal from independent production;
- prioritize intelligibility over native-accent imitation;
- require actual contingent turns before claiming interaction capability;
- ASR cannot become a mastery gate unless validated for the exact population/task/claim.

### Grammar/constructions

`RQ-012`

- teach form as form-meaning-use mappings inside useful messages;
- rule recognition is not productive grammar evidence;
- constructions should reappear across modalities and changed contexts.

### Reading and writing

`RQ-013`, `RQ-014`

- reading/writing are not separate textbook silos;
- connect them to known communicative capabilities;
- distinguish support-assisted production from independent writing;
- correction of one text is not evidence of future writing transfer.

### Fluency/automaticity

`RQ-016`

- fluency practice begins after enough accuracy/meaning access exists;
- faster repeated performance is not global fluency;
- changed-task and delayed evidence remain necessary.

### Curriculum integration

`RQ-017`

- organize around capabilities;
- make one bottleneck primary when feasible;
- increase task complexity gradually;
- maintain rolling input/output/language-focus/fluency balance without forcing every strand into every session.

### Useful return

`RQ-018`

- optimize return to useful learning, not return to the app at any cost;
- break recovery should compress/repair the learning queue rather than punish the learner;
- streaks/rewards, if used, remain behavioral mechanisms and never mastery evidence.

### AI reliability

`RQ-020`

- AI may generate candidates, mediate, rephrase, classify low-risk content or personalize wording;
- deterministic constraints and provenance apply where possible;
- AI abstains/escalates when a high-value claim is not reliable enough;
- model/provider/prompt changes require regression validation when they affect learning decisions.

## Canonical session loop

The default session is state-driven, not a fixed page sequence.

Candidate near-A0 loop:

```text
1. choose capability + primary bottleneck
2. present smallest meaningful context
3. collect first attempt when humane/informative
4. reveal smallest useful support
5. focus on one useful target
6. retrieve without answer-bearing support
7. use target in a bounded changed context
8. store decomposable evidence + support provenance
9. schedule later review/transfer if warranted
10. select next action
```

Valid alternate entry points include:

```text
retention due → retrieval first
known language + weak interaction → interaction first
known meaning + weak sound-form access → listening discrimination first
known spoken target + weak written form → reading/writing mapping first
```

The system must not force the default sequence when learner evidence already makes a different entry point more useful.

## Evidence model

Every evidence event should identify at least:

```text
learner
capability / target
construct being inferred
input modality
response modality
task family
novelty / changed-context status
support visible before attempt
attempt before feedback
result
scorer type + scoring version
occurred_at
```

Derived states may summarize evidence, but raw evidence remains auditable.

### Core learner claims

Nếp may maintain summaries for:

```text
understood
recalled
transferred
retained
```

and task-specific claims such as:

```text
aural_form_recognition
short_utterance_production
interaction_contingency
interaction_repair
pronunciation_intelligibility
reading_message_comprehension
independent_micro_writing
fluency_effort
```

No claim is inferred merely because a lesson was completed.

## Support contract

Support is part of the evidence condition.

Examples:

```text
Vietnamese translation
English caption
full transcript
replay
word bank
sentence frame
visible speech model
planning time
partner rephrase
pronunciation comparator
AI hint
```

The engine must know whether support was:

```text
available
shown
learner-requested
automatically triggered
answer-bearing
shown before or after the independent attempt
```

A success after a full reveal remains useful practice but cannot overwrite the failed independent attempt.

## Unknown is a valid state

The learner model must support:

```text
known weak
known strong
uncertain
not yet observed
```

`not yet observed` must not silently become `weak`.

This matters especially for placement and for modalities that are deliberately deferred to reduce onboarding burden.

## AI/TTS/ASR position

```text
AI proposes / mediates
↓
policy + validation gate
↓
learner task
↓
observable learner behavior
↓
Evidence Engine decides what can be claimed
```

Never:

```text
AI says learner is A2
→ learner model accepts A2
```

TTS is an input source whose voice/model/version must be known. Natural/human speech remains necessary for claims that must generalize beyond a single synthetic voice.

ASR output can be used as a practice convenience where validated enough, but raw ASR confidence is not pronunciation or speaking mastery.

## Learner-facing product

The machinery should collapse into a small number of surfaces.

### 1. Start

```text
A few adaptive questions
→ Start learning
```

### 2. Today

```text
Continue: Order a drink
Review: 3 things worth keeping
```

### 3. Learning session

One context, one main bottleneck, progressive support, active attempt, changed use.

### 4. Review

Due evidence opportunities, not a giant card backlog.

### 5. Progress

Show useful capabilities and recent evidence quality. Avoid fake percentages such as `English 37% complete`.

### 6. Recovery

After a break, restart with the smallest useful action and re-estimate state instead of demanding backlog repayment.

## Nếp v1 release interpretation

"v1" should mean the first coherent version of the architecture, not every researched feature at full sophistication.

### Core runtime required

- placement bootstrap;
- learner/evidence model;
- capability graph;
- curriculum orchestrator;
- A0 learning loop;
- vocabulary/chunk evidence;
- Vietnamese scaffold controller;
- listening diagnosis;
- construction learning;
- guided speaking;
- intelligibility-first pronunciation;
- review + changed-context transfer;
- useful return/recovery;
- AI reliability gate for any AI used.

### Progressive modules

Reading, writing, interaction and fluency are part of the architecture but can ship progressively after the core runtime is stable.

Authentic video/caption/temporal-repair systems should not block v1. They attach later through the same unit/evidence contracts.

## Global guardrails

1. **No completion = mastery.**
2. **No support-blind evidence.**
3. **No recognition = retrieval.**
4. **No same-item repetition = transfer.**
5. **No immediate success = retention.**
6. **No self-report = direct ability.**
7. **No Vietnamese population prior = individual truth.**
8. **No accent strength = unintelligibility.**
9. **No ASR/LLM confidence = language mastery.**
10. **No one global level as runtime decision source.**
11. **No engagement metric substitutes for learning.**
12. **No AI-generated asset without provenance appropriate to its risk.**

## Primary product metric

Across the integrated system, the strongest common product metric is:

```text
delayed changed-context capability gain
──────────────────────────────────────
learner minutes
```

It should be accompanied by burden and return measures, not replaced by them.

## Remaining uncertainty

The research establishes architecture and guardrails more strongly than exact thresholds.

Still experimental:

- first capability catalogue;
- exact prerequisite graph;
- placement item count and stop rules;
- session length distribution;
- support-fading rules;
- task-complexity increments;
- review workload;
- transfer probe frequency;
- speaking/interaction unlock points;
- AI/ASR/TTS model thresholds;
- notification/recovery policy;
- monetization and willingness to pay.

These should be encoded as configuration/experiment parameters, not hidden constants presented as science.
