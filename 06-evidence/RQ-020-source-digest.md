# RQ-020 source digest — AI mediation, TTS and reliability

**Evidence ID:** `EVD-RQ-020`  
**Question:** How should Nếp use LLMs, AI feedback, conversation agents and TTS without turning model output into false learning evidence?

## Scope

This pass retained 14 sources spanning five workstreams:

1. L2 chatbot / GenAI learning effects;
2. AI feedback and automated assessment validity;
3. human-versus-chatbot interaction;
4. synthetic speech / TTS;
5. privacy, governance and model drift.

The evidence is strongest for writing, higher-education EFL settings and controlled chatbot interventions. It is much thinner for Vietnamese near-A0 adults, natural listening transfer and open-ended automated assessment.

## Retained evidence

| Source | Population / method | High-signal result | Product limitation |
| --- | --- | --- | --- |
| `SRC-0209` | 31 comparative L2 chatbot studies, 41 effects | medium positive average chatbot effect; important moderators | average effect does not validate a specific AI role |
| `SRC-0210` | 41 GenAI-SLA experiments/quasi-experiments, 3,515 participants | moderate-to-large positive average effect; moderator differences | new, heterogeneous evidence base |
| `SRC-0211` | 49 empirical GenAI language-classroom studies | roles include tutor, feedback, generator and partner; quality/overreliance issues recur | higher education and self-report dominate |
| `SRC-0212` | 144 empirical GenAI language studies from 2023–2024 | 86.7% higher education, 86.1% EFL; writing dominates | limited longitudinal and low-level evidence |
| `SRC-0213` | systematic review of 83 AI written-feedback papers / 85 studies | validation findings are less consistently positive than use/effect findings | writing-specific; many pre-frontier-LLM systems |
| `SRC-0214` | 119 ELL essays, four LLMs, repeated scoring | some LLMs show useful validity/reliability but scoring fluctuates by model/time | essay scoring is not the whole learner model |
| `SRC-0215` | 35 upper-intermediate L2 essays, ChatGPT-4 feedback analysis | many flagged problems accurate/relevant; specificity and classifications vary | precision among flags does not prove coverage |
| `SRC-0216` | 4,315 essays, psychometric human/LLM comparison | LLMs can help fine-grained/ranking tasks; less reliable for some absolute judgments | large-scale writing context, not beginner multimodal assessment |
| `SRC-0217` | 11 human-chatbot comparison experiments | some linguistic outcomes comparable; humans stronger on some interactive/social dimensions | small and fast-changing evidence base |
| `SRC-0218` | 29 EFL learners, TTS versus human speech | similar comprehension/intelligibility on several tasks; TTS less natural in some conditions | one TTS/population |
| `SRC-0219` | 653 L2 test takers, 13 matched listening items | synthetic and human versions elicited remarkably comparable item performance | constrained multiple-choice assessment domain |
| `SRC-0220` | 26 native + 31 non-native listeners across speech types/noise | synthetic speech could be least intelligible / more effortful; speech type matters | not a classroom training study |
| `SRC-0221` | longitudinal comparison of GPT service snapshots | model behavior/performance can drift substantially over short intervals | historical model family; causes of drift opaque |
| `SRC-0222` | systematic review of 53 GenAI-education papers | privacy, bias, autonomy, transparency and accountability are recurring governance risks | broad education context, not Nếp-specific controls |

## Convergence

### 1. AI effectiveness is real enough to use, not strong enough to trust blindly

The chatbot meta-analyses support using AI to expand practice and feedback opportunities. They do **not** justify:

```text
AI feature present
→ learning is better
```

The outcome depends on role, implementation, modality, comparison condition and learner context.

### 2. “AI” is not one measurement instrument

The same model can act as:

```text
generator
tutor
feedback provider
evaluator
conversation partner
TTS source
```

Each role creates a different validity claim. A model that is useful as a conversation partner is not automatically valid as a rater.

### 3. Assessment is the dangerous boundary

The writing-assessment literature shows that LLMs can be useful raters under constrained rubrics, but reliability differs by model, prompt, criterion and time.

For Nếp:

```text
AI says learner is wrong
≠
learner demonstrated an error
```

and:

```text
AI score = 82
≠
mastery = 82%
```

### 4. TTS is usable input, not natural-speech equivalence

Modern synthetic speech can work well in controlled EFL tasks and can scale audio production. But other evidence shows speech type changes intelligibility and effort.

Therefore:

```text
TTS success
→ evidence under synthetic-audio condition
```

not:

```text
TTS success
→ robust natural listening
```

### 5. Provider output is a moving dependency

A prompt-model pair validated today can regress after a provider/model update. AI-assisted evidence therefore needs provenance and regression testing just like production software.

### 6. Data governance is part of pedagogy

If personalization requires sending raw learner speech, writing, history or profile to third parties, privacy and accountability become part of feature validity. More personalization is not automatically better if it increases avoidable learner-data exposure.

## What is rejected

- “The newest model can safely grade everything.” — rejected.
- “Human-level correlation means mastery scoring is valid.” — rejected.
- “If AI feedback is usually correct, it must find every important error.” — rejected.
- “A fluent chatbot conversation proves human conversation capability.” — rejected.
- “Modern TTS is basically the same as natural speech.” — rejected.
- “A prompt validated once remains valid after model updates.” — rejected.
- “AI-generated lesson content can bypass curriculum constraints because the model is smart.” — rejected.
- “More learner data sent to the model is automatically better personalization.” — rejected.

## Evidence gap that matters most

The literature does not establish which AI roles are reliable enough for Vietnamese-speaking near-A0/A1 adults doing short mobile tasks.

`RQ-020` can therefore define a **role-specific reliability architecture**, but exact authority thresholds belong to `EXP-020`.
