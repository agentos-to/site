---
title: Auth resolution
description: How the engine picks one credential when multiple sources offer candidates for the same issuer. Timestamp-based, no fixed priority — the freshest cookie wins.
---

This page is the algorithm behind ["freshest wins"](/architecture/security/#auth-resolution--freshest-wins). It assumes you've read [Security](/architecture/security/) and want the actual decision procedure: who's asked, what's compared, who breaks ties, and what happens when the resolved cookie turns out to be stale.

## The problem

A skill says `client.get("https://github.com/...")`. The engine needs a cookie header. There could be a credential row in the store from when you set up the [GitHub skill](/skills/reference/dev/github/) last week, a fresh cookie jar in Chrome from a tab you opened five minutes ago, and an in-memory session from another skill call earlier this hour. Three sources, three timestamps, one issuer. "Pick the one the user configured" doesn't work — there is no configuration step, by design (see [Why this shape](#why-this-shape)). Picking the *first* one to answer doesn't work either: the store always answers fastest, but its data is usually the oldest. The engine needs a deterministic rule that doesn't require the user to think about provider priority.

## Three sources

`resolve_cookies()` (`crates/auth/src/resolve.rs:93`) gathers candidates from three places, in order. Each candidate is scored independently; the scores compete at the end.

| # | Source | Data | Freshness signal |
|---|---|---|---|
| 1 | In-memory cache (`SessionCache`) | Resolved sessions from the current engine lifetime, keyed by `(domain, identifier)` | `newest_cookie_at` carried over from the original extraction, plus per-cookie writeback timestamps stamped by `apply_cookie_delta` (`store.rs`) |
| 2 | Credential store (SQLite) | Encrypted rows in `~/.agentos/data/agentos.db`. `value` blob holds a structured `cookies: [Cookie, …]` array + `cookie_timestamps` map (legacy `cookie_header` strings still tolerated on read) | `newest_cookie_at()` reads the max timestamp from `cookie_timestamps`; falls back to row `obtained_at` for pre-tracking rows (`store.rs`) |
| 3 | Browser providers (skills) | Live extraction from [Brave](/skills/reference/browsers/brave-browser/) / Firefox / Chrome via CDP or each browser's on-disk cookie SQLite | Per-cookie `created` field (browsers that supply it) or "now" for CDP, which doesn't (`resolve.rs:326`) |

Source 3 is the most expensive — it spawns a Python skill subprocess, possibly attaches CDP. It's still always called when not in `skip_providers` mode, because freshness is the whole point: if Chrome has a newer cookie, the cache and store can't know that without asking. Live-session providers (Playwright tabs the user is actively using) are deliberately *skipped* unless explicitly preferred (`resolve.rs:184`) — borrowing cookies from a live tab causes session conflicts.

## Scoring

Each source produces a `ScoredResult` (`source.rs:8`). The score that actually decides the winner is `newest_cookie_at: f64` — a Unix timestamp.

```rust
// resolve.rs:118
fn consider(best: &mut Option<...>, candidate: ScoredResult, ...) -> bool {
    let dominated = match &best {
        None => true,
        Some((current, _)) => candidate.newest_cookie_at > current.newest_cookie_at,
    };
    if dominated { *best = Some((candidate, info)); }
    dominated
}
```

Why `newest_cookie_at` and not something else?

- **Not `created_at` of the row.** A credential row written six months ago can have a `session` cookie that the browser refreshed last hour. Per-cookie creation time tracks the actual session, not the time you first set up the skill.
- **Not `expires_at`.** Long expirations don't mean fresh — a cookie set yesterday with a one-year expiry is older than a cookie set this morning that expires in 24 hours. Expiration is filtered (expired cookies dropped at `source.rs:43`) but does not rank.
- **Not `last_verified`.** That's "did our auth check pass" — orthogonal to "is this the cookie the browser most recently issued."
- **`f64`, not `i64`.** Browser cookie databases store sub-second precision in the `created` field. Truncating to integer seconds would make the cache always tie with the browser on the same-second case, and the cache would always win the tiebreak — biasing toward stale data (`resolve.rs:319-321`).

## Tiebreak

`consider()` uses a strict greater-than on `newest_cookie_at` (`resolve.rs:120`). On exact equality, the *first* candidate considered keeps the lead. The gather order is fixed: cache → store → providers. So when timestamps tie:

1. Cache beats store beats providers.
2. The result for a given `(domain, identifier)` doesn't flap between calls within the same engine lifetime — the cache wins repeated reads.
3. There's a fast path at `resolve.rs:258`: if the cache won, the engine returns the cached session immediately without re-running `account.check`, persisting, or re-caching. This keeps repeated calls cheap.

The richer `is_better()` ordering in `source.rs:147` (required-names → live-session → newest → cookie count) exists for the older provider-vs-provider comparison path. The current `resolve_cookies()` implementation uses the simpler `consider()` because the gather phase already filters by `has_all_required` upstream and `live_session` providers are skipped unless explicitly preferred.

## Worked examples

All timestamps are Unix epoch seconds. Treat "now" as `1_744_675_200` (April 14, 2026, 12:00:00 UTC).

### Example 1 — Fresh Chrome cookie beats stored credential

You configured the GitHub skill last week. This morning you logged into github.com in Chrome.

| Source | `newest_cookie_at` | Notes |
|---|---|---|
| Cache | (empty) | First call this engine lifetime |
| Store | `1_744_070_400` (7 days ago) | Original setup, still valid |
| `brave-browser` provider | `1_744_654_800` (1h 50m ago) | Login from this morning |

Comparison: `1_744_654_800 > 1_744_070_400 > 0`. Provider wins. The engine runs `account.check` against the fresh cookies, persists the new `cookie_header` + `cookie_timestamps` to the store row (which `INSERT … ON CONFLICT` updates in place — `store.rs:228`), and caches it. The next call within this engine lifetime is a cache hit.

The "primary" credential never enters the comparison. There is no concept of primary.

### Example 2 — Two stored credentials for the same issuer, newer wins

You imported a Linear cookie six months ago, then re-imported it last Tuesday after a logout. Both rows survive in the store under `(linear.app, "joe@example.com")` because the `(domain, identifier, item_type, source)` unique index (`store.rs:35`) admits them as separate rows when their `source` differs (one from `manual-import`, one from `brave-browser`). `get_best()` returns one row by its own ordering (refreshable → expires_at → last_verified → id), but `score_stored()` then scores whichever row was returned.

| Row | `obtained_at` | `cookie_timestamps.session` | `newest_cookie_at()` |
|---|---|---|---|
| Old (manual) | `1_728_950_400` | absent | `1_728_950_400` (falls back to `obtained_at`) |
| New (brave-browser) | `1_744_588_800` | `1_744_588_800.317` | `1_744_588_800.317` |

`get_best()` ordering picks the new row first (newer `id`). Even if it picked the old one, providers run after and the brave-browser provider would still produce a fresher candidate from live extraction. The newer row wins either way. Architecturally, this is the point: storage layout doesn't have to encode "which credential is primary" because freshness comparison is layered on top.

### Example 3 — Browser provider unreachable, store fallback

Brave is closed. CDP refuses to connect. Firefox isn't installed.

| Source | Outcome | `newest_cookie_at` |
|---|---|---|
| Cache | miss | — |
| Store | `1_744_588_800` | `1_744_588_800` |
| `brave-browser` | `Failed: connection refused` | (no candidate produced) |
| `firefox-browser` | `Failed: profile not found` | (no candidate produced) |

Each provider failure is recorded as an `Attempt` with `outcome: Failed` (`resolve.rs:235`) but does not abort resolution. The store's candidate is the only one in `best`, so it wins. The provenance the skill receives lists every attempted provider with its failure reason — useful when triaging "why did it use the stale cookie?"

If the store had also missed, `best` would be `None` and `resolve_cookies` would return `AuthError::NoProvider` with the joined `tried` summary (`resolve.rs:246`).

## Retry and escalation

The cookie that wins resolution may still fail at the wire — the server returns 401, or the skill's own response parser throws `SESSION_EXPIRED`. The `ExecutionContext` (`crates/core/src/execution/engine.rs`) carries the last resolved session on `ctx.last_session`; the retry path in `crates/core/src/skills/executor.rs` reads from there.

When the operation fails and `err.is_auth_failure()` returns true, the retry path:

1. Reads `ctx.last_session`, calls `auth_store.invalidate(sess)` — drops the cache entry and deletes the store row (`resolve.rs`).
2. Re-runs the operation. The next `resolve_cookies()` call sees a cache miss + store miss, so it has to call providers, which forces a fresh extraction.
3. After retry, compares the *new* `cookie_header` (derived from `session.cookies`) against the failed one. If they're byte-identical, the browser itself has stale cookies — re-extraction is pointless and the retry is purely diagnostic. The log line `"Retry used identical cookies — session truly expired in browser"` tells the operator to log in.

Cookie writeback during a tool call rides the `__cookie_delta__` sidecar on the tool result. The Python worker snapshot-diffs its ambient Jar (live vs seed) at tool exit and emits `{added, changed, removed}`; the engine's `apply_cookie_delta_writeback` (`executor.rs`) routes that through `agentos_auth::store::apply_cookie_delta` to upsert structured cookies into the row by `(domain, path, name)`.

## Why this shape

Timestamp-based resolution trades a UX feature (the user can't pin a "primary" credential) for a structural property (zero per-service config). Every alternative — provider priority lists, per-domain default sources, "primary credential" flags — requires the user to make a decision that the engine can answer correctly from data already in hand. The freshest candidate is empirically the right answer for the overwhelming majority of cases (you logged in most recently with whichever browser you actually use), and when it isn't, `preferred_provider` on the request gives the skill a single explicit override (`resolve.rs:195`). The honest cost is that "I want this one" requires writing code, not clicking a checkbox — which is fine for a system whose primary user is an agent.
