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
