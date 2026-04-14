---
title: skill
description: "A connected service/integration in agentOS. Each skill provides tools"
sidebar:
  label: skill
---

A connected service/integration in agentOS. Each skill provides tools
and adapts external data into graph entities.

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

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/shapes/shape-design-principles/) for how prior art informs shape design.

- **[Model Context Protocol (MCP) — Server](https://modelcontextprotocol.io/specification)** — Our skill = an MCP-registerable capability provider. skillId ≈ MCP server name; status tracks connection lifecycle.
- **[OpenAPI 3.1 (Info + Servers)](https://spec.openapis.org/oas/v3.1.0)** — Our description/website/privacyPolicy/termsOfService ≈ OpenAPI info.description/info.termsOfService/info.license/contact.
- **[Anthropic Tool Use (skills-as-tools)](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)** — Each AgentOS skill publishes tools consumed via MCP/Tool-Use. status/error surface tool-call health back to the agent.
