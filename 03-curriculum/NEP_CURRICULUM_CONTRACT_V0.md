# Nếp Curriculum Contract v0

**Status:** provisional curriculum source-of-truth derived from `SYN-METHOD-001`  
**Pedagogical parent:** `07-syntheses/SYN-METHOD-001-nep-method-v0.md`  
**Validation parent:** `00-foundations/NEP_METHOD_VALIDATION_CONTRACT.md`  
**Scope:** Vietnamese-speaking adults beginning near zero / Pre-A1  
**Important:** this contract does not yet define the universal first capability list or a full A1 course.

---

## 1. Purpose

This document converts the Method into constraints for curriculum design.

It answers:

```text
what is a curriculum capability?
what language is allowed to enter?
what does “next” mean?
what tasks are required?
what evidence is allowed?
when may support appear?
when is a target revisited?
when may the curriculum expand?
```

It does **not** answer yet:

```text
Unit 1 = X
Unit 2 = Y
30 A1 lessons
exact vocabulary count
exact grammar order
exact daily schedule
```

Those require target-needs/content evidence and validation.

---

# 2. Primary curriculum unit: capability

The primary curriculum unit is a **useful capability**, not a grammar point, word count, topic or CEFR inventory item.

A capability is:

> a bounded ability to understand and/or produce meaning for a real or defensible target purpose under stated conditions.

Examples of capability *forms* include:

- understand a short request;
- ask for repetition;
- give simple relevant information;
- respond to a follow-up;
- understand a practical message;
- write a practical message;
- repair misunderstanding.

These are examples only. The first actual capability set must pass the V1 target-needs gate.

## 2.1 Required capability record

Every curriculum capability must specify:

```text
capability_id
purpose
representative target task(s)
target domain(s)
input modality
response modality
success condition
communicative consequence
required sub-capabilities
candidate language resources
real prerequisites
support allowed during learning
independent evidence task
changed-context evidence design
delayed evidence requirement if durable ability is claimed
known uncertainties
validation status
```

No capability may exist only because:

```text
“this is A1 grammar”
“this is lesson 4 in a textbook”
“this is a top-500 word”
“AI thinks beginners should learn it”
```

---

# 3. Language-resource model

Capabilities recruit multiple language-resource types.

The curriculum must represent at least:

```text
LEXEME / SENSE
MULTIWORD UNIT / COLLOCATION
CONSTRUCTION / FORM↔MEANING/FUNCTION PATTERN
PRAGMATIC / INTERACTION ROUTINE
```

These may overlap.

For example, a useful routine may contain common words and instantiate a construction. The curriculum does not need to pretend each representation is psychologically independent.

## 3.1 Resource record

Each candidate resource should record when relevant:

```text
resource type
form
meaning/function
spoken form
written form
common variants
register/domain
frequency
range/dispersion
formulaicity/collocational evidence
construction/pragmatic role
target-task links
coverage contribution
Vietnamese-L1 difficulty prior
generative/prerequisite value
learner evidence
source/corpus provenance
```

No field is automatically a ranking score.

---

# 4. Content-entry rule — “Is this worth learning?”

A language resource enters the candidate inventory through a defensible combination of:

```text
target-task value
+ portable general utility
+ frequency
+ range / dispersion
+ representative corpus fit
+ modality / register fit
+ multiword / construction / pragmatic value
+ coverage contribution
+ learning cost
+ Vietnamese-L1 prior where evidence exists
+ generative / prerequisite value
+ learner-specific gap evidence
```

## 4.1 Dominance rules

Some dimensions can override raw frequency.

Examples:

- a lower-frequency expression may be essential for a high-value target task;
- a highly frequent word may not deserve deliberate productive teaching yet;
- a frequent written item may have low early value for an oral target;
- a construction may deserve early attention because it unlocks many useful utterances;
- a population-level Vietnamese difficulty can raise diagnostic priority but cannot prove an individual gap.

## 4.2 Forbidden content shortcuts

Never derive curriculum directly from:

```text
one frequency list
one CEFR vocabulary profile
one grammar inventory
one textbook scope-and-sequence
one corpus
one AI-generated beginner list
```

These may contribute evidence, not authority.

---

# 5. Sequencing rule — “What is useful and learnable next?”

Content selection and sequencing are different decisions.

For each learner/capability, the next target should consider:

```text
capability value now
learner's current evidence
true prerequisites
processing burden
language already accessible
support available
previous exposure
retrieval/review need
transfer need
target modality
opportunity for useful reuse
```

## 5.1 Real prerequisite rule

A resource is a prerequisite only if lack of it materially blocks the intended capability or learning task.

A syllabus order is not a prerequisite.

Do not require:

```text
present simple mastered
→ before learner may ask for clarification
```

