---
title: Account-Platform Relationship Ontology
description: Desk-review companion covering what to call the edge between `account` and the service it lives at. `issuer` is wrong — what's right?
---

Desk-review companion to `platform-identity-standards.md` and
`platform-space-models.md`. Those cover *which platforms exist* and *how
platforms model themselves*. This one covers the narrower question:
**what do we call the edge between `account` and the service it lives at?**
`issuer` is wrong. What's right?

---

## 1. Survey

### FOAF — `foaf:account` + `foaf:accountServiceHomepage`

FOAF is the only ontology that explicitly separates the three things we
care about. An `Agent` (Person) *holds* an `OnlineAccount` via
`foaf:account` (domain Agent, range OnlineAccount, label "account",
comment "Indicates an account held by this agent"). The account then
points at the service via `foaf:accountServiceHomepage` (range Document),
*not* at a platform entity — the service is identified by the URL of its
homepage. The name on the account is `foaf:accountName`. The spec text is
explicit: an OnlineAccount "represents the provision of some form of
online service, by some party (indicated indirectly via a
accountServiceHomepage) to some Agent." Note three things: (1) "held" is
FOAF's verb for the person↔account edge, (2) the service is a *homepage
URL*, not a typed entity, and (3) the edge to the service is named in
terms of what the service *provides* ("accountServiceHomepage"), not in
terms of custody or hosting. FOAF learned this the hard way after
hardcoding `foaf:aimChatID`, `foaf:icqChatID` etc. and watching them
rot — documented in our existing `platform-identity-standards.md`.

### Schema.org — `provider` (everywhere) + `sameAs` (for identity links)

Schema.org does **not** have a property called `issuer`, `host`, or
`platform` on any account type. `BankAccount` extends `FinancialProduct`
extends `Service`, and `Service` has **one** property that covers all the
cases we care about: `provider` — "The service provider, service
operator, or service performer; the goods producer" (range Organization
or Person). That is the single relationship schema.org uses for Chase →
a Chase checking account, Principal → a retirement fund, and Twitter →
(by implication) a user's account. When schema.org models a Person's
*social* account, it doesn't use an account class at all — it uses
`sameAs` on the Person, pointing at the profile URL. The identity is
*implicit in the URL domain*. There is no `sameOn`, no `accountAt`, no
`host`. The relationship between a person and their social presence is
degenerate — just a `sameAs` link to a web document.

### ActivityPub / ActivityStreams 2.0 — *implicit via URL authority*

This one is fascinating because ActivityPub deliberately refuses to name
the relationship. An `Actor` has an `id` (a URI), an `inbox`, an
`outbox`, and an `endpoints` map. There is **no** `host`, `instance`,
`server`, or `attributedTo` property that points at the instance. The
W3C spec says the server affiliation is "implicit: an Actor's `id` (a
URI with authority belonging to that of their originating server)
establishes which server hosts it." The hosting relationship is encoded
in the URL authority of the actor's ID, not as a first-class property.
This is elegant for a federated protocol (the instance *is* the domain),
but it means ActivityPub has nothing to teach us about the
*name* of the edge — they just refused to name it.

### Solid / WebID — `solid:oidcIssuer`

