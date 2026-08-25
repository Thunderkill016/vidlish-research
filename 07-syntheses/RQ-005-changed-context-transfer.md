---
id: SYN-TRN-001
title: Changed-context transfer policy for Nếp
status: initial-synthesis
research_question: RQ-005
last_verified: 2026-08-25
---

# RQ-005 — Measuring transfer without over-testing beginners

## Decision summary

Nếp should only label evidence `transferred` when the learner succeeds on an **unseen, changed requirement**, but near A0 the change should be small enough that failure can still be attributed to the target language rather than to unrelated novelty.

The core distinction is:

```text
TRAINED EPISODE
"I want water." + known picture/context
        ↓
exact replay/retest
        = retention / trained-context evidence

UNSEEN PARALLEL EPISODE
"I want tea." / new speaker / new café cue
        ↓
same target relation, changed context
        = candidate transfer evidence
```

Transfer is not “a harder quiz.” It is evidence that the learner's capability survived a meaningful change.

## Why Nếp needs transfer evidence

Without it, a learner can appear strong because the app repeatedly supplies:

- the same sentence;
- the same picture;
- the same speaker;
- the same answer positions;
- the same L1 cue;
- the same task type.

That can produce excellent lesson accuracy while leaving the underlying language tied to one training episode.

`SRC-0041` establishes the measurement boundary: transfer is different from ordinary same-task retention and varies with what changes between learning and assessment.

## What the evidence supports

### 1. A changed-context probe must actually change something meaningful

A verbatim replay of a training item cannot demonstrate generalisation merely because it occurs later.

Useful change dimensions include:

```text
referent / object
surface wording
sentence exemplar
speaker / voice
visual situation
cue direction
modality
required response
communicative scenario
```

**Product consequence:** every transfer attempt needs a `novelty_signature` describing how it differs from training.

### 2. Near transfer is the right starting point for near A0

Transfer research and contextual-learning studies show benefits from changed contexts, but the L2 evidence also shows that variability adds processing demand (`SRC-0046`, `SRC-0047`, `SRC-0048`). `SRC-0047` is especially important: contextual diversity could be adverse for learners with lower lexical proficiency.

**Product consequence:** Nếp should not jump from one trained phrase to a completely open conversation. Begin with an unseen **parallel** context that changes one important dimension while preserving enough known language.

### 3. Familiar-context success can be real but narrower

Same-context repetition can produce faster processing and stronger immediate performance (`SRC-0046`). `SRC-0045` and `SRC-0048` also show why familiar contexts can support context-bound or episodic retrieval.

**Product consequence:** store familiar-context success as valid evidence, but do not silently upgrade it to flexible transfer.

### 4. Context variation can support flexibility, but more is not always better

`SRC-0045` and `SRC-0049` provide convergent evidence that varied learning contexts can make word knowledge easier to apply in new contexts. Yet direct L2 results are mixed, and high diversity is not uniformly advantageous (`SRC-0046`, `SRC-0047`).

**Product consequence:** vary examples progressively across learning, not maximally. The transfer system should seek **controlled novelty**, not novelty for its own sake.

### 5. Match transfer evidence to the claimed capability

A new-context multiple-choice item may show semantic/comprehension transfer. It does not prove the learner can independently produce the target.

Productive vocabulary training tends to produce stronger productive outcomes than receptive-only practice (`SRC-0052`). Productive vocabulary assessment also has different practical constraints (`SRC-0053`).

**Product consequence:** keep distinct labels such as:

```text
transfer_recognition
transfer_comprehension
transfer_controlled_production
transfer_open_production
```

These are evidence/task categories, not latent-skill claims.

### 6. Do not make A0 prove everything with free production

Free speaking/writing adds many uncontrolled demands: lexical choice, grammar, spelling/pronunciation, planning, anxiety/interface burden and synonym ambiguity. A failure may not isolate the target at all.

`SRC-0053` supports the practical role of controlled production for lower vocabulary levels, while `SRC-0052` supports including productive tasks when production is the desired outcome.

**Product consequence:** Nếp may use bounded production such as one missing chunk, word-order assembly without the answer visible, short L1→L2 retrieval, or a constrained scenario response before asking for open production.

### 7. Difficulty must be desirable, not merely difficult

Foreign-vocabulary work shows that harder training can sometimes improve delayed retention/transfer (`SRC-0050`), but the 2025 re-examination shows no universal benefit and even negative transfer under some interference conditions (`SRC-0051`).

**Product consequence:** transfer difficulty should increase only after enough foundation exists. A failed far-transfer probe at A0 may measure overload rather than weak language knowledge.

