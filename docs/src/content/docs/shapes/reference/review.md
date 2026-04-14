---
title: review
description: "A user review of a product. Reviews are also posts, so they carry engagement metrics."
sidebar:
  label: review
---

A user review of a product. Reviews are also posts, so they carry engagement metrics.

| Metadata | Value |
|---|---|
| **Plural** | `reviews` |
| **Subtitle field** | `author` |
| **Also** | [`post`](/docs/shapes/reference/post/) |

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
| `reviews` | [`product`](/docs/shapes/reference/product/) |
| `postedBy` | [`account`](/docs/shapes/reference/account/) |

## Inherited

From [`post`](/docs/shapes/reference/post/):

| Field | Type |
|---|---|
| `externalUrl` | `url` |
| `postType` | `string` |

| Relation | Target |
|---|---|
| `attachment` | [`file[]`](/docs/shapes/reference/file/) |
| `contains` | [`video[]`](/docs/shapes/reference/video/) |
| `media` | [`image[]`](/docs/shapes/reference/image/) |
| `publish` | [`community`](/docs/shapes/reference/community/) |
| `replies` | [`post[]`](/docs/shapes/reference/post/) |
| `repliesTo` | [`post`](/docs/shapes/reference/post/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Review](https://schema.org/Review)** — Our rating ≈ reviewRating.ratingValue; ratingMax ≈ bestRating; reviews = itemReviewed; isVerified has no direct property (extension).
- **[schema.org/AggregateRating](https://schema.org/AggregateRating)** — For product review aggregates. Our rating/ratingMax map to ratingValue/bestRating; reviewCount is inherited when computed.

## Skills that produce this shape

- [goodreads](/docs/skills/reference/media/goodreads/) — `list_book_reviews`, `list_reviews`
