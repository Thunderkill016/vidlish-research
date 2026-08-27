# YouTube Content Acquisition for Nếp

**Status:** tooling/content-source contract; not pedagogical evidence  
**Checked:** 2026-08-28  
**Relevant method:** `SYN-METHOD-001`  
**Relevant research:** RQ-009, RQ-010, RQ-011, RQ-015, RQ-020, RQ-027

---

## 1. Decision

YouTube can be a major source of **candidate learning material** for Nếp, but it is not a pedagogical source of truth.

```text
YouTube
→ raw content candidates
→ metadata/transcript analysis
→ curriculum/content filters
→ learner × clip readiness
→ support policy
→ learning task
```

Never:

```text
YouTube video exists
→ therefore good learning material
```

and never:

```text
popular English-learning creator
→ therefore research evidence
```

Research papers/books/reviews remain in the research evidence graph. YouTube videos belong to a separate **content corpus** unless the video itself is a primary source intentionally being studied.

---

# 2. YouTube.js status

The LuanRT `YouTube.js` project (`youtubei.js`) is an unofficial JavaScript client for YouTube's internal InnerTube API.

As checked on 2026-08-28:

- latest GitHub release: `v18.0.0` (2026-08-13);
- package name: `youtubei.js`;
- supports Node.js and browser-compatible runtimes;
- exposes search/video-information APIs;
- exposes transcript access in current examples via `VideoInfo#getTranscript()`;
- the library also exposes streaming/download functionality.

References:

- https://github.com/LuanRT/YouTube.js
- https://github.com/LuanRT/YouTube.js/releases/tag/v18.0.0
- https://github.com/LuanRT/YouTube.js/tree/main/examples/transcript

The project explicitly states that it is not affiliated with or endorsed by YouTube.

## Important stability boundary

InnerTube is an internal API.

Therefore:

```text
works today
≠ stable public contract
```

YouTube server/client changes can break parsers, transcript endpoints, authentication or other behavior without a public deprecation cycle.

Nếp must not make curriculum/evidence integrity depend on one private endpoint continuing to work.

---

# 3. Compliance boundary

The library's technical ability to perform an operation does not establish that Nếp should perform it.

Current YouTube Terms restrict automated access except where permitted, and official YouTube API policies place strong restrictions on downloading/storing audiovisual content, separating audio/video, background playback and modification of the YouTube player/content.

Official references:

- https://www.youtube.com/t/terms
- https://developers.google.com/youtube/terms/developer-policies
- https://developers.google.com/youtube/terms/developer-policies-guide

## Nếp default rule

Do **not** build the product around unauthorized downloading, audiovisual caching, audio extraction or restriction-circumvention.

Even though YouTube.js exposes methods such as `download()`, Nếp treats these as **disabled by product policy unless a specific rights/compliance basis exists**.

Preferred production model:

```text
store video identity + derived educational metadata
→ play through permitted YouTube playback/embed path
```

rather than:

```text
download video/audio
→ re-host it as Nếp media
```

## Rights status must be explicit

Every candidate should record one of:

```text
creator_owned
explicit_permission
creative_commons_or_other_compatible_license
standard_youtube_license
unknown
```

A rights state controls what Nếp may store, transform and redistribute.

---

# 4. Architecture: content-source adapter, not learning engine

Define an abstraction such as:

```ts
interface VideoContentSource {
  search(query: string): Promise<VideoCandidate[]>;
  getMetadata(videoId: string): Promise<VideoMetadata>;
  getTranscript?(videoId: string): Promise<TranscriptResult>;
}
```

Possible implementations:

```text
ManualUrlSource
OfficialYouTubeApiSource
ExperimentalInnerTubeSource (YouTube.js)
OwnedContentSource
```

The curriculum/learning layer must not know which adapter supplied the candidate.

Therefore a YouTube.js outage can be handled by:

```text
adapter unavailable
→ discovery degrades/falls back
```

not:

```text
adapter unavailable
→ curriculum/evidence system fails
```

---

# 5. Production versus research/prototyping policy

## Production default

Prefer official YouTube APIs/player/embed behavior where feasible and comply with their policies.

## Experimental/internal discovery

YouTube.js may be evaluated as an **optional adapter** for local research/prototyping only after reviewing the relevant current terms and intended usage.

It must be:

- version pinned;
- feature-flagged;
- replaceable;
- isolated from learner evidence logic;
- monitored for endpoint/parser failure;
- prohibited from silently switching to download/re-host behavior.

## Do not put credentials into client code

If any authenticated YouTube workflow is eventually needed, authentication/secrets must follow the security model of the chosen API and environment. Public client code must not contain secrets.

---

# 6. Candidate ingestion pipeline

```text
QUERY / CHANNEL / MANUAL URL
        ↓
DISCOVERY ADAPTER
        ↓
VIDEO METADATA
        ↓
TRANSCRIPT / CAPTION AVAILABILITY
        ↓
RIGHTS + PLAYBACK CHECK
        ↓
LANGUAGE / CONTENT ANALYSIS
        ↓
WINDOW SEGMENTATION
        ↓
RQ-027 CONTENT VALUE
        ↓
RQ-009 LEARNER × WINDOW READINESS
        ↓
RQ-010/011 SUPPORT POLICY
        ↓
CURRICULUM CANDIDATE
```

A discovered YouTube result is only `candidate`, never automatically `approved`.

---

# 7. Minimum candidate record

