---
title: conversion
description: "A contextual unit conversion — one that is NOT intrinsic to the units"
sidebar:
  label: conversion
---

A contextual unit conversion — one that is NOT intrinsic to the units
and therefore cannot live on the `unit` node.

Intrinsic conversions (ft→m, °C→K) depend only on the two units and are
stored on unit.toBaseFactor / toBaseOffset. A `conversion` node exists
only when the factor depends on something ELSE — an external, often
time-varying parameter. Two cases:

molar-mass — mg/dL ↔ mmol/L needs the analyte's molar mass. The
factor is a property of the SUBSTANCE, not the unit
pair: glucose and cholesterol convert differently
between the same two units.
fx         — USD ↔ EUR needs a dated exchange rate. The rate is an
external fact that moves daily; `asOf` pins which day.

This is the same lesson as health-reference-range: when a "property"
actually depends on a third thing, model the third thing. The
`parameter` link points at it — a substance node, a rate-source node —
with no shape constraint, because the two cases point at different
kinds of node.

`name` (inherited) is a human label, e.g. "USD→EUR 2026-05-15".

| Metadata | Value |
|---|---|
| **Plural** | `conversions` |
| **Subtitle field** | `kind` |
| **Also** | [`event`](/shapes/reference/event/) |

## Fields

| Field | Type |
|---|---|
| `kind` | `string` |
| `factor` | `number` |
| `rate` | `number` |

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

- **[NIH/NLM — UCUM conversion service](https://ucum.nlm.nih.gov/ucum-service.html)** — The NIH service requires a MOLWEIGHT parameter to convert between molar and mass concentration — direct proof that the conversion is not intrinsic to the unit pair but depends on the substance.
- **[QUDT — currency units carry no conversionMultiplier](https://qudt.org/doc/2024/12/DOC_VOCAB-UNITS-CURRENCY.html)** — QUDT explicitly notes that FX rates are external data not encoded in QUDT — the same reason fx conversions are their own node here rather than a property of the currency unit.
- **[ISO 4217 — Currency codes](https://www.iso.org/iso-4217-currency-codes.html)** — Currency identity for the from/to units of an fx conversion.
