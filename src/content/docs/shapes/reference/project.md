---
title: project
description: "A project that groups tasks. Tasks belong to projects."
sidebar:
  label: project
---

A project that groups tasks. Tasks belong to projects.

| Metadata | Value |
|---|---|
| **Plural** | `projects` |
| **Subtitle field** | `state` |
| **Identity** | `at`, `id` |

## Fields

| Field | Type |
|---|---|
| `state` | `string` |
| `color` | `string` |
| `parentId` | `string` |

## Relations

| Relation | Target |
|---|---|
| `at` | [`actor`](/shapes/reference/actor/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[Linear API — Project](https://developers.linear.app/docs/graphql/working-with-the-graphql-api)** — Our state/color come directly from Linear's Project model.
- **[GitHub Projects (v2)](https://docs.github.com/en/graphql/reference/objects#projectv2)** — Canonical open-source project-board model. state ≈ ProjectV2SingleSelectFieldOption; color is per-field metadata.
- **[schema.org/Project](https://schema.org/Project)** — Generic project-as-effort type. Thinner than the practical APIs; mainly useful for outbound JSON-LD.

## Skills that produce this shape

- [todoist](/skills/reference/productivity/todoist/) — `list_projects`
- [linear](/skills/reference/dev/linear/) — `list_projects`
