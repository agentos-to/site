---
title: session
description: "An MCP session — a client connected, made some calls, disconnected."
sidebar:
  label: session
---

An MCP session — a client connected, made some calls, disconnected.
One node per unique client+project+branch combo, updated on reconnection.

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
| `participant` | [`actor`](/shapes/reference/actor/) |
| `folder` | [`folder`](/shapes/reference/folder/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[Model Context Protocol (MCP) session](https://modelcontextprotocol.io/specification)** — Direct source. Our client/sessionType come from MCP's client/transport concepts (STDIO, HTTP+SSE).
- **[OpenTelemetry Spans (root span ≈ session)](https://opentelemetry.io/docs/concepts/signals/traces/)** — Our startedAt/endedAt/messageCount/tokenCount align with span lifecycle + attributes in a trace context.
- **[OpenID Connect Session Management 1.0](https://openid.net/specs/openid-connect-session-1_0.html)** — Classical web-session model. Our participant ≈ authenticated subject; projectId/gitBranch are AgentOS-specific scoping.

## Skills that produce this shape

- [cursor](/skills/reference/dev/cursor/) — `op_list_sessions`, `op_backfill_session`, `op_get_session`
