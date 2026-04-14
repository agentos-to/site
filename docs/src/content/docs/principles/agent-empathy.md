---
title: Agent empathy
description: The practice of building for the smallest model that can do the work. Not a feeling — a discipline.
---

> *"The real problem is not whether machines think but whether men do."* — B.F. Skinner

We serve two users. The human side has decades of UX research, design systems, and accessibility standards. The agent side has almost nothing. We're writing the playbook.

**The customer is the smallest model.** Not Opus. Not Sonnet. The smallest model that can do tool calling — a 1B-parameter model running on a Raspberry Pi with a 4K context window. If that model can read our readme, understand the domain, and complete a task on the first try, we've succeeded. If it can't, no amount of capability in larger models compensates for the failure. This is our accessibility standard: design for the most constrained agent, and every agent benefits.

This isn't hypothetical generosity. It's engineering discipline. A readme that works for a small model is a readme that's clear. An API that needs one call instead of two is an API with less surface area for bugs. Constraints on the consumer force clarity in the producer.

## The practice

Agent empathy is not a feeling. It's a practice — a set of things you do every time you build something an agent will touch.

**Observe before designing.** Watch an agent use what you built. Not in theory — actually do it. Call the readme, read what comes back, and follow the path a small model would take. Where does it reach for the wrong tool? Where does it misinterpret silence as absence? Where does it waste a round-trip on something the server already knows? The pain is in the observation, not in the spec.

**Understanding precedes empathy. Empathy precedes solutions.** You cannot design for agents until you have felt their confusion. Read the readme as if you had no prior context. Try to complete a task using only what the documentation tells you, nothing you happen to know. The gap between what you know and what the document teaches is the exact gap every new agent falls into.

**Teach the model, not the syntax.** An agent that understands the domain makes good decisions even with imperfect information. An agent that only knows the API surface makes random decisions confidently. Always establish *what things are* and *why they work this way* before *how to call them*. Mental model first, reference card second.

**One call, not two.** Every round-trip is a chance for error, confusion, context loss, and token waste. If two steps can be collapsed into one step, collapse them. If the server knows something the agent will need, include it in the response — don't make the agent ask. The agent's context window is finite and precious. Respect it.

**Show, don't list.** A tree with counts teaches spatial relationships that a 60-row alphabetical table never can. An example you can copy teaches more than a syntax reference you have to interpret. Concrete beats abstract. Always.

**Dynamic beats static.** If the system knows the answer at response time, put it in the response. Don't make the agent query for context the server already has. A readme that says "you have 142 people and 1,204 messages in your graph" is worth more than a readme that says "use `list` to find out what's in your graph." The former orients; the latter assigns homework.

**Inline, not tabular.** Agents read tokens, not pixels. Markdown tables waste tokens on pipe characters, header separators, and padding. The **inline format** is our standard for agent-facing output: one entity per line, name first, metadata in parentheses — `Task Name (high, ready, updated Feb 27, abc123)`. For detail views, properties are simple `key: value` lines, not table rows. Relationships are `type: Name (id)` lines. A self-teaching footer lists available fields and relationships the agent didn't ask for but could. Everything an agent needs to act on — the entity ID, the status, the related entity IDs — is right there in the text, no parsing required. This is our accessibility format: if a 1B model can extract the ID from a parenthetical, we've succeeded.

**Entities first, skills second.** The graph covers 90% of what an agent needs. Skills are the escape hatch for capabilities the graph can't provide — searching the web, sending a message, calling an external API. If an agent reaches for a skill when an entity query would have worked, the documentation failed, not the agent.

**Absent is not false.** This is the foundational data semantics rule. In a sparse graph, most entities don't have most fields. Filtering by `done=false` doesn't mean "not done" — it means "the done field exists AND equals false." An agent that doesn't understand this will query itself into a wall, get zero results, and confidently report that nothing exists. Every interface we build must account for how absence, presence, and computed values actually work — and teach it.

## The test

When you build something an agent will touch — a readme, a tool response, an error message, a data format — ask yourself:

1. Could a small model complete the task after reading this once?
2. Does this teach the domain or just the API?
3. Am I making the agent ask for something I already know?
4. If the agent gets zero results, will it understand why?
5. What's the fewest number of round-trips to success?

If the answer to #1 is no, the rest doesn't matter yet. Start there.

## Why this matters beyond agents

These principles make the system better for humans too. A readme that a 1B model can follow is a readme a new contributor can follow. An API that minimizes round-trips is an API that's fast. Dynamic responses that include context are responses that save everyone's time. Error messages that explain absence are error messages that don't waste anyone's afternoon.

Designing for the most constrained user has always been the shortcut to designing for everyone. The accessibility movement proved this for humans. We're proving it for agents.
