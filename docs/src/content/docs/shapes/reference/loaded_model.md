---
title: loaded_model
description: "A currently loaded/running AI model instance."
sidebar:
  label: loaded_model
---

A currently loaded/running AI model instance.

Example sources: Ollama

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

## Skills that produce this shape

- [ollama](/docs/skills/reference/ai/ollama/) — `ps`
