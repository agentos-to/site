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

## `load`

Load a skill manual (readme + tool list) before calling run.

### Examples

```js
load({ skill: "exa" })
```
