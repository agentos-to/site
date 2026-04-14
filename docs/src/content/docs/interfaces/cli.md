---
title: CLI
description: The agentos binary — call operations, run the engine daemon, inspect auth, test skills. Same binary, multiple subcommands.
---

The `agentos` binary is the Swiss Army knife of AgentOS. It's **the same fat binary** for all subcommands — the engine, the web bridge, the MCP proxy, the skill tester — which means one install, one upgrade path, one thing to restart.

## The subcommands

### `agentos call [tool] [--params '{...}']`

One-shot tool invocation. Connects directly to the engine socket, sends one JSON-RPC call, prints the response.

```bash
# Read a node by identity
agentos call graph.read --params '{"shape": "person", "name": "Joe"}'

# Search the full-text index
agentos call graph.search --params '{"q": "memex", "limit": 10}'

# Invoke a skill operation
agentos call skills.run --params '{"skill": "goodreads", "op": "search_books", "args": {"q": "licklider"}}'
```

By default the output is pretty-printed markdown if the engine returns a structured response. Pass `--json` to get raw JSON — useful for piping into `jq` or another tool.

`agentos call` is the fastest way to poke at anything. If a skill is broken, an MCP tool is misbehaving, or you just want to check what's in the graph — reach for `call` first.

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

Introspect the engine's authentication and request machinery. Useful when you're reverse-engineering a platform for a new skill and you need to know exactly what session the engine would use.

- `agentos browse cookies` — list stored cookies per issuer, with timestamps. The "which cookie is freshest" question.
- `agentos browse auth` — trace how the engine would resolve auth for a given issuer. Shows the candidate list and the winner.
- `agentos browse request` — dry-run a request to see what auth/headers the engine would attach.

### `agentos test-skill [skill] [--op OP] [--graph]`

Run a skill's operation against its declared shapes. Validates the return dict, checks identity, optionally writes results into the graph.

```bash
# Test a specific operation
agentos test-skill goodreads --op get_book --args '{"isbn": "9780140449136"}'

# Also validate graph integration
agentos test-skill goodreads --op get_book --args '{"isbn": "9780140449136"}' --graph
```

This is the skill author's primary development loop. Faster than going through MCP; fully introspectable.

## Output formats

Most commands emit pretty-printed structured output by default. When a command returns graph records, you get a markdown table. When it returns JSON-RPC results, you get formatted JSON with comments.

- `--json` — raw JSON, no formatting. Script-friendly.
- `--quiet` — suppress headers and blank lines, just the data.
- `--verbose` — additional trace output to stderr.

## Trust model

The CLI inherits the trust of the user running it. There is no `agentos login`, no API key, no per-command ACLs. If you can exec `agentos` and read `~/.agentos/engine.sock`, you have full access.

This is intentional: CLI access is for the user who owns the machine. The [MCP interface](/interfaces/mcp/) has the same trust model by extension — an AI client running as your user gets the same access.

## Exit codes

- `0` — success.
- `1` — generic error (skill threw, bad input, engine rejected).
- `2` — engine unreachable (socket missing, daemon dead).
- `3` — singleton conflict (tried to start a second engine / bridge).

## Under the hood

The CLI crate is transport-thin. Every subcommand:

1. Parses its args with clap.
2. Translates them into a JSON-RPC request.
3. Connects to `~/.agentos/engine.sock`.
4. Sends, receives, formats, exits.

There is almost no logic in the CLI — it's a protocol adapter. That's why `agentos call` is so close to `curl against an API`: the engine is the API, and the CLI is a smart curl.
