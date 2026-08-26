# Nếp v1 — Runtime architecture and engine contracts

**Status:** implementation-facing architecture  
**Depends on:** `SYN-SYS-001`, `05-products/nep-v1-executable-product-spec.md`

## 1. Architecture goal

Make learning decisions traceable and replaceable.

The architecture must let the application answer:

```text
Why did this learner get this task now?
What support was allowed and actually shown?
What did the learner demonstrate before feedback?
Which engine is allowed to update which state?
What evidence would reverse the current decision?
```

If those questions cannot be answered from stored data, the architecture is too opaque.

## 2. Logical components

```text
Client
  │
  ▼
Learning API / Orchestration boundary
  │
  ├── Placement Service
  ├── Learner Model Service
  ├── Capability/Curriculum Service
  ├── Session Planner
  ├── Task Runtime
  ├── Support Policy Service
  ├── Evidence Service
  ├── Review/Transfer Service
  ├── Recovery Service
  └── AI Reliability Gateway
          ├── LLM
          ├── ASR
          └── TTS
```

These are logical boundaries. Nếp v1 may implement them in one application/backend rather than separate network microservices.

Do **not** create distributed-system complexity merely because the responsibilities are separated here.

## 3. Ownership rules

### Placement Service

Owns:

- placement priors;
- anchor/probe routing;
- provisional start recommendation;
- route uncertainty;
- early recalibration flags.

Does not own:

- durable mastery;
- review scheduling after normal learning is underway;
- global CEFR truth.

### Learner Model Service

Owns derived learner-state views built from evidence.

It does not invent evidence.

### Capability/Curriculum Service

Owns:

- capability graph;
- prerequisite definitions;
- candidate-next generation;
- primary bottleneck selection;
- task complexity decisions;
- curriculum balance audit.

Does not own modality-specific scoring.

### Session Planner

Turns a learner snapshot and a selected capability into a bounded session plan.

It may compose existing engines but should not duplicate their domain rules.

### Task Runtime

Owns:

- presenting a task;
- capturing attempt before reveal;
- applying support events;
- storing response artifacts required by scorer policy;
- requesting scoring;
- generating task outcome events.

### Support Policy Service

Owns which supports are allowed/triggered for the current task condition.

Every support event is observable by Evidence Service.

### Evidence Service

Owns immutable or append-oriented evidence records and scoring provenance.

It is the only boundary allowed to convert task outcomes into learner evidence records.

### Review/Transfer Service

Owns:

- when a target/capability deserves another evidence opportunity;
- review candidate ranking;
- changed-context probe selection;
- delayed-probe scheduling.

It does not claim retention merely because an item was scheduled.

### Recovery Service

Owns re-entry after absence:

- compress overdue work;
- select a small diagnostic return task;
- trigger recalibration when evidence changed;
- avoid punishment/backlog dumping.

### AI Reliability Gateway

All LLM/ASR/TTS calls that can affect learning content, feedback or evidence pass through this gateway.

The gateway owns:

- provider/model/prompt version;
- role policy;
- allowed learner data;
- validator pipeline;
- abstention/fallback;
- cost/latency telemetry;
- regression-test compatibility.

## 4. Canonical request flow

### Start or resume learning

```text
GET /learning/next
  ↓
load learner snapshot
  ↓
placement/recovery check
  ↓
review urgency check
  ↓
curriculum candidate generation
  ↓
rank candidate action
  ↓
create SessionPlan / TaskSpec
  ↓
return learner-facing task
```

### Submit attempt

```text
POST /attempts
  ↓
validate task/session version
  ↓
record raw attempt
  ↓
run scorer policy
  ↓
record support provenance
  ↓
create evidence event(s)
  ↓
update derived learner snapshot
  ↓
return feedback + next task instruction
```

The client must not compute durable learner mastery locally.

## 5. Core domain types

```ts
type Modality =
  | "listening"
  | "speaking"
  | "reading"
  | "writing"
  | "interaction"
  | "multimodal";

type EvidencePurpose =
  | "placement"
  | "learning"
  | "practice"
  | "independent_probe"
  | "transfer_probe"
  | "delayed_probe"
  | "repair";

type EvidenceConstruct =
  | "understood"
  | "recalled"
  | "transferred"
  | "retained"
  | "aural_form_recognition"
  | "reading_comprehension"
  | "construction_mapping"
  | "short_utterance_production"
  | "pronunciation_intelligibility"
  | "interaction_contingency"
  | "interaction_repair"
  | "independent_writing"
  | "fluency_effort";
```

