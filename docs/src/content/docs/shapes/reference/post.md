---
title: post
description: "A piece of published content — a Reddit submission, HN story, YouTube upload,"
sidebar:
  label: post
---

A piece of published content — a Reddit submission, HN story, YouTube upload,
tweet, etc. Posts can contain media (videos, images, files). A comment is
just a post that replies_to another post. Reviews extend post via `also`.

| Metadata | Value |
|---|---|
| **Plural** | `posts` |
| **Subtitle field** | `author` |
| **Identity** | `platform`, `id` |

## Fields

| Field | Type |
|---|---|
| `externalUrl` | `url` |
| `postType` | `string` |

## Relations

| Relation | Target |
|---|---|
| `postedBy` | [`account`](/docs/shapes/reference/account/) |
| `publish` | [`community`](/docs/shapes/reference/community/) |
| `repliesTo` | [`post`](/docs/shapes/reference/post/) |
| `replies` | [`post[]`](/docs/shapes/reference/post/) |
| `contains` | [`video[]`](/docs/shapes/reference/video/) |
| `media` | [`image[]`](/docs/shapes/reference/image/) |
| `attachment` | [`file[]`](/docs/shapes/reference/file/) |

## Used as a base by

- [`review`](/docs/shapes/reference/review/)

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/shapes/shape-design-principles/) for how prior art informs shape design.

- **[ActivityStreams 2.0 (Note/Article + Create)](https://www.w3.org/TR/activitystreams-vocabulary/)** — Fediverse post model. Our postedBy ≈ actor/attributedTo; publish(community) ≈ audience/to; repliesTo/replies ≈ inReplyTo/replies; media/attachment ≈ attachment.
- **[OpenGraph protocol](https://ogp.me/)** — How posts surface when linked. Our externalUrl + media[] correspond to og:url and og:image/og:video; postType loosely parallels og:type (article, video).
- **[ATProto app.bsky.feed.post](https://atproto.com/lexicons/app-bsky-feed)** — Modern practical lexicon. Our repliesTo ≈ reply.parent; media ≈ embed.images; externalUrl ≈ embed.external.

## Skills that produce this shape

- [hackernews](/docs/skills/reference/media/hackernews/) — `list_posts`, `search_posts`, `comments_post`, `get_post`
- [youtube](/docs/skills/reference/media/youtube/) — `list_posts`
- [moltbook](/docs/skills/reference/media/moltbook/) — `list_posts`, `get_feed`, `list_comments`, `get_post`
- [reddit](/docs/skills/reference/media/reddit/) — `search_posts`, `list_posts`, `comments_post`, `get_post`
