---
title: unit
description: "A unit of measure — a concrete scale for a quantity. mg/dL, USD, pascal,"
sidebar:
  label: unit
---

A unit of measure — a concrete scale for a quantity. mg/dL, USD, pascal,
day. Identified primarily by its UCUM code.

A unit carries the data for INTRINSIC conversion: a constant factor and
an affine offset to the coherent base unit of its dimension
(value_in_base = value * toBaseFactor + toBaseOffset). Conversions that
need EXTERNAL context — a currency FX rate, a substance's molar mass —
are NOT here; they are `conversion` nodes. The dividing line: if the
number depends on anything other than the two units, it is not a unit
property.

There is no single authoritative unit-code registry — no "ISO 4217 for
units". Units predate computing by centuries and the space is
fragmented: ISO 80000 defines units in prose and assigns no codes; NIST
publishes guidance only. So the unit node carries SEVERAL cross-
reference identifiers, the way an airline carries both an IATA and an
ICAO code:
ucumCode              — the universal working identity (UCUM)
siDigitalFrameworkUri — the authoritative SI reference (BIPM), when
the unit is part of the SI; NULL otherwise,
and that null is itself a machine-checkable
assertion "this unit is not SI"
unCefactCommonCode    — the trade/interop code (== schema.org unitCode)
qudtUnitIri           — the semantic-web cross-reference hub
wikidataId            — the universal glue identifier

`kind` distinguishes unit families that behave differently under
conversion — the engine must branch on it:
physical    — real SI dimension, intrinsic linear/affine conversion
currency    — ISO 4217, no real dimension; conversion is contextual (FX)
logarithmic — pH, dB, Richter — conversion is exponential, not linear
arbitrary   — UCUM arbitrary units ([IU], [CFU]) — no conversion at all
count       — dimensionless tallies

`name` (inherited) is the human label, e.g. "milligram per deciliter".

| Metadata | Value |
|---|---|
| **Plural** | `units` |
| **Subtitle field** | `symbol` |
| **Identity (any)** | `ucumCode`, `siDigitalFrameworkUri`, `iso4217` |

## Fields

| Field | Type |
|---|---|
| `ucumCode` | `string` |
| `symbol` | `string` |
| `label` | `string` |
| `kind` | `string` |
| `siDigitalFrameworkUri` | `string` |
| `unCefactCommonCode` | `string` |
| `qudtUnitIri` | `string` |
| `wikidataId` | `string` |
| `toBaseFactor` | `number` |
| `toBaseOffset` | `number` |
| `iso4217` | `string` |
| `iso4217Numeric` | `string` |
| `minorExponent` | `integer` |
| `logBase` | `number` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[UCUM — Unified Code for Units of Measure](https://ucum.org/ucum)** — ucumCode is the primary working identity — case-sensitive variant (mg is not MG; h hour is not H henry). Compositional, and the de-facto healthcare standard (FHIR Quantity mandates it, LOINC and HL7 use it). Machine-readable database: ucum-essence.xml.
- **[BIPM — SI Digital Framework / SI Reference Point](https://www.si-digital-framework.org/)** — Launched March 2024 by the BIPM CIPM Task Group on the Digital SI. Publishes resolvable persistent URIs for SI units, prefixes, and defining constants (base namespace si-digital-framework.org/SI/ units/), served as TTL plus a JSON/XML API. The most authoritative source for SI units — treaty-level. siDigitalFrameworkUri carries it; null for non-SI units, and that null is meaningful.
- **[UN/CEFACT Recommendation 20 — Codes for Units of Measure Used in International Trade](https://unece.org/trade/uncefact/cl-recommendations)** — Around 700 short codes (KGM kilogram, MTR metre, LTR litre, CEL degree Celsius). Rev 17 (2021), freely downloadable as XLSX or genericode XML. schema.org's unitCode property uses exactly these codes — unCefactCommonCode is the interop join key.
- **[QUDT — Quantities, Units, Dimensions and Types](https://www.qudt.org/doc/DOC_VOCAB-UNITS.html)** — qudtUnitIri cross-references QUDT, itself a cross-reference hub (QUDT units carry qudt:ucumCode, qudt:uneceCommonCode, qudt:wikidataMatch). toBaseFactor/toBaseOffset correspond to qudt:conversionMultiplier / conversionOffset; kind=currency corresponds to qudt:CurrencyUnit, which also carries NO conversion multiplier — FX is external.
- **[Wikidata](https://www.wikidata.org/wiki/Q11570)** — wikidataId (kilogram = Q11570) is a universal glue identifier — links to every Wikipedia language edition and many external databases. Free SPARQL endpoint plus dumps.
- **[ISO 4217 — Currency codes](https://www.iso.org/iso-4217-currency-codes.html)** — iso4217 (alpha) plus iso4217Numeric and minorExponent for currency units. ISO 4217 IS the authoritative currency-code registry — notably, currency is the ONE unit family with a single authoritative code system; physical units have none.
- **[schema.org — unitCode](https://schema.org/unitCode)** — Precedent that the minimum unit model is (value, unitCode), and that unitCode in practice means a UN/CEFACT Rec 20 code.
- **[NIST SP 811 / SP 330 — and why NIST is NOT a field](https://www.nist.gov/pml/special-publication-811)** — Recorded deliberately. NIST publishes SI usage guidance (SP 811) and the US edition of the SI Brochure (SP 330) — prose only. NIST assigns no unit codes and maintains no unit registry; there is nothing to cross-reference, so no NIST field exists on this shape. Same for ISO 80000 — it defines units in prose and assigns no codes.
