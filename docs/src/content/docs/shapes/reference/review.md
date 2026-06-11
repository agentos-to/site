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
| `posted_by` | [`account`](/shapes/reference/account/) |

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
| `at_namespace` | [`actor`](/shapes/reference/actor/) |
| `contains` | [`video[]`](/shapes/reference/video/) |
| `published_in` | [`community`](/shapes/reference/community/) |
| `replies` | [`post[]`](/shapes/reference/post/) |
| `replies_to` | [`post`](/shapes/reference/post/) |
| `shows` | [`image[]`](/shapes/reference/image/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Review](https://schema.org/Review)** — Our rating ≈ reviewRating.ratingValue; ratingMax ≈ bestRating; reviews = itemReviewed; isVerified has no direct property (extension).
- **[schema.org/AggregateRating](https://schema.org/AggregateRating)** — For product review aggregates. Our rating/ratingMax map to ratingValue/bestRating; reviewCount is inherited when computed.

## Apps that produce this shape

- [goodreads](/apps/reference/media/goodreads/) — `list_book_reviews`, `list_reviews`
