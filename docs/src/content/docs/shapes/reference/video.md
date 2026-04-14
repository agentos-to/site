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

Example sources: YouTube (via post), local files

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

## Skills that produce this shape

- [youtube](/docs/skills/reference/media/youtube/) — `search_videos`, `search_recent_video`, `list_videos`
- [youtube](/docs/skills/reference/media/youtube/) — `get_video`, `transcript_video`
