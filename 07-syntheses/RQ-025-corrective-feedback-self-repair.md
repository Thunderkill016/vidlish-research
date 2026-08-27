# RQ-025 — Corrective feedback and self-repair policy

**Status:** initial meta-foundation synthesis complete  
**Date:** 2026-08-27  
**Claims:** `CLM-CF-001`–`CLM-CF-019`  
**Evidence digest:** `06-evidence/RQ-025-source-digest.md`

## 1. Decision summary

Nếp should use **adaptive corrective feedback**, not one universal correction style.

The core rule is:

```text
independent attempt
↓
diagnose error + task consequence + learner repair readiness
↓
smallest useful feedback
↓
self-repair if feasible
↓
escalate if blocked
↓
record original attempt and supported repair separately
↓
later independent probe
```

This rejects both extremes:

```text
never correct errors
```

and:

```text
correct every error immediately with the full answer
```

## 2. Feedback is a treatment, not a truth label

The learner says or writes something.

The system then chooses an intervention.

These must remain separate:

```text
OBSERVATION
what learner did independently
```

```text
FEEDBACK
what the system did in response
```

```text
REPAIR
what learner could do after feedback
```

```text
LATER EVIDENCE
what learner can do again independently
```

If feedback supplies the answer, the subsequent correct response is supported practice.

It is not evidence that the answer was independently available before feedback.

This directly inherits RQ-024.

## 3. Feedback families and their jobs

Nếp should think in **information/retrieval demand**, not only classroom taxonomy labels.

### F0 — Acknowledge / no correction

Use when:
- response is acceptable for the current target;
- variation is communicatively valid;
- correcting a non-target difference would add noise.

### F1 — Minimal error signal / clarification prompt

Examples of function:
- indicate something is wrong or unclear;
- ask learner to try again;
- repeat/question the problematic segment without supplying the answer.

Purpose:
- test whether repair is already available;
- trigger retrieval/self-monitoring.

### F2 — Targeted cue / metalinguistic or semantic hint

Adds information but still withholds the full answer.

Purpose:
- narrow the search space;
- make form/meaning/function problem visible;
- support an achievable self-repair.

### F3 — Recast/model

Supplies a correct or improved form while preserving meaning/context.

Purpose:
- provide positive evidence/model;
- maintain conversational flow;
- help when self-repair is unlikely or too costly.

### F4 — Explicit correction/explanation

Clearly marks the error and may explain why/how.

Purpose:
- resolve ambiguity;
- establish declarative understanding where useful;
- address repeated or opaque form/function problems.

### F5 — Full supported reconstruction

Used when the learner cannot continue meaningfully with lower support.

Purpose:
- finish learning episode without unproductive repeated failure;
- rebuild response with high support;
- defer independent evidence to a later probe.

These are functional categories. Actual oral/written implementations can differ.

## 4. Self-repair is conditional, not ideological

Prompts show strong average results in classroom oral-CF research.

That supports a productive-learning idea:

```text
if knowledge is retrievable
→ make learner retrieve it
```

But a near-A0 learner may not possess the form needed to repair.

Repeated prompting can then become:

```text
fail
→ guess
→ fail
→ guess
→ frustration
```

Therefore:

```text
repair readiness
```

is a required decision variable.

Candidate logic:

```text
high repair readiness
→ F1/F2 first

uncertain repair readiness
→ one bounded F1/F2 attempt
→ then escalate

low repair readiness / novel target
→ F3/F4 sooner
```

Exact thresholds are not yet validated.

## 5. Recasts have a specific role

Recasts are especially plausible when:
- flow matters;
- correct model can be perceived easily;
- learner does not need a lengthy explicit explanation;
- the error can be reformulated naturally.

But recasts can be ambiguous.

Therefore Nếp should not assume:

```text
heard correct reformulation
→ noticed correction
```

A later check or slight salience cue may be needed when form learning matters.

## 6. Explicit feedback has a specific role

Explicit/metalinguistic feedback is plausible when:
- learner repeatedly fails to notice a low-salience contrast;
- L1 transfer creates a persistent wrong mapping;
- rule/concept is compact and useful;
- an explicit explanation can save large amounts of blind trial-and-error.

RQ-022 already rejected a false choice between explicit and implicit learning.

RQ-025 therefore rejects:

```text
explicit feedback = bad because unnatural
```

and:

```text
explain every mistake in grammar terminology
```

The test is whether explanation helps the target performance efficiently.

## 7. Timing policy

### Correct immediately when:
- misunderstanding blocks the task;
- error changes critical meaning;
- a current learning target benefits from immediate comparison;
- learner can immediately reuse the corrected knowledge.

### Consider delaying to a natural break when:
- interaction is meaning-focused;
- the error is low consequence;
- interruption would destroy fluency/communication;
- several small errors can be grouped into one useful reflection.

