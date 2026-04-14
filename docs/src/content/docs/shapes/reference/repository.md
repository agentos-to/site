---
title: repository
description: "A source code repository."
sidebar:
  label: repository
---

A source code repository.

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
| `forkedFrom` | [`repository`](/docs/shapes/reference/repository/) |
| `owner` | [`account`](/docs/shapes/reference/account/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/shapes/shape-design-principles/) for how prior art informs shape design.

- **[Git internals + Git refs](https://git-scm.com/book/en/v2/Git-Internals-Git-References)** — Our defaultBranch is a Git ref (refs/heads/main); forkedFrom is explicit in our model vs. implicit in Git (recorded only by forges).
- **[GitHub REST API — Repository](https://docs.github.com/en/rest/repos/repos)** — Direct source. Our stars/forks/openIssues/topics/defaultBranch/ license/size/isArchived/isPrivate all come from the GitHub Repository resource.
- **[SPDX License List](https://spdx.org/licenses/)** — Our license values are SPDX identifiers (MIT, Apache-2.0, GPL-3.0-or-later).

## Skills that produce this shape

- [git](/docs/skills/reference/dev/git/) — `get_repository`
