---
title: schedule
description: "A recurring pattern that produces instances when it fires."
sidebar:
  label: schedule
---

A recurring pattern that produces instances when it fires.

The universal recurrence primitive. Covers automation triggers (cron agents),
transit timetables (bus every 15 min), service hours (Costco delivers Sat 9:30-7),
and anything else that repeats and produces typed instances.

NOT an event — events are things you attend (meetings, classes). A schedule is
the *pattern* that produces things. Events have their own `recurrence` field
for calendar display. When something is both (a recurring yoga class you book),
the event models attendance and the schedule models availability.

The `produces` relation links a schedule to what each occurrence creates:
a trip (transport), an event (class/meeting), or nothing typed (just runs a prompt).

Example sources: Claude Code (cron agents), GTFS (transit), Uber Eats (store hours),
future: flight timetables, gym class schedules

| Metadata | Value |
|---|---|
| **Plural** | `schedules` |
| **Subtitle field** | `cronExpression` |

## Fields

| Field | Type |
|---|---|
| `scheduleType` | `string` |
| `cronExpression` | `string` |
| `rrule` | `string` |
| `hours` | `json` |
| `timezone` | `string` |
| `prompt` | `string` |
| `enabled` | `boolean` |
| `durability` | `string` |
| `providerJobId` | `string` |
| `lastFiredAt` | `datetime` |
| `nextFireAt` | `datetime` |

## Relations

| Relation | Target |
|---|---|
| `produces` | [`trip`](/docs/reference/shapes/trip/) |
| `provider` | [`skill`](/docs/reference/shapes/skill/) |
| `operator` | [`organization`](/docs/reference/shapes/organization/) |

## Used as a base by

- [`route`](/docs/reference/shapes/route/)
