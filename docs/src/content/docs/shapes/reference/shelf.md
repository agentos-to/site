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

## Skills that produce this shape

- [goodreads](/docs/skills/reference/media/goodreads/) — `list_shelves`
