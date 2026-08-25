---
id: FEAT-ASR-001
title: ASR evidence gate
status: research-backed-candidate
research_question: RQ-008
---

# Feature research spec — ASR evidence gate

## Learner problem

Immediate speech feedback is valuable, but generic ASR and commercial pronunciation scores can generate false certainty. For Vietnamese-speaking learners, model error may reflect accent/L1/task bias as well as the learner's actual pronunciation.

A false correction is pedagogically expensive: the learner can spend time changing a harmless or already-intelligible feature because a model failed.

## Target capability

Use automated speech technology to accelerate practice while preventing unvalidated machine outputs from becoming mastery claims.

## Research basis

- `SYN-ASR-001`
- `CLM-ASR-001` through `CLM-ASR-015`
- `PRN-076` through `PRN-090`
- `FEAT-PRN-001`
- `FEAT-SPK-001`
- `FEAT-TRN-001`

## Non-goals

- one opaque pronunciation score;
- native-accent imitation score;
- treating successful transcription as correct pronunciation;
- treating failed recognition as proof of mispronunciation;
- letting a vendor model silently define learner mastery;
- using a read-speech calibration to grade spontaneous speech.

## Architecture

```text
Audio Attempt
   ↓
Preflight
   ├── clipping/noise/duration checks
   └── expected target / task provenance
   ↓
Machine Observers
   ├── ASR transcript
   ├── alignment/confidence
   └── optional feature-specific detector
   ↓
Validity Gate
   ├── detector version in validated scope?
   ├── population/task/audio conditions match?
   ├── signals agree?
   └── uncertainty acceptable?
   ↓
Decision
   ├── observation only
   ├── diagnostic candidate
   ├── bounded corrective feedback
   └── validated supporting evidence
   ↓
Evidence Engine
```

## Evidence object

```ts
type MachineSpeechEvidence = {
  attemptId: string;
  targetId?: string;
  taskType: string;
  expectedText?: string;
  expectedIntent?: string;

  provider: string;
  model: string;
  modelVersion: string;
  configVersion: string;
  scoringRuleVersion: string;

  transcript?: string;
  confidence?: number;
  alignment?: Array<{
    expected?: string;
    observed?: string;
    operation?: "match" | "substitution" | "deletion" | "insertion";
  }>;

  detectorId?: string;
  featureTarget?: string;
  rawDetectorOutput?: unknown;

  audioQuality: {
    clipping?: boolean;
    signalQuality?: number;
    noiseClass?: string;
  };

  scope: {
    populationMatch: boolean;
    taskMatch: boolean;
    audioConditionMatch: boolean;
    featureMatch: boolean;
  };

  evidenceClass:
    | "machine_observation"
    | "machine_candidate"
    | "validated_machine_evidence";

  uncertaintyReason?: string;
  occurredAt: string;
};
```

## Hard product rules

1. No raw ASR output may directly set pronunciation mastery.
2. No global vendor pronunciation percentage may directly set pronunciation mastery.
3. Every machine observation stores provider/model/config/scoring-rule versions.
4. A detector can only issue feature-specific correction inside its validated feature/population/task scope.
5. ASR recognition success does not imply feature accuracy.
6. ASR non-recognition does not imply learner error until audio/task/model failure alternatives are checked.
7. Read-aloud validation does not authorize spontaneous-speech scoring.
8. Vietnamese population bias must be measured during calibration; do not hide subgroup error inside an aggregate metric.
9. Machine-human disagreement returns uncertainty, not a punitive learner score.
10. First-seen transfer and delayed human-relevant outcomes remain independent evidence even when machine feedback is used during practice.

## Candidate decision logic

```text
if audio_preflight_failed:
    request_new_sample

elif detector_not_validated_for_scope:
    log_machine_observation
    optionally_show_nonjudgmental_transcript

elif strong_feature_detector_signal and repeatable:
    create_machine_candidate
    give_bounded_feedback
    request_new_attempt

elif validated_detector and calibrated_confidence:
    add_validated_supporting_evidence

else:
    return_uncertain
```

Thresholds are deliberately absent until `EXP-008` calibrates them.

## Feedback design

Bad:

```text
Pronunciation: 63/100
Try harder.
```

Better:

```text
I may not be hearing the final sound clearly.
Try "likes" once more in the new sentence.
```

Only show that message when the relevant detector is validated enough to justify it. Otherwise show a neutral retry or omit correction.

## Relationship to learner evidence

```text
machine_observation
≠ mastery evidence

machine_candidate
≠ mastery evidence

validated_machine_evidence
= supporting evidence inside validated scope

first-seen listener/message success
= stronger intelligibility evidence
```

## Falsification

Reject or narrow this feature if:

- false corrective feedback remains common after calibration;
- subgroup error for Vietnamese varieties is materially unequal and cannot be mitigated;
- machine-derived feedback does not improve delayed first-seen listener outcomes;
- a simpler record/listen/compare flow performs as well or better;
- provider/model drift makes validation maintenance impractical.

## Required experiment

`EXP-008`.
