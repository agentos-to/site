---
title: branch
description: "A git branch."
sidebar:
  label: branch
---

A git branch.

Example sources: git

| | |
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
| `repository` | [`repository`](/docs/reference/shapes/repository/) |

## Skills that produce this shape

- [git](/docs/reference/skills/git/) — `list_branches`
- [git](/docs/reference/skills/git/) — `get_branch`
