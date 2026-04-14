---
title: shelf
description: "A bookshelf. Shelves are lists that contain books instead of generic products."
sidebar:
  label: shelf
---

A bookshelf. Shelves are lists that contain books instead of generic products.

Example sources: Goodreads

| Metadata | Value |
|---|---|
| **Plural** | `shelves` |
| **Also** | [`list`](/docs/shapes/reference/list/) |

## Fields

| Field | Type |
|---|---|
| `isExclusive` | `boolean` |

## Relations

| Relation | Target |
|---|---|
| `contains` | [`book[]`](/docs/shapes/reference/book/) |

## Inherited

From [`list`](/docs/shapes/reference/list/):

| Field | Type |
|---|---|
| `isDefault` | `boolean` |
| `isPublic` | `boolean` |
| `listId` | `string` |
| `listType` | `string` |
| `privacy` | `string` |

| Relation | Target |
|---|---|
| `belongsTo` | [`account`](/docs/shapes/reference/account/) |
| `platform` | [`product`](/docs/shapes/reference/product/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/ontology/shape-design-principles/) for how prior art informs shape design.

- **[Goodreads API — Shelves](https://www.goodreads.com/api)** — Direct source. Our isExclusive maps to Goodreads' "exclusive shelves" (read, to-read, currently-reading).
- **[schema.org/ItemList (bookshelf)](https://schema.org/ItemList)** — Generic collection peer. contains(book[]) ≈ itemListElement.

## Skills that produce this shape

- [goodreads](/docs/skills/reference/media/goodreads/) — `list_shelves`
