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
- [`list`](#list) — List nodes by shape, user_tag, name match, FTS via `q`, system metadata, or skill membership
- [`update`](#update) — Set or delete vals on an existing node
- [`create`](#create) — Create a node (`{shape, name?, vals?, identity?}`), or a relationship (`{from, label, to}`)
- [`delete`](#delete) — Soft-delete a node or relationship
- [`restore`](#restore) — Restore a soft-deleted node

## `read`

Read one node (or link) by id.

### Examples

```js
read({ id: "abc123" })
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {
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
    }
  },
  "required": [
    "id"
  ],
  "type": "object"
}
```

## `list`

List nodes by shape, user_tag, name match, FTS via `q`, system metadata, or skill membership.

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
  "description": "Pass exactly one of shape | user_tag | name | about | skill | q. The handler rejects empty calls.",
  "properties": {
    "about": {
      "description": "Engine introspection (e.g. \"shapes\").",
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
    "skill": {
      "description": "List entities (or skill manifest with type=\"entity\") for this skill.",
      "type": "string"
    },
    "type": {
      "description": "Modifier for `skill`: list entities (vs. the skill manifest).",
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
create({ shape: "bookmark", name: "Aircraft", vals: { address: "?shape=aircraft" } })
create({ shape: "person", name: "Joe", identity: { email: "joe@example.com" } })
create({ from: "abc123", label: "measures", to: "def456" })
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
      "description": "Link form: target node id.",
      "type": "string"
    },
    "vals": {
      "description": "Node form: initial vals. Same shape as data.update vals.",
      "type": "object"
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
