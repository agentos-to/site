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
| `assignedTo` | [`person`](/docs/reference/shapes/person/) |
| `project` | [`project`](/docs/reference/shapes/project/) |
| `repository` | [`repository`](/docs/reference/shapes/repository/) |
| `parent` | [`task`](/docs/reference/shapes/task/) |
| `children` | [`task[]`](/docs/reference/shapes/task/) |
| `blockedBy` | [`task[]`](/docs/reference/shapes/task/) |
| `blocks` | [`task[]`](/docs/reference/shapes/task/) |

## Used as a base by

- [`spec`](/docs/reference/shapes/spec/)

## Skills that produce this shape

- [todoist](/docs/reference/skills/productivity/todoist/) — `list_tasks`, `list_all_tasks`, `filter_task`
- [todoist](/docs/reference/skills/productivity/todoist/) — `get_task`, `create_task`, `update_task`, `move_task`
- [linear](/docs/reference/skills/dev/linear/) — `list_tasks`
- [linear](/docs/reference/skills/dev/linear/) — `get_task`, `create_task`, `update_task`
- [github](/docs/reference/skills/dev/github/) — `list_tasks`
- [github](/docs/reference/skills/dev/github/) — `get_task`
