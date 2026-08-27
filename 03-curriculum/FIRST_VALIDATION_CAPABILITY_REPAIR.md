# First Validation Capability — Initiate Repair After Global Non-Understanding

**Status:** owner-first validation capability; provisional  
**Parent:** `NEP_CURRICULUM_CONTRACT_V0.md`  
**Needs basis:** `V1_OWNER_TARGET_NEEDS.md`  
**Research basis:** `CLM-INT-005`, `CLM-INT-006`, `CLM-INT-017`, `CLM-SPK-002`, `CLM-VAL-008`, `CLM-TRN-001`, `CLM-REV-001`

---

## 1. Capability statement

> When a short spoken message is not understood, the learner can recognize the communication breakdown and **orally initiate repair** so the interlocutor understands that repetition/clarification is needed.

This capability is intentionally narrower than:

- general conversation;
- general listening comprehension;
- pronunciation proficiency;
- knowing one memorized sentence;
- understanding the repeated message after repair.

---

## 2. Real purpose

In real interaction, not understanding is not automatically failure.

A competent next action can be:

```text
problem hearing / understanding
→ signal trouble
→ interlocutor repairs / repeats / clarifies
→ interaction continues
```

RQ-015 treats repair as part of interactional competence rather than as evidence of incompetence.

`CLM-INT-017` further distinguishes:

```text
OPEN REPAIR
“I did not get the prior turn globally.”

vs

SPECIFIC REPAIR
“I know which part is the problem.”
```

The first slice focuses on **open/global repair**.

---

## 3. Why this is the first owner slice

It is unusually useful for validating Nếp Method because it combines:

```text
meaning/function
+ listening breakdown
+ actual spoken retrieval
+ intelligibility
+ interaction contingency
+ feedback/repair
+ support fading
+ changed-context use
+ delayed re-probe
```

while requiring very little language.

It also directly tests whether the product can avoid old Vidlish errors such as:

```text
typed answer → called speaking
exact translation recall → called transfer
ASR success → called mastery
post-reveal repetition → called independent evidence
```

---

# 4. Target construct

The primary construct is:

> **oral initiation of open repair after genuine or represented global trouble in hearing/understanding.**

Observable components:

1. learner recognizes that normal task response is not currently available;
2. learner chooses a repair action instead of guessing/remaining silent;
3. learner produces an oral repair signal/request;
4. the signal is intelligible enough for an interlocutor to treat it as a request for repair/repetition.

The capability does not require native-like pronunciation or one exact sentence.

---

# 5. Candidate language resources

Natural-conversation research supports a family of open repair initiators rather than one universal phrase.

For the first near-A0 learning slice, use a **small teachable repertoire** rather than treating all variants as new curriculum items.

## 5.1 Core candidate

```text
Sorry?
```

Function here:

```text
open repair initiation
≈ “I did not get that; please repair/repeat.”
```

Important: the same word can perform other actions in other contexts. Prosody/sequential context matters.

## 5.2 Explicit extension candidate

```text
Could you say that again?
```

This makes the requested repair more explicit and can be introduced as a longer reusable chunk after the short open repair form is understood.

## 5.3 Acceptable alternative evidence

Independent capability evidence should not fail solely because the learner uses a different understandable repair form.

Examples that may be functionally acceptable depending on context include other open or repetition-request forms.

The implementation must therefore avoid one exact-string answer as the definition of success.

## 5.4 Not yet fixed

This document does **not** claim that `Sorry?` is globally the politest or universally best first phrase.

Exact phrase inventory, register/politeness guidance and variant order remain curriculum-validation questions.

---

# 6. Initial prerequisite model

True prerequisites are deliberately small.

The learner does **not** need to master:

- present simple;
- question formation generally;
- a large vocabulary;
- all words inside `Could you say that again?` analytically;
- broad conversation.

For the short open-repair form, required learning is mainly:

```text
spoken form
↔ repair function
+
oral intelligibility
+
knowing when the action is appropriate
```

The longer form can initially be a formulaic multiword unit while its internal constructions deepen later.

---

# 7. Learning design

## Stage A — Establish the function

Show/listen to a very short interaction in which one speaker does not understand and initiates repair.

Goal:

```text
understand what the repair move accomplishes
```

Vietnamese explanation is allowed for rapid semantic/pragmatic establishment.

This is not independent speaking evidence.

## Stage B — Form ↔ function discrimination

Learner hears/sees several short turns and identifies which one functions as a repair request in context.

Include contrasts so the learner is not merely recognizing one visible string.

Possible contrast functions:

- apology;
- normal answer;
- repair initiation.

## Stage C — Spoken-form access

Learner hears the repair form naturally and practices its spoken shape.

Model-visible repetition is rehearsal only.

Record separately from independent retrieval.

