---
id: FEAT-CUR-001
title: Adaptive capability curriculum orchestrator
status: research-backed-candidate
research_question: RQ-017
synthesis: SYN-CUR-001
experiment: EXP-017
---

# FEAT-CUR-001 — Adaptive capability curriculum orchestrator

## Learner problem

A comprehensive English product can fail in two opposite ways:

1. it fragments English into disconnected skill/features;
2. it overloads beginners by trying to train every skill and language component in every session.

Nếp needs a curriculum layer that can make the learner experience feel like **one useful piece of English**, while preserving enough diagnostic structure underneath to know what the learner actually understands, remembers and can use.

## Target capability

Select and assemble the next smallest useful learning experience that advances a practical communicative capability, given the learner's current prerequisite evidence, without introducing avoidable overload or masking weak components with support.

## Research basis

Primary:
- `SYN-CUR-001`
- `PRN-213`–`PRN-228`
- `SRC-0001` CEFR action-oriented framework
- `SRC-0007` Four Strands
- `SRC-0183`–`SRC-0189` task/program/complexity/planning evidence
- `SRC-0123` comprehension versus production evidence

The orchestrator must also compose rather than replace:
- `FEAT-VOC-001`
- `FEAT-SCF-001`
- `FEAT-LIS-001`
- `FEAT-REV-001`
- `FEAT-TRN-001`
- `FEAT-SPK-001`
- `FEAT-PRN-001`
- `FEAT-GRM-001`
- `FEAT-READ-001`
- `FEAT-WRI-001`
- `FEAT-INT-001`
- `FEAT-FLU-001`

## Non-goals

This feature is not:
- a fixed CEFR textbook sequence;
- a lesson-count progression;
- a `do all four skills every day` rule;
- a hard-coded 25/25/25/25 Four-Strands timer;
- a generic LLM deciding what feels useful;
- a single combined English mastery score;
- a reason to duplicate logic already owned by modality-specific engines;
- proof that TBLT is universally superior.

## Architecture position

```text
                    Curriculum Orchestrator
                             │
             learner state + capability graph
                             │
          choose capability + primary bottleneck
                             │
                choose task complexity vector
                             │
             choose allowed support + evidence
                             │
      ┌───────────────┬──────┴────────┬───────────────┐
      ▼               ▼               ▼               ▼
 Listening        Language        Production      Interaction
  engine          engines           engines          engine
                    │                                  │
           vocab / grammar /                     speaking / repair
            pronunciation
      │               │               │               │
      └───────────────┴──────┬────────┴───────────────┘
                             ▼
                       Evidence Engine
                             │
                  review / transfer / next step
```

The orchestrator decides **what next and why**. Existing engines decide **how their specific learning operation works**.

## Capability node

```ts
type CapabilityNode = {
  id: string;
  canDo: string;
  domain: "personal" | "daily-life" | "service" | "travel" | "work" | "online" | "other";

  scenarios: string[];

  prerequisites: {
    capabilities: string[];
    vocabularyIds: string[];
    chunkIds: string[];
    constructionIds: string[];
    listeningTargetIds?: string[];
    pronunciationTargetIds?: string[];
    pragmaticFunctionIds?: string[];
  };

  modalities: Array<"listening" | "speaking" | "reading" | "writing" | "interaction">;
  transferFamilies: string[];
  complexityBands: string[];
};
```

Example:

```yaml
id: CAP-ORDER-DRINK-01
canDo: Can order one familiar drink and answer a simple size question.
prerequisites:
  vocabularyIds: [coffee, tea, small, large]
  chunkIds: [id-like]
  constructionIds: [want-request-basic]
  listeningTargetIds: [small-or-large]
modalities:
  - listening
  - speaking
  - interaction
```

The graph should not assume every prerequisite must be independently mastered before first exposure. It is a readiness model, not a rigid lock tree.

## Learner capability state

