---
title: payment_method
description: "A saved payment instrument — credit/debit card, PayPal/Venmo account,"
sidebar:
  label: payment_method
---

A saved payment instrument — credit/debit card, PayPal/Venmo account,
device wallet (Apple Pay, Google Pay, Paze), bank/ACH, travel credit,
gift card, corporate account (UATP), BNPL handle, crypto wallet.

Generic across vendors. A United "AMEX Platinum ending 1007", a Stripe
`pm_xxx`, a PayPal billing agreement, a Shopify Shop Pay token, and
a `com.apple.pay` merchant token are all the same shape — what differs
is `type`, `subtype`, and the opaque `providerTokens` blob.

--- PCI SAFETY: WHAT THIS SHAPE IS FOR, AND WHAT IT ISN'T ---
PCI DSS v4.0 (Req. 3.3.1) forbids storing the PAN, CVV, full track
data, PIN, or PIN block. AgentOS MUST NEVER persist any of those —
not in a field, not in `providerTokens`, not in the graph database,
not in logs. What IS storable (PCI-safe), and what this shape carries:
* BIN (first 6, or 6+2 BIN range) — `binRange`
* last 4 digits — `last4`
* expiry month + year — `expMonth`, `expYear`
* brand / issuer name — `brand`, `subtype`
* cardholder display name — `holderName`
* opaque provider-issued tokens (PersistentToken, AccountNumberToken,
Stripe `pm_xxx`, PayPal billingAgreementId, Apple Pay device PAN
reference) — `providerTokens` (json; agent passes through but
never inspects)
The opaque tokens ARE the detokenization references held by the
provider — the whole point of the PCI tokenization pattern is that
possession of the token lets the MERCHANT charge the card, but the
token alone is not card data. Same pattern as Stripe payment_methods,
Apple Pay's DPAN, Google Pay's network token, Visa Token Service.

--- SUBTYPE CODES ---
`subtype` uses the IATA airline payment code when context is air
travel (AX/VI/MC/DS/DC/TP/JC/UP), falling back to a normalized token
otherwise (PP, PZ, AP, TC, MPVI, ACH, APPLE_PAY, GOOGLE_PAY, SHOP_PAY,
KLARNA, AFFIRM). IATA 2-char codes are defined in IATA Resolution
890 and live in the PADIS catalog; they're what airline PNRs and
EMDs use in the FOP field.

--- DISTINCT FROM ADJACENT SHAPES ---
- `financial_account` is the SOURCE of funds (your Chase checking,
your Coinbase wallet). A `payment_method` is the INSTRUMENT used
to present those funds at a merchant. One financial_account can
back many payment_methods (physical card + Apple Pay virtual card
+ ACH).
- `account` is a login identity. One account (united.com login)
holds many payment_methods.
- `transaction` is the POST-CHARGE record.
- `billing_address` is the postal address bound to this instrument.

Identity: (at, identifier). `at` is the namespace that issued the
saved reference (united.com, stripe.com, paypal.com). `identifier`
is the stable provider-side id — AccountNumberToken for airlines,
`pm_xxx` for Stripe, billingAgreementId for PayPal. NEVER the PAN.

| Metadata | Value |
|---|---|
| **Plural** | `payment_methods` |
| **Subtitle field** | `displayName` |
| **Identity** | `at`, `identifier` |

## Fields

| Field | Type |
|---|---|
| `identifier` | `string` |
| `type` | `string` |
| `subtype` | `string` |
| `brand` | `string` |
| `displayName` | `string` |
| `customDescription` | `string` |
| `holderName` | `string` |
| `last4` | `string` |
| `binRange` | `string` |
| `expMonth` | `integer` |
| `expYear` | `integer` |
| `expirationDate` | `string` |
| `currency` | `string` |
| `balance` | `number` |
| `fingerprint` | `string` |
| `isDefault` | `boolean` |
| `isPrimary` | `boolean` |
| `isExpired` | `boolean` |
| `isSelected` | `boolean` |
| `status` | `string` |
| `providerTokens` | `json` |
| `metadata` | `json` |

## Relations

| Relation | Target |
|---|---|
| `at` | [`actor`](/shapes/reference/actor/) |
| `account` | [`account`](/shapes/reference/account/) |
| `holder` | [`person`](/shapes/reference/person/) |
| `billingAddress` | [`place`](/shapes/reference/place/) |
| `fundingAccount` | [`financial_account`](/shapes/reference/financial_account/) |
| `issuer` | [`actor`](/shapes/reference/actor/) |
| `membership` | [`membership`](/shapes/reference/membership/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[Stripe PaymentMethod API](https://docs.stripe.com/api/payment_methods/object)** — The gold standard. Our type/subtype ≈ Stripe's `type` + `card.brand`; last4/expMonth/expYear/fingerprint map 1:1 to `card.last4/exp_month/exp_year/fingerprint`. Stripe's billing_details is our `billingAddress` relation. Stripe's `pm_xxx` id is the canonical opaque handle.
- **[PCI DSS v4.0 Requirement 3 (Protect Stored Account Data)](https://www.pcisecuritystandards.org/document_library/)** — Defines what's storable: PAN truncated, expiry, cardholder name, service code. FORBIDS full PAN (unencrypted), CVV/CVC2/CID, PIN/PIN block, track data. This shape carries only the permitted subset. Opaque tokens are NOT card data under PCI — they're the merchant/provider's detokenization references; storing them is the recommended mitigation (Req. 3.5 tokenization).
- **[IATA Resolution 890 / PADIS Form-of-Payment codes](https://www.iata.org/en/publications/store/passenger-and-baggage-tariffs/)** — Source for the airline 2-char `subtype` codes: AX (Amex), VI (Visa), MC (MasterCard), DS (Discover), DC (Diners), TP (UATP), JC (JCB), UP (UnionPay). These are the codes embedded in PNR FOP fields and EMD records. We keep them verbatim so airline checkout round-trips work without translation.
- **[W3C Payment Request API / Payment Method Identifiers](https://www.w3.org/TR/payment-method-id/)** — Browser-standard payment abstraction. `basic-card`, `https://apple.com/apple-pay`, `https://google.com/pay`, `https://paypal.com` are the method identifiers — our type/subtype combo is a normalized form.
- **[Apple Pay Payment Token / Google Pay Network Token](https://developer.apple.com/documentation/passkit/apple_pay/payment_token_format_reference)** — Device-bound token replaces the PAN on-chain. The DPAN and cryptogram live in `providerTokens`; `last4` on the wallet surfaces the DEVICE last-4, not the funding card's last-4.
- **[schema.org/PaymentMethod + LoyaltyProgram](https://schema.org/PaymentMethod)** — schema.org's PaymentMethod is a thin enum (CreditCard, Cash, PaymentCard, ByInvoice). We extend it into a real shape with tokens and holder. Our `type` overlaps its enumeration values.
- **[PayPal Billing Agreements / Vault](https://developer.paypal.com/docs/multiparty/vault/)** — PayPal's saved-method pattern — billingAgreementId is the opaque handle, used like our `providerTokens`. Payer given_name → `holderName`. No last4 (PayPal-as-wallet has no card number surface); our shape accommodates via nullable last4.
- **[EMVCo Tokenisation Framework v2.0](https://www.emvco.com/specifications/payment-tokenisation/)** — Industry spec for network tokens (Visa Token Service, Mastercard MDES). Defines token requestor, token reference id, PAR (Payment Account Reference) — PAR is the cross-token dedupe primitive our `fingerprint` field aligns with when the provider surfaces it.
