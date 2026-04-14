---
title: tag
description: "A tag or label — Gmail label, Todoist label, GitHub label, git tag, etc."
sidebar:
  label: tag
---

A tag or label — Gmail label, Todoist label, GitHub label, git tag, etc.
Cross-skill: anything can carry tags. An email has labels, a task has tags,
a PR has labels, a git commit has tags.

Example sources: Gmail, Todoist, GitHub

| | |
|---|---|
| **Plural** | `tags` |
| **Subtitle field** | `tagType` |

## Fields

| Field | Type |
|---|---|
| `color` | `string` |
| `tagType` | `string` |

## Skills that produce this shape

- [todoist](/docs/reference/skills/todoist/) — `list_tags`
- [git](/docs/reference/skills/git/) — `list_tags`
- [git](/docs/reference/skills/git/) — `get_tag`
- [gmail](/docs/reference/skills/gmail/) — `list_labels`
- [gmail](/docs/reference/skills/gmail/) — `create_label`, `update_label`
