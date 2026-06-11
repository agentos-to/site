---
title: volume
description: "A mounted Volume — any named source of typed nodes the engine has"
sidebar:
  label: volume
---

A mounted Volume — any named source of typed nodes the engine has
attached to the Registry: a `.db` memex file, a YAML text volume, or a
transport volume served live by a skill (the host filesystem, a USB
stick, a browser's data). The home graph is the always-mounted
writeable Volume; it is the hardcoded constant. Every OTHER mount IS a
`volume` node — one row per mount, persisted so the mount survives
engine restart (`auto_mount: true`).

Mount lifecycle is six steps; this shape captures the persisted state
of step 5. See `core/_roadmap/p2/realms-transports/plan.md`.

| Metadata | Value |
|---|---|
| **Plural** | `volumes` |
| **Subtitle field** | `kind` |

## Fields

| Field | Type |
|---|---|
| `volume_id` | `string` |
| `kind` | `string` |
| `address` | `string` |
| `provider` | `string` |
| `auto_mount` | `boolean` |
| `readOnly` | `boolean` |
| `removable` | `boolean` |
| `totalBytes` | `integer` |
| `freeBytes` | `integer` |
| `scope` | `string` |
| `icon` | `string` |
| `default_view` | `string` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[HDT (Header, Dictionary, Triples)](https://www.rdfhdt.org/what-is-hdt/)** — RDF binary file format; one file = one queryable graph. The Header describes the dataset in its own vocabulary — same shapes-ride-along move as our embedded ontology.
- **[Stardog Virtual Graphs](https://docs.stardog.com/virtual-graphs/)** — Register an external source under a URI; query as a named graph. Our volume shape is the registration row; mount/unmount is the verb pair.
- **[macOS Disk Utility / DMG](https://support.apple.com/guide/disk-utility/welcome/mac)** — The UX mental model. A volume is an attached, browseable disk; the Finder shows it in the sidebar; eject detaches it without destroying the underlying file.
