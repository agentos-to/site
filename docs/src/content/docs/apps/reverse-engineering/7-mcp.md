---
title: "Reverse Engineering — MCP Servers"
description: "How to discover, evaluate, and map Model Context Protocol (MCP) servers for apps that need to connect as MCP clients."
---

How to discover, evaluate, and map Model Context Protocol (MCP) servers for apps that need to connect as MCP clients. Unlike web reverse-engineering, MCPs are **self-describing** — `tools/list` hands you the full tool catalog. What you're reverse-engineering is auth, actual response shapes, coverage gaps, and behavioral quirks.

**Tool:** The MCP test harness in `agentos/scripts/mcp-test.mjs` is the primary probe. Use it to discover tools, test calls, and inspect responses. Smithery registry (`mcp-test.mjs smithery search`) finds third-party MCPs.

### Transport — use httpx, not urllib

HTTP MCPs (Granola, Linear, etc.) often sit behind CloudFront or Cloudflare. Python `urllib` and `requests` advertise `http/1.1` and get flagged by JA4 fingerprinting. **Follow [1-transport](./1-transport.md):** use `httpx` with `http2=True` for Python probes. Node `fetch` is fine (negotiates HTTP/2). App-local probe scripts (e.g. `apps/productivity/granola/mcp-probe.py`) should use httpx.

---

## Layer 0: Existence — Does the platform have an MCP?

Before anything else, determine if an MCP exists for the platform. Three discovery paths:

### Convention probing

Most platforms follow predictable URL patterns. Probe these for every app you have:

| Pattern | Example |
|---------|---------|
| `https://mcp.{domain}/mcp` | Granola: `mcp.granola.ai/mcp`, Linear: `mcp.linear.app/mcp` |
| `https://{domain}/mcp` | `https://example.com/mcp` |
| `https://api.{domain}/mcp` | `https://api.example.com/mcp` |

**Probe:** Send a bare `POST` with an `initialize` JSON-RPC request. A 404 or connection refused means nothing there. A JSON-RPC response or auth challenge means you found one.

```bash
# Using mcp-test.mjs with a raw URL (no auth)
node scripts/mcp-test.mjs http https://mcp.granola.ai/mcp
```

### Smithery registry

