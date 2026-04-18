---
title: community
description: "An online community — a subreddit, Facebook group, or similar."
sidebar:
  label: community
---

An online community — a subreddit, Facebook group, or similar.

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
| `platform` | [`product`](/shapes/reference/product/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[ActivityPub Group Actor](https://www.w3.org/TR/activitypub/)** — AP Group Actor models shared-inbox communities (Lemmy, Kbin, Mbin). Our privacy ≈ audience/to visibility.
- **[schema.org/Organization](https://schema.org/Organization)** — A community-as-organization is a loose fit; privacy has no direct schema.org property.
- **[Reddit API — Subreddit](https://www.reddit.com/dev/api/#GET_subreddits_where)** — Practical source. Our privacy ≈ subreddit_type (public/private/ restricted); text ≈ public_description.

## Skills that produce this shape

- [moltbook](/skills/reference/media/moltbook/) — `list_communities`, `get_community`, `create_community`
- [facebook](/skills/reference/media/facebook/) — `get_community`
- [reddit](/skills/reference/media/reddit/) — `get_community`, `search_communities`
