---
id: FEAT-INT-001
title: Adaptive interaction progression engine
status: research-backed-candidate
research_question: RQ-015
synthesis: SYN-INT-001
experiment: EXP-015
---

# FEAT-INT-001 — Adaptive interaction progression engine

## Learner problem

A learner can succeed at isolated speaking prompts and still fail in conversation because conversation requires coordination in real time:

```text
hear another person
→ understand what they are doing/saying
→ produce a relevant next turn
→ manage the exchange
→ repair misunderstandings
→ move toward a shared goal
```

Most speaking apps can accidentally hide this problem by prompting a monologue, accepting any semantically related response, or letting an AI partner do most of the interactional work.

## Target capability

The learner can complete a short familiar interaction by:
- understanding the partner's relevant turns;
- responding contingently;
- using known vocabulary/constructions intelligibly;
- managing simple turn/listener behavior;
- initiating clarification/repair when needed;
- selecting an appropriate pragmatic action;
- continuing until the shared communicative goal is completed.

## Research basis

Primary principles:
- `PRN-181`–`PRN-196`
- `SYN-INT-001`

Evidence themes:
- interaction supports L2 development (`SRC-0156`);
- oral interactional feedback can support development (`SRC-0060`);
- interactive tasks are needed to elicit interactional ability (`SRC-0059`);
- response contingency, turn-taking, listener support, repair and sequence management are interactional-competence dimensions (`SRC-0158`–`SRC-0163`);
- pragmatics is teachable (`SRC-0157`);
- AI/voice chatbots can increase practice opportunities but have authenticity/ASR/pragmatic limitations (`SRC-0164`–`SRC-0167`).

## Non-goals

This feature is not:
- an endless chatbot;
- a monologue prompt with an avatar;
- an AI fluency score;
- a pronunciation-only roleplay;
- a list of polite phrases;
- a scripted dialogue memorization engine;
- proof of real-world interaction merely because an LLM understood the learner.

## Core session loop

```text
SCENARIO + SHARED GOAL
        ↓
partner turn
        ↓
learner FIRST RESPONSE
        ↓
record contingency + support provenance
        ↓
continue if shared understanding holds
        ↓
if breakdown: learner REPAIR opportunity
        ↓
interaction progresses
        ↓
task goal completes
        ↓
brief post-task feedback
        ↓
changed wording / context / partner
        ↓
delayed transfer
```

Do not interrupt every turn with correction.

## Interaction stages

### I0 — action recognition + bounded response

Partner produces one familiar move.

Example:

```text
"What's your name?"
```

Learner chooses or produces a known relevant response.

Evidence:
- recognized incoming social/semantic action;
- linked response to it.

This is highly supported interaction, not independence.

### I1 — independently produced adjacency response

Partner:

```text
"Tea or coffee?"
```

Learner generates a response without full model visible.

Optional hint only after a first-pass response or explicit help request.

### I2 — short predictable goal sequence

2–4 learner turns.

Example: café order, basic check-in, directions, meeting time, delivery confirmation.

The learner cannot preload the whole script because the partner supplies each next turn.

### I3 — repair-enabled sequence

Add one controlled breakdown opportunity:
- unfamiliar wording;
- ambiguous number/name;
- deliberately less-clear but valid turn;
- one plausible misunderstanding.

Learner may:
- ask to repeat;
- ask to clarify;
- confirm a choice;
- state non-understanding.

Successful repair counts positively.

### I4 — wording/partner variation

Same underlying function, changed realization:

```text
"What would you like?"
"What can I get you?"
"What do you want to order?"
```

Use different voices/partners where the listening engine says the variation is learnable.

### I5 — bounded open interaction

Partner selects among a controlled set of plausible next actions based on learner response.

Learner must manage a small goal, not recite a fixed branch.

### I6 — external transfer

Human partner, peer, or human-rated interaction sample when feasible.

Use for product validation and periodic capability calibration, not necessarily every session.

## Scenario specification

```ts
type InteractionScenario = {
  id: string;
  stage: "I0" | "I1" | "I2" | "I3" | "I4" | "I5" | "I6";
  sharedGoal: string;
  learnerRole: string;
  partnerRole: string;

  prerequisiteIds: string[];
  vocabularyIds: string[];
  constructionIds: string[];
  pragmaticFunctionIds: string[];

  partnerMoveGraph: PartnerMove[];
  repairOpportunities: RepairOpportunity[];

  maxTurns?: number;
  supportPolicyId: string;
  partnerPolicyId: string;
};
```

## Turn evidence

