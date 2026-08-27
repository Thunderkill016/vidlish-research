# Task Spec v0 — Open Repair / Request Repetition Slice

**Status:** implementation-ready research/curriculum contract; not yet software implementation  
**Capability parent:** `FIRST_VALIDATION_CAPABILITY_REPAIR.md`  
**Method parent:** `SYN-METHOD-001`  
**Primary construct:** oral initiation of repair after global non-understanding

---

## 1. Non-negotiable invariants

The implementation must preserve all of these:

```text
1. typing cannot satisfy speaking evidence
2. answer-bearing form shown before response → not independent retrieval
3. model-visible repetition → rehearsal, not independent speaking
4. replayed trouble-source audio ≠ first-seen listening condition
5. post-feedback correction ≠ original success
6. exact-string match ≠ interactional repair capability
7. ASR transcript/score ≠ mastery
8. same scenario repeated ≠ changed-context transfer
9. immediate success ≠ delayed retention
10. success must retain support/scorer/exposure provenance
```

If implementation violates one, the slice fails construct fidelity even if UX looks good.

---

# 2. Language inventory for v0

## Primary taught form

```text
Sorry?
```

Target function in this slice:

> open other-initiated repair: signal that the preceding spoken turn was not adequately heard/understood and invite the interlocutor to repair/repeat.

## Extension form

```text
Could you say that again?
```

Treat initially as a formulaic chunk. Do not require the learner to master the internal grammar before using it.

## Functional alternatives

The scorer may classify other understandable repetition/repair requests as functionally successful or partially successful.

Do not hard-code one target string as the capability definition.

Candidate categories:

```text
OPEN_REPAIR
EXPLICIT_REPETITION_REQUEST
SPECIFIC_REPAIR
BREAKDOWN_SIGNAL_WITHOUT_REQUEST
UNRELATED_RESPONSE
NO_RESPONSE
UNCERTAIN
```

`SPECIFIC_REPAIR` is valid interaction but outside the primary instructional target of this first slice.

---

# 3. Audio provenance

Every audio stimulus must record:

```text
audio_id
speaker_id / voice_id
human | TTS
provider/model/voice/version if TTS
recording date/version if human
script
playback speed
processing applied
exposure_index
```

### Learning audio

High-quality TTS may be used for controlled initial exemplars if provenance is stored.

### Stronger validation audio

At least one changed-context/delayed validation probe should use an **unseen human-recorded voice** before claiming robust transfer beyond TTS practice.

Do not apply artificial slowing/noise unless the task explicitly studies that support/condition.

---

# 4. Task-state model

```text
FUNCTION_ESTABLISHMENT
→ FUNCTION_DISCRIMINATION
→ SPOKEN_MODEL_REHEARSAL
→ CUED_INDEPENDENT_ORAL_RETRIEVAL
→ CONTINGENT_BREAKDOWN_TASK
→ FEEDBACK_REPAIR if needed
→ CHANGED_CONTEXT_PROBE
→ DELAYED_CHANGED_CONTEXT_PROBE
```

This sequence is the v0 experiment design, not a universal Nếp lesson template.

---

# 5. T0 — Function establishment

## Goal

Understand that repair is a useful conversational action.

## Stimulus

Short two-turn interaction:

```text
A: [short natural utterance]
B: Sorry?
A: [repeats or clarifies]
```

Vietnamese micro-explanation allowed:

> Khi không nghe/hiểu lượt vừa rồi, người nói có thể báo hiệu để người kia nói lại hoặc làm rõ.

## Evidence

```text
learning_exposure only
```

No speaking capability update.

---

# 6. T1 — Function discrimination

## Goal

Link the form to its interactional function rather than memorizing orthography only.

## Minimum item types

Use at least three contextual contrasts:

1. `Sorry?` as repair initiation;
2. `Sorry.` as apology;
3. an ordinary response that does not initiate repair.

Audio and sequential context should carry the distinction.

## Learner behavior

Choose/identify the action being performed.

## Allowed inference

```text
repair_function_recognition
```

