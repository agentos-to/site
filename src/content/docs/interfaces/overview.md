---
title: Overview
description: AgentOS is a single engine with four surfaces — MCP for AI clients, a CLI for humans and scripts, an HTTP web bridge for local apps, and the GUI that serves as an OS-like window into the graph.
---

AgentOS is a **single engine** with **four surfaces**. The engine is a Rust daemon that speaks JSON-RPC over a Unix socket. Everything else — Claude Desktop, the `agentos` CLI, the GUI, a shell script — is a client that reaches the engine through one of these four interfaces.

| Interface | For | How |
|---|---|---|
| [MCP](/interfaces/mcp/) | AI clients (Claude Desktop, Cursor, Claude Code) | stdio JSON-RPC through `agentos-mcp` proxy |
| [CLI](/interfaces/cli/) | Developers, operators, scripts | `agentos` binary, direct socket connection |
| [HTTP](/interfaces/http/) | Local browser apps | Localhost HTTP/SSE on `127.0.0.1:3456` |
| [GUI](/apps/overview/) | End users | Web server on the HTTP bridge, browsed via Tauri or a standard browser |

All four converge on the same engine. The engine doesn't know which interface made a call — it sees JSON-RPC requests and dispatches to skills. Interfaces are transport; the engine is logic.

## Pick one

- **You're building a skill** — use the **CLI** to test it (`agentos test-skill`) and the **MCP** interface to see how an AI client would invoke it.
- **You're writing an AI-client integration** — **MCP** is the protocol. Everything else is implementation detail.
- **You're building a browser app** — talk to the **HTTP** bridge. Don't try to connect to the engine socket directly.
- **You just want to use AgentOS** — launch the **[GUI](/apps/overview/)**.

## Why four, not one

Different clients want different things:

- AI clients (Cursor, Claude Desktop) speak **MCP** natively. They want stdio JSON-RPC over a subprocess lifetime. Meeting them there means zero adapter code on the client side.
- Humans want a **CLI** — it's faster for one-shot calls, pipeable, scriptable, and familiar. `agentos call ...` is the fastest way to poke at the graph.
- Browsers can't speak Unix sockets, so a **localhost HTTP** bridge translates. Apps get a regular fetch-based API; the engine stays in its own process.
- The **GUI** is how end users actually see the thing. The engine itself serves a web server; you browse it through Tauri (native window) or any standard browser (`http://localhost:3456`). It's the OS-like window into your graph — inspect entities, run skills, launch [apps](/apps/overview/) that live on top of the HTTP bridge. Optional: the CLI and engine work fully without it.

None of these is primary. The engine is the primary thing; each surface is a transport.

## What you'll find in each interface page

Each page is self-contained — you don't need to read them in order.

- **Wire details** — what the transport looks like on the socket / pipe / port.
- **Authentication / trust model** — what the interface can do, what it can't.
- **Common operations** — the three or four things you'll actually use it for.
- **Failure modes** — what goes wrong when it goes wrong.

## What's missing

The engine is a fat binary and a graph database. There is no gRPC server, no WebSocket subscription API, no remote HTTP endpoint. Some of that may come; right now, if it's not in the table at the top of this page, it doesn't exist.

Multi-device access is not a surface — it's a data-sync problem, and AgentOS doesn't solve it yet. See [Local-first](/architecture/local-first/) for the state of the roadmap.
