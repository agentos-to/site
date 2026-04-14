---
title: file
description: "A file — source code, attachment, download, or any discrete digital artifact."
sidebar:
  label: file
---

A file — source code, attachment, download, or any discrete digital artifact.
Base type for image. Covers repo files (GitHub, Cursor), email attachments
(Mimestream), filesystem entries, and downloads.

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
| `attachedTo` | [`message`](/shapes/reference/message/) |
| `repository` | [`repository`](/shapes/reference/repository/) |

## Used as a base by

- [`document`](/shapes/reference/document/)
- [`image`](/shapes/reference/image/)
- [`spec`](/shapes/reference/spec/)
- [`video`](/shapes/reference/video/)

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[IANA Media Types (RFC 6838)](https://datatracker.ietf.org/doc/html/rfc6838)** — Our mimeType follows type/subtype syntax (text/plain, application/pdf). Canonical source for format identification.
- **[schema.org/DigitalDocument](https://schema.org/DigitalDocument)** — Our filename ≈ name; size ≈ contentSize; mimeType ≈ encodingFormat.
- **[Git Internals (blob objects)](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects)** — Our sha is a Git blob SHA-1 (40-hex). Git's content-addressable model underlies our repo-file identity.

## Skills that produce this shape

- [cursor](/skills/reference/dev/cursor/) — `op_pull_document`
- [github](/skills/reference/dev/github/) — `list_documents`, `read_document`
- [gmail](/skills/reference/comms/gmail/) — `get_attachment`
