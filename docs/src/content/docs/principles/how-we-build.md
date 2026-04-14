---
title: How we build
description: Foundation first. Spec before code. Delete fearlessly. Infinite time horizon.
---

We are **co-CTOs** — human and AI — making strategic decisions together. This is not task execution. It's collaborative architecture.

## The posture

- **Foundation first.** The most foundational thing that prevents tech debt is always the priority. Not quick wins, not "almost done" items, not cleanup. The thing everything else builds on.
- **Spec before code.** Design the right thing, then build it. A wrong implementation done fast is worse than no implementation.
- **Delete fearlessly.** No attachment to past code. If the model changes, the code changes. We write for the current best understanding, not for backwards compatibility.
- **Infinite time horizon.** No customers, no deadlines, no pressure to ship. The right architecture at the right time.
- **Pain-driven.** If you can't articulate the pain, don't build it.
- **Blast radius is not a cost — stale architecture is.** An "audacious" refactor that touches the engine and every skill in one shot is *not more expensive* than a one-line fix. Pre-launch means zero migration cost.

See [Architectural laws](/docs/principles/architectural-laws/) for the full rule set.

## Skills

Each skill is a directory with a `readme.md` (YAML frontmatter for identity + connections, markdown body for the agent-facing guide) plus one or more `.py` files whose `@returns`-decorated functions are the tools. No separate manifest — operations are extracted from the Python AST at load time. The community repo tracks shipped skills under `skills/`.

Start at the [Skills overview](/docs/skills/overview/).

## Shapes

The ontology is a directory of YAML files — one shape per file — at `site/docs/shapes/`. Shapes describe entity types (fields, relations, display hints, operations). Add a shape, reseed, restart the engine; the graph now knows about a new entity type. No Rust change required.

Read the [Shape design principles](/docs/ontology/shape-design-principles/) before proposing a new shape.

## Apps

TypeScript/React UIs for humans. Each app is self-contained and built against the `apps/_sdk/`. Apps never talk to skills directly — they ask the engine for a capability, the engine routes to a skill that `@provides(...)` it.

See [Apps overview](/docs/apps/overview/).

## Proposals & roadmap

Design thinking lives in `_roadmap/` — pain, proposal, review, closeout. The pipeline is described in [Roadmap & proposals](/docs/principles/roadmap-and-proposals/).

**Proposals must include prior art.** Don't design in a vacuum — search for how others solved similar problems before proposing.

## Build discipline

- **Test through real services, not mocks.** No unit tests. Integration tests via MCP against the running engine.
- **Architecture over quick.** Always choose the right long-term architecture. No shortcuts.
- **Dogfooding is the whole point.** Every session, building with the SDK should get easier. DX wins beat feature wins. If something isn't intuitive, *improve the SDK, don't work around it.*
