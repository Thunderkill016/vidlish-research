---
id: EXP-010
title: Adaptive caption/support policy validation
status: proposed
research_question: RQ-010
---

# EXP-010 — Does adaptive support improve unsupported listening?

## Question

Can a failure-contingent support controller produce better delayed **unsupported** listening than simpler subtitle policies without excessive friction?

## Population

Vietnamese-speaking Nếp learners in the first product stage where `FEAT-VID-002` admits short authentic/semi-authentic windows.

Stratify by:

- prior aural vocabulary evidence;
- listening evidence;
- current caption reliance/support history.

## Conditions

### A — L2 captions always on

All target windows display synchronized English captions.

### B — Vietnamese subtitles always on

All target windows display Vietnamese meaning support.

### C — audio-first fixed ladder

```text
no text
→ if failed: English caption
→ if failed: Vietnamese support
```

### D — adaptive failure-contingent policy

```text
no answer-bearing text
→ diagnose failure
→ choose replay / L2 form support / Vietnamese meaning support / transcript
→ hide support when feasible
```

## Important measurement rule

Immediate success under each condition is not the primary outcome because the conditions expose different amounts of answer-bearing information.

## Primary outcome

After delay, use **first-seen parallel windows with no captions/subtitles/transcript**.

Measure:

```text
gist comprehension
critical-detail comprehension
aural word/chunk recognition
support-free transfer
```

Primary efficiency metric:

```text
delayed unsupported listening gain
────────────────────────────────
video-learning minutes
```

## Secondary outcomes

- immediate supported comprehension;
- number of replays;
- amount/type of answer-bearing support;
- time-on-task;
- learner effort/frustration;
- caption reliance on later probes;
- voluntary support requests;
- abandonment/completion.

## Key diagnostic metrics

### Over-support rate

Learner would have succeeded without answer-bearing support, but policy revealed it anyway.

### Under-support rate

Learner repeatedly fails and policy withholds a support that would make the window learnable.

### Support dependence

Performance drops sharply when support is removed on matched unseen windows.

## Hypotheses

- Always-on L1 subtitles may maximize immediate content comprehension but underperform on unsupported listening transfer.
- Always-on L2 captions may improve form mapping and immediate comprehension but can create heavy text reliance in lower-proficiency learners.
- Adaptive support may reduce answer-bearing exposure while maintaining learnability.

These are product hypotheses, not established facts.

## Decision rule

Adopt adaptive support only if it provides a meaningful improvement in delayed unsupported listening and/or equal learning with materially less answer-bearing support, without unacceptable friction.
