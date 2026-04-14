---
title: hardware
description: "A physical hardware product — computer, phone, appliance, component."
sidebar:
  label: hardware
---

A physical hardware product — computer, phone, appliance, component.

Examples: MacBook Pro, iPhone, Arduino, server rack

| | |
|---|---|
| **Plural** | `hardware` |
| **Subtitle field** | `author` |
| **Identity** | `serialNumber` |
| **Also** | [`product`](/docs/reference/shapes/product/) |

## Fields

| Field | Type |
|---|---|
| `modelNumber` | `string` |
| `serialNumber` | `string` |
| `specs` | `json` |

## Relations

| Relation | Target |
|---|---|
| `manufacturer` | [`organization`](/docs/reference/shapes/organization/) |

## Inherited

From [`product`](/docs/reference/shapes/product/):

| Field | Type |
|---|---|
| `aisle` | `string` |
| `availability` | `string` |
| `barcode` | `string` |
| `calories` | `number` |
| `categories` | `string[]` |
| `currency` | `string` |
| `department` | `string` |
| `images` | `json` |
| `novaGroup` | `integer` |
| `nutritionScore` | `string` |
| `originalPrice` | `string` |
| `originalPriceAmount` | `number` |
| `price` | `string` |
| `priceAmount` | `number` |
| `quantity` | `integer` |
| `servingSize` | `string` |
| `sku` | `string` |
| `soldByWeight` | `boolean` |
| `weight` | `string` |
| `weightUnit` | `string` |
| `weightValue` | `number` |

| Relation | Target |
|---|---|
| `brand` | [`brand`](/docs/reference/shapes/brand/) |
| `tagged` | [`tag[]`](/docs/reference/shapes/tag/) |
