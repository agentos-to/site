---
title: The two users
description: AgentOS serves humans and AI agents as equal first-class citizens. Each has a different core problem.
---

AgentOS serves humans and AI agents as equal first-class citizens. Each has a different core problem, and the whole system is shaped by both.

## For humans: anxiety

> **Anxiety = Uncertainty × Powerlessness**

When AI acts, you feel uncertain (*"what is it doing?"*) and powerless (*"can I stop it?"*). AgentOS solves both:

- The AI **screen-shares** with you — uncertainty drops to zero.
- You **control what it can do** — powerlessness drops to zero.

If either factor is zero, anxiety is zero. This is the reason the human-facing layer exists at all: to keep the human in the loop, seeing everything and in control of everything.

## For agents: error propagation

> **Error Rate = f(Dependency Depth)**

Every round-trip is a chance for errors to compound. We collapse complexity: smart defaults, self-teaching responses, schema validation, minimal round-trips. If a small local model can complete the task, we've done our job.

**The customer is the smallest model.** Not Opus. Not Sonnet. The smallest model that can do tool calling — a 1B-parameter model running on a Raspberry Pi with a 4K context window. If that model can read our readme, understand the domain, and complete a task on the first try, we've succeeded. If it can't, no amount of capability in larger models compensates for the failure.

This is our accessibility standard: design for the most constrained agent, and every agent benefits.

## Why this matters beyond agents

These principles make the system better for humans too. A readme that a 1B model can follow is a readme a new contributor can follow. An API that minimizes round-trips is an API that's fast. Dynamic responses that include context are responses that save everyone's time.

Designing for the most constrained user has always been the shortcut to designing for everyone. The accessibility movement proved this for humans. We're proving it for agents.

For the full practice of designing-for-agents, see [Agent empathy](/docs/principles/agent-empathy/).
