---
id: SYN-WRI-001
title: Writing progression from supported production to independent meaningful transfer
status: initial-synthesis
research_question: RQ-014
last_verified: 2026-08-26
---

# RQ-014 — Writing progression for near-A0 learners

## Decision summary

Nếp should not treat a polished final draft as evidence that a learner can write. Beginner writing must be modeled as a progression from **retrieving language for a communicative purpose** to **organizing a short message**, **using feedback to self-repair**, and finally **writing new content independently after support has disappeared**.

Core rule:

```text
learner writes first
→ capture independent evidence
→ smallest useful feedback
→ learner revises
→ optional comparator/model
→ support disappears
→ learner writes NEW content
→ delayed new-task writing
```

The system must preserve four different outcomes:

```text
draft_quality
revision_quality
new_task_transfer
delayed_new_task_retention
```

A high-quality text produced after AI rewriting, a model sentence, translation, or direct correction is useful practice evidence, but it is not independent-writing mastery.

## Writing is not one score

Writing combines multiple processes and products. Planning research shows that changing planning conditions can affect fluency, accuracy and complexity differently rather than uniformly improving one global writing ability (`SRC-0144`, `SRC-0145`).

For near-A0 Nếp should separate at least:

```text
communicative_intent
idea_selection
lexical_retrieval
construction_retrieval
sentence_formation
message_organization
linguistic_accuracy
writing_fluency
monitoring
revision
new_task_transfer
```

This avoids two false conclusions:

```text
final draft has no errors
→ learner can write independently
```

and:

```text
learner wrote many words quickly
→ learner communicated successfully
```

## Candidate progression

The writing curriculum should grow the amount of meaning the learner must generate while gradually reducing language support.

### Stage W0 — bounded reconstruction

Examples:

```text
I / coffee / want
→ I want coffee.
```

or selecting/reordering a known chunk.

Purpose:
- establish written form and construction order;
- connect already-understood language to production;
- reduce initial typing/spelling load.

This is support-heavy practice and must not be counted as independent production.

### Stage W1 — guided sentence production

Example:

```text
Situation: You want water.
Prompt: I want ____.
```

The learner supplies a meaningful slot or target construction with partial support.

Evidence:
- can retrieve a needed lexical item;
- can complete a known construction;
- support level is explicit.

### Stage W2 — changed-content sentence production

Example:

```text
You are at a café. Ask for tea.
[blank response]
```

No full target sentence is visible. Optional hint levels may reveal only what is needed.

This begins to test whether the learner can transfer a construction rather than copy it.

### Stage W3 — connected micro-writing

Examples:

```text
Introduce yourself in 2–3 short sentences.
Tell a friend what you want to eat and drink.
Write a short message saying where you are and when you will arrive.
```

Targets:
- connect two or more propositions;
- maintain a simple referent/topic;
- select known vocabulary/constructions without a full model;
- organize the message enough for its purpose.

### Stage W4 — repeated genre, new content

Keep the functional genre stable while changing the content:

```text
message 1: ask a friend to meet
message 2: tell a coworker you are late
message 3: confirm a delivery time
```

Reusing the communicative structure reduces genre novelty while forcing new retrieval. The product should compare improvement across **new instances**, not merely repeated drafts of one text.

### Stage W5 — short independent functional writing

As evidence grows, introduce less scaffolded practical writing:
- short personal messages;
- requests;
- confirmations;
- descriptions;
- simple narratives;
- short responses to everyday/work situations.

Authentic communicative purpose matters more than essay length. Near-A0 learners do not need academic paragraphs to prove that writing is real.

## Planning should be available but bounded

Planning is a genuine writing process, but systematic reviews do not support a simplistic rule that more pre-task planning always produces better overall writing (`SRC-0144`, `SRC-0145`).

Candidate beginner planning:

```text
What do I need to say?
Who is it for?
2–3 ideas / known chunks
```

Possible UI:

```text
GOAL: tell Mai you will arrive at 7
IDEAS:
- late
- arrive 7
- sorry
```

Then hide or collapse planning support during the independent probe.

Store:

```text
planning_ms
planning_support_level
planner_items_used
```

Do not score a planning template as writing ability.

## Feedback must improve the next act of writing

Written corrective feedback has evidence for improving L2 grammatical accuracy, including delayed effects, but results are moderated and no single feedback type is universally superior (`SRC-0146`, `SRC-0147`).