The actual implementation may use extensible IDs rather than a closed enum, but every value must have a documented interpretation.

## 6. Learner snapshot

```ts
type LearnerSnapshot = {
  learnerId: string;
  version: number;

  placement?: PlacementSummary;
  capabilityStates: Record<string, CapabilityState>;
  targetStates: Record<string, TargetState>;

  dueEvidence: DueEvidence[];
  activeCapabilities: string[];
  currentBottlenecks: Bottleneck[];

  supportProfile: SupportProfile;
  deviceContext?: DeviceContext;

  lastUsefulSessionAt?: string;
  recoveryState?: RecoveryState;
};
```

Snapshots are derived/cacheable views. Evidence events remain the auditable source.

## 7. Capability candidate contract

```ts
type CapabilityCandidate = {
  capabilityId: string;
  readiness: "not-ready" | "repairable" | "ready" | "already-easy";
  readinessReasons: string[];

  expectedLearningValueBand: "low" | "medium" | "high";
  retentionUrgencyBand: "none" | "low" | "medium" | "high";
  transferGapBand: "unknown" | "low" | "medium" | "high";
  estimatedBurdenBand: "low" | "medium" | "high";

  viablePrimaryBottlenecks: string[];
  viableModalities: Modality[];
};
```

Avoid fake decimal precision before data justifies it.

## 8. Ranking policy

A policy should return both selection and reasons.

```ts
type NextActionDecision = {
  actionType:
    | "placement_probe"
    | "learn_capability"
    | "review"
    | "transfer_probe"
    | "prerequisite_repair"
    | "recovery_probe"
    | "continue_session";

  capabilityId?: string;
  targetIds?: string[];
  policyVersion: string;
  reasons: DecisionReason[];
};
```

Candidate decision reason examples:

```text
RETENTION_DUE
PLACEMENT_UNCERTAINTY_HIGH
ACTIVE_CAPABILITY_BOTTLENECK
TRANSFER_EVIDENCE_MISSING
PREREQUISITE_FAILED
CAPABILITY_TOO_EASY
SESSION_TIME_LIMIT
LEARNER_TOPIC_PREFERENCE
```

## 9. Task lifecycle

```text
CREATED
→ PRESENTED
→ ATTEMPTED
→ SCORED
→ FEEDBACK_SHOWN
→ COMPLETED
```

Optional branches:

```text
ATTEMPTED → SUPPORT_SHOWN → RETRY
ATTEMPTED → SCORER_ABSTAINED → FALLBACK
PRESENTED → SKIPPED
```

The original independent attempt must remain stored even if the learner later corrects the response after reveal.

## 10. Support event contract

```ts
type SupportEvent = {
  id: string;
  attemptId: string;
  supportType: string;
  strengthBand: "minimal" | "partial" | "answer-bearing";
  trigger: "learner" | "policy" | "teacher" | "system-repair";
  shownBeforeIndependentAttempt: boolean;
  createdAt: string;
};
```

The scorer/evidence layer must be able to ask whether answer-bearing support existed before the response.

## 11. Scorer contract

```ts
type ScorerRequest = {
  taskSpecId: string;
  taskVersion: string;
  attemptArtifact: AttemptArtifact;
  acceptedVariants?: AcceptedVariant[];
  scorerPolicyId: string;
};

type ScorerResult = {
  status: "scored" | "abstain" | "invalid";
  outcomes: ScoredOutcome[];
  scorerType: "deterministic" | "human" | "asr" | "llm" | "hybrid";
  scorerVersion: string;
  confidenceBand?: "low" | "medium" | "high";
  flags: string[];
};
```

For high-value evidence, `abstain` is preferable to fabricated certainty.

## 12. Evidence ingestion rules

Before creating evidence, validate:

```text
Was there a genuine learner attempt?
Was the intended construct actually elicited?
Was answer-bearing support already visible?
Was the response mode appropriate to the claim?
Was the task trained, parallel, changed-context or delayed?
Did the scorer have authority for this claim?
```

If not, downgrade or do not emit the claim.

## 13. Review scheduling boundary

Review scheduler input:

