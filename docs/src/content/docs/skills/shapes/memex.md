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
| `owner` | [`person`](/docs/reference/shapes/person/) |
| `forkedFrom` | [`memex`](/docs/reference/shapes/memex/) |
| `snapshots` | [`memex[]`](/docs/reference/shapes/memex/) |
