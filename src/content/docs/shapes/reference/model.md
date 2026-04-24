---
title: model
description: "An AI model — LLM, embedding model, or other ML model."
sidebar:
  label: model
---

An AI model — LLM, embedding model, or other ML model.

Identity: (at, name) — graph-native. `at` is a relation to the entity
providing the model (an organization like Anthropic/OpenAI, or a product
like ollama for self-hosted). The model node persists across provider
rebrands or reorganizations.

| Metadata | Value |
|---|---|
| **Plural** | `models` |
| **Subtitle field** | `name` |
| **Identity** | `at`, `name` |

## Fields

| Field | Type |
|---|---|
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

## Relations

| Relation | Target |
|---|---|
| `at` | [`actor`](/shapes/reference/actor/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[Hugging Face Model Cards](https://huggingface.co/docs/hub/en/model-cards)** — Our provider/contextLength/modality/family/quantization/ parameterSize align with HF model-card metadata conventions.
- **[Ollama /api/show + Modelfile](https://github.com/ollama/ollama/blob/main/docs/modelfile.md)** — Our quantization/quantizationLevel/format/digest/parameterSize come directly from Ollama's show-model response.
- **[OpenRouter Models API](https://openrouter.ai/docs/models)** — Our contextLength/contextWindow/maxOutput/pricingInput/ pricingOutput mirror OpenRouter's model spec.

## Skills that produce this shape

- [openrouter](/skills/reference/ai/openrouter/) — `list_models`
- [claude](/skills/reference/ai/claude/) — `list_models`, `list_models_cli`
- [ollama](/skills/reference/ai/ollama/) — `list_models`, `list_models_cli`
