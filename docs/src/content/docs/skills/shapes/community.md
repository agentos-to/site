---
title: community
description: "An online community — a subreddit, Facebook group, or similar."
sidebar:
  label: community
---

An online community — a subreddit, Facebook group, or similar.

Example sources: Reddit, Facebook

| Metadata | Value |
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

- [moltbook](/docs/reference/skills/media/moltbook/) — `list_communities`
- [moltbook](/docs/reference/skills/media/moltbook/) — `get_community`, `create_community`
- [facebook](/docs/reference/skills/media/facebook/) — `get_community`
- [reddit](/docs/reference/skills/media/reddit/) — `get_community`
- [reddit](/docs/reference/skills/media/reddit/) — `search_communities`
