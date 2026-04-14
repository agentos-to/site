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
| `platform` | [`product`](/docs/shapes/reference/product/) |
| `belongsTo` | [`account`](/docs/shapes/reference/account/) |
| `contains` | [`product[]`](/docs/shapes/reference/product/) |

## Used as a base by

- [`playlist`](/docs/shapes/reference/playlist/)
- [`shelf`](/docs/shapes/reference/shelf/)

## Skills that produce this shape

- [amazon](/docs/skills/reference/logistics/amazon/) — `list_lists`
- [amazon](/docs/skills/reference/logistics/amazon/) — `get_list`
