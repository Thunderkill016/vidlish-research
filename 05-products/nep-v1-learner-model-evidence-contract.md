# Nếp v1 — Learner model and evidence contract

**Status:** implementation-facing data/evidence decision layer  
**Depends on:** `SYN-SYS-001`, `ADR-001`

## 1. Purpose

Define what Nếp is allowed to believe about a learner, what observations can support those beliefs, and what the system must preserve so later decisions remain auditable.

The learner model is not a biography and not one proficiency number.

It is a structured set of provisional claims supported by evidence under known task conditions.

## 2. Core rule

```text
observation
+ task conditions
+ scorer provenance
→ evidence event
→ derived learner state
```

Never:

```text
lesson completed
→ mastered
```

or:

```text
AI says "good speaking"
→ speaking mastered
```

## 3. Evidence event as source of truth

```ts
type EvidenceEvent = {
  id: string;
  learnerId: string;

  capabilityIds: string[];
  targetIds: string[];
  construct: string;

  purpose:
    | "placement"
    | "learning"
    | "practice"
    | "independent_probe"
    | "transfer_probe"
    | "delayed_probe"
    | "repair";

  inputMode: string;
  responseMode: string;
  taskFamilyId: string;
  taskSpecVersion: string;

  novelty:
    | "trained-item"
    | "parallel-item"
    | "changed-context"
    | "new-context";

  firstSeen: boolean;
  delayedFromPriorExposureMs?: number;

  attemptBeforeFeedback: boolean;
  answerBearingSupportBeforeAttempt: boolean;
  supportEventIds: string[];

  outcome:
    | "success"
    | "partial"
    | "failure"
    | "invalid"
    | "unscored";

  outcomeDetails?: Record<string, unknown>;

  scorerType: "deterministic" | "human" | "asr" | "llm" | "hybrid";
  scorerVersion: string;
  scoringConfidenceBand?: "low" | "medium" | "high";

  occurredAt: string;
  policyVersion: string;
};
```

Exact implementation field names may change. The semantic distinctions must remain.

## 4. Evidence constructs

### Cross-cutting core

#### `understood`

Learner demonstrated meaning comprehension of target input under recorded support conditions.

Does not automatically mean the learner can produce it.

#### `recalled`

Learner retrieved the target without the full answer visible before the attempt.

Recognition and copying do not count.

#### `transferred`

Learner succeeded in a changed/unseen context where success could not reasonably be explained by exact-item memory alone.

The novelty requirement must be stored.

#### `retained`

Learner demonstrated the relevant capability after a meaningful delay.

Immediate post-teaching success is not retention.

## 5. Component/task-specific constructs

Candidate supported construct IDs:

```text
aural_form_recognition
spoken_message_comprehension
written_form_recognition
reading_message_comprehension
lexical_recall
chunk_recall
construction_interpretation
construction_production
short_utterance_production
controlled_recombination
guided_turn_response
interaction_contingency
interaction_repair
pronunciation_intelligibility
independent_micro_writing
writing_revision_transfer
fluency_effort
```

These are not assumed to be statistically independent latent traits. They are named evidence claims useful for decisions.

## 6. Evidence strength dimensions

A derived state should consider at least:

```text
independence
novelty
support dependence
delay
number of opportunities
recency
scorer reliability
task diversity
```

Avoid collapsing them into one opaque score when product decisions need the dimensions separately.

## 7. Derived target state

```ts
type TargetState = {
  targetId: string;

  observed: boolean;

  understanding?: EvidenceSummary;
  recall?: EvidenceSummary;
  transfer?: EvidenceSummary;
  retention?: EvidenceSummary;

  supportDependence?: SupportDependenceSummary;
  modalityEvidence: Record<string, EvidenceSummary>;

  lastIndependentAttemptAt?: string;
  lastSuccessAt?: string;
  lastFailureAt?: string;

  uncertaintyBand: "high" | "medium" | "low";
  currentEvidenceIds: string[];
};
```

No required `mastered: boolean`.

If implementation needs a fast routing flag, it must be explicitly derived from this richer state and versioned by policy.

## 8. Derived capability state

```ts
type CapabilityState = {
  capabilityId: string;
  observed: boolean;

  readinessBand: "unknown" | "not-ready" | "repairable" | "ready" | "stable";

  evidenceByModality: Record<string, EvidenceSummary>;
  changedContextEvidence?: EvidenceSummary;
  delayedEvidence?: EvidenceSummary;

  prerequisiteCoverageBand: "unknown" | "low" | "medium" | "high";
  supportDependenceBand: "unknown" | "high" | "medium" | "low";

  bottleneckIds: string[];
  evidenceIds: string[];
  statePolicyVersion: string;
};
```

`stable` means enough evidence for a current product decision, not permanent mastery.

## 9. Four-state observation rule

For any construct/capability, preserve:

```text
NOT_OBSERVED
UNCERTAIN
EVIDENCE_WEAK
EVIDENCE_STRONG
```

Do not merge `NOT_OBSERVED` and `EVIDENCE_WEAK`.

This is mandatory for cold-start placement.

## 10. Support provenance

A learner can succeed under different conditions:

```text
no support
image/context only
Vietnamese gloss
partial English cue
word bank
sentence frame
caption
transcript
full visible model
partner rephrase
AI hint
```

These successes are not interchangeable.

### Support dependence summary

Candidate internal representation:

