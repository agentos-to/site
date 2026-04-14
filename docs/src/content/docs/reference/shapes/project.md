---
title: project
description: "A project that groups tasks. Tasks belong to projects."
sidebar:
  label: project
---

A project that groups tasks. Tasks belong to projects.

Example sources: Linear, Todoist

| | |
|---|---|
| **Plural** | `projects` |
| **Subtitle field** | `state` |
| **Identity** | `platform`, `id` |

## Fields

| Field | Type |
|---|---|
| `state` | `string` |
| `color` | `string` |

## Skills that produce this shape

- [todoist](/docs/reference/skills/todoist/) — `list_projects`
- [linear](/docs/reference/skills/linear/) — `list_projects`
