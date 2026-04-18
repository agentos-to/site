---
title: Shapes
description: "Every shape in the AgentOS ontology. Browse all 81, or follow a tag chain."
---

The AgentOS ontology — **73** shapes. Each shape defines what an entity *is* (fields, relations, display hints). Shapes can extend other shapes via `also:`, which makes that shape a **tag** on the entity — a person is also an actor; a book is also a product.

See [Overview](/shapes/overview/) for the tactical reference and [Shape design principles](/shapes/shape-design-principles/) for the rules.

## All shapes

- [`account`](/shapes/reference/account/) — A user's presence on a platform — their GitHub handle, Gmail address, etc
- [`activity`](/shapes/reference/activity/) — An immutable change event — a graph mutation, skill run, search, or load
- [`actor`](/shapes/reference/actor/) — Base type for anything that can be attributed as "who did this" in the graph
- [`agent`](/shapes/reference/agent/) — also `actor` — An AI agent that acts on behalf of a user. Agents are actors — they
- [`aircraft`](/shapes/reference/aircraft/) — also `product` — An aircraft type (not an individual plane). Linked from flight search results
- [`album`](/shapes/reference/album/) — A curated collection of images produced by the engine or a skill
- [`app`](/shapes/reference/app/) — A graphical app (TS/React) that runs on top of the engine — browser,
- [`book`](/shapes/reference/book/) — also `product` — A book. Books are also products, so they inherit price/brand fields
- [`branch`](/shapes/reference/branch/) — A git branch
- [`brand`](/shapes/reference/brand/) — A consumer brand. Extracted from product listings
- [`calendar`](/shapes/reference/calendar/) — A calendar — container for events
- [`channel`](/shapes/reference/channel/) — A content channel — typically a YouTube channel. Videos are uploaded to channels
- [`class`](/shapes/reference/class/) — also `event` — A scheduled, bookable group activity — gym classes, workshops, courses
- [`community`](/shapes/reference/community/) — An online community — a subreddit, Facebook group, or similar
- [`conversation`](/shapes/reference/conversation/) — A message thread — an iMessage chat, WhatsApp group, email thread, Claude
- [`dns_record`](/shapes/reference/dns_record/) — A DNS record for a domain. One domain has many records (A, CNAME, MX, TXT, etc.)
- [`document`](/shapes/reference/document/) — also `file` — A document — any human-readable text content with structure and authorship
- [`domain`](/shapes/reference/domain/) — A registered domain name. Also auto-created from email sender/recipient addresses
- [`email`](/shapes/reference/email/) — also `message` — An email message. Emails are also messages — querying by "message"
- [`episode`](/shapes/reference/episode/) — A single episode of a podcast or show. Transcribable
- [`event`](/shapes/reference/event/) — Something that happens — at a time, optionally at a place, involving people
- [`file`](/shapes/reference/file/) — A file — source code, attachment, download, or any discrete digital artifact
- [`folder`](/shapes/reference/folder/) — A filesystem directory or workspace. Used to track project roots,
- [`git_commit`](/shapes/reference/git_commit/) — A git commit — a single point in version control history
- [`group`](/shapes/reference/group/) — A group or community — online group, reading group, etc
- [`hardware`](/shapes/reference/hardware/) — also `product` — A physical hardware product — computer, phone, appliance, component
- [`image`](/shapes/reference/image/) — also `file` — An image file. Photos, screenshots, diagrams, artwork
- [`invitation`](/shapes/reference/invitation/) — An invitation to join something — an organization, a workspace, a team, a
- [`job`](/shapes/reference/job/) — A running or completed unit of work the engine is responsible for —
- [`leg`](/shapes/reference/leg/) — One continuous movement on a single vehicle — takeoff to landing,
- [`list`](/shapes/reference/list/) — A generic collection of items. Base type for shelf (books) and playlist (videos)
- [`loaded_model`](/shapes/reference/loaded_model/) — A currently loaded/running AI model instance
- [`meeting`](/shapes/reference/meeting/) — also `event` — A calendar meeting — an event with virtual meeting details and transcripts
- [`memex`](/shapes/reference/memex/) — A memex — a portable knowledge graph. Named for Vannevar Bush's
- [`message`](/shapes/reference/message/) — A single message in a conversation. Base type — email extends this via `also`
- [`model`](/shapes/reference/model/) — An AI model — LLM, embedding model, or other ML model
- [`note`](/shapes/reference/note/) — Private text content, primarily for the author. Journal entries, PKM notes,
- [`offer`](/shapes/reference/offer/) — A purchasable offer — typically a flight itinerary with a price
- [`order`](/shapes/reference/order/) — A purchase order. Contains products and tracks delivery
- [`organization`](/shapes/reference/organization/) — also `actor` — A company, nonprofit, or other organization. Organizations are actors — they
- [`person`](/shapes/reference/person/) — also `actor` — A real human. People are actors — they can own accounts, hold roles, attend meetings
- [`place`](/shapes/reference/place/) — A physical location — address, building, city, or point of interest
- [`platform`](/shapes/reference/platform/) — also `software` — A service that users interact with — Amazon, Gmail, Reddit, WhatsApp
- [`playlist`](/shapes/reference/playlist/) — also `list` — A video playlist. Playlists are lists that contain videos instead of products
- [`podcast`](/shapes/reference/podcast/) — A podcast series. Contains episodes. Not the audio itself — that's on the episode
- [`post`](/shapes/reference/post/) — A piece of published content — a Reddit submission, HN story, YouTube upload,
- [`product`](/shapes/reference/product/) — A purchasable item. Base type for book and aircraft
- [`project`](/shapes/reference/project/) — A project that groups tasks. Tasks belong to projects
- [`quote`](/shapes/reference/quote/) — A notable quote. Attribution is a graph relationship, not a field —
- [`repository`](/shapes/reference/repository/) — A source code repository
- [`result`](/shapes/reference/result/) — A search result — a pointer to something found. Not the thing itself
- [`review`](/shapes/reference/review/) — also `post` — A user review of a product. Reviews are also posts, so they carry engagement metrics
- [`role`](/shapes/reference/role/) — A person's position at an organization (job title, board seat, etc.)
- [`search`](/shapes/reference/search/) — A search query and its results. Every search is a graph entity with click
- [`session`](/shapes/reference/session/) — An MCP session — a client connected, made some calls, disconnected
- [`shelf`](/shapes/reference/shelf/) — also `list` — A bookshelf. Shelves are lists that contain books instead of generic products
- [`shortcut`](/shapes/reference/shortcut/) — A named alias that expands to a location URI at parse time
- [`simulation`](/shapes/reference/simulation/) — A simulation — an isolated runtime where an agent runs. The "VM"
- [`skill`](/shapes/reference/skill/) — A connected service/integration in agentOS. Each skill provides tools
- [`software`](/shapes/reference/software/) — also `product` — A software application — web app, desktop app, mobile app, CLI tool
- [`source`](/shapes/reference/source/) — A content source — where skills, themes, shapes, and wallpapers live
- [`spec`](/shapes/reference/spec/) — also `task`, `file` — A spec — a design document describing work to be done
- [`tag`](/shapes/reference/tag/) — A tag or label — Gmail label, Todoist label, GitHub label, git tag, etc
- [`task`](/shapes/reference/task/) — A work item — issue, ticket, or to-do. Supports hierarchy (parent/children)
- [`theme`](/shapes/reference/theme/) — An OS theme — window chrome, taskbar, scrollbars, desktop styling
- [`tool_call`](/shapes/reference/tool_call/) — A single tool invocation made by an agent during a message
- [`transaction`](/shapes/reference/transaction/) — A financial transaction — credit card charge, bank transfer, etc
- [`transcript`](/shapes/reference/transcript/) — A text transcript of audio/video content. Linked from meetings and videos
- [`trip`](/shapes/reference/trip/) — A directed journey from origin to destination — one direction of travel
- [`video`](/shapes/reference/video/) — also `file` — A video file — the media artifact, not the social context around it
- [`volume`](/shapes/reference/volume/) — A storage volume — local disk, external drive, network share, or cloud drive
- [`webpage`](/shapes/reference/webpage/) — A web page. Base type for search result. Also used for browser history
- [`website`](/shapes/reference/website/) — A published website (not a single page — see webpage for that)
