---
title: "Identity Verification Across Platforms: 2025-2026 Research"
description: Research for the AgentOS `claims` relationship model — how Person entities link to Account entities with epistemic provenance.
---

## Table of Contents

1. [Taxonomy of Verification Methods](#1-taxonomy-of-verification-methods)
2. [Grassroots & Community Verification](#2-grassroots--community-verification)
3. [Decentralized Identity Standards](#3-decentralized-identity-standards)
4. [Platform-Level Verification](#4-platform-level-verification)
5. [Web of Trust Models](#5-web-of-trust-models)
6. [AI-Era Challenges](#6-ai-era-challenges)
7. [Practical Patterns for a Local Knowledge Graph](#7-practical-patterns-for-a-local-knowledge-graph)
8. [Recommendations for the Claims Relationship](#8-recommendations-for-the-claims-relationship)
9. [Key References](#9-key-references)

---

## 1. Taxonomy of Verification Methods

Ranked by confidence level, highest to lowest. Each method produces different evidence and has different requirements.

| Tier | Method | Confidence | Evidence Produced | Requires | Decay Rate |
|------|--------|-----------|-------------------|----------|------------|
| **S** | Cryptographic key proof | 0.95-0.99 | Signed statement linking identities | Private key access | Low (key compromise) |
| **S** | Biometric + liveness (Worldcoin Orb) | 0.95 | Iris hash, zero-knowledge proof | Physical hardware | Very low |
| **A** | In-person verification | 0.90-0.95 | Witness attestation, key signing | Physical co-presence | Medium (people change) |
| **A** | Bidirectional link (rel-me) | 0.85-0.90 | Two URLs linking to each other | Write access to both platforms | Medium (links can break) |
| **A** | DNS TXT record proof (Bluesky, Keyoxide) | 0.85-0.90 | DNS record content | Domain control | Medium (domain can lapse) |
| **B** | OAuth/OIDC login | 0.80-0.85 | Access token, ID token with subject claim | Account session on provider | High (sessions expire) |
| **B** | Platform API confirmation | 0.80-0.85 | API response with account details | API access, auth | High (tokens expire) |
| **B** | Social graph verification (BrightID) | 0.75-0.85 | Connection graph, group membership | Real social connections | Medium |
| **B** | Platform badge (blue check, etc.) | 0.70-0.80* | Badge status via API or scraping | Platform grants it | Medium (policies change) |
| **C** | Self-claimed (user told us) | 0.65-0.75 | User assertion + timestamp | User input | Low (unless revoked) |
| **C** | Bio/profile cross-reference | 0.50-0.65 | Link found in bio text | One-directional link | High (bios change) |
| **C** | Same handle heuristic | 0.30-0.50 | Username match | Nothing | Low (but low confidence) |
| **D** | AI extraction/inference | 0.20-0.40 | Model output, source text | NLP pipeline | High |
| **D** | Third-party assertion | 0.15-0.35 | Someone else's claim | Another person's credibility | Depends on asserter |

*Platform badges dropped in confidence since 2023 — Twitter/X blue checks are now purchasable ($8/mo) and no longer imply identity verification. Meta Verified requires government ID (higher confidence). YouTube verification requires 100K subscribers (social proof, not identity).*

**Key insight:** No single method is conclusive. The strongest signal comes from **combining multiple methods** (Gitcoin Passport's model). A self-claimed link + bidirectional rel-me + same handle across platforms = much higher combined confidence than any single method.

---

## 2. Grassroots & Community Verification

### Crypto Community Patterns

**Selfie verification on Telegram/Signal:**
Crypto communities use ad-hoc KYC in group chats. Common pattern: new member must post a selfie holding a handwritten note with the group name and date. Moderators visually confirm. Evidence: photo saved in chat history. Weakness: deepfakes are making this less reliable; works best in small high-trust groups where members know faces.

**Telegram KYC bots:**
Automated bots (`@IDCheckBot`, `@PersonaKYCbot`) can require government ID + live selfie matching before granting group access. This is essentially centralized KYC outsourced to a bot service — higher confidence but requires trusting the bot operator with your ID.

**Key signing parties (PGP tradition):**
In-person events where participants exchange PGP key fingerprints and verify government IDs. Each participant signs the others' public keys, creating web-of-trust edges. Still practiced in some FOSS communities. The format: exchange fingerprints on paper, verify ID in person, sign keys later at home. Evidence: cross-signatures on public keys.

**What works:** Small group, high-stakes contexts where members have existing social connections. Verification is a social ritual, not a technical protocol. The social pressure of "everyone in this group vouched for you" is itself a trust mechanism.

### Proof of Personhood Systems

**Worldcoin / World ID:**
- Uses custom biometric hardware (the "Orb") for iris scanning
- Creates a privacy-preserving proof via zero-knowledge proofs — you can prove you're a unique human without revealing which human
- Verification levels: Orb (strong biometric), Orb+ (adds ongoing authentication), Secure Document
- ~7M verified users as of late 2025
- Controversy: collecting biometric data, hardware centralization, privacy concerns
- **For our model:** Worldcoin proof = very high confidence that an account is operated by a unique human, but doesn't link to a specific known person. It's proof of personhood, not proof of identity.

**BrightID:**
- Social graph-based: you connect with people who know you, the graph structure reveals duplicates
- "Meets" verification: join a video call with a designated "Seed" host, show your face, respond to questions. ~73K people verified this way.
- Connection levels: "already known," "just met," "suspicious"
- Avoids biometrics entirely — relies on human recognition over AI
- Groups must have minimum 3 people; groups verify each other
- **For our model:** BrightID verification = moderate-high confidence of unique personhood, evidence is the social graph itself + connection timestamps.

**Gitcoin Passport:**
- Aggregator model: collect "stamps" from multiple verification providers
- Each stamp has a weight; combined score determines credibility
- Stamp sources include: BrightID, Proof of Humanity, ENS, GitHub activity, Google account, Facebook, Twitter, LinkedIn, Discord
- Threshold: score of 20+ out of 100 required for Gitcoin donation matching
- **For our model:** This IS the pattern we should learn from. Multiple weak signals combined = strong composite signal. The scoring/weighting approach maps directly to confidence levels on claims.

**Proof of Humanity (now Humanity Protocol):**
- Video submission + vouching from existing verified members
- Creates a Sybil-resistant registry of unique humans
- On-chain, uses Kleros for dispute resolution
- **For our model:** Evidence is the video submission + voucher chain.

### Patterns That Emerged Organically

1. **Layered verification:** Communities naturally develop tiers — new members get limited access, prove themselves over time through participation, eventually get vouched for full access. Time + activity + social vouching = graduated trust.

2. **Reputation portability:** Active GitHub profile → trust in developer communities. Stack Overflow karma → credibility. These aren't formal verification — they're social proof through sustained activity.

3. **The "introduction" pattern:** In high-trust groups (invite-only Discords, private Telegram groups), new members need an existing member to introduce them. The introducer's reputation is at stake. This is the oldest verification mechanism: "I know this person."

---

## 3. Decentralized Identity Standards

### W3C DID (Decentralized Identifiers)

**Status:** DID v1.1 is in Working Draft (January 2026). DID v1.0 reached W3C Recommendation in 2022.

**How it works:**
- A DID is a URI like `did:web:example.com` or `did:plc:abc123`
- Resolves to a DID Document containing public keys, service endpoints, authentication methods
- The DID method (the part after `did:`) determines how resolution works
- Multiple DID methods exist for different trust models

**Key DID methods for our model:**

| Method | Resolution | Trust Model | Used By |
|--------|-----------|-------------|---------|
| `did:web` | HTTPS fetch of `/.well-known/did.json` | DNS/TLS (web PKI) | General purpose |
| `did:key` | Self-contained in the identifier | Cryptographic (key IS the identity) | Ephemeral, local |
| `did:plc` | Public Ledger of Credentials | Auditable operation log | Bluesky/AT Protocol |
| `did:pkh` | Blockchain address | Blockchain consensus | Ethereum/crypto wallets |
| `did:ion` | Bitcoin-anchored (Sidetree) | Bitcoin blockchain | Microsoft ION |

**For our model:** DIDs are the emerging standard for persistent, cryptographically verifiable identifiers. `did:key` is interesting for local-first — the identifier IS the public key, no resolution infrastructure needed. We could generate `did:key` identifiers for local person entities.

### W3C Verifiable Credentials (VC 2.0)

**Status:** Reached W3C Recommendation in May 2025 — this is now a full standard.

**The three-party model:**
```
Issuer  ───issues───→  Credential  ───held by───→  Holder
                                                      │
                                                   presents
                                                      │
                                                      ▼
                                                   Verifier
```

**Credential structure:**
- **Subject:** Who the credential is about
- **Issuer:** Who made the claim (with cryptographic signature)
- **Claims:** The actual assertions (name, age, membership, etc.)
- **Evidence:** How the issuer determined the claims are true
- **Validity period:** When the credential expires
- **Status:** Revocation information (Bitstring Status List v1.0)
- **Proof:** Cryptographic signature (EdDSA, ECDSA, or JOSE/COSE)

**Key capabilities:**
- Selective disclosure — holder can present only some claims
- Zero-knowledge proofs — prove properties without revealing values ("I'm over 21" without revealing birthdate)
- Multiple encoding formats: JSON-LD, SD-JWT
- Crypto-agile: designed to accommodate post-quantum cryptography

**For our model:** The VC claim structure maps beautifully to our `claims` relationship. A claim has an issuer (who asserted it), evidence (how they know), confidence (how sure), and a timestamp. We don't need to implement the full VC stack, but the conceptual model is exactly right.

### IndieWeb rel-me

**How it works:**
1. Your website has `<a rel="me" href="https://twitter.com/yourname">` 
2. Your Twitter profile links back to your website
3. Any verifier can check both links exist → bidirectional proof of control

**Real-world adoption:**
- Mastodon displays green checkmarks for verified rel-me links on profiles
- No central authority, no documents to submit, works for everyone
- Privacy-friendly: verification is public links, not private data
- Tools: Indiewebify.me, verify-me browser extension

**Strengths:** Dead simple, privacy-respecting, decentralized, already deployed at scale (Mastodon). **Weaknesses:** Only works for entities with web presence (websites, profiles with link fields). Doesn't prove the person behind the keyboard — proves the same entity controls both pages.

**For our model:** rel-me checking is one of the best verification methods we can actually perform locally. Given a person's website and their social profiles, we can check for bidirectional links. Evidence: the two URLs + timestamp of check. Confidence: 0.85-0.90.

### Keybase Proofs Model

**How it worked (the gold standard for cross-platform identity):**
1. User has a Keybase account with a cryptographic key pair
2. User "announces" their key on Twitter by posting a signed message
3. User does the same on GitHub (signed gist), Reddit (signed post), their website (signed file), etc.
4. Keybase client verifies: the message on each platform is (a) signed by the user's key and (b) posted from the claimed account
5. Result: cryptographically provable chain — Keybase ↔ Twitter ↔ GitHub ↔ Reddit ↔ website

**The Proof Verification Language (PVL):**
- JSON-based DSL for describing how to validate proofs on each platform
- Server-updatable without client updates (critical for mobile)
- PVL instructions hashed into Merkle tree for auditability
- Handles platform format changes gracefully

**Device evolution:**
- Originally single PGP key (fragile — moving keys between devices was painful)
- Evolved to per-device NaCl keys connected through a "sigchain" (chain of authority)
- New devices provisioned via peer-to-peer auth with existing devices
- Key lesson: multi-device key management is the hard UX problem

**What happened after Zoom acquisition (2020):**
- Development effectively ceased
- Blog went silent
- Integrations broke (Mastodon removed Keybase support)
- Service still technically running but unmaintained
- No new platform proof types added
- Community trust eroded — single point of failure realized

**Lessons for our model:**
1. The proof model was brilliant — the implementation dying because it depended on one company is the lesson
2. Store proofs locally, not on a central service
3. The PVL concept (declarative proof verification rules) is worth adopting — rules for how to verify each platform's proofs
4. Per-device keys > single key

### Keyoxide (Modern Replacement)

**What it is:** Fully decentralized Keybase replacement based on the Ariadne Identity Specification.

**How it works:**
- Identity proofs embedded directly in OpenPGP keys as notations: `proof@ariadne.id=https://twitter.com/username`
- No central service required — proofs live in the key itself
- Verification: fetch the key, read the proof notations, check each proof URL
- Supports: Mastodon, Reddit, Bluesky, Twitter, GitHub, Telegram, DNS records, more
- Community-driven spec (Ariadne Ratification Committee)

**For our model:** Keyoxide's approach — proofs embedded in keys, verification performed locally — is exactly the local-first pattern we need. No central server, no dependency on a service surviving.

### Bluesky / AT Protocol

**Identity model:**
- Every user has a DID (typically `did:plc:...`) — the persistent identity
- Human-readable handles (`@user.bsky.social` or `@yourdomain.com`) are separate from DIDs
- Handle resolution via DNS TXT record (`_atproto` record) or HTTPS well-known endpoint
- DID documents contain signing keys and service endpoints
- **Custom domain as verification:** Using your own domain as your handle (e.g., `@jay.bsky.team`) proves domain control — like rel-me but built into the protocol

**Public Ledger of Credentials (PLC):**
- Operation log for each DID — all key rotations, handle changes, service endpoint updates
- Auditable history of identity changes
- Currently operated by Bluesky PBC (centralization concern), but protocol allows alternatives

**For our model:** The handle-as-domain-verification pattern is elegant. If someone's Bluesky handle is their own domain, that's strong evidence of domain control (confidence: 0.85-0.90). PLC operation logs show identity history — useful for understanding when an identity was established and how it's changed.

### Farcaster

**Identity model:**
- Numeric Farcaster ID (fid) assigned on-chain via IdGateway contract on Ethereum
- Human-readable usernames (Fnames) optional, associated with fids
- EdDSA key pairs for message signing
- Apps can request delegated signing keys
- Recovery address for key loss

**Key design decisions:**
- Separating numeric ID from namespace prevents squatting/impersonation
- On-chain registration means identity creation has a cost (gas) — Sybil resistance through economics
- Key registry is a smart contract — transparent, auditable

**For our model:** Farcaster proof = high confidence (on-chain identity, economic cost to create). Evidence: Ethereum transaction hash, fid, associated keys. The separation of persistent ID (fid) from human-readable name is a good pattern.

### ENS (Ethereum Name Service)

- `.eth` names as decentralized identifiers (e.g., `vitalik.eth`)
- Text records can store social links, avatars, email — essentially a decentralized profile
- Sign In With Ethereum (SIWE) for authentication
- ENSv2 coming with L2 support
- **For our model:** ENS ownership = proof of Ethereum wallet control. If someone's ENS resolves to social profiles, that's a cross-reference. Confidence: 0.80-0.85 (depends on ENS record accuracy, which is self-asserted).

### Lens Protocol

- Social identity as on-chain primitives (profiles, follows, posts)
- Username system under customizable namespaces
- Built on zkSync L2 — fast, cheap transactions
- Gasless/signless UX for mainstream adoption
- **For our model:** Lens profile ownership = on-chain proof. Lower adoption than ENS/Farcaster, but same pattern.

---

## 4. Platform-Level Verification

### Signal Safety Numbers

**How it works:**
- Each 1:1 chat has a unique "safety number" derived from both parties' public keys
- Displayed as 12 groups of 5 digits (e.g., `12345 67890 12345 ...`)
- Verification: scan QR code in person, or compare numbers verbally/visually
- If a key changes (new device, reinstall), the safety number changes and both parties are alerted
- Verified contacts show a checkmark

**What it proves:** That you're communicating with the same cryptographic identity as before. NOT that the identity belongs to a specific person — that requires out-of-band verification (meeting in person, calling by phone).

**For our model:** Safety number verification between two people = high confidence that future messages come from the same device/key. Evidence: verified safety number + timestamp. But this proves continuity of identity, not initial identity binding.

### Matrix Emoji Verification (Cross-Signing)

**How it works:**
1. Two devices initiate verification (either via in-room message or direct)
2. Both devices display the same set of emojis (Short Authentication String)
3. Users compare emojis out-of-band (in person, via call)
4. If match → devices are cross-signed
5. Once your devices are cross-signed, verifying a person once verifies all their devices

**Key improvement over PGP:** Verify the person once, not every device separately. Cross-signing creates a trust chain from your master key → your device keys → their master key → their device keys.

**For our model:** Emoji verification = high confidence (0.90+). Evidence: cross-signing record, timestamp, method. The cross-signing pattern (verify person, not device) is relevant for how we think about multi-account verification.

### Platform Verification Badges

**Twitter/X (2025):**
- Blue check: $8-16/mo subscription. Account must be 30+ days old, have profile photo, active posting. Government ID optional in some regions.
- Gold check: $1,000/mo for organizations
- Gray check: Government officials
- **Confidence:** Low (0.40-0.60) for blue checks — they prove willingness to pay, not identity. Higher for gold/gray.

**Meta Verified:**
- Requires government-issued photo ID
- Available for Facebook and Instagram
- Monthly subscription ($12-15/mo)
- **Confidence:** Moderate-high (0.75-0.85) — government ID verification is real, but the ID is verified by Meta, not by us.

**YouTube Verification:**
- Requires 100K+ subscribers
- YouTube verifies the channel represents the real creator/brand
- **Confidence:** Moderate (0.65-0.75) — proves the channel is notable and verified by YouTube, but social proof ≠ identity proof.

**For our model:** Platform badge status is a property of the Account entity (`verified: boolean`), not evidence of the Person→Account claim. It's useful context but shouldn't be the primary confidence signal.

### OAuth/OIDC

**How it works for identity:**
1. User clicks "Sign in with Google/GitHub/etc."
2. Redirected to provider, authenticates
3. Provider returns an ID Token containing: subject identifier (sub), issuer, email, name, authentication time
4. The ID Token cryptographically proves: "this person has an active session with this provider, and the provider identifies them as subject X"

**OpenID Connect for Identity Assurance (eKYC):**
- Extension for high-assurance contexts
- Provider can include verification evidence in the token (e.g., "identity verified via government ID on 2025-03-15")
- Assurance levels: self-asserted → email-verified → document-verified → biometric-verified

**For our model:** OAuth is powerful because it proves real-time account access without us storing credentials. If a person can OAuth with their GitHub account, we know they control that account *right now*. Evidence: ID token claims + timestamp. Confidence: 0.80-0.85. But it requires a server (redirect URL) — not ideal for local-first. However, we could store evidence of past OAuth verifications.

---

## 5. Web of Trust Models

### PGP Web of Trust: What Worked and What Failed

**The model:** Users sign each other's public keys after in-person identity verification. Trust propagates: if I trust Alice and Alice signed Bob's key, I can trust Bob's key (at a configurable depth).

**What worked:**
- Strong cryptographic foundation
- Decentralized — no certificate authority
- In-person key signing parties created genuine community trust

**What failed:**
- **UX was terrible.** Users had to understand public key cryptography, manage keyrings, make explicit trust decisions. Adoption never went mainstream.
- **The "ultimate responsibility" problem.** Users must decide trust roots from scratch — most people can't or won't do this.
- **Key management.** Keys get lost, compromised, or forgotten. Revocation is "imperfect, not fully understood, and not as widely implemented as it could be" (OpenPGP spec authors' own assessment).
- **sks-keyservers.net shutdown (2021).** The decentralized keyserver network collapsed — poisoned keys, spam, abuse.
- **No temporal dimension.** A key signed in 2010 might belong to someone who's changed names, died, or had their key compromised. Signatures didn't expire by default.
- **Privacy.** The web of trust is public — everyone can see who signed whose key, revealing social connections.

**Lessons for our model:**
1. Don't make users think about cryptography. Ever. It should be invisible.
2. Trust decisions must have temporal bounds — signatures should decay or require refresh.
3. Privacy of the trust graph matters — who you vouch for reveals social connections.
4. Key management must be transparent to the user (Keybase's device-based model was the right direction).
5. The social graph IS the trust infrastructure — the math just makes it verifiable.

### Modern Takes: Keyoxide and keys.openpgp.org

**Keyoxide:** Already covered above. The key innovation: proofs in the key itself, not in a central database.

**keys.openpgp.org:** Modern keyserver that only distributes keys after email verification. Addresses the spam/abuse problems of old keyservers. But centralized (single operator).

### Social Vouching Patterns

**Coordinape (Web3 contributor circles):**
- Circle members vote to invite new contributors
- Vouches require ETH address and name
- Configurable threshold: 1 vouch to unanimous required
- Consequence: voucher's reputation is at stake

**Stamp Network:**
- Users verify each other through "stamps" (attestations)
- Stamps are revocable
- When you collect enough stamps, a "passport" is emitted based on community-defined thresholds
- Trust graph emerges from stamp relationships

**Ethos Network:**
- On-chain reputation scores from reviews, vouches, and "slashes" (negative attestations)
- Invite-only with shared responsibility — your invitees' behavior affects you
- XP rewards for honest, active participation

**For our model:** The vouching pattern maps to: Person A claims "Person B controls Account X" — a third-party assertion with the asserter's identity as evidence. The interesting wrinkle is **stake**: if the voucher's reputation is at risk, the assertion is more trustworthy.

### Trust Propagation Algorithms

**EigenTrust:**
- Peer-to-peer reputation algorithm
- Your reputation = weighted sum of others' opinions of you, weighted by their reputation
- Converges to principal eigenvector of the trust matrix (same math as PageRank)
- Starts with "seed peers" (pre-trusted nodes) to bootstrap
- **Key insight:** Trust is transitive but attenuated. You trust your friends' opinions, but less than your own.

**TrustGraph protocol:**
- Open protocol for decentralized reputation
- Agent-centric: each person has their own view of the trust graph
- **TrustAtom format:**
  ```
  {
    source: <hash of rater's public key>,
    target: <hash or URL of entity being rated>,
    value: <numeric, 0 to 1>,
    content: <description/tags>,
    timestamp: <datetime>
  }
  ```
- Trust cascades: trusting someone incorporates their TrustGraph into your view
- Built on Holochain (peer-to-peer, agent-centric framework)

**For our model:** The TrustAtom format is remarkably similar to what we need for claims. A claim is essentially: source (who asserts), target (what account), value (confidence), content (method/evidence), timestamp. The agent-centric view is exactly right for local-first — YOUR trust graph, on YOUR machine.

**KGTrust (Knowledge-Enhanced):**
- Combines knowledge graphs with graph neural networks
- Uses semantic knowledge from behavior + external data
- Captures heterogeneous trust relationships
- **For our model:** Long-term, we could compute trust scores from graph structure (how many independent paths confirm a person-account link?).

---

## 6. AI-Era Challenges

### Deepfake Detection: Current State

**The uncomfortable reality (2025):**
- Fewer than half of tested deepfake detectors achieve AUC > 60%
- Basic image processing (JPEG compression) degrades detector performance significantly
- Detectors trained on lab datasets fail against real-world deepfakes
- Adversarial perturbations can defeat most detectors
- **Bottom line:** Deepfake detection is not reliable enough to be a verification method. It's a cat-and-mouse game where the cats are winning.

**Implications for identity:**
- Video/selfie verification is becoming less trustworthy
- "Proof of life" (live video challenges) still works but for how long?
- BrightID's decision to use human recognition over AI recognition is looking prescient

### Account Takeover Patterns

**Scale of the problem (2025):**
- 83% of organizations experienced at least one ATO incident
- $17 billion in projected losses
- Primary vectors: credential stuffing, phishing, infostealer malware

**Detection signals (relevant for our confidence model):**
- New/unfamiliar device login
- Impossible travel (login from two distant locations within impossible timeframe)
- Behavioral changes (typing patterns, navigation, access times)
- Sudden changes to security settings (email, phone, 2FA)
- Multiple failed login attempts followed by success

**For our model:** Account takeover means a previously valid person→account claim may no longer be true. This is why **temporal confidence decay** matters. Evidence of ATO (public suspension, security incident reports) should reduce confidence.

### AI-Generated Personas

**Current prevalence:**
- ~0.02-0.04% of active Twitter/X accounts use GAN-generated profile photos (~10K daily active synthetic accounts)
- Used for: scams, spam, coordinated manipulation, astroturfing
- Detection: GAN-generated faces have consistent eye placement patterns (detectable), but newer generators may not

**The deeper problem:**
- AI can generate consistent personas across platforms — matching bios, posting history, interaction patterns
- LLMs can maintain conversational consistency that passes casual inspection
- The cost of creating convincing fake identities is dropping exponentially
- Traditional heuristics (account age, post frequency, follower ratios) are being gamed

**For our model:** This reinforces that **behavioral signals alone are insufficient**. Cryptographic proofs (key-based), social graph structure (BrightID-style), and bidirectional verification (rel-me) are more AI-resistant than behavioral heuristics.

### Content Provenance (C2PA)

**What it is:** Open standard for cryptographically signing content with metadata about its creation and editing history. "Nutrition labels for digital media."

**How it works:**
- Content Credentials are cryptographically bound to media files (images, video, audio, documents)
- Record: who created it, what tools were used, what edits were made, whether AI was involved
- Use X.509 certificates, CBOR, JUMBF for tamper-evident signatures
- Backed by Adobe, BBC, Google, Meta, Microsoft, OpenAI, Sony
- Spec version 2.3 current

**For our model:** C2PA is relevant for verifying evidence attached to claims. If someone submits a screenshot as proof of account ownership, C2PA credentials on the screenshot could verify it wasn't fabricated. Long-term play, but worth tracking.

### What Defenses Are AI-Resistant?

Ranked by resistance to AI-powered attacks:

1. **Cryptographic proofs** — AI can't forge private keys. Still the gold standard.
2. **Bidirectional verification** — Requires write access to two independent systems simultaneously. Hard to fake at scale.
3. **Social graph structure** — Creating a convincing social graph with real, verified humans vouching for you requires real social connections.
4. **Economic cost** — On-chain identity (Farcaster, ENS) costs real money. Raises the cost of Sybil attacks.
5. **Temporal consistency** — Maintaining a consistent identity over years with real activity is expensive for attackers.
6. **Behavioral biometrics** — Typing patterns, navigation habits. Being actively researched but not yet reliable.
7. **Visual/audio verification** — Rapidly losing effectiveness against deepfakes.

---

## 7. Practical Patterns for a Local Knowledge Graph

### What a Local-First App Can Actually Verify

**Can do locally (no server needed):**
- Check rel-me bidirectional links (HTTP fetch both URLs, check for `rel="me"`)
- Verify DNS TXT records (DNS lookup)
- Verify Keyoxide/Ariadne proofs (fetch OpenPGP key, check notations, verify proof URLs)
- Check if social profile bios mention each other (HTTP fetch + text search)
- Compare handles across platforms (string matching)
- Verify cryptographic signatures on locally-stored proofs
- Check C2PA content credentials on media files
- Resolve Bluesky DIDs (fetch from plc.directory)
- Read ENS text records (Ethereum RPC call)

**Can do with user interaction:**
- OAuth verification (needs user to authenticate, but we can store the evidence)
- Request user to post a verification message on a platform ("post this code to your Twitter")
- QR code exchange for in-person verification
- Safety number comparison (Signal, Matrix)

**Cannot do locally:**
- Biometric verification (needs hardware like Worldcoin Orb)
- Platform API calls requiring platform-specific OAuth tokens (but we CAN store results from adapters that do have access)
- Real-time account status checking without API access

### Strongest Signals with Least Friction

| Method | Friction | Confidence | Local-First? |
|--------|----------|-----------|--------------|
| Same handle check | None (automated) | 0.30-0.50 | Yes |
| Bio cross-reference | None (automated) | 0.50-0.65 | Yes |
| rel-me check | None (automated, if links exist) | 0.85-0.90 | Yes |
| DNS proof check | None (automated) | 0.85-0.90 | Yes |
| Self-claimed by user | Low (user types it) | 0.65-0.75 | Yes |
| OAuth proof | Medium (redirect flow) | 0.80-0.85 | Partial |
| Post verification code | Medium (user posts publicly) | 0.85-0.90 | Yes (verification is) |
| In-person QR exchange | High (physical meeting) | 0.90-0.95 | Yes |

**Recommendation:** Start with automated checks (rel-me, bio, same handle), layer user-initiated verification on top. The Gitcoin Passport model of combining multiple stamps is the right UX — "you've verified 3 of 7 possible methods, confidence: 0.82."

### Confidence Decay Model

Verification freshness matters. A rel-me link verified today is more trustworthy than one verified two years ago (links break, accounts get hacked, domains lapse).

**Proposed decay function:**

```
effective_confidence = base_confidence × decay_factor(age)

where decay_factor(age) = max(min_floor, e^(-λ × age_in_days))
```

**Suggested parameters by method:**

| Method | λ (decay rate) | Min Floor | Half-Life | Rationale |
|--------|---------------|-----------|-----------|-----------|
| Cryptographic proof | 0.0001 | 0.70 | ~19 years | Keys rarely compromised if well-managed |
| In-person verification | 0.0003 | 0.50 | ~6 years | People don't change that fast |
| rel-me / DNS proof | 0.001 | 0.40 | ~2 years | Links break, domains lapse |
| OAuth proof | 0.005 | 0.30 | ~5 months | Sessions and tokens expire |
| Bio cross-reference | 0.003 | 0.20 | ~8 months | Bios change frequently |
| Same handle heuristic | 0.0005 | 0.20 | ~4 years | Handles are fairly stable |
| Self-claimed | 0.0002 | 0.50 | ~10 years | User's own assertion, stable unless revoked |
| AI inference | 0.01 | 0.10 | ~2 months | Models improve, context changes |

**Re-verification triggers (reset decay):**
- User explicitly re-confirms a claim
- Automated check re-verifies (e.g., rel-me still valid)
- New evidence for the same claim arrives from a different source

**Confidence collapse triggers (immediate drop):**
- Account reported as compromised/hacked
- Account suspended or deleted by platform
- Contradictory evidence (someone else claims the same account with higher confidence)
- User explicitly revokes a claim

### What Evidence to Store

For each claim (Person → claims → Account), store:

```yaml
claim:
  # The assertion itself
  person_id: "person:joe"
  account_id: "account:twitter:jcontini"
  
  # Confidence
  confidence: 0.87          # Computed from method + age + corroboration
  base_confidence: 0.90     # Confidence at time of verification
  
  # Method and evidence
  method: "rel_me"           # How this was verified
  evidence:
    - type: "bidirectional_link"
      source_url: "https://joe.com"
      target_url: "https://twitter.com/jcontini"
      source_contains_target: true
      target_contains_source: true
      checked_at: "2026-02-09T14:30:00Z"
    - type: "same_handle"
      platforms: ["twitter", "github", "mastodon"]
      handle: "jcontini"
      checked_at: "2026-02-09T14:30:00Z"
  
  # Provenance
  asserted_by: "self"        # Who made this claim (self, system, person:alice)
  asserted_at: "2026-02-09T14:30:00Z"
  verified_at: "2026-02-09T14:30:00Z"  # Last verification time
  
  # For decay calculation
  verification_count: 3      # How many times independently verified
  last_checked: "2026-02-09T14:30:00Z"
  
  # Corroboration (other evidence pointing the same way)
  corroborating_claims:
    - method: "same_handle"
      confidence: 0.45
    - method: "bio_extraction"  
      confidence: 0.55
```

**Types of evidence to capture:**
- **URL evidence:** Source URL, target URL, content at time of check, HTTP headers
- **Cryptographic evidence:** Signed messages, key fingerprints, signature timestamps
- **Screenshot evidence:** Image + timestamp + C2PA credentials if available (note: screenshots are weak evidence due to easy fabrication)
- **Social graph evidence:** Who vouched, their trust level, vouching timestamp
- **Behavioral evidence:** Account age, posting frequency, follower count at time of check
- **Platform evidence:** Verification badge status, API-confirmed account details

---

## 8. Recommendations for the Claims Relationship

### Design Decisions

**1. `claims` should be a first-class relationship type (not a `references` role).**

The epistemic provenance (confidence, method, evidence, decay) is core to this relationship — it's not metadata on a generic edge. Every query about person↔account links will want to filter/sort by confidence. This is important enough to be its own type.

**2. Support multiple evidence sources per claim.**

A single person→account link might have evidence from rel-me, same handle, AND self-claim. These should stack, not replace each other. Combined confidence > any individual method.

**3. Claims are event-sourced.**

Each verification event is a timestamped record. Current confidence is computed from the full history. This gives you an audit trail and enables re-computation if decay parameters change.

**4. Claims are directional: Person → claims → Account.**

But also allow: Person A → asserts → (Person B → claims → Account X). Third-party assertions are weaker but still valuable data.

### Proposed Claims Relationship Schema

```yaml
id: claims
name: Claims
inverse_name: Claimed by
description: Assertion that a person controls or is associated with an account
is_relationship: true
from_type: person
to_type: account
temporal_nature: snapshot  # Event-sourced: multiple verifications over time

properties:
  # Core confidence
  confidence:
    type: number
    min: 0
    max: 1
    description: |
      Current effective confidence in this claim, computed from:
      base_confidence × decay_factor × corroboration_boost
      
      0.90-1.0  = Cryptographically proven or in-person verified
      0.75-0.90 = Strong evidence (rel-me, OAuth, DNS proof)
      0.50-0.75 = Moderate evidence (self-claimed, bio reference)
      0.25-0.50 = Weak evidence (same handle, AI inference)
      0.00-0.25 = Speculative (third-party rumor, very old evidence)

  # How we know
  method:
    type: string
    description: |
      Primary verification method. One of:
      - cryptographic_proof: Signed statement linking identities
      - in_person: Verified face-to-face (key signing, QR exchange)
      - rel_me: Bidirectional link verification
      - dns_proof: DNS TXT record verification
      - oauth: OAuth/OIDC authentication proof
      - platform_api: Confirmed via platform API
      - post_verification: User posted a verification code
      - social_graph: BrightID or similar social verification
      - self_claimed: User asserted this directly
      - bio_extraction: Found link in profile bio
      - same_handle: Same username across platforms
      - third_party: Someone else asserted this
      - inferred: System heuristic or AI extraction

  # Provenance
  asserted_by:
    type: string
    description: |
      Who made this claim. One of:
      - "self" (the person themselves)
      - "system" (automated verification)
      - person:<id> (a third party)
  
  # Evidence (stored as JSON array for flexibility)
  evidence:
    type: array
    description: Evidence supporting this claim
    items:
      type: object
      properties:
        type:
          type: string
          description: Evidence type (url_check, signature, screenshot, voucher, api_response)
        data:
          type: object
          description: Type-specific evidence data
        captured_at:
          type: datetime
          description: When this evidence was captured

  # For re-verification
  verified_at:
    type: datetime
    description: When this claim was last verified
  
  verification_count:
    type: integer
    description: How many times independently verified
```

### Key Standards Worth Adopting

| Standard | What to Take | How |
|----------|-------------|-----|
| **W3C Verifiable Credentials** | Claim structure (issuer, subject, evidence, validity) | Inform our schema, not implement the full stack |
| **IndieWeb rel-me** | Bidirectional link verification | Implement as a verification method |
| **Ariadne/Keyoxide** | Proofs embedded in keys, local verification | Reference for how to store/check proofs |
| **Bluesky DID:PLC** | DID resolution, handle-as-domain | Resolve Bluesky identities natively |
| **TrustGraph TrustAtom** | Agent-centric trust, signed claims with value + content + timestamp | Our claims model IS this pattern |
| **Gitcoin Passport** | Multiple stamps composing into a score | UX model for showing combined confidence |
| **EigenTrust** | Trust propagation through graph | Long-term: compute trust from graph structure |
| **C2PA** | Content provenance on evidence media | Verify evidence authenticity |

### Interesting Patterns We Might Not Have Thought Of

**1. Negative claims (distrust signals).**
Not just "I believe person X controls account Y" but also "I believe person X does NOT control account Y." Contradictory evidence is as valuable as confirming evidence. The TrustGraph model supports negative values (-1 to +1). Account takeover = negative claim against the old person→account link.

**2. Claim inheritance through social graph.**
If I verify that Alice is @alice on Twitter, and Alice tells me Bob is @bob on GitHub, that's a transitive claim with attenuated confidence. The graph should support this: claim confidence flows through trust edges, decaying at each hop. (EigenTrust math applies here.)

**3. Verification challenges (Keybase-style).**
Instead of just checking existing links, we could generate a unique challenge string and ask the user to post it on their claimed account. This is how Keybase proofs worked — post a signed message. Evidence: the challenge string + the platform post containing it. Higher confidence than passive checking.

**4. "Proof of continued control" as a background process.**
Periodically re-check rel-me links, DNS records, bio mentions. If a previously verified link is gone, flag it (don't delete the claim, but reduce confidence and mark as "unverifiable since [date]").

**5. The Mastodon pattern: domain-as-identity.**
If someone uses their own domain as their Mastodon handle or Bluesky handle, that domain IS their identity. Every account linked from that domain gets higher confidence automatically. This is the IndieWeb vision: your domain is your identity hub.

**6. Collective identity resolution.**
Multiple adapters might independently discover the same person→account link (WhatsApp adapter sees phone number matching a contact, Reddit adapter sees same handle, YouTube adapter sees same display name). Each is weak evidence individually. The graph should automatically combine them.

**7. Semantic types of "claims."**
Not all person→account relationships are the same:
- **"controls"** — this person has login access to this account (strongest)
- **"represents"** — this account is a public identity of this person (brand/org accounts)
- **"operated_by"** — multiple people operate this account (team accounts)
- **"formerly_controlled"** — historical ownership (account sold, transferred)

These could be roles on the claims relationship, similar to `references` roles.

**8. Privacy layers on claims.**
Some claims should be private (I know my friend's Reddit handle but they don't want it linked publicly). Local-first makes this easier — the claim lives on YOUR machine — but if we ever sync or share graphs, privacy levels matter.

---

## 9. Key References

### Standards and Specifications
- [W3C Verifiable Credentials 2.0](https://www.w3.org/TR/vc-data-model/) — Now a W3C Recommendation (May 2025)
- [W3C Decentralized Identifiers v1.1](https://w3.org/TR/did-1.1) — Working Draft (Jan 2026)
- [W3C Digital Credentials API](https://www.w3.org/blog/2025/w3c-digital-credentials-api-publication/) — Browser integration
- [Ariadne Identity Specification](https://ariadne.id/) — Decentralized identity proofs
- [C2PA Content Credentials](https://c2pa.org/) — Content provenance standard (v2.3)
- [IndieWeb rel-me](https://indieweb.org/rel-me) — Bidirectional link verification
- [AT Protocol Identity](https://docs.bsky.app/docs/advanced-guides/resolving-identities) — Bluesky identity resolution
- [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0-final.html) — OAuth identity layer

### Protocols and Implementations
- [Keyoxide](https://docs.keyoxide.org/) — Decentralized identity verification
- [Keybase Proofs](https://github.com/keybase/proofs) — Cross-platform proof system (archived)
- [Keybase Proof Verification Language](https://keybase.io/docs/client/pvl_spec) — Declarative proof validation
- [TrustGraph](https://trustgraph.net/) — Decentralized reputation protocol
- [EigenTrust (OpenRank)](https://docs.openrank.com/reputation-algorithms/eigentrust) — Trust propagation algorithm
- [Stamp Network Web of Trust](https://docs.stamp.network/use-cases/web-of-trust-for-communities) — Stamp-based verification

### Proof of Personhood
- [Worldcoin/World ID](https://docs.worldcoin.org/world-id) — Biometric proof of personhood
- [BrightID](https://brightid.gitbook.io/brightid) — Social graph verification
- [Gitcoin Passport](https://support.passport.xyz/passport-knowledge-base) — Multi-stamp identity scoring

### Identity Systems
- [Farcaster Protocol](https://github.com/farcasterxyz/protocol/blob/main/docs/OVERVIEW.md) — On-chain social identity
- [ENS Documentation](https://docs.ens.domains/) — Ethereum Name Service
- [Mastodon Verification](https://joinmastodon.org/verification) — rel-me in practice
- [Vouchsafe](https://getvouchsafe.org/) — Offline-first self-verifying identity
- [local-first/auth](https://github.com/local-first-web/auth) — Decentralized auth for local-first apps

### Research
- [Temporal Factors in Virtual Identity Trustworthiness](https://arrow.tudublin.ie/cgi/viewcontent.cgi?article=1368&context=scschcomcon)
- [AI-Generated Fake Social Media Profiles](https://tsjournal.org/index.php/jots/article/download/197/83)
- [Account Takeover in the Era of Agentic AI (Sift Q3 2025)](https://sift.com/index-reports-account-takeover-fraud-q3-2025/)
- [PGP Web of Trust Failures](https://soatok.blog/2024/11/15/what-to-use-instead-of-pgp/)
- [Moving from Keybase to Keyoxide](https://eyalkalderon.com/blog/moving-from-keybase-to-keyoxide/)

---

*This research informs the `claims` relationship design in AgentOS. The model is local-first, epistemic (confidence + evidence, not binary truth), and designed to compose multiple weak signals into strong identity assertions.*
