---
id: SYN-PAU-001
title: Auto-pause as repair, not default listening mode
status: initial-synthesis
research_question: RQ-011
last_verified: 2026-08-25
---

# RQ-011 — Does auto-pause improve learning or fragment comprehension?

## Decision summary

Nếp should **not auto-pause authentic listening by default**.

The evidence supports pausing, replay and temporal control as useful scaffolds, but it does not support turning natural speech into permanently chopped input. Pause placement changes processing conditions, learner-controlled playback has documented value, and automatic difficult-segment repetition has promising local decoding results. The safest product policy is therefore:

```text
continuous first pass
        ↓
record natural-flow evidence
        ↓
if failure: diagnose local vs global breakdown
        ↓
repair layer
  ├── learner replay/pause
  ├── exact-window replay
  └── optional system micro-pause at safe boundary
        ↓
retry
        ↓
return to continuous playback
        ↓
delayed unseen continuous probe
```

Auto-pause is a **repair mechanism**, not the listening curriculum.

## What the literature supports

### Learner-controlled playback is useful, but not automatically well used

A 2024 systematic review found that playback controls help L2 listeners deploy strategies, repair comprehension problems and improve listening performance, while also noting proficiency-related limits and the need to train learners to use controls purposefully (`SRC-0111`).

This argues for visible pause/replay controls and usage provenance. It does not prove that the system should interrupt everyone at the same points.

### Targeted automatic repetition is promising for local decoding

Mirzaei and Meshgi's partial/synchronized-caption work automatically detected difficult speech regions and used repetition/slowdown; intermediate learners improved local recognition and reported the features as useful (`SRC-0112`).

But the measured gain is narrower than Nếp's target:

```text
better recognition on assisted target segment
≠
better delayed continuous listening on unseen speech
```

So the mechanism is promising for repair, not sufficient for mastery.

### Pause location changes the signal

Artificial pause insertion changes prosodic and parsing cues. Fang et al. found different effects for A2 and C1 learners depending on whether pauses occurred between or within phrase boundaries (`SRC-0113`). Classic L2 work also found that pausing can influence comprehension (`SRC-0117`).

Therefore a system pause is not neutral UI chrome. It modifies the linguistic input.

### General multimedia evidence is supportive but not decisive

In non-language multimedia presentations, complexity-determined system pausing and learner pausing both outperformed continuous presentation under some conditions, with no clear superiority of system over learner pausing (`SRC-0114`).

This supports processing-time plausibility, but Nếp must not convert a general multimedia result into a language-mastery rule.

### Pausing is especially valuable as diagnosis

Paused transcription can expose exactly what a learner decoded or mis-segmented from connected speech (`SRC-0115`). That makes pauses useful for diagnostic microtasks after a breakdown.

This fits `FEAT-LIS-001`:

```text
continuous message attempt
→ failure
→ paused/short transcription probe
→ identify segmentation/form bottleneck
→ targeted repair
```

not:

```text
every sentence
→ automatic stop
→ question
→ automatic stop
→ question
```

## Continuous and segmented listening are different evidence states

Nếp should store at minimum:

```text
continuous_first_seen_success
continuous_repeated_success
learner_paused_success
system_paused_success
segmented_repair_success
```

A learner who succeeds only after the audio has been segmented has learned something useful, but the system must not infer natural-flow mastery.

## Pause provenance

```ts
type PauseEvent = {
  attemptId: string;
  clipWindowId: string;
  mode: "learner" | "system";
  reason:
    | "learner_request"
    | "diagnostic_failure"
    | "predicted_difficulty"
    | "complexity"
    | "experiment";
  boundaryType: "clause" | "phrase" | "prosodic" | "word" | "unknown";
  durationMs: number;
  positionMs: number;
  exposureIndex: number;
  replayCount: number;
  detectorModel?: string;
  detectorVersion?: string;
  triggerConfidence?: number;
}
```

## Default candidate policy

### First pass

```text
continuous
normal temporal flow
no system pause
```

provided `FEAT-VID-002` says the clip is ready enough.

### Repair pass

If a local listening failure is detected:

```text
1. offer/replay exact short window
2. let learner pause/replay manually
3. if system support is warranted, pause at a safe boundary
4. combine with FEAT-VID-001 / FEAT-LIS-001 support only as needed
```

### Return to natural flow

After repair:

```text
remove forced pause
→ replay continuously
→ later unseen continuous clip
```

## Why not pause every unknown word?

Unknown-word prediction is itself uncertain. A word may be unknown orthographically but recognizable in context; another known word may fail acoustically. Interrupting at every predicted unknown can:

- fragment gist construction;
- distort natural prosody and segmentation cues;
- increase session time;
- train waiting for boundaries supplied by the app;
- create unnecessary interruptions when the learner could infer meaning.

Current evidence does not justify this default (`CLM-PAU-010`).

## Relationship to other features

```text
FEAT-VID-002
Is this clip/window ready?
        ↓
FEAT-VID-003
Should temporal flow remain continuous or enter repair mode?
        ↓
FEAT-LIS-001
What failed: perception/segmentation or meaning?
        ↓
FEAT-VID-001
Which textual/L1 support is justified?
        ↓
Evidence Engine
What does this attempt actually prove?
```

If machine difficulty detection triggers a pause, `FEAT-ASR-001`-style validity rules apply to the detector.

## What RQ-011 does not establish

It does not establish:

- one universal pause duration;
- one universal pause frequency;
- that clause boundaries are always optimal for near-A0 learners;
- that learner control is always superior to system control;
- that system control is always superior for beginners;
- a confidence threshold for predicted-difficulty auto-pause;
- the exact point at which temporal support should fade.

Those remain direct Nếp experiments.

## Product decision

Create `FEAT-VID-003` — **Adaptive temporal repair controller**.

Default state is continuous playback. System pausing is an evidence-aware repair intervention and must prove itself by improving later unseen continuous listening relative to simpler learner-controlled replay.
