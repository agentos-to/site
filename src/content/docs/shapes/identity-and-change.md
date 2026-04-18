---
title: Identity & change
description: Every actor has an identity. Every change is an entity. How AgentOS captures provenance without a separate audit log.
---

Two rules, one consequence:

1. **Every actor has an identity.**
2. **Changes are entities.**

Put these together and provenance stops being a bolt-on audit log — it becomes native graph structure.

## Every actor has an identity

The human owner, each AI agent, and the system itself are all entities on the graph. When the human edits a task, the change is attributed to them. When an agent creates a plan, it's attributed to that agent. Every change has a *who*.

This is **identification, not authentication** — on a single-user local system, localhost binding is the access boundary. We're not gatekeeping *who can act*; we're recording *who did*.

- **The human owner** — one entity per AgentOS install. Your edits.
- **AI agents** — Claude, Cursor, your custom skills. Each a distinct entity.
- **The system** — automated processes like sync, indexing, migration. Attributed to a `system` actor, not hidden.

## Changes are entities

When an entity is created, updated, or deleted, the operation itself becomes a **change entity** on the graph. A change has relationships to:

- the **actor** (who did it)
- the **target** (what changed)
- optionally the **source** (where data came from — a platform, a file, an API response)

This follows the pattern established by W3C PROV-O, ActivityStreams, and Git: make events first-class objects, not edges.

## Provenance as traversal

Because changes are entities, provenance isn't a static field — it's the full chain of change entities. Walk backwards to reconstruct any previous state.

- "Who last edited this task?" — the newest change entity pointing at the task.
- "When did this email arrive?" — the creation change for the message entity.
- "Did the agent modify this, or did I?" — the actor on the most recent change.
- "Show me everything that happened yesterday" — query change entities by time.

No audit log table. No `created_by` / `updated_at` duplication per entity. One change shape, used universally.

## Prior art

- **W3C PROV-O** — provenance ontology: agent, activity, entity. This is the pattern.
- **ActivityStreams / ActivityPub** — the fediverse's answer to "what happened?" is an activity entity with an actor.
- **Git** — every commit is an entity with an author, a parent, and a diff. Same pattern, different domain.

See [Research → Relationships and events](/research/relationships-and-events/causal-chains-entity-graphs/) for deeper background.

## See also

- [Design principles](/architecture/design-principles/) — "changes are entities" and "every actor has an identity" listed among the first-principles rules.
- [Ontology overview](/shapes/overview/) — the `change` and `actor` shapes.
