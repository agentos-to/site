---
title: readme
description: "Orient yourself"
sidebar:
  label: readme
---

# `readme` namespace

Orient yourself. Read this first, every session.

## Ops

- [`get`](#get) — Identity, tools, and the roadmap for your working directory

## `get`

Identity, tools, and the roadmap for your working directory.

### Examples

```js
readme()
readme({ cwd: "/path/to/project" })
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {
    "cwd": {
      "description": "Working directory to orient against. Optional \u2014 defaults to the session's directory (MCP clients supply it via roots; the CLI passes $PWD).",
      "type": "string"
    }
  },
  "type": "object"
}
```
