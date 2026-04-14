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

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/ontology/shape-design-principles/) for how prior art informs shape design.

- **[Git Internals — Branches](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)** — A branch is a movable pointer to a commit. Our commit field is the HEAD sha; ahead/behind mirror `git rev-list --count`.
- **[GitHub REST — branches](https://docs.github.com/en/rest/branches/branches)** — Practical API surface. Our upstream ≈ the remote tracking ref; we flatten protection/commit metadata that GitHub nests.

## Skills that produce this shape

- [git](/docs/skills/reference/dev/git/) — `list_branches`
- [git](/docs/skills/reference/dev/git/) — `get_branch`
