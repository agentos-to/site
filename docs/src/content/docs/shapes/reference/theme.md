---
title: theme
description: "An OS theme — window chrome, taskbar, scrollbars, desktop styling."
sidebar:
  label: theme
---

An OS theme — window chrome, taskbar, scrollbars, desktop styling.
Themes are reference data seeded from theme.yaml files in source directories.
The user's pref:theme on their person entity points to a theme by themeId.

Identity: themeId — unique per source namespace (e.g., "xp", "macos9").
Qualified references use sourceId.themeId (e.g., "community.xp").

| Metadata | Value |
|---|---|
| **Plural** | `themes` |
| **Subtitle field** | `family` |
| **Identity** | `themeId` |

## Fields

| Field | Type |
|---|---|
| `themeId` | `string` |
| `family` | `string` |
| `colorScheme` | `string` |
| `description` | `text` |

## Relations

| Relation | Target |
|---|---|
| `wallpaper` | [`image`](/shapes/reference/image/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[CSS color-scheme (W3C CSS Color Adjustment)](https://www.w3.org/TR/css-color-adjust-1/#color-scheme-prop)** — Our colorScheme = CSS color-scheme values (light/dark/both).
- **[System theme APIs (macOS NSAppearance, Windows WinUI)](https://developer.apple.com/documentation/appkit/nsappearance)** — OS-level theme abstraction. Our family parallels NSAppearance.Name (aqua, darkAqua) and Windows theme families.
