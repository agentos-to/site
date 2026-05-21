---
title: health-immunization
description: "An immunization — a single vaccine administration at a point in time."
sidebar:
  label: health-immunization
---

An immunization — a single vaccine administration at a point in time.
"DTP on 1987-03-06", "Covid-19 (Pfizer) on 2021-09-12". One node per
dose: a 3-dose Hep B series is three health-immunization nodes.

`also: [event]` — an immunization IS an event: something that happened
at a time (eventType 'immunization'). Vaccines are instantaneous, so we
add `dateAdministered` as the precise field rather than overloading the
event's startDate/endDate (which suit spanning procedures).

CVX is the CDC's vaccine code system — `cvxCode` is the join key
(DTaP = 20, COVID-19 mRNA Pfizer = 208). `doseNumber` + `seriesDoses`
capture position in a series ("dose 2 of 3").

`name` (inherited via event) is the vaccine name — "DTP", "Yellow Fever".

| Metadata | Value |
|---|---|
| **Plural** | `health-immunizations` |
| **Subtitle field** | `dateAdministered` |
| **Also** | [`event`](/shapes/reference/event/) |

## Fields

| Field | Type |
|---|---|
| `dateAdministered` | `datetime` |
| `cvxCode` | `string` |
| `manufacturer` | `string` |
| `lotNumber` | `string` |
| `doseNumber` | `integer` |
| `seriesDoses` | `integer` |
| `site` | `string` |
| `route` | `string` |
| `diseaseTarget` | `string` |
| `notes` | `text` |

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

- **[HL7 FHIR R5 — Immunization](https://www.hl7.org/fhir/immunization.html)** — The resource for an administered vaccine. dateAdministered ≈ occurrenceDateTime; manufacturer ≈ manufacturer; lotNumber ≈ lotNumber; site/route ≈ site/route; doseNumber ≈ protocolApplied.doseNumber; seriesDoses ≈ protocolApplied.seriesDoses.
- **[CDC CVX — Vaccine Administered code set](https://www2a.cdc.gov/vaccines/iis/iisstandards/vaccines.asp?rpt=cvx)** — The US standard vaccine code system. cvxCode is the canonical vaccine identity (CVX 208 = COVID-19 Pfizer, CVX 20 = DTaP). FHIR Immunization.vaccineCode is CVX-coded.
- **[HL7 v2.x — VXU (Unsolicited Vaccination Update)](https://www.cdc.gov/vaccines/programs/iis/technical-guidance/hl7.html)** — The message format Immunization Information Systems exchange. The RXA segment carries date, CVX, lot, manufacturer, site, route — confirms the field set.
