---
title: system
description: "Engine lifecycle"
sidebar:
  label: system
---

# `system` namespace

Engine lifecycle.

## Ops

- [`boot`](#boot) — Session bootstrap: identity, project, recent activity, tools
- [`status`](#status) — Engine snapshot: version, uptime, PID, DB path, recent op stats
- [`schema`](#schema) — Emit the full tool surface registry as JSON — single source of truth for SDK codegen and docs generation (see D11)
- [`schema_hash`](#schema_hash) — Deterministic content hash of the AgentOS ontology — pinned in every data-porter export to detect schema drift on import
- [`schema_diff`](#schema_diff) — Walk the migration chain from a given pin to the current SCHEMA_HASH

## `boot`

Session bootstrap: identity, project, recent activity, tools.

### Examples

```js
boot()
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {},
  "type": "object"
}
```

## `status`

Engine snapshot: version, uptime, PID, DB path, recent op stats.

### Examples

```js
status()
status({ recent: 50 })
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {
    "recent": {
      "description": "Number of recent op events to include. Default 20, capped at the ring capacity.",
      "minimum": 0,
      "type": "integer"
    }
  },
  "type": "object"
}
```

## `schema`

Emit the full tool surface registry as JSON — single source of truth for SDK codegen and docs generation (see D11).

### Examples

```js
system.schema()
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {},
  "type": "object"
}
```

## `schema_hash`

Deterministic content hash of the AgentOS ontology — pinned in every data-porter export to detect schema drift on import.

### Examples

```js
system.schema_hash()
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {},
  "type": "object"
}
```

## `schema_diff`

Walk the migration chain from a given pin to the current SCHEMA_HASH. Returns the ordered list of migration ids that data.import would replay, or a no_chain result with the stuck hash when no migration exists from the current cursor.

### Examples

```js
system.schema_diff({ pin: "sha256:abc..." })
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {
    "pin": {
      "description": "An ontology hash to diff against current \u2014 `sha256:<hex>` (typically from an export's `_meta.schema_version`).",
      "type": "string"
    }
  },
  "required": [
    "pin"
  ],
  "type": "object"
}
```
