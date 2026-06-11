---
title: skills
description: "Skill introspection and direct dispatch"
sidebar:
  label: skills
---

# `skills` namespace

Skill introspection and direct dispatch.

## Ops

- [`run`](#run) — Execute a skill tool directly
- [`load`](#load) — Load a skill manual (readme + tool list + per-connection auth state) before calling run
- [`connect`](#connect) — Store a credential for a skill connection (api-key connections)
- [`disable`](#disable) — Switch a plugin off: it drops out of matchmaking, run, and readme()'s tool list
- [`enable`](#enable) — Switch a disabled plugin back on
- [`accounts`](#accounts) — Every account + every skill connection with auth kind, status, identifier, and freshness — the identity surface behind the skills

## `run`

Execute a skill tool directly.

### Examples

```js
run({ skill: "exa", tool: "search", params: { query: "..." } })
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {
    "account": {
      "description": "Force a specific credential/account when the skill has multiple.",
      "type": "string"
    },
    "execute": {
      "description": "Live-execution override; consult the skill manifest for accepted shapes."
    },
    "params": {
      "description": "Op-level params forwarded to the skill.",
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
    "skill": {
      "description": "Skill id (e.g. \"exa\").",
      "type": "string"
    },
    "tool": {
      "description": "Tool name within the skill (e.g. \"search\").",
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
    "skill",
    "tool"
  ],
  "type": "object"
}
```

## `load`

Load a skill manual (readme + tool list + per-connection auth state) before calling run.

### Examples

```js
load({ skill: "exa" })
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {
    "skill": {
      "description": "Skill id to load (readme + tool list).",
      "type": "string"
    }
  },
  "required": [
    "skill"
  ],
  "type": "object"
}
```

## `connect`

Store a credential for a skill connection (api-key connections). Encrypted vault row + account node; the secret never lands in the graph. Returns the skill's per-connection auth state.

### Examples

```js
connect({ skill: "firecrawl", key: "fc-..." })
connect({ skill: "porkbun", key: "pk1_...:sk1_..." })
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {
    "connection": {
      "description": "Connection name. Optional when the skill declares exactly one authenticated connection.",
      "type": "string"
    },
    "identifier": {
      "description": "Account identity at the service (email/handle), when known.",
      "type": "string"
    },
    "key": {
      "description": "The API key/secret. For multi-part keys, use the format the skill's manual states (e.g. porkbun: \"apikey:secretapikey\").",
      "type": "string"
    },
    "label": {
      "description": "Display label for the credential.",
      "type": "string"
    },
    "skill": {
      "description": "Skill id (e.g. \"porkbun\").",
      "type": "string"
    },
    "value": {
      "description": "Alternative to key: explicit secret fields ({ field: secret, \u2026 }).",
      "type": "object"
    }
  },
  "required": [
    "skill"
  ],
  "type": "object"
}
```

## `disable`

Switch a plugin off: it drops out of matchmaking, run, and readme()'s tool list. The graph node and any stored credentials stay; enable reverses it.

### Examples

```js
disable({ skill: "porkbun" })
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {
    "skill": {
      "description": "Plugin (skill) id to switch off \u2014 it drops out of matchmaking, run, and readme until re-enabled.",
      "type": "string"
    }
  },
  "required": [
    "skill"
  ],
  "type": "object"
}
```

## `enable`

Switch a disabled plugin back on.

### Examples

```js
enable({ skill: "porkbun" })
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {
    "skill": {
      "description": "Plugin (skill) id to switch back on.",
      "type": "string"
    }
  },
  "required": [
    "skill"
  ],
  "type": "object"
}
```

## `accounts`

Every account + every skill connection with auth kind, status, identifier, and freshness — the identity surface behind the skills.

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
