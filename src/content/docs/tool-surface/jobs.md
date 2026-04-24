---
title: jobs
description: "Async processes — one-shot jobs AND long-running watchers"
sidebar:
  label: jobs
---

# `jobs` namespace

Async processes — one-shot jobs AND long-running watchers.

## Ops

- [`watch`](#watch) — Start a live skill event stream
- [`cancel`](#cancel) — Stop a running watcher or cancel an async job
- [`list`](#list) — List running watchers and their status

## `watch`

Start a live skill event stream. The watcher runs indefinitely.

### Examples

```js
jobs.watch({ skill: "whatsapp", stream: "messages" })
```

## `cancel`

Stop a running watcher or cancel an async job.

### Examples

```js
jobs.cancel({ id: "whatsapp:messages" })
```

## `list`

List running watchers and their status.

### Examples

```js
jobs.list()
```
