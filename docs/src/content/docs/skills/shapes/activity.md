---
title: activity
description: "An immutable change event — a graph mutation, skill run, search, or load."
sidebar:
  label: activity
---

An immutable change event — a graph mutation, skill run, search, or load.
Fields for what happened, relations for who/what/where.

Example sources: agentOS engine (all tool calls)

| Metadata | Value |
|---|---|
| **Plural** | `activities` |
| **Subtitle field** | `action` |

## Fields

| Field | Type |
|---|---|
| `action` | `string` |
| `published` | `datetime` |
| `changedKeys` | `string[]` |
| `toolName` | `string` |
| `duration` | `number` |
| `success` | `boolean` |

## Relations

| Relation | Target |
|---|---|
| `session` | [`session`](/docs/reference/shapes/session/) |
| `folder` | [`folder`](/docs/reference/shapes/folder/) |
