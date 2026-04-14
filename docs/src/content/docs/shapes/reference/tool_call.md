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
| `platform` | [`product`](/docs/shapes/reference/product/) |
| `from` | [`actor`](/docs/shapes/reference/actor/) |
| `inMessage` | [`message`](/docs/shapes/reference/message/) |
| `repliesTo` | [`tool_call`](/docs/shapes/reference/tool_call/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/shapes/shape-design-principles/) for how prior art informs shape design.

- **[Anthropic Tool Use API](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)** — Our name/input/output/isError map to tool_use/tool_result blocks in Claude's message API.
- **[OpenAI Function Calling / tool_calls](https://platform.openai.com/docs/guides/function-calling)** — Our name/input = function.name/function.arguments; output is the tool-result message content.
- **[OpenTelemetry GenAI semconv](https://opentelemetry.io/docs/specs/semconv/gen-ai/)** — Emerging observability standard. Our durationMs/isError align with gen_ai.tool.* span attributes.
