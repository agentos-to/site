---
title: report
description: "A report — structured output from a research task, analysis, or agent run."
sidebar:
  label: report
---

A report — structured output from a research task, analysis, or agent run.
Reports are first-class graph entities: they link to what was studied
(subject), who commissioned the work (commissioned_by), and which specs
the findings inform (related_specs).

report_type drives how the UI surfaces the entity:
research    — open-ended exploration, summarizes what was found
analysis    — systematic breakdown of a specific artifact or dataset
comparison  — side-by-side evaluation of multiple options
audit       — compliance or quality check against known criteria
review      — qualitative assessment (code review, skill review, etc.)

| Metadata | Value |
|---|---|
| **Plural** | `reports` |
| **Subtitle field** | `reportType` |
| **Also** | [`document`](/shapes/reference/document/) |

## Fields

| Field | Type |
|---|---|
| `reportType` | `string` |
| `methodology` | `text` |
| `findings` | `text` |
| `recommendations` | `text` |
| `confidence` | `number` |
| `dataSources` | `string[]` |
| `subjectId` | `string` |

## Relations

| Relation | Target |
|---|---|
| `commissionedBy` | [`actor`](/shapes/reference/actor/) |
| `relatedSpecs` | [`spec[]`](/shapes/reference/spec/) |

## Inherited

From [`document`](/shapes/reference/document/):

| Field | Type |
|---|---|
| `abstract` | `text` |
| `contentType` | `string` |
| `encoding` | `string` |
| `filename` | `string` |
| `format` | `string` |
| `kind` | `string` |
| `language` | `string` |
| `lineCount` | `integer` |
| `mimeType` | `string` |
| `path` | `string` |
| `sha` | `string` |
| `size` | `integer` |
| `tableOfContents` | `text` |
| `wordCount` | `integer` |

| Relation | Target |
|---|---|
| `attachedTo` | [`message`](/shapes/reference/message/) |
| `author` | [`actor`](/shapes/reference/actor/) |
| `citedBy` | [`document[]`](/shapes/reference/document/) |
| `references` | [`document[]`](/shapes/reference/document/) |
| `repository` | [`repository`](/shapes/reference/repository/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Report](https://schema.org/Report)** — Our reportType ≈ reportNumber/about; methodology ≈ description; findings = text; recommendations has no direct peer.
- **[W3C DCAT 3 (Data Catalog)](https://www.w3.org/TR/vocab-dcat-3/)** — Our dataSources[] map to dcat:distribution/prov:used; methodology ≈ dcterms:description.
- **[PROV-O (W3C Provenance)](https://www.w3.org/TR/prov-o/)** — commissionedBy aligns with prov:wasAttributedTo; dataSources with prov:used. Canonical for auditable agent output.