```ts
type InteractionTurnEvidence = {
  interactionId: string;
  turnIndex: number;
  partnerType: "ai" | "peer" | "human";

  incomingMoveId?: string;
  incomingMeaningIds: string[];

  responseText?: string;
  responseAudioId?: string;

  contingencyEvidence?: number;
  goalProgressEvidence?: number;
  pragmaticFitEvidence?: number;
  lexicalConstructionEvidence?: number;
  intelligibilityEvidence?: number;

  responseLatencyMs?: number;

  repairNeeded: boolean;
  repairInitiatedBy?: "learner" | "partner" | "system";
  repairStrategyId?: string;
  repairResolved?: boolean;

  supportLevel: number;
  modelVisible: boolean;
  transcriptVisible: boolean;
  translationVisible: boolean;

  partnerRescueEvents: string[];
};
```

Do not infer all fields automatically until validity is established.

## Interaction-level evidence

```ts
type InteractionAttempt = {
  id: string;
  scenarioId: string;
  partnerType: "ai" | "peer" | "human";

  goalCompleted: boolean;
  turnCount: number;
  contingentResponseRate?: number;
  successfulRepairRate?: number;
  learnerInitiationCount: number;
  partnerRescueCount: number;
  supportDependence: number;

  delayedProbeOf?: string;
};
```

## Response contingency

Before evaluating grammar, ask:

> Did this response make sense as a next turn to what the partner just did?

Candidate levels:

```text
0 unrelated / no response
1 weakly related but misses required action/information
2 functionally relevant but incomplete
3 relevant and sufficient for current stage
```

This scale is a product hypothesis until validated against human raters.

Never let high grammar accuracy compensate for an unrelated response.

## Incoming-turn comprehension

Use interaction itself as evidence when possible.

Example:

```text
Partner asks for a time
→ learner supplies plausible time
```

If the learner responds incorrectly, the diagnostic engine may fall back to:
- replay;
- meaning-choice probe;
- transcript after first attempt;
- targeted vocabulary/construction support.

This links `FEAT-LIS-001` to interaction without turning every turn into a quiz.

## Turn-taking behavior

Track low-inference observable behaviors first:
- did learner produce a turn where a response was expected?
- did learner interrupt because of system latency or actual overlap?
- did learner sustain a needed turn?
- did learner yield/close successfully?

Do not create a universal “ideal pause milliseconds” threshold.

Latency depends on:
- stage;
- input difficulty;
- speech-recognition delay;
- device/network;
- planning need;
- whether learner is repairing.

## Listener-support behavior

Candidate beginner functions:
- acknowledgement;
- confirmation;
- surprise/interest;
- request to continue/repeat.

Teach them inside relevant positions.

Do not reward random backchannel spam.

## Repair engine

### Repair detection

A breakdown can come from:
- learner did not hear;
- learner heard but did not know a word/construction;
- learner's output was not understood;
- partner turn was ambiguous;
- speech recognition failed;
- AI partner interpreted incorrectly.

Log cause separately when known.

### Learner repair options

Near-A0 candidate inventory:

```text
Sorry?
Again, please.
Slower, please.
What does ___ mean?
Do you mean ___?
___ or ___?
I don't understand.
```

### Repair success

A successful repair means:

```text
problem signaled
→ clarification/repetition occurs
→ shared understanding restored
→ task progresses
```

Do not mark the initial problem as a simple failure if repair succeeds.

## Engineered breakdown policy

Repair needs practice, but fake breakdowns can become annoying and unrealistic.

Parameters for `EXP-015`:
- frequency;
- type;
- linguistic difficulty;
- whether learner or partner initiates;
- whether the breakdown is naturally plausible.

Never intentionally misrecognize learner speech outside an explicit experiment/scenario policy.

## Pragmatic-function model

```ts
type PragmaticFunction = {
  id: string;
  function: string;
  contextFeatures: {
    relationship?: string;
    power?: string;
    distance?: string;
    imposition?: string;
    setting?: string;
  };
  candidateRealizations: string[];
  sequencePositions: string[];
  risks: string[];
};
```

Near-A0 should not expose academic labels like `power`/`imposition` unless useful. The engine uses them to choose scenarios/forms.

## Pragmatic teaching loop

```text
context
→ hear/see a social action
→ interpret intention
→ choose/produce a response
→ compare alternatives if needed
→ changed relationship/context
→ use again
```

Examples:
- request from café staff vs request to a friend;
- decline an offer;
- apologize for being late;
- ask a stranger to repeat;
- correct an order politely enough for the context.

## Avoid one “politeness score”

Pragmatic appropriateness is contextual and culturally variable.

Prefer concrete feedback:

```text
This sounds very direct for this situation.
A common option here is: "Could I have...?"
```

rather than:

```text
Politeness: 62/100
```

