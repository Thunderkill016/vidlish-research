---
id: FEAT-PRN-001
title: Intelligibility-first pronunciation priority engine
status: research-backed-candidate
research_question: RQ-007
---

# Feature research spec — Intelligibility-first pronunciation priority engine

## Learner problem

Pronunciation products often expose beginners to a broad IPA inventory, native-accent imitation or opaque scores. That can spend learner time correcting harmless accent features while missing sound patterns that actually hide a word, erase grammatical information or make a listener work much harder.

Vietnamese-speaking learners also show population-level pronunciation risks, but those risks vary by learner, task, region and listener. A product must use them as **diagnostic priors**, not stereotypes.

## Target capability

Select and practice the smallest pronunciation target that materially improves the probability that an unfamiliar listener correctly understands the learner's intended word/message, then verify transfer in first-seen utterances.

## Research basis

- `SYN-PRN-001`
- `CLM-PRN-001` through `CLM-PRN-014`
- `PRN-062` through `PRN-075`
- RQ-001 evidence provenance
- RQ-003 listening diagnostics
- RQ-005 first-seen transfer
- `FEAT-SPK-001` guided speaking ladder
- `SYN-ASR-001` / `FEAT-ASR-001` validity gate for automated speech evidence

## Non-goals

- erase Vietnamese accent;
- force one native dialect;
- teach every IPA symbol in sequence;
- award a global pronunciation percentage;
- make ASR confidence a mastery criterion;
- correct every detectable segmental difference.

## Architecture

```text
Curriculum target / learner intent
          ↓
Candidate Pronunciation Targets
          │
          ├── Vietnamese prior risk
          ├── functional/information load
          ├── known dialect scope
          └── research confidence
          ↓
Learner Diagnostic Evidence
          │
          ├── does learner collapse/omit target?
          ├── task/context dependence?
          └── support history
          ↓
Communicative-Risk Ranker
          ↓
Practice Selector
  perception / noticing / bounded production
          ↓
Independent Speaking Attempt
          ↓
Feature + Listener-Outcome Evidence
          ↓
Changed-context / delayed recheck
          ↓
Evidence Engine
```

## Candidate priority tiers

```text
Tier I   word/coda/cluster information preservation
Tier II  high-value lexical contrasts + stress/vowel integrity
Tier III focus/timing/chunking for easier comprehension
Tier IV  interactional prosody + optional accent refinement
```

The tier is a product heuristic, not a CEFR mapping.

## Hard product rules

1. Accentedness alone never creates a pronunciation failure.
2. Do not assign meaningful practice from a Vietnamese population prior without learner-level evidence unless the feature is being used as a brief diagnostic probe.
3. Prioritize actual word/message risk over phonetic distance from a native model.
4. Keep `feature_accuracy_candidate`, `intelligibility`, and `comprehensibility` separate.
5. If the learner's intended word/message is reliably understood, do not force correction solely for accent conformity.
6. Preserve first-seen provenance for pronunciation-transfer attempts.
7. Log listener/scoring background and scoring rule version.
8. Route all ASR/vendor pronunciation outputs through `FEAT-ASR-001`; machine output alone never sets mastery.
9. Do not make one Vietnamese regional variety the hidden default for every learner.
10. A feature detected in controlled repetition must transfer to model-hidden production before it can support independent pronunciation evidence.

## Candidate target metadata

```ts
type PronunciationTarget = {
  id: string;
  featureFamily:
    | "coda"
    | "cluster"
    | "consonant_contrast"
    | "vowel_contrast"
    | "lexical_stress"
    | "sentence_focus"
    | "timing"
    | "intonation";
  communicativeFunction: string;
  vietnamesePrior: "high" | "moderate" | "unknown";
  functionalLoad: "high" | "moderate" | "low" | "unknown";
  dialectScope: string[];
  evidenceIds: string[];
  acceptedVariation: string[];
  prerequisiteTargetIds: string[];
};
```

Do not use `nativeCorrect: boolean`.

## Candidate attempt metadata

