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
