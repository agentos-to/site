---
title: user_identity
description: "An identity claim — 'the engine-level user X identifies as person:Y"
sidebar:
  label: user_identity
---

An identity claim — "the engine-level user X identifies as person:Y
in volume Z". Phase 5 of the volumes spec; lets one OS user map onto
multiple persona-nodes across multiple mounted volumes.

`user_id` is foreign to `engine.db::users` — the engine's user
table — not to a graph node. A user_identity row is the bridge.

Many mappings per user are normal:
user joe → person:joe in users/joe.db                 (active=true)
user joe → person:harry_potter in pods/hp.db          (active=false; role-play)
user joe → person:joe_health_subject in pods/health.db (active=true; explicit subject)

The `active` flag picks the "default" person inside each volume when
the user has multiple mappings into the same one.

| Metadata | Value |
|---|---|
| **Plural** | `user_identities` |
| **Subtitle field** | `volume_id` |

## Fields

| Field | Type |
|---|---|
| `user_id` | `string` |
| `volume_id` | `string` |
| `person_node_id` | `string` |
| `active` | `boolean` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[Solid (Tim Berners-Lee)](https://solidproject.org/faq)** — Solid Pod ↔ WebID is the per-user identity model. A Solid user owns one personal pod whose WebID is the authoritative identity; cross-pod identity is a single relation. We split: User is engine state; Person is graph content; user_identity is the explicit bridge that can be many-to-many across volumes.
- **[Unix/macOS — /etc/passwd vs /Users/<u>](https://en.wikipedia.org/wiki/Passwd)** — OS users (engine.db::users) and home directories (~/.agentos/users/<u>.db) follow the Unix convention. The identity *within* the home is content the home owns.
