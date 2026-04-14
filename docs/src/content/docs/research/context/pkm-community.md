---
title: PKM Community Research
description: Web research on what the Personal Knowledge Management community wants from note-taking tools.
---

## Top Features the PKM Community Wants

### 1. Better Search & Discovery
- **Semantic search** is the #1 pain point — users hate that default search is "barely substring matching" and want meaning-based retrieval like Google
- **Smart Connections plugin** (4,500+ GitHub stars, 800K+ downloads) shows massive demand for AI-powered semantic search that finds related notes automatically
- Users want **proactive surfacing** — the tool should show you relevant notes without you having to search

### 2. Real-Time AI Recall
- As you type, show related notes from your past
- "Don't make me remember tags or search manually — retrieve relevance for me"
- This is the killer feature that new tools like Mem.ai and Constella are building around

### 3. Multiplayer/Collaboration
- Collaborative note editing and sharing is on Obsidian's official roadmap
- Teams want to effortlessly discover related project information without manual curation

### 4. Better Mobile Experience
- Obsidian's mobile app is praised, but Roam's mobile "was a flop"
- Quick capture from anywhere, including voice
- Navigation and note retrieval on mobile remains frustrating compared to Apple Notes

### 5. Calendar & Time-Based Views
- Calendar view for bases/databases is highly requested (on Obsidian roadmap)
- Kanban views for task management
- Better daily notes workflows

### 6. Knowledge Graphs That Actually Help
- Graph view is popular but often "completely unusable if you have a large number of notes"
- Users want **local graphs** that update automatically and help navigate connections
- Obsidian's graph view is praised as "incredible" with filters, groups, and customization

### 7. Block-Level References
- Roam/Logseq excel here — every block is its own addressable unit
- Obsidian's block references feel "hacky" with weird identifiers
- People want to link and embed atomic note elements across notes easily

---

## Common Frustrations with Current Tools

### 1. The "Mess" Problem
> "Every attempt at PKM has landed me in the same place: a huge mess"

- Users collect thousands of notes that never get reviewed or connected
- Quick capture creates massive unprocessed backlogs
- "When there are 200+ notes on a topic, distilling useful information becomes impossible"

### 2. Feature Bloat & Setup Fatigue
- "The more a tool can do, the more it demands from you"
- "You're not thinking — you're maintaining"
- Obsidian infamous for the "tinker loop": install plugins, configure CSS, style graphs, never actually take notes
- "Every feature is another decision"

### 3. Productivity Theater
- Beautiful dashboards that never get looked at again
- "High-maintenance digital gardens that require more watering than they return in fruit"
- Systems that look helpful but waste time

### 4. Tool Hopping
- Constantly switching between Notion, Obsidian, Roam, Bear, Evernote, Anki
- Searching for the "perfect solution" and losing momentum each time

### 5. Choice Paralysis
- "Every new note opens up a decision tree: Should this be a page? A subpage? A template?"
- "The last thing you need mid-idea is five technical questions about structure"

### 6. Poor Recall
- "Most PKMs are great at capture... but almost none are built for recall"
- "I can't find what I need. Or worse — I forget that I already captured something, because it never surfaces again"

### 7. Sync Issues
- File system timestamps get changed when copying/syncing
- No official API for accessing Obsidian Sync data
- LogSeq still lacks a sync service

---

## How People Want AI to Integrate with Their Notes

### 1. Chat With Your Notes
- Natural language queries: "What did I learn about X?" or "Find notes related to this project"
- Mem.ai's Chat feature lets you "interact with your notes using natural language"
- "Ask questions, edit notes, organize collections, recall details from your knowledge base"

### 2. Automatic Semantic Connections
- AI should understand meaning, not just keywords
- Smart Connections plugin uses 1,536-dimensional vectors (OpenAI embeddings) to find semantically similar notes
- Real-time suggestions as you type

### 3. Proactive Surfacing
- "Heads Up" features that surface related notes while you work
- "Future apps will anticipate information needs based on context, schedule, and work patterns"
- Show relevant past notes without manual search

### 4. Automated Summarization
- 30% reduction in time organizing notes after meetings with AI summarization
- Auto-generate meeting recaps, action items
- Summarize long notes highlighting key points

### 5. Smart Organization
- AI Note Tagger plugin is trending in 2025
- Auto-categorization and tagging
- Concept mapping and knowledge graph generation

