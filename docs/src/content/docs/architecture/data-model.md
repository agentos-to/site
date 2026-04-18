---
title: Data model
description: How AgentOS stores everything — the three graph primitives, shapes as schema, identity-based deduplication, and why the engine knows nothing about entity types.
---

The entire AgentOS data model fits in three primitives and one idea.

## The three primitives

Everything in AgentOS lives in one SQLite database at `~/.agentos/data/agentos.db`. The schema is tiny:

- **Nodes** — bare identities. A node has an ID and timestamps. That's it.
- **Edges** — labeled, directional links between two nodes (`tagged_with`, `replied_to`, `parent`).
- **Values** — keyed fields on a node (`name = "Joe"`) or on an edge (`weight = 0.8`).

Plus two supporting tables:

- **Content** — large text blobs with full-text search (FTS5-indexed). Used for message bodies, file contents, articles.
- **Settings** — key-value for app-level state that isn't graph-native.

That's the whole database. No `tasks` table, no `messages` table, no type column on nodes. **Semantic type lives in the data, not in the DDL.**

## Shapes as schema

A **shape** is a definition — field names, types, display rules, relations. It has no data. A **record** is a stored instance that conforms to one or more shapes.

Shapes are YAML files in `docs/shapes/` that get loaded into the graph at engine startup. They declare:

- **Fields** — `name: string`, `done: boolean`, `priority: integer`.
- **Relations** — `parent: folder`, `tags: tag[]`.
- **Identity** — which fields uniquely identify a record of this shape.
- **`also` chains** — tag implication. A book is *also* a product, so it inherits product's fields and can be queried as either.

The engine uses the shape registry for type coercion (`"495"` → integer, `"true"` → boolean) and for validation when skills write. It does **not** use the registry to branch on entity types — coercion is a shape-level operation, not a type-level one.

See [Shapes overview](/shapes/overview/) for the authoring format and [Identity & change](/shapes/identity-and-change/) for how identity works across time.

## Identity and deduplication

Every shape declares identity. When a skill writes a record and the identity keys match an existing node, the engine **updates the existing node** instead of creating a duplicate.

Two flavors:

- **`identity: [issuer, identifier]`** — compound. All fields must match.
- **`identity_any: [path, url]`** — alternative. Any one match is enough.

This is how a WhatsApp contact and an iMessage contact with the same phone number become the same `person` node. It's how the same webpage read twice gets one `webpage` node with two `read` activities attached. It's how the graph stays clean without a human deduping.

Identity is also how the graph survives skill churn. Uninstall the WhatsApp skill and the person's WhatsApp handle is still on that person node — edges and values outlive the skill that wrote them.

## How skills write

A skill returns plain Python dicts decorated with the shape name:

```python
@returns("book")
def get_book(isbn: str) -> dict:
    ...
    return {
        "isbn13": "9780140449136",
        "title": "Meditations",
        "author": "Marcus Aurelius",
        "pages": 254,
    }
```

The engine receives that dict, looks up `book` in the shape registry, coerces each field to its declared type, looks up the identity keys (`isbn13, isbn`), and either creates a new node or updates the matching one. Unknown keys are logged as warnings but don't block the write — shape drift is diagnostic, not fatal.

The SDK validator (`agent-sdk validate`) AST-checks return dicts against `@returns(...)` declarations at skill-authoring time. The engine validates again at write time.

## Why the engine is entity-agnostic

The engine knows *about* shapes — field types, relations, identity keys. It does not know *what those fields mean*. It can coerce `priority` to an integer without having any opinion about what priority sorts first. It can follow a `parent` edge without knowing what a parent is.

This is the principle that keeps the engine generic. If the engine ever learned that tasks have priorities and priorities are sortable, every new entity type would require a Rust change. Instead, meaning lives in:

- **[Skills](/skills/overview/)** — they decide what gets extracted and how.
- **[Apps](/apps/overview/)** — they decide how to render, sort, group.
- **Shapes** — they describe the structure everyone agrees on.

See [Architectural laws](/architecture/architectural-laws/) for the full list of things the engine refuses to do.

## Edges as first-class data

Edges are not a join table. They have their own IDs, timestamps, and can carry values. `mentioned_in` can hold `offset` and `length`; `tagged_with` can hold `added_by`.

The edge table is identical in shape to the node table:

```sql
CREATE TABLE edges (
  id          TEXT PRIMARY KEY,
  from_id     TEXT NOT NULL REFERENCES nodes(id),
  label       TEXT NOT NULL,
  to_id       TEXT NOT NULL REFERENCES nodes(id),
  created_at  TEXT,
  updated_at  TEXT,
  deleted_at  TEXT
);
```

And edge values live in `edge_vals`, parallel to `node_vals`. Same story: no type-specific semantics in Rust, just storage.

## What you do with the graph

From an app: read shape-conformant records via the web bridge (`/graph` endpoint, JSON). From a skill: write shape-conformant dicts via `@returns(...)`. From MCP: both, through the engine.

Nobody queries SQL directly. The API surface is the shape registry + the capability broker. The DDL is internal.
