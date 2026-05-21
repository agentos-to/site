---
title: image
description: "An image file. Photos, screenshots, diagrams, artwork."
sidebar:
  label: image
---

An image file. Photos, screenshots, diagrams, artwork.

An image is BOTH a creative_work (the photograph / illustration is the
work — its author, publisher, license, datePublished come from there)
AND a file (the bytes on disk, with a specific format and dimensions).

| Metadata | Value |
|---|---|
| **Plural** | `images` |
| **Subtitle field** | `format` |
| **Identity (any)** | `url` |
| **Also** | [`creative_work`](/shapes/reference/creative_work/) · [`file`](/shapes/reference/file/) |

## Fields

| Field | Type |
|---|---|
| `width` | `integer` |
| `height` | `integer` |
| `format` | `string` |
| `altText` | `string` |
| `appName` | `string` |
| `windowId` | `integer` |
| `displayId` | `integer` |
| `displayIndex` | `integer` |

## Inherited

From [`creative_work`](/shapes/reference/creative_work/) · [`file`](/shapes/reference/file/):

| Field | Type |
|---|---|
| `copyrightYear` | `integer` |
| `coverage` | `string` |
| `dateCreated` | `date` |
| `description` | `string` |
| `encoding` | `string` |
| `filename` | `string` |
| `kind` | `string` |
| `language` | `string` |
| `license` | `string` |
| `lineCount` | `integer` |
| `mimeType` | `string` |
| `path` | `string` |
| `sha` | `string` |
| `size` | `integer` |
| `tags` | `string[]` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/ImageObject](https://schema.org/ImageObject)** — Our width/height = width/height; format ≈ encodingFormat; altText = caption/accessibilityCaption.
- **[IANA Media Types (image/*)](https://www.iana.org/assignments/media-types/media-types.xhtml#image)** — Our format values (PNG, JPEG, WebP, SVG) align with registered image/* media types.
- **[Exif 2.3 (JEITA CP-3451)](https://www.cipa.jp/std/documents/e/DC-008-Translation-2019-E.pdf)** — Source of most image metadata fields. width/height come from Exif PixelXDimension/PixelYDimension.

## Skills that produce this shape

- [macos-control](/skills/reference/macos/macos-control/) — `screenshot_display`, `screenshot_window`
