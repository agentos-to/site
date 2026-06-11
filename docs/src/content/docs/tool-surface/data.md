---
title: data
description: "Query and mutate graph entities"
sidebar:
  label: data
---

# `data` namespace

Query and mutate graph entities.

## Ops

- [`read`](#read) — Read one node (or link) by id
- [`list`](#list) — List nodes by shape, user_tag, name match, FTS via `q`, system metadata, or app membership
- [`update`](#update) — Set or delete vals on an existing node
- [`create`](#create) — Create a node (`{shape, name?, vals?, identity?}`), or a relationship (`{from, label, to}`)
- [`delete`](#delete) — Soft-delete a node or relationship
- [`restore`](#restore) — Restore a soft-deleted node
- [`resolve`](#resolve) — Resolve an address (node/link id, or handle) to its target's identity — node_id, volume, shapes, listType, name, via — without reading content
- [`export`](#export) — Export a typed subgraph to a SQLite artifact
- [`import`](#import) — Import a previously-exported artifact, replaying any migration chain from its pin to live SCHEMA_HASH
- [`mount`](#mount) — Mount a memex `
- [`unmount`](#unmount) — Detach a mounted Volume by volume_id (the slug)
- [`volume_stats`](#volume_stats) — Disk + content statistics for a Volume: file size on disk, node count, shape histogram, schema version

## `read`

Read one node (or link) by id. On a volume read, add `expand`/`depth` to get a hydrated nested subtree (the whole tree in one call) following containment edges — see the `expand` param.

### Examples

```js
read({ id: "abc123" })
read({ id: "roadmap", volume: "agentos-roadmap", depth: 4 })
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {
    "depth": {
      "description": "SUBTREE PROJECTION (volume reads): hops to follow `expand` edges. Default 4. Supplying `expand` or `depth` switches read into subtree mode.",
      "minimum": 0,
      "type": "integer"
    },
    "expand": {
      "description": "SUBTREE PROJECTION (volume reads): containment edge labels to follow from this node, e.g. [\"contains\",\"owns\",\"has_step\"]. Returns a hydrated, NESTED tree (each child under `children`, with `_via` = the label) instead of a flat node \u2014 the whole subtree in ONE call. Reference edges (depends_on, upholds, serves, \u2026) are never expanded. If omitted but `depth` is set, defaults to the containment spine (contains/owns/has_step/has_part).",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "fields": {
      "description": "SUBTREE PROJECTION: project each node's vals to this subset (id/name/shape always kept).",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "id": {
      "description": "Node or link id.",
      "type": "string"
    },
    "view": {
      "additionalProperties": false,
      "properties": {
        "content_length": {
          "description": "Max chars for content body. Integer, or the string \"full\"."
        },
        "depth": {
          "description": "Link-traversal depth. 0 = no relationships.",
          "minimum": 0,
          "type": "integer"
        },
        "fields": {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "format": {
          "enum": [
            "markdown",
            "json",
            "text"
          ],
          "type": "string"
        },
        "include": {
          "description": "Named projections (createdAt, modifiedAt, lastActivity).",
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "rel_limit": {
          "minimum": 0,
          "type": "integer"
        }
      },
      "type": "object"
    },
    "volume": {
      "description": "Which Volume to read from. Defaults to \"home\". A mounted memex's volume_id targets that memex's pool.",
      "type": "string"
    }
  },
  "required": [
    "id"
  ],
  "type": "object"
}
```

## `list`

List nodes by shape, user_tag, name match, FTS via `q`, system metadata, or app membership.

### Examples

```js
list({ shape: "task", priority: 1 })
list({ user_tag: "follow-up" })
list({ q: "meeting", limit: 10 })
list({ about: "shapes" })
```

### Input schema

```json
{
  "additionalProperties": false,
  "description": "Pass exactly one of shape | user_tag | name | about | app | q. The handler rejects empty calls.",
  "properties": {
    "about": {
      "description": "Engine introspection (e.g. \"shapes\").",
      "type": "string"
    },
    "app": {
      "description": "List entities (or app manifest with type=\"entity\") for this app.",
      "type": "string"
    },
    "limit": {
      "description": "Max rows. Defaults vary per filter.",
      "minimum": 1,
      "type": "integer"
    },
    "name": {
      "description": "Substring match against node names.",
      "type": "string"
    },
    "q": {
      "description": "FTS query \u2014 folds the previous `data.search` op.",
      "type": "string"
    },
    "query": {
      "description": "Legacy alias for q. Prefer q.",
      "type": "string"
    },
    "shape": {
      "description": "Shape name (e.g. \"task\") or array of shape names (union).",
      "oneOf": [
        {
          "type": "string"
        },
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        }
      ]
    },
    "type": {
      "description": "Modifier for `app`: list entities (vs. the app manifest).",
      "enum": [
        "entity"
      ],
      "type": "string"
    },
    "user_tag": {
      "description": "User-tag name (or array \u2014 intersection).",
      "oneOf": [
        {
          "type": "string"
        },
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        }
      ]
    },
    "view": {
      "additionalProperties": false,
      "properties": {
        "content_length": {},
        "depth": {
          "minimum": 0,
          "type": "integer"
        },
        "fields": {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "format": {
          "enum": [
            "markdown",
            "json",
            "text"
          ],
          "type": "string"
        },
        "include": {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "rel_limit": {
          "minimum": 0,
          "type": "integer"
        }
      },
      "type": "object"
    },
    "volume": {
      "description": "Which Volume to list from. Defaults to \"home\". Mutually exclusive with `volumes`.",
      "type": "string"
    },
    "volumes": {
      "description": "Federation: union across multiple Volumes. Array of ids, or the string \"all\" for every mounted Volume.",
      "oneOf": [
        {
          "type": "string"
        },
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        }
      ]
    }
  },
  "type": "object"
}
```

## `update`

Set or delete vals on an existing node. `null` value deletes a val; non-null sets it. Unit auto-inferred from JSON type when not given.

### Examples

```js
update({ id: "abc123", vals: { "pref:ui": { themeId: "xp", fontSize: 14 } } })
update({ id: "abc123", vals: { name: "Renamed" } })
update({ id: "abc123", vals: { "pref:legacy": null } })
```

### Input schema

```json
{
  "additionalProperties": false,
  "description": "Pass exactly one of `id` (node) or `link` (link val). Link val deletion is not supported \u2014 pass a non-null value.",
  "properties": {
    "id": {
      "description": "Node id to update.",
      "type": "string"
    },
    "link": {
      "description": "Link id to update (writes link_vals \u2014 icon position, fares, etc.).",
      "type": "string"
    },
    "vals": {
      "additionalProperties": true,
      "description": "Map of val key \u2192 value. `null` deletes (nodes only). Non-null sets. Object form `{value, unit}` overrides the inferred unit.",
      "type": "object"
    },
    "volume": {
      "description": "Which Volume to write to. Defaults to \"home\". Errors on read-only mounts.",
      "type": "string"
    }
  },
  "required": [
    "vals"
  ],
  "type": "object"
}
```

## `create`

Create a node (`{shape, name?, vals?, identity?}`), or a relationship (`{from, label, to}`). With `identity`, an existing node is updated instead of duplicated (upsert semantics).

### Examples

```js
create({ shape: "person", name: "Joe", identity: { email: "joe@example.com" } })
create({ from: "abc123", label: "measures", to: "def456" })
// bookmark: a named handle → any node, one atomic call
create({ shape: "bookmark", vals: { handle: "home" }, links_out: [{ label: "points_to", target_id: "<node-id>" }] })
```

### Input schema

```json
{
  "additionalProperties": false,
  "oneOf": [
    {
      "required": [
        "shape"
      ]
    },
    {
      "required": [
        "from",
        "label",
        "to"
      ]
    }
  ],
  "properties": {
    "from": {
      "description": "Link form: source node id.",
      "type": "string"
    },
    "identity": {
      "description": "Node form: scalar (key, value) pairs. With `identity`, an existing match is updated instead of duplicated (upsert semantics).",
      "type": "object"
    },
    "label": {
      "description": "Link form: relationship label.",
      "type": "string"
    },
    "name": {
      "description": "Node form: display name for the node.",
      "type": "string"
    },
    "shape": {
      "description": "Node form: shape name. Lazily registered on first use.",
      "type": "string"
    },
    "to": {
      "description": "Link form: target node id. Accepts the qualified `\"<volume_id>:<node_id>\"` form to bridge into a mounted memex.",
      "type": "string"
    },
    "vals": {
      "description": "Node form: initial vals. Same shape as data.update vals.",
      "type": "object"
    },
    "volume": {
      "description": "Which Volume to write the new node/link in. Defaults to \"home\". Errors on read-only mounts.",
      "type": "string"
    }
  },
  "type": "object"
}
```

## `delete`

Soft-delete a node or relationship. With `permanent: true`, hard-delete a soft-deleted node (purge).

### Examples

```js
delete({ id: "abc123" })
delete({ id: "abc123", permanent: true })
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {
    "id": {
      "description": "Node or link id. Soft-delete.",
      "type": "string"
    },
    "permanent": {
      "description": "When true, hard-delete a soft-deleted node (purge from disk). Used by 'empty trash'.",
      "type": "boolean"
    },
    "volume": {
      "description": "Which Volume to delete from. Defaults to \"home\". Errors on read-only mounts.",
      "type": "string"
    }
  },
  "required": [
    "id"
  ],
  "type": "object"
}
```

## `restore`

Restore a soft-deleted node. Flips deleted_at back to null on the node and on the original cascade batch of links. Emits an activity record.

### Examples

```js
restore({ id: "abc123" })
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {
    "id": {
      "description": "Soft-deleted node id. Flips deleted_at back to null on the node and on every link in the original cascade batch.",
      "type": "string"
    }
  },
  "required": [
    "id"
  ],
  "type": "object"
}
```

## `resolve`

Resolve an address (node/link id, or handle) to its target's identity — node_id, volume, shapes, listType, name, via — without reading content. The kernel resolver's public face: identity before acting.

### Examples

```js
resolve({ address: "desktop" })
resolve({ address: "abc123" })
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {
    "address": {
      "description": "Any address \u2014 a node/link id, or a handle. Resolved by the same kernel resolver every data op uses: literal id wins, then handle \u2192 bookmark \u2192 points_to target.",
      "type": "string"
    }
  },
  "required": [
    "address"
  ],
  "type": "object"
}
```

## `export`

Export a typed subgraph to a SQLite artifact. Writes _meta.schema_version pin for safe re-import.

### Examples

```js
export({ selection: { shapes: ["health-*"] }, out_path: "~/health.db", label: "Health profile" })
export({ selection: { shapes: ["transaction", "account"] }, out_path: "~/finance.db", label: "Finance 2026" })
export({ selection: { nodes: ["abc123"] }, out_path: "~/seed.db", closure: { max_depth: 2 } })
export({ selection: { all: true }, out_path: "~/full.db" })
```

### Input schema

```json
{
  "additionalProperties": false,
  "description": "Export a typed subgraph to a self-describing memex `.db` file. Stamps `_meta.type='memex'` and embeds referenced shape definitions. Returns artifact file:// URI + counts + schema_version pin.",
  "properties": {
    "closure": {
      "additionalProperties": false,
      "description": "Optional closure filters. V1 walks every link by default.",
      "properties": {
        "exclude_links": {
          "description": "Never follow these labels.",
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "include_deleted": {
          "description": "Include soft-deleted nodes/links. Default false.",
          "type": "boolean"
        },
        "include_links": {
          "description": "If non-empty, only follow these labels.",
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "max_depth": {
          "description": "Hop budget from any seed. Unbounded if omitted.",
          "minimum": 0,
          "type": "integer"
        }
      },
      "type": "object"
    },
    "description": {
      "description": "One-paragraph human description of what this memex contains. Persisted to _meta.description.",
      "minLength": 1,
      "type": "string"
    },
    "icon": {
      "description": "Icon-shape `purpose` name (e.g. \"book\", \"heart\", \"home\"). Persisted to _meta.icon. Theme adapters resolve names to renderable assets.",
      "minLength": 1,
      "type": "string"
    },
    "name": {
      "description": "Display name for the memex \u2014 \"Joe Health\", \"Bible\", \"US IP Law (2026)\". Persisted to _meta.name.",
      "minLength": 1,
      "type": "string"
    },
    "out_path": {
      "description": "Destination path (~ expanded). Existing file is overwritten.",
      "type": "string"
    },
    "selection": {
      "additionalProperties": false,
      "description": "One of {all: true} (full-DB backup \u2014 bypasses closure, includes orphans + trash by default), {shapes: [..]} (type-driven closure), or {nodes: [..]} (explicit seeds + closure).",
      "oneOf": [
        {
          "required": [
            "all"
          ]
        },
        {
          "required": [
            "shapes"
          ]
        },
        {
          "required": [
            "nodes"
          ]
        }
      ],
      "properties": {
        "all": {
          "type": "boolean"
        },
        "nodes": {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "shapes": {
          "items": {
            "type": "string"
          },
          "type": "array"
        }
      },
      "type": "object"
    }
  },
  "required": [
    "selection",
    "out_path",
    "name",
    "icon",
    "description"
  ],
  "type": "object"
}
```

## `import`

Import a previously-exported artifact, replaying any migration chain from its pin to live SCHEMA_HASH.

### Examples

```js
import({ in_path: "~/health.db" })
import({ in_path: "~/health.db", plan_only: true })
```

### Input schema

```json
{
  "additionalProperties": false,
  "description": "Import a previously-exported artifact, replaying any migration chain from its pin to live SCHEMA_HASH.",
  "properties": {
    "in_path": {
      "description": "Artifact path (~ expanded). SQLite for v1.",
      "type": "string"
    },
    "on_id_collision": {
      "description": "Default merge: overwrite vals + ensure links/shapes/content on existing id.",
      "enum": [
        "merge",
        "skip",
        "error"
      ],
      "type": "string"
    },
    "on_schema_drift": {
      "description": "Default migrate: replay chain from artifact pin to live.",
      "enum": [
        "migrate",
        "error"
      ],
      "type": "string"
    },
    "plan_only": {
      "description": "Compute the diff + per-row category, do not write.",
      "type": "boolean"
    }
  },
  "required": [
    "in_path"
  ],
  "type": "object"
}
```

## `mount`

Mount a memex `.db` file as a read-only Volume. Persists a volume node + emits a create activity. Survives engine restart.

### Examples

```js
mount({ path: "~/bible.db" })
mount({ path: "/Users/joe/dev/agentos/_joe/health.db" })
```

### Input schema

```json
{
  "additionalProperties": false,
  "description": "Mount a memex `.db` file as a read-only Volume. Verifies _meta.type='memex', derives a kebab-case volume_id, persists a `volume`-shape node in the System mount registry, and emits an activity. Survives engine restart via auto_mount=true.",
  "properties": {
    "path": {
      "description": "Path to a memex `.db` file (~ expanded). Must carry _meta.type='memex'.",
      "type": "string"
    }
  },
  "required": [
    "path"
  ],
  "type": "object"
}
```

## `unmount`

Detach a mounted Volume by volume_id (the slug). Soft-deletes the volume node + emits a delete activity. File on disk is untouched.

### Examples

```js
unmount({ id: "joe-health" })
```

### Input schema

```json
{
  "additionalProperties": false,
  "description": "Detach a mounted Volume by its volume_id (the slug \u2014 e.g. \"joe-health\"). Soft-deletes the matching `volume` node in home and emits a delete activity. The `.db` file on disk is untouched.",
  "properties": {
    "id": {
      "description": "Volume id (the slug returned by data.mount), NOT the graph node id.",
      "type": "string"
    }
  },
  "required": [
    "id"
  ],
  "type": "object"
}
```

## `volume_stats`

Disk + content statistics for a Volume: file size on disk, node count, shape histogram, schema version. Powers Properties' General tab (used space, node count) and the shape donut. Defaults to the home Volume when `id` is omitted.

### Examples

```js
volume_stats({})                       // home
volume_stats({ id: "joe-health" })     // a mounted pod
```

### Input schema

```json
{
  "additionalProperties": false,
  "description": "Disk + content statistics for a Volume. Defaults to the home Volume when `id` is omitted; accepts \"home\" / \"memex\" for the home vault and the slug (e.g. \"joe-health\") for a mounted pod.",
  "properties": {
    "id": {
      "description": "Volume id slug. Accepts \"home\" / \"memex\" for the home vault. Defaults to \"home\" when omitted.",
      "type": "string"
    }
  },
  "type": "object"
}
```
