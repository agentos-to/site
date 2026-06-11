---
title: Google Chrome
description: "CDP access to Google Chrome — debug-attachable sessions for the engine's browser_session host, attach or launch"
sidebar:
  label: google-chrome
---

| Metadata | Value |
|---|---|
| **Category** | `browsers` |
| **Services** | `http`, `shell` |
| **Website** | <https://www.google.com/chrome/> |

## Readme

Chrome DevTools Protocol access to Google Chrome. Provides the
`cdp_access` service — the layer the engine's `browser_session` system
app consumes to host live, debug-attachable browser sessions. Any
Chromium-family browser app can provide the same service (Brave ships
the identical shape); the user's default app for the service decides
which browser hosts sessions.

## Requirements

- **macOS only** — launches via LaunchServices (`open -na`)
- **Google Chrome installed**

## Modes

- **attach** — find the user's daily Chrome already running with
  `--remote-debugging-port`. If it isn't, returns a structured
  `NeedsDebugBrowser` error carrying the exact relaunch command.
- **launch** — spawn (or reuse) an engine-owned Chrome instance with
  its own profile at `~/.agentos/browsers/chrome`. A dedicated,
  always-on session host that never shares fate with the user's
  daily browsing. Reuse is keyed on the profile's `DevToolsActivePort`
  answering `/json/version`; a frozen instance is killed and waited
  out before relaunch.

## Usage

```
OPERATION       DESCRIPTION
-----------     -------------------------------------------------------
cdp_connect     Return {ws_url, target_id, browser_version, tabs} for a
                debug-attachable Chrome (mode: attach | launch)
```

Consumers should almost never call this directly — ask for the
`browser_session` service instead and let the engine hold the socket.
