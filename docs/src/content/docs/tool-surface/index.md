---
title: Tool surface
description: "Every tool the AgentOS engine exposes — 8 namespaces, one registry."
---

The engine's tool surface is organized into **8 namespaces**. The registry in `crates/core/src/tools.rs` is the single source of truth — this page, the MCP `tools/list`, and the Python `Client` SDK are all generated from it.

See [`_roadmap/p1/unified-surface/unified-surface.md`](https://github.com/agentos-to) for the architecture.

## Namespaces

- [`data`](/tool-surface/data/) (3 ops) — Query and mutate graph entities
- [`shapes`](/tool-surface/shapes/) *(empty)* — Shape definitions and typed upserts
- [`credentials`](/tool-surface/credentials/) *(empty)* — Encrypted credential vault
- [`skills`](/tool-surface/skills/) (2 ops) — Skill introspection and direct dispatch
- [`accounts`](/tool-surface/accounts/) (1 op) — Stored credentials, auth health, and providers
- [`system`](/tool-surface/system/) (3 ops) — Engine lifecycle
- [`tools`](/tool-surface/tools/) *(empty)* — Dynamic capability providers contributed by installed skills
