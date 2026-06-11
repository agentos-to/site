---
title: shelf
description: "A bookshelf. Shelves are lists that contain books instead of generic products."
sidebar:
  label: shelf
---

A bookshelf. Shelves are lists that contain books instead of generic products.

| Metadata | Value |
|---|---|
| **Plural** | `shelves` |
| **Subtitle field** | `isExclusive` |
| **Also** | [`list`](/shapes/reference/list/) |

## Fields

| Field | Type |
|---|---|
| `isExclusive` | `boolean` |

## Relations

| Relation | Target |
|---|---|
| `contains` | [`book[]`](/shapes/reference/book/) |

## Inherited

From [`list`](/shapes/reference/list/):

| Field | Type |
|---|---|
| `arrangement` | `string` |
| `default_view` | `string` |
| `icon_size` | `integer` |
| `isDefault` | `boolean` |
| `isPublic` | `boolean` |
| `itemCount` | `integer` |
| `listId` | `string` |
| `listType` | `string` |
| `member_shape` | `string` |
| `ordering_mode` | `string` |
| `path` | `string` |
| `privacy` | `string` |
| `sort_by` | `string` |

| Relation | Target |
|---|---|
| `at_namespace` | [`actor`](/shapes/reference/actor/) |
| `backed_by` | [`image`](/shapes/reference/image/) |
| `belongs_to` | [`account`](/shapes/reference/account/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[Goodreads API — Shelves](https://www.goodreads.com/api)** — Direct source. Our isExclusive maps to Goodreads' "exclusive shelves" (read, to-read, currently-reading).
- **[schema.org/ItemList (bookshelf)](https://schema.org/ItemList)** — Generic collection peer. contains(book[]) ≈ itemListElement.

## Skills that produce this shape

- [goodreads](/skills/reference/media/goodreads/) — `list_shelves`
