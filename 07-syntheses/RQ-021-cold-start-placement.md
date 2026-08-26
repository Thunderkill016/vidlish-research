# RQ-021 — Cold-start placement and learner-model bootstrap

**Synthesis ID:** `SYN-PLC-001`  
**Status:** initial synthesis complete  
**Depends on:** `RQ-001`, `RQ-003`, `RQ-005`, `RQ-006`, `RQ-008`, `RQ-012`, `RQ-015`, `RQ-017`, `RQ-019`, `RQ-020`

## Research question

How should Nếp determine a new learner's starting point quickly enough to deliver learning value immediately, while still producing defensible evidence for Vietnamese adults near A0/A1?

## Short answer

Do **not** build a miniature IELTS/CEFR exam at signup.

Build a **progressive learner-model bootstrap**:

```text
context + self-report prior
        ↓
small common anchor set
        ↓
coarse capability region
        ↓
targeted frontier probes only where uncertain
        ↓
provisional starting profile
        ↓
start real lesson
        ↓
validated evidence from first sessions
        ↓
rapid recalibration
```

The product goal is not maximum score precision. It is the lowest-cost decision that produces a useful next learning task while limiting harmful over-placement and under-placement.

## Placement target: capability region, not global level

Cold-start output should look conceptually like:

```text
listening_form_recognition: low / uncertain
written_form_meaning:       emerging / moderate confidence
chunk_comprehension:        low / moderate confidence
controlled_recall:          not yet evidenced
speaking:                   unknown
writing:                    unknown

recommended_start:
  capability = basic personal identification / everyday needs
  support = high
  primary_mode = listening + image/text support
```

not:

```text
CEFR = A1
```

A CEFR mapping may be shown later as a descriptive orientation, but the curriculum engine should consume the capability profile.

## What cold-start evidence is allowed to mean

Cold-start evidence is **routing evidence**.

It may support claims such as:

```text
likely too easy
likely learnable now
likely too difficult
uncertain — probe again
```

It must not by itself support:

```text
mastered
retained
transfers flexibly
can converse with humans
```

Those require the existing evidence rules from earlier RQs.

## Proposed bootstrap architecture

### Stage 0 — zero-cost context prior

Collect only information that can change routing:

- first language: Vietnamese;
- prior English exposure/study;
- whether the learner can read Latin alphabet comfortably;
- current goal/context;
- optional concrete self-assessment;
- audio/microphone availability.

Do not ask long biography questions.

These fields update a prior, not learner truth.

### Stage 1 — common confidence-preserving anchors

Use a small set of tasks every new learner sees. They should be:

- genuinely informative at Pre-A1/A1;
- easy enough that a true beginner has a chance to demonstrate partial knowledge;
- varied enough to avoid a single grammar/vocabulary construct dominating the estimate;
- simple to understand without knowing test mechanics.

Candidate anchor families:

```text
1. picture → familiar spoken word/chunk recognition
2. picture → familiar written word/chunk recognition
3. very short audio → meaning choice
4. simple written message → meaning choice
5. high-frequency construction interpretation
6. very small recall/reconstruction opportunity
```

Exact count is unresolved.

### Stage 2 — frontier search

After the anchors, the system asks:

```text
Which next piece of evidence can most change the learning decision?
```

Examples:

```text
written success + audio failure
→ probe listening/phonological decoding

recognition success + recall unknown
→ probe unsupported retrieval

basic comprehension strong
→ try changed but nearby context

mixed results near a route boundary
→ collect another targeted task
```

Do not waste time probing a skill that cannot alter the next lesson.

### Stage 3 — optional expensive probes

Speaking and writing should not automatically block onboarding.

Trigger them when:

- the learner self-reports meaningful productive ability;
- receptive evidence suggests they may skip substantial beginner material;
- productive capability will immediately change the curriculum route;
- uncertainty remains high at an important boundary.

Because `RQ-008` and `RQ-020` already constrain automated speaking/AI judgments, a low-confidence machine result must not silently decide placement.

### Stage 4 — provisional placement

Store a decision with uncertainty:

