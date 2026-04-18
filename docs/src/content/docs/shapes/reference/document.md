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

| Metadata | Value |
|---|---|
| **Plural** | `documents` |
| **Subtitle field** | `author` |
| **Also** | [`file`](/shapes/reference/file/) |

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
| `author` | [`actor`](/shapes/reference/actor/) |
| `references` | [`document[]`](/shapes/reference/document/) |
| `citedBy` | [`document[]`](/shapes/reference/document/) |

## Inherited

From [`file`](/shapes/reference/file/):

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
| `attachedTo` | [`message`](/shapes/reference/message/) |
| `repository` | [`repository`](/shapes/reference/repository/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[Dublin Core Metadata Initiative](https://www.dublincore.org/specifications/dublin-core/dces/)** — Our contentType ≈ dc:format; language = dc:language; author = dc:creator; references/citedBy ≈ dc:relation.
- **[schema.org/DigitalDocument](https://schema.org/DigitalDocument)** — Our abstract ≈ abstract; tableOfContents = hasPart or accessModeSufficient; wordCount = wordCount.
- **[W3C Web Annotation Data Model](https://www.w3.org/TR/annotation-model/)** — Our references[]/citedBy[] are annotation target/body relationships between documents.
