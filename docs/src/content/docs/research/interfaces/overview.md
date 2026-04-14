---
title: "Interfaces surface (research)"
description: "How the AgentOS engine exposes itself: MCP, CLI, HTTP web bridge, and optional GUI layer. Documentation patterns from prior art systems."
---

## Interfaces overview

AgentOS is architecturally a **single engine** with **four distinct communication surfaces**, each serving different clients and use cases. The engine is transport-agnostic—it lives in a Rust daemon that speaks Unix sockets and JSON-RPC. Everything external goes through one of these four interfaces.

### 1. MCP (Model Context Protocol)

**Transport:** STDIO ↔ Unix socket bridge (agentos-mcp crate)  
**Clients:** Claude Desktop, Cursor, Claude Code, any MCP-capable agent  
**Wire format:** Newline-delimited JSON-RPC

When an MCP host (e.g., Cursor) starts an agent session, it spawns `agentos mcp`, a thin stdio proxy that:
- Ensures the engine daemon is running (`agentos_engine::bootstrap::ensure_engine()`)
- Bridges newline-delimited JSON-RPC from stdin to `~/.agentos/engine.sock`
- Replays saved `initialize` request + `notifications/initialized` on engine reconnect with jittered backoff

The proxy itself **does not parse** MCP messages—it's a byte bridge. All tool dispatch, skill execution, and graph access live in the engine process. Wire traffic is logged to `~/.agentos/logs/mcp.log` (timestamps, `←` / `→` markers).

### 2. CLI (Command-line interface)

**Transport:** Direct Unix socket connection  
**Clients:** Developers, operators, scripts  
**Wire format:** One-shot JSON-RPC (agentos call) or daemon control (agentos engine/bridge/mcp)

The same fat binary (`agentos`) that runs the engine also provides three main command families:

- **`agentos call [tool] [params]`** — one-shot MCP tool invocation. Connects directly to engine socket, sends a single JSON-RPC call, prints the response as pretty JSON or markdown (unless `--json` bypasses the renderer). Equivalent to `curl` against the engine.
- **`agentos engine [--daemon]`** — runs the engine process. Uses `flock` to ensure only one daemon per machine; subsequent invocations just connect to the running instance.
- **`agentos bridge [--port 3456]`** — runs the local web server. Also uses `flock` to ensure singleton behavior.
- **`agentos browse [request|cookies|auth]`** — introspect authenticated HTTP requests, trace auth resolution, view cookies and timestamps.
- **`agentos test-skill [skill] [--op op-name] [--graph]`** — test a skill's operations against declared shapes and graph integration.

The CLI is transport-thin: it marshals args to JSON, sends to the engine socket, and formats the response. All logic lives in the engine.

### 3. HTTP Web Bridge

**Transport:** Localhost HTTP/SSE at `127.0.0.1:3456` (agentos-web-bridge crate)  
**Clients:** Browser-based React apps in `~/dev/agentos/apps/`  
**Wire format:** JSON (POST `/graph`) and SSE (GET `/observer/stream`)

