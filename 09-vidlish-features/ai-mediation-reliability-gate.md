# FEAT-AIG-001 — AI mediation and reliability gate

**Status:** research-backed candidate  
**Research question:** `RQ-020`  
**Synthesis:** `SYN-AI-001`  
**Experiment:** `EXP-020`

## Purpose

Provide one shared reliability boundary for LLM generation, AI tutoring, automated feedback, AI evaluation, conversation agents and TTS.

This feature does **not** replace domain engines. It decides what authority a particular AI output is allowed to have.

## Core invariant

```text
model output
≠
learner evidence
```

## Supported roles

```text
generator
tutor
feedback
evaluator
conversation_partner
tts_source
```

A provider/model can be enabled for one role and disabled for another.

## Role registry

```text
ai_role_policy
  role
  provider
  model_family
  model_version
  allowed_constructs[]
  allowed_task_types[]
  allowed_population_scope
  max_authority
  required_validators[]
  required_regression_suite
  abstention_policy
  privacy_profile
  active
```

## Authority states

```text
PROPOSE
ASSIST
DIAGNOSE
SUPPORT_EVIDENCE
DURABLE_EVIDENCE
```

`DURABLE_EVIDENCE` is exceptional. New model/role combinations default to `PROPOSE`.

## Request contract

```text
ai_mediation_request
  request_id
  role

  learner_scope
    anonymized_learner_id
    proficiency_band
    l1_if_relevant

  curriculum_scope
    capability_id
    target_ids[]
    prerequisite_ids[]
    allowed_vocabulary_band
    allowed_constructions[]
    forbidden_support[]

  construct
  task_type
  response_mode

  provider
  model
  model_version
  prompt_id
  prompt_version
  rubric_id
  rubric_version
  generation_config

  privacy
    data_classes[]
    raw_audio_included
    raw_text_included
    history_window
```

## Response contract

```text
ai_mediation_result
  request_id
  raw_output_ref
  parsed_output

  validation
    schema_valid
    deterministic_checks[]
    curriculum_constraints_passed
    support_leakage_passed
    scope_valid
    regression_version_valid
    disagreement_state

  confidence_class
  permitted_action
  evidence_authority

  provenance
    provider
    model
    model_version
    prompt_version
    rubric_version
    generated_at
```

## Generator gate

Generated content must pass schema, target/prerequisite constraints, vocabulary/construction bounds, answer-leakage checks and an acceptable-response contract.

Generated content is disposable; learner state must not depend on generation success.

## Tutor gate

AI tutor output may explain, contrast, hint, ask repair questions or provide Vietnamese support when scaffold policy allows it.

Any revealed information increments support provenance. A correct answer after support is not independent evidence.

## Feedback gate

Prefer structured candidates:

```text
feedback_candidate
  construct
  span_or_event
  suspected_issue
  evidence
  suggested_repair_type
  confidence
```

Avoid unsupported holistic scores such as `Fluency 76` or `Pronunciation 88%`.

## Evaluator gate

Before evaluator output can become supporting evidence:

1. construct and rubric are defined;
2. population/task scope matches validation;
3. model/prompt/rubric version is current;
4. regression suite is passing;
5. output schema passes;
6. confidence/abstention rules pass.

Even then, the Evidence Engine—not the LLM—maps observations into learner state.

## Conversation-partner gate

Record partner model/version, accommodation policy, repair behavior, timing and voice source.

Store support events such as:

```text
partner_rephrased
partner_inferred_intent
partner_offered_word
partner_corrected_grammar
partner_ignored_error
```

This prevents `AI understood me` from silently becoming `humans will understand me`.

## TTS gate

```text
tts_asset
  asset_id
  text
  target_ids[]
  provider
  engine
  engine_version
  voice_id
  locale
  rate
  generated_at

  qa
    text_match
    target_form_check
    pronunciation_check
    clipping_check
    unexpected_pause_check
    approved_for[]
```

Approval classes can include instruction audio, controlled practice, changed-context practice, listening probe and transfer probe. Default `TTS transfer_probe = false` until validated.

## Regression registry

```text
ai_validation_record
  role
  provider
  model_version
  prompt_version
  rubric_version
  validated_at
  population_scope
  task_scope
  construct_scope
  benchmark_set_version
  n_cases
  error_metrics
  subgroup_metrics
  allowed_authority
  expires_on_change
```

Revalidate after model/provider/prompt/rubric/parser/scorer changes, and after TTS engine/voice changes when evidence audio depends on them.

## Required Nếp regression slices

- task constraint following;
- A0/A1 vocabulary bounds;
- construction correctness;
- Vietnamese-L1 likely error cases;
- answer/support leakage;
- false correction;
- missed correction;
- pragmatic variation;
- conversation over-accommodation;
- TTS target-form realization.

Aggregate pass rate alone is insufficient because a model can improve overall and regress on a critical learner slice.

## Privacy profile

Each role receives a data budget. Generator should need no raw learner data; feedback normally needs only the current response and target context; conversation gets a bounded history window.

Do not attach full learner history merely because it is available.

## Fallbacks

```text
generator → curated item
tutor → authored hint
feedback → self-repair / rule feedback
evaluator → deterministic evidence / no judgment
conversation → scripted branch
TTS → curated human recording
```

## Telemetry

Track role, authority requested/granted, rejection reason, abstention, disagreement, false-correction audit, missed-issue audit, cost, latency, data classes sent, exact model/prompt/rubric version and downstream delayed learning outcome.

## Product metric

AI is valuable if it improves learning gain/minute, diagnosis accuracy/minute, useful practice diversity or production cost without unacceptable false correction, false mastery, support dependence, privacy exposure, latency or provider lock-in.

## Principles

Implements `PRN-261` through `PRN-276`.

## Open implementation decisions

Provider/model per role; confidence thresholds; deterministic validator coverage; escalation rate; TTS voice/QA policy; natural-speech transfer frequency; raw-data retention; regression cadence; acceptable cost and latency.
