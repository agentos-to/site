---
title: file
description: "A file — source code, attachment, download, or any discrete digital artifact."
sidebar:
  label: file
---

A file — source code, attachment, download, or any discrete digital artifact.
Base type for image. Covers repo files (GitHub, Cursor), email attachments
(Mimestream), filesystem entries, and downloads.

Example sources: GitHub, Cursor, Mimestream, filesystem

| Metadata | Value |
|---|---|
| **Plural** | `files` |
| **Subtitle field** | `path` |

## Fields

| Field | Type |
|---|---|
| `filename` | `string` |
| `mimeType` | `string` |
| `size` | `integer` |
| `path` | `string` |
| `format` | `string` |
| `encoding` | `string` |
| `lineCount` | `integer` |
| `kind` | `string` |
| `sha` | `string` |

## Relations

| Relation | Target |
|---|---|
| `attachedTo` | [`message`](/docs/shapes/reference/message/) |
| `repository` | [`repository`](/docs/shapes/reference/repository/) |

## Used as a base by

- [`document`](/docs/shapes/reference/document/)
- [`image`](/docs/shapes/reference/image/)
- [`spec`](/docs/shapes/reference/spec/)
- [`video`](/docs/shapes/reference/video/)

## Skills that produce this shape

- [cursor](/docs/skills/reference/dev/cursor/) — `op_pull_document`
- [github](/docs/skills/reference/dev/github/) — `list_documents`
- [github](/docs/skills/reference/dev/github/) — `read_document`
- [gmail](/docs/skills/reference/comms/gmail/) — `get_attachment`
