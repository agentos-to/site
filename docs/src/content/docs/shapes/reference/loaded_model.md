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
| **Also** | [`event`](/shapes/reference/event/) |

## Fields

| Field | Type |
|---|---|
| `size` | `string` |
| `quantization` | `string` |
| `vramUsage` | `string` |
| `sizeVram` | `integer` |
| `digest` | `string` |

## Inherited

From [`event`](/shapes/reference/event/):

| Field | Type |
|---|---|
| `allDay` | `boolean` |
| `currentUrl` | `string` |
| `dateUpdated` | `datetime` |
| `distinctId` | `string` |
| `endDate` | `datetime` |
| `icalUid` | `string` |
| `properties` | `json` |
| `recurrence` | `string[]` |
| `showAs` | `string` |
| `sourceTitle` | `string` |
| `sourceUrl` | `url` |
| `startDate` | `datetime` |
| `status` | `string` |
| `timezone` | `string` |
| `visibility` | `string` |

| Relation | Target |
|---|---|
| `at_namespace` | [`actor`](/shapes/reference/actor/) |
| `concerns` | [`person`](/shapes/reference/person/) |
| `created_by` | [`person`](/shapes/reference/person/) |
| `held_at` | [`place`](/shapes/reference/place/) |
| `involves` | [`person[]`](/shapes/reference/person/) |
| `organized_by` | [`person`](/shapes/reference/person/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[Ollama API — /api/ps](https://github.com/ollama/ollama/blob/main/docs/api.md#list-running-models)** — Direct source. Our size/vramUsage/sizeVram/quantization/digest/ expiresAt map to Ollama's ListRunningModelsResponse fields.
- **[OpenTelemetry Resource semconv (ML/AI)](https://opentelemetry.io/docs/specs/semconv/gen-ai/)** — Emerging conventions for GenAI observability. Our size/digest align with gen_ai.model.* resource attributes.

## Apps that produce this shape

- [ollama](/apps/reference/ai/ollama/) — `ps`
