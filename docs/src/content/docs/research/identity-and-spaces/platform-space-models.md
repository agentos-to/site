---
title: How Major Platforms Model Their Own Spaces
description: Full synthesis of how major platforms model the containers where content lives and interaction happens, with a cross-platform comparison table.
---

Here's the full synthesis. I'll go platform by platform, then close with a cross-platform comparison table showing the patterns.

---

## 1. YouTube

**Hierarchy:** Google Account → Brand Account (optional) → Channel → Playlist / Video

**What is a channel?** A channel is the fundamental "space" — it's a content hub with its own identity (name, handle, icon, banner, description), its own subscriber base, and its own content library. In the API, a `channel` resource contains `snippet` (metadata), `contentDetails` (playlist IDs for uploads, likes), `brandingSettings`, `status`, and `statistics`.

**Ownership:** A Google Account owns channels. One Google Account can own multiple channels. A **Brand Account** is a shell/container that decouples channel ownership from a personal Google identity, enabling multiple Google Accounts to manage the same channel with different permission levels.

**Content types:** Videos, Shorts, Live streams, Community posts, Playlists, Stories (deprecated). Channels also have Sections (curated groupings on the channel page).

**Subscription model:** **Subscribe** (free, one-way follow — you see their content in your feed). Separately, **Channel Memberships** (paid recurring subscription for perks — badges, emotes, exclusive content). These are two completely different relationships.

**Key insight:** Channel ≈ identity + space. A YouTube channel IS both the creator identity and the content container. There's no separation — the "who" and the "where" are fused.

---

## 2. Discord

**Hierarchy:** Guild (Server) → Category → Channel → Thread

**Terminology split:** The API calls it a **Guild**. The UI calls it a **Server**. Everywhere in the developer docs it's `guild_id`, `APIGuild`, etc. Users never see the word "guild."

**What is a Guild/Server?** A container with its own identity (name, icon, banner), a role/permission system, and a hierarchical channel structure. The `APIGuild` object contains `owner_id`, `roles[]`, `verification_level`, `default_message_notifications`, `premium_tier` (boost level), and more.

**Channel types (via `type` field):**
- `GUILD_TEXT` (0) — standard text channel
- `GUILD_VOICE` (2) — voice/video channel
- `GUILD_CATEGORY` (4) — organizational container for channels
- `GUILD_ANNOUNCEMENT` (5) — news channel
- `GUILD_STAGE_VOICE` (13) — stage events
- `GUILD_FORUM` (15) — forum-style (thread-first)
- `PUBLIC_THREAD` / `PRIVATE_THREAD` / `ANNOUNCEMENT_THREAD`

**Categories** are channels with `type=4`. Child channels reference their parent via `parent_id`. A category can hold up to 50 children. Threads also use `parent_id` to reference the text channel they were created in.

**Ownership:** One user is the `owner_id`. Roles provide granular permission delegation. `permission_overwrites` on each channel allow per-role or per-user permission overrides.

**Membership model:** **Join** (you become a "member" of the server). Joining is explicit — you use an invite link or Discovery. No concept of "follow" or "subscribe" at the server level. Within a server, you **opt into** threads.

**Key insight:** Discord has the deepest nesting of any consumer platform — 4 levels (Server → Category → Channel → Thread). The "Guild" abstraction is a full isolated world with its own permission system, roles, and culture.

---

## 3. Reddit

**Hierarchy:** Reddit (platform) → Subreddit → Post → Comment thread. Sub-spaces: Flairs, Wiki, Collections, Widgets.

**What is a subreddit?** Reddit's official language: "a community or forum within Reddit where users can share content and discussion around specific topics." In the data model, a Subreddit is a first-class `Thing` object (same abstraction level as links, comments, accounts) persisted in their ThingDB/PostgreSQL system. The `Subreddit` class has: `id`, `name` (r/name), `title`, `description`, `numberOfSubscribers`, `numberOfActiveUsers`, `language`, `nsfw`, settings, and flair/wiki management methods.