```ts
type CapabilityState = {
  capabilityId: string;

  prerequisiteCoverage: number;
  evidenceByModality: Record<string, EvidenceSummary>;
  supportDependence: Record<string, number>;
  changedContextEvidence: EvidenceSummary;
  delayedEvidence: EvidenceSummary;

  currentBottlenecks: Bottleneck[];
  nextCandidateChallenges: ChallengeCandidate[];
};
```

No field such as:

```ts
passed: true
```

should replace the richer evidence.

## Primary bottleneck

A unit should declare one **primary** learning bottleneck whenever feasible.

Candidate values:

```text
meaning_not_understood
sound_form_not_recognized
word_chunk_not_recalled
construction_mapping_unstable
pronunciation_hurts_intelligibility
reading_form_not_accessible
writing_retrieval_unstable
interaction_response_not_contingent
repair_missing
fluency_effort_high
transfer_not_demonstrated
retention_due
```

Secondary challenges may exist but should not silently become equally novel.

## Unit contract

```ts
type CurriculumUnitSpec = {
  capabilityId: string;
  primaryBottleneck: string;
  primaryModality: string;
  secondaryModalities: string[];

  targetIds: string[];
  prerequisiteSnapshotId: string;

  taskFamilyId: string;
  taskComplexity: TaskComplexity;

  allowedSupport: SupportPolicy;
  firstAttemptPolicy: FirstAttemptPolicy;

  evidenceExpected: EvidenceContract[];
  changedContextProbe?: ProbeSpec;
  delayedContinuation?: ContinuationSpec;
};
```

## Task complexity vector

```ts
type TaskComplexity = {
  lexicalNovelty: number;
  constructionNovelty: number;
  inputLength: number;
  inputRate: number;
  propositionCount: number;
  inferenceDemand: number;
  outputLength: number;
  interactionTurns: number;
  partnerOrVoiceNovelty: number;
  supportReduction: number;
  timePressure: number;
  contextNovelty: number;
};
```

Each dimension should have an interpretable product definition. Avoid fake decimal precision until validated.

## Near-A0 assembly rule

Candidate default:

```text
one major new learning burden
+ mostly known supporting language
+ smallest useful support
```

Example:

If new target is understanding `Small or large?`, do not simultaneously require:
- three unknown drink names;
- a new tense construction;
- fast unfamiliar accent;
- free multi-turn production;
- a new written form;
- no support.

The exact overload threshold belongs to `EXP-017`.

## First-attempt policy

The system should prefer an informative first attempt before giving the strongest support when safe and humane.

Example:

```text
hear short question
→ meaning attempt
→ if fail: smaller support
→ diagnose bottleneck
→ targeted learning
```

Do not expose a full model, translation and answer before collecting any evidence if the learner could reasonably attempt the task.

## Input → language focus → output is adaptive, not fixed

Candidate near-A0 default:

```text
processable input
→ meaning attempt
→ focus on useful target
→ retrieval
→ constrained output
→ changed use
```

But the orchestrator may enter at another point when evidence says so:

```text
retention due
→ retrieval first
```

or:

```text
known language, interaction weak
→ interaction task first
```

or:

```text
reading form weak, meaning already known
→ orthographic mapping task
```

The sequence is state-driven, not one immutable lesson template.

## Planning and scaffolding

Allowed support types can include:
- scenario preview;
- image/context grounding;
- English model;
- Vietnamese meaning support;
- word bank;
- sentence frame;
- planning time;
- rehearsal;
- replay;
- transcript/caption;
- partner rephrase;
- pronunciation comparator.

Every support event must be provenance-visible to the Evidence Engine.

```ts
type SupportEvent = {
  type: string;
  strength: number;
  beforeAttempt: boolean;
  learnerRequested: boolean;
};
```

## Primary and secondary modalities

Example listening-led unit:

```yaml
primaryModality: listening
secondaryModalities:
  - speaking
  - chunk_retrieval
```