unless the target task actually requires that knowledge.

## 5.2 Skip rule

If valid evidence already supports a capability/resource under the needed conditions:

```text
skip redundant instruction
→ probe/use/review as appropriate
```

Coverage completion is not a reason to force instruction.

---

# 6. Near-A0 cognitive/load contract

A beginner task should normally introduce or diagnose **one main bottleneck at a time** while keeping supporting language accessible or deliberately scaffolded.

This does not imply one new word per task.

It means the task should not accidentally test five unknown things when the intended learning target is one construction, word, listening distinction or interaction move.

There is no universal `knownWords >= X%` task rule.

Load should be checked by:

- lexical accessibility;
- construction familiarity;
- spoken decoding demand;
- response complexity;
- number of new elements;
- task instructions;
- memory/attention burden;
- support availability.

---

# 7. Capability learning arc

The curriculum may use the following **orchestration arc** where appropriate:

```text
1. meaningful target / purpose
2. understandable exemplars
3. necessary form↔meaning/function processing
4. concise explicit/L1 help when useful
5. target-modality retrieval / performance
6. feedback + bounded repair
7. repeated practice
8. meaningful variation
9. contextual use / interaction where relevant
10. spaced revisit
11. independent delayed / changed-context evidence when claimed
```

This is not a fixed lesson template.

A target can skip/reorder stages when learner evidence supports it.

---

# 8. Task contract

Every curriculum task must specify four things before implementation:

```text
TARGET CONSTRUCT
OBSERVABLE BEHAVIOR
AVAILABLE SUPPORT / EXPOSURE
ALLOWED INFERENCE
```

## 8.1 Task truthfulness examples

### Listening

If learner reads the transcript while answering:

```text
allowed: transcript-supported comprehension
not allowed: independent audio-only listening
```

### Speaking

If learner types an answer:

```text
allowed: typed productive retrieval
not allowed: speaking capability
```

### Writing

If AI supplies most of the final text:

```text
allowed: assisted revision / feedback response
not allowed: independent writing generation
```

### Transfer

If learner repeats the same task/item:

```text
allowed: repeated-task retention/practice evidence
not allowed: changed-context transfer
```

## 8.2 Attempt-before-reveal

When independent retrieval/generation is the target, answer-bearing support must normally come after an attempt.

When comprehension/initial establishment is the target, reveal-before-attempt may be legitimate.

Task purpose decides the rule.

---

# 9. Support contract

Support is a learning tool, not a failure state.

Possible supports include:

- Vietnamese meaning/explanation;
- model/example;
- caption/transcript;
- replay;
- planning;
- partial cue;
- segmentation/slowing for repair;
- explicit rule/pattern explanation.

Every answer-bearing or processing-altering support must remain visible in evidence provenance.

## 9.1 Fading

Candidate direction:

```text
supported success
→ reduce the support that is no longer needed
→ independent probe later
```

Do not fade because:

```text
learner reached A1
learner learned N words
seven days passed
```

unless direct validation supports that rule.

---

# 10. Feedback contract

Feedback exists to improve the next attempt or future capability.

Possible jobs:

```text
notice mismatch
clarify meaning/function
supply missing form
elicit self-repair
improve intelligibility
repair task failure
improve pragmatic fit
support revision
```

Candidate escalation:

```text
preserve original attempt
→ smallest useful information
→ self-repair when feasible
→ more explicit/model feedback when repair is not feasible
→ store repaired response separately
→ re-probe independently later
```

No global rule says prompts, recasts, direct correction or delayed feedback always wins.

---

# 11. Modality-specific curriculum obligations

## 11.1 Vocabulary/chunks

Do not reduce knowledge to one `known` flag.

Teach/measure according to need:

- form access;
- meaning/function;
- productive retrieval;
- spoken/written access;
- chunk/collocation knowledge;
- contextual use;
- delayed availability.

## 11.2 Listening

Curriculum must be able to distinguish/repair:

```text
decoding
spoken-word access
segmentation
construction parsing
message understanding
```

A transcript may diagnose/support but cannot substitute for independent listening evidence.

## 11.3 Speaking

Speaking curriculum requires actual oral production.

Near-A0 may begin bounded and formulaic, then move toward independent retrieval, recombination and contingent interaction.

## 11.4 Pronunciation

Prioritize intelligibility/comprehensibility and communicatively consequential distinctions, not native-accent imitation.

Vietnamese-specific findings generate diagnostic priors, not mandatory error lessons.

## 11.5 Grammar/constructions

Teach form↔meaning/function/use.

Rule knowledge may support learning but rule-quiz success cannot substitute for interpretation/production evidence when those are the capability target.

## 11.6 Reading

