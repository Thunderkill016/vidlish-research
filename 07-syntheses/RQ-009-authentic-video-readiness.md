---
id: SYN-VID-002
title: Learner- and clip-specific readiness for authentic audiovisual input
status: initial-synthesis
research_question: RQ-009
last_verified: 2026-08-25
---

# RQ-009 — When is an authentic clip usable?

## Decision summary

Nếp should **not unlock authentic video from one global vocabulary count or CEFR label**.

Authentic audiovisual input should be admitted through a learner × clip readiness gate:

```text
learner evidence
  ×
clip-specific aural lexical coverage
  ×
speech-processing load
  ×
visual-semantic support
  ×
topic/context familiarity
  ×
support required
        ↓
video readiness state
```

The useful unit is initially a **short window inside a source**, not an entire YouTube video, episode or movie.

## Why a global “3,000 words unlocks video” rule is wrong

Large corpus studies show that knowledge around the 3,000-frequency level often yields roughly 95% lexical coverage of TV/movie dialogue (`SRC-0091`, `SRC-0092`, `SRC-0093`). But those are averages across huge corpora. Genre, episode and local-window demands vary substantially.

So this inference is invalid:

```text
learner knows 3,000 word families
→ any TV clip is appropriate
```

and so is this:

```text
learner knows only 800 words
→ no authentic clip can ever be usable
```

A carefully selected 15–45 second authentic window may contain almost entirely known language, clear visual grounding and one predictable message. Conversely, a “beginner” video can be unusable if it packs unknown words, multiple speakers, fast reductions and weak visual support.

The exact window length is a product assumption, not a literature-established threshold.

## Lexical coverage: use it, but do not worship it

Listening work indicates that lexical coverage is strongly related to comprehension, with ~95% a useful candidate level for relatively stable comprehension of informal spoken narratives and 90% producing more learner variation (`SRC-0087`, `SRC-0088`).

Viewing work makes the picture more nuanced. In short documentary viewing, `SRC-0090` found substantially useful content comprehension even at lower coverage because imagery contributes meaning; the authors proposed 95% for optimal adequate comprehension and 80% for minimal adequate comprehension in that task.

Nếp must preserve the distinction:

```text
content comprehension aided by imagery
≠
audio comprehension
≠
listening-learning readiness
```

Therefore 80% must **not** become an “authentic listening is safe” threshold.

### Candidate product interpretation

These are heuristic readiness bands to test, not scientific constants:

```text
>= ~95% aural lexical coverage
+ manageable speech load
+ useful visual grounding
→ candidate independent/supported authentic window

~90–95%
→ candidate supported window if one narrow learning target is selected

< ~90%
→ usually too lexically dense for audio-led near-A0 work
   unless the window is deliberately bounded/pre-taught and the goal is not independent listening
```

For Vietnamese near-A0 learners, `EXP-009` must calibrate these bands directly.

## Measure aural knowledge, not merely visual vocabulary

For video readiness, “known vocabulary” should prefer evidence that the learner can access the word/chunk from speech (`FEAT-LIS-001`, `FEAT-VOC-001`).

This is weaker evidence:

```text
learner sees "water"
→ knows meaning
```

than:

```text
learner hears /ˈwɔːtər/
→ recognizes WATER
→ accesses meaning
```

A clip can have high orthographic coverage but still be impossible if the learner cannot segment its known words in connected speech.

## Viewing is not just listening with pictures

`SRC-0089` and `SRC-0090` show that imagery changes comprehension. Visuals can:

- reveal referents;
- disambiguate actions and participants;
- provide world/context information;
- let viewers answer some questions without fully decoding audio.

This is useful pedagogically, but it creates a measurement trap.

Nếp should score at least two different outcomes:

```text
message_understanding_with_video

audio_based_understanding
```

A learner who gets the story from imagery has gained useful comprehension, but that attempt should not automatically update independent listening mastery.

## Visual-semantic grounding matters

`SRC-0095` found that imagery close to the spoken occurrence of a word was positively related to vocabulary learning.

Therefore clip analysis should record whether the visuals actually ground the language:

```text
high grounding
speaker says "coffee"
→ cup/coffee/order visibly present

low grounding
speaker discusses an abstract relationship
→ generic talking head / unrelated B-roll
```

The first type is more suitable earlier even if both clips are “authentic”.

## Speech-processing load is multidimensional

Vocabulary is only one bottleneck. Candidate load dimensions include:

```text
speech rate / playback rate
connected-speech reduction
speaker clarity
number of speakers
turn-switch density
overlap
acoustic noise/music
accent familiarity
utterance length
syntactic density
proper-name density
visual complexity
```

`SRC-0097` supports the interaction between playback rate, captions and proficiency. RQ-009 does not establish one safe words-per-minute value. A learner may handle faster highly predictable speech better than slower lexically dense speech.

Nếp should therefore estimate speech rate as one feature in a readiness model, never as the whole model.

## Topic familiarity is support, not mastery

Prior knowledge can reduce the inferential burden of listening. Topic/context familiarity should be treated as a support variable:

```text
same language + familiar café scenario
< difficulty
same language + unfamiliar technical process
```

But if a learner succeeds only because the message was obvious from prior knowledge, Nếp should not over-credit audio comprehension.

## Captions change the task

`SRC-0094` and `SRC-0096` reinforce that captions/subtitles can increase comprehension, especially at lower proficiency. That is useful, but it means readiness has two different questions:

1. Can this clip be made pedagogically usable with support?
2. Can this learner process enough of its speech without answer-bearing text for it to function as listening input?

RQ-010 will determine caption/reveal policy. RQ-009 establishes that support level must be part of the readiness state.

## Readiness states

Candidate product states:

### V0 — not ready

```text
critical lexical load too high
or
speech processing far beyond learner evidence
or
message depends on unsupported language
```

Do not offer as ordinary learning input.

### V1 — scaffolded exposure

```text
clip has useful authentic value
but learner needs pre-teaching / English caption / bounded Vietnamese support
```

Allowed as an exposure/learning source. Success does not equal independent viewing/listening mastery.

### V2 — audio-led learning window

```text
most lexical material is aurally accessible
speech load is manageable
visual context supports rather than replaces audio
```

First attempt can reasonably hide answer-bearing captions and collect comprehension evidence.

### V3 — independent authentic window

```text
learner repeatedly understands first-seen matched windows
with little/no answer-bearing support
and can transfer across speaker/context variants
```

This is an evidence-derived learner capability, not a vocabulary-size badge.

## Clip windows, not source labels

One source can contain:

```text
00:10–00:28  usable
00:29–00:51  too dense
00:52–01:08  usable with scaffold
```

Therefore Nếp should ingest sources into windows and rank windows individually. The original video remains provenance; the pedagogical unit is the window.

## Readiness is dynamic

A clip can move from V0/V1 to V2/V3 as the learner develops:

```text
learner model changes
→ recompute aural coverage
→ recompute evidence match
→ unlock new window or reduce support
```

This makes authentic video a graduated destination rather than a separate “advanced mode”.

## What Nếp must not claim yet

RQ-009 does not establish:

- exact lexical bands for Vietnamese near-A0;
- exact clip length;
- exact WPM thresholds;
- exact speaker-count penalty;
- exact visual-grounding score;
- exact amount of pre-teaching allowed;
- a fixed vocabulary count before the first authentic clip.

Those values belong to `EXP-009` and later product data.
