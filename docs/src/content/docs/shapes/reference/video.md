---
title: video
description: "A video file — the media artifact, not the social context around it."
sidebar:
  label: video
---

A video file — the media artifact, not the social context around it.
Engagement metrics (views, likes, comments) belong on the post that
contains this video, not on the video itself. A video on your hard
drive has no likes.

| Metadata | Value |
|---|---|
| **Plural** | `videos` |
| **Subtitle field** | `author` |
| **Also** | [`file`](/docs/shapes/reference/file/) |

## Fields

| Field | Type |
|---|---|
| `durationMs` | `integer` |
| `resolution` | `string` |
| `frameRate` | `number` |
| `codec` | `string` |

## Relations

| Relation | Target |
|---|---|
| `channel` | [`channel`](/docs/shapes/reference/channel/) |
| `transcribe` | [`transcript`](/docs/shapes/reference/transcript/) |
| `addTo` | [`playlist`](/docs/shapes/reference/playlist/) |

## Inherited

From [`file`](/docs/shapes/reference/file/):

| Field | Type |
|---|---|
| `encoding` | `string` |
| `filename` | `string` |
| `format` | `string` |
| `kind` | `string` |
| `lineCount` | `integer` |
| `mimeType` | `string` |
| `path` | `string` |
| `sha` | `string` |
| `size` | `integer` |

| Relation | Target |
|---|---|
| `attachedTo` | [`message`](/docs/shapes/reference/message/) |
| `repository` | [`repository`](/docs/shapes/reference/repository/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/VideoObject](https://schema.org/VideoObject)** — Our durationMs ≈ duration (ISO 8601 period); resolution ≈ videoFrameSize; frameRate has no direct property; codec ≈ encodingFormat.
- **[IANA Media Types (video/*)](https://www.iana.org/assignments/media-types/media-types.xhtml#video)** — Our codec values map to registered video/* media types (mp4, webm, ogg).
- **[MPEG / ITU video codec specs](https://www.itu.int/rec/T-REC-H.264)** — Canonical codec definitions. Our codec values are MPEG/ITU codec short names (h264, vp9, av1).

## Skills that produce this shape

- [youtube](/docs/skills/reference/media/youtube/) — `search_videos`, `search_recent_video`, `list_videos`, `get_video`, `transcript_video`
