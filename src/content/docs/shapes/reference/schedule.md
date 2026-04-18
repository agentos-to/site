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
| `produces` | [`trip`](/shapes/reference/trip/) |
| `provider` | [`skill`](/shapes/reference/skill/) |
| `operator` | [`organization`](/shapes/reference/organization/) |

## Used as a base by

- [`route`](/shapes/reference/route/)

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[RFC 5545 RRULE (iCalendar)](https://datatracker.ietf.org/doc/html/rfc5545#section-3.3.10)** — Our rrule field IS an RFC 5545 RRULE string; timezone follows iCal TZID conventions.
- **[POSIX cron](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/crontab.html)** — Our cronExpression is a 5-field cron string (minute, hour, dom, month, dow).
- **[GTFS calendar.txt + calendar_dates.txt](https://gtfs.org/documentation/schedule/reference/#calendartxt)** — Transit schedules. Our hours (operating-hours JSON) and scheduleType=timetable map to GTFS service-id + day flags.
