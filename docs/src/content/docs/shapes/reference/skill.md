---
title: skill
description: "A connected service/integration in agentOS. Each skill provides tools"
sidebar:
  label: skill
---

A connected service/integration in agentOS. Each skill provides tools
and adapts external data into graph entities.

Example sources: agentOS engine (auto-registered from skill YAML files)

| Metadata | Value |
|---|---|
| **Plural** | `skills` |
| **Subtitle field** | `description` |

## Fields

| Field | Type |
|---|---|
| `skillId` | `string` |
| `description` | `text` |
| `color` | `string` |
| `status` | `string` |
| `error` | `text` |

## Relations

| Relation | Target |
|---|---|
| `website` | [`website`](/docs/shapes/reference/website/) |
| `privacyPolicy` | [`webpage`](/docs/shapes/reference/webpage/) |
| `termsOfService` | [`webpage`](/docs/shapes/reference/webpage/) |
