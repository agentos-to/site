---
title: sound
description: "An audio clip — startup chimes, error beeps, notification dings,"
sidebar:
  label: sound
---

An audio clip — startup chimes, error beeps, notification dings,
UI feedback sounds. Short, role-specific audio a theme (or app)
bundles for system events.

Distinct from longer-form audio: a recorded song belongs in `album`
/ `track` (when those exist); a podcast segment belongs in `episode`;
a meeting recording belongs in `transcript`. Sound is for the
system-event slice of audio.

A sound IS one file (one startup.wav, one error.mp3) so it
`also: [creative_work, file]` — both the abstract work (composer,
license) and the file artifact (size, mimeType).

| Metadata | Value |
|---|---|
| **Plural** | `sounds` |
| **Subtitle field** | `purpose` |
| **Identity (any)** | `url` |
| **Also** | [`creative_work`](/shapes/reference/creative_work/) · [`file`](/shapes/reference/file/) |

## Fields

| Field | Type |
|---|---|
| `durationMs` | `integer` |
| `channels` | `integer` |
| `sampleRate` | `integer` |
| `bitDepth` | `integer` |
| `purpose` | `string` |

## Inherited

From [`creative_work`](/shapes/reference/creative_work/) · [`file`](/shapes/reference/file/):

| Field | Type |
|---|---|
| `copyrightYear` | `integer` |
| `coverage` | `string` |
| `dateCreated` | `date` |
| `description` | `string` |
| `encoding` | `string` |
| `filename` | `string` |
| `format` | `string` |
| `kind` | `string` |
| `language` | `string` |
| `license` | `string` |
| `lineCount` | `integer` |
| `mimeType` | `string` |
| `path` | `string` |
| `sha` | `string` |
| `size` | `integer` |
| `tags` | `string[]` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/AudioObject](https://schema.org/AudioObject)** — Our durationMs ≈ duration (ISO 8601 period). Most metadata comes from creative_work via `also`; AudioObject's surface is sparse (contentUrl, encodingFormat, transcript).
- **[ID3v2 (audio metadata in MP3)](https://id3.org/id3v2.4.0-structure)** — TPE1=artist (author via creative_work); TALB=album; TIT2=title (name via creative_work); TYER=year (copyrightYear via creative_work); TCOP=copyright; TCOM=composer.
- **[WAV LIST INFO chunks](https://www.recordingblogs.com/wiki/list-chunk-of-a-wave-file)** — IART=artist; ICOP=copyright; ICRD=creation date; INAM=name; IGNR=genre. Inherited from creative_work where they apply.
- **[Broadcast Wave Format (BWF) bext chunk](https://tech.ebu.ch/docs/tech/tech3285.pdf)** — BWF carries Originator (creator), OriginationDate, OriginatorReference — production-pipeline provenance for broadcast audio. Inherited via creative_work; AgentOS doesn't currently parse bext chunks.
