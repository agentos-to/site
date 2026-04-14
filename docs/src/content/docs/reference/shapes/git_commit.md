---
title: git_commit
description: "A git commit — a single point in version control history."
sidebar:
  label: git_commit
---

A git commit — a single point in version control history.

Example sources: git skill

| Metadata | Value |
|---|---|
| **Plural** | `git_commits` |
| **Subtitle field** | `author` |

## Fields

| Field | Type |
|---|---|
| `sha` | `string` |
| `shortHash` | `string` |
| `message` | `text` |
| `additions` | `integer` |
| `deletions` | `integer` |
| `filesChanged` | `integer` |
| `committedAt` | `datetime` |

## Relations

| Relation | Target |
|---|---|
| `author` | [`account`](/docs/reference/shapes/account/) |
| `committer` | [`account`](/docs/reference/shapes/account/) |
| `repository` | [`repository`](/docs/reference/shapes/repository/) |
| `parent` | [`git_commit`](/docs/reference/shapes/git_commit/) |

## Skills that produce this shape

- [git](/docs/reference/skills/dev/git/) — `list_git_commits`, `search_git_commits`
- [git](/docs/reference/skills/dev/git/) — `get_git_commit`
