---
id: EVD-RQ-001
status: verified-digest
research_question: RQ-001
last_verified: 2026-08-25
---

# RQ-001 source digest — independent word/chunk knowledge

This digest records the sources used for the first RQ-001 synthesis. Full citation metadata also lives in `data/sources.json`. Claims are intentionally narrower than whole-paper summaries.

| ID | Source | Evidence relevant to RQ-001 | Main limit for Nếp |
| --- | --- | --- | --- |
| `SRC-0002` | Nation, *Learning Vocabulary in Another Language* | Vocabulary knowledge includes form, meaning and use with receptive/productive manifestations. | Framework/book; not a validated Nếp state machine. |
| `SRC-0008` | Laufer & Goldstein (2004), *Language Learning* | In 435 ESL learners, passive recognition → active recognition → passive recall → active recall formed a difficulty hierarchy; recall was harder than recognition. | Primarily bilingual form-meaning testing, not transfer or long-term retention. |
| `SRC-0009` | González-Fernández (2022), *SSLA* | Eight measures across 314 Chinese/Spanish EFL learners loaded on one underlying vocabulary construct; separate performances need not be separate latent faculties. | Not Vietnamese/A0; selected written measures only. |
| `SRC-0010` | González-Fernández (2025), *TESOL Quarterly* | Recognition preceded recall across tested form-meaning, collocation, multiple-meaning and derivative components. | Same 314-learner dataset as related 2022 work; not an independent replication. |
| `SRC-0011` | Webb (2023), *Language Teaching* meta-analysis | 24 studies / N=2,771: observed incidental gains varied by test format, input mode and retention interval. | Incidental learning is not identical to Nếp deliberate A0 instruction. |
| `SRC-0012` | Webb, Yanagisawa & Uchihara (2020), *Modern Language Journal* meta-analysis | Across 22 studies / 100 effects, strong immediate meaning/form recall gains dropped substantially on delayed tests. | Selected intentional word-focused activities; does not measure full communicative use. |
| `SRC-0013` | Rice & Tokowicz (2020), *SSLA* review | Adult training should build phonological, orthographic and meaning representations/connections; retrieval/spacing/elaboration improve on repetition-only approaches. | Laboratory literature; transfer to long-term real use is not automatic. |
| `SRC-0014` | Lei & Reynolds (2022), systematic research synthesis | In 32 word-card studies, receptive knowledge was tested much more often than productive knowledge; form/meaning much more than use. | Specific to word-card literature. |
| `SRC-0015` | Ding et al. (2025), systematic review | Review of 153 collocation studies found many receptive measures but limited validated productive instruments; cues/task format affect inference. | Collocation-specific and not A0/Vietnamese-specific. |
| `SRC-0016` | Webb (2008), *SSLA* | Receptive vocabulary size exceeded productive size under fuller-knowledge scoring; scoring sensitivity changed the observed gap. | Vocabulary-size/translation measures do not equal item-level communicative use. |

## High-signal convergence

1. **Recognition is valid but weaker evidence than recall.** Multiple-choice/selection tasks should only update recognition claims.
2. **Observed knowledge is test-dependent.** Cueing, response mode, scoring and timing change what a correct answer means.
3. **Immediate performance is not durable retention.** Delayed re-demonstration is required for a retention claim.
4. **Productive/use knowledge is systematically undermeasured.** A product that only measures recognition will overstate what it knows about the learner.
5. **Aural and written form should not be conflated.** For a listening-first beginner product, orthographic success cannot substitute for spoken-form recognition.
6. **Chunks require phrase-level measurement.** Revealing part of a phrase or a first letter changes the evidence from independent to scaffolded.

## Important contradiction / refinement

The repo originally spoke loosely about `understood`, `recalled`, `transferred`, and `retained` as separate “dimensions.” `SRC-0009` makes that wording too strong. The safer conclusion is:

> Nếp should record these separately because they come from different tasks and time points, while remaining agnostic about whether they are independent latent psychological abilities.

That distinction is now reflected in `PRN-002` and `SYN-VOC-002`.

## Search coverage for this pass

The discovery pass reviewed 50+ search-result candidates across construct/assessment, retrieval/retention, multiword-unit measurement, and recent acquisition-sequence work, then fetched and retained the sources above because they were the most directly relevant and methodologically useful for RQ-001. Product blogs and low-signal summaries were excluded from the evidence base.
