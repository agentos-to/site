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
| **Also** | [`file`](/docs/shapes/reference/file/) |

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
| `author` | [`actor`](/docs/shapes/reference/actor/) |
| `references` | [`document[]`](/docs/shapes/reference/document/) |
| `citedBy` | [`document[]`](/docs/shapes/reference/document/) |

## Inherited

From [`file`](/docs/shapes/reference/file/):

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
| `attachedTo` | [`message`](/docs/shapes/reference/message/) |
| `repository` | [`repository`](/docs/shapes/reference/repository/) |

## Used as a base by

- [`report`](/docs/shapes/reference/report/)
