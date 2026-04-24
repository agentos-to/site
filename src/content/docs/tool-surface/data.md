---
title: data
description: "Query and mutate graph entities"
sidebar:
  label: data
---

# `data` namespace

Query and mutate graph entities.

## Ops

- [`read`](#read) — Read graph data by id, name, tags, shape, or system metadata
- [`search`](#search) — Full-text search over local graph entities
- [`delete`](#delete) — Soft-delete a node or relationship

## `read`

Read graph data by id, name, tags, shape, or system metadata.

### Examples

```js
read({ id: "abc123" })
read({ shape: "task", priority: 1 })
read({ about: "shapes" })
```

## `search`

Full-text search over local graph entities.

### Examples

```js
search({ query: "project status" })
search({ query: "pending tasks", shape: "task" })
```

## `delete`

Soft-delete a node or relationship.

### Examples

```js
delete({ id: "abc123" })
```
