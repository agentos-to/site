---
title: result
description: "A search result — a pointer to something found. Not the thing itself."
sidebar:
  label: result
---

A search result — a pointer to something found. Not the thing itself.
A search might return webpages, products, people, articles — anything.
The result just carries search-specific metadata (when indexed, what type).

Example sources: Brave Search, Exa, Moltbook

| | |
|---|---|
| **Plural** | `results` |
| **Subtitle field** | `url` |

## Fields

| Field | Type |
|---|---|
| `indexedAt` | `datetime` |
| `resultType` | `string` |

## Skills that produce this shape

- [moltbook](/docs/reference/skills/moltbook/) — `search_posts`
- [brave](/docs/reference/skills/brave/) — `search`
- [exa](/docs/reference/skills/exa/) — `search`