```ts
type VideoCandidate = {
  provider: "youtube";
  videoId: string;
  url: string;

  title: string;
  channelId?: string;
  channelTitle?: string;
  publishedAt?: string;
  durationSeconds?: number;

  declaredLanguage?: string;
  detectedLanguage?: string;

  captionsAvailable?: boolean;
  captionLanguages?: string[];
  transcriptSource?:
    | "creator_caption"
    | "youtube_auto_caption"
    | "licensed_external"
    | "owner_transcript"
    | "unavailable";

  rightsStatus:
    | "creator_owned"
    | "explicit_permission"
    | "compatible_license"
    | "standard_youtube_license"
    | "unknown";

  playbackMode: "youtube_embed" | "external_link" | "owned_media";

  acquisitionAdapter:
    | "manual"
    | "youtube_official_api"
    | "youtubejs_innertube"
    | "other";
  adapterVersion?: string;

  acquiredAt: string;
};
```

Do not conflate YouTube metadata with educational analysis.

---

# 8. Transcript policy

Transcripts are extremely useful for **analysis**, but they are not automatically ground truth.

Store provenance:

```text
human creator caption
YouTube automatic caption
other ASR
manually corrected transcript
```

Automatic captions may contain errors in:

- word identity;
- proper nouns;
- reduced/connected speech;
- punctuation;
- speaker boundaries;
- timing.

Therefore transcript-derived lexical/grammar metrics inherit transcript uncertainty.

For educationally critical windows, use manual/editorial verification when practical.

## YouTube.js transcript access

The current library example uses:

```ts
const info = await yt.getInfo(videoId);
const transcriptInfo = await info.getTranscript();
```

This confirms a current technical path, not a guaranteed future public API contract.

If transcript acquisition fails:

```text
no transcript
→ candidate may still be playable
→ automatic curriculum analysis is unavailable/degraded
```

Do not fabricate a transcript.

---

# 9. Analysis derived from a transcript/window

For each 15–45 second candidate window, Nếp may derive signals such as:

```text
lexical coverage against learner evidence
critical unknown words/chunks
multiword/construction coverage
speech rate estimate
utterance length
density of new language
topic/domain
caption availability
speaker count estimate
turn density
overlap/noise/music estimate
connected-speech burden
visual-semantic support estimate
```

These are **compatibility signals**, not an automatic CEFR score.

Model-derived estimates must store model/version provenance where relevant.

---

# 10. RQ-027 content-value filter

A YouTube candidate should be favored when it contributes to useful target capabilities, not merely because it is frequent or entertaining.

Candidate value dimensions include:

```text
target-task value
portable utility
frequency / range where relevant
spoken-register fit
chunk/construction value
coverage contribution
prerequisite/generative value
learner gap
interest/relevance
```

Popularity/views/likes may be metadata, but they are not learning-value evidence.

---

# 11. RQ-009 learner × clip readiness

Do not assign a single permanent level to a YouTube video.

```text
learner evidence
×
video window
→ readiness
```

Important dimensions:

- aural lexical coverage;
- speech-processing load;
- speaker/turn complexity;
- connected speech;
- visual support;
- topic familiarity;
- critical unknowns;
- support required.

A 20-minute video can contain both usable and unusable windows for the same learner.

Therefore Nếp should index **windows**, not only whole videos.

---

# 12. Support policy for YouTube windows

RQ-010/011 continue to apply.

```text
first useful listening attempt
→ capture condition
→ if failure, diagnose
→ add the smallest useful support
→ retry
→ later remove/reduce answer-bearing support
```

Possible supports:

- replay;
- English captions;
- selected transcript line;
- Vietnamese micro-gloss;
- bounded explanation;
- temporal repair/segment replay.

Never infer:

```text
understood with captions
→ independent listening mastered
```

or:

```text
understood Vietnamese subtitle
→ understood English audio
```

---

# 13. YouTube is not required for the first validation slice

The first owner validation capability is open conversational repair/requesting repetition.

For this slice, controlled human/TTS audio is preferable because it allows the experiment to isolate:

- function learning;
- oral retrieval;
- feedback;
- changed-context use;
- delayed retention;
- evidence semantics.

Using arbitrary YouTube clips too early would add uncontrolled lexical/speech/content variables.

YouTube becomes especially valuable after the foundational loop works, for:

```text
authentic listening exposure
changed-context transfer
real speaker/voice variety
interest-driven input
content/domain branches
later independent media comprehension
```

---

# 14. Recommended implementation boundary

When product implementation begins, Cursor/agents may implement a package such as:

```text
content-sources/
  youtube-official.ts
  youtube-inner-tube.experimental.ts
  manual-url.ts
  owned-media.ts

content-analysis/
  transcript-normalization.ts
  window-segmentation.ts
  lexical-analysis.ts
  difficulty-signals.ts
  readiness.ts
```

But learning code consumes only normalized `VideoCandidate` / `VideoWindow` records.

Forbidden dependency:

```text
lesson component
→ directly calls Innertube
```

Preferred:

```text
source adapter
→ normalized content record
→ analysis
→ curriculum approval
→ learner task
```

---

# 15. Failure and fallback policy

Possible failures:

```text
InnerTube endpoint changed
transcript unavailable
caption language missing
video deleted/private
embedding disabled
region/age restriction
rights unclear
metadata shape changed
```

Response:

```text
mark candidate unavailable/degraded
→ do not corrupt curriculum state
→ find replacement window/content
```

A content-source outage must never delete learner evidence or change what previous attempts meant.

---

# 16. Bottom line

YouTube can become an enormous **content reservoir** for Nếp.

YouTube.js is technically interesting for discovery/metadata/transcript experimentation, but because it uses YouTube's internal API it must stay **optional, isolated and replaceable**.

Nếp's moat is not:

```text
we can scrape YouTube without an API key
```

It should be:

```text
we can take permitted, relevant real-world content
→ analyze it against a learner's actual evidence
→ choose a learnable window
→ apply the right support
→ later test independent transfer
```

That is the part controlled by Nếp Method, not by YouTube.js.