Not speaking.

---

# 7. T2 — Spoken model rehearsal

## Goal

Build a usable spoken representation.

## Flow

```text
hear target model
→ learner records repetition
→ playback/compare
→ optional bounded feedback
```

Text may be visible because the purpose is rehearsal.

## Evidence

```text
repair_form_rehearsal
support = model_visible
```

Never promote to independent retrieval.

---

# 8. T3 — Cued independent oral retrieval

## Goal

Test whether the repair form/function can be retrieved orally without answer-bearing form support.

## Situation cue

A short scenario may state the communicative problem, e.g.:

> You did not catch what the speaker just said. Respond aloud.

Vietnamese can be used for the scenario during early learning, but the target phrase itself must not be shown.

## Learner behavior

Record an oral response.

## Support forbidden before first attempt

- target English phrase;
- transcript containing target phrase;
- model audio of target phrase;
- first-letter/word cue that reveals the response.

## Allowed inference

If functionally successful:

```text
repair_oral_independent_cued_function
```

This is still weaker than spontaneous breakdown detection because the task tells the learner that repair is needed.

---

# 9. T4 — Contingent breakdown task

## Goal

Test whether the learner selects repair as the next action when normal response is unavailable.

## Task design

1. learner hears a short first-seen utterance;
2. system requests/affords a natural oral next turn;
3. no prompt says “ask them to repeat”;
4. learner may either respond to the message if understood or initiate repair if not;
5. if repair is initiated, interlocutor repeats/clarifies and interaction proceeds.

## Critical design rule

The task must not make repair the obviously pre-labeled correct answer.

## Example stimulus families

Use short practical utterances whose exact lexical content is not itself the curriculum target, e.g. information about:

- time;
- location;
- a simple request;
- a simple status/update.

Do not reuse the same sentence across all probes.

## Allowed inference

A functionally successful oral repair here can support:

```text
repair_oral_independent
+
repair_choice_under_breakdown
```

subject to scorer limitations.

---

# 10. Feedback and repair policy

After an unsuccessful first attempt:

```text
1. preserve original audio + classification
2. give smallest useful feedback
3. allow self-repair
4. escalate only if needed
5. store each attempt separately
```

Candidate escalation:

### F1 — function cue

> Try signaling that you did not understand.

No target English form yet.

### F2 — partial semantic cue

Vietnamese explanation of the repair function.

Still no full English target if self-repair remains plausible.

### F3 — model

Provide `Sorry?` or explicit repetition-request model.

### F4 — rehearsal

Learner repeats/records the model.

Post-F3/F4 success is supported rehearsal evidence, not independent success.

---

# 11. Response classification

## Primary success

A response is functionally successful when a reasonable interlocutor would understand that the learner is initiating repair/repetition after the prior turn.

### Strong examples

```text
Sorry?
Could you say that again?
Can you say that again?
Pardon?
```

Other forms may also be valid.

### Related but not equivalent

```text
I don't understand.
```

This signals breakdown but does not explicitly request a repair. Classify separately rather than simply marking wrong.

### Incorrect

- unrelated answer when the learner demonstrably did not understand;
- silence where a response is required;
- output unintelligible to the listener/scorer;
- English words that do not perform a repair action.

---

# 12. Scorer architecture for v0

## 12.1 Automated layer

ASR/LLM may propose:

```text
transcript
candidate functional category
possible pronunciation issue
confidence / uncertainty
```

It may not write durable learner-state truth directly.

Required provenance:

```text
provider
model
version
prompt/rubric version
confidence where available
```

## 12.2 Dogfood decision

For owner-only V3 dogfood, use:

```text
automated proposal
+
manual playback/self-review when uncertain
```

This is sufficient to find product/measurement failures, not to validate population speaking ability.

## 12.3 Later V4/V5 validation

Use listener/human reference judgments appropriate to the capability, especially for:

- intelligibility;
- repair intent;
- false ASR accept/reject rate;
- subgroup/model disagreement.

---

# 13. Changed-context probe

