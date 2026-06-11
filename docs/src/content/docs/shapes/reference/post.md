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
| **Identity** | `at`, `id` |

## Fields

| Field | Type |
|---|---|
| `externalUrl` | `url` |
| `postType` | `string` |
| `score` | `integer` |
| `commentCount` | `integer` |
| `community` | `string` |

## Relations

| Relation | Target |
|---|---|
| `at_namespace` | [`actor`](/shapes/reference/actor/) |
| `posted_by` | [`account`](/shapes/reference/account/) |
| `published_in` | [`community`](/shapes/reference/community/) |
| `replies_to` | [`post`](/shapes/reference/post/) |
| `replies` | [`post[]`](/shapes/reference/post/) |
| `contains` | [`video[]`](/shapes/reference/video/) |
| `shows` | [`image[]`](/shapes/reference/image/) |

## Used as a base by

- [`review`](/shapes/reference/review/)

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[ActivityStreams 2.0 (Note/Article + Create)](https://www.w3.org/TR/activitystreams-vocabulary/)** — Fediverse post model. Our postedBy ≈ actor/attributedTo; publish(community) ≈ audience/to; repliesTo/replies ≈ inReplyTo/replies; media/attachment ≈ attachment.
- **[OpenGraph protocol](https://ogp.me/)** — How posts surface when linked. Our externalUrl + media[] correspond to og:url and og:image/og:video; postType loosely parallels og:type (article, video).
- **[ATProto app.bsky.feed.post](https://atproto.com/lexicons/app-bsky-feed)** — Modern practical lexicon. Our repliesTo ≈ reply.parent; media ≈ embed.images; externalUrl ≈ embed.external.

## Apps that produce this shape

- [hackernews](/apps/reference/media/hackernews/) — `list_posts`, `search_posts`, `comments_post`, `get_post`
- [youtube](/apps/reference/media/youtube/) — `list_posts`
- [moltbook](/apps/reference/media/moltbook/) — `list_posts`, `get_feed`, `list_comments`, `get_post`
- [reddit](/apps/reference/media/reddit/) — `search_posts`, `list_posts`, `comments_post`, `get_post`
