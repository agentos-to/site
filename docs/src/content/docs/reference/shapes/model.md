---
title: model
description: "An AI model — LLM, embedding model, or other ML model."
sidebar:
  label: model
---

An AI model — LLM, embedding model, or other ML model.

Example sources: Ollama, OpenRouter, Anthropic API

| | |
|---|---|
| **Plural** | `models` |
| **Subtitle field** | `provider` |
| **Identity** | `provider`, `name` |

## Fields

| Field | Type |
|---|---|
| `provider` | `string` |
| `contextLength` | `integer` |
| `contextWindow` | `integer` |
| `maxOutput` | `integer` |
| `pricingInput` | `string` |
| `pricingOutput` | `string` |
| `modality` | `string[]` |
| `modelType` | `string` |
| `quantization` | `string` |
| `quantizationLevel` | `string` |
| `size` | `string` |
| `parameterSize` | `string` |
| `format` | `string` |
| `family` | `string` |
| `digest` | `string` |

## Skills that produce this shape

- [openrouter](/docs/reference/skills/openrouter/) — `list_models`
- [claude](/docs/reference/skills/claude/) — `list_models`, `list_models_cli`
- [ollama](/docs/reference/skills/ollama/) — `list_models`, `list_models_cli`
