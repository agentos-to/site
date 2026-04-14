---
title: tag
description: "A tag or label — Gmail label, Todoist label, GitHub label, git tag, etc."
sidebar:
  label: tag
---

A tag or label — Gmail label, Todoist label, GitHub label, git tag, etc.
Cross-skill: anything can carry tags. An email has labels, a task has tags,
a PR has labels, a git commit has tags.

| Metadata | Value |
|---|---|
| **Plural** | `tags` |
| **Subtitle field** | `tagType` |

## Fields

| Field | Type |
|---|---|
| `color` | `string` |
| `tagType` | `string` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/shapes/shape-design-principles/) for how prior art informs shape design.

- **[GitHub REST API — Labels](https://docs.github.com/en/rest/issues/labels)** — Our color/name/tagType ≈ GitHub Label's color/name/default.
- **[Gmail API — Labels](https://developers.google.com/gmail/api/reference/rest/v1/users.labels)** — Practical source. Our tagType distinguishes Gmail's SYSTEM vs USER label types.
- **[Dublin Core dc:subject](https://www.dublincore.org/specifications/dublin-core/dces/)** — Generic classification vocabulary — tags on any resource.

## Skills that produce this shape

- [todoist](/docs/skills/reference/productivity/todoist/) — `list_tags`
- [git](/docs/skills/reference/dev/git/) — `list_tags`, `get_tag`
- [gmail](/docs/skills/reference/comms/gmail/) — `list_labels`, `create_label`, `update_label`
