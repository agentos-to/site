---
title: windows
description: "Query and drive the desktop shell's windows — by route and policy, not pixels"
sidebar:
  label: windows
---

# `windows` namespace

Query and drive the desktop shell's windows — by route and policy, not pixels. Requires the AgentOS desktop to be open; every mutation renders live and lands as an activity on the graph.

## Ops

- [`list`](#list) — Every open window: id, route, title, bounds, size policy, focused, minimized
- [`read`](#read) — A window's content as a graph read — the window's route plus its hydrated subject node
- [`open`](#open) — Open a window at a route — the same spawn/dedup path a human launch takes
- [`close`](#close) — Close a window by id
- [`focus`](#focus) — Bring a window to the front (restores if minimized)
- [`move`](#move) — Move a window to (x, y)
- [`resize`](#resize) — Resize a free-sized window
- [`respond`](#respond) — Shell-internal: the desktop delivers a command's result back to the engine

## `list`

Every open window: id, route, title, bounds, size policy, focused, minimized.

### Examples

```js
list({})
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {},
  "type": "object"
}
```

## `read`

A window's content as a graph read — the window's route plus its hydrated subject node. No DOM scraping; views and apps have no subject (null).

### Examples

```js
read({ id: "window-…" })
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {
    "id": {
      "description": "Window id (from windows.list / windows.open).",
      "type": "string"
    }
  },
  "required": [
    "id"
  ],
  "type": "object"
}
```

## `open`

Open a window at a route — the same spawn/dedup path a human launch takes. Returns the window id.

### Examples

```js
open({ route: "node/abc123" })
open({ route: "?app=display&tab=Background", bounds: { x: 200, y: 120 } })
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {
    "bounds": {
      "additionalProperties": false,
      "description": "Optional initial position/size. Omitted fields fall to saved position, then cascade.",
      "properties": {
        "height": {
          "type": "number"
        },
        "width": {
          "type": "number"
        },
        "x": {
          "type": "number"
        },
        "y": {
          "type": "number"
        }
      },
      "type": "object"
    },
    "route": {
      "description": "Shell route to open \u2014 `node/<id>`, `?list=<id>`, `?app=<id>`, or a view query. Same dedup as a human launch: an existing window at the route is focused, not duplicated.",
      "type": "string"
    }
  },
  "required": [
    "route"
  ],
  "type": "object"
}
```

## `close`

Close a window by id.

### Examples

```js
close({ id: "window-…" })
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {
    "id": {
      "description": "Window id (from windows.list / windows.open).",
      "type": "string"
    }
  },
  "required": [
    "id"
  ],
  "type": "object"
}
```

## `focus`

Bring a window to the front (restores if minimized).

### Examples

```js
focus({ id: "window-…" })
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {
    "id": {
      "description": "Window id (from windows.list / windows.open).",
      "type": "string"
    }
  },
  "required": [
    "id"
  ],
  "type": "object"
}
```

## `move`

Move a window to (x, y).

### Examples

```js
move({ id: "window-…", x: 300, y: 160 })
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {
    "id": {
      "description": "Window id.",
      "type": "string"
    },
    "x": {
      "type": "number"
    },
    "y": {
      "type": "number"
    }
  },
  "required": [
    "id",
    "x",
    "y"
  ],
  "type": "object"
}
```

## `resize`

Resize a free-sized window. Fit windows refuse — their size derives from content (policy is law).

### Examples

```js
resize({ id: "window-…", width: 900, height: 640 })
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {
    "height": {
      "type": "number"
    },
    "id": {
      "description": "Window id. Free-sized windows only \u2014 a fit window's size derives from its content and the shell refuses to override it.",
      "type": "string"
    },
    "width": {
      "type": "number"
    }
  },
  "required": [
    "id",
    "width",
    "height"
  ],
  "type": "object"
}
```

## `respond`

Shell-internal: the desktop delivers a command's result back to the engine. Agents never call this.

### Input schema

```json
{
  "additionalProperties": false,
  "description": "Shell-internal: the desktop delivers a command's result. Not for agents.",
  "properties": {
    "command": {
      "description": "The shell_command event's command id.",
      "type": "string"
    },
    "decline": {
      "description": "This shell doesn't own the targeted window \u2014 another desktop's answer settles the command.",
      "type": "boolean"
    },
    "error": {
      "description": "Why execution was refused, when it was.",
      "type": "string"
    },
    "result": {
      "description": "The executed command's result."
    }
  },
  "required": [
    "command"
  ],
  "type": "object"
}
```
