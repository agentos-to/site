---
title: ui
description: "Interact with window content the way a human does — by labeled control, never pixels"
sidebar:
  label: ui
---

# `ui` namespace

Interact with window content the way a human does — by labeled control, never pixels. Tabs and rows are routes (windows.open covers them); ui covers only what routes can't express. Every invoke renders live on the desktop and lands as an activity.

## Ops

- [`invoke`](#invoke) — Activate a labeled control (OK / Cancel / Apply) in a window

## `invoke`

Activate a labeled control (OK / Cancel / Apply) in a window. The real button is focused, pressed, and clicked — the human watches it happen. Minimized windows and disabled controls refuse (policy is law).

### Examples

```js
invoke({ windowId: "window-…", control: "OK" })
```

### Input schema

```json
{
  "additionalProperties": false,
  "properties": {
    "control": {
      "description": "The control's visible label, case-insensitive \u2014 OK, Cancel, Apply, Browse\u2026. A miss returns the window's labeled controls.",
      "type": "string"
    },
    "windowId": {
      "description": "Window id (from windows.list / windows.open).",
      "type": "string"
    }
  },
  "required": [
    "windowId",
    "control"
  ],
  "type": "object"
}
```
