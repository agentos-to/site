---
title: spec
description: "A spec — a design document describing work to be done."
sidebar:
  label: spec
---

A spec — a design document describing work to be done.
Specs are markdown files with YAML frontmatter in docs/specs/.
State is derived from location: docs/specs/ = active, docs/specs/done/ = done.

Example sources: filesystem (docs/specs/)

| Metadata | Value |
|---|---|
| **Plural** | `specs` |
| **Subtitle field** | `state` |
| **Also** | [`task`](/docs/shapes/reference/task/) · [`file`](/docs/shapes/reference/file/) |

## Fields

| Field | Type |
|---|---|
| `problem` | `text` |
| `successCriteria` | `text` |

## Relations

| Relation | Target |
|---|---|
| `dependsOn` | [`spec[]`](/docs/shapes/reference/spec/) |
| `supersedes` | [`spec[]`](/docs/shapes/reference/spec/) |

## Inherited

From [`task`](/docs/shapes/reference/task/) · [`file`](/docs/shapes/reference/file/):

| Field | Type |
|---|---|
| `encoding` | `string` |
| `filename` | `string` |
| `format` | `string` |
| `kind` | `string` |
| `labels` | `string[]` |
| `lineCount` | `integer` |
| `mimeType` | `string` |
| `path` | `string` |
| `priority` | `integer` |
| `remoteId` | `string` |
| `sha` | `string` |
| `size` | `integer` |
| `startedAt` | `datetime` |
| `state` | `string` |
| `targetDate` | `datetime` |

| Relation | Target |
|---|---|
| `assignedTo` | [`person`](/docs/shapes/reference/person/) |
| `attachedTo` | [`message`](/docs/shapes/reference/message/) |
| `blockedBy` | [`task[]`](/docs/shapes/reference/task/) |
| `blocks` | [`task[]`](/docs/shapes/reference/task/) |
| `children` | [`task[]`](/docs/shapes/reference/task/) |
| `parent` | [`task`](/docs/shapes/reference/task/) |
| `project` | [`project`](/docs/shapes/reference/project/) |
| `repository` | [`repository`](/docs/shapes/reference/repository/) |
