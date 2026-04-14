---
title: folder
description: "A filesystem directory or workspace. Used to track project roots,"
sidebar:
  label: folder
---

A filesystem directory or workspace. Used to track project roots,
working directories, and document collections.

Example sources: agentOS engine (session working directories), filesystem

| | |
|---|---|
| **Plural** | `folders` |
| **Subtitle field** | `path` |
| **Identity** | `path` |

## Fields

| Field | Type |
|---|---|
| `path` | `string` |
| `workspaceType` | `string` |
| `hasReadme` | `boolean` |

## Relations

| Relation | Target |
|---|---|
| `repository` | [`repository`](/docs/reference/shapes/repository/) |
| `contains` | [`file[]`](/docs/reference/shapes/file/) |
