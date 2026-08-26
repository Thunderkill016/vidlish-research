# RQ-020 — AI mediation without false learning evidence

**Synthesis ID:** `SYN-AI-001`  
**Status:** initial synthesis complete  
**Depends on:** `RQ-001`, `RQ-003`, `RQ-005`, `RQ-008`, `RQ-010`, `RQ-014`, `RQ-015`, `RQ-017`, `RQ-019`

## Research question

How should Nếp use LLMs, generative feedback, AI conversation and TTS so that they increase practice and personalization without becoming an unvalidated hidden authority over curriculum or learner evidence?

## Short answer

Treat every AI output as a **role-scoped, versioned signal**, not truth.

```text
learning need
    ↓
declare AI role
    ↓
apply role-specific scope
    ↓
generate / observe
    ↓
validate what can be validated
    ↓
record provenance + uncertainty
    ↓
bounded product action
    ↓
independent learner evidence
```

The closer AI gets to changing durable learner state, the stronger the gate must become.

## Role taxonomy

### 1. Generator

Can propose examples, distractors, changed-context variants, micro-dialogues, explanations and exercise candidates.

It must not decide by itself what concept is ready, whether prerequisites are satisfied, whether a task leaks the answer, or whether generated language belongs at the learner's current difficulty.

```text
broad generation
+
strict downstream constraints
```

### 2. Tutor / scaffold

Can provide bounded explanation, contrast, hint, repair question or Vietnamese explanation when scaffold policy allows it.

If support exposes information:

```text
learner succeeds after AI hint
→ supported evidence
```

not independent mastery.

### 3. Feedback provider

Feedback is a `candidate diagnosis` unless the exact feedback construct is validated.

A bounded candidate such as `third-person -s appears missing` is different from an unsupported holistic statement such as `Your English fluency is 84/100`.

### 4. Evaluator

This is the highest-risk LLM role. It needs a defined construct, response/task type, rubric, validated population/scope, model/prompt/rubric provenance, uncertainty or abstention behavior, regression tests and external reference evidence.

Even then:

```text
LLM evaluation
→ supporting measurement
```

before it can become durable learner evidence.

### 5. Conversation partner

AI can supply abundant, low-pressure turns, but it may infer incomplete meaning, silently repair malformed language, simplify unexpectedly, tolerate unrealistic pauses or avoid real social friction.

Therefore:

```text
successful AI conversation
= AI-supported interaction evidence
```

Human or deliberately less-accommodating transfer remains separate.

### 6. TTS source

TTS offers scalable prompts, arbitrary target sentences, repeatable audio and cheap changed-context material. But synthetic speech is a source condition.

Store provider, engine/version, voice, locale, rate, generation time and QA.

Nếp may use TTS heavily for controlled learning if validated, but robust listening claims require later success with unseen natural/human speech.

## Authority ladder

```text
LEVEL 0 — PROPOSE
LEVEL 1 — ASSIST
LEVEL 2 — DIAGNOSE
LEVEL 3 — SUPPORT_EVIDENCE
LEVEL 4 — DURABLE_EVIDENCE
```

Default AI role begins at low authority. Authority is earned by validation, not model brand.

## Evidence contract

Every AI-mediated attempt that can influence the learner model needs provenance:

```text
ai_mediation
  role
  provider
  model
  model_version
  prompt_id
  prompt_version
  rubric_id
  rubric_version
  generation_config
  timestamp

  input_scope
  learner_data_classes_sent
  target_ids
  capability_id
  construct

  output
  validation_checks
  validation_status
  confidence_class
  disagreement_state

  permitted_action
  evidence_authority
```

For TTS:

```text
tts_provenance
  provider
  engine
  engine_version
  voice_id
  locale
  rate
  generated_at
  pronunciation_qa
  target_form_qa
```

## Fail-closed behavior

High-authority calls must be allowed to abstain. `confidently wrong` is much worse than `no judgment available` for a learning system.

If output violates schema, conflicts with deterministic evidence, is outside validated scope, produces evaluator disagreement, comes from an unvalidated new model version, or lacks provenance, then:

```text
no durable evidence update
```

Fallbacks include deterministic checks, simpler tasks, self-repair prompts, neutral retries, later re-probes, curated content and human-calibrated research samples.

## Deterministic before generative

Use rules where the task genuinely has rules: target list, construction set, prerequisite graph, answer visibility, word count, required slot, exact-choice key and unsupported-vocabulary bounds.

AI can create candidates. Asking the same LLM whether its own candidate is valid is not a strong validator.

## TTS policy

```text
controlled practice
    TTS allowed after QA

changed-context practice
    TTS or human

listening evidence
    source provenance preserved

robust transfer
    unseen natural/human speech required
```

## Conversation policy

Candidate progression:

```text
scripted / constrained AI
↓
adaptive AI
↓
less accommodating AI / engineered repair
↓
different voice/model/context
↓
human-like or human validation sample
```

AI practice volume is useful; it must not erase the final transfer target.

## Model drift

The tested object is:

```text
provider + model/version + prompt/version + rubric/version + configuration
```

not merely `GPT` or another model family name.

A version change creates a new measurement dependency. Before evidence authority resumes, rerun fixed regression slices for Vietnamese near-A0 writing errors, beginner construction feedback, pragmatic judgments, task constraint compliance, support leakage, conversation accommodation, TTS target forms and relevant safety/refusal behavior.

## Privacy boundary

Send only what a role needs. For one-sentence feedback, the model usually needs the target, learner sentence, construction and bounded rubric—not the full profile, entire learning history, account identity or unrelated raw speech archive.

Durable learner evidence and raw AI conversation should remain separable where feasible.

## Relationship to existing engines

`FEAT-AIG-001` is not a learning engine.

```text
Curriculum Engine
Learning Engines
Evidence Engine
        │
        ▼
   FEAT-AIG-001
 reliability gate
        │
 ┌──────┼──────┐
 LLM   TTS    AI partner
```

Existing domain engines retain ownership of learner-state meaning. `FEAT-ASR-001` owns ASR validity; `FEAT-WRI-001` writing progression; `FEAT-INT-001` interaction; `FEAT-LIS-001` listening diagnosis.

## Product decision

Build AI into Nếp as a replaceable mediation layer, not as curriculum brain or evidence truth source.

The product should remain functional when a model is unavailable, expensive, regressed, unsafe for a role, or removed from evidence authority.

## What RQ-020 does not establish

It does not establish a preferred commercial provider, universal confidence score, that two-model voting equals truth, that human judgment is infallible, exact TTS voice mix, exact privacy retention period, exact cost ceiling or exact escalation thresholds.

## Research-backed candidate

`FEAT-AIG-001 — AI mediation and reliability gate`

## Required experiment

`EXP-020 — role-gated AI mediation validity`

The experiment must compare learner outcomes and false-feedback/error rates, not merely AI benchmark scores.
