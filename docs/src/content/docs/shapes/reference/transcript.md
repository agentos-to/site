---
title: transcript
description: "A text transcript of audio/video content. Linked from meetings and videos."
sidebar:
  label: transcript
---

A text transcript of audio/video content. Linked from meetings and videos.

| Metadata | Value |
|---|---|
| **Plural** | `transcripts` |

## Fields

| Field | Type |
|---|---|
| `language` | `string` |
| `sourceType` | `string` |
| `contentRole` | `string` |
| `durationMs` | `integer` |
| `segmentCount` | `integer` |
| `segments` | `json` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/shapes/shape-design-principles/) for how prior art informs shape design.

- **[WebVTT (W3C)](https://www.w3.org/TR/webvtt1/)** — Our segments are WebVTT cues (start/end/text). language follows WebVTT's LANGUAGE header.
- **[SRT SubRip Subtitles](https://matroska.org/technical/subtitles.html#srt-subtitles)** — Practical alternative cue format. Same segment shape.
- **[Whisper JSON output](https://github.com/openai/whisper)** — Practical source — many transcript skills return Whisper-shaped JSON (segments with start/end/text). Direct match.
