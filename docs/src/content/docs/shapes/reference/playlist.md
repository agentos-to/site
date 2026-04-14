---
title: playlist
description: "A video playlist. Playlists are lists that contain videos instead of products."
sidebar:
  label: playlist
---

A video playlist. Playlists are lists that contain videos instead of products.

Example sources: YouTube

| Metadata | Value |
|---|---|
| **Plural** | `playlists` |
| **Subtitle field** | `text` |
| **Also** | [`list`](/docs/shapes/reference/list/) |

## Relations

| Relation | Target |
|---|---|
| `contains` | [`video[]`](/docs/shapes/reference/video/) |

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
