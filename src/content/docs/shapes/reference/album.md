---
title: album
description: "A curated collection of images produced by the engine or a skill."
sidebar:
  label: album
---

A curated collection of images produced by the engine or a skill.
The engine seeds system albums (e.g. "Wallpapers") at boot; skills
may produce additional albums for photo libraries, screenshots, etc.

Albums group images; the `image --add_to--> album` edge is the reverse
of a user-facing "add to album" action. Membership is immutable once
the link is made (delete the edge to remove an image).

| Metadata | Value |
|---|---|
| **Plural** | `albums` |
| **Subtitle field** | `id` |
| **Identity** | `id` |

## Fields

| Field | Type |
|---|---|
| `id` | `string` |

## Relations

| Relation | Target |
|---|---|
| `contains` | [`image[]`](/shapes/reference/image/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[Apple Photos Album / IPTC PhotoMetadata](https://www.iptc.org/std/photometadata/specification/IPTC-PhotoMetadata)** — Albums are the simplest photo-grouping primitive. No EXIF, no date range — just a named bucket. IPTC's "Album" PMV is the de-facto interchange format for this.
