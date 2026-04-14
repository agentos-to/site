---
title: document
description: "A document — any human-readable text content with structure and authorship."
sidebar:
  label: document
---

A document — any human-readable text content with structure and authorship.
Base type for reports, manuscripts, briefs, whitepapers, analyses.
article, note, and webpage are siblings (not children) for now; they may
gain also: [document] in a future migration once the shape stabilizes.

Example sources: filesystem, agent output, skill results

| Metadata | Value |
|---|---|
| **Plural** | `documents` |
| **Subtitle field** | `author` |
| **Also** | [`file`](/docs/reference/shapes/file/) |

## Fields

| Field | Type |
|---|---|
| `contentType` | `string` |
| `language` | `string` |
| `wordCount` | `integer` |
| `abstract` | `text` |
| `tableOfContents` | `text` |

## Relations

| Relation | Target |
|---|---|
| `author` | [`actor`](/docs/reference/shapes/actor/) |
| `references` | [`document[]`](/docs/reference/shapes/document/) |
| `citedBy` | [`document[]`](/docs/reference/shapes/document/) |

## Inherited

From [`file`](/docs/reference/shapes/file/):

| Field | Type |
|---|---|
| `encoding` | `string` |
| `filename` | `string` |
| `format` | `string` |
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

## Used as a base by

- [`report`](/docs/reference/shapes/report/)
