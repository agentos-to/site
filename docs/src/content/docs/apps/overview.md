---
title: Apps overview
description: The optional GUI layer. Linux + optional desktop environment. TypeScript/React UIs for humans, brokered by the engine.
---

Apps are a **completely optional GUI layer** — think Linux plus an optional desktop environment. The CLI and engine work fully without them. Apps are TypeScript/React UIs rendered by the engine's web bridge, hosted in the [`apps/`](https://github.com/agentos-to/apps) repo.

## Apps and skills must never know about each other

An app asks *"give me an LLM"*. The engine picks a skill that `@provides(llm)`. Neither side learns the other's name. The engine is the only broker.

This is **security by architecture**. If an app and a skill can't name each other, they can't trust each other. Every capability request and every credential dereference passes through the engine.

See [Local-first](/docs/introduction/local-first/) for the full framing.

## Shipped apps

Each app is a self-contained React surface built against the `_sdk/`:

```
accounts/      Identity + connection management
messages/      Unified inbox across comms skills
settings/      Engine + skill configuration
store/         Install skills, apps, themes
```

## Building an app

The app SDK and shared React components live next to the apps:

```
apps/
  _sdk/          TypeScript Apps SDK — the engine API surface for apps
  _components/   Shared React components
  <your-app>/    A self-contained app
```

An app calls the engine via the SDK. It never reaches into a skill's internals, never holds a credential, and never imports another app. The engine is always in the middle.

## Headless is first-class

A headless AgentOS — API and AI only — works perfectly without apps. Apps are there when you want a human-facing surface for an entity type (a Videos app for video entities, a Messages app for conversation/message entities). The default entity viewer renders any entity with schema-driven components, so you don't need an app just to *see* data.

## See also

- [Principles → How we build](/docs/principles/how-we-build/)
- [Principles → Design principles → Three concerns](/docs/principles/design-principles/#three-concerns) — entities, skills, and apps as independent concerns.
- The [`apps/` repo](https://github.com/agentos-to/apps) — where apps live.
