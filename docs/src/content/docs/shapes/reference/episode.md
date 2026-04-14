---
title: episode
description: "A single episode of a podcast or show. Transcribable."
sidebar:
  label: episode
---

A single episode of a podcast or show. Transcribable.

Example sources: YouTube, future podcast skill

| Metadata | Value |
|---|---|
| **Plural** | `episodes` |
| **Subtitle field** | `author` |

## Fields

| Field | Type |
|---|---|
| `durationMs` | `integer` |
| `episodeNumber` | `integer` |
| `seasonNumber` | `integer` |

## Relations

| Relation | Target |
|---|---|
| `series` | [`podcast`](/docs/shapes/reference/podcast/) |
| `transcribe` | [`transcript`](/docs/shapes/reference/transcript/) |
| `guest` | [`person[]`](/docs/shapes/reference/person/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/ontology/shape-design-principles/) for how prior art informs shape design.

- **[Apple Podcasts RSS Extensions (itunes:episode)](https://help.apple.com/itc/podcasts_connect/#/itcb54353390)** — De-facto podcast metadata standard. Our episodeNumber/seasonNumber/ durationMs = itunes:episode/itunes:season/itunes:duration.
- **[schema.org/PodcastEpisode](https://schema.org/PodcastEpisode)** — Our series ≈ partOfSeries (PodcastSeries); transcribe ≈ transcript; guest ≈ actor.
- **[Podcast Namespace (podcast:*)](https://podcastindex.org/namespace/1.0)** — Modern open extension to RSS. Covers our guest, season, episode, and transcript relations via podcast:person, podcast:season, etc.
