---
title: model
description: "An AI model — LLM, embedding model, or other ML model."
sidebar:
  label: model
---

An AI model — LLM, embedding model, or other ML model.

| Metadata | Value |
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

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/shapes/shape-design-principles/) for how prior art informs shape design.

- **[Hugging Face Model Cards](https://huggingface.co/docs/hub/en/model-cards)** — Our provider/contextLength/modality/family/quantization/ parameterSize align with HF model-card metadata conventions.
- **[Ollama /api/show + Modelfile](https://github.com/ollama/ollama/blob/main/docs/modelfile.md)** — Our quantization/quantizationLevel/format/digest/parameterSize come directly from Ollama's show-model response.
- **[OpenRouter Models API](https://openrouter.ai/docs/models)** — Our contextLength/contextWindow/maxOutput/pricingInput/ pricingOutput mirror OpenRouter's model spec.

## Skills that produce this shape

- [openrouter](/docs/skills/reference/ai/openrouter/) — `list_models`
- [claude](/docs/skills/reference/ai/claude/) — `list_models`, `list_models_cli`
- [ollama](/docs/skills/reference/ai/ollama/) — `list_models`, `list_models_cli`
