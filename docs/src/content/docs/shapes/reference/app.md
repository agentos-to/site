---
title: app
description: "An application — something the shell can spawn as a window. Includes"
sidebar:
  label: app
---

An application — something the shell can spawn as a window. Includes
system apps (Finder, Settings, eventually Recycle Bin — engine-resident,
code-only, seeded by `seed_system_apps()` in identity.rs) and
user-installed apps (any skill returning an app-shape dict). The shape
is identical either way; only the seeding path differs.

Themes never reference app ids by string literal. They reference
role-based list ids ('primary-launcher', 'tray', 'desktop') and render
whatever bookmarks those lists contain. Per-theme renames happen via
the theme bundle's `appOverrides[appId] = { name?, icon? }` map — the
theme owns presentation, not identity.

| Metadata | Value |
|---|---|
| **Plural** | `apps` |
| **Subtitle field** | `name` |
| **Identity** | `id` |

## Fields

| Field | Type |
|---|---|
| `id` | `string` |
| `name` | `string` |
| `iconRole` | `string` |
| `route` | `string` |
| `defaultView` | `string` |
| `isSystem` | `boolean` |
| `handles` | `string[]` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[macOS .app bundle (Info.plist)](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/BundleTypes/BundleTypes.html)** — CFBundleIdentifier ≈ id; CFBundleName ≈ name; CFBundleIconFile ≈ iconRole (we use a role rather than a file path so themes can override).
- **[freedesktop .desktop entry](https://specifications.freedesktop.org/desktop-entry-spec/latest/)** — Name, Icon, Exec — the Linux/XDG peer. We model the launchable surface, not the executable (the engine knows how to spawn).
- **[Windows AppUserModelID](https://learn.microsoft.com/en-us/windows/win32/shell/appids)** — Stable per-app identity decoupled from the executable on disk. Our `id` plays the same role — themes and bookmarks reference it, the binary is an implementation detail of seed_system_apps().