Solid (Tim Berners-Lee's decentralized web project) has a WebID profile
ontology where a person's profile document links to the OIDC provider
that authenticates them. The property is `solid:oidcIssuer`
(`http://www.w3.org/ns/solid/terms#oidcIssuer`), range is a URL of the
identity provider. Note the name: **`oidcIssuer`**, not `issuer` —
Solid deliberately namespaced the jargon because the word "issuer" alone
is meaningless outside OAuth context. That's a warning sign for us.

### OAuth 2.0 / OIDC — `iss` is *load-bearing* for tokens

`iss` (issuer) in OIDC means: "Issuer Identifier for the Issuer of the
response" — a case-sensitive HTTPS URL that is the *signing authority*
for this token. It exists in the context of a JWT that has a signature
and a subject claim (`sub`) that is "locally unique and never reassigned
within the Issuer." The OIDC spec does not pick "issuer" over "provider"
for any ontological reason — it's specifically about **who cryptographically
signed this assertion**. If you're not storing a signature and a subject
claim, you're not using `iss` in its spec'd sense. Copying the word into
an account shape is cargo-culting: it carries OAuth baggage for zero
OAuth benefit.

### FIBO — `hasAccountHolder` (the customer), servicer for the bank

FIBO (the Financial Industry Business Ontology, the reference ontology
for banking) is structured around "the party that holds an account"
being the *customer*, not the bank. A reference to `hasAccountHolder`
exists in FIBO's derivatives (DER/Futures) modules. The bank side is
named in ISO 20022 terms (see next), not as "issuer" or "provider." FIBO's
top-level modeling treats an account as an agreement between two parties:
the holder (customer) and the servicer (bank). "Holder" in banking means
the opposite of what it means colloquially — the customer holds it, the
bank services it. That's exactly the custody flip that Joe was pointing
at in the original framing.

### ISO 20022 — `AccountServicer` and `AccountOwner`

ISO 20022, the global standard for financial messaging (used by SWIFT,
SEPA, Fedwire), nails the distinction cleanly. Every cash account
message references two party roles:

- **AccountOwner** — "Party that owns the account." In colloquial terms,
  the customer. Joe owns the Chase checking account.
- **AccountServicer** — "Party that manages the account on behalf of the
  account owner, that is, manages the registration and booking of
  entries on the account, calculates balances on the account and
  provides information about the account." In colloquial terms, Chase.

The verb is **"services."** Chase *services* Joe's account. Principal
*services* the 401(k). This is the most precise vocabulary any of the
surveyed ontologies offers for the custodial case. Note that ISO 20022
also distinguishes `AccountServicer` from `Custodian` (a custodian holds
securities) and `IssuingInstitution` (the entity that *created* a
financial instrument, e.g. the Treasury for a T-bill). Three distinct
roles, three distinct words.

### Wikidata — platforms-as-entities, no verb

Wikidata models platforms as first-class entities with Q-IDs (Q918 for
Twitter/X, Q866 for YouTube, Q144644 for defunct ICQ). The edge from an
account to the platform is typically via `P2002` (Twitter username) or
similar per-platform properties — still the FOAF `aimChatID` pathology.
Wikidata hasn't named the *abstract* relationship either. What Wikidata
contributes is a stable external reference (Q-IDs survive rebrand), but
no vocabulary for the edge itself. Already covered in our existing
`platform-identity-standards.md` research note.

### PKM tools — they all fudge it

- **Obsidian (Dataview, Bases)**: no schema. Users write whatever
  frontmatter key they feel like — `source:`, `platform:`, `service:`,
  `where:`. No convention, no enforcement.
- **Logseq**: properties are untyped. Same situation.
- **Roam**: attributes are free-form. Same.
- **Notion**: databases have typed properties but no ontology. Every
  user invents their own "Platform" select field.
- **Tana**: supertags give you real schema, but the name of the edge is
  whatever the schema author chose. Tana itself ships no guidance.
- **Readwise**: uses a `source` field (Kindle, Instapaper, Twitter) as
  a tagged string. Not an entity, not a relationship, just a label.

None of these can teach us the *right* name because none of them have
been forced to face the question. They punt to string fields and let
users sort it out. We're building a typed graph, so we can't punt.

---

## 2. The Three Relationships — Collapse or Split?

From the survey, there are genuinely three different edges hiding
inside our current `issuer` field:

**(a) Host / platform — the service is the place the identity exists.**
Reddit, GitHub, Facebook, Mastodon instance. The account has no meaning
*off* the platform; if the platform dies, the identity dies with it.
Schema.org models this with nothing (it uses `sameAs` at the Person
level). FOAF models it with `accountServiceHomepage`. ActivityPub
encodes it in the URL authority. There is **no verb** — the account just
*is on* the platform.

**(b) Custodian / servicer — the service holds a thing on your behalf,
and you can move the thing.** Chase checking, Principal 401(k),
Coinbase custodial wallet. The account references an asset that has
independent existence; if Chase dies, you move your money to another
bank and the balance survives. ISO 20022 calls this **`AccountServicer`**
and FIBO calls the customer side **`AccountHolder`**. The verb is
"services" or "is held by / is serviced by."

**(c) Token issuer — cryptographic signer of an assertion.** OIDC `iss`.
This is the *smallest* of the three — it only matters when you're
storing a signed token and need to know who can verify the signature.
It's also the *least like* what we currently mean by `issuer` on
`account`. When a skill like `reddit-web` stores an account for
`joe_reddit`, there is no JWT, no signature, no `sub` claim — we're
just recording a cookie-authed identity. Calling Reddit the "issuer"
is a category error. We're using an OAuth word for a non-OAuth thing.

**So: collapse or split?**

The cleanest answer is **two, not three**. The token issuer (c) is a
proper subset of the host case (a) whenever the host runs an OIDC
provider. In the FOAF/schema.org tradition both (a) and (b) collapse
into a single `provider` relationship; the distinction between
"hosts an identity" and "holds an asset" is a property of the *service
kind*, not of the edge. A Chase account's provider is a bank; a Reddit
account's provider is a platform. The edge is the same edge, just
pointing at differently-typed nodes.

The argument for **keeping them split** is that the user actions differ:
you can *move* a custodial asset (transfer your 401(k) from Principal
to Fidelity → the account's custodian changes but the asset is the
same), but you cannot *move* a social identity (you can't transfer
`github.com/joe` to another host — you can only create a new account
elsewhere and link them). That operational asymmetry *is* real. But it
doesn't have to live in the name of the relationship; it can live in
whether the shape allows the relationship to be *rewritten* (custody
can change; host cannot). We can model that with a single edge name and
a shape-level rule that `host` edges are immutable on an account record
while `servicer` edges are mutable — or with a single edge and rely on
the downstream shape of the service node.

**My read: one edge, one name.** The ontology stays clean, the
difference between "you can leave Chase" and "you can't leave Reddit"
belongs in the service node's type (`financial_institution` vs
`platform`), not in the edge name. This matches schema.org (`provider`
everywhere), FOAF (`accountServiceHomepage` for both social and
financial), and ISO 20022 (one `AccountServicer` for both retail bank
and asset manager).

