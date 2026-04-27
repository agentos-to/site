---
title: accounts
description: "Stored credentials, auth health, and providers"
sidebar:
  label: accounts
---

# `accounts` namespace

Stored credentials, auth health, and providers.

## Ops

- [`list`](#list) — List accounts, auth health, and providers (forwards `action` for login/logout/add/remove)

## `list`

List accounts, auth health, and providers (forwards `action` for login/logout/add/remove).

### Examples

```js
accounts.list()
accounts.list({ skill: "exa" })
```
