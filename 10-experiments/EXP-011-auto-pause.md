---
id: EXP-011
title: Auto-pause versus learner-controlled temporal repair
status: proposed
research_question: RQ-011
---

# EXP-011 — Auto-pause or repair only?

## Primary question

Which temporal-support policy gives the best delayed comprehension of **unseen continuous speech** per minute of learning?

## Population

Vietnamese-speaking Nếp learners who have reached the first authentic/semi-authentic video stage admitted by `FEAT-VID-002`.

Stratify by:

- listening evidence;
- aural vocabulary access;
- prior pause/replay reliance;
- source-window difficulty.

## Conditions

### A — continuous + learner controls

```text
continuous playback
learner may pause/replay
no system interruption
```

### B — fixed boundary auto-pause

```text
automatic pause at preselected clause/phrase boundaries
```

### C — predicted-difficulty auto-pause

```text
system predicts hard segment
→ bounded pause/replay
```

### D — continuous first + failure-contingent repair

```text
continuous first pass
→ only after measured failure, enter short repair mode
→ return to continuous playback
```

## Training materials

Use matched short windows with:

- similar lexical readiness;
- similar speaker count;
- controlled visual grounding;
- annotated clause/phrase/prosodic boundaries;
- known target difficulty regions.

Do not evaluate only the exact windows used for training.

## Primary outcome

After delay, use first-seen parallel windows with:

```text
continuous natural flow
normal playback rate
no forced pauses
no captions/transcript
```

Measure:

- gist comprehension;
- critical-detail comprehension;
- aural word/chunk recognition;
- natural-flow transfer.

Primary efficiency metric:

```text
delayed unseen continuous-listening gain
──────────────────────────────────────
listening-learning minutes
```

## Secondary outcomes

- immediate comprehension;
- local segmentation accuracy;
- replay/pause count;
- interruptions per minute;
- total added time;
- subjective effort;
- abandonment;
- support dependence;
- later voluntary pause usage.

## Trigger-quality metrics

For condition C/D system-triggered events:

```text
true useful pause
false pause      # interrupted learner who did not need it
missed pause     # repair would have helped but trigger did not fire
boundary safety
```

If an AI/ASR-derived detector is used, analyze by model/version and learner subgroup.

## Hypotheses

1. Fixed auto-pause may improve immediate comprehension while increasing interruption cost.
2. Learner control may work well for learners who already self-regulate playback effectively.
3. Failure-contingent repair may preserve natural-flow evidence while still rescuing local breakdowns.
4. Predicted-difficulty auto-pause only deserves deployment if its trigger precision is high enough to beat simpler repair policies.

These are hypotheses, not expected facts.

## Decision rule

Do **not** ship global default auto-pause merely because it raises same-session comprehension.

Adopt a system-triggered policy only if it improves delayed unseen continuous listening or provides equal learning with materially lower effort/time, without creating unacceptable pause dependence or false interruptions.
