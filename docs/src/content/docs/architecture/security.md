---
title: Security
description: Security by architecture, not by permissions check. Skills and apps never name each other. Credentials live in Keychain. The engine is the sole broker.
---

Security in AgentOS is not a layer of permissions bolted onto a permissive core. It's the shape of how the pieces connect. If two components can't name each other, they can't trust each other, and the engine remains the only broker.

## Capability brokering

**Skills and apps never know about each other.** This is the load-bearing invariant.

A skill declares what it provides:

```python
@provides("llm")
def chat(messages): ...
```

An app asks for a capability:

```typescript
await agentos.capability("llm").invoke({ messages })
```

Between those two calls, the engine picks the skill. Neither side learns the other's identity. Uninstalling a skill has zero runtime impact on apps as long as *some* skill still provides the capability. Uninstalling an app is invisible to skills.

This isn't a policy check. It's a name-resolution architecture. There is no API an app could call that would let it invoke a specific skill by name — the engine's dispatch layer only takes capabilities.

## Connections are sandboxed identities

Every time a skill reaches an external service, it does so through a
**connection** — a module-level `connection("name", ...)` declaration
in the skill's `.py` file. Each connection is a sandboxed identity
profile with its own cookies, its own auth, and its own mode. Tools
on different connections never share state.

Isolation is by construction, not by policy check:

- **Connections key into the credential store on `(domain,
  identifier)`, not `(skill, connection_name)`.** The connection's
  `base_url` derives the domain (`api.exa.ai` →  `exa.ai`). Two
  skills that both declare a connection named `portal` don't
  collide — they resolve to different domains because their
  `base_url`s point at different services.
- **Cookies live in two jars.** The **credential store** is the
  persistent vault — encrypted at rest, keyed on `(domain,
  identifier)`. The **per-call jar** is ambient inside the SDK for
  the duration of one tool call — seeded from the store on entry,
  diffed back on exit. Plaintext cookies exist only in the Python
  worker's memory, only while the tool body runs.
- **A compromised skill cannot reach across identities.** Its
  resolved connection maps to exactly one credential row. It has
  no way to enumerate rows, open a jar for a different domain, or
  read another connection's cookies.
- **Skill rename / reorganize is safe.** Move `amazon.py`, rename
  its `web` connection to `account` — cookies stay put because
  they're keyed on `amazon.com`, not on the skill's directory.

See [Connections as browsers](/architecture/connections-as-browsers/)
for the full model, including the three modes (`browser`, `fetch`,
`api`), the per-call jar lifecycle, and how `Set-Cookie` writeback
keeps rotating session tokens current across engine restarts.

## Auth resolution — freshest wins

When a skill needs a session (cookie, bearer token, OAuth pair), it asks the engine via the SDK. The engine looks in three places:

1. **In-memory cache** — resolved sessions from the current engine lifetime.
2. **Credential store** — encrypted entries in `~/.agentos/data/agentos.db`.
3. **Browser providers** — live extractions from Brave / Firefox / Chrome via CDP.

Each candidate carries a per-cookie timestamp. **The freshest candidate wins.** There is no fixed priority, no provider ranking. A recently-extracted browser session beats an older stored credential, even if the store entry was "configured" first.

The engine then runs the skill's own `account.check` on the resolved session to validate identity. If check fails, the engine falls through to the next candidate. Skills see only the resolved session — never the raw credential store, never another source's entry.

## Encryption at rest

Credential values in the database are encrypted with **AES-256-GCM**. The 32-byte key lives in the **macOS Keychain** under service `"AgentOS Credential Store"`, account `"encryption-key"`, and is read once per engine lifetime into a `OnceLock`.

- **Key generation** — first run generates 32 random bytes via `getrandom` and writes to Keychain through the `security` CLI.
- **Nonce** — 12-byte random nonce per encryption, standard for GCM.
- **Key never on disk** — the database contains ciphertext + nonce + auth tag; the key only ever lives in the Keychain and process memory.

If Keychain is unreachable (non-macOS, locked), the credential store currently falls back to unencrypted with a warning. That fallback is a known rough edge, not a design goal.

## What the engine refuses to do

The Rust engine is a **generic entity store**. It knows about *nodes*, *edges*, *values*, *shapes*, *operations*. It does not know about *tasks*, *messages*, *people*, or any specific entity type.

Things the engine will not do:

- Hardcode a field name (`priority`, `done`, `blocks`, `blocked_by`).
- Branch on an entity type's name.
- Sort, group, partition, or render based on entity type.
- Call out to a bespoke fetcher for a specific kind of record.

Violations are architecture bugs, caught at code review. The reason is structural: if the engine grows an opinion about what a "task" is, then skills and apps can no longer define new entity types without modifying the Rust binary. The ontology lives in [shapes](/shapes/overview/), not in the engine.

## Boundaries and trust

Each of the [four boundaries](/architecture/overview/#the-four-boundaries) is a trust boundary:

| Boundary | Trust relationship |
|---|---|
| MCP STDIO → `agentos-mcp` | Local-only; MCP client is trusted to act on the user's behalf. |
| `agentos-mcp` → engine socket | Unix socket, filesystem-permission-gated. |
| Engine → Python subprocess | Skill runs user-space; SDK dispatches back for any side-effect. |
| Engine → web bridge (HTTP) | Localhost only (`127.0.0.1:3456`). Read-only DB handle; writes go through the engine socket. |

A compromised skill can't touch the credential store directly — it has to dispatch a `secrets.get(...)` back to the engine, which applies the auth-resolution policy above. A compromised app can't write to the graph directly — its HTTP reads are served from a read-only connection; writes require a capability call.

## Honest caveats

A few things that CLAUDE.md and the principles assert but the code does not fully enforce:

- **Decoupling is SDK-layer, not engine-layer.** Nothing in the engine binary stops a rogue skill from hardcoding an app name in a dispatch. The isolation is convention + decorator patterns, enforced at skill validation and code review.
- **Multi-device is not implemented.** The graph is portable (one file, copy it), but there is no sync daemon, conflict resolution, or merge layer. If two machines edit the same graph file, last-writer-wins via filesystem timestamps.
- **Keychain fallback is unencrypted.** On systems without Keychain, the credential store currently emits a warning and stores values in plaintext.

See [Architectural laws](/architecture/architectural-laws/) for the full structural constraints.
