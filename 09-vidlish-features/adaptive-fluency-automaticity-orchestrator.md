---
id: FEAT-FLU-001
title: Adaptive fluency and automaticity orchestrator
status: research-backed-candidate
research_question: RQ-016
synthesis: SYN-FLU-001
experiment: EXP-016
---

# FEAT-FLU-001 — Adaptive fluency and automaticity orchestrator

## Learner problem

Learners can know useful English yet retrieve/process it so slowly that real-time use collapses. The opposite problem also exists: repeated practice can make one sentence/task fast without making the underlying English flexibly available.

Nếp needs to reduce processing friction while refusing the false shortcut:

```text
fast practiced performance = fluent mastery
```

## Target capability

For a learned communicative capability, the learner can understand/retrieve/use relevant language efficiently enough for the target modality while preserving meaning and acceptable accuracy, and can do so across changed tasks after delay without strong support.

## Research basis

Primary principles:
- `PRN-197`–`PRN-212`
- `SYN-FLU-001`

Evidence themes:
- fluency is multidimensional (`SRC-0169`, `SRC-0170`, `SRC-0177`);
- L1/personal speaking style affects L2 temporal fluency (`SRC-0171`);
- practice can proceduralize/automatize language but is skill-specific (`SRC-0172`, `SRC-0173`, `SRC-0178`);
- repetition schedule and variability alter gains/transfer (`SRC-0058`, `SRC-0174`, `SRC-0175`, `SRC-0176`);
- chunks/collocations can support efficient retrieval but must generalize beyond memorized strings (`SRC-0179`, `SRC-0180`, `SRC-0061`);
- reading fluency must retain comprehension and unseen-text evidence (RQ-013).

## Non-goals

This feature is not:
- a speed game;
- an always-on timer;
- a WPM leaderboard;
- a “no pauses” trainer;
- endless repetition;
- a script memorizer;
- proof that fast recognition equals fast production;
- proof that fast monologue equals fast interaction.

## Readiness gate

Before a target enters deliberate fluency practice, require sufficient evidence of meaningful knowledge.

Candidate gate inputs:

```text
understood
recalled
basic transfer
accuracy / intelligibility floor
support dependence
```

Possible state:

```ts
type FluencyReadiness = {
  targetId: string;
  modality: string;
  meaningReady: boolean;
  retrievalReady: boolean;
  transferReadyEnough: boolean;
  errorRisk: number;
};
```

If `errorRisk` is high or meaning is unstable, route to learning/retrieval rather than time pressure.

Exact thresholds belong to `EXP-016`.

## Core practice loop

```text
FIRST meaningful performance
        ↓
record quality + friction
        ↓
SHORT same-task/content repetition
        ↓
reduce support where safe
        ↓
CHANGED CONTENT, same useful procedure/function
        ↓
CHANGED surface/context/partner
        ↓
SPACE next exposure
        ↓
DELAYED changed-task probe
```

## Repetition provenance

Every attempt must know what is being repeated:

```ts
type RepetitionProvenance = {
  exactItemRepeat: boolean;
  sameContentRepeat: boolean;
  sameTaskProcedure: boolean;
  sameCommunicativeFunction: boolean;
  samePartnerOrVoice: boolean;
  priorExposureCount: number;
};
```

This prevents the Evidence Engine from treating repetition #5 on identical content as equivalent to first-pass transfer.

## Fluency evidence

```ts
type FluencyAttemptEvidence = {
  attemptId: string;
  targetIds: string[];
  modality: "listening" | "speaking" | "reading" | "writing" | "interaction";
  taskFamilyId: string;

  meaningSuccess?: number;
  taskSuccess?: number;
  accuracy?: number;
  intelligibility?: number;

  speedMeasure?: number;
  breakdownMeasure?: number;
  repairMeasure?: number;
  processingLatencyMs?: number;

  replayCount?: number;
  hintCount?: number;
  lookupCount?: number;
  partnerRescueCount?: number;

  repetitionIndex: number;
  noveltyLevel: number;
  delayed: boolean;
};
```

No single field sets fluency mastery.

## Guardrails

A temporal gain can count positively only when required quality remains above stage-appropriate bounds.

Conceptually:

```ts
if (speedImproved && meaningCollapsed) {
  doNotPromoteFluency();
}
```

Likewise:

```ts
if (pauseRateImproved && accuracyCollapsed) {
  doNotPromoteFluency();
}
```

Guardrail dimensions by modality:
- listening: comprehension / next-action success;
- speaking: meaning + intelligibility + target accuracy;
- reading: comprehension;
- writing: message fulfillment + target accuracy;
- interaction: response contingency + shared-goal progress + intelligibility.

## Speaking fluency

Track dimensions separately where speech sample length is sufficient:

```text
speed
breakdown
repair
```

Candidate measures:
- articulation rate;
- speech rate;
- mid-clause pause frequency/duration;
- clause-boundary pause behavior;
- mean length of run;
- repetitions/reformulations.

### Short-response caveat

Near-A0 responses may be too short for stable temporal metrics. When measurement reliability is weak, prefer simpler evidence:
- successful retrieval latency;
- number of disruptive attempts;
- support use;
- human/validated intelligibility;
- changed-task success.

Do not manufacture precision from a two-word answer.

## Personal/L1 style normalization

If enough data exists, compare the learner primarily against:
- their own earlier performance on matched task families;
- their own typical pause/speech style;
- validated stage/task ranges.

Never punish a naturally slower speaker merely for not matching a universal native-speaker rate.