```ts
type SupportDependenceSummary = {
  strongestIndependentSuccess?: string;
  minimumSupportForRecentSuccess?: string;
  answerBearingSupportOftenRequired: boolean;
  evidenceIds: string[];
};
```

Do not infer a learner-wide dependency from one difficult task.

## 11. Placement evidence

Placement evidence is allowed to initialize routing state but has lower durability than normal delayed learning evidence.

Rules:

- placement success cannot create `retained`;
- self-report creates no direct evidence event;
- untested modality remains not observed;
- first normal sessions can rapidly override placement estimates;
- route correction is logged explicitly.

## 12. Rehearsal versus independent production

For speaking/writing:

```text
exact answer/model visible during response
→ supported/rehearsal evidence
```

```text
model hidden before attempt
+ attempt occurs before feedback
→ candidate independent production evidence
```

A post-reveal correct retry does not delete the original failure.

## 13. Listening evidence

Listening task records enough conditions to avoid transcript masking.

Candidate fields:

```text
audio_source_type
voice_id / speaker_id
speech_rate_band
replay_count_before_answer
caption_visible
transcript_visible
Vietnamese_support_visible
```

If transcript was visible before response, do not call the result unsupported listening comprehension.

## 14. Pronunciation evidence

Pronunciation claims are separated from accent judgments.

Potential evidence:

```text
intended word/message identified by listener
specific contrast preserved where communicatively relevant
repair requested due to pronunciation
listener success across changed words/contexts
```

Do not store "native-like" as the goal.

ASR-derived observations retain provider/model/task provenance and cannot silently become listener-intelligibility truth.

## 15. Interaction evidence

Interaction evidence requires a prior partner turn and a learner response whose appropriateness/meaning depends on it.

Candidate fields:

```text
partner_turn_id
partner_support_level
partner_rephrase_count
learner_response_contingent
repair_opportunity
repair_success
```

A memorized script can be practice without proving contingent interaction.

## 16. Writing evidence

Distinguish:

```text
copying
reconstruction
frame-completion
independent micro-writing
revision after feedback
new-task writing transfer
```

Corrected current text is not automatically future writing capability.

## 17. Fluency evidence

Temporal metrics can include:

```text
response latency
pause pattern
speech duration
reading duration
repair/disfluency observations
```

But speed is interpreted alongside task familiarity, accuracy, meaning and context.

Same-task speedup is not broad fluency transfer.

## 18. Engagement data separation

Store product behavior separately from learner evidence.

Examples:

```text
session_started
session_completed
time_on_app
streak_day
notification_opened
video_watched
hint_clicked
```

These can inform product behavior and opportunity-to-learn but do not directly update language evidence.

If a future model predicts learning from behavioral data, it still requires validation and explicit claim boundaries.

## 19. Snapshot update policy

Evidence events are append-oriented.

Derived state is recomputed or incrementally updated using a versioned policy.

```text
Evidence events
→ State policy v7
→ Learner snapshot v104
```

A later state-policy change can re-evaluate prior evidence without rewriting the raw event history.

## 20. Conflict handling

Contradictory evidence is normal.

Example:

```text
success yesterday
failure today with new speaker
```

Do not overwrite one with the other.

Instead update uncertainty/support/task-generalization state.

Useful conflict reasons:

```text
speaker novelty
context novelty
support difference
delay
fatigue/device issue
scoring uncertainty
true instability
```

## 21. Evidence expiry versus forgetting

Evidence does not need to be deleted because it is old.

Its weight for current routing may decay.

Historical evidence remains useful for learning trajectories and scheduler evaluation.

Do not equate lower current confidence with proof that knowledge was erased.

## 22. Privacy/minimization

The evidence model should not require indefinite storage of raw audio, full AI conversation transcripts or unnecessary personal text.

Separate:

```text
raw artifact retention policy
from
derived evidence retention policy
```

Where possible, retain the minimal scored observations/provenance needed for learner decisions after raw-artifact expiry.

Exact retention/deletion rules remain a product/legal policy decision.

## 23. Evidence query examples

### Can the learner independently recall this chunk?

Query recent events where:

```text
construct = chunk_recall
attemptBeforeFeedback = true
answerBearingSupportBeforeAttempt = false
```

### Do we have transfer evidence?

Require events with:

```text
novelty in [parallel-item, changed-context, new-context]
purpose = transfer_probe or an explicitly transfer-valid learning task
```

### Do we have retention evidence?

Require:

```text
delayedFromPriorExposureMs >= policy-defined meaningful delay
```

The exact delay is policy-dependent, not hard-coded here.

## 24. Anti-corruption rules

The following external/provider values cannot be written directly into the authoritative learner state:

```text
LLM holistic level
ASR confidence
vendor pronunciation score
video completion
quiz percentage
course level
streak
self-rated CEFR
```

They may become contextual observations only through a documented adapter and validation rule.

## 25. Acceptance criteria

The learner model is valid for Nếp v1 when:

1. supported and unsupported success can be separated;
2. rehearsal and independent production can be separated;
3. trained-item and changed-context evidence can be separated;
4. immediate and delayed evidence can be separated;
5. unobserved and weak can be separated;
6. listening and text evidence can diverge without contradiction;
7. placement can initialize but not permanently dominate state;
8. scorer/provider versions are traceable;
9. engagement telemetry cannot directly create language mastery;
10. every learner-facing progression decision can cite the evidence/state fields that justified it.