### 8. A transfer probe is also a learning event

Retrieval/testing itself can change later performance (`SRC-0041`, RQ-004). Once an unseen transfer item is shown, it is no longer unseen.

**Product consequence:** preserve `probe_id`, `first_seen_at` and novelty metadata. Do not reuse the exact same “transfer” item and continue calling later successes independent transfer.

## Proposed transfer ladder

This is a **product taxonomy to test**, not a scientifically fixed scale.

### `T0` — trained-context retention

```text
same sentence / same cue / same speaker or close replay
```

Useful for retention. **Not transfer.**

### `T1` — minimal near transfer

Change one bounded feature while preserving the function/construction.

Example:

```text
trained: I want water.
probe:   I want tea.
```

or a new picture with the same language relation.

### `T2` — parallel-context transfer

Use a new surface sentence or situation while preserving the target meaning/function and keeping surrounding language highly known.

Example:

```text
trained in home context: "I need water."
new shop context: identify/produce "I need a bag."
```

### `T3` — modality / speaker / response transfer

Change an additional relevant dimension:

```text
read → listen
speaker A → speaker B
recognize → controlled produce
```

Only use when the new dimension is itself sufficiently supported.

### `T4` — open/farther transfer

The learner must independently formulate language in a substantially new situation.

This is valuable later, but it is too confounded and costly to be the default evidence probe for every near-A0 item.

## Probe construction rules

A useful near-A0 transfer probe should:

1. be unseen before the attempt;
2. retain the same target capability being tested;
3. change one or a small number of pre-declared dimensions;
4. keep non-target vocabulary/grammar within demonstrated learner capability;
5. hide answer-bearing support before the scored attempt;
6. avoid accidental answer cues from pictures, word order or distractors;
7. record support and response modality;
8. never infer a broader capability than the task demonstrates.

## Example: lexical + listening target

Training:

```text
🔊 "I want water."
meaning understood
"want" recalled
```

Bad transfer test:

```text
same recording
same picture
same three answers
```

Better `T1/T2` listening transfer:

```text
new speaker
🔊 "I want tea."
new picture set
question asks intended meaning
```

This can support **listening/comprehension transfer** for the pattern. It does not yet prove speaking.

Production probe later:

```text
context: café + tea image
Vietnamese task instruction only: "Bạn muốn trà. Nói câu ngắn."
→ learner produces "I want tea."
```

If the answer was not shown and surrounding language was already known, this is stronger controlled-production transfer evidence.

## Example: construction target

Training exemplars:

```text
I want water.
I want coffee.
```

A new example:

```text
I want a ticket.
```

can test whether the learner handles the construction with a new lexical slot **only if `ticket` is independently known**. Otherwise the probe confounds construction transfer with new vocabulary.

## Data model

Every candidate transfer attempt should retain:

```text
transfer_attempt
  learner_id
  target_id
  capability_claim

  training_family_id
  probe_id
  probe_first_seen

  transfer_level
  novelty_dimensions[]
  changed_context_id
  changed_speaker
  changed_modality
  changed_response_type

  non_target_coverage
  support_level
  support_types[]

  response
  correctness
  latency
  occurred_at
```

For generated content also store:

```text
generator_version
content_review_status
novelty_rule_version
```

## Sampling policy

Transfer probes should be **diagnostic samples**, not a tax paid on every repetition.

Candidate behavior:

```text
new target
→ establish comprehension/recall
→ one near-transfer sample
→ delayed review
→ transfer sampled again when evidence is stale/important
```

A high-frequency/critical construction may deserve more transfer sampling than a low-value lexical item.

The exact frequency is a product assumption for `EXP-005`.

## Relationship to RQ-001–004

```text
RQ-001
what evidence means "knows a word/chunk"
        ↓
RQ-002
what support was visible
        ↓
RQ-003
what was heard vs understood
        ↓
RQ-004
when another attempt is useful
        ↓
RQ-005
whether capability survives a changed requirement
```

Together these make it possible for Nếp to say something much narrower and more defensible than “lesson completed.”

## Current answer to RQ-005

For near A0, use **graduated unseen parallel probes** rather than exact replays or immediate open conversation.

A transfer label requires:

```text
unseen item
+ meaningful controlled change
+ answer hidden
+ bounded non-target difficulty
+ task-matched evidence
```

Start with near transfer; increase novelty only after lower-level evidence is stable. Sample transfer often enough to detect context-bound learning, but not so often that assessment dominates instruction.

The exact novelty threshold, probe frequency and cheapest predictive task remain product assumptions and must be calibrated in `EXP-005`.
