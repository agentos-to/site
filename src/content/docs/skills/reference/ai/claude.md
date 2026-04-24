---
title: Claude
description: "Claude — Anthropic's AI model family. Inference via API or local CLI, plus claude.ai chat history."
sidebar:
  label: claude
---

| Metadata | Value |
|---|---|
| **Category** | `ai` |
| **Capabilities** | `http`, `secrets`, `shell` |
| **Website** | <https://claude.ai> |

## Returns shapes

- [`account`](/shapes/reference/account/) — from `check_session`
- [`conversation`](/shapes/reference/conversation/) — from `get_conversation`, `read_conversation_cli`
- [`conversation[]`](/shapes/reference/conversation/) — from `list_conversations`, `search_conversations`, `list_conversations_cli`
- [`message[]`](/shapes/reference/message/) — from `import_conversation`
- [`model[]`](/shapes/reference/model/) — from `list_models`, `list_models_cli`

## Readme

One skill for everything Claude. Four access modalities, one product.

| Connection | File | What it does |
|---|---|---|
| `api` | `claude_api.py` | Inference via the Claude API (Messages endpoint) |
| `code` | `claude_code.py` | Inference via the local `claude` CLI, plus reads local Claude Code state |
| `web` | `claude_web.py` | Browse/search/import claude.ai chat history |

Models are **never hardcoded**. All operations accept a `model` parameter that is
resolved through the graph (`list_models` on the relevant connection populates it).
See `docs/specs/done/no-hardcoded-models.md` for rationale.

## Usage

### `api` connection — Claude API inference

| Tool | Description |
|---|---|
| `list_models` | Fetch the current model catalog from `api.anthropic.com/v1/models` |
| `chat` | Send a single Messages API request. Supports tools, system prompts, temperature. Returns raw tool_use blocks for the caller to process. |

### `code` connection — Claude Code

Uses the user's logged-in `claude` binary (no API key required) AND reads local
on-disk state under `~/.claude/projects/`.

| Tool | Description |
|---|---|
| `agent` | Run Claude as an agent via `claude -p`. Full agent loop — tool use + structured output via `--mcp-config` / `--json-schema`. |
| `list_models_cli` | List Claude models via the keychain OAuth token (no API key). Same endpoint as `list_models`, different auth. |
| `list_projects` | List every project directory under `~/.claude/projects/` with conversation counts and last activity. |
| `list_conversations_cli` | List local Claude Code conversations (one per JSONL transcript) as shape-native `conversation[]`. Optional `project` scope, optional `limit`. |
| `read_conversation_cli` | Read a full conversation transcript — returns one `conversation` with a nested `message[]` relation (content, blocks, author, published, tool calls). |

> **Note:** The `code` connection uses `agent` rather than `chat` because it behaves
> fundamentally differently from the API — it loops internally over tool calls.
> Both still `@provides(llm)` so capability routing can pick either.
>
> The `_cli` suffix on `list_models_cli` / `list_conversations_cli` /
> `read_conversation_cli` is because skill tool names share a flat namespace
> across all `.py` files in the skill, and the same names are already taken by
> the `api` and `web` connections (for the Anthropic API model list and
> claude.ai web chats, respectively).

### `web` connection — claude.ai chat history

| Tool | Description |
|---|---|
| `list_conversations` | Browse conversations, most recent first |
| `get_conversation` | Full conversation with all messages |
| `search_conversations` | Search by title (client-side filter) |
| `import_conversation` | Import messages into graph for FTS |
| `list_orgs` | Discover orgs and capabilities |
| `check_session` | Verify cookies are valid, return identity |
| `extract_magic_link` | Parse magic link from raw email (used during login) |

## Setup

### `api` connection
1. Get an API key from https://console.anthropic.com/settings/keys
2. Add credential in AgentOS Settings → Skills → Claude (API Key)

### `code` connection
Install Claude Code and log in:
```bash
curl -fsSL https://claude.ai/install.sh | bash    # or: brew install claude-code
claude auth login                                   # opens browser for OAuth
```
Works with Pro/Max/Team/Enterprise subscriptions. Once logged in, `claude_code.py`
uses that auth state directly — no key exchange with agentOS.

### `web` connection
No setup needed if you're logged in to claude.ai in a supported browser (Brave/Firefox).
Cookie provider matchmaking extracts `sessionKey` automatically.
