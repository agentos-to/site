---
title: apps
description: "App introspection and direct dispatch"
sidebar:
  label: apps
---

# `apps` namespace

App introspection and direct dispatch.

## Ops

- [`run`](#run) — Execute an app tool directly
- [`load`](#load) — Load an app manual (readme + tool list + per-connection auth state) before calling run
- [`connect`](#connect) — Store a credential for an app connection (api-key connections)
- [`disable`](#disable) — Switch a plugin off: it drops out of matchmaking, run, and readme()'s tool list
- [`enable`](#enable) — Switch a disabled plugin back on
- [`accounts`](#accounts) — Every account + every app connection with auth kind, status, identifier, and freshness — the identity surface behind the apps

## `run`

Execute an app tool directly.

### Examples

```js
run({ app: "exa", tool: "search", params: { query: "..." } })
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {
    "account": {
      "description": "Force a specific credential/account when the app has multiple.",
      "type": "string"
    },
    "app": {
      "description": "App id (e.g. \"exa\").",
      "type": "string"
    },
    "execute": {
      "description": "Live-execution override; consult the app manifest for accepted shapes."
    },
    "params": {
      "description": "Op-level params forwarded to the app.",
      "type": "object"
    },
    "provider": {
      "description": "Force a cookie provider (e.g. \"brave-browser\").",
      "type": "string"
    },
    "remember": {
      "description": "Persist the live result to the graph. Default true.",
      "type": "boolean"
    },
    "tool": {
      "description": "Tool name within the app (e.g. \"search\").",
      "type": "string"
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
  "required": [
    "app",
    "tool"
  ],
  "type": "object"
}
```

## `load`

Load an app manual (readme + tool list + per-connection auth state) before calling run.

### Examples

```js
load({ app: "exa" })
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {
    "app": {
      "description": "App id to load (readme + tool list).",
      "type": "string"
    }
  },
  "required": [
    "app"
  ],
  "type": "object"
}
```

## `connect`

Store a credential for an app connection (api-key connections). Encrypted vault row + account node; the secret never lands in the graph. Returns the app's per-connection auth state.

### Examples

```js
connect({ app: "firecrawl", key: "fc-..." })
connect({ app: "porkbun", key: "pk1_...:sk1_..." })
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {
    "app": {
      "description": "App id (e.g. \"porkbun\").",
      "type": "string"
    },
    "connection": {
      "description": "Connection name. Optional when the app declares exactly one authenticated connection.",
      "type": "string"
    },
    "identifier": {
      "description": "Account identity at the service (email/handle), when known.",
      "type": "string"
    },
    "key": {
      "description": "The API key/secret. For multi-part keys, use the format the app's manual states (e.g. porkbun: \"apikey:secretapikey\").",
      "type": "string"
    },
    "label": {
      "description": "Display label for the credential.",
      "type": "string"
    },
    "value": {
      "description": "Alternative to key: explicit secret fields ({ field: secret, \u2026 }).",
      "type": "object"
    }
  },
  "required": [
    "app"
  ],
  "type": "object"
}
```

## `disable`

Switch a plugin off: it drops out of matchmaking, run, and readme()'s tool list. The graph node and any stored credentials stay; enable reverses it.

### Examples

```js
disable({ app: "porkbun" })
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {
    "app": {
      "description": "Plugin (app) id to switch off \u2014 it drops out of matchmaking, run, and readme until re-enabled.",
      "type": "string"
    }
  },
  "required": [
    "app"
  ],
  "type": "object"
}
```

## `enable`

Switch a disabled plugin back on.

### Examples

```js
enable({ app: "porkbun" })
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {
    "app": {
      "description": "Plugin (app) id to switch back on.",
      "type": "string"
    }
  },
  "required": [
    "app"
  ],
  "type": "object"
}
```

## `accounts`

Every account + every app connection with auth kind, status, identifier, and freshness — the identity surface behind the apps.

### Examples

```js
accounts()
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {
    "view": {
      "additionalProperties": false,
      "properties": {
        "format": {
          "enum": [
            "markdown",
            "json",
            "text"
          ],
          "type": "string"
        }
      },
      "type": "object"
    }
  },
  "type": "object"
}
```
