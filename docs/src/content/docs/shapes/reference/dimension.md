---
title: dimension
description: "A physical dimension — the abstract nature of a quantity, expressed as"
sidebar:
  label: dimension
---

A physical dimension — the abstract nature of a quantity, expressed as
a vector of exponents over the 7 SI base dimensions. Mass-per-volume is
L⁻³M¹. Speed is L¹T⁻¹. A pure ratio is the zero vector.

Dimension is the TYPE of a quantity. The algebra of what may be added
and what may be converted is decided HERE, not at the unit layer: two
values may be added only if their dimensions are equal; two units may
be converted only if their dimensions are equal. A unit is one possible
encoding of a dimension (kg, lb, oz all encode mass M¹); the dimension
is the invariant they share.

`key` is the canonical exponent-vector string — the natural key. The
form is each nonzero base symbol followed by its signed exponent, in a
fixed order (L, M, T, I, Θ→Q, N, J): "L-3M1" for mass concentration,
"L1T-2" for acceleration, "" for the dimensionless quantity. The same
seven exponents are also stored as separate integer fields so the
engine can do dimension arithmetic (multiply = add the vectors, divide
= subtract) without parsing the string.

`name` (inherited) is the human label, e.g. "mass per volume".

| Metadata | Value |
|---|---|
| **Plural** | `dimensions` |
| **Subtitle field** | `label` |
| **Identity** | `key` |

## Fields

| Field | Type |
|---|---|
| `key` | `string` |
| `label` | `string` |
| `length` | `integer` |
| `mass` | `integer` |
| `time` | `integer` |
| `current` | `integer` |
| `temperature` | `integer` |
| `amount` | `integer` |
| `luminous` | `integer` |
| `dimensionless` | `boolean` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[BIPM — SI Brochure, 9th edition (2019)](https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf)** — Defines the 7 base quantities (length, mass, time, electric current, thermodynamic temperature, amount of substance, luminous intensity) and their dimensions L, M, T, I, Θ, N, J. The seven exponent fields here are exactly those base dimensions.
- **[ISO 80000-1 — Quantities and units, Part 1: General](https://www.iso.org/standard/76921.html)** — The ISQ (International System of Quantities) — the rigorous definition of a quantity dimension as a product of base-quantity powers. This shape is a direct encoding of an ISQ dimension.
- **[QUDT — QuantityKindDimensionVector](https://www.qudt.org/doc/DOC_SCHEMA-QUDT.html)** — QUDT encodes the same 7 exponents as separate properties (qudt:dimensionExponentForMass etc.) plus a compact vector IRI. Our `key` mirrors that compact form; the seven integer fields mirror the per-dimension properties.
