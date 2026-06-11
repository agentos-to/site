---
title: user
description: "An AgentOS user — the seat at this machine. Carries the user's"
sidebar:
  label: user
---

An AgentOS user — the seat at this machine. Carries the user's
preference state: pref:ui (render) and pref:system (engine behavior),
resolved through the V6/V8 cascade alongside shape-def + instance
overrides. Linked to a person via --identified_as--> when the user
is human-identified; linkless users are anonymous.

Distinct from `person` (universal human shape — schema.org / vCard)
and `agent` (AI actor). person stays clean of AgentOS-specific
fields; user is the carrier for everything OS-runtime.

`prefsSchemas` (top-level metadata, not a per-instance field) declares
the universal pref vocabulary for AgentOS users. The engine seeds
these onto the USER shape-def node at boot; SettingsPanel reads them
off the def, walks the entries, and writes resolved values back to
the active user instance under `pref:<namespace>`. The cascade does
the rest.

| Metadata | Value |
|---|---|
| **Plural** | `users` |
| **Subtitle field** | `name` |
| **Identity (any)** | `osUsername` |
| **Also** | [`actor`](/shapes/reference/actor/) |

## Fields

| Field | Type |
|---|---|
| `osUsername` | `string` |
| `primaryUser` | `boolean` |

## Relations

| Relation | Target |
|---|---|
| `identified_as` | [`person`](/shapes/reference/person/) |

## Inherited

From [`actor`](/shapes/reference/actor/):

| Field | Type |
|---|---|
| `actorType` | `string` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[POSIX getpwuid (passwd database)](https://pubs.opengroup.org/onlinepubs/9699919799/functions/getpwuid.html)** — The OS-level "user" — uid + login name + home dir. Our `osUsername` mirrors `pw_name`; identity-by-OS-account follows the same pattern. We diverge by separating the OS seat (`user`) from the human (`person`); POSIX conflates them.
- **[schema.org/Audience](https://schema.org/Audience)** — Loose fit. schema.org has no "OS user" concept — user accounts are product-specific. We model it explicitly because AgentOS is the product, and the user-as-pref-carrier is load-bearing.
- **[macOS NSUserDefaults](https://developer.apple.com/documentation/foundation/nsuserdefaults)** — The Apple model: per-user preference store, keyed by the OS account. Our `pref:ui` / `pref:system` blobs play the same role, but live in the graph (queryable, multi-process safe) rather than a plist file.
