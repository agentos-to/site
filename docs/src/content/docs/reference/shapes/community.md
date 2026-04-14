---
title: community
description: "An online community — a subreddit, Facebook group, or similar."
sidebar:
  label: community
---

An online community — a subreddit, Facebook group, or similar.

Example sources: Reddit, Facebook

| | |
|---|---|
| **Plural** | `communities` |
| **Subtitle field** | `text` |
| **Identity** | `platform`, `id` |

## Fields

| Field | Type |
|---|---|
| `privacy` | `string` |

## Relations

| Relation | Target |
|---|---|
| `platform` | [`product`](/docs/reference/shapes/product/) |

## Skills that produce this shape

- [moltbook](/docs/reference/skills/moltbook/) — `list_communities`
- [moltbook](/docs/reference/skills/moltbook/) — `get_community`, `create_community`
- [facebook](/docs/reference/skills/facebook/) — `get_community`
- [reddit](/docs/reference/skills/reddit/) — `get_community`
- [reddit](/docs/reference/skills/reddit/) — `search_communities`
