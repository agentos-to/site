---
title: Local-first
description: No cloud. No accounts. No data sharing. Everything runs on your machine — and that's the architecture, not a limitation.
---

No cloud. No accounts. No data sharing. Everything runs on your machine.

This isn't a limitation — it's the architecture. Local-first means:

- **Privacy by design** — your messages, tasks, and contacts never leave your computer.
- **No gatekeepers** — no API rate limits from our servers, no subscription tiers, no "free tier" that degrades.
- **Offline works** — your graph lives in SQLite on disk, always available.
- **You own the data** — export it, delete it, nuke the database, start fresh. It's yours.

## Security by architecture

Skills and apps **never know about each other**. The engine is the sole broker. An app asks "give me an LLM"; the engine picks a skill that `@provides(llm)`; neither side learns the other's name. If they can't name each other, they can't trust each other, and the engine remains the only broker of capability and auth.

This is *security by architecture* — not bolted on as a permissions check, but built into the shape of how the pieces connect. See [Architectural laws](/docs/principles/architectural-laws/) for the full structural constraints.

## We can break anything, anytime

There are no customers to migrate. No production database to preserve. No backwards compatibility to maintain. This is a superpower: it means we can always choose the right architecture over the safe one.

If a schema changes, we rebuild from scratch. If a decision turns out to be wrong, we change it. Data is disposable — the architecture is not.

## Where everything lives

```
~/.agentos/
  data/agentos.db        The graph + encrypted credentials (one SQLite file)
  logs/                  engine.log, mcp.log, engine-io.jsonl
  engine.sock, mcp.sock  IPC endpoints for MCP and the web bridge
  engine.pid             Singleton guard
```

One directory. Copy it, back it up, move it to a new machine. Your entire AgentOS lives there.