## Stage D — Independent oral retrieval

Create a bounded interaction where the learner cannot appropriately continue because the prior spoken turn was not understood.

Do **not** display the answer-bearing repair phrase.

Prompt can be minimal, e.g. the interlocutor waits for the learner's next move.

Learner must speak.

Typing cannot satisfy this stage.

## Stage E — Feedback + repair

If the first spoken attempt fails:

```text
preserve original attempt
→ smallest useful cue
→ learner tries again
→ model only if needed
```

A post-model repetition is learning/rehearsal, not retroactive independent success.

## Stage F — Changed-context use

Use a new prior utterance/context/interlocutor voice.

The learner must again detect that repair is the appropriate next action.

Do not prompt with Vietnamese equivalent such as:

> “Hãy nói: nói lại giúp tôi.”

because that supplies the communicative intention and weakens transfer evidence.

## Stage G — Delayed re-probe

Later, present a new breakdown context without answer-bearing support.

The learner chooses and produces a repair initiation orally.

---

# 8. How to create a legitimate breakdown

Do not deliberately make every audio clip artificially incomprehensible.

Candidate validation contexts:

### Context 1 — naturally difficult first-seen utterance

Use a short utterance whose speech-processing load is plausible for the learner.

If the learner cannot answer the content question, allow repair initiation as a functional response.

### Context 2 — controlled missing/uncertain segment

Create a bounded communication task where a key spoken detail is genuinely uncertain and repetition is a sensible action.

### Context 3 — roleplay contingency

The partner gives an utterance; learner can either respond normally if understood or initiate repair if not.

This is stronger than explicitly telling the learner to request repetition.

---

# 9. Evidence contract

Store conditions separately.

Candidate evidence labels:

```text
repair_function_recognition
repair_form_rehearsal
repair_oral_independent
repair_oral_supported
repair_changed_context
repair_delayed_changed_context
```

Required provenance:

- audio/interlocutor variant;
- first-seen vs repeated;
- support shown;
- model shown;
- number of attempts;
- response audio;
- scorer type/version;
- whether partner actually treated the output as repair;
- time since prior learning exposure.

---

# 10. Scoring boundary

## 10.1 Strongest practical success signal

For the target construct, a meaningful success signal is:

```text
learner produces oral repair move
→ unfamiliar/representative listener understands the repair intent
→ interlocutor repeats/clarifies
```

## 10.2 AI/ASR limitation

ASR may help:

- transcribe for practice;
- detect obvious target forms;
- route feedback;
- surface possible pronunciation problems.

ASR success is **not** durable speaking/interaction evidence by itself.

During owner dogfood, manual playback/self-review can expose obvious product failures, but later validation requires listener evidence appropriate to the claim.

## 10.3 Exact-match rejection

Do not implement:

```text
normalized transcript == "sorry"
→ correct
else
→ wrong
```

because the capability is interactional repair, not exact-string recall.

---

# 11. Changed-context design

A transfer probe should vary meaningful features while retaining the repair function.

Possible changes:

- different speaker voice;
- different topic;
- different preceding utterance length;
- different lexical content;
- different setting;
- different point of breakdown.

Do not call it transfer if only background artwork changes while cue/response mapping is identical.

---

# 12. Delayed criterion

Immediate independent success is useful current-capability evidence.

Durable evidence requires later performance.

There is no literature-derived universal delay for this capability yet.

For initial owner dogfood, use at least a later session/day as a practical validation probe while keeping the exact retention policy provisional.

---

# 13. Falsification conditions

This first slice should be revised if:

- learner memorizes a phrase but repeatedly fails to choose repair when genuine non-understanding occurs;
- learner can type the repair but cannot produce it orally;
- model/reveal is required every time;
- ASR passes output that human listeners do not understand;
- the repair phrase is learned but does not survive new contexts/delay;
- task design makes the correct action obvious without requiring breakdown detection;
- the slice consumes excessive time for a tiny capability compared with a simpler learning design.

---

# 14. What this slice is allowed to prove

If successful under proper validation, this slice can support claims about:

- one bounded interaction-repair capability;
- whether the Nếp Method can be implemented coherently end-to-end for that capability;
- whether evidence semantics survive actual software implementation;
- whether the owner retains/transfers the capability under tested conditions.

It cannot prove:

```text
Nếp Method as a whole is optimal
owner has general speaking ability
owner has general listening ability
all Vietnamese beginners should learn this first
AI conversation is validated
```

---

# 15. Next implementation artifact

Before writing the app slice, derive a **task specification** containing:

```text
exact learning stimuli
exact audio provenance
allowed supports
attempt states
feedback states
accepted functional responses
evidence-event semantics
changed-context variants
delayed probe
manual/automated scorer roles
```

Only then should Cursor/another coding agent implement the slice.