**Sub-spaces within a subreddit:**
- **Post Flairs** — categorical tags that organize posts (filterable). Controlled by mods.
- **User Flairs** — identity tags within that community.
- **Wiki** — collaborative documentation space per subreddit. Has its own contributor/ban lists.
- **Collections** — curated post groupings.
- **Widgets** — sidebar content (rules, related subs, etc.)

**Ownership:** Created by a user who becomes the first **moderator**. Moderators manage the space (rules, flairs, bans, wiki, automod). There's no single "owner" in the API — it's a moderation team. Reddit admins (employees) sit above moderators.

**Content types:** Text posts, Link posts, Image/Video posts, Polls, Comments (threaded), Wiki pages, Live threads (deprecated).

**Membership model:** **Join** (Reddit's current terminology, formerly "subscribe"). Joining is lightweight — it affects your home feed. You don't need to join to read, post, or comment in most subreddits. Some subreddits are private (require approval) or restricted (anyone can view, only approved users can post).

**Key insight:** Subreddits are community-owned spaces with no single owner identity. The space IS the identity (r/programming, r/rust), not a person. This is the opposite of YouTube where the channel IS a person.

---

## 4. Twitch

**Hierarchy:** User/Broadcaster → Channel → Stream (live) → Chat / VODs / Clips

**What is a channel?** In Twitch, a channel is **1:1 with a user account**. Every Twitch user has a channel at `twitch.tv/username`. The channel is the "page" where streams happen, VODs are stored, and the community gathers. There's no way to create multiple channels per account (unlike YouTube).

**In the API:** Channel endpoints operate on `broadcaster_id` — which IS the user ID. `Get Channel Information` takes a broadcaster user ID and returns: `broadcaster_id`, `broadcaster_name`, `game_name`, `title`, `tags`, `content_classification_labels`, `is_branded_content`. The channel and user are the same entity from different angles.

**Content types:** Live streams, VODs (recorded streams), Clips (community-created highlights), Chat (live), Channel Points, Raids, Polls, Predictions, Emotes.

**Ownership:** The broadcaster (user) IS the channel owner. Channel Editors can be granted limited management access. Moderators manage chat.

**Membership model:** Two tiers:
- **Follow** (free, one-way — you get notified when they go live)
- **Subscribe** (paid, $4.99/$9.99/$24.99 tiers — emotes, badges, ad-free viewing). Also: Gifted Subs, Prime Gaming subs.

**Key insight:** Twitch has the simplest space model — User = Channel, period. Even simpler than YouTube because you can't have multiple channels. The "space" only comes alive when the broadcaster is live. It's fundamentally a **temporal** space — the live stream IS the gathering, not the channel page.

---

## 5. Slack / Microsoft Teams

### Slack
**Hierarchy:** Enterprise Grid Organization → Workspace → Channel → Thread

**What is a Workspace?** A self-contained environment with its own member directory, channels, conversations, and files. In Enterprise Grid, an Organization contains multiple Workspaces. Users maintain the same identity across workspaces (Enterprise user IDs starting with `U` or `W`).

**What is a Channel?** Slack's Conversations API unifies all channel-like things under one model: public channels (`C` prefix), private channels (`G` prefix), DMs (`D` prefix), group DMs, and multi-workspace shared channels. All are "conversations."

**Threads:** A thread is a reply chain under a parent message. `thread_ts` (timestamp of parent) links replies to their parent. Threads can optionally be "sent to channel" to surface in the main flow.

**Ownership:** Workspace Owners/Admins. Channels can have specific posting permissions. Enterprise Org Admins sit above workspace-level admins.

**Membership model:** **Invited/Added** (someone adds you to a workspace) or **Join** (for public channels within a workspace). You don't "follow" or "subscribe" — you're either in or you're not. Leaving a channel is explicit.

### Microsoft Teams
**Hierarchy:** Organization (M365 Tenant) → Team → Channel → Thread (reply chain)

**What is a Team?** A Team maps to a Microsoft 365 Group. It's a collaboration space with its own membership, channels, and shared resources (files, OneNote, Planner). In the Graph API: `team` resource under `/groups/{id}/team`.

**What is a Channel?** Channels within a Team contain messages (`chatMessage` resources). Messages can be root-level or threaded via `replyToId`. Channels can be Standard, Private, or Shared (cross-team).

**Membership model:** **Added** to a Team (by owner/admin or self-join if allowed). Channels within a team are accessible to all team members (except Private channels which have their own membership).

**Key insight:** Enterprise tools don't have "follow" or "subscribe" — they have **membership**. You're either in the space or not. This reflects the enterprise model where access = authorization, not interest.

---

## 6. GitHub

**Hierarchy:** User/Organization → Repository → Issues / Discussions / PRs / Code

**Account types:**
- **Personal Account** — owns repos directly. Two permission levels: owner + collaborators.
- **Organization** — shared account for teams. Owns repos with granular role-based access. Multiple people can be org owners. Contains **Teams** (nested groups with cascading permissions).

**Is a repo a "space"?** Yes — a repository is the primary collaboration space. It has its own Issues, Discussions, PRs, Wiki, Actions, Settings, and access control. A repo has a **name**, **description**, **visibility** (public/private), and its own permission model.

**Discussions** function as a community forum scoped to a repo (or org-level). Categories within Discussions add sub-structure.

**Issues** now support **Sub-issues** — creating a hierarchy within the issue tracker.

**Ownership:** Repos are owned by a personal account OR an organization. Organization repos have granular roles: Admin, Maintain, Write, Triage, Read. Teams can be granted repo-level access.

**Membership model:**
- **Watch** a repo (notifications about activity — like subscribe)
- **Star** a repo (bookmark / signal interest — like favorite)
- **Fork** a repo (create your own copy — unique to code)
- **Member** of an org/team (access control)

**Key insight:** GitHub has a dual model — repos are both content containers AND collaboration spaces. "Watch" is the closest thing to subscribe, but there's no "join" because public repos are open by default. The access model is fundamentally about **permissions on code**, not community membership.

---

## 7. Mastodon / Fediverse

**Hierarchy:** Instance (Server) → User (Actor) → Posts (Notes). No sub-spaces.

**What is an Instance?** An independently operated server running Mastodon (or compatible software). Each instance has its own domain (e.g., `mastodon.social`), its own admin, its own rules, its own **local timeline** (posts from users on that instance). Instances federate with each other via ActivityPub.

**Actor Model:** Every user is an ActivityPub **Actor** with:
- An **inbox** (receives messages from the federation)
- An **outbox** (sends messages to the federation)
- A globally unique ID: `@user@instance.domain`

**Content types:** Notes (statuses/toots), Questions (polls), Boosts (reshares), Favourites (likes). The protocol can also handle Articles, Pages, Images, Audio, Video, Events.

**Federation activities:** Create, Delete, Like, Announce (boost), Update, Undo, Flag (report). These are the verbs that flow between instances.

**Ownership:** Instance admins own/run the server. Users own their account but are subject to instance rules. There's no "space" below the instance level — no groups, no channels, no subreddits (by default, though some fediverse software adds groups).

**Membership model:** **Follow** (user-to-user, cross-instance). No concept of "joining" an instance community — you **register an account** on an instance, which is closer to citizenship than membership. Following is the only subscription primitive. Hashtags serve as ad-hoc topic spaces but aren't owned or moderated.

**Key insight:** Mastodon's "space" is the **instance itself** — but it's a very thin space. There's no hierarchy below it. The real innovation is that spaces are **federated** — your identity on Instance A can interact with people on Instance B. The tradeoff: extremely flat structure, no sub-communities within an instance (unlike every other platform).

---

## Cross-Platform Comparison Table

| Dimension | YouTube | Discord | Reddit | Twitch | Slack | Teams | GitHub | Mastodon |
|---|---|---|---|---|---|---|---|---|
| **Top-level space** | Channel | Guild/Server | Subreddit | Channel | Workspace | Team | Org/User | Instance |
| **Depth of nesting** | 2 (Channel → Playlist) | 4 (Server → Category → Channel → Thread) | 3 (Sub → Post → Comment) | 1 (Channel → Stream) | 3 (Workspace → Channel → Thread) | 3 (Team → Channel → Thread) | 3 (Org → Repo → Issue/Discussion) | 1 (Instance → User) |
| **Space = Identity?** | Yes (channel IS the creator) | No (server is a place) | No (subreddit is a topic) | Yes (channel IS the user) | No (workspace is a team) | No (team is a group) | Partial (user/org owns repos) | Partial (instance is a community) |
| **Multi-space per account** | Yes (multiple channels) | Yes (create many servers) | Yes (create many subs) | No (1 channel per user) | Yes (many workspaces) | Yes (many teams) | Yes (many repos) | No (1 account per instance*) |
| **Ownership model** | Single owner (Google Account) | Single owner + roles | Moderator team (no single owner) | Broadcaster (= user) | Workspace Owner(s) | Team Owner(s) | Account owner or Org owners | Instance admin |
| **Join terminology** | Subscribe | Join (via invite) | Join (was "subscribe") | Follow | Invited / Join | Added / Join | Watch / Star / Member | Register / Follow |
| **Free follow** | Subscribe | N/A (must join server) | Join | Follow | N/A | N/A | Watch / Star | Follow |
| **Paid tier** | Channel Membership | Server Boost | Reddit Premium / Awards | Subscribe ($4.99+) | N/A (enterprise pricing) | N/A (enterprise pricing) | Sponsors | N/A |
| **Primary content** | Video | Messages (text + voice) | Posts + Comments | Live streams + Chat | Messages | Messages | Code + Issues + Discussions | Notes (statuses) |
| **API term for space** | `channel` | `guild` | `subreddit` (Thing) | `broadcaster`/`channel` | `conversation`/`team` | `team`/`channel` | `repository`/`organization` | `actor` / instance |
| **Permission granularity** | Low (owner + managers) | High (roles + per-channel overrides) | Medium (mod tools) | Low (broadcaster + mods + editors) | High (workspace + channel level) | High (org + team + channel) | High (org + team + repo roles) | Low (instance rules + blocks) |

## Key Patterns That Emerge

**1. Space-as-Identity vs. Space-as-Place.** YouTube and Twitch fuse the space with the person — "the channel IS the creator." Discord, Reddit, Slack, and Teams treat spaces as **places** that exist independently of any single person. GitHub and Mastodon sit in between.

**2. Depth correlates with interaction complexity.** Discord (4 levels) and Slack (3 levels) need deep nesting because they host ongoing, real-time, multi-topic conversations. YouTube and Twitch (1-2 levels) are shallow because they're broadcast-oriented — one creator, many consumers.

**3. "Subscribe" vs "Join" vs "Follow" are not interchangeable.** "Follow" and "Subscribe" are **one-way, low-commitment** signals of interest (you can leave silently). "Join" and "Member" are **two-way, identity-in-space** relationships (the space knows you're there, you appear in member lists, you can be kicked). Enterprise tools only have "Join" — there is no passive consumption tier.

**4. The API name often diverges from the UI name.** Discord: guild vs. server. Reddit: subreddit vs. community. Slack: conversation vs. channel. This is worth noting for data modeling — the internal model is often more precise than the marketing term.

**5. Content moderation tracks ownership model.** Single-owner spaces (YouTube, Twitch) have simple mod: the owner delegates. Community-owned spaces (Reddit, Discord) need richer permission systems because governance is distributed. Federated spaces (Mastodon) push moderation to instance admins with no platform-level override.

**6. No platform has groups-within-groups natively.** Discord has Categories but they're purely organizational — no permissions, no membership of their own. Reddit has no sub-subreddits. Slack has no sub-channels. The deepest nesting anyone achieves is Discord's 4-level hierarchy, and even that is flat compared to file system trees or org charts.
