# FEAT-VIE-001 — Vietnamese learner calibration layer

**Status:** research-backed-candidate  
**Synthesis:** `SYN-VIE-001`

## Purpose

Use Vietnamese-L1 research to reduce wasted diagnostic and practice time while preventing nationality-based stereotyping.

This feature is a thin routing layer over existing Nếp engines. It does not own mastery, lessons or a separate curriculum.

## Core contract

```text
L1 evidence may choose what to test first.
Only learner evidence may confirm what this learner needs.
```

## Data model

```text
l1_risk_prior
  learner_l1
  target_family
  construct
  prior_weight
  evidence_source_ids[]
  applicable_stage
  moderators[]

learner_calibration_probe
  probe_id
  target_family
  construct
  input_mode
  response_mode
  support_level
  context
  result
  attempted_at

learner_l1_calibration
  target_family
  state              not_tested | uncertain | confirmed | disconfirmed
  confidence
  last_evidence_at
  evidence_refs[]
```

The `l1_risk_prior` row is design-time / model metadata. It is not a learner score.

## Initial candidate probe families

### Pronunciation / speech perception

- simple word-final coda preservation;
- selected final-cluster simplification;
- word-prominence identification;
- short phrase prominence/timing;
- selected lexical contrasts only where confusion changes meaning.

Every pronunciation target has separate:

```text
perception_evidence
production_evidence
intelligibility_impact
```

### Listening

Use known-language controls.

Example diagnostic sequence:

```text
1. play: “She works here.”
2. learner misses it
3. show written form without translation
4. written meaning succeeds
5. replay / isolate relevant chunk
```

Possible inference:

```text
lexical meaning probably available
phonological decoding / chunk recovery remains suspect
```

The system still records bounded evidence, not a diagnosis of a cognitive disorder.

### Vocabulary / chunks

Candidate metadata:

```text
l1_congruency
  unknown
  approximately_congruent
  noncongruent
  mixed
```

Use it to vary initial attention/support. Never use it as a correctness shortcut.

### Grammar / constructions

Candidate risk families:

- article / definiteness mapping;
- plural morphology and number meaning;
- mass-count flexibility;
- tense/aspect form-meaning marking;
- third-person agreement;
- copula + adjective.

Probe only when the construction is stage-appropriate or required by the current capability.

### Pragmatics

No A0 national-style score.

At later stages, probe through concrete scenarios with explicit relationship and setting variables.

## Priority algorithm

Illustrative only:

```text
if observed_valid_failure:
    priority = impact × frequency × readiness × persistence_of_failure
elif high_l1_prior and cheap_probe_available:
    schedule_probe
else:
    no special intervention
```

`high_l1_prior` alone must never schedule repeated remediation.

## Routing behavior

```text
confirmed coda production issue
→ FEAT-PRN-001

written-known / audio-missed chunk
→ FEAT-LIS-001

noncongruent chunk retrieval weakness
→ FEAT-VOC-001 + FEAT-REV-001

article/number meaning-form weakness
→ FEAT-GRM-001

contextual request mismatch
→ FEAT-INT-001
```

## Guardrails

1. Do not display “Vietnamese learners usually fail X” to the learner as a diagnosis.
2. Do not infer dialect from country or city.
3. Do not use nationality as a mastery feature.
4. Do not force pronunciation work after the learner has demonstrated reliable intelligible performance.
5. Do not count written grammar errors as speaking failure without speaking evidence.
6. Do not treat accent difference as error unless the target contrast matters for meaning/intelligibility or the learner explicitly wants accent coaching.
7. Do not create separate learner-state truth from L1 priors; actual attempt history remains authoritative.

## Product UI

The UI should surface the consequence, not the stereotype.

Good:

> You hear **worked** correctly in isolation, but the ending disappears for you in a short sentence. We’ll train that contrast in context.

Bad:

> Vietnamese people often drop final sounds, so you need this lesson.

## Success condition

`FEAT-VIE-001` is useful only if it improves one or more of:

- diagnostic precision,
- time to identify a real bottleneck,
- delayed changed-context learning per minute,
- learner recovery from persistent errors,

without increasing unnecessary remediation for learners who do not exhibit the predicted risk.

That trade-off is tested in `EXP-019`.
