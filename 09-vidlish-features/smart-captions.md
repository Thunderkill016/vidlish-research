---
id: FEAT-VID-001
title: Smart captions for graduated video input
status: later-stage-experiment
---

# Feature research spec — Smart captions

## Scope

This is **not** a first-session A0 feature. It applies when a learner has graduated to short authentic or semi-authentic video input that passes a difficulty gate.

## Learner problem

Audio may be partly understandable while individual words/phrases remain hard to segment or recognize. Permanent bilingual subtitles can solve comprehension by replacing listening with reading.

## Target capability

Understand a bounded video message with progressively less textual/L1 support.

## Research links

- `SYN-VID-001` captions.
- `SYN-LIS-001` listening model.
- `PRN-006` scaffold/fade support.

## Candidate interaction

```text
attempt 1: video/audio + visual context
→ ask gist / target meaning
→ reveal English caption on request or after failure
→ tap phrase for bounded Vietnamese support
→ replay exact window
→ later replay with less support
→ changed clip/window probe when feasible
```

## Do not assume

- bilingual subtitles are always harmful;
- English-only captions are always superior;
- auto-pause is beneficial;
- tapping every unknown word should create a flashcard;
- watching to completion is a learning outcome.

## Experiments

Compare support policies on matched clips:

- A: English captions always on;
- B: bilingual captions always on;
- C: progressive English → Vietnamese-on-demand;
- D: audio-first then caption after attempt.

Measure comprehension, delayed target-word retention, listening performance on an unseen parallel clip, completion and subjective effort separately.