The [Smithery registry](https://smithery.ai) indexes MCPs published by third parties. Use this for platforms that might have community MCPs but no official one:

```bash
node scripts/mcp-test.mjs smithery search "granola"
node scripts/mcp-test.mjs smithery search "linear"
```

### Web search

Platforms are publicly announcing MCP support. Search for `"{platform name}" MCP` or `"{platform name}" Model Context Protocol` in changelogs, blog posts, or docs.

### Output: Existence table

| App | MCP URL | Transport | Status |
|-------|---------|-----------|--------|
| granola | `mcp.granola.ai/mcp` | HTTP | found |
| linear | `mcp.linear.app/mcp` | HTTP | found |
| todoist | `npx @abhiz123/todoist-mcp-server` | stdio | found (3rd party) |
| goodreads | — | — | none found |

---

## Layer 1: Transport — How does the session work?

MCPs run over two transports. The harness handles both; you need to log what you observe.

### Streamable HTTP

- POST JSON-RPC to the URL
- Response may be plain JSON or SSE (`event: message\ndata: {...}`)
- `mcp-session-id` in response headers — session-stateful vs stateless
- Used by: Granola, Linear, other hosted MCPs

### Stdio

- Spawn subprocess: `npx -y @package/mcp-server`
- JSON-RPC over stdin/stdout, newline-delimited
- Used by: Todoist, Notion, Slack (npm packages)

### What to log

| Field | How to check |
|-------|--------------|
| `mcp-session-id` | Response headers on first request |
| Response format | SSE vs plain JSON body |
| `protocolVersion` | From `initialize` response `result.serverInfo` |
| `capabilities` | Tools, resources, prompts, logging |
| Server-initiated requests | Any during handshake? |

---

## Layer 2: Auth — What does it need and how do you get in?

MCP auth discovery is a waterfall. The protocol is designed for this.

### Step 1: Naked probe

Send `initialize` with no auth headers.

| Outcome | Meaning |
|---------|---------|
| Success | Public MCP, no auth (rare for user data) |
| `401` with `WWW-Authenticate` | Auth required; header describes scheme |
| Connection accepted, `tools/call` fails | Auth is per-call, not per-session |

### Step 2: OAuth discovery

Two discovery paths. The `401` response may include `resource_metadata` pointing at one of these:

**Protected resource discovery** (RFC 9729):
```
GET {origin}/.well-known/oauth-protected-resource
```
Returns `authorization_servers`, `resource`, `bearer_methods_supported`. Example: Granola's `401` pointed to this; response: `{"authorization_servers":["https://mcp-auth.granola.ai"], ...}`.

**OAuth authorization server discovery** (RFC 8414):
```
GET {origin}/.well-known/oauth-authorization-server
```
Returns `authorization_endpoint`, `token_endpoint`, `scopes_supported` for the full OAuth flow.

### Step 3: Token reuse hypothesis

For platforms where you already have an app: **can you reuse the existing token?** Granola's supabase token, Linear's API key — do they work as `Authorization: Bearer {token}` against the MCP endpoint? This is a single-line test.

### Step 4: Scope mapping

Once authenticated: does the MCP give full access or a restricted view? Some MCPs expose read-only tools even if the underlying API supports writes.

---

## Layer 3: Tool catalog — What's exposed?

This is where MCPs are radically easier than web reverse-engineering. `tools/list` returns the full catalog:

```json
{
  "tools": [{
    "name": "list_meetings",
    "description": "List recent meetings",
    "inputSchema": { "type": "object", "properties": { "limit": { "type": "integer" } } }
  }]
}
```

### Cross-reference with the existing app

For each MCP tool, find the corresponding operation in your existing app. Build a coverage matrix:

| Your Operation | MCP Tool | Match? | Notes |
|----------------|----------|--------|-------|
| `list_meetings` | `list_meetings` | exact | Same params? |
| `get_meeting` | `get_document` | name differs | Check if transcript included |
| `list_conversations` | — | no match | MCP doesn't expose Q&A |
| — | `create_note` | no match | MCP has write we don't |

This matrix is the key deliverable — it tells you whether the MCP is superset, subset, or lateral complement.

### Annotation analysis

Check `tool.annotations`:

- `readOnlyHint` — safe to probe, no mutating
- `destructiveHint` — mutates state, be careful in testing

---

## Layer 4: Response analysis — What does the data look like?

MCP input schemas are declared; output is usually opaque `content: [{type: "text", text: "..."}]`. You must call each tool and inspect.

### For each read-safe tool

1. Call with minimal params
2. Unwrap `content[0].text` and parse as JSON
3. Document the actual response shape — field names, nesting, types
4. Compare field-by-field to your existing app's normalized output

This answers: **Is the MCP richer, thinner, or different?** Does Granola's MCP return raw utterances like the internal API, or only a pre-formatted summary?

---

## Layer 5: Gap analysis — Is it worth connecting?

For each platform, combine layers 0–4 into a verdict:

| Signal | Implication |
|--------|-------------|
| MCP covers all your operations with equal or richer data | MCP as primary, existing app as fallback |
| MCP covers some, misses others | Multi-connection: MCP for what it covers, API for the rest |
| MCP is thinner than your app | Keep the existing app; MCP not worth it |
| MCP exposes tools you don't have (especially writes) | MCP as additive connection |
| Auth is significantly easier via MCP | MCP worth it for auth stability alone |

---

## Running the analysis

For each platform, work through layers 0–4 using `mcp-test.mjs`:

```bash
# Generic harness (agentos repo) — pass URL; MCP_BEARER_TOKEN for auth
node scripts/mcp-test.mjs http https://mcp.granola.ai/mcp
node scripts/mcp-test.mjs http https://mcp.granola.ai/mcp call list_meetings '{"limit": 3}'

# App-local exploration (apps repo) — reads token from the Granola desktop app
python3 apps/productivity/granola/mcp-probe.py
python3 apps/productivity/granola/mcp-probe.py tools
```

Start with platforms where you already have apps (Granola, Linear). You have ground truth — your existing app tells you exactly what data to expect. The output is a completed coverage matrix and a clear verdict.

---

## Real-World Examples

| App | MCP URL | Transport | Auth | Coverage |
|-------|---------|-----------|------|----------|
| granola | `mcp.granola.ai/mcp` | HTTP | **Different auth** — supabase token invalid. `401` returns `WWW-Authenticate: Bearer error="invalid_token"`, `resource_metadata="https://mcp.granola.ai/.well-known/oauth-protected-resource"`. MCP uses OAuth; internal API token does not work. Probe with httpx succeeds (no TLS block). |
| linear | `mcp.linear.app/mcp` | HTTP | OAuth / API key | TBD — run analysis |

Fill this table as you run the analysis. See `apps/productivity/granola/` for the existing Python app's operations and adapter schema.

### Probe commands

Use the generic harness (no platform-specific code) or app-local scripts:

```bash
# Generic MCP harness (agentos repo) — pass URL; set MCP_BEARER_TOKEN for auth
node scripts/mcp-test.mjs http https://mcp.granola.ai/mcp
MCP_BEARER_TOKEN=$(python3 -c "
import json
from pathlib import Path
p = Path.home() / 'Library/Application Support/Granola/supabase.json'
t = json.loads(json.load(p.open())['workos_tokens'])
print(t['access_token'])
") node scripts/mcp-test.mjs http https://mcp.granola.ai/mcp

# App-local exploration (apps repo)
python3 apps/productivity/granola/mcp-probe.py
```
