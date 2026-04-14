---
title: list
description: "A generic collection of items. Base type for shelf (books) and playlist (videos)."
sidebar:
  label: list
---

A generic collection of items. Base type for shelf (books) and playlist (videos).

Example sources: Goodreads (via shelf), YouTube (via playlist)

| Metadata | Value |
|---|---|
| **Plural** | `lists` |
| **Identity** | `platform`, `id` |

## Fields

| Field | Type |
|---|---|
| `listId` | `string` |
| `privacy` | `string` |
| `listType` | `string` |
| `isDefault` | `boolean` |
| `isPublic` | `boolean` |

## Relations

| Relation | Target |
|---|---|
| `platform` | [`product`](/docs/reference/shapes/product/) |
| `belongsTo` | [`account`](/docs/reference/shapes/account/) |
| `contains` | [`product[]`](/docs/reference/shapes/product/) |

## Used as a base by

- [`playlist`](/docs/reference/shapes/playlist/)
- [`shelf`](/docs/reference/shapes/shelf/)

## Skills that produce this shape

- [amazon](/docs/reference/skills/logistics/amazon/) — `list_lists`
- [amazon](/docs/reference/skills/logistics/amazon/) — `get_list`
