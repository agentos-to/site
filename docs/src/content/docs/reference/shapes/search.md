---
title: search
description: "A search query and its results. Every search is a graph entity with click"
sidebar:
  label: search
---

A search query and its results. Every search is a graph entity with click
tracking — re-searching shows previously-found results first.

Example sources: location system (cross-scheme search)

| | |
|---|---|
| **Plural** | `searches` |
| **Subtitle field** | `query` |
| **Identity** | `query` |

## Fields

| Field | Type |
|---|---|
| `query` | `string` |
| `searchedAt` | `datetime` |
| `searchCount` | `integer` |
| `resultCount` | `integer` |
