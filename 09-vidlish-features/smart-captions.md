---
id: FEAT-VID-001
title: Adaptive on-screen support controller
status: research-backed-candidate
research_question: RQ-010
---

# Feature research spec — Adaptive on-screen support controller

## Scope

This is not a first-session A0 feature. It runs only after a video window passes `FEAT-VID-002` or is deliberately used as scaffolded exposure.

## Learner problem

Permanent subtitles can make difficult audiovisual content understandable while hiding whether the learner is actually processing speech. Conversely, removing all text too early can turn useful input into noise and frustration.

## Target capability

Help the learner recover meaning and speech form with the smallest useful scaffold, while preserving clean evidence about what was possible before support appeared.

## Research basis

- `SYN-CAP-001`
- `SYN-VID-002`
- `SYN-SCF-001`
- `SYN-LIS-002`
- `PRN-105` through `PRN-119`

## Architecture

```text
Video Window
   ↓
Initial Support State
   ↓
Attempt
   ↓
Evidence Capture
   ↓
Failure Classifier
   ├── exposure/attention problem
   ├── segmentation/form problem
   ├── meaning problem
   └── global overload/not-ready
   ↓
Support Selector
   ├── replay
   ├── L2 targeted cue
   ├── L2 full caption
   ├── Vietnamese micro-gloss
   ├── transcript
   └── full Vietnamese meaning support
   ↓
Retry / analysis
   ↓
Support-reduced attempt
   ↓
Delayed unseen probe
```

## Support object

```ts
type VideoSupportEvent = {
  attemptId: string;
  clipWindowId: string;
  action:
    | "replay"
    | "show_l2_keyword"
    | "show_l2_caption"
    | "show_vi_micro_gloss"
    | "show_l2_transcript"
    | "show_vi_full_meaning";
  reason:
    | "learner_request"
    | "segmentation_failure"
    | "meaning_failure"
    | "global_comprehension_failure"
    | "experiment_policy";
  exposureIndex: number;
  revealsForm: "none" | "partial" | "full";
  revealsMeaning: "none" | "partial" | "full";
  answerBearing: boolean;
  occurredAt: string;
};
```

## Candidate interaction

```text
1. play short window without answer-bearing text
2. ask a bounded gist/meaning probe
3. if correct → continue / optional consolidation replay
4. if wrong → small diagnostic
5. choose support matching the failure
6. replay the exact window
7. hide support again when feasible
8. later use an unseen parallel window
```

## Evidence rules

### Rule 1 — support never rewrites history

If attempt 1 failed before support and attempt 2 succeeds after a full caption:

```text
attempt 1 = independent failure
attempt 2 = caption-supported success
```

Do not overwrite attempt 1.

### Rule 2 — replay is exposure, not answer reveal

Replay may remain eligible as unsupported listening evidence, but `exposureIndex > 1` must be recorded. It is not first-seen evidence.

### Rule 3 — full L1 meaning is explicit support

Success with Vietnamese subtitle/full translation can support content learning, but cannot be counted as independent L2 meaning comprehension.

### Rule 4 — caption visibility is target-sensitive

A visible L2 caption invalidates an independent **form/segmentation** claim for that same segment, but it may still allow other learning observations to be stored.

## Do not build

- one global subtitle toggle as the complete pedagogy;
- automatic permanent bilingual subtitles for every learner;
- a fixed `audio → EN → VI` ladder applied to every error;
- `caption_used = true` without finer provenance;
- mastery updates based on caption-visible answers;
- a CEFR-only rule for permanently switching captions off;
- keyword captions as the default based on the assumption that less text is always better.

## Dependencies

- `FEAT-VID-002` decides whether the window is suitable.
- `FEAT-LIS-001` helps diagnose perception versus meaning problems.
- `FEAT-SCF-001` governs Vietnamese semantic support.
- `FEAT-TRN-001` supplies unseen/support-reduced transfer probes.

## Falsification

This feature is weakened if adaptive support does not improve delayed unsupported listening relative to simpler always-on or always-off policies, or if its extra interaction cost produces no meaningful gain.

## Experiment

See `EXP-010`.
