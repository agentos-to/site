---
title: What is AgentOS
description: A local operating system for human-AI collaboration. Built for agents first.
---

AgentOS is a local operating system for human-AI collaboration. Your data stays on your machine. AI agents get real tools that work. You see everything they do. Together, you and AI think better than either can alone.

We're building toward J.C.R. Licklider's vision of **human-computer symbiosis** — not AI that replaces human thinking, but AI that amplifies it. The human sets direction, makes judgments, asks the right questions. The AI does the routinizable work that prepares the way for insight.

The agent is the primary customer. AgentOS is the operating system *for* agents, not around them.

## The pieces

**The engine** — a Rust binary that runs the graph (a SQLite database — the "memex"), executes skills, resolves auth, and speaks **MCP** so any MCP-capable agent (Claude Code, Cursor, etc.) can use AgentOS as its tool surface.

**Skills** — Python adapters that connect to external services (macOS apps, cloud services, keychains) or act as pure agent tools. They declare the *capabilities* they provide (`@provides(llm)`, `@provides(web_search)`), and the engine matchmakes requests to the best available provider.

**Apps** — an optional GUI layer for humans (TypeScript/React). Think Linux plus an optional desktop environment: the CLI and engine work fully without it.

**The graph** — your personal knowledge store. Everything is an entity; entities connect via relationships. It all lives in a single portable SQLite file at `~/.agentos/data/agentos.db`.

Skills and apps never know about each other. The engine is the sole broker — **security by architecture**.

## Where to go next

- [Vision](/docs/introduction/vision/) — the full story of the memex, the graph, and symbiosis.
- [The two users](/docs/introduction/two-users/) — why we design for humans and agents as equal first-class citizens.
- [Local-first](/docs/introduction/local-first/) — why your data never leaves your machine.
- [Contributing → Skills](/docs/contributing/skills/overview/) — start building.
