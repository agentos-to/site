---
title: review
description: "A user review of a product. Reviews are also posts, so they carry engagement metrics."
sidebar:
  label: review
---

A user review of a product. Reviews are also posts, so they carry engagement metrics.

Example sources: Goodreads, Amazon

| Metadata | Value |
|---|---|
| **Plural** | `reviews` |
| **Subtitle field** | `author` |
| **Also** | [`post`](/docs/reference/shapes/post/) |

## Fields

| Field | Type |
|---|---|
| `rating` | `number` |
| `ratingMax` | `number` |
| `tags` | `string[]` |
| `isVerified` | `boolean` |

## Relations

| Relation | Target |
|---|---|
| `reviews` | [`product`](/docs/reference/shapes/product/) |
| `postedBy` | [`account`](/docs/reference/shapes/account/) |

## Inherited

From [`post`](/docs/reference/shapes/post/):

| Field | Type |
|---|---|
| `externalUrl` | `url` |
| `postType` | `string` |

| Relation | Target |
|---|---|
| `attachment` | [`file[]`](/docs/reference/shapes/file/) |
| `contains` | [`video[]`](/docs/reference/shapes/video/) |
| `media` | [`image[]`](/docs/reference/shapes/image/) |
| `publish` | [`community`](/docs/reference/shapes/community/) |
| `replies` | [`post[]`](/docs/reference/shapes/post/) |
| `repliesTo` | [`post`](/docs/reference/shapes/post/) |

## Skills that produce this shape

- [goodreads](/docs/reference/skills/media/goodreads/) — `list_book_reviews`, `list_reviews`
