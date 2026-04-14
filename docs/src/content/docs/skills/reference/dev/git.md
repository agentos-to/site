---
title: Git
description: "Local git repository data — commits, branches, tags, and repo info"
sidebar:
  label: git
---

| Metadata | Value |
|---|---|
| **Category** | `dev` |
| **Capabilities** | `shell` |
| **Website** | <https://git-scm.com> |

## Returns shapes

- [`branch`](/docs/shapes/reference/branch/) — from `get_branch`
- [`branch[]`](/docs/shapes/reference/branch/) — from `list_branches`
- [`git_commit`](/docs/shapes/reference/git_commit/) — from `get_git_commit`
- [`git_commit[]`](/docs/shapes/reference/git_commit/) — from `list_git_commits`, `search_git_commits`
- [`repository`](/docs/shapes/reference/repository/) — from `get_repository`
- [`tag`](/docs/shapes/reference/tag/) — from `get_tag`
- [`tag[]`](/docs/shapes/reference/tag/) — from `list_tags`

## Readme

Local git repository data — commits, branches, tags, and repo info. Wraps the git CLI
to bring version control history into the graph as searchable entities.

## No Auth Required

Git reads from local repositories. No API keys, no tokens — just the git binary
that's already on your machine.

## Entity Mappings

| Git Concept | AgentOS Entity | Relationship |
|-------------|----------------|--------------|
| Commits | `git_commit` (extends message) | Author → person, commit → in → repository |
| Branches | `branch` (extends place) | branch → in → repository |
| Tags | `tag` (existing entity) | tag → tag → git_commit |
| Repositories | `repository` (existing entity) | Populated from local git info |

## Usage

```bash
# List recent commits
git_commit.list (skill: git, path: "/Users/joe/dev/agentos")

# Search commit messages
git_commit.search (skill: git, path: "/Users/joe/dev/agentos", query: "readme")

# Get a specific commit
git_commit.get (skill: git, path: "/Users/joe/dev/agentos", id: "f9f9f57")

# List branches
branch.list (skill: git, path: "/Users/joe/dev/agentos")

# Get repo info
repository.get (skill: git, path: "/Users/joe/dev/agentos")

# Live status (not stored — computed fresh)
git.status (path: "/Users/joe/dev/agentos")

# View diff
git.diff (path: "/Users/joe/dev/agentos", staged: true)
```

## Design Decisions

**Commits are messages.** `git commit -m` — you're sending a message into a repository.
The inheritance chain is work → document → post → message → git_commit.

**Authors are people with email accounts.** Git gives us a name + email pair.
The transformer creates a person entity (deduped on email) and links it via the
sender relationship. The email becomes an account entity via claims.

**Only immutable data is stored.** A commit's hash, message, author, and diff stats
never change. Branch ahead/behind counts, working tree status, and other ephemeral
state come from utilities that query live.

**Tags reuse the existing tag entity.** A git tag is a named label applied to a
commit — exactly what the tag entity already represents.