---

## 3. Recommendation

### Top two naming options

**Option A: `at` (the preposition)**

- `account.at` → the service the account exists at
- `post.at` → the service the post was published at
- `message.at` → the service the message was sent at

Arguments for: English-native. Reads out loud correctly for every case
("Joe's account at Chase," "Joe's account at GitHub," "the post at
reddit.com," "the message at Signal"). Two letters — impossible to
over-specify. Survives all three edge cases (host, custodian, issuer)
because "at" makes no claim about the nature of the relationship, just
about location. Fits Joe's camelCase convention trivially (`at` stays
`at`). No OAuth baggage. No FIBO baggage.

Arguments against: very short names are *sometimes* hard to grep for
(`.at(` matches Python method calls). Ambiguous with `Object.at()` in
some JS contexts. Not an existing property name in any surveyed
ontology, so we're inventing rather than stealing.

**Option B: `service` (the noun)**

- `account.service` → the service this account belongs to
- `post.service` → the service this post was published on

Arguments for: directly mirrors schema.org's `Service` class (the
parent of BankAccount, Reservation, etc.). Semantically precise — "this
account is an instance of the `Service` offered by X." Matches FOAF's
wording (the OnlineAccount "represents the provision of some form of
online service"). Matches how Readwise/Obsidian users already casually
write `service: kindle`. No confusion with "platform" (which carries
both "technology platform" and "publishing platform" baggage).

Arguments against: `service` is overloaded in engineering ("backend
service," "service worker," "account service provider"). Slightly more
typing than `at`. Doesn't read as naturally in sentences
("Joe's account service GitHub" vs. "Joe's account at GitHub").

**My pick:** `at`. It's short, idiomatic, and free of prior art baggage.
`service` is my backup if we ever need a noun form alongside the edge
(e.g. `service_kind: "financial_institution" | "platform" | "imap_server"`).

Discarded candidates:
- `platform` — already muddy in the current schema; loses for carrying
  OAuth/PKM fudge-field smell.
- `provider` — semantically clean but collides with OAuth "identity
  provider" and is already overloaded as a term of art. Skim any
  Terraform file.
- `hostedBy`, `custodiedBy` — force the split we just argued against.
- `heldBy` — technically correct for banking but *backwards* in the
  FIBO sense (the holder is the customer, not the bank).
- `on` — good for `post.on reddit.com` but bad for `account.on chase`
  (you don't have an account *on* Chase, you have one *at* Chase).
- `accountAt`, `onService` — redundant compounds where the prefix
  duplicates the shape name.
- `issuer` — the thing we're trying to kill.

### Concrete proposal for the RFP

The shapes-from-skills RFP open question #5 is:
> How do the identity rules interact with the existing `also` chain?
> If `email` is also a `message`, and `message.identity = [[messageId]]`,
> does email inherit the identity rule?

Neighboring that question, add a new open question:

**#5b. Rename `issuer` on the `account` shape to `at`.** Simultaneously,
kill the standalone `platform` field on `post`, `message`, and `task`
shapes — replace it with `at`, pointing at the same service node that
`account.at` points at. The identity rule for `account` becomes
`[[at, identifier]]` (still compound, same semantics). Migration is
zero: no users, no data. Net effect: one edge name across all
shape-level "which service does this live at" references, consistent
with FOAF's `accountServiceHomepage` wording at a third of the
characters. Downstream: service nodes get a `kind` field
(`platform | bank | broker | mail_server | imap | phone_carrier`) so
skills can still branch on "is this a custodial asset or a social
identity" when they need to.

This also resolves an architectural wart: today, `platform` on `post`
and `issuer` on `account` are *the same relationship*, expressed with
two different words. Unifying them under `at` means a Reddit post and
the Reddit account that authored it both point at the *same* service
node, which is the whole memex dream.

---

## 4. Edge Cases That Break Any Scheme

These are the ones worth walking through before committing, because
they're where the pretty naming scheme falls down.

**Phone-number identities (iMessage, SMS, WhatsApp).** What is the
"service" for `+1-555-...`? For iMessage, it's Apple — but that phone
number also works on SMS through whatever carrier you're on, and it
*also* works on WhatsApp, Telegram, Signal. One identifier, many
services. Answer: the phone number is a *contact point* (schema.org's
`ContactPoint`), not an account. The account is `joe@apple.com` (or
the Apple ID), and iMessage *delivers to* that phone number. Phone
number → `ContactPoint` entity, `contactPointOn: [imessage, sms,
whatsapp, signal]` — a different edge entirely from `account.at`. This
is the same reason FOAF split `foaf:mbox` (mailbox) from `foaf:account`.

**Email addresses.** Is `joe@gmail.com` an account at Gmail, or an
email address at the gmail.com domain? Both. Model the account
(`at: gmail.com`, `identifier: joe`) and the email address as a
derived `ContactPoint` tied to it. Any skill using it for identity
uses the account; any skill using it for delivery uses the ContactPoint.
The `at` edge survives cleanly because the email address doesn't *have*
an `at` — it's a value, not an account.

**Federated logins ("Sign in with Google" to Notion).** The account at
Notion has `at: notion.so`, and is linked (via a separate `authenticatedBy`
or `sameAs` edge) to the Google account at `at: google.com`. Two
accounts, two `at` edges, one cross-link. The fact that the Notion
session is signed by Google's OIDC issuer is a property of the *session*
or *token*, not of the Notion account shape. This is where a `token`
shape — if we ever add one — *would* legitimately carry an OIDC `iss`
field, using the real spec word in the real spec context.

**Multi-custodian assets (a retirement fund that rolled over).** A 401(k)
was at Principal 2018–2023, then moved to Fidelity 2023–present. Two
options: (a) one `account` record with a mutable `at` edge and history
in a separate `account_transfer` shape, or (b) two `account` records
linked by `continuationOf` / `rolledOverTo`. ISO 20022 takes approach
(b) — each custodian-account pair is a distinct account, with
relationships between them. I lean (b) for AgentOS too: it preserves
immutable history, makes queries easier ("show me the balance at
Principal in 2022"), and avoids the "what was the value of this
record at time T" versioning problem. `at` stays immutable per record.

**Brokerage accounts holding assets from multiple issuers.** A Fidelity
brokerage holds AAPL shares (issued by Apple), a Treasury bond (issued
by the US Treasury), and cash (issued by the Fed). The brokerage is the
`at` / servicer. The *assets inside* the account point at issuers via
a different edge (`issuer` on the `security` shape, now used in its
proper ISO 20022 sense — the entity that created the instrument). This
is the case where `issuer` actually earns its keep. On `account` →
wrong word. On `security` → right word.

**Self-hosted / self-custody.** If I run my own Mastodon instance at
`mastodon.joe.com`, the `at` is... my own domain? A "self" entity? The
cleanest answer is that self-hosted services are still services, and
get service entities. `mastodon.joe.com` is a service node with
`kind: platform, software: mastodon, operated_by: person:joe`. My
account at it has `at: mastodon.joe.com`. No special case needed. Same
for a self-custody crypto wallet: the "service" is the protocol
(Ethereum) or the hardware (Ledger), depending on what matters for
the query.

**Offline accounts (a mattress-stuffed savings, a cash envelope).** There
is no service. The `at` edge is null or points at a `self` entity.
This is the degenerate case, and it's fine — null `at` just means
"no external service is involved." Identity rule `[[at, identifier]]`
becomes `[[identifier]]` effectively (identifier unique within the
owner's graph).

---

## 5. One-line summary

Steal **`at`** for the edge, adopt ISO 20022's intuition that the
service *services* the account (not issues it), put the platform-vs-bank
distinction on the service node as a `kind`, and fold
recommendation-for-RFP-open-question-5b into the shapes-from-skills
proposal phase. Sources below for traceability.

---

## Sources

- [FOAF Spec — OnlineAccount](https://xmlns.com/foaf/spec/#term_OnlineAccount)
- [Schema.org — BankAccount](https://schema.org/BankAccount)
- [Schema.org — FinancialProduct](https://schema.org/FinancialProduct)
- [Schema.org — sameAs](https://schema.org/sameAs)
- [Schema.org — ContactPoint](https://schema.org/ContactPoint)
- [ActivityStreams 2.0 Vocabulary (W3C)](https://www.w3.org/TR/activitystreams-vocabulary/)
- [ActivityPub (W3C)](https://www.w3.org/TR/activitypub/)
- [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)
- [Solid WebID Profile](https://solid.github.io/webid-profile/)
- [Solid Vocabularies (`solid:oidcIssuer`)](http://solid.github.io/vocab/)
- [FIBO — EDM Council](https://spec.edmcouncil.org/fibo/)
- [FIBO GitHub — orphaned `hasAccountHolder`](https://github.com/edmcouncil/fibo/issues/989)
- [ISO 20022 Data Dictionary](https://www.iso20022.org/understanding-data-dictionary)
- [ISO 20022 — AccountServicer / AccountOwner (SWIFT)](https://www.swift.com/standards/iso-20022/iso-20022-standards)
- [Wikidata](https://www.wikidata.org/)
- Prior AgentOS research: `_projects/_research/platform-identity-standards.md`
- Prior AgentOS research: `_projects/_research/platform-space-models.md`