L1 calibration may be researched but should not be required for ordinary onboarding.

## Same-task repetition policy

Candidate:

```text
repeat only while:
- performance remains meaningful;
- friction is still falling;
- transfer has not yet been demonstrated;
- repetition has not become verbatim script playback;
```

Stop when:
- plateau;
- quality declines;
- changed-content probe succeeds;
- memorization signature becomes too strong;
- expected benefit per minute becomes low.

## Variation policy

After initial stabilization, vary one or more dimensions:
- lexical slot;
- actor/object/time/place;
- prompt wording;
- voice/accent;
- interlocutor;
- scenario;
- input realization;
- text passage.

Variation should remain within prerequisite readiness; “novel” must not secretly mean “contains lots of unknown English.”

## Blocked vs interleaved scheduling

The literature does not justify one universal winner.

Candidate orchestrator behavior:
- early stabilization may use short blocked bursts;
- subsequent practice introduces task/content variation;
- delayed sessions sample multiple targets/functions;
- the experiment decides when interleaving helps/hurts near-A0 users.

Log schedule so outcomes can be analyzed.

## Spacing

Reuse `FEAT-REV-001` infrastructure but treat fluency scheduling as its own evidence problem.

Possible event:

```ts
type FluencyReviewRequest = {
  capabilityId: string;
  modality: string;
  desiredNovelty: number;
  earliestAt: string;
  rationale: "transfer" | "retention" | "automaticity";
};
```

Do not schedule only the exact old task. Prefer changed-content probes after stabilization.

## Time-pressure policy

Time pressure is optional and gated.

Allowed only if:
- learner can already complete task meaningfully;
- time window is not below a validated reasonable bound;
- quality is monitored;
- learner can fall back to self-paced practice after collapse.

Candidate 4/3/2-like use should be modified for short beginner tasks rather than copied literally.

Never present “beat your previous speed” as the sole goal.

## Formulaic chunk fluency

Candidate chunk loop:

```text
hear/understand chunk
→ retrieve chunk
→ retrieve under modest time demand
→ substitute slot
→ changed sentence
→ changed scenario
→ interaction use
→ delayed spontaneous retrieval
```

Store:

```text
chunkId
slotVariationCount
contextVariationCount
scriptSimilarity
```

A chunk with high verbatim script similarity and low variation remains context-bound.

## Listening fluency

Candidate progression:

```text
understand short normal-speed input
→ fewer replays
→ less segmentation support
→ longer connected input
→ changed voice/wording
→ relevant next action/turn
```

Useful evidence:
- first-pass comprehension;
- replay/support reduction;
- segmentation dependence;
- changed-voice transfer;
- interactional next-turn response.

Do not use answer reaction time alone.

## Reading fluency

Integrate `FEAT-READ-001`:

```text
first-pass text-only comprehension
→ repeated/assisted repair where useful
→ changed/unseen text
→ delayed unseen text
```

Temporal improvement without comprehension does not count.

## Writing fluency

Integrate `FEAT-WRI-001`.

Track process timing carefully but control for device/input method.

Candidate focus:
- known target retrieval becomes less disruptive;
- fewer lookups/hints for basic forms;
- message is completed more efficiently;
- delayed changed-task quality is maintained.

Do not expose typing speed as English mastery.

## Interaction fluency

Integrate `FEAT-INT-001`.

Candidate interaction efficiency:

```text
relevant response
+ manageable latency
+ less partner rescue
+ successful repair
+ shared goal maintained
```

A learner may appropriately pause or ask clarification. The engine must not optimize away competent repair behavior.

## Learner fluency state

```ts
type FluencyCapabilityState = {
  capabilityId: string;
  modality: string;

  meaningfulAvailability: EvidenceSummary;
  repeatedEfficiency: EvidenceSummary;
  changedTaskEfficiency: EvidenceSummary;
  delayedEfficiency: EvidenceSummary;

  qualityGuardrails: EvidenceSummary;
  supportDependence: EvidenceSummary;
};
```

Candidate internal progression:

```text
F0 supported availability
F1 meaningful but effortful
F2 efficient on familiar repetition
F3 efficient on changed content
F4 delayed varied efficiency
F5 less-controlled transfer
```

Do not display this as a fake universal level until it proves useful to learners.

## Progress UI

Prefer capabilities:

```text
Can respond to simple café choices without needing a model
✓ across changed items

Can use "I'd like..." quickly in familiar requests
✓ changed content
△ delayed interaction evidence still limited

Can read a short known-level message smoothly while understanding it
✓ unseen text
```

Avoid:

```text
Fluency 86/100
```

## Learning metrics

Primary:

```text
delayed changed-task efficiency gain with quality preserved
────────────────────────────────────────────────────────
practice minutes
```

Report at least:
- meaning/task success;
- accuracy/intelligibility/comprehension guardrail;
- temporal/friction metric;
- novelty level;
- support dependence.

Secondary:
- within-training improvement;
- same-task performance;
- learner effort;
- voluntary retries.

Do not optimize secondary metrics at the expense of primary transfer.

## Falsification

Redesign or weaken `FEAT-FLU-001` if:
- speed improves only on exact practiced items;
- time pressure degrades meaning/accuracy without later benefit;
- repetition increases script dependence;
- novel/delayed tasks show no efficiency gain;
- personal/L1 style explains more variation than purported learning for chosen metric;
- fluency training consumes significant time without better real interaction/listening/reading use;
- a simpler retrieval/review policy produces equal delayed transfer.

## Experiment

See `EXP-016`.