unless such scoring is validated.

## Interactional feedback policy

During the exchange:

```text
meaning-blocking problem
→ repair now

learner requests help
→ bounded help now

high-value target error that permits brief repair
→ short cue/recast

non-blocking low-priority error
→ defer until task boundary
```

After task:
- at most a bounded set of high-value observations;
- include one interactional behavior, not only grammar/pronunciation;
- ask learner to replay/retry a changed mini-sequence.

## AI partner contract

AI may:
- select a next move from allowed scenario goals;
- vary surface wording within readiness limits;
- ask a contextually relevant follow-up;
- repeat/rephrase after learner repair request;
- trigger configured repair opportunities;
- provide post-task feedback candidates;
- generate parallel transfer scenarios for review.

AI must not silently:
- infer mastery because it understood malformed speech/text;
- provide learner's intended answer before retrieval;
- resolve every breakdown without learner involvement;
- accept unrelated answers merely to keep chat friendly;
- claim a pragmatic judgment is culturally universal;
- turn the task into long AI monologues.

## Partner-assistance provenance

Log:

```text
partner_rephrase
partner_repeat
partner_hint
partner_supplied_word
partner_supplied_sentence
partner_clarification_request
partner_inferred_intent_without_clarification
```

This allows the Evidence Engine to distinguish independent interaction from partner-rescued completion.

## AI accommodation gate

Candidate policy:

```text
if learner output is ambiguous to a human-like threshold:
  ask clarification
else:
  continue
```

But the threshold itself requires validation.

Use human listener data to calibrate:
- intelligibility;
- semantic recoverability;
- response relevance.

Do not let LLM inference confidence stand in for human evidence.

## ASR integration

`FEAT-ASR-001` remains authoritative for speech-recognition evidence.

If ASR fails:
- do not automatically tell the learner their English was wrong;
- distinguish `recognition_failure` from `learner_language_failure`;
- allow replay/retry;
- use human validation samples in research.

## Interaction learner state

Avoid:

```ts
conversationLevel = 73;
```

Prefer:

```ts
type InteractionCapabilityState = {
  capabilityId: string;
  incomingTurnEvidence: EvidenceSummary;
  contingentResponseEvidence: EvidenceSummary;
  repairEvidence: EvidenceSummary;
  pragmaticEvidence: EvidenceSummary;
  goalCompletionEvidence: EvidenceSummary;
  humanTransferEvidence?: EvidenceSummary;
  supportDependence: EvidenceSummary;
};
```

## Task selection

```text
known scenario + ready vocabulary/constructions
        ↓
choose shortest interaction just above current IC evidence
        ↓
if contingent responses stable
→ add another turn / surface variation
        ↓
if breakdown handling weak
→ targeted repair task
        ↓
if AI task stable
→ changed partner/context
        ↓
periodically validate against human interaction
```

Do not unlock only because the learner completed N chats.

## Review integration

Interaction review should replay **functions**, not scripts.

Examples:
- answer same question with changed wording;
- clarify a different number/name;
- request same object from a different interlocutor;
- decline in a different context;
- complete one changed 3-turn sequence.

## Progress integration

Human-readable examples:

```text
Interaction

Can answer simple choice questions relevantly
✓ across different wording

Can ask for repetition when a detail is unclear
✓ in guided scenarios

Can complete a short café order
△ AI partner only; human transfer not yet checked

Can decline a request appropriately
○ not enough evidence
```

This is much more informative than “Speaking level 42.”

## Learning metrics

Primary:

```text
delayed unsupported changed-partner interaction gain
──────────────────────────────────────────────────
practice minutes
```

Dimensions:
- shared-goal completion;
- response contingency;
- incoming-turn understanding;
- learner-initiated repair success;
- pragmatic fit;
- intelligibility;
- lexical/construction retrieval;
- partner rescue/support dependence.

## Engagement metrics

Keep separate:
- interaction starts/completions;
- turns spoken;
- voluntary retries;
- AI session duration;
- anxiety/self-report;
- abandonment;
- partner preference.

These can matter for product use but are not mastery.

## Falsification

Redesign or weaken `FEAT-INT-001` if:
- AI roleplay gains fail to transfer to human/changed-partner interaction;
- the system accepts off-topic/ambiguous turns at unacceptable rates;
- engineered repair produces scripted behavior without spontaneous transfer;
- pragmatic feedback has low inter-rater agreement or strong cultural bias;
- AI/ASR errors are misdiagnosed as learner errors too often;
- extra interaction complexity raises time/anxiety without meaningful delayed gain;
- a simpler speaking/listening sequence performs equally well on human interaction outcomes.

## Experiment

See `EXP-015`.
