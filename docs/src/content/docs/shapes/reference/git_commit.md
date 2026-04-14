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
| `author` | [`account`](/docs/shapes/reference/account/) |
| `committer` | [`account`](/docs/shapes/reference/account/) |
| `repository` | [`repository`](/docs/shapes/reference/repository/) |
| `parent` | [`git_commit`](/docs/shapes/reference/git_commit/) |

## Skills that produce this shape

- [git](/docs/skills/reference/dev/git/) — `list_git_commits`, `search_git_commits`
- [git](/docs/skills/reference/dev/git/) — `get_git_commit`
