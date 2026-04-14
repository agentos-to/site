---
title: folder
description: "A filesystem directory or workspace. Used to track project roots,"
sidebar:
  label: folder
---

A filesystem directory or workspace. Used to track project roots,
working directories, and document collections.

| Metadata | Value |
|---|---|
| **Plural** | `folders` |
| **Subtitle field** | `path` |
| **Identity** | `path` |

## Fields

| Field | Type |
|---|---|
| `path` | `string` |
| `workspaceType` | `string` |
| `hasReadme` | `boolean` |

## Relations

| Relation | Target |
|---|---|
| `repository` | [`repository`](/docs/shapes/reference/repository/) |
| `contains` | [`file[]`](/docs/shapes/reference/file/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/shapes/shape-design-principles/) for how prior art informs shape design.

- **[POSIX / Single Unix Specification](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html)** — Our path is a POSIX pathname. hasReadme is AgentOS-specific (README convention from repos).
- **[schema.org/DataCatalog](https://schema.org/DataCatalog)** — Folder-as-collection loose fit. contains(file[]) ≈ hasPart.
