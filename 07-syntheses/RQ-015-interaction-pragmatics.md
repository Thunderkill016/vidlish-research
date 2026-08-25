---
id: SYN-INT-001
title: Interaction progression from controlled turns to shared understanding
status: initial-synthesis
research_question: RQ-015
last_verified: 2026-08-26
---

# RQ-015 — Interaction and pragmatics for near-A0 learners

## Decision summary

Nếp must treat **interaction** as a distinct capability, not as “speaking but with two avatars.” A learner can pronounce sentences fluently and still fail to understand the previous turn, answer a different question, miss a request, fail to ask for clarification, or use a socially inappropriate response.

The core interaction loop should be:

```text
LISTEN to a real turn
        ↓
INTERPRET what action/meaning it carries
        ↓
RESPOND contingently
        ↓
manage TURN / LISTENER behavior
        ↓
if breakdown: REPAIR
        ↓
continue toward a shared GOAL
        ↓
later transfer to a NEW PARTNER / NEW CONTEXT
```

AI roleplay can provide scalable low-stakes practice, but success with an accommodating AI must not be treated as proof of human conversational ability.

## Interaction is not monologue plus response time

Interaction research shows a robust relationship between meaningful interaction and L2 development, while effects depend on task, interlocutor and learner variables (`SRC-0156`, `SRC-0060`).

Interactional-competence research adds another point: conversational ability is **co-constructed**. Performance depends on how a learner coordinates with another participant, not only on the grammar/fluency of isolated utterances (`SRC-0158`, `SRC-0159`, `SRC-0161`).

Therefore Nếp should separate:

```text
monologic production
from
turn-by-turn interaction
```

and should never infer the latter from the former alone.

## Candidate interaction dimensions

For early Nếp interaction, maintain separate evidence for:

```text
incoming_turn_comprehension
response_contingency
communicative_goal_progress
turn_taking
listener_support
repair_detection
repair_execution
pragmatic_fit
lexical_construction_retrieval
intelligibility
interactional_latency
```

These dimensions can interact, but they should not initially be collapsed into one `conversation_score`.

## Response contingency is central evidence

`SRC-0160` focuses on contingent responding: a response should demonstrably connect to the preceding speaker's contribution.

Example:

```text
A: What time do you arrive?
B: At seven.
```

The next turn provides evidence that B understood both the question's action and relevant content.

Contrast:

```text
A: What time do you arrive?
B: I like coffee.
```

B may have produced accurate English, but the interaction failed.

Therefore:

```text
linguistically correct response
≠
interactionally successful response
```

Nếp should score/record response relevance separately from surface accuracy.

## Understanding can be observed through the next turn

In interaction, comprehension is not always best measured by pausing the conversation and asking a multiple-choice meaning question. A contextually appropriate next action can itself provide evidence of understanding.

Candidate sequence:

```text
Partner: "Do you want tea or coffee?"
Learner: "Coffee, please."
```

This is stronger interaction evidence than:

```text
Partner: "Do you want tea or coffee?"
[conversation stops]
MCQ: What did the person ask?
```

The MCQ can be used diagnostically when interaction breaks down, but should not replace natural contingency when the learner can continue.

## Turn-taking is a skill

Interactional-competence research identifies turn management as part of higher-quality interaction (`SRC-0158`, `SRC-0159`, `SRC-0161`). For near-A0 Nếp this does not require teaching conversation-analysis terminology.

Teach observable routines:
- recognizing when a response is expected;
- answering without excessive avoidable delay;
- using a simple turn opener;
- keeping the floor briefly when needed;
- yielding after completing a small action;
- not replying with memorized content unrelated to the turn.

The exact latency threshold must remain task- and device-aware rather than becoming a universal “fast = fluent” rule.

## Listener behavior matters

Interaction is not only speaking. Learners need to display recipiency and shared understanding.

Near-A0 examples:

```text
okay
yeah
right
mm-hm
I see
really?
```

But backchannels should not be drilled as decorative fillers. They need to occur in relevant sequential positions and with plausible meaning.

Store:

```text
listener_response_type
contingency_to_prior_turn
position_in_sequence
```

## Repair is a core survival capability

Real conversation contains breakdowns in hearing, understanding and production. `SRC-0161` and broader interaction research treat repair as a central interactional mechanism.

Near-A0 learners should learn to keep a conversation alive with small routines:

```text
Sorry?
Again, please.
What does ___ mean?
Do you mean ___?
Seven or eleven?
I don't understand.
```

This may be more useful than forcing the learner to pretend they understood.

Candidate repair loop:

```text
problem detected
→ learner signals problem
→ partner clarifies/repeats/rephrases
→ learner confirms or responds
→ interaction continues
```

Evidence should distinguish:
- learner noticed a breakdown;
- learner initiated repair;
- repair strategy was appropriate;
- repaired input was understood;
- task progressed afterward.

## Do not punish repair as failure

A system that awards the highest score only for zero clarification requests encourages fake comprehension.

Sometimes:

