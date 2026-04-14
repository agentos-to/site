---
title: channel
description: "A content channel — typically a YouTube channel. Videos are uploaded to channels."
sidebar:
  label: channel
---

A content channel — typically a YouTube channel. Videos are uploaded to channels.

Example sources: YouTube

| Metadata | Value |
|---|---|
| **Plural** | `channels` |
| **Identity** | `platform`, `id` |

## Fields

| Field | Type |
|---|---|
| `banner` | `url` |

## Relations

| Relation | Target |
|---|---|
| `platform` | [`product`](/docs/shapes/reference/product/) |

## Skills that produce this shape

- [youtube](/docs/skills/reference/media/youtube/) — `get_channel`, `get_avatar_channel`
