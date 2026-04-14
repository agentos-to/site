---
title: task
description: "A work item — issue, ticket, or to-do. Supports hierarchy (parent/children)"
sidebar:
  label: task
---

A work item — issue, ticket, or to-do. Supports hierarchy (parent/children)
and dependency tracking (blocked_by/blocks).

Example sources: Linear, Todoist, GitHub

| Metadata | Value |
|---|---|
| **Plural** | `tasks` |
| **Subtitle field** | `state` |
| **Identity** | `platform`, `id` |

## Fields

| Field | Type |
|---|---|
| `remoteId` | `string` |
| `priority` | `integer` |
| `state` | `string` |
| `labels` | `string[]` |
| `startedAt` | `datetime` |
| `targetDate` | `datetime` |

## Relations

| Relation | Target |
|---|---|
| `assignedTo` | [`person`](/docs/shapes/reference/person/) |
| `project` | [`project`](/docs/shapes/reference/project/) |
| `repository` | [`repository`](/docs/shapes/reference/repository/) |
| `parent` | [`task`](/docs/shapes/reference/task/) |
| `children` | [`task[]`](/docs/shapes/reference/task/) |
| `blockedBy` | [`task[]`](/docs/shapes/reference/task/) |
| `blocks` | [`task[]`](/docs/shapes/reference/task/) |

## Used as a base by

- [`spec`](/docs/shapes/reference/spec/)

## Skills that produce this shape

- [todoist](/docs/skills/reference/productivity/todoist/) — `list_tasks`, `list_all_tasks`, `filter_task`
- [todoist](/docs/skills/reference/productivity/todoist/) — `get_task`, `create_task`, `update_task`, `move_task`
- [linear](/docs/skills/reference/dev/linear/) — `list_tasks`
- [linear](/docs/skills/reference/dev/linear/) — `get_task`, `create_task`, `update_task`
- [github](/docs/skills/reference/dev/github/) — `list_tasks`
- [github](/docs/skills/reference/dev/github/) — `get_task`
