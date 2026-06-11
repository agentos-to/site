---
title: Ollama
description: "Local AI models running on your machine via Ollama"
sidebar:
  label: ollama
---

| Metadata | Value |
|---|---|
| **Category** | `ai` |
| **Services** | `http`, `shell` |
| **Website** | <https://ollama.com> |

## Returns shapes

- [`loaded_model[]`](/shapes/reference/loaded_model/) — from `ps`
- [`model[]`](/shapes/reference/model/) — from `list_models`, `list_models_cli`

## Readme

Run local AI models — inference, tool calling, and model management — entirely on your machine. No API keys, no cloud, no cost per token.

## Setup

Install Ollama (if not already installed):

```bash
brew install ollama
brew services start ollama
```

Pull a model to use:

```bash
ollama pull qwen3.5:9b-q8_0    # recommended: 11GB, tools + vision + thinking, 256K ctx
ollama pull glm-4.7-flash       # coding specialist: 19GB, best local SWE-bench
```

The app auto-starts the Ollama server if it is not running — no manual setup required.

## Connections

| Connection | What it does |
|---|---|
| `api` (default) | REST API at `localhost:11434` — fast inference, most operations |
| `cli` | Ollama CLI binary — server start/stop, model pulls, management |

## Usage

| Tool | Connection | Description |
|---|---|---|
| `status` | cli | Check if server is running; start it if not |
| `chat` | api / cli | Multi-turn chat with tool calling and thinking mode |
| `generate` | api | One-shot text generation (faster for simple prompts) |
| `list_models` | api / cli | List all downloaded models with size and metadata |
| `pull_model` | cli / api | Download a model from the Ollama registry |
| `delete_model` | api / cli | Delete a model to free disk space |
| `ps` | api | Show models currently loaded in memory |
| `show_model` | api | Show model details: arch, context length, template |

## Tool calling

`chat` normalizes Ollama's tool call format to the canonical AgentOS shape:

```
{ id, name, input }
```

Pass tools as `{ name, description, input_schema }` — the same format used by the Claude app.

## Thinking mode

Models that support extended reasoning (qwen3, glm-4.7-flash, etc.) can be activated with `thinking: true`. The reasoning trace is returned in the `thinking` field, separate from `content`.

## Notes

- `chat` with `connection: cli` collapses message history into a single prompt — suitable for single-turn only
- `pull_model` defaults to the CLI connection for reliable progress on large downloads (19GB models)
- `ps` shows what is currently warm in unified memory — useful before running a new model to estimate reload time
- The `generate` operation skips chat overhead — use it for classification, extraction, or quick single-turn tasks where speed matters
