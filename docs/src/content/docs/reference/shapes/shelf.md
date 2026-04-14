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
| **Also** | [`list`](/docs/reference/shapes/list/) |

## Fields

| Field | Type |
|---|---|
| `isExclusive` | `boolean` |

## Relations

| Relation | Target |
|---|---|
| `contains` | [`book[]`](/docs/reference/shapes/book/) |

## Inherited

From [`list`](/docs/reference/shapes/list/):

| Field | Type |
|---|---|
| `isDefault` | `boolean` |
| `isPublic` | `boolean` |
| `listId` | `string` |
| `listType` | `string` |
| `privacy` | `string` |

| Relation | Target |
|---|---|
| `belongsTo` | [`account`](/docs/reference/shapes/account/) |
| `platform` | [`product`](/docs/reference/shapes/product/) |

## Skills that produce this shape

- [goodreads](/docs/reference/skills/media/goodreads/) — `list_shelves`