The bridge is a read-heavy HTTP/1.1 server serving several routes:

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/healthz` | Liveness check — can reach observer socket? |
| GET | `/observer/history` | One-shot tool-activity history (queryable by session/client) |
| GET | `/observer/stream` | SSE stream of live observer events |
| POST | `/graph` | Graph read API: `{ "tool": "tags"\|"read"\|"search"\|"delete"\|"run", "params": {...} }` |
| GET | `/graph/shapes` | All shape definitions (fields, relations, display) for the frontend |
| GET | `/apps` | Installed + bundled app definitions |
| GET | `/user` | Unified user profile (person prefs + desktop prefs + theme metadata) |
| PUT | `/user/pref` | Update person-level preference values |
| GET `/ui/*`, `/files/*` | Static assets: themes, wallpapers, app icons, file previews |

The bridge owns a **read-only SQLite connection** via `agentos_core::database`. The engine still owns all writes and skill execution. Observer events stream via a separate Unix socket (`~/.agentos/observer.sock`).

### 4. GUI Apps (Optional layer)

**Location:** `~/dev/agentos/apps/` (sibling repo)  
**Clients:** End users  
**Tech:** TypeScript/React, shipped as bundles

Apps are a completely **optional, detachable layer**. The engine and web bridge work fully without them. Apps speak to the bridge, never directly to the engine. The bridge's `/graph` and `/observer/stream` endpoints are the contract.

**Isolation principle:** Apps and skills must never know about each other. Installing or removing an app has zero impact on skills, and vice versa. The engine is the only matchmaker—apps ask "give me an LLM", the engine picks a skill that `@provides(llm)`, and neither side knows the other's name. This is **security by architecture**.

---

## Part A: Verification

All four interfaces have been verified to exist as described:

- **`crates/mcp/`** — Confirmed stdio proxy with `UnixStream` connection, wire logging, and reconnect with handshake replay. Exact match to description.
- **`crates/cli/`** — Fat binary with `agentos call`, `agentos engine`, `agentos bridge`, `agentos browse`, and `agentos test-skill` subcommands. Dispatch to transport crates is thin; logic lives in agentos-core.
- **`crates/web-bridge/`** — Axum HTTP server on `:3456` serving `/healthz`, `/observer/history`, `/observer/stream`, `/graph`, `/graph/shapes`, `/apps`, `/user`, theme/wallpaper/icon routes, and file previews. Read-mostly SQLite connection separate from engine.
- **`~/dev/agentos/apps/`** — TypeScript/React apps (accounts, messages, settings, store) shipping with `_sdk/` and `_components/` shared code. Apps speak only to the web bridge.

**No corrections needed.** The four-interface model is accurate.

---

## Part B: Prior art patterns

### Kubernetes

Kubernetes serves one API via three major clients: kubectl (CLI), Kubernetes API (direct/libraries), and the Dashboard (web UI). Documentation is **structured by client, not by operation**.

**Pattern:**
- Each client type gets its own reference section: `/docs/reference/kubectl/`, `/docs/reference/kubernetes-api/`, `/docs/tasks/access-application-cluster/web-ui-dashboard/`
- "Same operation across interfaces" is **not systematically documented** — no comparison tables like "get a pod in kubectl vs. API vs. Dashboard"
- Conceptual guides (`/docs/concepts/`) are interface-agnostic; task-based docs (`/docs/tasks/`) show the preferred method (usually kubectl)

**Insight:** Kubernetes treats interfaces as **separate reference trees**, not a unified surface. The downside is users must learn each interface independently.

### Docker

Docker Engine exposes CLI (`docker`), REST API (`/var/run/docker.sock`), and Compose (higher-level YAML). Documentation is **split by use case** rather than by component.

**Pattern:**
- CLI docs, API docs, and Compose docs exist as separate sections
- No unified "here's how to run a container across three interfaces" guide
- The Engine page mentions "the daemon" and "the CLI uses the API" but doesn't consolidate documentation

**Insight:** Docker's docs acknowledge the relationship but keep them separate. No single "Interfaces" landing page.

### PostgreSQL

PostgreSQL separates the **client interface** (libpq, ECPG, psql) from the **wire protocol** in its table of contents.

**Pattern:**
- **Section IV. Client Interfaces** covers libpq, large objects, ECPG, information schema
- **Section VIII. Internals** covers the Frontend/Backend Protocol (wire level)
- psql is mentioned under "Reference: Client Applications" but not given a dedicated section
- No unified comparison of "execute a query via psql vs. libpq vs. ODBC"

**Insight:** PostgreSQL separates **how you talk to the server** (clients) from **what protocol the server speaks** (wire). Wire protocol lives in Internals, not at the top level.

### Redis

Redis has a **"Tools"** section listing redis-cli, Redis Insight (GUI), and client libraries, but keeps them separate from the command reference.

**Pattern:**
- Commands documentation is interface-agnostic (works in any client)
- Client libraries get language-specific subsections
- GUI tools are documented separately
- RESP protocol is mentioned but not prominently featured

**Insight:** Redis treats the **command set** as transport-independent and keeps client implementations separate.

---

## Recommendation: Top-level sidebar section "Interfaces" vs. folding under "Architecture"

### Option A: New top-level "Interfaces" section

**Pros:**
- Signals that multi-interface access is a **core design** of AgentOS
- Brings parity awareness early ("you can use AgentOS via MCP, CLI, HTTP, or apps")
- One landing page where developers learn the full surface before diving into a specific client
- Forces documentation discipline—each interface must be explicitly documented

**Cons:**
- Adds a top-level section (increases sidebar complexity)
- If most users only care about one interface, it's one extra click
- Risk of turning "Interfaces" into a hub full of cross-links instead of self-contained guides

### Option B: Fold under "Architecture"

**Pros:**
- Keeps sidebar lean (one fewer section)
- "Interfaces" conceptually belongs under "how AgentOS is built"
- Reduces cognitive load for users who know what interface they want

**Cons:**
- Buries multi-interface awareness under a technical section
- Users looking for "how do I use AgentOS?" won't find the interfaces overview
- Less likely to be discovered by non-technical stakeholders (who might benefit from knowing the browser option exists)
- Weaker signal about the intentionality of the multi-interface design

### Decision: **Create new top-level "Interfaces" section**

**Justification:**

1. **AgentOS's core selling point is access diversity.** Unlike single-interface systems (e.g., "use our CLI or don't use us"), AgentOS lets you pick your mode: AI agent (MCP), developer (CLI), scripter (HTTP), or end user (GUI). This deserves first-class documentation real estate.

2. **Prior art shows separation, not hierarchy.** Kubernetes, Docker, and PostgreSQL all treat interfaces as peer concerns, not sub-topics. This suggests a top-level organizational structure resonates with users.

3. **Early guidance prevents wrong choices.** A new developer landing on the site should immediately learn all four interfaces and pick one. If "Interfaces" is buried under "Architecture," they might assume CLI-only and miss the HTTP/GUI paths.

4. **Multi-interface is non-obvious.** A single-interface system (like git) doesn't need a dedicated "Interfaces" page—there's only one way to use it. But AgentOS deliberately offers four. That choice needs visible documentation.

5. **Future-proof for new surfaces.** If AgentOS later adds a gRPC interface, Python REPL shell, or other surfaces, they all live in the same "Interfaces" section. It's a natural home for "all the ways to talk to the engine."

**Structure (proposed):**

```
Interfaces (top-level section)
├── Overview (you are here)
│   └── The four surfaces, prior art, why they exist
├── MCP (Model Context Protocol)
│   ├── How it works (stdio proxy, Unix socket)
│   ├── Reconnect & resilience
│   ├── Integration with Claude Desktop / Cursor / Claude Code
│   └── Schema + capabilities
├── CLI
│   ├── agentos call (one-shot operations)
│   ├── agentos engine / bridge / browse (daemon control)
│   ├── Examples (common operations)
│   └── Output formats (markdown, JSON)
├── HTTP Web Bridge
│   ├── API reference (/graph, /observer/stream, /user)
│   ├── Running locally (bootstrap, port config)
│   └── Building browser apps
└── Apps & GUI
    ├── Architecture (why optional, how it's isolated)
    ├── Building a new app (React template)
    ├── The app SDK
    └── Examples (accounts, messages, settings)
```

This structure ensures:
- **New users get oriented quickly** on all available modes
- **Each interface has its own deep-dive docs** without cross-contamination
- **The "apps are optional" principle is explicit**
- **No duplication**—an operation documented in one interface doesn't need to be re-taught in another (use cross-references instead)

