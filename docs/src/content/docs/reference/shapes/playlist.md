---
title: playlist
description: "A video playlist. Playlists are lists that contain videos instead of products."
sidebar:
  label: playlist
---

A video playlist. Playlists are lists that contain videos instead of products.

Example sources: YouTube

| | |
|---|---|
| **Plural** | `playlists` |
| **Subtitle field** | `text` |
| **Also** | [`list`](/docs/reference/shapes/list/) |

## Relations

| Relation | Target |
|---|---|
| `contains` | [`video[]`](/docs/reference/shapes/video/) |

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
