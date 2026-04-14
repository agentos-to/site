---
title: invitation
description: "An invitation to join something — an organization, a workspace, a team, a"
sidebar:
  label: invitation
---

An invitation to join something — an organization, a workspace, a team, a
calendar event. The universal "you're invited" primitive.

Invitations have a lifecycle: pending → accepted / declined / revoked / expired.
They cross platforms: Greptile org invites, GitHub org invites, Slack workspace
invites, Google Calendar event invites, Linear team invites — all the same shape.

Identity: [platform, id] — one node per platform+invite combo. The id is
typically the invite token or a platform-specific invite id.

invitationType is an open vocabulary — skills set whatever makes sense:
"organization", "workspace", "team", "repository", "event", "channel", etc.

Standard fields (inherited): id, name, url, image, published, content
published = when the invitation was created/sent.

Example sources: Greptile, GitHub, Slack, Google Calendar, Linear

| Metadata | Value |
|---|---|
| **Plural** | `invitations` |
| **Subtitle field** | `invitationType` |
| **Identity** | `platform`, `id` |

## Fields

| Field | Type |
|---|---|
| `invitationType` | `string` |
| `email` | `string` |
| `role` | `string` |
| `status` | `string` |
| `token` | `string` |
| `expiresAt` | `datetime` |
| `acceptedAt` | `datetime` |
| `revokedAt` | `datetime` |
| `message` | `text` |

## Relations

| Relation | Target |
|---|---|
| `inviter` | [`account`](/docs/shapes/reference/account/) |
| `invitee` | [`account`](/docs/shapes/reference/account/) |
| `organization` | [`organization`](/docs/shapes/reference/organization/) |
| `platform` | [`product`](/docs/shapes/reference/product/) |

## Skills that produce this shape

- [greptile](/docs/skills/reference/dev/greptile/) — `list_invites`
- [greptile](/docs/skills/reference/dev/greptile/) — `send_invite`
