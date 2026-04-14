---
title: Vision
description: Human-computer symbiosis, the memex, and why AgentOS is built the way it is.
---

> *"The hope is that, in not too many years, human brains and computing machines will be coupled together very tightly, and that the resulting partnership will think as no human brain has ever thought."* — J.C.R. Licklider, "Human-Computer Symbiosis," 1960

AgentOS is a local operating system for human-AI collaboration. Your data stays on your machine. AI agents get real tools that work. You see everything they do. Together, you and AI think better than either can alone.

We're building toward Licklider's vision of **human-computer symbiosis** — not AI that replaces human thinking, but AI that amplifies it. The human sets direction, makes judgments, asks the right questions. The AI does the routinizable work that prepares the way for insight.

## The graph

> *"Consider a future device… in which an individual stores all his books, records, and communications, and which is mechanized so that it may be consulted with exceeding speed and flexibility."* — Vannevar Bush, "As We May Think," 1945

We call it **the graph** — your personal knowledge store. We call it your **memex**, after Vannevar Bush's 1945 vision of a personal device for storing, linking, and traversing all of one's knowledge. Everything is an entity, and entities connect through relationships. The graph doesn't care where data came from (Todoist, iMessage, YouTube) — it cares about what things *are* and how they connect.

A task, a person, a message, a video, a webpage, a calendar event — they're all entities in your graph. Relationships are the connections between them. This isn't just a database design. It's a way of thinking. When you ask "what am I working on?" the answer isn't in one app — it's in the connections between your tasks, your messages, your calendar, the people involved. The graph makes those connections visible.

Your memex is a portable SQLite file — your entire mind in a `.db` file. Copy it, back it up, load it on another machine. Domain memex (astronomy, law, medicine) can be mounted read-only into agent simulations — plug in expertise like a CD-ROM. When AgentOS users connect to each other, their memex form a network — Licklider's **intergalactic network**, but for knowledge graphs instead of terminals.

**Everything is an entity** means:

- A YouTube channel is a community. A YouTube comment is a post. A transcript is a document.
- A WhatsApp contact and an iMessage contact with the same phone number are the same person.
- A skill that connects to a service is itself an entity. The system models itself.
- If something exists and has properties and relationships, it belongs in your graph.

The graph is the foundation. Every feature we build — search, feeds, timelines, recommendations, agents — reads from the same graph. Get the graph right, and features compose naturally. Get it wrong, and everything built on top is a special case.

## Local and remote are the same thing

People are used to two mental models for files: **local** (on my computer, only changes when I change it) and **cloud** (iCloud, Dropbox, Drive — somewhere out there, syncing in the background). These feel like different things. AgentOS dissolves that boundary.

A document in your graph can be backed by a local file, a GitHub repo, an API response, or all three simultaneously. The NEPOMUK ontology calls this the separation between **content** (the information itself) and **storage** (where it lives). One document, many access paths. The graph tracks the content; skills handle the storage.

## What it looks like when it works

You say: *"What did I miss this week?"*

The agent queries your graph: messages received, tasks completed by others, calendar events that happened, posts from communities you follow, videos published by channels you subscribe to. It cross-references people — who sent messages AND completed tasks AND posted content. It notices patterns — "Sarah mentioned the project in Slack, completed 3 tasks in Linear, and posted a video update."

All of this from one graph. No special integrations. No "Slack + Linear" connector. Your graph already has the entities and relationships. The agent just traverses.

That's the vision. We're not there yet. But every entity we model correctly, every relationship we capture, every skill we build — it gets closer.

## Where to go next

- [The two users](/docs/introduction/two-users/) — why we serve humans and agents as equal first-class citizens.
- [Local-first](/docs/architecture/local-first/) — why your data never leaves your machine.
- [Inspiration](/docs/introduction/inspiration/) — the shoulders we stand on.
- [Design principles](/docs/architecture/design-principles/) — how these ideas become code.
