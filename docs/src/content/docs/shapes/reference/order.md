---
title: order
description: "A purchase order. Contains products and tracks delivery."
sidebar:
  label: order
---

A purchase order. Contains products and tracks delivery.
Used for both e-commerce (Amazon) and delivery (Uber Eats) orders.

| Metadata | Value |
|---|---|
| **Plural** | `orders` |
| **Subtitle field** | `total` |
| **Identity** | `at`, `orderId` |
| **Also** | [`event`](/shapes/reference/event/) |

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
| `deliveryInstructions` | `string` |
| `interactionType` | `string` |
| `orderUuid` | `string` |
| `body` | `text` |
| `head` | `text` |
| `messages` | `json` |
| `timeline` | `json` |
| `itemStates` | `json` |
| `latestArrival` | `datetime` |
| `progress` | `number` |
| `progressTotal` | `number` |

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

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Order](https://schema.org/Order)** — Our orderId = orderNumber; orderDate = orderDate; total = totalPaymentDue; status = orderStatus; shippingAddress = orderDelivery.
- **[schema.org/OrderStatus (enum)](https://schema.org/OrderStatus)** — Our status values (placed, confirmed, delivering, completed, cancelled) map to OrderProcessing/OrderInTransit/OrderDelivered/ OrderCancelled.
- **[Amazon Order Reports (MWS / SP-API)](https://developer-docs.amazon.com/sp-api/docs/orders-api-v0-reference)** — Practical source. Our orderId, fareBreakdown, savings, eta are lifted from Amazon/Uber Eats order structures.

## Skills that produce this shape

- [uber](/skills/reference/logistics/uber/) — `list_deliveries`, `get_cart`, `get_delivery`, `get_messages`, `add_to_cart`, `checkout`, `track_delivery`
- [amazon](/skills/reference/logistics/amazon/) — `list_orders`, `get_order`
