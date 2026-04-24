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
| **Also** | [`post`](/shapes/reference/post/) |

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
| `reviews` | [`product`](/shapes/reference/product/) |
| `postedBy` | [`account`](/shapes/reference/account/) |

## Inherited

From [`post`](/shapes/reference/post/):

| Field | Type |
|---|---|
| `commentCount` | `integer` |
| `community` | `string` |
| `externalUrl` | `url` |
| `postType` | `string` |
| `score` | `integer` |

| Relation | Target |
|---|---|
| `at` | [`actor`](/shapes/reference/actor/) |
| `attachment` | [`file[]`](/shapes/reference/file/) |
| `contains` | [`video[]`](/shapes/reference/video/) |
| `media` | [`image[]`](/shapes/reference/image/) |
| `publish` | [`community`](/shapes/reference/community/) |
| `replies` | [`post[]`](/shapes/reference/post/) |
| `repliesTo` | [`post`](/shapes/reference/post/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Review](https://schema.org/Review)** — Our rating ≈ reviewRating.ratingValue; ratingMax ≈ bestRating; reviews = itemReviewed; isVerified has no direct property (extension).
- **[schema.org/AggregateRating](https://schema.org/AggregateRating)** — For product review aggregates. Our rating/ratingMax map to ratingValue/bestRating; reviewCount is inherited when computed.

## Skills that produce this shape

- [goodreads](/skills/reference/media/goodreads/) — `list_book_reviews`, `list_reviews`
