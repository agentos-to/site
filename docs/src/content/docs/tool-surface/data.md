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
- [`update`](#update) — Set or delete vals on an existing node
- [`create`](#create) — Create a new node of the given shape
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

## `update`

Set or delete vals on an existing node. `null` value deletes a val; non-null sets it. Unit auto-inferred from JSON type when not given.

### Examples

```js
update({ id: "abc123", vals: { "pref:theme": "xp" } })
update({ id: "abc123", vals: { "pref:fontSize": 14 } })
update({ id: "abc123", vals: { "pref:legacy": null } })
```

## `create`

Create a new node of the given shape. With `identity`, looks up an existing node first and updates it instead of creating a duplicate (upsert semantics).

### Examples

```js
create({ shape: "bookmark", name: "Aircraft", vals: { address: "?shape=aircraft" } })
create({ shape: "person", name: "Joe", identity: { email: "joe@example.com" } })
```

## `delete`

Soft-delete a node or relationship.

### Examples

```js
delete({ id: "abc123" })
```
