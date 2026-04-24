---
title: podcast
description: "A podcast series. Contains episodes. Not the audio itself — that's on the episode."
sidebar:
  label: podcast
---

A podcast series. Contains episodes. Not the audio itself — that's on the episode.

| Metadata | Value |
|---|---|
| **Plural** | `podcasts` |
| **Subtitle field** | `author` |
| **Identity** | `at`, `id` |

## Fields

| Field | Type |
|---|---|
| `feedUrl` | `url` |

## Relations

| Relation | Target |
|---|---|
| `host` | [`person[]`](/shapes/reference/person/) |
| `at` | [`actor`](/shapes/reference/actor/) |
| `episode` | [`episode[]`](/shapes/reference/episode/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[RSS 2.0 (feed + channel)](https://www.rssboard.org/rss-specification)** — Our feedUrl is a canonical RSS feed URL; episodes relation ≈ channel's item elements.
- **[Apple Podcasts RSS extensions (itunes:*)](https://help.apple.com/itc/podcasts_connect/#/itcb54353390)** — De-facto standard. Our host[] ≈ itunes:author; our series-episode hierarchy aligns with itunes:episode/itunes:season.
- **[Podcast Namespace (podcast:*)](https://podcastindex.org/namespace/1.0)** — Modern open extension. podcast:person covers guests/hosts; podcast:transcript covers our transcribe relation.
