---
title: Apps index
description: "Every app in the AgentOS catalog. Browse all or filter by category."
---

The AgentOS app catalog — **46** apps across **15** categories. Each app is a Python adapter that connects to a service or provides a pure agent tool.

See [Apps → Overview](/apps/overview/) for how to build one.

## [agents](/apps/reference/agents/)

- [**Itineraries**](/apps/reference/agents/itineraries/) — Render travel itineraries (flights, lodging, rentals, dining) from graph `reservation` nodes — PDF, markdown, text
- [**reverse-engineering**](/apps/reference/agents/reverse-engineering/) — Systematically analyze and document how software systems work internally. Use when you need to understand closed-source systems, third-party integrations, or undocumented APIs

## [ai](/apps/reference/ai/)

- [**Claude**](/apps/reference/ai/claude/) — Claude — Anthropic's AI model family. Inference via API or local CLI, plus claude.ai chat history
- [**Ollama**](/apps/reference/ai/ollama/) — Local AI models running on your machine via Ollama
- [**OpenRouter**](/apps/reference/ai/openrouter/) — Unified AI gateway for models across providers via one API

## [browsers](/apps/reference/browsers/)

- [**Brave Browser**](/apps/reference/browsers/brave-browser/) — Browsing history, bookmarks, and cookies from Brave Browser on macOS — including session key extraction for claude.ai
- [**Google Chrome**](/apps/reference/browsers/google-chrome/) — CDP access to Google Chrome — debug-attachable sessions for the engine's browser_session host, attach or launch

## [comms](/apps/reference/comms/)

- [**Gmail**](/apps/reference/comms/gmail/) — Full-featured Gmail — read, search, send, reply, forward, label, archive, draft, attachments, filters, and batch operations. Auth can use the shared `google` OAuth service when a provider integration is available
- [**iMessage**](/apps/reference/comms/imessage/) — Send and read iMessages and SMS from macOS Messages app
- [**Mimestream**](/apps/reference/comms/mimestream/) — Read and search email from Mimestream, a native macOS email client for Gmail
- [**WhatsApp**](/apps/reference/comms/whatsapp/) — Full WhatsApp presence via live WhatsApp Web — read, send text and media, react, show typing, search the full server-side history

## [dev](/apps/reference/dev/)

- [**Cursor**](/apps/reference/dev/cursor/) — AI-first code editor with built-in MCP support
- [**Git**](/apps/reference/dev/git/) — Local git repository data — commits, branches, tags, and repo info
- [**GitHub**](/apps/reference/dev/github/) — Work with GitHub issues, pull requests, and repository files through the local gh CLI. Use when working with GitHub repos, issues, PRs, or reading files from a repo
- [**Greptile**](/apps/reference/dev/greptile/) — AI code review and codebase search — organization and member management via dashboard session
- [**Linear**](/apps/reference/dev/linear/) — Project management for engineering teams
- [**Logo.dev**](/apps/reference/dev/logo-dev/) — Company logos via CDN - lookup by domain, ticker, or name

## [finance](/apps/reference/finance/)

- [**Copilot Money**](/apps/reference/finance/copilot-money/) — Read accounts, transactions, and balance history from Copilot Money, a personal finance app for macOS/iOS

## [fitness](/apps/reference/fitness/)

- [**Austin Boulder Project**](/apps/reference/fitness/austin-boulder-project/) — Class schedules and bookings for the Austin Bouldering Project gym

## [hosting](/apps/reference/hosting/)

- [**Gandi**](/apps/reference/hosting/gandi/) — Domain and DNS management via the Gandi API
- [**here.now**](/apps/reference/hosting/here-now/) — Publish static websites instantly — HTML, images, PDFs — no account needed
- [**Porkbun**](/apps/reference/hosting/porkbun/) — Domain and DNS management via the Porkbun API

## [logistics](/apps/reference/logistics/)

- [**Amazon**](/apps/reference/logistics/amazon/) — Search products, get details, and access your Amazon account
- [**SpaceX**](/apps/reference/logistics/spacex/) — SpaceX launch data — upcoming, past, and individual launch details
- [**Uber**](/apps/reference/logistics/uber/) — Ride history, trip details, Eats order history, and account info from Uber
- [**United Airlines**](/apps/reference/logistics/united/) — Flight search, reservations, boarding passes, travel history, and MileagePlus account access

## [macos](/apps/reference/macos/)

- [**macOS Control**](/apps/reference/macos/macos-control/) — Inspect macOS apps, processes, displays, windows, screenshots, and filesystem with built-in system tools
- [**macOS Keychain**](/apps/reference/macos/macos-keychain/) — Credential provider backed by the macOS login Keychain. Exposes internet-password entries matching a domain via `@provides(login_credentials)` so apps' `login` tools can pull `{email, password}` without pasting anything
- [**macOS Security**](/apps/reference/macos/macos-security/) — Audit macOS credentials, Keychain entries, and app tokens. Lists what OAuth tokens, API keys, and session credentials are stored on this machine, extracts specific tokens, identifies which apps have Google OAuth access, and scans macOS Internet Accounts

## [media](/apps/reference/media/)

- [**Facebook**](/apps/reference/media/facebook/) — Query public Facebook group information without login
- [**Goodreads**](/apps/reference/media/goodreads/) — Read your Goodreads profile, books, reviews, friends, and activity
- [**Hacker News**](/apps/reference/media/hackernews/) — Read Hacker News stories, comments, and discussions
- [**Moltbook**](/apps/reference/media/moltbook/) — Read and publish Moltbook posts, comments, feeds, communities, and agent profiles. Use when working with Moltbook, submolts, or agent social posting
- [**Reddit**](/apps/reference/media/reddit/) — Read public Reddit communities, posts, and comments
- [**YouTube**](/apps/reference/media/youtube/) — Get video metadata and transcripts using yt-dlp

## [misc](/apps/reference/misc/)

- [**Health Records**](/apps/reference/misc/health/) — Parses on-disk lab reports into the health graph

## [productivity](/apps/reference/productivity/)

- [**Google Calendar**](/apps/reference/productivity/google-calendar/) — Read, create, update, and delete Google Calendar events — replaces apple-calendar with Google API + OAuth
- [**Google Contacts**](/apps/reference/productivity/google-contacts/) — Read, search, create, and update Google Contacts via the People API
- [**Granola**](/apps/reference/productivity/granola/) — Meeting transcripts, AI summaries, and Q&A conversations from Granola
- [**Todoist**](/apps/reference/productivity/todoist/) — Personal task management

## [secrets](/apps/reference/secrets/)

- [**1Password**](/apps/reference/secrets/onepassword/) — Credential provider backed by the 1Password CLI (`op`). Exposes Login and API-Credential vault items via `@provides(login_credentials)` and `@provides(api_key)` so apps' `login` tools can pull `{email, password}` or API keys without the user pasting anything

## [web](/apps/reference/web/)

- [**Brave Search**](/apps/reference/web/brave/) — Privacy-focused web search with independent index
- [**Exa**](/apps/reference/web/exa/) — Semantic web search and content extraction
- [**Firecrawl**](/apps/reference/web/firecrawl/) — Read webpages with browser rendering for JS-heavy sites
- [**PostHog**](/apps/reference/web/posthog/) — Product analytics — events, persons, and session recordings
- [**SerpAPI**](/apps/reference/web/serpapi/) — Google search results API — flights, hotels, web search, and more