```text
placement_snapshot
  profile_estimates
  confidence_by_construct
  evidence_ids
  unsupported_constructs
  recommended_start_node
  support_level
  estimated_overplacement_risk
  estimated_underplacement_risk
  created_at
```

Important:

```text
unknown != weak
```

If speaking was not probed, its state is `unknown`, not `A0`.

### Stage 5 — begin learning immediately

The first real Nếp session is also part of calibration.

Use tasks whose learning value is real even if the placement estimate is imperfect.

For example:

```text
understand short message
→ retrieve target
→ changed-context use
```

Those attempts already fit the learner-evidence architecture defined in previous RQs.

### Stage 6 — rapid recalibration

Early-session evidence should outrank the cold-start prior quickly.

Conceptually:

```text
cold_start_prior weight ↓ rapidly
real independent evidence weight ↑ rapidly
```

A learner who was under-placed should skip forward quickly.

A learner who was over-placed should receive more support / easier prerequisites without being told they "failed a level."

## Why Nếp should not optimize exact CEFR at signup

Every extra category creates another boundary to classify.

Classification research shows that more simultaneous cut points generally make classification harder. Nếp only needs enough resolution to choose the next useful capability region.

So the initial problem may be closer to:

```text
STARTER
FOUNDATION
EARLY-A1
A1-PLUS / needs deeper placement
```

than to dozens of fine score bands.

The names above are illustrative, not final product labels.

## Low-end bank requirement

This is a P0 technical requirement for Nếp.

The bank must include items with information below conventional A1 course-entry tasks.

Each item should carry at minimum:

```text
item_id
construct
capability_ids
input_mode
response_mode
support_level
difficulty_estimate
calibration_n
item_information / discrimination representation
language_load
content_tags
known_dependencies
expected_time
```

Until enough data exists for robust IRT, Nếp can begin with expert-stratified difficulty + empirical pass/error data, but should not pretend those values are calibrated latent-trait parameters.

## Content balancing rule

Pure maximum-information adaptive selection is not enough.

The bootstrap must preserve a minimum blueprint across the constructs needed for the next decision.

For example, Nếp should never return:

```text
"good beginner listening"
```

if every item the learner saw was written grammar.

## Self-assessment rule

Use concrete statements such as:

```text
I can understand my name, numbers and very common words when spoken slowly.
I can read a short message such as “Meet me at 7.”
I can say a few sentences about myself without reading them.
```

not:

```text
What is your CEFR level?
```

Even concrete self-assessment remains prior information.

## Learner experience rule

Do not make adaptivity psychologically opaque.

A short explanation can say, in product language:

> Nếp will change the questions based on your answers so you don't waste time on things that are far too easy or too hard.

The system should begin with confidence-preserving tasks and avoid a run of impossible questions for true beginners.

## Stopping logic

The stopping decision should be about actionability.

Conceptually stop when:

```text
a recommended start node exists
AND
probability of a materially different route is acceptably low
AND
minimum construct coverage has been met
```

Or stop at a maximum burden:

```text
max_time / max_items reached
→ route conservatively
→ mark uncertainty
→ continue calibration during learning
```

Do not fabricate confidence to avoid an `uncertain` state.

## Placement errors are asymmetric

Over-placement and under-placement do not necessarily cost the same.

### Over-placement can cause

- incomprehensible input;
- excessive Vietnamese/support dependence;
- repeated failure;
- wrong interpretation that the learner is incapable.

### Under-placement can cause

- boredom;
- wasted time;
- obvious known-content repetition;
- loss of trust in personalization.

`EXP-021` must estimate both costs empirically.

## What the product should learn after launch

The system should track:

```text
initial route
→ first-session outcomes
→ route corrections
→ delayed gain
→ support use
→ learner friction
```

Then estimate which cold-start responses predict useful learning decisions.

Placement itself becomes a learnable product model—but only from outcome-linked evidence, not conversion alone.

## Product conclusion

Nếp should not have a one-time "placement score" architecture.

It should have:

```text
BOOTSTRAP ESTIMATE
        ↓
LEARN
        ↓
OBSERVE VALID EVIDENCE
        ↓
RECALIBRATE
        ↓
LEARN BETTER
```

This converts onboarding from an entrance exam into the first phase of the Evidence Engine.
