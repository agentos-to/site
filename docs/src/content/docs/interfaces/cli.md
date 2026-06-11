---
title: CLI
description: The agentos binary — call operations, run the engine daemon, inspect auth, manage app sources. Same binary, multiple subcommands.
---

The `agentos` binary is the Swiss Army knife of AgentOS. It's **the same fat binary** for all subcommands — [the engine](/architecture/overview/), the web bridge, the [MCP](/interfaces/mcp/) proxy, the auth inspector — which means one install, one upgrade path, one thing to restart.

## The subcommands

### `agentos call [namespace] ['{...}']`

One-shot tool invocation. Connects directly to the engine socket, sends one JSON-RPC call, prints the response. The CLI exposes the engine's MCP namespaces — `data`, `apps`, `system`, `services`, `readme`, `windows`, and `ui`. Every call is `agentos call <namespace> '{"op":"<op>","params":{...}}'`:

```bash
# List the namespaces
agentos call --list

# Read a node by id
agentos call data '{"op":"read","params":{"id":"abc123"}}'

# Search the full-text index
agentos call data '{"op":"list","params":{"q":"memex","limit":10}}'

# Set a val on a node
agentos call data '{"op":"update","params":{"id":"abc123","vals":{"pref:theme":"xp"}}}'

# Create or upsert a node
agentos call data '{"op":"create","params":{"shape":"bookmark","name":"Aircraft","vals":{"address":"?shape=aircraft"}}}'

# Invoke an app tool
agentos call apps '{"op":"run","params":{"app":"goodreads","tool":"search_books","params":{"query":"licklider"}}}'
```

By default the output is pretty-printed markdown if the engine returns a structured response. Pass `--json` to get raw JSON — useful for piping into `jq` or another tool. `-q` drops the engine build stamp.

`agentos call` is the fastest way to poke at anything. If an app is broken, an [MCP](/interfaces/mcp/) tool is misbehaving, or you just want to check what's in the graph — reach for `call` first.

### `agentos readme`

Orientation — identity, tools, connected accounts, and the roadmap for the working directory. The CLI twin of the MCP `readme()` tool. Read it first, every session.

### `agentos engine [--daemon]`

Runs the engine process. One engine per machine, enforced by `flock` on `~/.agentos/engine.lock`. Subsequent invocations detect the running daemon and exit silently.

```bash
# Start and tail logs
agentos engine

# Start in the background
agentos engine --daemon
```

You rarely start the engine by hand — `agentos-mcp` and `agentos bridge` both call `ensure_engine()` on startup. But when you want to see engine logs live, this is how.

### `agentos bridge [--port 3456]`

Runs the web bridge (the [HTTP interface](/interfaces/http/)). Same singleton model — one bridge per port. Port configurable via `--port` or the `AGENTOS_BRIDGE_PORT` env var.

### `agentos mcp`

Runs the [MCP stdio proxy](/interfaces/mcp/). You don't invoke this directly; an AI client spawns it.

### `agentos browse [subcommand]`

Introspect the engine's authentication and request machinery. Useful when you're reverse-engineering a platform for a new app and you need to know exactly what session the engine would use.

- `agentos browse cookies <app>` — list stored cookies per issuer, with timestamps. The "which cookie is freshest" question.
- `agentos browse auth <app>` — trace how the engine would resolve auth for a given issuer. Shows the candidate list and the winner.
- `agentos browse request <app> <path>` — make an authenticated request to see what auth/headers the engine attaches.

### `agentos sources [list|add|remove]`

Manage source directories — where apps live on disk. A source root must contain an `apps/` subdirectory; the engine walks it at dispatch time.

```bash
agentos sources list
agentos sources add /Users/joe/dev/agentos
```

## Output formats

Most commands emit pretty-printed structured output by default. When a command returns graph records, you get a markdown table.

- `--json` — raw JSON, no formatting. Script-friendly.
- `-q` / `--quiet` — suppress the engine build stamp.

## Trust model

The CLI inherits the trust of the user running it. There is no `agentos login`, no API key, no per-command ACLs. If you can exec `agentos` and read `~/.agentos/engine.sock`, you have full access.

This is intentional: CLI access is for the user who owns the machine. The [MCP interface](/interfaces/mcp/) has the same trust model by extension — an AI client running as your user gets the same access.

## Exit codes

- `0` — success.
- `1` — generic error (app threw, bad input, engine rejected).
- `2` — engine unreachable (socket missing, daemon dead).
- `3` — singleton conflict (tried to start a second engine / bridge).

## Under the hood

The CLI crate is transport-thin. Every subcommand:

1. Parses its args with clap.
2. Translates them into a JSON-RPC request.
3. Connects to `~/.agentos/engine.sock`.
4. Sends, receives, formats, exits.

There is almost no logic in the CLI — it's a protocol adapter. That's why `agentos call` is so close to `curl against an API`: the engine is the API, and the CLI is a smart curl.
