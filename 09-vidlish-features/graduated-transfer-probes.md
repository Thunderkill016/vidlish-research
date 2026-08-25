---
id: FEAT-TRN-001
title: Graduated changed-context transfer probes
status: candidate-core
research_question: RQ-005
---

# Feature research spec — Graduated changed-context transfer probes

## Learner problem

A learner can memorize an app's exact sentence, picture, speaker and answer pattern without being able to use the same language when any of those cues change. Conversely, a probe that changes too much can make a near-A0 learner fail for reasons unrelated to the target.

## Target capability

Measure whether a learned lexical item, chunk, listening pattern or construction survives a controlled change in context, while keeping the probe cheap enough to use repeatedly inside a real learning product.

## Research basis

- `SYN-TRN-001`
- `CLM-TRN-001` through `CLM-TRN-010`
- `PRN-040` through `PRN-049`
- RQ-001 evidence model
- RQ-002 scaffold provenance
- RQ-003 listening evidence
- RQ-004 review orchestrator

## Architecture

```text
Training Family
      │
      ├── target capability
      ├── known context/exemplars
      └── learner prerequisite evidence
      ↓
Transfer Probe Selector
      │
      ├── choose novelty dimensions
      ├── enforce non-target coverage
      └── choose response type
      ↓
Unseen Probe
      ↓
Attempt before reveal
      ↓
Evidence Interpreter
      │
      ├── retention only
      ├── near-transfer evidence
      └── insufficient / confounded
      ↓
Evidence Engine + Review Engine
```

## Transfer levels

```text
T0 trained-context retest        → retention, not transfer
T1 one bounded dimension changed → minimal near transfer
T2 new parallel context          → stronger near transfer
T3 modality/speaker/response shift when prerequisites permit
T4 open/farther transfer         → later / sampled
```

The level is product metadata. It is not a universal psychological scale.

## Novelty dimensions

Candidate enum:

```text
referent
lexical_slot
surface_wording
sentence_exemplar
visual_context
scenario
speaker
acoustic_realization
modality
cue_direction
response_type
target_position
```

A probe may change several dimensions, but near A0 should normally begin with one important change.

## Hard constraints for scored transfer

1. `probe_first_seen = true` at scored attempt.
2. Answer-bearing English/Vietnamese support hidden before response.
3. Non-target language is already known or explicitly below a calibrated novelty budget.
4. The changed dimension is recorded.
5. The response requirement matches the capability claim.
6. Exact trained item is never labeled transfer.
7. The probe cannot be reused as an independent unseen probe for the same learner.

## Candidate capability mappings

### Meaning / lexical semantic transfer

```text
new context + target form
→ learner selects/recalls meaning
```

### Listening transfer

```text
parallel utterance + new speaker/context
→ learner demonstrates message/target understanding audio-only
```

### Controlled productive transfer

```text
new bounded situation
→ learner retrieves target English without answer cue
```

### Construction transfer

```text
known construction + known new slot item
→ learner interprets/produces a novel exemplar
```

Do not introduce an unknown slot word and then blame the construction when the learner fails.

## Probe catalogue before generative AI

Initial A0 content should prefer human-authored/reviewed probe families:

```text
training_family
  canonical_examples[]
  T1_probes[]
  T2_probes[]
  prerequisites[]
  forbidden_cues[]
```

AI may later propose variants, but they must pass coverage/novelty checks before becoming scored evidence.

## Attempt state

```text
transfer_attempt
  learner_id
  target_id
  capability_claim
  training_family_id
  probe_id
  first_seen_at
  transfer_level
  novelty_dimensions[]
  response_type
  modality
  speaker_id?
  non_target_coverage
  support_level
  support_types[]
  correctness
  latency
  scoring_rule_version
  occurred_at
```

## Interpretation examples

```text
same sentence correct after 7 days
→ retained = evidence
→ transferred = no

new sentence, known surrounding language, target meaning correct
→ transfer_comprehension = evidence

new scenario, learner independently produces target chunk
→ transfer_controlled_production = evidence

new scenario but learner opened full Vietnamese translation first
→ scaffolded use; not independent transfer
```

## Sampling behavior

Do not transfer-test every target on every review.

Candidate selector prioritizes probes when:

- no transfer evidence exists;
- existing transfer evidence is old;
- target is curriculum-critical/high frequency;
- familiar-context accuracy is high but generalisation is uncertain;
- a stage unlock depends on transferable use.

Session budget remains a hard guardrail.

## UX

The learner should experience this as natural variation, not as a label saying “TRANSFER TEST.”

Example progression:

```text
learn: "I want water."
...
later:
[new café image]
🔊 "I want tea."
What does the person want?
```

Then, only when ready:

```text
[café + coffee image]
"Bạn muốn cà phê. Nói câu ngắn."
🎤 / text response
```

## Risks

- unknown distractors turn transfer into vocabulary difficulty;
- too many changed dimensions overload A0;
- generated probes leak the answer;
- fixed templates become learnable meta-patterns;
- free production makes automatic scoring unreliable;
- transfer probing consumes too much session time;
- repeated probes become training but are still mislabeled unseen.

## Falsification

This feature is not justified if cheap near-transfer probes do not predict later performance on more meaningful unseen tasks, or if their incremental diagnostic value is too small relative to learner time/friction.

## Learning metrics

- delayed unseen parallel performance;
- predictive value of T1/T2 for later criterion tasks;
- productive transfer where sampled;
- audio-only transfer where sampled;
- transfer evidence per probe minute.

## Guardrails

- failure attributable to unknown non-target language;
- average probe time;
- support requests;
- frustration/abandonment;
- curriculum time displaced by probing;
- false-positive transfer from answer leakage.