A changed-context probe must alter meaningful conditions.

Minimum changes from training should include at least two of:

```text
new preceding utterance
new lexical content
new speaker/voice
new setting/task purpose
new position of trouble
less explicit cue
```

The target function remains repair initiation.

## Not enough

```text
same prompt
same audio
same response
new background image
```

is not transfer.

---

# 14. Delayed probe

For owner dogfood v0:

- do not count same-session retries as delayed retention;
- schedule a fresh probe in a later session/day;
- use a new context and preferably a new voice;
- do not show the repair phrase before the first delayed attempt.

Exact retention horizon remains provisional.

Evidence label:

```text
repair_delayed_changed_context
```

---

# 15. Evidence-event fields

Minimum event schema semantics:

```text
event_id
learner_id
capability_key = "open_repair_after_nonunderstanding"
task_id
task_type
attempt_index
timestamp
response_modality = audio
audio_response_ref
stimulus_audio_id
stimulus_exposure_index
first_seen: boolean
support_state
model_visible: boolean
function_cue_visible: boolean
replay_count
response_classification
scorer_type
scorer_provider/model/version
scorer_confidence
manual_review_state
post_feedback: boolean
changed_context_dimensions[]
delay_since_last_target_exposure
```

Do not store only:

```text
correct = true
```

---

# 16. Learner-state update rules

### T1 success

May update:

```text
function recognition evidence
```

### T2 rehearsal success

May update:

```text
spoken rehearsal / supported production evidence
```

### T3 success

May update:

```text
independent oral retrieval under explicit function cue
```

### T4 first-attempt success

Candidate evidence for:

```text
current independent repair capability
```

but confidence depends on scorer quality and representativeness.

### Supported repair after feedback

Update:

```text
mediated/emerging repair capability
```

not independent capability.

### Changed-context success

Candidate generalization/transfer evidence.

### Delayed + changed-context success

Strongest evidence available in this slice for durable portable repair capability under tested conditions.

---

# 17. Minimal content set

Do not expand the slice with unrelated grammar/vocabulary.

Required learning content is bounded to:

```text
repair function
primary short repair form
one explicit extension form
spoken realization/intelligibility
recognition of when repair is appropriate
```

Everything else belongs only if needed to make a task comprehensible.

---

# 18. Acceptance tests for the future implementation

The implementation is not accepted unless tests or manual verification establish:

- [ ] first T3/T4 response is recorded before any answer-bearing feedback;
- [ ] speaking task cannot be completed by typing;
- [ ] rehearsal events cannot update independent-speaking state;
- [ ] support/replay provenance survives refresh/persistence;
- [ ] post-feedback attempts remain separate from original attempt;
- [ ] ASR classification is stored as scorer output, not ground truth;
- [ ] functional alternatives are possible; no exact-string-only capability rule;
- [ ] changed-context probe actually changes meaningful task conditions;
- [ ] delayed probe uses a later timestamp/session and no prior answer reveal;
- [ ] UI never claims “mastered speaking” from one successful attempt;
- [ ] evidence can be reconstructed after reload.

---

# 19. V3 owner dogfood success criteria

This stage is primarily a **coherence/failure test**, not efficacy proof.

The slice is ready for broader pilot consideration only if:

1. the owner can understand what the capability is for;
2. the learner can complete real oral attempts without hidden typing shortcuts;
3. feedback helps without overwriting original evidence;
4. changed-context/delayed probes are genuinely different;
5. evidence survives persistence/reload correctly;
6. automated scoring errors are visible rather than silently promoted;
7. the lesson feels small enough to use but does not reduce learning to a token click.

---

# 20. Stop condition before coding more curriculum

Do not add capability 2 merely because capability 1 is implemented.

First inspect:

```text
implementation fidelity
+ owner dogfood evidence
+ delayed changed-context behavior
+ scoring failures
+ support dependence
+ learning-time cost
```

Then decide:

```text
RETAIN / MODIFY / NARROW / REJECT / UNRESOLVED
```

Only after that should the curriculum branch expand.
