---
title: project
description: "A project that groups tasks. Tasks belong to projects."
sidebar:
  label: project
---

A project that groups tasks. Tasks belong to projects.

Example sources: Linear, Todoist

| Metadata | Value |
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

- [todoist](/docs/skills/reference/productivity/todoist/) — `list_projects`
- [linear](/docs/skills/reference/dev/linear/) — `list_projects`
