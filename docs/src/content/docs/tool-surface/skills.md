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
- [`load`](#load) — Load a skill manual (readme + tool list) before calling run

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

Load a skill manual (readme + tool list) before calling run.

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
