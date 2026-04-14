---
title: group
description: "A group or community — online group, reading group, etc."
sidebar:
  label: group
---

A group or community — online group, reading group, etc.

Example sources: Goodreads

| Metadata | Value |
|---|---|
| **Plural** | `groups` |
| **Subtitle field** | `category` |
| **Identity** | `platform`, `id` |

## Fields

| Field | Type |
|---|---|
| `memberCount` | `integer` |
| `category` | `string` |

## Skills that produce this shape

- [goodreads](/docs/reference/skills/media/goodreads/) — `list_groups`
