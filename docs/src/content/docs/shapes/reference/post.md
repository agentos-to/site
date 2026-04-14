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
| `postedBy` | [`account`](/docs/shapes/reference/account/) |
| `publish` | [`community`](/docs/shapes/reference/community/) |
| `repliesTo` | [`post`](/docs/shapes/reference/post/) |
| `replies` | [`post[]`](/docs/shapes/reference/post/) |
| `contains` | [`video[]`](/docs/shapes/reference/video/) |
| `media` | [`image[]`](/docs/shapes/reference/image/) |
| `attachment` | [`file[]`](/docs/shapes/reference/file/) |

## Used as a base by

- [`review`](/docs/shapes/reference/review/)

## Skills that produce this shape

- [hackernews](/docs/skills/reference/media/hackernews/) — `list_posts`, `search_posts`, `comments_post`
- [hackernews](/docs/skills/reference/media/hackernews/) — `get_post`
- [youtube](/docs/skills/reference/media/youtube/) — `list_posts`
- [moltbook](/docs/skills/reference/media/moltbook/) — `list_posts`, `get_feed`, `list_comments`
- [moltbook](/docs/skills/reference/media/moltbook/) — `get_post`
- [reddit](/docs/skills/reference/media/reddit/) — `search_posts`, `list_posts`, `comments_post`
- [reddit](/docs/skills/reference/media/reddit/) — `get_post`
