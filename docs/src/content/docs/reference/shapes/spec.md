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

| | |
|---|---|
| **Plural** | `specs` |
| **Subtitle field** | `state` |
| **Also** | [`task`](/docs/reference/shapes/task/) · [`file`](/docs/reference/shapes/file/) |

## Fields

| Field | Type |
|---|---|
| `problem` | `text` |
| `successCriteria` | `text` |

## Relations

| Relation | Target |
|---|---|
| `dependsOn` | [`spec[]`](/docs/reference/shapes/spec/) |
| `supersedes` | [`spec[]`](/docs/reference/shapes/spec/) |

## Inherited

From [`task`](/docs/reference/shapes/task/) · [`file`](/docs/reference/shapes/file/):

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
| `assignedTo` | [`person`](/docs/reference/shapes/person/) |
| `attachedTo` | [`message`](/docs/reference/shapes/message/) |
| `blockedBy` | [`task[]`](/docs/reference/shapes/task/) |
| `blocks` | [`task[]`](/docs/reference/shapes/task/) |
| `children` | [`task[]`](/docs/reference/shapes/task/) |
| `parent` | [`task`](/docs/reference/shapes/task/) |
| `project` | [`project`](/docs/reference/shapes/project/) |
| `repository` | [`repository`](/docs/reference/shapes/repository/) |
