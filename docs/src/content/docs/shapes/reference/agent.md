---
title: agent
description: "An AI agent that acts on behalf of a user. Agents are actors — they"
sidebar:
  label: agent
---

An AI agent that acts on behalf of a user. Agents are actors — they
can be attributed as the "who" on any change in the graph, alongside
people and organizations.

Examples: Claude in Cursor, a background job agent, a scheduled task runner.

| Metadata | Value |
|---|---|
| **Plural** | `agents` |
| **Subtitle field** | `model` |
| **Also** | [`actor`](/docs/shapes/reference/actor/) |

## Fields

| Field | Type |
|---|---|
| `model` | `string` |
| `provider` | `string` |
| `sessionId` | `string` |

## Inherited

From [`actor`](/docs/shapes/reference/actor/):

| Field | Type |
|---|---|
| `actorType` | `string` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/shapes/shape-design-principles/) for how prior art informs shape design.

- **[ActivityStreams 2.0 Service](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-service)** — AS2's Service Actor is the closest peer for an automated agent. We add model/provider/sessionId for AI-specific lineage.
- **[Anthropic Tool Use API (Claude)](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)** — Mirrors our model/provider fields. sessionId groups related tool invocations from a single agent run.
