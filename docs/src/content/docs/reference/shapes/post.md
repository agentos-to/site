---
title: post
description: "A piece of published content — a Reddit submission, HN story, YouTube upload,"
sidebar:
  label: post
---

A piece of published content — a Reddit submission, HN story, YouTube upload,
tweet, etc. Posts can contain media (videos, images, files). A comment is
just a post that replies_to another post. Reviews extend post via `also`.

Example sources: Reddit, Hacker News, YouTube, Moltbook

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
| `postedBy` | [`account`](/docs/reference/shapes/account/) |
| `publish` | [`community`](/docs/reference/shapes/community/) |
| `repliesTo` | [`post`](/docs/reference/shapes/post/) |
| `replies` | [`post[]`](/docs/reference/shapes/post/) |
| `contains` | [`video[]`](/docs/reference/shapes/video/) |
| `media` | [`image[]`](/docs/reference/shapes/image/) |
| `attachment` | [`file[]`](/docs/reference/shapes/file/) |

## Used as a base by

- [`review`](/docs/reference/shapes/review/)

## Skills that produce this shape

- [hackernews](/docs/reference/skills/media/hackernews/) — `list_posts`, `search_posts`, `comments_post`
- [hackernews](/docs/reference/skills/media/hackernews/) — `get_post`
- [youtube](/docs/reference/skills/media/youtube/) — `list_posts`
- [moltbook](/docs/reference/skills/media/moltbook/) — `list_posts`, `get_feed`, `list_comments`
- [moltbook](/docs/reference/skills/media/moltbook/) — `get_post`
- [reddit](/docs/reference/skills/media/reddit/) — `search_posts`, `list_posts`, `comments_post`
- [reddit](/docs/reference/skills/media/reddit/) — `get_post`