### Never infer:

```text
immediate always better
```

or:

```text
delayed always preserves fluency better
```

Timing is part of the feedback policy and must be tested by task type.

## 8. Error-priority policy

Nếp should not optimize **number of errors corrected**.

Candidate priority dimensions:

```text
1. communicative consequence
2. target-capability relevance
3. recurrence/persistence
4. learner readiness to benefit
5. transfer/prerequisite value
6. correction cost / interruption cost
```

### High priority
- changes intended meaning;
- prevents task completion;
- causes interlocutor misunderstanding;
- is the current form/function target;
- recurs despite prior feedback;
- blocks a high-value prerequisite.

### Lower priority in the current moment
- harmless non-target variation;
- accent difference with no intelligibility impact;
- stylistic preference represented as a rule;
- minor grammar issue during a task whose main goal is different.

This connects directly to RQ-007 intelligibility-first pronunciation and RQ-023 target tasks.

## 9. Written feedback policy

Written feedback gives more processing time than live interaction.

Nếp can exploit this without turning every writing attempt into a red-marked page.

Candidate sequence:

```text
independent text
↓
identify current high-value issue(s)
↓
if self-edit feasible → indirect/coded cue
if not → direct/model + brief explanation
↓
learner revision
↓
new writing task later
```

The new writing task matters because:

```text
fixing the marked sentence
≠
using the form accurately in new writing
```

## 10. Content versus form feedback

A learner can produce grammatically correct language that fails the task.

So feedback should distinguish:

```text
meaning/task fulfillment
organization/discourse
pragmatics
lexis
morphosyntax
pronunciation/intelligibility
interaction/repair
```

The target capability determines which layer has priority.

For example:

```text
Task: ask customer to confirm delivery time
```

A minor article error may matter less than:
- wrong time;
- overly ambiguous request;
- missing confirmation move.

## 11. Feedback engagement

A displayed correction is not processed feedback.

For important targets, Nếp should create one small learner action after feedback where appropriate:

- retry;
- choose why meaning changed;
- reconstruct the form;
- compare versions;
- use it in a new micro-context.

Do not require an elaborate reflection after every error.

The goal is enough processing to make feedback educationally meaningful.

## 12. AI feedback contract

Automated feedback is allowed only under the RQ-024 evidence/validity contract.

The system must distinguish:

### Low-stakes coaching
Example:
- optional paraphrase suggestion;
- explanation offered as a learning aid.

A moderate uncertainty may be tolerable if clearly framed.

### Capability-affecting correction
Example:
- “your pronunciation was wrong”;
- “this interaction failed pragmatically”;
- downgrade learner state;
- schedule remediation.

This requires stronger model/task/population validation.

Store where relevant:

```text
provider
model
version
rubric/prompt version
feedback confidence
error category
```

## 13. Candidate adaptive feedback controller

Research abstraction only:

```text
ATTEMPT
↓
classify current target + error consequence
↓
estimate repair readiness
↓
choose information level F0–F5
↓
REPAIR ATTEMPT
↓
if productive struggle → continue
if unproductive struggle → escalate
↓
finish meaning-focused task
↓
later independent probe
```

The controller must not confuse:

```text
more struggle
→ more learning
```

Desirable difficulty has a boundary: repeated unrecoverable failure is not a learning virtue.

## 14. Evidence semantics after feedback

Example event history:

```text
A1 independent speaking attempt: incorrect
F1 prompt: “Try the time again.”
A2 self-repair: correct
```

Store:

```text
independent attempt = failed
self-repair-after-minimal-prompt = succeeded
```

Do not store:

```text
mastered = true
```

Later:

```text
new changed-context speaking probe: correct without prompt
```

can support stronger independent/generalization evidence.

## 15. What remains unresolved

RQ-025 does not specify:
- exact F0–F5 thresholds;
- repair-readiness estimator;
- number of repair attempts;
- whether some feedback types should be skipped by proficiency;
- exact timing windows;
- target-error priority weights;
- feedback density per interaction;
- direct/indirect writing policy by learner state;
- ideal metalinguistic explanation length;
- learner preference/affect adaptation;
- AI confidence arbitration.

Those remain `EXP-025` and RQ-026 questions.

## 16. Strong rejection rules

Nếp Method should reject:

```text
all errors must be corrected
```

```text
never interrupt communication to correct
```

```text
recast is always best because it is implicit
```

```text
prompts are always best because self-repair is deeper
```

```text
explicit explanation is always inefficient
```

```text
corrected output immediately after feedback = acquired
```

```text
AI generated correction = verified learner error
```

The supported rule is conditional feedback matched to target, task, learner readiness and downstream evidence.
