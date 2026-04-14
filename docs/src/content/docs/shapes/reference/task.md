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

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/ontology/shape-design-principles/) for how prior art informs shape design.

- **[GitHub REST API — Issues](https://docs.github.com/en/rest/issues/issues)** — Direct source. Our remoteId/state/labels/assignedTo/parent/ children/blockedBy/blocks map to GitHub Issue + sub-issues + task-list tracking.
- **[Linear GraphQL API — Issue](https://developers.linear.app/docs/graphql/working-with-the-graphql-api)** — Practical canonical. Our priority/state/project/targetDate align with Linear's Issue model exactly.
- **[Todoist REST API v2 — Tasks](https://developer.todoist.com/rest/v2/)** — Consumer-grade task model. Our startedAt/targetDate ≈ created_at/due; labels match directly.

## Skills that produce this shape

- [todoist](/docs/skills/reference/productivity/todoist/) — `list_tasks`, `list_all_tasks`, `filter_task`
- [todoist](/docs/skills/reference/productivity/todoist/) — `get_task`, `create_task`, `update_task`, `move_task`
- [linear](/docs/skills/reference/dev/linear/) — `list_tasks`
- [linear](/docs/skills/reference/dev/linear/) — `get_task`, `create_task`, `update_task`
- [github](/docs/skills/reference/dev/github/) — `list_tasks`
- [github](/docs/skills/reference/dev/github/) — `get_task`
