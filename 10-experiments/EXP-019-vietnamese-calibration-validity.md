# EXP-019 — Vietnamese calibration validity

**Research question:** Does a Vietnamese-L1 prior plus individual diagnostic updating improve learning efficiency over generic sequencing or fixed nationality-based targeting?

## Why this experiment exists

RQ-019 found real Vietnamese-specific patterns, but most studies do not sample true near-A0 Nếp users. The product must test whether those patterns predict useful individual decisions.

## Population

Vietnamese-L1 adults around A0 to low A1.

Before launch, preregister:

- inclusion test,
- target age range,
- sample size from power analysis,
- dialect/background variables collected,
- prior formal-English exposure,
- exact probe scoring and listener criteria.

Do not use university-English-major convenience samples as the only validation population.

## Phase 1 — validate priors

Candidate risk families:

- coda / final-cluster perception and production;
- word prominence / stress-timing;
- known-text versus aural chunk recovery;
- selected high-frequency chunk retrieval;
- articles / number morphology / copula / basic tense-time mapping when stage-appropriate.

For each risk prior calculate:

```text
confirmation rate
false-positive rate
false-negative rate
information gained per probe minute
```

A Vietnamese prior that fails to predict the actual learner population is downgraded or removed.

## Phase 2 — adaptive learning comparison

Randomize learners to:

### A — generic evidence-first

Existing Nếp engines with no Vietnamese-specific probe prioritization.

### B — fixed Vietnamese targeting

Teach/practice a predefined Vietnamese-risk package without requiring individual confirmation.

This is an intentionally important comparator: it tests the tempting “error list” product design.

### C — Vietnamese prior + learner-evidence updating

Use Vietnamese priors only to select cheap probes, then route intervention from actual evidence. Disconfirmed priors are suppressed.

## Primary outcomes

1. delayed changed-context capability gain per learner minute;
2. time-to-correct-identification of the learner’s active bottleneck;
3. unnecessary-remediation minutes on targets the learner already controls;
4. delayed retention on confirmed-risk targets.

## Secondary outcomes

- useful return;
- frustration / perceived relevance;
- hints and reveals;
- pronunciation intelligibility by human listeners for relevant targets;
- transfer from isolated target to phrase / message / interaction;
- dialect/background moderator estimates if sample supports them.

## Expected decision logic

Prefer C only if it:

```text
reduces unnecessary remediation
AND identifies genuine bottlenecks faster
AND does not reduce delayed changed-context gain/minute
```

If generic A performs equally well, remove the added calibration complexity.

If fixed B outperforms C on a specific target with low false-positive cost, that target can become a stronger default — but it still must not become permanent learner truth.

## Red-team checks

- Are we merely improving performance on probes that resemble the calibration test?
- Are pronunciation gains audible to independent listeners or only visible to ASR?
- Are grammar gains tied to meaning in changed contexts or only rule-form exercises?
- Does a successful written task hide an aural weakness?
- Are cluster tasks too hard for A0 and therefore measuring task overload?
- Does collecting dialect information improve prediction enough to justify the complexity?
- Are learners in one education background dominating the sample?

## Stop / simplify rule

Remove any Vietnamese-specific predictor or intervention if:

- it produces high false-positive remediation,
- it does not improve routing or delayed outcomes,
- its effect disappears after controlling for general proficiency/current knowledge,
- or maintaining it requires a parallel curriculum rather than a thin calibration layer.

## Output

EXP-019 should produce a calibrated table such as:

```text
target_family
stage
prior_strength
cheap_probe
confirmation_rate
false_positive_cost
recommended_action
```

Only after this experiment should RQ-019 priors be promoted from research-backed candidates into default learner-model behavior.
