---
title: auth_challenge
description: "A platform demands something only a human (usually) can do — scan a QR"
sidebar:
  label: auth_challenge
---

A platform demands something only a human (usually) can do — scan a QR
with a phone, click an OAuth consent, type a code that was mailed out of
band. The challenge is a successful result, not an error: the login op
did its job, and this is what came back. `artifact` is display-ready
text — a Unicode QR block, a consent URL — so one string renders on
every surface an agent lives on: a terminal, a chat, the desktop act
window. No image pipeline, no per-surface renderer.

For `code_sent` the human may not be needed at all: `instructions`
tells the agent to try `email_lookup` providers before relaying.

| Metadata | Value |
|---|---|
| **Plural** | `auth_challenges` |
| **Subtitle field** | `instructions` |

## Fields

| Field | Type |
|---|---|
| `kind` | `string` |
| `payload` | `string` |
| `artifact` | `text` |
| `instructions` | `text` |
| `expiresAt` | `datetime` |
| `continueWith` | `string` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[OAuth 2.0 Device Authorization Grant (RFC 8628)](https://datatracker.ietf.org/doc/html/rfc8628)** — The device flow returns the human-must-act moment as data, not as an error: user_code + verification_uri + expires_in, with the client polling the token endpoint until the human acts. Same anatomy here — payload/artifact ≈ user_code/verification_uri, expiresAt ≈ expires_in, continueWith ≈ the polling step.
- **[whatsapp-web.js + qrcode-terminal](https://github.com/pedroslopez/whatsapp-web.js)** — The proven precedent for QR-as-text: the linked-device QR payload is re-rendered as Unicode block characters in a terminal and scanned straight off the screen. `artifact` generalizes that to every text surface.
