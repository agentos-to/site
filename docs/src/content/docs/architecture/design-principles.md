---
title: Design principles
description: The architectural rules that make AgentOS composable. How graph, skills, and apps fit together.
---

These are the first-principles rules that hold the system together. Every architectural decision traces back to one of them.

## Everything on the graph

No shadow tables, no side stores, no parallel data structures. If something is worth tracking — changes, provenance, audit trails, agent memory — it's an entity with relationships. If you find yourself designing a separate SQL table for something, stop and model it as entities instead.

## Computed, not stored

Properties that can be derived from the graph are never stored as fields — they're computed at query time or inferred by traversal. A task's status is computed from its completion state and blockers. A contact card is a view computed from graph traversals over a person's claimed accounts. The graph stores atoms; intelligence computes molecules.

See [Shape design principles](/docs/shapes/shape-design-principles/) for how this shapes the ontology — in particular *#2 no counts on shapes*.

## The user owns the graph

Skills are connectors, not owners. They sync data in, but the graph is the authority. Installing a skill imports data; uninstalling it doesn't delete what was imported. "Source of truth" is the graph, always — skills are remotes you pull from, not landlords who control your data.

## Changes are entities

When an entity is created, updated, or deleted, the operation itself becomes a **change entity** on the graph. A change has relationships to the actor (who did it), the target (what changed), and optionally the source (where data came from). This follows the pattern established by W3C PROV-O, ActivityStreams, and Git: make events first-class objects, not edges. Provenance isn't a static field — it's the full chain of change entities. Walk backwards to reconstruct any previous state.

See [Identity & change](/docs/shapes/identity-and-change/).

## Every actor has an identity

The human owner, each AI agent, and the system itself — all are entities on the graph. When the human edits a task, the change is attributed to them. When an agent creates a plan, it's attributed to that agent. Every change has a *who*. This is identification, not authentication — on a single-user local system, localhost binding is the access boundary.

## The graph bootstraps itself

Entities describe data. But entities, skills, and relationships are also data. The system models itself — skills as entities, schemas as entities, the meta-layer that describes the graph. This is how the system becomes self-aware and self-documenting.

## Three concerns

Entities, skills, and apps are independent concerns that compose into the full experience.

**Entity types** define the ontology — *what things are*. A video has a title, duration, and view count. A person has a name and relationships. You can have entities without skills (manually entered data).

**Skills** are the capability layer — connecting to external services, providing agent instructions. A YouTube skill knows how to fetch video metadata. A Todoist skill knows how to create tasks via their API. Skills can also be pure markdown — instructions that help AI agents understand a domain, with no API bindings at all. You can have skills without apps (AI-only workflows).

**Apps** are optional UI experiences for humans. The Videos app renders video entities with an embed player. The default entity viewer renders any entity with schema-driven components. A headless AgentOS — API and AI only — works perfectly without apps. You can have apps without skills (local-only data).

## See also

- [Architectural laws](/docs/architecture/architectural-laws/) — the structural constraints that keep the engine generic.
- [Agent empathy](/docs/skills/agent-empathy/) — the practice of building for the smallest model.
- [Shape design principles](/docs/shapes/shape-design-principles/) — how these apply at the ontology level.
