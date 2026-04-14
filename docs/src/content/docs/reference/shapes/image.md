---
title: image
description: "An image file. Photos, screenshots, diagrams, artwork."
sidebar:
  label: image
---

An image file. Photos, screenshots, diagrams, artwork.

Example sources: macOS screenshots, email attachments, web scraping

| | |
|---|---|
| **Plural** | `images` |
| **Also** | [`file`](/docs/reference/shapes/file/) |

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

From [`file`](/docs/reference/shapes/file/):

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
| `attachedTo` | [`message`](/docs/reference/shapes/message/) |
| `repository` | [`repository`](/docs/reference/shapes/repository/) |

## Skills that produce this shape

- [macos-control](/docs/reference/skills/macos-control/) — `screenshot_display`, `screenshot_window`
