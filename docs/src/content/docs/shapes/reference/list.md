---
title: list
description: "A generic collection of items. Base type for shelf (books) and playlist (videos)."
sidebar:
  label: list
---

A generic collection of items. Base type for shelf (books) and playlist (videos).

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
| `platform` | [`product`](/shapes/reference/product/) |
| `belongsTo` | [`account`](/shapes/reference/account/) |
| `contains` | [`product[]`](/shapes/reference/product/) |

## Used as a base by

- [`playlist`](/shapes/reference/playlist/)
- [`shelf`](/shapes/reference/shelf/)

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/ItemList](https://schema.org/ItemList)** — Our listType ≈ itemListOrder; contains ≈ itemListElement; isPublic ≈ publicAccess.
- **[ActivityStreams 2.0 Collection / OrderedCollection](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-collection)** — Our contains[] ≈ items; isDefault has no AS2 peer (platform-level concept).

## Skills that produce this shape

- [amazon](/skills/reference/logistics/amazon/) — `list_lists`, `get_list`
