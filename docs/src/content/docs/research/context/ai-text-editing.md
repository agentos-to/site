---
title: AI Text & Code Editing UX Research
description: Web research on how leading AI editors show proposed changes and balance power with simplicity.
---

## How Leading AI Editors Show Proposed Changes

### Cursor

- **Inline diff with color-coding**: When using Inline Edit (Cmd+K), Cursor shows additions in green and deletions in red before acceptance
- **Cursor Flow**: Predicts next location + next edit, allowing users to Tab through a sequence of low-entropy changes (Tab pressed 11 times, other keys only 3)
- **Cursor Blame (Enterprise)**: Links each line of code to the conversation that produced it, distinguishing between Tab completions, agent runs, and human edits
- **Background editing**: For larger edits, work happens asynchronously — users write pseudocode that gets "compiled" into full changes

**Philosophy**: *"Should feel like an extension of your will. The moment you think of a change, minimal intent executes it instantly."*

### GitHub Copilot (VS Code)

- **Ghost text**: Dimmed placeholder text at cursor for completions, accepted via Tab
- **Next Edit Suggestions (NES)**: Arrow in gutter indicates available edit suggestions for *existing* code (not just completions). Tab navigates to it, Tab again accepts
- **Inline diff for multi-file edits**: Changes applied directly to disk with pending status tracked. Squared-dot icon in Explorer and tabs indicates pending edits
- **Accept/Discard widgets**: Hover over changes to accept/reject individually or all at once
- **Working Set concept**: Users explicitly define which files can be edited, giving precise control over scope

### Windsurf

- **Cascade Bar**: Dedicated UI showing which files have been changed by the AI agent
- **Continuous context awareness**: Memories track codebase details, Rules maintain code patterns
- **Tab to Jump / Tab to Import**: Suggestions go beyond code to include navigation and dependency management
- **Turbo Mode**: Auto-executes terminal commands to keep developers in flow

---

## Diff Visualization Best Practices

| Pattern | Description |
|---------|-------------|
| **Unified vs Split views** | Let users toggle based on preference |
| **Intraline highlighting** | Show character-level changes within modified lines |
| **Whitespace detection** | Auto-collapse whitespace-only changes to reduce noise |
| **Collapsible context** | Hide unchanged code by default, expand incrementally |
| **Gutter indicators** | Color-coded margins (green/red/yellow) show change status at a glance |
| **Navigation arrows** | Up/down controls to jump between changes |
| **Inline comments** | Feedback directly on specific lines within the diff |
| **Keyboard navigation** | Full keyboard support for accessibility (arrow keys, Enter to accept) |
| **Source control integration** | Staging changes auto-accepts pending AI edits |
| **Sensitive file protection** | Approval prompts with diff preview for config files (`.env`, `.vscode/*.json`) |

**Key insight**: Context management is critical — showing enough surrounding code to understand changes without overwhelming the reviewer.

---

## Balancing Power Features with Simplicity

### The Evolution Insight (from UX research)

> "We're still in a command-line moment, wearing wizard hats just to ask a machine for help."

The article traces computing UX evolution:
1. **Batch processing** → Submit instructions, wait hours
2. **Command line** → Type precise commands
3. **GUI** → Visual, drag-and-drop
4. **ChatGPT moment** → Simple chatbox anyone can use

AI editors are transitioning from #2 to #3 right now.

### Design Principles for Non-Technical Users

| Principle | Implementation |
|-----------|----------------|
| **State intent, not method** | Users say "what they want," AI figures out "how" (Manus approach) |
| **Embedded, not external** | AI lives inside the workspace, not in a separate chat window |
| **On-demand initiation** | Let users request suggestions rather than constantly interrupting |
| **Micro-suggestions** | Sentence/line-level changes, not full rewrites |
| **Voice anchoring** | Maintain the user's style rather than homogenizing |
| **Provenance** | Show why suggestions were made to build trust |

### Preserving User Agency (Research Finding)

AI assistance can *reduce* users' sense of authorship (–0.85-1.0 points on a 7-point scale). Mitigations:
- Style personalization partially restores ownership (+0.43 points)
- Let users accept/reject granularly
- Show the reasoning behind changes

### Bear/Apple Notes Design Principles (for simplicity)

- Three-pane layout (familiar mental model)
- Text-focused, distraction-free
- Markdown with hidden syntax (power when needed, clean when reading)
- Light/dark modes
- Quick capture as the primary use case

---

## Preview Patterns Across Platforms

### Quick Look Model (macOS)

- Press Space to preview without opening
- Support for images, PDFs, code with syntax highlighting
- Extensions via plugins (Glance adds format support)
- No commitment required — pure read-only inspection

### Alternatives

- **iPreview**: Instant previews across Finder/Spotlight, syntax highlighting for developers
- **Fileloupe**: Fast browsing without imports/library management

### AI Editor Preview Patterns

| Pattern | Example |
|---------|---------|
| **Ghost text** | GitHub Copilot inline suggestions |
| **Inline diff overlay** | VS Code Copilot Edits showing changes in-place |
| **Gutter arrows** | Copilot NES indicating available edits |
| **Side-by-side panels** | Copilot Edits in Secondary Side Bar while Testing view in Primary |
| **Cascade Bar** | Windsurf's dedicated file change indicator |
| **Plan visualization** | Cursor's Mermaid diagrams for agent plans |

---

## VS Code Extension Marketplace Design

- **Integrated browsing**: Extensions view via Activity Bar (⇧⌘X)
- **Discovery features**: Popular extensions, ratings, download counts
- **Search/filter**: By title, metadata, categories (predefined list)
- **Detail pages**: Full description, README, changelog
- **One-click install**: Install button → Manage gear
- **Version management**: Right-click for specific versions
- **Security dialog**: Trust confirmation for third-party publishers (since v1.97)
- **Sync settings**: "Do Not Sync" option per extension

---

## Key Takeaways for AgentOS

1. **The best prompt is no prompt**: Next Edit Suggestions and Cursor Flow show the frontier is *anticipating* user intent, not waiting for instructions

2. **Inline > Modal**: Changes shown in-place with accept/reject controls beat separate preview windows

3. **Scope control matters**: Working Set concept lets users define boundaries for AI changes

4. **Speed over perfection**: Users can iterate quickly with Undo/Redo rather than waiting for perfect first results

5. **Progressive disclosure**: Start simple (Tab to accept), reveal power features (partial accept, multi-file navigation) on demand

6. **Non-technical users need goal-level interfaces**: "Build a login page" not "create auth.tsx and import bcrypt"

7. **Trust through transparency**: Cursor Blame, provenance, and diff views build confidence in AI changes
