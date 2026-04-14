---
title: repository
description: "A source code repository."
sidebar:
  label: repository
---

A source code repository.

Example sources: GitHub

| Metadata | Value |
|---|---|
| **Plural** | `repositories` |
| **Subtitle field** | `language` |
| **Identity** | `path`, `url` |

## Fields

| Field | Type |
|---|---|
| `stars` | `integer` |
| `forks` | `integer` |
| `language` | `string` |
| `topics` | `string[]` |
| `openIssues` | `integer` |
| `isArchived` | `boolean` |
| `isPrivate` | `boolean` |
| `defaultBranch` | `string` |
| `license` | `string` |
| `size` | `integer` |

## Relations

| Relation | Target |
|---|---|
| `forkedFrom` | [`repository`](/docs/reference/shapes/repository/) |
| `owner` | [`account`](/docs/reference/shapes/account/) |

## Skills that produce this shape

- [git](/docs/reference/skills/dev/git/) — `get_repository`
