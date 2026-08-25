---
id: EXP-015
title: Turn-by-turn interaction, repair and human-transfer validation
status: proposed
research_question: RQ-015
---

# EXP-015 — From controlled speaking to real interaction

## Primary question

Which interaction-training policy produces the best **delayed unsupported changed-partner interaction gain per practice minute** for Vietnamese near-A0 learners?

Secondary question:

How much does performance with an AI voice partner transfer to interaction with a human or human-rated unfamiliar partner/context?

## Population

Vietnamese-speaking Nếp learners near A0/A1 with prerequisite evidence for the target:
- listening items/constructions;
- core vocabulary/chunks;
- guided speaking;
- pronunciation/intelligibility targets.

Stratify by:
- listening evidence;
- speaking-production evidence;
- pronunciation/intelligibility evidence;
- baseline repair knowledge;
- baseline AI/ASR familiarity;
- speaking anxiety if measured;
- device/network/input conditions.

## Experimental conditions

### A — monologic speaking practice

Matched target language and approximate practice time.

Example:

```text
Prompt: Tell me what you want to order.
Learner speaks one response.
Feedback.
```

Purpose:
estimate what interaction adds beyond ordinary controlled speaking.

### B — scripted short dialogue

```text
partner line
→ learner expected line
→ partner line
→ learner expected line
```

Some surface variation can exist, but learner sequence is highly predictable.

Purpose:
estimate whether memorized turn structure is enough.

### C — adaptive AI interaction

```text
shared goal
→ partner selects plausible move
→ learner contingent response
→ variable next move
→ bounded feedback/repair
→ goal completion
```

No transcript/translation before first response unless learner's current stage explicitly requires it.

### D — adaptive AI interaction + explicit repair curriculum

Condition C plus:
- repair routines taught before/within practice;
- occasional plausible controlled breakdowns;
- requirement/opportunity for learner-initiated clarification;
- delayed changed-breakdown probes.

## Optional human-practice comparator

Where operationally feasible, include a smaller condition with matched peer/human interaction practice.

This is useful for estimating whether AI practice has different transfer characteristics, but it is not required for every production rollout.

## Scenario families

Use practical bounded goals:

### Family 1 — café/order

```text
choose item
choose size
confirm quantity
decline/accept extra
finish order
```

### Family 2 — meeting/time

```text
ask/answer time
clarify number
confirm location
respond to change
close exchange
```

### Family 3 — delivery/work update

```text
identify problem
answer detail question
clarify missing information
agree next action
```

### Family 4 — simple social interaction

```text
greet
answer personal/basic question
ask one reciprocal question
respond to closing
```

Do not treat all scenario families as equally difficult.

## Interaction novelty

Manipulate separately:
- lexical novelty;
- construction novelty;
- surface wording novelty;
- voice/accent novelty;
- partner policy novelty;
- pragmatic-context novelty;
- repair/breakdown novelty.

This allows transfer to be measured rather than assumed.

## Baseline

Before treatment, collect short interactive probes:

```text
known content
unfamiliar wording
bounded shared goal
no strong support on first pass
```

Measure:
- incoming-turn interpretation via next-turn behavior;
- response contingency;
- goal progress/completion;
- learner repair initiation;
- pragmatic action choice;
- intelligibility by configured evidence source;
- support dependence.

Do not use a monologue score as the sole baseline.

## Immediate per-turn evidence

For each partner turn:
- expected semantic/action space;
- whether learner responded;
- response relevance/contingency;
- target meaning supplied;
- lexical/construction evidence;
- pragmatic fit;
- intelligibility evidence;
- response latency;
- support opened;
- partner rescue.

If the system cannot confidently score a dimension, preserve raw evidence rather than manufacturing certainty.

## Repair manipulation

### Natural repair

Occurs because learner or system actually experiences ambiguity/misunderstanding.

Track separately from engineered repair.

### Engineered repair

Candidate controlled cases:
- ambiguous number pair;
- one unexpected synonym/paraphrase within readiness range;
- one intentionally incomplete partner reference;
- a plausible clarification request from partner.

Do **not** intentionally inject ASR failure and present it as learner error.

### Repair outcomes

```text
breakdown_noticed
repair_initiated
strategy_selected
clarification_received
understanding_restored
goal_progressed
```

Primary repair metric:

```text
successful learner-initiated repair
─────────────────────────────────
repair opportunities
```

Interpret with listening difficulty; high repair count alone is neither good nor bad.

## Pragmatics manipulation

Teach/test high-value functions in context:
- request;
- accept/decline;
- apologize;
- ask permission;
- clarify;
- confirm;
- correct information;
- greet/close.

Changed-context probe example:

```text
practice: request from café staff
transfer: request help from stranger
```

