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
- **Blast radius is not a cost — stale architecture is.** An "audacious" refactor that touches the engine and every app in one shot is *not more expensive* than a one-line fix. Pre-launch means zero migration cost.

See [Architectural laws](/architecture/architectural-laws/) for the full rule set.

## Apps

Each app is a directory with a `readme.md` (YAML frontmatter for identity + test config, markdown body for the agent-facing guide) plus one or more `.py` files whose decorated functions are the tools. No separate manifest — tools are extracted from the Python AST at load time. The public [apps repo](https://github.com/agentos-to/apps) tracks shipped apps.

Apps never name each other. An app declares the services it `@provides(...)`; a consumer asks the engine for the service; the engine matchmakes. And nobody hand-writes app UI — every installed app renders in the desktop shell as a generated window built from its contract (`@returns` shapes + JSON-Schema input schemas).

Start at the [Apps overview](/apps/overview/).

## Shapes

The ontology is a directory of YAML files — one shape per file — at `platform/ontology/shapes/`. Shapes describe entity types (fields, relations, display hints). One generator (`platform/codegen/generate.py`) projects them into the Python SDK, the engine's Rust contract, and the shell's typed contract. Add a shape, regenerate; the graph learns the new entity type lazily when an app first returns it. No Rust change required.

Read the [Shape design principles](/shapes/shape-design-principles/) before proposing a new shape.

## Proposals & roadmap

Design thinking lives in `_roadmap/` — pain, proposal, review, closeout. The pipeline is described in [Roadmap & proposals](/introduction/roadmap-and-proposals/).

**Proposals must include prior art.** Don't design in a vacuum — search for how others solved similar problems before proposing.

## Build discipline

- **Test through real platforms, not mocks.** No unit tests. Integration tests via MCP against the running engine.
- **Architecture over quick.** Always choose the right long-term architecture. No shortcuts.
- **Dogfooding is the whole point.** Every session, building with the SDK should get easier. DX wins beat feature wins. If something isn't intuitive, *improve the SDK, don't work around it.*
