---
title: spec
description: "A spec — a design document describing work to be done."
sidebar:
  label: spec
---

A spec — a design document describing work to be done.
Specs are markdown files with YAML frontmatter in docs/specs/.
State is derived from location: docs/specs/ = active, docs/specs/done/ = done.

| Metadata | Value |
|---|---|
| **Plural** | `specs` |
| **Subtitle field** | `state` |
| **Also** | [`task`](/shapes/reference/task/) · [`file`](/shapes/reference/file/) |

## Fields

| Field | Type |
|---|---|
| `problem` | `text` |
| `successCriteria` | `text` |

## Relations

| Relation | Target |
|---|---|
| `depends_on` | [`spec[]`](/shapes/reference/spec/) |
| `supersedes` | [`spec[]`](/shapes/reference/spec/) |

## Inherited

From [`task`](/shapes/reference/task/) · [`file`](/shapes/reference/file/):

| Field | Type |
|---|---|
| `allDay` | `boolean` |
| `currentUrl` | `string` |
| `dateUpdated` | `datetime` |
| `distinctId` | `string` |
| `encoding` | `string` |
| `endDate` | `datetime` |
| `filename` | `string` |
| `format` | `string` |
| `icalUid` | `string` |
| `kind` | `string` |
| `labels` | `string[]` |
| `lineCount` | `integer` |
| `mimeType` | `string` |
| `parentId` | `string` |
| `path` | `string` |
| `priority` | `integer` |
| `projectId` | `string` |
| `properties` | `json` |
| `recurrence` | `string[]` |
| `remoteId` | `string` |
| `sha` | `string` |
| `showAs` | `string` |
| `size` | `integer` |
| `sourceTitle` | `string` |
| `sourceUrl` | `url` |
| `startDate` | `datetime` |
| `state` | `string` |
| `status` | `string` |
| `target` | `json` |
| `targetDate` | `datetime` |
| `timezone` | `string` |
| `visibility` | `string` |

| Relation | Target |
|---|---|
| `assigned_to` | [`person`](/shapes/reference/person/) |
| `at_namespace` | [`actor`](/shapes/reference/actor/) |
| `attached_to` | [`message`](/shapes/reference/message/) |
| `blocked_by` | [`task[]`](/shapes/reference/task/) |
| `blocks` | [`task[]`](/shapes/reference/task/) |
| `concerns` | [`person`](/shapes/reference/person/) |
| `created_by` | [`person`](/shapes/reference/person/) |
| `has_subtask` | [`task[]`](/shapes/reference/task/) |
| `held_at` | [`place`](/shapes/reference/place/) |
| `in` | [`repository`](/shapes/reference/repository/) |
| `involves` | [`person[]`](/shapes/reference/person/) |
| `organized_by` | [`person`](/shapes/reference/person/) |
| `references` | [`repository`](/shapes/reference/repository/) |
| `subtask_of` | [`task`](/shapes/reference/task/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[IETF RFC process](https://www.ietf.org/standards/rfcs/)** — Canonical "design doc with problem statement and success criteria" lineage. Our problem/successCriteria mirror the RFC structure.
- **[Architectural Decision Records (ADR / MADR)](https://adr.github.io/)** — Modern in-repo equivalent. supersedes[] matches ADR's "Supersedes" link; dependsOn[] has no direct ADR peer.
- **[Python PEP (spec-as-markdown)](https://peps.python.org/pep-0001/)** — PEP states problem, rationale, spec, rejected alternatives. Our fields are a slim version of the PEP template.
