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

| | |
|---|---|
| **Plural** | `agents` |
| **Subtitle field** | `model` |
| **Also** | [`actor`](/docs/reference/shapes/actor/) |

## Fields

| Field | Type |
|---|---|
| `model` | `string` |
| `provider` | `string` |
| `sessionId` | `string` |

## Inherited

From [`actor`](/docs/reference/shapes/actor/):

| Field | Type |
|---|---|
| `actorType` | `string` |
