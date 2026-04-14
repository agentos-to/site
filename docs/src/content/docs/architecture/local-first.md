---
title: Local-first
description: No cloud. No accounts. No data sharing. Everything runs on your machine — and that's the architecture, not a limitation.
---

No cloud. No accounts. No data sharing. Everything runs on your machine.

This isn't a limitation — it's the architecture. Local-first means:

- **Privacy by design** — your messages, tasks, and contacts never leave your computer unless a skill you installed specifically sends them somewhere.
- **No gatekeepers** — no API rate limits from our servers, no subscription tiers, no "free tier" that degrades.
- **Offline works** — your graph lives in SQLite on disk, always available.
- **You own the data** — export it, delete it, nuke the database, start fresh. It's yours.

## What "local-first" means concretely

### What lives on your machine

Everything that counts as *your data*:

- **The graph** — every node, edge, and value you've ever stored. One SQLite file.
- **Encrypted credentials** — sessions for services you've connected. Keys in Keychain, values in that same SQLite file.
- **Skill code** — the Python that runs when you invoke a skill. Read at call time from `~/dev/agentos/skills/` or wherever you installed the skill.
- **Settings and preferences** — stored as graph values (key-value on nodes), not in cloud configs.

### What goes over the network

AgentOS itself makes zero outbound calls. The engine never phones home — there's no telemetry, no update check, no "anonymous usage stats."

What *does* go over the network is whatever the **[skills](/skills/overview/) you installed** choose to send. A [GitHub skill](/skills/reference/dev/github/) makes requests to `api.github.com`. An LLM skill makes requests to Anthropic or OpenAI. That's the skill's business, not the engine's — and the skill's code is on your disk for you to read.

The contract: the engine is the authority for what's *stored locally*. What a skill *sends out* is what you installed it to do.

### What we don't do

- **No sync daemon.** There is no background process shipping your data anywhere.
- **No accounts.** There is no `agentos.to/signup`. The only identity that matters is the macOS user running the binary.
- **No "freemium."** The same binary has the same capabilities for everyone.

## The state map

```
~/.agentos/
  data/agentos.db        The graph + encrypted credentials (one SQLite file)
  logs/                  engine.log, mcp.log, engine-io.jsonl
  engine.sock, mcp.sock  IPC endpoints for MCP and the web bridge
  engine.pid             Singleton guard
  engine.lock            flock — one engine per machine
```

One directory. Copy it to a new machine and your AgentOS comes with it. Delete it and you start fresh.

## Multi-device (roadmap, not shipped)

The graph is portable — it's one SQLite file. You *can* copy it to another machine, and it will work. But AgentOS does **not** yet ship a sync layer, conflict resolution, or intent-based merging. If you edit the graph on two machines, last-writer-wins via filesystem timestamps.

The long-term vision is content/storage separation: your graph lives somewhere you trust (a local server, a VPS, a NAS), and any device with the right key can talk to it. This is not built yet. For now, local-first means *one machine at a time*.

## We can break anything, anytime

There are no customers to migrate. No production database to preserve. No backwards compatibility to maintain. This is a superpower: it means we can always choose the right architecture over the safe one.

If a schema changes, we rebuild from scratch. If a decision turns out to be wrong, we change it. **Data is disposable — the architecture is not.**

## Why local-first is load-bearing

An agent that reads your messages, your bank transactions, your location history — that agent should run on a machine you trust, not on someone else's server. When the compute is remote, "trust the model" becomes "trust every layer between you and the model." Local-first collapses that chain.

See [Security](/architecture/security/) for why the engine's brokering architecture matters for this — and why skills can't exfiltrate data they don't have permission to touch.
