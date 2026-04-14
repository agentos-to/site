---
title: order
description: "A purchase order. Contains products and tracks delivery."
sidebar:
  label: order
---

A purchase order. Contains products and tracks delivery.
Used for both e-commerce (Amazon) and delivery (Uber Eats) orders.

Example sources: Amazon, Uber Eats

| Metadata | Value |
|---|---|
| **Plural** | `orders` |
| **Subtitle field** | `total` |
| **Identity** | `platform`, `orderId` |

## Fields

| Field | Type |
|---|---|
| `orderId` | `string` |
| `orderDate` | `datetime` |
| `total` | `string` |
| `totalAmount` | `number` |
| `originalTotal` | `string` |
| `originalTotalAmount` | `number` |
| `savings` | `number` |
| `currency` | `string` |
| `status` | `string` |
| `deliveryDate` | `datetime` |
| `eta` | `string` |
| `subtotal` | `number` |
| `tipAmount` | `number` |
| `deliveryFee` | `number` |
| `taxes` | `number` |
| `summary` | `string` |
| `fareBreakdown` | `json` |

## Relations

| Relation | Target |
|---|---|
| `platform` | [`platform`](/docs/reference/shapes/platform/) |
| `contains` | [`product[]`](/docs/reference/shapes/product/) |
| `shippingAddress` | [`place`](/docs/reference/shapes/place/) |
| `store` | [`place`](/docs/reference/shapes/place/) |
| `delivery` | [`trip`](/docs/reference/shapes/trip/) |
| `tracking` | [`webpage`](/docs/reference/shapes/webpage/) |

## Skills that produce this shape

- [uber](/docs/reference/skills/logistics/uber/) — `list_deliveries`, `get_cart`
- [uber](/docs/reference/skills/logistics/uber/) — `get_delivery`, `get_messages`, `add_to_cart`, `checkout`, `track_delivery`
- [amazon](/docs/reference/skills/logistics/amazon/) — `list_orders`
- [amazon](/docs/reference/skills/logistics/amazon/) — `get_order`
