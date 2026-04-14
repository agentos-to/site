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
| `wallpaper` | [`image`](/docs/reference/shapes/image/) |
