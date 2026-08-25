---
id: FEAT-WRI-001
title: Adaptive writing progression engine
status: research-backed-candidate
research_question: RQ-014
synthesis: SYN-WRI-001
experiment: EXP-014
---

# FEAT-WRI-001 — Adaptive writing progression engine

## Learner problem

Near-A0 learners often face one of two bad writing experiences:

```text
too much support
→ copy / translate / accept AI rewrite
→ polished output
→ little evidence of independent ability
```

or:

```text
blank page too early
→ cannot retrieve enough language
→ guessing / avoidance / translation dependence
```

Nếp needs a middle path that grows independent written production without pretending that corrected or generated text belongs to the learner's language system.

## Target capability

The learner can independently write a short, useful English message for a familiar purpose, using previously learned vocabulary and constructions, and can reuse that language in changed content after feedback and after delay.

## Research basis

Primary principles:

- `PRN-165`–`PRN-180`
- `SYN-WRI-001`

Key evidence themes:
- planning changes writing dimensions differently (`SRC-0144`, `SRC-0145`);
- written corrective feedback can improve accuracy but is moderated (`SRC-0146`, `SRC-0147`);
- revision gains can exceed new-composition gains (`SRC-0148`);
- automated feedback has positive but heterogeneous effects (`SRC-0149`, `SRC-0150`, `SRC-0155`);
- self-regulated writing instruction can support later performance (`SRC-0151`, `SRC-0152`);
- post-draft model texts can provide useful positive evidence (`SRC-0153`, `SRC-0154`).

## Non-goals

This feature is not:
- a grammar checker;
- an AI ghostwriter;
- an essay generator;
- a translation box;
- a single holistic writing score;
- a permanent sentence-frame system;
- a requirement to correct every error.

## Core learner loop

```text
COMMUNICATIVE GOAL
        ↓
optional bounded PLAN
        ↓
WRITE with current support level
        ↓
CAPTURE independent / support provenance
        ↓
CHECK message success
        ↓
smallest useful FEEDBACK
        ↓
learner SELF-REPAIRS / REVISES
        ↓
optional COMPARATOR / positive evidence
        ↓
support disappears
        ↓
NEW-CONTENT WRITE
        ↓
DELAYED NEW-TASK WRITE
```

## Writing stages

### W0 — reconstruction

UI may provide:
- ordering;
- matching;
- constrained construction assembly.

Evidence label:
`supported_reconstruction`

Never infer independent writing from W0 alone.

### W1 — guided sentence

UI may provide:
- partial sentence frame;
- small word bank;
- bounded Vietnamese situation description.

Candidate unlock signal:
learner repeatedly retrieves target slots/construction with low support.

### W2 — independent changed-content sentence

UI:
- situation/purpose;
- empty response field;
- hints hidden initially.

Evidence:
`independent_sentence_transfer` if no strong support was opened before submission.

### W3 — connected micro-writing

Target:
2–4 propositions depending on learner state, not a fixed universal sentence count.

Examples:
- self-introduction;
- simple request + reason/time;
- short status/update message;
- basic description.

### W4 — repeated functional genre, new content

Keep discourse purpose somewhat stable while varying people, objects, times, places and intent details.

Goal:
reduce genre novelty while increasing lexical/construction retrieval and organization.

### W5 — short independent functional writing

Less constrained real-life/work contexts with sparse support.

## Task specification

```ts
type WritingTaskSpec = {
  id: string;
  stage: "reconstruction" | "guided-sentence" | "independent-sentence" | "microtext" | "functional";
  communicativeGoal: string;
  audience?: string;
  scenario: string;

  requiredMeanings: string[];
  targetVocabularyIds: string[];
  targetConstructionIds: string[];
  prerequisiteIds: string[];

  allowedSupport: {
    sentenceFrame: boolean;
    wordBank: boolean;
    vietnamesePlanning: boolean;
    translation: boolean;
    comparator: boolean;
    aiFeedback: boolean;
  };

  transferFamilyId: string;
  noveltyLevel: number;
};
```

## Attempt evidence

```ts
type WritingAttemptEvidence = {
  attemptId: string;
  taskId: string;
  userId: string;

  firstSeen: boolean;
  submittedText: string;

  sentenceFrameVisible: boolean;
  wordBankVisible: boolean;
  translationVisible: boolean;
  modelVisible: boolean;
  aiRewriteVisible: boolean;
  hintLevel: number;

  planningMs: number;
  writingMs: number;
  revisionMs: number;

  messageFulfilled?: boolean;
  meaningCoverage?: number;
  lexicalEvidence?: number;
  constructionEvidence?: number;
  organizationEvidence?: number;
  accuracyEvidence?: number;
  mechanicsEvidence?: number;

  feedbackEvents: FeedbackEvent[];
  occurredAt: string;
};
```

Do not store only the final text. The event/provenance trail determines what the text can validly evidence.

## Support provenance classes

Candidate ordered classes:

```text
P0 independent
P1 planning-only support
P2 lexical/word-bank hint
P3 sentence-frame or targeted construction hint
P4 direct correction / comparator visible
P5 AI sentence rewrite visible
P6 AI full-message rewrite visible
```

Higher number does not mean worse learning. It means the resulting output is weaker evidence of independent production.

Any attempt with `P5/P6` cannot upgrade independent-writing mastery directly.

## Feedback engine

### Step 1 — meaning first

