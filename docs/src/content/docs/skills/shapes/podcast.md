---
title: podcast
description: "A podcast series. Contains episodes. Not the audio itself — that's on the episode."
sidebar:
  label: podcast
---

A podcast series. Contains episodes. Not the audio itself — that's on the episode.

Example sources: YouTube (some channels are podcasts), future podcast skill

| Metadata | Value |
|---|---|
| **Plural** | `podcasts` |
| **Subtitle field** | `author` |
| **Identity** | `platform`, `id` |

## Fields

| Field | Type |
|---|---|
| `feedUrl` | `url` |

## Relations

| Relation | Target |
|---|---|
| `host` | [`person[]`](/docs/reference/shapes/person/) |
| `platform` | [`product`](/docs/reference/shapes/product/) |
| `episode` | [`episode[]`](/docs/reference/shapes/episode/) |
