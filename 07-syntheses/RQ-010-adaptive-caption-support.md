---
id: SYN-CAP-001
title: Adaptive on-screen support policy for authentic video
status: initial-synthesis
research_question: RQ-010
last_verified: 2026-08-25
---

# RQ-010 — Adaptive captions, Vietnamese support, transcript and replay

## Decision summary

Nếp should **not** default to always-on subtitles and should **not** enforce a rigid universal sequence such as "audio → English caption → Vietnamese subtitle" for every learner and every failure.

The correct product contract is:

```text
first attempt under known support state
        ↓
record what learner could do
        ↓
if failure: diagnose likely bottleneck
        ↓
select the smallest support that targets that bottleneck
        ↓
retry / learn
        ↓
remove answer-bearing support when feasible
        ↓
later test on unseen or support-reduced input
```

Captioning is a learning scaffold. Caption-visible success is not retroactively independent listening success.

## Why always-on captions are dangerous as a measurement policy

Captions often improve immediate comprehension and vocabulary-related outcomes (`SRC-0098`, `SRC-0110`). But eye-tracking/reliance research also shows that lower-proficiency learners can allocate most of their processing to text (`SRC-0101`, `SRC-0102`, `SRC-0108`).

Therefore:

```text
video + captions → correct gist
```

supports a claim such as:

```text
understood_with_L2_caption = true
```

not:

```text
independent_listening = true
```

This distinction is essential for Nếp because the product goal is eventual comprehension without permanent answer-bearing text.

## Support is multi-dimensional, not a single ladder

A replay and a translation are fundamentally different interventions.

### Replay

Replay gives another encounter with the same audio. It can improve processing opportunity without revealing the answer. But after replay, the attempt is no longer a first-exposure attempt.

Store:

```text
exposure_index
replay_count
window_start
window_end
```

### L2 caption

L2 captions reveal orthographic form and segmentation. They are especially useful when the learner knows a word in print but fails to identify it in connected speech.

They can support:

```text
sound ↔ word-form mapping
segmentation
confirmation of lexical form
```

They can also dominate attention for lower-proficiency learners.

### Vietnamese micro-gloss

A micro-gloss is a targeted semantic scaffold. It should be used when the learner has accessed the L2 form but meaning is blocking comprehension.

It should not reveal more message content than necessary.

### Full L2 transcript

A full transcript is a strong form/segmentation scaffold because the entire spoken sequence can be inspected at the learner's pace. It is better treated as a repair/analysis tool than as default listening display.

### Full Vietnamese subtitle / translation

This is the strongest direct semantic route. It can be appropriate when content comprehension is the objective or when the learner otherwise cannot recover the message. But success after full L1 meaning support cannot count as independent L2 message comprehension.

## Failure-contingent policy

After an unsupported or minimally supported first attempt:

```text
A. message seems understood
   → no extra support
   → optionally replay to consolidate

B. learner heard/identified little
   → replay short window
   → if still blocked: L2 caption / highlighted phrase

C. learner identifies phrase but meaning is missing
   → Vietnamese micro-gloss

D. learner is globally lost despite bounded support
   → full caption or transcript for analysis
   → if still necessary: full Vietnamese meaning support

E. learner needs persistent full translation to follow the clip
   → mark clip as scaffold-heavy / possibly not ready
   → do not treat completion as listening success
```

This integrates `FEAT-LIS-001`, `FEAT-SCF-001` and `FEAT-VID-002` rather than creating a separate subtitle-only learning system.

## Full vs keyword captions

The literature does not justify a universal rule that "less text is better." Full captions outperform keyword captions for some comprehension outcomes, while differentiated/partial modes can work better for some caption-reliance profiles (`SRC-0099`, `SRC-0104`).

Therefore Nếp should not make keyword captions the default merely to appear more listening-focused.

Candidate rule:

```text
use full L2 caption when segmentation/global decoding is the bottleneck
use targeted/highlighted form when a narrow lexical target is the bottleneck
```

The exact mode remains falsifiable.

## L1 versus L2 text

L1 subtitles can improve immediate content comprehension (`SRC-0094`, `SRC-0109`), while L2 captions more directly expose the relationship between heard and written L2 forms and have strong support for vocabulary/form learning (`SRC-0098`, `SRC-0110`).

So the choice must follow the learning objective:

```text
objective: understand story/content now
→ L1 support may be efficient

objective: decode L2 speech / form mapping
→ L2 caption is more directly aligned

objective: independent listening evidence
→ neither may be visible during the scored attempt
```

## When should captions disappear?

No literature-backed CEFR threshold can answer this for Nếp's learning objective.

A 2024 study found captions improved TV *content comprehension* across proficiency levels until the highest band in that sample (`SRC-0107`). That does **not** imply Nếp should keep captions on until C2, because Nếp also wants to measure and train listening without text.

Removal should instead depend on learner evidence:

```text
if learner succeeds repeatedly with lower support
→ sample a no-caption attempt

if no-caption performance remains stable on unseen parallel windows
→ reduce caption frequency

if performance collapses
→ restore targeted support, not permanent full captions
```

## Support-fading evidence

Progressive reduction is pedagogically plausible and learners report positive experiences with it (`SRC-0105`), but current evidence is not strong enough for a fixed global sequence.

Nếp should therefore test **adaptive fading** rather than hard-code a weekly schedule.

## Evidence provenance

Every attempt should capture:

```ts
type ViewingSupportState = {
  captionMode: "none" | "keyword" | "full" | "enhanced";
  captionLanguage: "none" | "en" | "vi" | "dual";
  transcriptVisible: boolean;
  vietnameseGlossLevel: "none" | "micro" | "phrase" | "full";
  replayCount: number;
  playbackRate: number;
  exposureIndex: number;
  answerBearingSupport: boolean;
}
```

Evidence interpretation must be support-sensitive.

## What RQ-010 does not establish

It does not establish:

- a universal caption order;
- that audio-first is always superior to captions-first for learning;
- that keyword captions are always better than full captions;
- that L1 subtitles are harmful;
- a CEFR level at which captions should permanently disappear;
- a fixed number of replays;
- that transcript access is equivalent to synchronized captions;
- the exact optimal support sequence for Vietnamese near-A0 learners.

Those remain direct Nếp experiments.

## Product decision

Upgrade `FEAT-VID-001` from a generic later-stage idea into a research-backed **adaptive support controller**. It may operate only on clips already admitted by `FEAT-VID-002`.
