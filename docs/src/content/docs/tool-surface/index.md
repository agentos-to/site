---
title: Tool surface
description: "Every tool the AgentOS engine exposes — 8 namespaces, one registry."
---

The engine's tool surface is organized into **8 namespaces**. The registry in `crates/core/src/tools.rs` is the single source of truth — this page, the MCP `tools/list`, and the Python `Client` SDK are all generated from it.

See [`_roadmap/p1/unified-surface/unified-surface.md`](https://github.com/agentos-to) for the architecture.

## Namespaces

- [`data`](/tool-surface/data/) (12 ops) — Query and mutate graph entities
- [`skills`](/tool-surface/skills/) (6 ops) — Skill introspection and direct dispatch
- [`system`](/tool-surface/system/) (4 ops) — Engine lifecycle
- [`windows`](/tool-surface/windows/) (8 ops) — Query and drive the desktop shell's windows — by route and policy, not pixels
- [`ui`](/tool-surface/ui/) (1 op) — Interact with window content the way a human does — by labeled control, never pixels
- [`readme`](/tool-surface/readme/) (1 op) — Orient yourself
- [`tools`](/tool-surface/tools/) *(empty)* — Dynamic capability providers contributed by installed skills
