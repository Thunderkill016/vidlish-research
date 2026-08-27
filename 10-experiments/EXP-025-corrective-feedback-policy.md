# EXP-025 — Corrective-feedback and self-repair policy validation

**Status:** planned validation study  
**Depends on:** RQ-025, RQ-024  
**Purpose:** determine which feedback escalation policies improve later independent performance efficiently for Vietnamese-speaking learners near Pre-A1/A1.

## 1. Primary question

For common Nếp task families, when should the system prompt self-repair, provide a cue, recast/model, explain explicitly, delay correction, or leave a non-target error alone?

## 2. Do not test one universal feedback tournament

The experiment should stratify by:

- construct: lexis / morphosyntax / pronunciation / writing / interaction-pragmatics;
- learner evidence level;
- whether the target is new or previously learned;
- error consequence for task meaning;
- response modality;
- communicative versus language-focused task goal.

## 3. Candidate oral/productive conditions

### A — Full model immediately

```text
error
→ correct model
→ repeat/retry
```

### B — Minimal prompt first

```text
error
→ minimal signal
→ self-repair attempt
→ model if blocked
```

### C — Graduated adaptive feedback

```text
error
→ choose F1/F2/F3/F4 from repair readiness + consequence
→ bounded repair
→ escalate only when needed
```

### D — Delayed batch feedback

Meaning-focused task continues unless error blocks communication; selected errors are addressed after the task.

## 4. Candidate writing conditions

Compare where sample size permits:

- direct correction;
- indirect/coded feedback with self-edit;
- graduated indirect → direct escalation;
- focused current-target feedback;
- broader high-consequence feedback.

Do not use grammatical accuracy as the only outcome if task fulfillment or discourse quality is part of the target capability.

## 5. Primary criterion

Later **independent performance on new parallel/changed-context tasks**.

Measure separately:
- accuracy or communicative success;
- retention after delay;
- transfer to a changed task;
- learner time.

Candidate efficiency metric:

```text
delayed changed-context capability gain
──────────────────────────────────────
learning + feedback minutes
```

## 6. Repair-process measures

Record:

```text
initial_error_type
feedback_level
repair_attempt_count
self_repair_success
model_required
latency_to_repair
same-session_reuse
```

These are process variables, not final acquisition outcomes.

## 7. Feedback-timing measures

For communicative tasks compare:

- immediate interruption;
- natural-break correction;
- post-task feedback.

Measure:
- target accuracy;
- task completion;
- fluency/interaction continuity;
- later independent target use;
- perceived interruption/effort.

## 8. Error-priority validation

Candidate priority model:

```text
priority = f(
  communicative consequence,
  current target relevance,
  recurrence,
  learner repair readiness,
  prerequisite/transfer value,
  interruption cost
)
```

Compare against simpler baselines:
- correct every detectable error;
- correct only current target;
- fixed top-N errors.

## 9. Beginner-specific analysis

Test whether very low-evidence learners benefit from earlier modeling/explicit help relative to repeated prompting.

Important failure signal:

```text
prompt
→ repeated guessing
→ escalating time/frustration
→ no later gain
```

If observed, reduce prompt depth for that learner/construct state.

## 10. Automated-feedback validity

For AI/ASR-generated feedback:

- retain model/provider/version;
- sample outputs for human/domain review;
- estimate false-correction and missed-error rates;
- analyze communicatively acceptable variants wrongly rejected;
- separate explanation quality from scoring validity;
- test whether wrong automated feedback causes later learner error.

A system that produces polished explanations but misidentifies errors must not control learner-state updates.

## 11. Learner engagement/affect

Collect lightweight measures:
- whether feedback was understood;
- whether learner attempted repair;
- repeated dismissal/skip;
- frustration/effort where practical.

RQ-026 will determine how much affect/individual-difference adaptation is justified.

## 12. Decision rule

A feedback policy should not ship globally because it maximizes immediate corrected responses.

Prefer policies that improve:

```text
later independent performance
+
retention/transfer where relevant
+
learning efficiency
```

without unacceptable:
- interaction fragmentation;
- repeated unproductive failure;
- false automated corrections;
- learner abandonment.

## 13. Falsification

Reject the adaptive escalation policy if a simpler policy performs equally or better on delayed changed-context outcomes per learner minute.

Reject self-repair-first for any learner/construct state where it reliably adds failure/friction without later benefit.

Reject immediate interruption for task classes where delayed/natural-break feedback preserves communication and yields equal or better later learning.
