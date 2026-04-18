---
title: memex
description: "A memex — a portable knowledge graph. Named for Vannevar Bush's"
sidebar:
  label: memex
---

A memex — a portable knowledge graph. Named for Vannevar Bush's
1945 vision of a personal knowledge store with associative trails.

A memex is a SQLite database file containing entities, relationships,
and trails. It's the "disk image" to a simulation's "VM" — persistent
knowledge that can be loaded, forked, snapshotted, and shared.

Types: personal (your mind), domain (expertise), snapshot (point-in-time),
fork (experimental copy), community (published for others).

Plural is "memex" (same word, like aircraft or fish).

Examples: joe.db (personal), astronomy.db (domain), spacex-history.db (community)

| Metadata | Value |
|---|---|
| **Plural** | `memex` |
| **Subtitle field** | `description` |

## Fields

| Field | Type |
|---|---|
| `description` | `text` |
| `origin` | `string` |
| `filePath` | `string` |
| `nodeCount` | `integer` |
| `edgeCount` | `integer` |
| `fileSize` | `string` |
| `snapshotOf` | `datetime` |
| `published` | `boolean` |

## Relations

| Relation | Target |
|---|---|
| `owner` | [`person`](/shapes/reference/person/) |
| `forkedFrom` | [`memex`](/shapes/reference/memex/) |
| `snapshots` | [`memex[]`](/shapes/reference/memex/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[Vannevar Bush — "As We May Think" (1945)](https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/)** — The original concept. Our memex is named after and modeled on Bush's personal knowledge store with associative trails.
- **[W3C RDF 1.1 + Named Graphs](https://www.w3.org/TR/rdf11-concepts/)** — Formal underpinning. Our nodeCount/edgeCount mirror RDF subject-predicate-object triples; snapshots ≈ named-graph versioning.
- **[Roam Research / Obsidian / Logseq PKM model](https://obsidian.md/)** — Practical modern precedents. Our origin values (personal, domain, fork) generalize the single-user PKM model to shareable graphs.