```text
"Sorry, seven or eleven?"
```

is better evidence of interactional competence than guessing incorrectly.

Nếp should reward successful repair when the source turn was genuinely difficult/ambiguous while still tracking whether repeated repair signals an underlying listening problem.

## Topic and goal progressivity

Interaction should move somewhere. `SRC-0158`, `SRC-0161` and `SRC-0162` describe topic/sequence management and progressivity as relevant interactional phenomena.

For beginners, use concrete goals rather than abstract “chat for five minutes” tasks:

```text
order one drink
confirm the price
ask where the bathroom is
agree on a meeting time
report a delivery problem
ask for one missing item
```

The task can finish when the shared goal is accomplished.

This makes evidence interpretable:

```text
task_goal_completed
turns_required
repair_events
support_used
```

rather than measuring only conversation length.

## Interaction progression

### I0 — recognize action + bounded response

Example:

```text
Partner: "What's your name?"
Learner chooses/produces a known response.
```

Purpose:
link listening comprehension to a socially appropriate next action.

### I1 — single adjacency exchange

```text
question → answer
request → acceptance/decline
thanks → response
greeting → greeting
```

Learner generates the response with decreasing support.

### I2 — short goal sequence

2–4 learner turns in a predictable situation.

Example:

```text
A: What would you like?
B: Coffee, please.
A: Small or large?
B: Small.
A: Anything else?
B: No, thanks.
```

The learner must process each new turn rather than recite one long script.

### I3 — repair-enabled interaction

Introduce controlled uncertainty:
- one faster/unfamiliar token;
- one alternative formulation;
- one ambiguous number/name;
- one intentional clarification opportunity.

The learner can repair rather than fail silently.

### I4 — changed partner / changed realization

Same communicative function, different wording/voice/partner.

Example:

```text
"What do you want?"
"What would you like?"
"Can I get you anything?"
```

Learner must recognize the action, not memorize one trigger sentence.

### I5 — short open functional interaction

The partner can choose among bounded plausible next moves while the learner works toward a goal.

### I6 — human-transfer probe

When feasible for validation, the learner performs a parallel interaction with a human interlocutor or human-rated recording/live exchange.

AI-only success cannot substitute for this validation layer.

## Pragmatics is part of meaning

Pragmatics asks not only whether a sentence is grammatical but whether it performs an appropriate social action in context.

`SRC-0157` provides strong meta-analytic evidence that pragmatics instruction can improve pragmatic competence. `SRC-0168` emphasizes that speech acts belong inside turn-by-turn interaction rather than isolated phrase lists.

For Nếp, teach:

```text
FORM
+ FUNCTION
+ RELATIONSHIP/CONTEXT
+ SEQUENCE POSITION
```

Example:

```text
"Water."
```

may communicate a lexical meaning, but:

```text
"Could I have some water, please?"
```

serves a different pragmatic function/relationship in many contexts.

Do not reduce this to “one sentence is polite, one is rude.” Appropriateness is contextual and variable.

## Near-A0 pragmatic syllabus should be functional

Candidate high-value functions:
- greeting/closing;
- thanking/responding to thanks;
- simple requesting;
- accepting/declining;
- apologizing;
- asking permission;
- asking for repetition/clarification;
- confirming information;
- basic disagreement/correction;
- getting attention.

Each should be taught in small sequences, not as decontextualized vocabulary.

## Separate pragmalinguistic and sociopragmatic support

The learner may know **what** social action is needed but not know a usable English form.

Or the learner may know a form but use it in an unsuitable context.

Record separately:

```text
recognized_social_action
selected_appropriate_strategy
retrieved_target_expression
sequence_fit
```

Avoid a single opaque `politeness_score`.

## Corrective feedback inside interaction

Oral-feedback meta-analysis (`SRC-0060`) supports corrective feedback but does not justify interrupting every turn.

Nếp should protect interaction progressivity.

Candidate rule:

```text
if error blocks meaning/task
→ repair now

if target construction error is high-value
→ brief prompt/recast when interaction can continue

if low-value surface error
→ log and defer feedback until task boundary
```

Feedback must not transform every conversation into grammar interrogation.

## AI roleplay: what it is good for

AI/chatbot reviews and newer meta-analytic evidence (`SRC-0164`, `SRC-0165`, `SRC-0166`) support the potential of AI for increasing speaking opportunities and lowering practice barriers. `SRC-0167` provides directly relevant preliminary evidence with Vietnamese undergraduates.

Useful AI roles:
- always-available practice partner;
- bounded scenario partner;
- variable wording/voice generator;
- controlled follow-up question generator;
- repair practice partner;
- delayed retry partner;
- source of candidate feedback after the interaction.

This solves a real scarcity problem: one learner can practice more turns than classroom time often permits.

## AI roleplay: what it cannot prove

Voice-chatbot reviews report:
- ASR failures;
- unnatural interaction;
- weak or inconsistent corrective feedback;
- limited contextual/pragmatic sensitivity (`SRC-0164`, `SRC-0165`).