Do not score only phrase matching. Evaluate whether the learner chose a workable action/form for the situation.

## AI accommodation experiment

AI can over-infer learner intention.

Compare partner policies:

### Normal accommodating AI
Standard conversational inference.

### Clarification-gated AI
When learner output falls below a calibrated ambiguity/intelligibility threshold, AI asks a clarification question rather than silently inferring the intended meaning.

Measure:
- task completion;
- learner repair;
- frustration;
- delayed human-transfer performance;
- false clarification rate;
- false acceptance rate.

The clarification-gated policy is adopted only if it better predicts/supports human interaction without excessive friction.

## AI rescue index

Calculate transparent process variables such as:

```text
partner repeats
partner rephrases
partner supplies missing word
partner supplies intended proposition
partner asks leading question
partner infers ambiguous intent without checking
```

Do not treat a goal completed with heavy partner rescue as equivalent to independent completion.

## Immediate changed-turn probe

After practice, keep communicative function but change partner realization.

Example:

```text
practice: "What would you like?"
probe: "What can I get you?"
```

This tests action recognition rather than sentence-trigger memorization.

## Delayed AI transfer probe

After delay:
- new scenario instance;
- no visible script;
- no translation before first response;
- partner wording not previously practiced;
- bounded target prerequisites still within learner state.

Measure same interaction dimensions.

## Human-transfer validation

This is critical for claims about real conversational capability.

Sample a subset of learners/tasks for:
- live human partner;
- peer partner under structured protocol; or
- recorded interaction judged by trained human listeners/raters when live interaction is infeasible.

Partner instructions should avoid excessive rescue and should be standardized enough for comparison while still allowing interaction.

Measure:

```text
human_goal_completion
human_response_contingency
human_listener_understanding
human_observed_repair
human_pragmatic_fit
```

Compare against AI metrics.

## Calibration questions

1. Does AI contingency scoring correlate sufficiently with human judgments?
2. How often does AI accept output humans find ambiguous/unintelligible?
3. How often does AI reject output humans understand?
4. Does AI partner assistance predict later human difficulty?
5. Does repair practice transfer to novel human breakdowns?
6. Does pragmatic feedback transfer across changed social contexts?

## Primary learning outcome

```text
delayed unsupported changed-partner interaction gain
──────────────────────────────────────────────────
practice minutes
```

Report dimensions separately before any composite:
- goal completion;
- response contingency;
- incoming-turn understanding;
- repair success;
- pragmatic fit;
- intelligibility;
- lexical/construction retrieval;
- partner rescue/support dependence.

## Interaction versus monologue analysis

Key comparison:

```text
monologue speaking gain
vs
interaction transfer gain
```

If monologue-only practice performs equally on real interaction outcomes, the additional interaction engine needs redesign or narrower scope.

## Script-dependence analysis

For scripted dialogue condition measure:

```text
performance on practiced sequence
vs
changed partner wording
vs
changed branch
vs
delayed human interaction
```

A large collapse under changed wording indicates script learning rather than interactional development.

## AI-dependence analysis

Potential warning pattern:

```text
AI goal completion ↑
AI turns ↑
while human transfer ↔ / ↓
```

Also track whether learners increasingly wait for AI leading prompts rather than initiating/repairing.

## Feedback timing

Compare where feasible:
- immediate meaning-blocking repair;
- brief delayed post-task language feedback;
- mixed policy.

Do not interrupt every non-blocking error.

Evaluate:
- interaction completion;
- target accuracy later;
- delayed transfer;
- perceived cognitive load.

## False-scoring audit

Manually review a stratified sample of:
- response-contingency judgments;
- pragmatic judgments;
- intelligibility/ASR judgments;
- repair classification;
- AI rescue classification.

Record false positive/negative rates by proficiency, task and accent/voice condition.

Automated scores do not graduate from experimental status without this audit.

## Falsification criteria

The proposed engine is weakened if:
- AI interaction practice does not outperform matched monologue/script practice on delayed changed-partner outcomes;
- AI performance correlates poorly with human interaction performance;
- the AI accepts ambiguous/unintelligible turns too often;
- repair instruction produces only memorized repair phrases without successful novel repair;
- pragmatic feedback has poor human agreement or unstable cross-context validity;
- interaction practice adds excessive time/anxiety with negligible delayed benefit;
- partner-rescue behavior explains most apparent goal completion.

## Adoption rule

Adopt interaction stages and AI roleplay only where they improve later unsupported interaction.

Adopt repair curriculum if it increases successful recovery and shared-goal progress in novel interactions.

Adopt automated response/pragmatic scoring only after human calibration.

Never claim that chatbot task completion alone proves real conversational competence.
