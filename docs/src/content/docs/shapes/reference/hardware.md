---
title: hardware
description: "A physical hardware product — computer, phone, appliance, component."
sidebar:
  label: hardware
---

A physical hardware product — computer, phone, appliance, component.

Examples: MacBook Pro, iPhone, Arduino, server rack

| Metadata | Value |
|---|---|
| **Plural** | `hardware` |
| **Subtitle field** | `author` |
| **Identity** | `serialNumber` |
| **Also** | [`product`](/docs/shapes/reference/product/) |

## Fields

| Field | Type |
|---|---|
| `modelNumber` | `string` |
| `serialNumber` | `string` |
| `specs` | `json` |

## Relations

| Relation | Target |
|---|---|
| `manufacturer` | [`organization`](/docs/shapes/reference/organization/) |

## Inherited

From [`product`](/docs/shapes/reference/product/):

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
| `brand` | [`brand`](/docs/shapes/reference/brand/) |
| `tagged` | [`tag[]`](/docs/shapes/reference/tag/) |
