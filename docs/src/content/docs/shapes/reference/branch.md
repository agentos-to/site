---
title: branch
description: "A git branch."
sidebar:
  label: branch
---

A git branch.

Example sources: git

| Metadata | Value |
|---|---|
| **Plural** | `branches` |
| **Subtitle field** | `commit` |

## Fields

| Field | Type |
|---|---|
| `commit` | `string` |
| `upstream` | `string` |
| `ahead` | `integer` |
| `behind` | `integer` |
| `isCurrent` | `boolean` |
| `isRemote` | `boolean` |

## Relations

| Relation | Target |
|---|---|
| `repository` | [`repository`](/docs/shapes/reference/repository/) |

## Skills that produce this shape

- [git](/docs/skills/reference/dev/git/) — `list_branches`
- [git](/docs/skills/reference/dev/git/) — `get_branch`
