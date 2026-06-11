---
title: app
description: "An application — the one installable, launchable unit. System apps"
sidebar:
  label: app
---

An application — the one installable, launchable unit. System apps
(Finder, Settings — engine-resident, code-only, seeded by
`seed_system_apps()` in identity.rs) and installed apps (Python
connectors discovered from source directories) are the same shape;
`isSystem` and the seeding path are the only differences. Installed
apps additionally carry connection lifecycle (`status` / `error`)
because they adapt external platforms.

What an app OFFERS the rest of the system is a `service` — see
shapes/agentos/service.yaml. The service node points at its providers
with `provided_by` edges (minted by the engine from each app's own
declarations, never authored). An app may provide zero services or
several.

Themes never reference app ids by string literal. They reference
role-based list ids ('primary-launcher', 'tray', 'desktop') and render
whatever bookmarks those lists contain. Per-theme renames happen via
the theme bundle's `appOverrides[appId] = { name?, icon? }` map — the
theme owns presentation, not identity.

| Metadata | Value |
|---|---|
| **Plural** | `apps` |
| **Subtitle field** | `description` |
| **Identity** | `id` |

## Fields

| Field | Type |
|---|---|
| `id` | `string` |
| `name` | `string` |
| `description` | `text` |
| `color` | `string` |
| `status` | `string` |
| `error` | `text` |
| `iconRole` | `string` |
| `route` | `string` |
| `defaultView` | `string` |
| `isSystem` | `boolean` |
| `handles` | `string[]` |
| `composition` | `json` |

## Relations

| Relation | Target |
|---|---|
| `online_at` | [`website`](/shapes/reference/website/) |
| `privacy_at` | [`webpage`](/shapes/reference/webpage/) |
| `terms_at` | [`webpage`](/shapes/reference/webpage/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[macOS .app bundle (Info.plist)](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/BundleTypes/BundleTypes.html)** — CFBundleIdentifier ≈ id; CFBundleName ≈ name; CFBundleIconFile ≈ iconRole (we use a role rather than a file path so themes can override).
- **[freedesktop .desktop entry](https://specifications.freedesktop.org/desktop-entry-spec/latest/)** — Name, Icon, Exec — the Linux/XDG peer. We model the launchable surface, not the executable (the engine knows how to spawn).
- **[Windows AppUserModelID](https://learn.microsoft.com/en-us/windows/win32/shell/appids)** — Stable per-app identity decoupled from the executable on disk. Our `id` plays the same role — themes and bookmarks reference it, the binary is an implementation detail of seed_system_apps().
- **[Model Context Protocol (MCP) — Server](https://modelcontextprotocol.io/specification)** — An installed app = an MCP-registerable provider. id ≈ MCP server name; status tracks connection lifecycle.
- **[OpenAPI 3.1 (Info + Servers)](https://spec.openapis.org/oas/v3.1.0)** — Our description/online_at/privacy_at/terms_at ≈ OpenAPI info.description/info.termsOfService/contact.
