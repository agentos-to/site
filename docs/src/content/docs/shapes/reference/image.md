---
title: image
description: "An image file. Photos, screenshots, diagrams, artwork."
sidebar:
  label: image
---

An image file. Photos, screenshots, diagrams, artwork.

| Metadata | Value |
|---|---|
| **Plural** | `images` |
| **Also** | [`file`](/shapes/reference/file/) |

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

From [`file`](/shapes/reference/file/):

| Field | Type |
|---|---|
| `encoding` | `string` |
| `filename` | `string` |
| `kind` | `string` |
| `lineCount` | `integer` |
| `mimeType` | `string` |
| `path` | `string` |
| `sha` | `string` |
| `size` | `integer` |

| Relation | Target |
|---|---|
| `attachedTo` | [`message`](/shapes/reference/message/) |
| `repository` | [`repository`](/shapes/reference/repository/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/ImageObject](https://schema.org/ImageObject)** — Our width/height = width/height; format ≈ encodingFormat; altText = caption/accessibilityCaption.
- **[IANA Media Types (image/*)](https://www.iana.org/assignments/media-types/media-types.xhtml#image)** — Our format values (PNG, JPEG, WebP, SVG) align with registered image/* media types.
- **[Exif 2.3 (JEITA CP-3451)](https://www.cipa.jp/std/documents/e/DC-008-Translation-2019-E.pdf)** — Source of most image metadata fields. width/height come from Exif PixelXDimension/PixelYDimension.

## Skills that produce this shape

- [macos-control](/skills/reference/macos/macos-control/) — `screenshot_display`, `screenshot_window`
