---
id: FEAT-VID-003
title: Adaptive temporal repair controller
status: research-backed-candidate
research_question: RQ-011
---

# Feature research spec — Adaptive temporal repair controller

## Learner problem

Authentic speech is transient. Near-beginner learners can lose a word boundary or short phrase and then lose the rest of the message. Automatic pausing may create processing time, but excessive or poorly placed pauses can change prosody, fragment gist and train dependence on segmented input.

## Target capability

Use replay/pause selectively to repair breakdowns while preserving and eventually improving comprehension of continuous natural-flow speech.

## Research basis

- `SYN-PAU-001`
- `CLM-PAU-001` through `CLM-PAU-013`
- `PRN-120` through `PRN-132`
- `FEAT-LIS-001`
- `FEAT-VID-001`
- `FEAT-VID-002`
- `FEAT-ASR-001`

## Non-goals

- pause every sentence;
- pause every unknown word;
- convert authentic speech into permanent phrase-by-phrase audio;
- count segmented success as continuous-listening mastery;
- trust an AI difficulty detector without calibration;
- mechanically slow all speech.

## State machine

```text
CONTINUOUS_FIRST_PASS
        ↓
   success? ── yes → CONTINUE
        │
       no
        ↓
DIAGNOSE_BREAKDOWN
        ↓
REPAIR_WINDOW
  ├── exact replay
  ├── learner pause/replay
  ├── diagnostic paused probe
  └── bounded system micro-pause
        ↓
RETRY_CONTINUOUS
        ↓
DELAYED_UNSEEN_CONTINUOUS_PROBE
```

## Pause event

```ts
type PauseEvent = {
  attemptId: string;
  clipWindowId: string;
  mode: "learner" | "system";
  reason: "learner_request" | "diagnostic_failure" | "predicted_difficulty" | "complexity" | "experiment";
  boundaryType: "clause" | "phrase" | "prosodic" | "word" | "unknown";
  positionMs: number;
  durationMs: number;
  exposureIndex: number;
  replayCount: number;
  detectorModel?: string;
  detectorVersion?: string;
  triggerConfidence?: number;
};
```

## Evidence interpretation

```text
first-seen continuous correct
→ strongest candidate natural-flow evidence

continuous replay correct
→ repeated-exposure continuous evidence

learner-paused correct
→ learner-controlled temporal-support evidence

system-paused correct
→ system-supported temporal evidence

paused transcription correct
→ local decoding/segmentation evidence
```

Do not collapse these into one `listening_correct` boolean.

## Safe-boundary candidate

When system pausing is used, prefer linguistically plausible boundaries:

```text
clause/prosodic boundary
→ phrase boundary
→ other validated boundary
```

Avoid arbitrary within-chunk pauses unless the instructional objective explicitly requires them and the event is labeled as modified input.

This ordering is a product candidate, not a universal scientific hierarchy.

## Trigger policy

A system pause can be considered only when:

1. a continuous attempt has already produced evidence, or the task is explicitly a diagnostic/repair exercise;
2. a bounded breakdown is likely;
3. the trigger source is known;
4. the pause point is safe enough for the intended task;
5. the event is stored with provenance.

If a model predicts difficulty, run the trigger through a validity gate. False triggers are product errors.

## UX

Keep manual controls obvious:

```text
Replay last phrase
Pause / continue
Hear again
```

Do not make the learner hunt through menus for basic listening repair.

If system repair is triggered, communicate it lightly rather than pretending the source audio naturally contains that pause.

## Falsification

This feature is weakened if:

- adaptive repair does not improve delayed unseen continuous listening over learner-controlled replay;
- interruptions materially increase abandonment/time without learning gain;
- system-trigger false positives are high;
- learners become less successful when pauses are removed;
- boundary detection is unreliable for the target source types.

## Experiment

See `EXP-011`.
