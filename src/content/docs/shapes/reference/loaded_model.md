---
title: loaded_model
description: "A currently loaded/running AI model instance."
sidebar:
  label: loaded_model
---

A currently loaded/running AI model instance.

| Metadata | Value |
|---|---|
| **Plural** | `loaded_models` |
| **Subtitle field** | `size` |

## Fields

| Field | Type |
|---|---|
| `size` | `string` |
| `quantization` | `string` |
| `expiresAt` | `datetime` |
| `vramUsage` | `string` |
| `sizeVram` | `integer` |
| `digest` | `string` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[Ollama API — /api/ps](https://github.com/ollama/ollama/blob/main/docs/api.md#list-running-models)** — Direct source. Our size/vramUsage/sizeVram/quantization/digest/ expiresAt map to Ollama's ListRunningModelsResponse fields.
- **[OpenTelemetry Resource semconv (ML/AI)](https://opentelemetry.io/docs/specs/semconv/gen-ai/)** — Emerging conventions for GenAI observability. Our size/digest align with gen_ai.model.* resource attributes.

## Skills that produce this shape

- [ollama](/skills/reference/ai/ollama/) — `ps`
