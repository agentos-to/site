---
title: session
description: "An MCP session — a client connected, made some calls, disconnected."
sidebar:
  label: session
---

An MCP session — a client connected, made some calls, disconnected.
One node per unique client+project+branch combo, updated on reconnection.

Example sources: agentOS engine (MCP session registration)

| Metadata | Value |
|---|---|
| **Plural** | `sessions` |
| **Subtitle field** | `client` |
| **Identity** | `client`, `projectId`, `gitBranch` |

## Fields

| Field | Type |
|---|---|
| `client` | `string` |
| `projectId` | `string` |
| `gitBranch` | `string` |
| `sessionType` | `string` |
| `startedAt` | `datetime` |
| `endedAt` | `datetime` |
| `messageCount` | `integer` |
| `tokenCount` | `integer` |

## Relations

| Relation | Target |
|---|---|
| `participant` | [`actor`](/docs/reference/shapes/actor/) |
| `folder` | [`folder`](/docs/reference/shapes/folder/) |

## Skills that produce this shape

- [cursor](/docs/reference/skills/dev/cursor/) — `op_list_sessions`, `op_backfill_session`
- [cursor](/docs/reference/skills/dev/cursor/) — `op_get_session`
