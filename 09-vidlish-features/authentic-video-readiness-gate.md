---
id: FEAT-VID-002
title: Authentic video readiness gate
status: research-backed-candidate
research_question: RQ-009
---

# Feature research spec — Authentic video readiness gate

## Learner problem

“Authentic video” is often treated as a content category: either beginners are blocked from it for a long time, or they are exposed to material far beyond their listening ability and survive by reading subtitles.

Both approaches waste useful authentic input.

## Target capability

Select short authentic audiovisual windows that are learnable for the current learner, state exactly what support they require, and distinguish content comprehension from independent listening evidence.

## Research basis

- `SYN-VID-002`
- `CLM-VID-002` through `CLM-VID-015`
- `PRN-091` through `PRN-104`
- `FEAT-VOC-001`
- `FEAT-LIS-001`
- `FEAT-SCF-001`
- `FEAT-TRN-001`
- `FEAT-VID-001`

## Non-goals

- unlock every video after a fixed vocabulary count;
- use CEFR label alone to choose clips;
- assume 80%, 90%, 95% or 98% coverage is a universal threshold;
- call subtitle-supported comprehension independent listening;
- score a full video with one average difficulty number;
- slow every authentic clip mechanically;
- make authentic video mandatory for the earliest sessions.

## Architecture

```text
Source video
   ↓
Window segmenter
   ↓
Clip analyzer
   ├── transcript + lexical profile
   ├── speech rate / turn density
   ├── speaker + acoustic metadata
   ├── visual-semantic grounding
   └── topic/context tags
   ↓
Learner matcher
   ├── aural known-item evidence
   ├── listening diagnostic evidence
   ├── topic familiarity proxy
   └── support history
   ↓
Readiness gate
   ├── V0 not ready
   ├── V1 scaffolded exposure
   ├── V2 audio-led learning
   └── V3 independent authentic window
   ↓
Support policy (RQ-010)
   ↓
Attempt + evidence
   ↓
Recalibrate learner × clip model
```

## Clip window object

```ts
type AuthenticVideoWindow = {
  id: string;
  sourceId: string;
  startMs: number;
  endMs: number;

  transcript: string;
  tokenCount: number;
  lexicalProfileVersion: string;

  speech: {
    wordsPerMinute?: number;
    speakerCount: number;
    turnCount: number;
    overlapRisk: "low" | "medium" | "high" | "unknown";
    noiseRisk: "low" | "medium" | "high" | "unknown";
    connectedSpeechRisk: "low" | "medium" | "high" | "unknown";
    accents?: string[];
  };

  visual: {
    groundingScore?: number;
    complexity: "low" | "medium" | "high" | "unknown";
    languageVisible?: boolean;
  };

  topics: string[];
  provenance: {
    url: string;
    title?: string;
    creator?: string;
    retrievedAt: string;
  };
};
```

## Learner × window readiness object

```ts
type VideoReadiness = {
  learnerId: string;
  windowId: string;

  estimatedAuralCoverage?: number;
  coverageBasis: "attempt-evidence" | "inferred" | "unknown";

  knownAudioTargets: number;
  uncertainAudioTargets: number;
  unknownCriticalTargets: number;

  speechLoad: "low" | "medium" | "high" | "unknown";
  visualSupport: "weak" | "moderate" | "strong" | "unknown";
  topicSupport: "unknown" | "unfamiliar" | "familiar";

  readiness: "V0" | "V1" | "V2" | "V3";
  requiredSupport: string[];
  reasons: string[];

  ruleVersion: string;
  computedAt: string;
};
```

## Lexical matching

Do not calculate readiness from a generic vocabulary checklist alone.

Prefer this order of evidence:

```text
aural independent recall / recognition evidence
        ↓
recent listening success with target
        ↓
text-only vocabulary evidence
        ↓
frequency-based inference
```

Text-only knowledge may contribute but should receive less confidence because RQ-003 established that knowing a written word does not guarantee recognizing it in speech.

## Critical unknowns

Raw percentage coverage can hide important structure.

Example:

```text
95% known tokens
but the unknown 5% contains:
"refund", "receipt", "exchange"
```

If those words carry the entire message, the clip may be unusable despite high token coverage.

Therefore store:

```text
unknown token count
unknown unique items
unknown critical content items
unknown function/support items
```

A clip with one critical unknown may need more support than a clip with several noncritical unknowns.

## Speech-load ranker

Initial ranker should treat these as independent features rather than collapsing them immediately into one opaque score:

```text
speech rate
speaker count
turn density
overlap
noise/music
connected-speech density
utterance length
accent familiarity
```

Exact weights remain `EXP-009` hypotheses.

## Visual-grounding ranker

Candidate rubric:

```text
strong
spoken referents/actions visibly coincide with the language

moderate
visual scene constrains meaning but does not show all critical content

weak
talking head / abstract B-roll / visuals do not resolve spoken meaning
```

Visual grounding can make V1/V2 possible earlier, but it cannot silently raise audio mastery.

## Evidence separation after viewing

```ts
type VideoAttemptEvidence = {
  understoodWithVideo?: boolean;
  understoodAudioBasedProbe?: boolean;
  captionSupportLevel: string;
  vietnameseSupportLevel: string;
  replayCount: number;
  playbackRate: number;
  firstAttemptWithoutAnswerText: boolean;
};
```

If the learner answers a visually solvable question, update `understood_with_video` but not independent listening evidence.

## Candidate interaction

```text
V2 window selected
↓
video first attempt, no answer-bearing caption
↓
gist / audio-based probe
↓
if failure:
  diagnostic listening branch
  + smallest support allowed by RQ-010
↓
replay
↓
changed first-seen window later
```

## Hard product rules

1. No global vocabulary-count unlock for authentic video.
2. Score windows, not whole sources, for learner readiness.
3. Estimate lexical coverage from aural evidence where possible.
4. Keep viewing comprehension and audio comprehension separate.
5. Captions/subtitles are support states, not proof that the window was independently ready.
6. Visual grounding can reduce pedagogical difficulty but cannot erase audio-evidence requirements.
7. Speech-rate thresholds must be calibrated by learner proficiency/task; do not hard-code a universal WPM boundary.
8. Do not use one aggregate difficulty score without preserving the contributing features.
9. High token coverage does not override critical unknown content words.
10. Readiness must be recomputed as the learner model changes.
11. Preserve source/window provenance and analysis-rule versions.
12. Treat V0/V1/V2/V3 boundaries as product hypotheses until `EXP-009` validates them.

## Relationship to Smart Captions

```text
FEAT-VID-002
selects whether/how the clip is usable
       ↓
FEAT-VID-001
controls textual support during that clip
```

RQ-010 will strengthen `FEAT-VID-001`; RQ-009 prevents captions from being used to rescue arbitrarily difficult clips.
