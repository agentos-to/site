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

invitationType is an open vocabulary — apps set whatever makes sense:
"organization", "workspace", "team", "repository", "event", "channel", etc.

Standard fields (inherited): id, name, url, image, published, content
published = when the invitation was created/sent.

| Metadata | Value |
|---|---|
| **Plural** | `invitations` |
| **Subtitle field** | `invitationType` |
| **Identity** | `at`, `id` |
| **Also** | [`event`](/shapes/reference/event/) |

## Fields

| Field | Type |
|---|---|
| `invitationType` | `string` |
| `email` | `string` |
| `role` | `string` |
| `status` | `string` |
| `token` | `string` |
| `acceptedAt` | `datetime` |
| `revokedAt` | `datetime` |
| `message` | `text` |

## Relations

| Relation | Target |
|---|---|
| `extended_by` | [`account`](/shapes/reference/account/) |
| `extended_to` | [`account`](/shapes/reference/account/) |
| `within_org` | [`organization`](/shapes/reference/organization/) |
| `at_namespace` | [`actor`](/shapes/reference/actor/) |

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
| `timezone` | `string` |
| `visibility` | `string` |

| Relation | Target |
|---|---|
| `concerns` | [`person`](/shapes/reference/person/) |
| `created_by` | [`person`](/shapes/reference/person/) |
| `held_at` | [`place`](/shapes/reference/place/) |
| `involves` | [`person[]`](/shapes/reference/person/) |
| `organized_by` | [`person`](/shapes/reference/person/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[ActivityStreams 2.0 Invite activity](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-invite)** — AS2 Invite is the canonical fediverse verb. Our inviter = actor; invitee = target; status tracks Accept/Reject/TentativeAccept responses.
- **[iCalendar ATTENDEE + PARTSTAT (RFC 5545)](https://datatracker.ietf.org/doc/html/rfc5545)** — Calendar-style invitations. Our status maps to PARTSTAT (NEEDS-ACTION/ACCEPTED/DECLINED/DELEGATED).
- **[SCIM 2.0 (RFC 7644) — user provisioning](https://datatracker.ietf.org/doc/html/rfc7644)** — Enterprise invitation/provisioning. Our email/role/organization align with SCIM User resource's email + entitlements + group membership.

## Skills that produce this shape

- [greptile](/skills/reference/dev/greptile/) — `list_invites`, `send_invite`
