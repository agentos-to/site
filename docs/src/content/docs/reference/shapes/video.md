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
| **Also** | [`file`](/docs/reference/shapes/file/) |

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
| `channel` | [`channel`](/docs/reference/shapes/channel/) |
| `transcribe` | [`transcript`](/docs/reference/shapes/transcript/) |
| `addTo` | [`playlist`](/docs/reference/shapes/playlist/) |

## Inherited

From [`file`](/docs/reference/shapes/file/):

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
| `attachedTo` | [`message`](/docs/reference/shapes/message/) |
| `repository` | [`repository`](/docs/reference/shapes/repository/) |

## Skills that produce this shape

- [youtube](/docs/reference/skills/media/youtube/) — `search_videos`, `search_recent_video`, `list_videos`
- [youtube](/docs/reference/skills/media/youtube/) — `get_video`, `transcript_video`
