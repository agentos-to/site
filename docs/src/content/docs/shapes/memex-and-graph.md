---
title: Memex & the graph
description: Your entire knowledge graph in a portable SQLite file. The history and shape of the memex as AgentOS implements it.
---

> *"Consider a future device… in which an individual stores all his books, records, and communications, and which is mechanized so that it may be consulted with exceeding speed and flexibility."* — Vannevar Bush, "As We May Think," 1945

We call it **the graph** — your personal knowledge store. We call it your **memex**, after Vannevar Bush's 1945 vision. Everything is an entity. Entities connect through relationships. It all lives in a single portable SQLite file at `~/.agentos/data/agentos.db`.

## One file, one mind

Your memex is a portable SQLite file — your entire mind in a `.db` file. Copy it, back it up, load it on another machine. This is not a metaphor. The graph really is one file. Credentials are encrypted in the same file (AES-256-GCM, key in macOS Keychain). Nuke the file and everything's gone.

Because the file is portable, domain memex (astronomy, law, medicine) can be mounted read-only into agent simulations — plug in expertise like a CD-ROM. When AgentOS users connect to each other, their memex form a network — Licklider's **intergalactic network**, but for knowledge graphs instead of terminals.

## Everything is an entity

- A YouTube channel is a community. A YouTube comment is a post. A transcript is a document.
- A WhatsApp contact and an iMessage contact with the same phone number are the same person.
- A skill that connects to a service is itself an entity. The system models itself.
- If something exists and has properties and relationships, it belongs in your graph.

The graph is the foundation. Every feature we build — search, feeds, timelines, recommendations, agents — reads from the same graph. Get the graph right, and features compose naturally. Get it wrong, and everything built on top is a special case.

## Shapes, not tables

The graph has one entity table and one relationship table. Entity **shape** is carried by the entity itself, via a `_type` entity that describes which fields, relations, and display hints apply. The engine doesn't know about `task` or `message` or `person` — it only knows that there's an entity whose `_type` points to a shape.

This is what makes the engine generic. Adding a new entity type is a YAML file in `docs/shapes/`, not a Rust change. See the [Ontology overview](/shapes/overview/) for the full shape system.

## Content vs. storage

The NEPOMUK Semantic Desktop drew a distinction we borrow: **content** (the information itself) and **storage** (where it lives). A document in your graph can be backed by a local file, a GitHub repo, an API response, or all three simultaneously. The graph tracks the content; skills handle the storage.

This is why "local" and "remote" aren't two different things in AgentOS. Our own roadmap specs on GitHub are live documents. A research paper cited in our vision is a document entity with a URL. The vision file on disk, the same file on GitHub, and the entity in your graph — one thing, three views. When AgentOS fetches the latest from a source, it's not "downloading a file" — it's refreshing an entity.

## See also

- [Ontology overview](/shapes/overview/) — the full shape system and the tactical reference.
- [Identity & change](/shapes/identity-and-change/) — why every actor and every change is an entity too.
- [Research → Ontology](/research/ontology/genealogical-relationships/) — prior art on knowledge graphs we studied.
- [Research → Context → Semantic file systems](/research/context/semantic-file-systems/) — why desktop OSes keep trying and failing to build something like this.
