---
title: milestone
description: "A point-in-time checkpoint — a significant, zero-duration moment in a"
sidebar:
  label: milestone
---

A point-in-time checkpoint — a significant, zero-duration moment in a
larger effort: "Phase 1 approved", "1000 users", "manuscript delivered".
A milestone IS-A event (it has a when), so it inherits the event timeline:
event.startDate is the planned point; event.status carries the lifecycle
(use values upcoming | reached | missed | cancelled). It adds only the
checkpoint specifics — when it was actually reached, and what counts as done.

| Metadata | Value |
|---|---|
| **Plural** | `milestones` |
| **Subtitle field** | `status` |
| **Also** | [`event`](/shapes/reference/event/) |

## Fields

| Field | Type |
|---|---|
| `reachedAt` | `datetime` |
| `criterion` | `text` |

## Inherited

From [`event`](/shapes/reference/event/):

| Field | Type |
|---|---|
| `allDay` | `boolean` |
| `currentUrl` | `string` |
| `dateUpdated` | `datetime` |
| `distinctId` | `string` |
| `endDate` | `datetime` |
| `icalUid` | `string` |
| `properties` | `json` |
| `recurrence` | `string[]` |
| `showAs` | `string` |
| `sourceTitle` | `string` |
| `sourceUrl` | `url` |
| `startDate` | `datetime` |
| `status` | `string` |
| `timezone` | `string` |
| `visibility` | `string` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[PMBOK Guide (PMI) — milestone](https://www.wrike.com/project-management-guide/faq/what-is-a-milestone-in-project-management/)** — "A significant point or event," zero duration → no span, just the planned point (event.startDate) + reachedAt; justifies also:[event].
- **[schema.org/Event (eventStatus, superEvent)](https://schema.org/Event)** — Inherits point-in-time + status + nesting; superEvent → part_of, eventStatus → the inherited status field.
- **[GitHub Milestones](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/about-milestones)** — Real-world milestone-as-aggregator with a due date bundling work items → the completes edge.
