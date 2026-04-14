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

Example sources: agent output (claude-code, cursor), skill runs, manual creation

| Metadata | Value |
|---|---|
| **Plural** | `reports` |
| **Subtitle field** | `reportType` |
| **Also** | [`document`](/docs/shapes/reference/document/) |

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
| `commissionedBy` | [`actor`](/docs/shapes/reference/actor/) |
| `relatedSpecs` | [`spec[]`](/docs/shapes/reference/spec/) |

## Inherited

From [`document`](/docs/shapes/reference/document/):

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
| `attachedTo` | [`message`](/docs/shapes/reference/message/) |
| `author` | [`actor`](/docs/shapes/reference/actor/) |
| `citedBy` | [`document[]`](/docs/shapes/reference/document/) |
| `references` | [`document[]`](/docs/shapes/reference/document/) |
| `repository` | [`repository`](/docs/shapes/reference/repository/) |
