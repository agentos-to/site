---
title: Skills index
description: "Every skill in the AgentOS catalog. Browse all or filter by category."
---

The AgentOS skill catalog — **46** skills across **14** categories. Each skill is a Python adapter that connects to a service or provides a pure agent capability.

See [Skills → Overview](/skills/overview/) for how to build one.

## [agents](/skills/reference/agents/)

- [**Code Review**](/skills/reference/agents/code-review/) — Evaluate code changes against project principles, refactoring specs, and architectural direction
- [**Itineraries**](/skills/reference/agents/itineraries/) — Render travel itineraries (flights, lodging, rentals, dining) from graph `reservation` nodes — PDF, markdown, text
- [**reverse-engineering**](/skills/reference/agents/reverse-engineering/) — Systematically analyze and document how software systems work internally. Use when you need to understand closed-source systems, third-party integrations, or undocumented APIs

## [ai](/skills/reference/ai/)

- [**Claude**](/skills/reference/ai/claude/) — Claude — Anthropic's AI model family. Inference via API or local CLI, plus claude.ai chat history
- [**Ollama**](/skills/reference/ai/ollama/) — Local AI models running on your machine via Ollama
- [**OpenRouter**](/skills/reference/ai/openrouter/) — Unified AI gateway for models across providers via one API

## [browsers](/skills/reference/browsers/)

- [**Brave Browser**](/skills/reference/browsers/brave-browser/) — Browsing history, bookmarks, and cookies from Brave Browser on macOS — including session key extraction for claude.ai

## [comms](/skills/reference/comms/)

- [**Gmail**](/skills/reference/comms/gmail/) — Full-featured Gmail — read, search, send, reply, forward, label, archive, draft, attachments, filters, and batch operations. Auth can use the shared `google` OAuth capability when a provider integration is available
- [**iMessage**](/skills/reference/comms/imessage/) — Send and read iMessages and SMS from macOS Messages app
- [**Mimestream**](/skills/reference/comms/mimestream/) — Read and search email from Mimestream, a native macOS email client for Gmail
- [**WhatsApp**](/skills/reference/comms/whatsapp/) — Read WhatsApp messages from local macOS database

## [dev](/skills/reference/dev/)

- [**Cursor**](/skills/reference/dev/cursor/) — AI-first code editor with built-in MCP support
- [**Git**](/skills/reference/dev/git/) — Local git repository data — commits, branches, tags, and repo info
- [**GitHub**](/skills/reference/dev/github/) — Work with GitHub issues, pull requests, and repository files through the local gh CLI. Use when working with GitHub repos, issues, PRs, or reading files from a repo
- [**Greptile**](/skills/reference/dev/greptile/) — AI code review and codebase search — organization and member management via dashboard session
- [**Linear**](/skills/reference/dev/linear/) — Project management for engineering teams
- [**Logo.dev**](/skills/reference/dev/logo-dev/) — Company logos via CDN - lookup by domain, ticker, or name

## [finance](/skills/reference/finance/)

- [**Copilot Money**](/skills/reference/finance/copilot-money/) — Read accounts, transactions, and balance history from Copilot Money, a personal finance app for macOS/iOS

## [fitness](/skills/reference/fitness/)

- [**Austin Boulder Project**](/skills/reference/fitness/austin-boulder-project/) — Class schedules and bookings for the Austin Bouldering Project gym

## [hosting](/skills/reference/hosting/)

- [**Gandi**](/skills/reference/hosting/gandi/) — Domain and DNS management via the Gandi API
- [**here.now**](/skills/reference/hosting/here-now/) — Publish static websites instantly — HTML, images, PDFs — no account needed
- [**Porkbun**](/skills/reference/hosting/porkbun/) — Domain and DNS management via the Porkbun API

## [logistics](/skills/reference/logistics/)

- [**Amazon**](/skills/reference/logistics/amazon/) — Search products, get details, and access your Amazon account
- [**SpaceX**](/skills/reference/logistics/spacex/) — SpaceX launch data — upcoming, past, and individual launch details
- [**Uber**](/skills/reference/logistics/uber/) — Ride history, trip details, Eats order history, and account info from Uber
- [**United Airlines**](/skills/reference/logistics/united/) — Flight search, reservations, boarding passes, travel history, and MileagePlus account access

## [macos](/skills/reference/macos/)

- [**macOS Control**](/skills/reference/macos/macos-control/) — Inspect macOS apps, processes, displays, windows, screenshots, and filesystem with built-in system tools
- [**macOS Keychain**](/skills/reference/macos/macos-keychain/) — Credential provider backed by the macOS login Keychain. Exposes internet-password entries matching a domain via `@provides(login_credentials)` so skills' `login` tools can pull `{email, password}` without pasting anything
- [**macOS Security**](/skills/reference/macos/macos-security/) — Audit macOS credentials, Keychain entries, and app tokens. Lists what OAuth tokens, API keys, and session credentials are stored on this machine, extracts specific tokens, identifies which apps have Google OAuth access, and scans macOS Internet Accounts

## [media](/skills/reference/media/)

- [**Facebook**](/skills/reference/media/facebook/) — Query public Facebook group information without login
- [**Goodreads**](/skills/reference/media/goodreads/) — Read your Goodreads profile, books, reviews, friends, and activity
- [**Hacker News**](/skills/reference/media/hackernews/) — Read Hacker News stories, comments, and discussions
- [**Moltbook**](/skills/reference/media/moltbook/) — Read and publish Moltbook posts, comments, feeds, communities, and agent profiles. Use when working with Moltbook, submolts, or agent social posting
- [**Reddit**](/skills/reference/media/reddit/) — Read public Reddit communities, posts, and comments
- [**YouTube**](/skills/reference/media/youtube/) — Get video metadata and transcripts using yt-dlp

## [productivity](/skills/reference/productivity/)

- [**Google Calendar**](/skills/reference/productivity/google-calendar/) — Read, create, update, and delete Google Calendar events — replaces apple-calendar with Google API + OAuth
- [**Google Contacts**](/skills/reference/productivity/google-contacts/) — Read, search, create, and update Google Contacts via the People API
- [**Granola**](/skills/reference/productivity/granola/) — Meeting transcripts, AI summaries, and Q&A conversations from Granola
- [**Todoist**](/skills/reference/productivity/todoist/) — Personal task management

## [secrets](/skills/reference/secrets/)

- [**1Password**](/skills/reference/secrets/onepassword/) — Credential provider backed by the 1Password CLI (`op`). Exposes Login and API-Credential vault items via `@provides(login_credentials)` and `@provides(api_key)` so skills' `login` tools can pull `{email, password}` or API keys without the user pasting anything

## [web](/skills/reference/web/)

- [**Brave Search**](/skills/reference/web/brave/) — Privacy-focused web search with independent index
- [**Curl**](/skills/reference/web/curl/) — Simple URL fetching using curl (no API key needed)
- [**Exa**](/skills/reference/web/exa/) — Semantic web search and content extraction
- [**Firecrawl**](/skills/reference/web/firecrawl/) — Read webpages with browser rendering for JS-heavy sites
- [**PostHog**](/skills/reference/web/posthog/) — Product analytics — events, persons, and session recordings
- [**SerpAPI**](/skills/reference/web/serpapi/) — Google search results API — flights, hotels, web search, and more