```ts
type ReviewCandidate = {
  targetId: string;
  capabilityIds: string[];
  lastIndependentEvidenceAt?: string;
  lastDelayedEvidenceAt?: string;
  lastOutcomeBand?: string;
  supportDependenceBand?: string;
  changedContextGap?: boolean;
  estimatedOpportunityCostBand: string;
};
```

Output is a **candidate evidence opportunity**, not a mastery update.

## 14. Placement integration

At account creation:

```text
Placement Service
→ creates provisional evidence/profile
→ recommends first capability/support
```

After learning starts:

```text
Evidence Service
→ normal evidence updates
→ Learner Model
→ may trigger PLACEMENT_TOO_EASY / TOO_HARD event
→ Curriculum Service reroutes
```

There is no separate permanent onboarding learner model.

## 15. Recovery integration

If the learner has been absent beyond a configurable threshold:

```text
normal next-action selection
→ recovery policy intercepts
→ selects smallest high-value evidence opportunity
→ state re-estimated
→ backlog compressed/ranked
```

The exact absence threshold is configuration, not a scientific constant.

## 16. AI gateway roles

```ts
type AIRolePolicy = {
  id: string;
  role: string;
  providerModelAllowlist: string[];
  canGenerateLearnerFacingContent: boolean;
  canAffectEvidence: boolean;
  requiredValidators: string[];
  fallbackPolicyId: string;
  learnerDataFieldsAllowed: string[];
  retentionPolicyId: string;
};
```

Examples:

### Example generation

May generate candidate distractors/examples, but deterministic lexical/target constraints should validate output before delivery.

### Feedback

May propose concise feedback. It does not overwrite deterministic evidence outcomes.

### Conversation partner

May generate partner turns under a state machine. Interaction evidence should be based on learner response behavior, not the model's subjective global rating.

### ASR

May provide transcript/feature observations only under task/provider policies validated for the slice.

### TTS

May render controlled input. Voice/model/version is stored with the task exposure.

## 17. Configuration over hard-coded truth

The following belong in versioned policy/configuration:

- placement minimum/maximum items;
- placement uncertainty threshold;
- session duration bands;
- support fading thresholds;
- review timing parameters;
- transfer sampling frequency;
- capability prerequisites;
- task complexity increments;
- scorer confidence thresholds;
- AI provider/model selection;
- recovery thresholds.

Changing these should be observable in experiment data.

## 18. Minimum persistence model

Candidate tables/collections:

```text
learner
learner_preference
capability
capability_prerequisite
capability_target
scenario
learning_target

task_spec
task_instance
session_plan
session
attempt
support_event
scorer_result
evidence_event

learner_capability_snapshot
learner_target_snapshot

review_candidate
placement_prior
placement_attempt
placement_decision

ai_call_provenance
policy_version
experiment_assignment
```

Do not over-normalize before implementation constraints are known, but preserve these semantic boundaries.

## 19. Versioning requirements

Every learner-affecting decision must be attributable to versions of:

- capability content;
- task spec;
- scorer policy;
- support policy;
- curriculum policy;
- review policy;
- placement policy;
- AI model/prompt where relevant.

Without this, experiment results become uninterpretable after content/model changes.

## 20. Observability requirements

Internal debug view for one learner should be able to reconstruct:

```text
current candidate capabilities
why one was chosen
what task was generated
what support appeared
what learner attempted
what scorer returned
what evidence was emitted
what learner state changed
what next action was selected
```

This debug trace is a product-development requirement, not a learner-facing feature.

## 21. Failure-safe principles

When a component is uncertain:

- placement chooses a conservative learnable route;
- scorer abstains rather than awarding mastery;
- AI falls back to deterministic/editorial content;
- missing modality stays unknown;
- review does not flood backlog;
- curriculum lowers complexity after repeated prerequisite failure;
- the client still allows a useful learning path when optional AI/video services fail.

## 22. Architecture acceptance criteria

The implementation architecture is faithful to the research layer when:

1. no global `currentLevel` is required to choose every task;
2. independent attempts and post-reveal retries are distinguishable;
3. support provenance is queryable;
4. evidence is decomposable by construct/modality/task condition;
5. placement can be corrected by normal learning evidence;
6. review scheduling cannot directly set mastery;
7. AI calls that affect learning are role/version/provenance-gated;
8. a learner can progress through the core A0 loop without authentic video or unrestricted AI chat;
9. next-action decisions have inspectable reasons;
10. policy parameters can be experimentally changed without rewriting core domain semantics.