Primary means:
- the major new burden is there;
- the main success metric is there;
- secondary modalities should be sufficiently supported/known not to confound diagnosis.

Later the same capability can return with another primary modality.

## Spiral scheduling

A capability may have a trajectory like:

```text
encounter in listening
→ retrieve as short speech
→ changed speaking use
→ read short related message
→ interact with follow-up
→ write related practical message
→ fluency consolidation
```

Do not hard-code this exact order for every capability.

Store:

```ts
type CapabilityEncounter = {
  capabilityId: string;
  modality: string;
  contextId: string;
  noveltyLevel: number;
  supportLevel: number;
  occurredAt: string;
};
```

## Four-Strands rolling audit

Internal only:

```ts
type CurriculumBalanceWindow = {
  windowStart: string;
  windowEnd: string;

  meaningFocusedInputMinutes: number;
  meaningFocusedOutputMinutes: number;
  languageFocusedLearningMinutes: number;
  fluencyDevelopmentMinutes: number;

  listeningOpportunities: number;
  speakingOpportunities: number;
  readingOpportunities: number;
  writingOpportunities: number;
  interactionOpportunities: number;
};
```

Use this to detect starvation or overconcentration.

Do not display:

```text
You are 25% behind on output
```

and do not count balance as mastery.

## Balance correction

If a rolling window shows a major curriculum imbalance, the orchestrator may raise the priority of an underrepresented learning condition **only when a suitable capability/task is ready**.

Bad:

```text
Need more writing minutes
→ force random writing task
```

Better:

```text
writing has been underrepresented
+ learner has a ready capability with known language
→ select related practical micro-writing continuation
```

Learning relevance outranks quota filling.

## Complexity progression

Candidate operation:

```ts
function nextChallenge(current, learner) {
  const candidates = generateSafeIncrements(current);
  return rankByExpectedLearningValue(candidates, learner);
}
```

Safe increments may include one or two of:
- one new lexical slot;
- one less scaffold;
- one extra proposition;
- one extra interaction turn;
- changed speaker;
- changed context;
- slightly longer input;
- reduced planning;
- later, modest time pressure.

Avoid increasing all simultaneously unless the purpose is a deliberate transfer assessment.

## Capability merging

Two capabilities can later merge into a larger scenario.

Example:

```text
CAP: order a drink
+
CAP: understand price
+
CAP: clarify misunderstanding

↓

SCENARIO: complete a short café transaction
```

Merge only when component capabilities have enough evidence that the combined task measures integration rather than simply overwhelming the learner.

## Dispatch to existing engines

### Vocabulary / chunks
Use `FEAT-VOC-001` for knowledge evidence and retrieval.

### Vietnamese support
Use `FEAT-SCF-001`; curriculum does not invent its own translation rules.

### Listening
Use `FEAT-LIS-001` for perception/comprehension diagnosis.

### Grammar/constructions
Use `FEAT-GRM-001` for form-meaning-use learning.

### Pronunciation
Use `FEAT-PRN-001` for intelligibility priorities.

### Speaking
Use `FEAT-SPK-001` for guided production progression.

### Reading
Use `FEAT-READ-001` for connected reading progression.

### Writing
Use `FEAT-WRI-001` for meaningful writing/revision progression.

### Interaction
Use `FEAT-INT-001` for turn-taking, contingency, repair and pragmatics.

### Fluency
Use `FEAT-FLU-001` only after readiness for automaticity practice.

### Review and transfer
Use `FEAT-REV-001` and `FEAT-TRN-001` rather than duplicating scheduling/probe logic.

## Evidence contract

Integrated learner experience must produce decomposable evidence.

Example:

```ts
[
  { type: "understood", modality: "listening", target: "small-or-large" },
  { type: "recalled", modality: "speaking", target: "id-like" },
  { type: "intelligibility", modality: "speaking", target: "small" },
  { type: "interaction_contingency", target: "size-response" }
]
```

Do not create:

