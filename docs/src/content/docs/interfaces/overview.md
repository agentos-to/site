---
title: Overview
description: AgentOS is a single engine with four surfaces — MCP for AI clients, a CLI for humans and scripts, an HTTP web bridge for local apps, and the optional GUI apps themselves. Pick your mode.
---

AgentOS is a **single engine** with **four surfaces**. The engine is a Rust daemon that speaks JSON-RPC over a Unix socket. Everything else — Claude Desktop, the `agentos` CLI, a React app, a shell script — is a client that reaches the engine through one of these four interfaces.

| Interface | For | How |
|---|---|---|
| [MCP](/docs/interfaces/mcp/) | AI clients (Claude Desktop, Cursor, Claude Code) | stdio JSON-RPC through `agentos-mcp` proxy |
| [CLI](/docs/interfaces/cli/) | Developers, operators, scripts | `agentos` binary, direct socket connection |
| [HTTP](/docs/interfaces/http/) | Local browser apps | Localhost HTTP/SSE on `127.0.0.1:3456` |
| [Apps](/docs/apps/overview/) | End users | React apps talking to the HTTP bridge |

All four converge on the same engine. The engine doesn't know which interface made a call — it sees JSON-RPC requests and dispatches to skills. Interfaces are transport; the engine is logic.

## Pick one

- **You're building a skill** — use the **CLI** to test it (`agentos test-skill`) and the **MCP** interface to see how an AI client would invoke it.
- **You're writing an AI-client integration** — **MCP** is the protocol. Everything else is implementation detail.
- **You're building a browser app** — talk to the **HTTP** bridge. Don't try to connect to the engine socket directly.
- **You just want to use AgentOS** — install the **[Apps](/docs/apps/overview/)**.

## Why four, not one

Different clients want different things:

- AI clients (Cursor, Claude Desktop) speak **MCP** natively. They want stdio JSON-RPC over a subprocess lifetime. Meeting them there means zero adapter code on the client side.
- Humans want a **CLI** — it's faster for one-shot calls, pipeable, scriptable, and familiar. `agentos call ...` is the fastest way to poke at the graph.
- Browsers can't speak Unix sockets, so a **localhost HTTP** bridge translates. Apps get a regular fetch-based API; the engine stays in its own process.
- **Apps** on top of the bridge are how end users actually use the thing. They're optional — the engine is fully functional without any GUI.

None of these is primary. The engine is the primary thing; each surface is a transport.

## What you'll find in each interface page

Each page is self-contained — you don't need to read them in order.

- **Wire details** — what the transport looks like on the socket / pipe / port.
- **Authentication / trust model** — what the interface can do, what it can't.
- **Common operations** — the three or four things you'll actually use it for.
- **Failure modes** — what goes wrong when it goes wrong.

## What's missing

The engine is a fat binary and a graph database. There is no gRPC server, no WebSocket subscription API, no remote HTTP endpoint. Some of that may come; right now, if it's not in the table at the top of this page, it doesn't exist.

Multi-device access is not a surface — it's a data-sync problem, and AgentOS doesn't solve it yet. See [Local-first](/docs/architecture/local-first/) for the state of the roadmap.
