# RQ-019 — Vietnamese-specific calibration without stereotyping

**Synthesis ID:** `SYN-VIE-001`  
**Status:** initial synthesis complete  
**Depends on:** `RQ-001`, `RQ-002`, `RQ-003`, `RQ-006`, `RQ-007`, `RQ-012`, `RQ-015`, `RQ-017`

## Research question

How should Nếp use Vietnamese-L1 evidence to choose what to test, teach and repair for near-A0/A1 adults without assuming every Vietnamese learner has the same errors?

## Short answer

Use Vietnamese evidence as a **Bayesian-style prior for diagnosis**, not as a learner label.

```text
Vietnamese-L1 evidence
        ↓
risk prior: what is worth probing cheaply
        ↓
individual learner attempt
        ↓
observed evidence
        ↓
priority / repair decision
        ↓
delayed + changed-context evidence
        ↓
update learner model
```

The individual attempt must outrank the population prior.

## Why a fixed “Vietnamese error list” is wrong

Several direct studies find recurring Vietnamese-L1 patterns, but the same literature also shows moderation by:

- proficiency,
- L2 experience,
- elicitation task,
- feature complexity,
- prior vocabulary,
- L1-L2 congruency,
- likely dialect/background differences.

A list such as:

```text
Vietnamese learner
→ final consonants bad
→ articles bad
→ stress bad
```

is therefore too coarse for a learner model.

The useful representation is:

```text
risk_prior(target, construct, context)
observed_evidence(target, construct, context)
```

not:

```text
nationality_error = true
```

## Candidate Vietnamese-specific risk families

### A. Speech form and pronunciation

High-value candidates for cheap diagnosis:

1. word-final consonants / codas;
2. simple versus complex final clusters;
3. selected cluster types with high functional load;
4. English word prominence;
5. phrase/compound prominence and timing;
6. selected vowel/consonant contrasts only when they cause lexical confusion for this learner.

Do **not** make accent reduction the goal. Priority should be driven by intelligibility and meaning.

A useful priority score is conceptually:

```text
priority
≈ observed_failure
× communicative_impact
× target_frequency
× current_capability_relevance
× estimated_learnability
```

L1 prior changes what gets probed; it does not substitute for `observed_failure`.

### B. Listening / phonological decoding

Nếp should distinguish:

```text
I do not know this word
```

from:

```text
I know this word in text
but I did not recover it from speech
```

and from:

```text
I recovered the words
but failed to build the message
```

Candidate Vietnamese-sensitive diagnostics:

- short coda contrasts,
- word-prominence identification,
- a known phrase in careful versus connected speech,
- chunk reconstruction with answer hidden,
- same lexical content in text after an audio miss.

This connects directly to `FEAT-LIS-001`; RQ-019 does not create a second listening engine.

### C. Vocabulary and chunks

The Vietnamese evidence strengthens the existing Nếp rule that chunks are first-class lexical targets.

Candidate learner-model fields:

```text
lexical_target
  kind: word | chunk
  l1_congruency: unknown | congruent | noncongruent | mixed
  form_evidence
  meaning_evidence
  aural_evidence
  production_evidence
  delayed_evidence
```

`l1_congruency` is a difficulty feature, not a mastery fact.

For near beginners, prioritize practical high-frequency chunks before academic collocations. The academic and B1 studies support the mechanism, not the A0 item list.

### D. Grammar / constructions

Vietnamese-specific evidence suggests some English meanings deserve earlier diagnostic attention because they are encoded differently or less morphologically in Vietnamese:

- definiteness / article choice,
- number and plural morphology,
- mass-count interpretation,
- tense/aspect marking,
- third-person agreement,
- copular adjective constructions.

But the teaching unit remains the **meaning-linked construction**, not the isolated rule.

Example:

```text
There is a café near here.
I went there yesterday.
She works here.
```

Nếp can expose the learner to the meaning contrast, require interpretation, then controlled production and changed-context use. It should not begin with a lecture about “Vietnamese has no English-style inflection.”

### E. Pragmatics

Vietnamese-specific pragmatic evidence is much thinner and often higher proficiency.

Therefore Nếp should not encode:

```text
Vietnamese people are indirect
```

Instead it should model scenario variables:

```text
relationship
power / role
social distance
imposition
setting
preferred tone
```

and teach multiple acceptable realizations.

## Proposed learner-model separation

```text
l1_risk_prior
  target_family
  construct
  prior_weight
  source_ids[]
  moderators[]

learner_evidence
  actual attempts from existing Evidence Engine

calibration_state
  confirmed_risk
  disconfirmed_risk
  uncertain
  not_tested
```

A `confirmed_risk` is still not a permanent trait. Later evidence can change it.

## How RQ-019 modifies the existing engines

| Existing engine | Vietnamese calibration contribution |
| --- | --- |
| Vocabulary evidence | add chunk congruency/risk metadata, no new mastery state |
| Diagnostic listening | choose high-information Vietnamese-risk probes when useful |
| Pronunciation priority | initialize likely high-impact targets, then rank from actual learner evidence |
| Grammar constructions | prioritize selected meaning-form mappings for diagnosis, not rule memorization |
| Interaction | add contextual pragmatic probes later; avoid national stereotypes |
| Curriculum orchestrator | use confirmed individual needs to adjust task mix and repair load |

## Product boundary

`FEAT-VIE-001` must **not** become a Vietnamese-only parallel curriculum.

Correct architecture:

```text
shared Nếp curriculum + engines
            ↑
Vietnamese calibration layer
            ↑
individual evidence
```

Wrong architecture:

```text
Vietnamese curriculum
English curriculum
Korean curriculum
Japanese curriculum
...
```

The second architecture duplicates pedagogy and turns L1 research into rigid nationality tracks.

## Confidence

High confidence:

- Vietnamese-specific priors must not be treated as individual truth.
- perception and production need separate evidence.
- formulaic language deserves independent treatment.
- pronunciation priority should be communicative rather than native-accent based.

Moderate confidence:

- coda/cluster and stress/timing families deserve cheap early probes.
- article/number/inflection mappings deserve targeted diagnostic attention.
- congruency is useful chunk-difficulty metadata.

Low / unresolved:

- exact A0 target set,
- exact dialect modifiers,
- exact probe count,
- exact remediation dose,
- exact stage at which each grammar/pragmatic risk becomes worth testing.

Those move to `EXP-019`.
