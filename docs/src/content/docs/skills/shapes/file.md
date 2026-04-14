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
| `attachedTo` | [`message`](/docs/reference/shapes/message/) |
| `repository` | [`repository`](/docs/reference/shapes/repository/) |

## Used as a base by

- [`document`](/docs/reference/shapes/document/)
- [`image`](/docs/reference/shapes/image/)
- [`spec`](/docs/reference/shapes/spec/)
- [`video`](/docs/reference/shapes/video/)

## Skills that produce this shape

- [cursor](/docs/reference/skills/dev/cursor/) — `op_pull_document`
- [github](/docs/reference/skills/dev/github/) — `list_documents`
- [github](/docs/reference/skills/dev/github/) — `read_document`
- [gmail](/docs/reference/skills/comms/gmail/) — `get_attachment`
