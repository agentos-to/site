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

| Metadata | Value |
|---|---|
| **Plural** | `tags` |
| **Subtitle field** | `tagType` |

## Fields

| Field | Type |
|---|---|
| `color` | `string` |
| `tagType` | `string` |

## Skills that produce this shape

- [todoist](/docs/reference/skills/productivity/todoist/) — `list_tags`
- [git](/docs/reference/skills/dev/git/) — `list_tags`
- [git](/docs/reference/skills/dev/git/) — `get_tag`
- [gmail](/docs/reference/skills/comms/gmail/) — `list_labels`
- [gmail](/docs/reference/skills/comms/gmail/) — `create_label`, `update_label`