Broad GenAI meta-analysis is positive but highly heterogeneous and does not establish human-interaction transfer (`SRC-0166`).

Therefore:

```text
AI understood learner
≠
human listener would understand learner
```

and:

```text
learner completed AI scenario
≠
learner can manage unfamiliar human interaction
```

AI practice is a scaffolded environment whose transfer must be measured independently.

## Guard against over-accommodating AI

A language model can infer intended meaning from malformed output better than an ordinary interlocutor. That can hide communication weaknesses.

Example:

```text
Learner speech/transcript: "tomorrow seven go station me"
AI infers intended plan and continues perfectly.
```

The learner may receive no signal that a human listener could struggle.

Product rule:
- separate `model_interpreted_intent` from `listener-likelihood`;
- do not treat semantic inference by the LLM as intelligibility proof;
- validate a sample with human listeners;
- include changed human/stricter-interlocutor probes in `EXP-015`.

## Guard against AI carrying the conversation

AI can also hide interaction weakness by:
- asking all questions;
- elaborating the learner's one-word responses;
- repairing breakdowns without learner initiative;
- accepting off-topic responses;
- supplying vocabulary before the learner needs to retrieve it.

Log partner assistance:

```text
ai_question_count
ai_repair_initiations
ai_rephrases
ai_suggested_content
ai_supplied_language
learner_initiations
learner_repair_initiations
```

A conversation with heavy partner rescue is not equivalent to independent interaction.

## Interaction evidence model

```ts
type InteractionTurnEvidence = {
  interactionId: string;
  turnIndex: number;
  partnerType: "ai" | "human" | "peer";
  scenarioId: string;

  incomingActionId?: string;
  incomingMeaningTargets: string[];

  learnerResponse: string;
  responseContingency?: number;
  taskProgress?: number;
  pragmaticFit?: number;
  lexicalConstructionEvidence?: number;
  intelligibilityEvidence?: number;

  responseLatencyMs?: number;

  repairNeeded: boolean;
  repairInitiatedBy?: "learner" | "partner" | "system";
  repairStrategy?: string;
  repairResolved?: boolean;

  supportLevel: number;
  modelLanguageVisible: boolean;
  translationVisible: boolean;
};
```

At interaction level:

```ts
type InteractionEvidence = {
  goalCompleted: boolean;
  contingentTurnRate: number;
  successfulRepairRate?: number;
  learnerInitiations: number;
  partnerRescues: number;
  supportDependence: number;
};
```

These are candidate variables, not validated universal scoring formulas.

## Do not treat conversation length as mastery

Ten minutes chatting can consist of:
- AI monologues;
- one-word learner replies;
- repeated misunderstandings;
- copy-pasted suggestions.

Better questions:

```text
Did learner understand relevant turns?
Did responses fit prior turns?
Did the shared goal advance?
Could learner repair a breakdown?
Could learner use an appropriate social action?
Did the learner manage without supplied language?
```

## Interaction assessment must stay low enough inference

`SRC-0161` emphasizes the ratability challenge: some interaction qualities are context-dependent and hard to reduce to automatic scores.

Nếp should favor observable evidence over vague AI judgments.

Prefer:

```text
responded to requested time correctly
initiated clarification after ambiguous number
completed request sequence
```

before:

```text
conversation naturalness = 83
social confidence = 91
```

Do not ship those opaque scores without validation.

## Product integration

```text
Listening Engine
      ↓
incoming-turn perception/comprehension
      ↓
Interaction Engine
      ↓
Speaking + Pronunciation + Construction Engine
      ↓
response / repair
      ↓
Pragmatics layer
      ↓
shared goal progression
      ↓
Evidence Engine
      ↓
changed partner/context + delayed interaction
```

Interaction is where previously separate skills become coordinated in real time.

## Product decision

Create `FEAT-INT-001` — **Adaptive interaction progression engine**.

It should:
- present bounded communicative goals;
- require contingent response to actual prior turns;
- teach repair as a positive strategy;
- vary wording and partner behavior progressively;
- teach pragmatic actions in sequences;
- use AI for scalable rehearsal with provenance;
- record how much the partner rescued the learner;
- require changed-context and human-rated/human-partner transfer before treating AI performance as real interaction capability.

## Open assumptions

- exact first interaction stage for true A0 learners;
- exact number of turns per stage;
- response-latency expectations by task/device;
- when backchannels/listener responses should be taught;
- optimal repair-routine set and sequencing;
- frequency and difficulty of engineered breakdowns;
- how much partner rephrasing counts as support;
- exact pragmatic-function order for Vietnamese learners;
- treatment of cultural variation in appropriateness;
- AI strictness/accommodation policy;
- whether/how AI may intentionally misunderstand for repair practice;
- safe automated response-contingency scoring;
- safe automated pragmatic-feedback scoring;
- minimum human-listener/human-partner validation sample;
- transfer criteria from AI practice to human interaction;
- interaction review scheduling and delayed-probe interval.