Independent reading requires connected unfamiliar/self-paced text when the claim concerns portable reading ability.

Audio/gloss assistance keeps separate provenance.

## 11.7 Writing

Independent writing evidence requires learner-generated language on a suitable task.

Later new-task writing is needed before broad transfer claims.

## 11.8 Interaction/pragmatics

Eventually require contingent response, shared-goal progress, turn management, repair and pragmatic fit.

An accommodating AI partner is practice, not proof of human-interaction transfer.

## 11.9 Fluency/automaticity

Do not optimize raw speed.

Seek:

```text
efficiency ↑
while relevant quality is preserved
and improvement survives changed tasks/context
```

---

# 12. Review and recycling contract

Important resources/capabilities should recur across time.

Review priority can use memory estimates, but:

```text
scheduler state
≠ language mastery
```

A review event should identify the capability/resource and response condition it rehearses.

Where useful, recycling should progress from familiar retrieval toward changed-context reuse rather than repeating an identical flashcard indefinitely.

Exact spacing/repetition policy remains an empirical curriculum decision.

---

# 13. Curriculum evidence states

Curriculum progression must not depend on one universal `mastered=true`.

At minimum preserve distinctions among:

```text
task-bound observation
mediated/emerging performance
generalization candidate
current independent capability
delayed retention evidence
changed-context transfer evidence
```

The implementation may model these probabilistically or otherwise; the semantic distinctions must survive.

---

# 14. Curriculum balance

The curriculum should be comprehensive **over time**, not mechanically balanced inside every lesson.

Across an appropriate window, learners should receive useful opportunities for:

```text
meaning-focused input
meaning-focused output
focused language learning when useful
fluency/automatization of known language
```

This is a balance heuristic, not a fixed 25/25/25/25 quota.

Target needs can legitimately make one modality dominant for a period.

---

# 15. Personalization boundary

Personalization priority:

```text
1. observed language evidence
2. observed response to task/support
3. declared goals / constraints / accessibility needs
4. validated population/L1 prior
5. stable trait only when treatment interaction is defensible
```

No VARK routing.

No permanent aptitude/working-memory ceiling.

Adaptations should be reversible unless strong evidence justifies otherwise.

---

# 16. AI and generated-content boundary

AI may help generate candidate:

- examples;
- variants;
- feedback wording;
- roleplay turns;
- explanations;
- content metadata.

AI may not silently decide:

```text
what is scientifically optimal
what learner has mastered
what exact curriculum order is correct
```

Generated learning assets must satisfy the same curriculum contract as authored assets and preserve model/version provenance when relevant.

---

# 17. First-slice selection rule

Do not begin by building the whole curriculum.

Select a very small number of first capabilities using:

1. direct target-needs value;
2. high portability/reuse;
3. feasibility for near-A0;
4. manageable language-resource set;
5. ability to elicit real independent behavior;
6. ability to create changed-context/delayed probes;
7. low enough technical complexity to validate the learning loop honestly.

The easiest capability to code is not automatically the best first capability.

The most impressive AI feature is not automatically the best first capability.

---

# 18. Curriculum capability acceptance checklist

A capability cannot be promoted into the first validation curriculum unless all relevant questions are answered:

- [ ] What real purpose does it serve?
- [ ] What target task(s) justify it?
- [ ] Is its early priority supported by needs evidence or explicitly owner-specific?
- [ ] What observable behavior proves current performance?
- [ ] What modality must the learner actually use?
- [ ] What language resources are necessary?
- [ ] Which resources are merely helpful rather than prerequisites?
- [ ] Is supporting language accessible enough for near-A0?
- [ ] What support is allowed during learning?
- [ ] What counts as an independent attempt?
- [ ] What feedback/repair is plausible?
- [ ] What is a meaningful changed-context probe?
- [ ] Is delayed evidence required for the intended claim?
- [ ] What evidence state may success update?
- [ ] What would falsify this curriculum choice?

---

# 19. What remains unresolved after this contract

This contract does not yet decide:

- the exact universal first capability list;
- the owner's first personal capability list;
- exact lexical/chunk/construction inventory;
- exact sequence weights;
- exact lesson/session shape;
- exact review scheduler;
- exact feedback policy by error;
- exact support fade;
- exact AI feature set;
- exact UI.

Those decisions must be made in the next gates rather than smuggled into this contract.

---

# 20. Next step

```text
Curriculum Contract v0
→ V1 target-needs confirmation
→ select 1–3 first capabilities
→ create capability specifications
→ design construct-faithful tasks/probes
→ implement only those slices
→ V3 dogfood
→ V4/V5 target learner validation
→ revise curriculum and Method if needed
```

The curriculum is now constrained enough to begin selecting the first validation capabilities without returning to the legacy Vidlish syllabus.
