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

| Metadata | Value |
|---|---|
| **Plural** | `invitations` |
| **Subtitle field** | `invitationType` |
| **Identity** | `at`, `id` |

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
| `inviter` | [`account`](/shapes/reference/account/) |
| `invitee` | [`account`](/shapes/reference/account/) |
| `organization` | [`organization`](/shapes/reference/organization/) |
| `at` | [`actor`](/shapes/reference/actor/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[ActivityStreams 2.0 Invite activity](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-invite)** — AS2 Invite is the canonical fediverse verb. Our inviter = actor; invitee = target; status tracks Accept/Reject/TentativeAccept responses.
- **[iCalendar ATTENDEE + PARTSTAT (RFC 5545)](https://datatracker.ietf.org/doc/html/rfc5545)** — Calendar-style invitations. Our status maps to PARTSTAT (NEEDS-ACTION/ACCEPTED/DECLINED/DELEGATED).
- **[SCIM 2.0 (RFC 7644) — user provisioning](https://datatracker.ietf.org/doc/html/rfc7644)** — Enterprise invitation/provisioning. Our email/role/organization align with SCIM User resource's email + entitlements + group membership.

## Skills that produce this shape

- [greptile](/skills/reference/dev/greptile/) — `list_invites`, `send_invite`