### 6. Voice Integration
- Voice-to-text transcription for brain dumps
- Capture notes verbally, have them processed into structured text

### 7. What People DON'T Want
- AI that requires manual setup/configuration
- Another system to maintain
- AI that doesn't understand personal context (just general training data)

---

## Frontmatter & Metadata Patterns People Use

### Best Practices from the Community

1. **Minimal by design**: "Only add properties you actively use rather than including unused fields"
2. **Purposeful metadata**: "If a property is not used to answer a relevant question, it should not be included"
3. **Consistency matters**: Use standardized, lowercase property names to avoid duplication

### Common Properties Used

| Property | Purpose |
|----------|---------|
| `aliases` | Easier linking (e.g., "Chuck" links to "Chuck Mangione") |
| `type` | Categorize notes: journal, people, place, organization, recipe |
| `tags` | Organization and DataView queries |
| `status` | Track note state (fleeting, evergreen, discharged) |
| `created_at` | When note was created (filesystem dates are unreliable across syncs) |
| `project` | Project association |
| `author` | For reference notes |
| `url` | Quick access to source |

### Advanced Patterns

- **Nested YAML**: Some users create hierarchical metadata (e.g., `event.location`, `event.date`) to separate file-level properties from content-level properties
- **Type-based templates**: Different note types (book, person, event) have different required properties
- **Genesis tracking**: Track whether note is `original`, `derived`, or `external` to measure how much is your own thinking

### Anti-Patterns

- Adding `creation_date` and `modification_date` when you don't use them
- Including blank/unused properties in notes
- Over-engineering metadata schemas before you have actual use cases

---

## What Makes Obsidian/Roam/Logseq Successful

### Obsidian's Success Factors

1. **Local-first**: Plain Markdown files stored on your computer, not in the cloud
2. **Privacy**: No telemetry, no data harvesting — you own your data completely
3. **Data portability**: Notes work in any text editor; you're never locked in
4. **Plugin ecosystem**: 2,692 plugins, 97.7M+ total downloads in 2025
5. **Customization**: Themes, CSS snippets, configurable everything
6. **Graph view**: Best-in-class visualization of note connections
7. **Mobile app**: Full-featured iOS app with plugin support
8. **Business model**: Free core app, paid add-ons (Sync, Publish) fund development without VC
9. **Community**: 110,000+ Discord members, grassroots growth to 1M+ users

### Roam Research's Success Factors

1. **Pioneered bidirectional linking** in mainstream PKM
2. **Block-level references**: Every block is addressable and linkable
3. **Clean UI**: Live preview rendering as you type
4. **Daily Notes first**: Opens to today's page, captures everything there
5. **Queries**: Powerful embedded queries that surface related blocks
6. **Task management**: Built-in todo cycling with keyboard shortcuts
7. **Outliner DNA**: Perfect for hierarchical, structured thinking

### Logseq's Success Factors

1. **Best of both worlds**: Roam's outliner UX + Obsidian's local Markdown files
2. **Free & open source**: No subscription required
3. **Block references**: Same power as Roam
4. **PDF annotation**: Built-in support
5. **Task states**: More granular than Roam (Now/Later/Done)
6. **Query table view**: Clean display for query results
7. **Privacy**: Local storage like Obsidian

### Common Success Themes Across All Three

| Factor | Why It Matters |
|--------|----------------|
| **Bidirectional linking** | Discover relationships organically without upfront organization |
| **Plain text foundation** | Future-proof, portable, works anywhere |
| **Extensibility** | Customize to your workflow |
| **Active community** | Plugins, themes, shared knowledge |
| **Philosophy over features** | Opinionated about how knowledge works |

---

## Key Insights for Building PKM Tools

1. **Reduce friction at capture time** — zero decisions, zero structure required
2. **Make recall automatic** — don't make users search; surface relevant content proactively  
3. **AI should understand meaning, not just keywords**
4. **Local-first wins trust** — privacy and data ownership matter enormously
5. **Avoid feature bloat** — every feature is a decision users must make
6. **Block-level granularity** matters for serious knowledge work
7. **The graph view is cool but often unusable** — local/filtered graphs are what actually help
8. **Mobile is still unsolved** for most tools
9. **Don't make users become janitors of metadata**
10. **The real problem is retrieval, not capture** — most tools fail at surfacing past knowledge