Therefore Nếp should not implement:

```text
find every error
→ replace every error
→ show perfect paragraph
```

The educational question is:

> What is the smallest intervention that helps this learner express the intended message more accurately now and retrieve/use the same knowledge later?

Candidate feedback priority for near A0:

```text
1. Is the intended message understandable?
2. Is a required word/chunk/construction missing?
3. Can the learner self-repair with a cue?
4. If not, provide bounded positive evidence / direct model.
5. Address high-value recurrent errors before low-value surface noise.
6. Require a new writing task after feedback.
```

## Self-repair before correction when knowledge is likely available

If learner history suggests the target form is already retrievable, first use a bounded prompt:

```text
You wrote: "I want coffee yesterday."
Hint: Which time form do you need for yesterday?
```

If the learner does not have the form or the prompt produces repeated guessing, provide positive evidence instead of withholding the answer indefinitely.

The exact prompt/direct-feedback policy remains experimental because WCF research does not identify one universal best feedback type (`SRC-0146`, `SRC-0147`).

## Feedback scope should be selective

Correcting everything can overwhelm a beginner and obscures what should be learned next. The writing engine should prioritize errors by:

```text
message blocking
→ target construction / current curriculum
→ high-frequency recurring error
→ intelligibility / ambiguity risk
→ lower-priority mechanics
```

This does not mean spelling/punctuation never matter. It means surface correctness should not crowd out communicative development.

Store all ignored and selected error candidates if machine feedback is used, so the policy can later be audited.

## Revision is useful evidence, but not transfer

Peer-feedback meta-analysis found larger effects on revisions than on new compositions (`SRC-0148`). Automated-feedback research also explicitly distinguishes current-text performance from learning/transfer (`SRC-0149`).

Thus:

```text
Draft 1
→ feedback
→ Draft 2 improves
```

establishes that the learner can use some support to improve a text.

It does **not** establish:

```text
learner can independently write a different message later
```

Nếp must preserve both measurements.

## Model texts: compare after ownership exists

Model texts can provide positive evidence across lexis, grammar, content and organization, and some studies show later benefits (`SRC-0153`, `SRC-0154`). But giving the ideal answer before the learner writes can turn the task into imitation.

Preferred sequence:

```text
learner first draft
→ record problems / uncertainty
→ show 1–2 short comparator examples
→ learner notices useful differences
→ model disappears
→ revise or write a new task
```

Models are **comparators**, not answer keys.

Near A0, a comparator might be one or two sentences rather than an essay.

## AI/AWE: feedback tool, not ghostwriter

Automated-writing feedback has positive average effects but substantial heterogeneity (`SRC-0149`, `SRC-0150`), and a 2026 meta-synthesis concludes that automated systems are more defensible as adjuncts than replacements, with stronger evidence for surface-level support than higher-order writing (`SRC-0155`).

Nếp must distinguish at least:

```text
AI diagnoses an issue
AI gives a hint
AI gives bounded alternatives
AI supplies a corrected form
AI rewrites the sentence
AI rewrites the whole message
```

The last two dramatically change evidence quality.

Hard rule:

```text
if full rewrite / ideal answer was visible before evidence capture,
that text cannot count as independent writing evidence.
```

If the learner accepts an AI rewrite without reconstructing or using the language later, Nếp has evidence of tool use, not language mastery.

## AI feedback needs confidence and scope gates

Machine-generated feedback can be wrong, overbroad or stylistically unnecessary. For near-A0 learners, false correction is especially harmful because the learner may not have enough English to challenge it.

Candidate gate:

```text
machine detects candidate issue
→ confidence / rule / target relevance check
→ if high-value and high-confidence: feedback
→ if uncertain: do not present as fact
→ log candidate and outcome
```

Never show a fake holistic score like:

```text
Writing: 87/100
```

unless the underlying scoring model has been validated for the task/population and the score has an interpretable construct.

## Self-regulation belongs in the writing engine

Longitudinal EFL studies indicate that instruction targeting self-regulated writing processes can improve writing performance and strategy use (`SRC-0151`, `SRC-0152`).

Nếp should teach a small recursive cycle instead of a long strategy lecture:

```text
GOAL
→ PLAN
→ WRITE
→ CHECK MESSAGE
→ CHECK ONE TARGET
→ REVISE
→ WRITE AGAIN LATER
```

For near A0, each step should be lightweight. The point is to create a reusable writing behavior, not to teach metacognitive terminology.