Check whether the learner fulfilled the communicative goal.

Example:

```text
Goal: tell An you will arrive at 7.
Learner: "I late. 7 arrive."
```

Message may be partly recoverable even though form accuracy is poor.

Return separate evidence:
- meaning communicated;
- target construction unavailable/unstable;
- ordering/grammar issue.

### Step 2 — choose at most a bounded feedback set

Candidate ranking:

```text
message-blocking issue
current target construction
high-frequency recurrent issue
ambiguity-producing issue
mechanics / style
```

Exact maximum feedback count is an experiment parameter.

### Step 3 — choose feedback strength

```text
learner likely knows form
→ retrieval/self-repair cue

learner has weak/absent evidence
→ bounded direct model / positive evidence

machine uncertain
→ do not assert correction as fact
```

### Step 4 — learner acts

Feedback should normally require:
- edit;
- reconstruct;
- choose between meaningful alternatives;
- explain/confirm intended meaning when ambiguity matters.

Passive “Got it” is weak learning evidence.

## Comparator model behavior

Comparator is hidden until after learner ownership exists.

Allowed flow:

```text
Draft 1 saved
→ learner identifies uncertainty / receives targeted prompt
→ show one or two compact alternatives/models
→ ask learner to notice useful difference
→ hide model
→ learner revises OR completes new-content task
```

Do not expose a full ideal answer at task start for an independent-writing probe.

## AI behavior contract

AI may:
- identify a likely communication problem;
- classify a candidate error;
- ask a clarification question;
- offer a small hint;
- provide bounded examples after evidence capture;
- generate candidate transfer tasks;
- summarize recurring learner problems for the curriculum engine.

AI must not, before independent evidence capture:
- write the target sentence for the learner;
- translate the learner's Vietnamese into finished English;
- rewrite the whole response;
- silently autocomplete enough of the answer to remove retrieval demand.

When AI supplies wording, log:

```text
feedback_source = ai
feedback_scope
shown_text
confidence
accepted_or_rejected
learner_edit_after
```

## Machine-feedback confidence gate

Candidate:

```ts
if (confidence < validatedThreshold) {
  doNotPresentAsCertainCorrection();
}
```

Threshold must be calibrated by target type, not globally guessed.

High-risk categories may be routed to:
- non-judgmental clarification;
- model comparison;
- no automated feedback;
- later human-reviewed research set.

## Revision vs transfer

Persist separate attempt relationships:

```text
original_attempt_id
revision_of_attempt_id
transfer_from_task_id
delayed_probe_for_target_ids
```

Progress view should not merge these.

Example learner state:

```text
Request construction

independent sentence: ✓
revision after cue: ✓
changed-content writing: △
delayed changed-content writing: pending
```

## Writing learner state

Avoid:

```ts
writingLevel = 78;
```

Prefer evidence by capability:

```ts
type WritingCapabilityState = {
  capabilityId: string;
  independentEvidence: EvidenceSummary;
  guidedEvidence: EvidenceSummary;
  revisionEvidence: EvidenceSummary;
  transferEvidence: EvidenceSummary;
  retainedEvidence: EvidenceSummary;
  lastSupportClass: string;
};
```

## Task selection

Candidate selector:

```text
learner has target meaning + vocabulary + construction prerequisites
        ↓
choose shortest useful generative task above current evidence
        ↓
if blank-page failure likely, allow bounded lower-level support
        ↓
if guided success stable, reduce support / change content
        ↓
if transfer succeeds, schedule delayed new-task probe
```

Do not unlock based only on completion count.

## Review integration

Writing review should not mean rewriting the same sentence forever.

Possible review types:
- retrieve one target sentence in new situation;
- repair a recurring construction error;
- write two connected propositions;
- reuse a known chunk in a different functional message.

Scheduler state remains separate from capability state.

## Progress integration

Show human-readable capabilities, for example:

```text
Writing

Can write a simple request with known items
✓ independently in 3 contexts

Can write a short arrival/update message
△ succeeds after a hint

Can connect 3 short ideas in a message
○ not enough evidence
```

Do not display AI-assisted polished drafts as independent achievements.

## Safety / trust constraints

- Never pretend automated writing feedback is certainly correct when confidence is unknown.
- Do not shame learner errors.
- Preserve original learner text for comparison/audit when permitted by privacy policy.
- Make it clear when wording came from the learner versus the system.
- Avoid excessive correction that replaces communication with proofreading.

## Learning metrics

Primary:

```text
delayed independent new-task writing performance
```

Dimensions:
- message fulfillment;
- required meaning coverage;
- lexical retrieval;
- target construction use;
- organization appropriate to stage;
- linguistic accuracy;
- support dependence.

Secondary:
- revision uptake;
- time to usable message;
- recurring-error reduction;
- voluntary writing continuation.

## Engagement metrics

Keep separate:
- task completion;
- revision completion;
- hint opens;
- AI feedback opens;
- session return;
- writing abandonment.

These may explain UX but do not establish learning.

## Falsification

`FEAT-WRI-001` should be weakened or redesigned if:
- guided writing improves only when frames/models remain visible;
- corrected drafts improve but new independent tasks do not;
- AI feedback increases final-draft quality while delayed unaided writing stagnates or worsens;
- support fading causes persistent failure without later adaptation;
- learner time/effort rises substantially without better delayed transfer;
- automated feedback produces unacceptable false-correction rates.

## Experiment

See `EXP-014`.
