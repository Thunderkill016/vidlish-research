# FEAT-ONB-001 — Progressive placement and learner-model bootstrap

**Feature ID:** `FEAT-ONB-001`  
**Research question:** `RQ-021`  
**Status:** research-backed candidate  
**Primary synthesis:** `SYN-PLC-001`

## Purpose

Get a new learner into an appropriately challenging Nếp learning path with the smallest defensible amount of pre-learning assessment, while preserving uncertainty and continuing calibration during normal learning.

## Non-goals

This feature is not:

- a certification exam;
- a permanent CEFR classifier;
- a replacement for delayed mastery evidence;
- an AI-generated holistic English score;
- a requirement to test every modality before the learner sees a lesson.

## Core contract

```text
Placement chooses a next learning region.
It does not certify what the learner permanently knows.
```

## Data model

### `placement_prior`

```text
user_id
l1
prior_exposure_band
concrete_self_assessment
learning_goal
alphabet_comfort
available_modalities
created_at
```

### `placement_attempt`

```text
user_id
item_id
construct
capability_ids
input_mode
response_mode
support_level
correct / rubric_result
latency_ms
confidence_if_collected
attempted_at
```

### `placement_profile_estimate`

```text
user_id
construct
estimate_band
uncertainty
support_conditions
source_attempt_ids
updated_at
```

### `placement_decision`

```text
user_id
recommended_start_capability
recommended_support_level
primary_mode
alternate_route
route_uncertainty
overplacement_risk
underplacement_risk
missing_constructs
created_at
```

## Pipeline

```text
1. PRIOR
2. COMMON ANCHORS
3. ADAPTIVE FRONTIER PROBES
4. DECISION
5. FIRST REAL LESSON
6. EARLY-SESSION RECALIBRATION
```

## 1. Prior

Use only cheap information that can alter item routing.

Rules:

- never mark a construct mastered from self-report;
- never skip all direct listening evidence because a learner says they listen well;
- allow learner history to select a more informative first branch;
- log the prior separately from observed evidence.

## 2. Common anchors

Candidate blueprint:

| Construct | Example elicitation | What success supports |
| --- | --- | --- |
| spoken form → meaning | hear familiar word/chunk + choose image/meaning | aural recognition |
| written form → meaning | read familiar word/chunk + choose image/meaning | written recognition |
| short listening message | hear micro-message + choose intended meaning | basic listening comprehension |
| short written message | read micro-message + choose meaning | basic reading comprehension |
| construction meaning | interpret high-frequency pattern in context | form-meaning construction evidence |
| small retrieval | answer/reconstruct without visible target | initial recall evidence |

The exact minimum blueprint is experimental.

## 3. Adaptive frontier probes

Each next probe must answer:

```text
Could this result change the recommended next learning route?
```

If no, do not administer it during cold start.

Example routing:

```text
written strong + audio weak
→ spoken-form / segmentation probe

recognition strong + recall unknown
→ low-support retrieval probe

anchors uniformly weak
→ verify low-end floor with easier concrete tasks

anchors uniformly strong
→ jump to higher capability probe

mixed near boundary
→ select boundary-discriminating item
```

## 4. Decision gate

A placement decision is valid only when:

- required construct coverage for that route exists;
- no critical construct is being inferred from an unrelated modality;
- uncertainty is below the locally validated threshold **or** a conservative fallback exists;
- minimum sample rule is met;
- maximum burden rule has not been violated.

Otherwise:

```text
NO PRECISE DECISION
→ choose conservative learnable route
→ flag for fast recalibration
```

## Speaking/writing trigger

Do not make these universal cold-start blockers.

A productive probe becomes valuable when it can materially distinguish:

```text
learner should start in high-support foundation
```

from:

```text
learner can skip controlled production prerequisites
```

Machine scoring must pass `FEAT-ASR-001` / `FEAT-AIG-001` gates as relevant.

## 5. First lesson as evidence opportunity

The first real lesson should include independent attempts that can revise the profile.

Example:

```text
comprehensible input
→ meaning check
→ retrieval
→ changed parallel use
```

These attempts are stored in the normal Evidence Engine, not in a special onboarding silo.

## 6. Recalibration

After each early learning attempt:

```text
new validated evidence
→ update learner profile
→ compare with cold-start estimate
→ keep route / accelerate / repair prerequisites
```

The cold-start prior should decay rapidly.

## Decision correction events

Record explicit events:

```text
PLACEMENT_TOO_EASY
PLACEMENT_TOO_HARD
SUPPORT_HIGHER_THAN_EXPECTED
KNOWN_CONTENT_SKIPPED_FORWARD
PRODUCTIVE_CAPABILITY_HIGHER_THAN_EXPECTED
LISTENING_CAPABILITY_LOWER_THAN_TEXT_CAPABILITY
```

These events are training/evaluation targets for improving the bootstrap system later.

## UI behavior

The learner should experience:

```text
few easy-to-understand questions
→ difficulty adjusts
→ immediate start
```

not:

```text
“Take a 30-minute English test before you can use the app.”
```

The UI should communicate that answers are used to choose a starting point, not to judge intelligence or assign a permanent level.

## Reporting

Learner-facing result should prefer capability language:

```text
You already recognize some common written English.
Listening needs more support, so we'll start there and adjust quickly as you learn.
```

Avoid false precision such as:

```text
English ability = 18.73%
```

CEFR orientation may be shown only when enough validated evidence exists and should be labeled as an estimate.

## Guardrails

### No support leakage

If a Vietnamese translation or transcript was visible, the result cannot be treated as unsupported English comprehension.

### No missing-as-low

Unprobed capability = `unknown`.

### No one-shot mastery

Cold-start success never creates retained/mastered evidence.

### No conversion-only optimization

A shorter placement flow is a regression if it increases harmful placement errors or reduces subsequent learning gain.

### No opaque AI authority

If LLM/ASR contributes to a placement decision, its role, scope and provenance follow `FEAT-AIG-001` / `FEAT-ASR-001`.

## Validation target

This feature graduates from candidate status only if `EXP-021` shows that it can reduce onboarding burden while preserving or improving downstream learning decisions relative to a longer curated baseline.