## Measure message success separately from form accuracy

A beginner can write a useful but inaccurate message:

```text
I late. arrive 7.
```

The communicative content may be recoverable even though construction accuracy is weak.

Another learner can produce a grammatically correct copied sentence that does not answer the situation.

Therefore evidence should separate:

```text
message_fulfilled
required_meaning_coverage
lexical_retrieval
construction_use
organization
accuracy
mechanics
fluency
support_provenance
```

Do not collapse these into one mastery number prematurely.

## Writing fluency is task-dependent

Writing time and amount produced are useful process observations, but faster typing can reflect keyboard skill, copying, shorter content or less monitoring. Likewise longer text is not automatically better.

Record:

```text
planning_ms
first_token_ms
writing_ms
revision_ms
characters_or_words
pauses if technically reliable
```

Interpret them only with message fulfillment and language evidence.

## Support provenance

Every writing attempt should record whether the learner saw:

```text
sentence frame
word bank
Vietnamese planning prompt
translation
model text
error location cue
metalinguistic hint
direct correction
AI suggestion
AI rewrite
```

Then evidence can distinguish:

```text
independent production
prompted production
model-assisted revision
AI-assisted revision
```

## New-task transfer is the central writing outcome

After feedback on one task, ask for a new message that requires some of the same language but changes content/context.

Example:

```text
Task A:
Tell a café worker you want tea.

feedback / repair

Task B:
Message a friend saying what food you want.
```

The learner cannot simply copy the previous answer, but the construction can transfer.

For broader writing development, later probes should change both content and some discourse demands while staying within the learner's readiness.

## Delayed writing matters

A revised text immediately after feedback may reflect short-term availability. `SRC-0146`, `SRC-0147`, `SRC-0151` and related work justify preserving delayed outcomes.

Candidate evidence ladder:

```text
same-draft revision
→ immediate new-task transfer
→ delayed new-task transfer
→ later functional use
```

No universal delay or mastery threshold is established; `EXP-014` must calibrate it.

## Proposed data model

```ts
type WritingAttempt = {
  taskId: string;
  taskStage: "reconstruction" | "guided-sentence" | "independent-sentence" | "microtext" | "functional";
  contextId: string;
  firstSeen: boolean;

  sentenceFrameVisible: boolean;
  wordBankVisible: boolean;
  modelVisible: boolean;
  translationVisible: boolean;
  aiRewriteVisible: boolean;
  hintLevel: number;

  planningMs: number;
  writingMs: number;
  revisionMs: number;

  messageFulfilled?: boolean;
  requiredMeaningCoverage?: number;
  lexicalRetrievalEvidence?: number;
  constructionUseEvidence?: number;
  organizationEvidence?: number;
  accuracyEvidence?: number;

  feedbackTypes: string[];
  editsAfterFeedback?: number;
};
```

Derived learner state should remain cautious and should not simply average these fields.

## Product integration

Writing should reuse the rest of Nếp:

```text
Curriculum / scenario
        ↓
Vocabulary + Construction readiness
        ↓
Writing task
        ↓
independent evidence capture
        ↓
Feedback / Scaffold Engine
        ↓
revision evidence
        ↓
Transfer Engine: new task
        ↓
Review Engine: delayed writing
```

A writing error can generate a later review candidate, but not every typo should automatically become a flashcard or grammar lesson.

## Product decision

Create `FEAT-WRI-001` — **Adaptive writing progression engine**.

It should increase communicative and generative demand gradually, capture the learner's own draft before strong support appears, deliver bounded feedback, and require new-task/delayed writing before treating corrected performance as independently usable knowledge.

## Open assumptions

- exact transition from reconstruction to independent sentence production;
- exact sentence-frame and word-bank fading thresholds;
- optimal micro-writing length for Vietnamese near-A0 adults;
- whether Vietnamese support is most useful in planning, feedback explanation, or both;
- how feedback priority should vary by stage;
- when to prompt self-repair versus provide direct positive evidence;
- how many feedback targets to show per draft;
- when model/comparator text should appear;
- optimal number of revision cycles before switching to a new task;
- how much AWE/AI feedback is beneficial without inducing dependence;
- confidence thresholds for automated feedback;
- safe scoring dimensions for very short beginner texts;
- typing/spelling/mechanics policy for mobile learners;
- order of practical genres;
- delayed interval and transfer novelty needed for writing mastery evidence.
