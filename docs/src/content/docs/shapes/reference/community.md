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
| `platform` | [`product`](/docs/shapes/reference/product/) |

## Skills that produce this shape

- [moltbook](/docs/skills/reference/media/moltbook/) — `list_communities`
- [moltbook](/docs/skills/reference/media/moltbook/) — `get_community`, `create_community`
- [facebook](/docs/skills/reference/media/facebook/) — `get_community`
- [reddit](/docs/skills/reference/media/reddit/) — `get_community`
- [reddit](/docs/skills/reference/media/reddit/) — `search_communities`