```ts
type PronunciationAttempt = {
  learnerId: string;
  targetFeatureId: string;
  speechTaskId: string;
  speakingLevel: string;
  firstSeen: boolean;
  supportLevel: string;
  modelVisibleAtResponse: boolean;
  attemptBeforeFeedback: boolean;
  scoringMethod: string;
  scoringRuleVersion: string;
  listenerBackground?: string;
  featureRealizedCandidate?: boolean;
  intendedWordIdentified?: boolean;
  intendedMessageUnderstood?: boolean;
  comprehensibilityRating?: number;
  repairNeeded?: boolean;
  repairSuccess?: boolean;
};
```

## Example — final `/s/`

Curriculum family:

```text
like / likes
```

Flow:

```text
hear contrast in meaning
→ identify which message was spoken
→ produce target in bounded word/chunk
→ "He likes tea."
→ unseen parallel: "She likes coffee."
→ listener/message check
→ delayed first-seen variant later
```

If the learner already preserves `/s/` reliably in connected speech, skip the lesson despite the Vietnamese population prior.

## Example — lexical stress

Do not teach:

```text
memorize stress mark for every word
```

Prioritize when a learner's realization changes a vowel/syllable enough to threaten word identification.

```text
word identified despite harmless prominence variation
→ no urgent correction

word repeatedly misidentified after stress + vowel distortion
→ target stress/vowel relationship
```

## Example — `/θ/`

`/θ/` may be nonnative or substituted for a learner. That alone is not enough to make it an early target.

```text
if substitution preserves intended words/messages
→ low urgency

if learner's actual substitution causes recurrent lexical confusion
→ learner-specific priority increases
```

This is the intended use of communicative/functional load rather than prestige norms.

## Practice modes

Candidate modes:

```text
P1 perception / identification
P2 contrast noticing with articulatory cue
P3 bounded production
P4 short utterance production
P5 changed-context production
P6 guided listener/interaction check
```

These are **practice modes**, not a second speaking ladder. They should be embedded inside `SP0`–`SP5` from `FEAT-SPK-001`.

## Feedback sequence

```text
independent attempt
      ↓
communication succeeds?
  ┌───┴────┐
 yes       no / high-risk failure
  ↓             ↓
continue     minimal contrast/articulation cue
                 ↓
              self-repair
                 ↓
       reveal model only if needed
                 ↓
         supported rehearsal
                 ↓
      later model-hidden attempt
```

## UI implications

The learner should see concrete communicative feedback such as:

```text
"Người nghe dễ bỏ mất âm cuối này, nên `rice` có thể thành `rai`."
```

or

```text
"Câu vẫn được hiểu rõ. Không cần sửa chỉ để nghe giống người bản xứ."
```

Avoid:

```text
Pronunciation: 72/100
Native score: 64%
Accent score: B-
```

until a validated construct exists—and accent conformity should not become the construct even then.

## Risks

- population priors become stereotypes;
- human listener judgments vary by background;
- ASR may systematically penalize accents rather than communication failure;
- a target can be easy in word lists and fail in spontaneous speech;
- feature correction can consume time without improving message success;
- overcorrection can make learners monitor every sound and harm fluency;
- “functional load” tables may not transfer unchanged to Vietnamese learner vocabulary and international listener populations.

## Falsification

`FEAT-PRN-001` should be redesigned if `EXP-007` shows the priority engine does not improve delayed first-seen listener understanding per practice minute over a simpler pronunciation curriculum.

## Learning metrics

Primary:

- listener word/message identification on first-seen utterances;
- delayed first-seen listener success;
- target-specific production transfer without model;
- repair success after communication breakdown.

Secondary:

- comprehensibility / listener effort;
- target feature realization under controlled scoring;
- practice minutes per recovered intelligibility failure;
- cross-listener-background stability.

## Engagement metrics (separate)

- pronunciation-task abandonment;
- voluntary retry;
- time-on-target;
- learner-reported usefulness.

None of these engagement metrics prove pronunciation learning.
