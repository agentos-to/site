---
title: tool_call
description: "A single tool invocation made by an agent during a message."
sidebar:
  label: tool_call
---

A single tool invocation made by an agent during a message.
Captures the tool name, input arguments, and the result that came back.
Tool calls are first-class entities so you can query "every time Claude
ran Grep on this repo" or "every tool call that errored."

Example sources: Claude Code transcripts, OpenAI function-calling logs,
any agent framework that records tool use.

| Metadata | Value |
|---|---|
| **Plural** | `tool_calls` |
| **Subtitle field** | `name` |
| **Identity** | `platform`, `id` |

## Fields

| Field | Type |
|---|---|
| `name` | `string` |
| `input` | `text` |
| `output` | `text` |
| `isError` | `boolean` |
| `durationMs` | `integer` |

## Relations

| Relation | Target |
|---|---|
| `platform` | [`product`](/docs/reference/shapes/product/) |
| `from` | [`actor`](/docs/reference/shapes/actor/) |
| `inMessage` | [`message`](/docs/reference/shapes/message/) |
| `repliesTo` | [`tool_call`](/docs/reference/shapes/tool_call/) |
