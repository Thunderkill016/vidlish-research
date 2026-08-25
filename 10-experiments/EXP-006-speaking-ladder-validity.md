---
id: EXP-006
title: Calibrate near-A0 speaking task ladder
status: proposed
research_question: RQ-006
---

# EXP-006 — What is the smallest speaking demand that produces useful later speech?

## Question

For Vietnamese-speaking adults near A0, which early speaking practice condition produces the best delayed unsupported performance on **unseen short speaking tasks** at acceptable time and failure cost?

## Core design

Use matched target chunks/constructions within learner after comparable comprehension/form learning.

### A — model-led rehearsal

```text
hear/see model
→ repeat / read aloud
```

This is an active rehearsal baseline, not independent production evidence.

### B — controlled independent oral retrieval

```text
brief preparation
→ hide answer-bearing model
→ picture/meaning/bounded cue
→ learner retrieves short utterance
→ feedback
```

### C — controlled retrieval + guided interaction

```text
condition B
+
standardized one- or two-turn conversational use
```

Example:

```text
interlocutor: "What do you want?"
learner: "I want tea."
```

Keep total practice time approximately matched where feasible. If exact matching would distort natural task delivery, record time precisely and analyze learning per minute.

## Delayed criterion

After pre-registered delays, assess all target sets on **unseen parallel tasks** with no answer-bearing support.

Criterion families:

1. short oral target/utterance retrieval;
2. controlled recombination with a known new slot;
3. standardized guided turn for a stratified subset;
4. later sampled multi-turn role-play if prerequisites are met.

Do not reuse training prompts as the primary criterion.

## Scoring

RQ-008 is not complete, so do not make opaque ASR scores the primary outcome.

Initial experiment should use:

- blinded human scoring for communicative/target success, or a validated tightly constrained scoring procedure;
- at least a reliability sample with two independent raters;
- explicit accepted-response variants;
- separate task-success and target-form judgments where useful.

## Primary outcomes

```text
delayed unseen productive success
────────────────────────────────
practice minutes
```

and

```text
probability of successful guided turn
on a first-seen parallel prompt
```

## Secondary outcomes

- support needed before independent response;
- response latency;
- successful self-repair after a prompt;
- speaking-task abandonment;
- voluntary retry;
- retention at a longer checkpoint;
- learner return for speaking review;
- gap between exact-task repetition and unseen parallel production.

## Key hypotheses to test, not assume

- B will outperform A on delayed independent production.
- C may outperform B on later guided interaction, but may add unnecessary burden for some near-A0 learners.
- Benefits may be concentrated in learners who already have enough comprehension/lexical prerequisites.
- Visible-script rehearsal may improve pronunciation/familiarity without predicting independent speaking well.

## Support-fading sub-study

Within B/C, compare feasible preparation paths such as:

```text
full model → keyword cue → independent
```

versus

```text
full model → independent
```

Do not compare too many support variants in the first experiment if sample size cannot support the design.

## Interaction standardization

For C:

- pin interlocutor wording/allowed variants;
- control speech rate and vocabulary;
- define repair behavior;
- keep target turn comparable across conditions;
- version the interaction script.

If generative AI is used for surface realization, log the exact prompt/output and constrain it to the same validated interaction contract.

## Decision rule

Ship the **least demanding** speaking progression that materially improves delayed unseen productive performance.

Do not expand to free AI conversation as a default if:

- controlled/guided tasks predict later performance just as well at much lower cost;
- open tasks create unscorable/confounded failures;
- learner abandonment rises substantially;
- performance depends mainly on memorized scripts.

## Pre-register

- near-A0 inclusion criteria;
- target chunks/constructions;
- prerequisite evidence requirement;
- exact rehearsal/retrieval/interaction procedures;
- support visibility rules;
- delayed test intervals;
- unseen criterion tasks;
- scoring rubric and accepted variants;
- scorer reliability procedure;
- practice-time accounting;
- minimum worthwhile production gain;
- maximum acceptable abandonment/failure rate;
- missing-session and exclusion rules.
