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

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/ontology/shape-design-principles/) for how prior art informs shape design.

- **[Git Internals — commit object](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects)** — Our sha/shortHash/message/parent match the commit object exactly. author/committer follow Git's distinct author-vs-committer model.
- **[Conventional Commits 1.0](https://www.conventionalcommits.org/en/v1.0.0/)** — Practical structure for message field (type(scope): subject). Optional — we don't enforce but it's compatible.

## Skills that produce this shape

- [git](/docs/skills/reference/dev/git/) — `list_git_commits`, `search_git_commits`
- [git](/docs/skills/reference/dev/git/) — `get_git_commit`
