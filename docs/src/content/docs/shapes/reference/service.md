---
title: service
description: "A service — a named interface the engine brokers between strangers."
sidebar:
  label: service
---

A service — a named interface the engine brokers between strangers.
The caller names the interface (web_search, web_read, llm), never the
app; the engine matchmakes a provider and dispatches. Rendering is NOT
a service — which app opens/renders a shape or mime is the app shape's
`handles` field, a shell association, not a brokered call.

The registry of canonical services is authored in
`platform/ontology/services/*.yaml` (one file per service; id = file
stem) and projected by codegen into the SDK constants and the engine's
compiled registry. Service NODES on the graph are minted by the engine
from that registry — never authored by hand. Apps point at them with
`provides` edges (link_vals: {via: the bound tool}); the user's
standing pick is a `defaults_to` link from the service node to an app
(XP's "Set Program Access and Defaults").

Keep the registry small and verb-shaped. If a candidate interface has
no second potential provider, it probably isn't a service yet.

| Metadata | Value |
|---|---|
| **Plural** | `services` |
| **Subtitle field** | `description` |
| **Identity** | `id` |

## Fields

| Field | Type |
|---|---|
| `id` | `string` |
| `description` | `text` |
| `params` | `json` |
| `returns` | `string` |

## Relations

| Relation | Target |
|---|---|
| `defaults_to` | [`app`](/shapes/reference/app/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[Debian alternatives system (update-alternatives)](https://wiki.debian.org/DebianAlternatives)** — A generic name (editor) resolves to one of several registered providers via a per-name symlink the admin can repoint. Our service id ≈ the generic name; defaults_to ≈ the symlink.
- **[Windows XP — Set Program Access and Defaults](https://learn.microsoft.com/en-us/windows/win32/shell/default-programs)** — The OS-level "which program answers this kind of request" surface. Our defaults_to link is that choice as graph state.
- **[Android Intents (action + default app)](https://developer.android.com/guide/components/intents-filters)** — Apps declare which actions they answer; the user picks a default per action. provides ≈ intent-filter; defaults_to ≈ the user's "always" choice.