```ts
{ lessonPassed: true, mastery: 0.86 }
```

as the primary knowledge model.

## Support masking checks

Before promoting capability state, ask:
- Was translation visible before meaning response?
- Was exact speech model visible before production?
- Did captions replace listening?
- Did AI partner rephrase until answer became obvious?
- Did a word bank contain the entire response?
- Was text reread enough times to create item familiarity?

Supported success can be useful learning evidence but should be labeled correctly.

## Progression ranking

Candidate ranking inputs:

```text
expected learning value
prerequisite readiness
retention urgency
transfer gap
curriculum starvation risk
learner-relevant utility
estimated cognitive load
estimated session cost
```

Do not rank only by:
- content novelty;
- engagement prediction;
- streak continuation;
- what an LLM says is interesting.

## Learner choice

Learner agency may alter scenario/topic selection when several candidates are pedagogically valid.

Example:

```text
system: 3 equally ready request capabilities
learner: prefers food/travel topic
→ choose matching scenario
```

Learner choice should not bypass critical prerequisites or falsely mark skipped capabilities as mastered.

Exact degree of choice belongs to `EXP-017`.

## Task-first versus model-first

Both are supported as candidate policies.

### Task-first

```text
attempt bounded task
→ diagnose
→ teach minimum needed
→ retry
```

Benefits:
- informative baseline;
- relevance of learning becomes clear.

Risks:
- frustration if task is too far beyond readiness.

### Model-first

```text
comprehensible model/input
→ meaning work
→ target focus
→ attempt
```

Benefits:
- lower initial burden;
- useful for truly novel near-A0 targets.

Risks:
- can hide baseline and promote imitation.

The orchestrator should not hard-code one globally. `EXP-017` should test readiness-dependent routing.

## Curriculum health versus learner mastery

Curriculum health asks:

```text
Has the program provided enough kinds of useful learning opportunities?
```

Mastery asks:

```text
What can this learner understand, retrieve, transfer and retain?
```

These must use different models/tables/metrics.

## Suggested data entities

```text
capability
capability_prerequisite
capability_scenario
learner_capability_state
curriculum_unit
curriculum_unit_target
curriculum_attempt
support_event
task_complexity_snapshot
capability_encounter
curriculum_balance_window
```

Avoid prematurely storing one authoritative `current_level` as the decision source.

## Product surfaces

The learner UI should feel simple:

```text
Today
Continue: Order a drink
```

not expose the orchestration machinery.

Possible path view:

```text
Everyday basics
✓ Say who you are
✓ Ask for a simple item
△ Handle a simple café choice
○ Understand a basic price
```

Progress can show capabilities with evidence quality, while internal component diagnostics remain available for engine decisions.

## Learning metrics

Primary product-level metric:

```text
delayed changed-context capability gain
──────────────────────────────────────
learning minutes
```

Component metrics remain those defined by modality engines.

Curriculum metrics:
- prerequisite violation rate;
- overload failure rate;
- support dependence;
- changed-context transfer rate;
- delayed retention;
- component diagnostic accuracy;
- modality/strand starvation;
- time to capability evidence;
- abandoned-session rate.

Engagement remains secondary.

## Falsification

Redesign or weaken `FEAT-CUR-001` if:
- capability-centered sequencing does not improve delayed changed-context performance over a simpler curriculum;
- the primary-bottleneck heuristic frequently chooses the wrong cause of failure;
- integrated tasks hide weak components and lead to poor next-item decisions;
- rolling balance produces low-value quota-filling activities;
- simple-to-complex increments under-challenge learners or slow progression;
- non-monotonic/adaptive task sequences outperform the assumed gradual sequence;
- task-first frustrates true beginners without improving diagnostic value;
- model-first creates imitation without transfer;
- prerequisite graphs become brittle or require excessive manual authoring;
- a much simpler fixed curriculum achieves equivalent learning per minute.

## Experiment

See `EXP-017`.
