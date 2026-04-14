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

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/ontology/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/MusicPlaylist / ItemList](https://schema.org/MusicPlaylist)** — Our contains(video[]) ≈ track/itemListElement. We generalize beyond music to any ordered media list.
- **[YouTube Data API — Playlist](https://developers.google.com/youtube/v3/docs/playlists)** — Practical source. Playlist = ordered Video collection — inherits list identity semantics.
