---
title: Response shaping (view.detail & view.format)
description: How skill responses are shaped for different audiences — structured JSON for machines, markdown for chat UIs, verbatim text for monospace artifacts.
---

Every `run()` call takes an optional `view:` block that shapes the
response before it hits the wire. Two knobs, orthogonal:

| Knob         | Values                                      | Controls                  |
| ------------ | ------------------------------------------- | ------------------------- |
| `view.detail`| `preview` *(default)* · `full`             | How much data to include. |
| `view.format`| `markdown` *(default)* · `json` · `text`   | How to render it.         |

Three formats, three audiences. Pick the one that matches *who is reading
this response*.

## `view.format`

### `markdown` — humans reading prose

The default. Tables, headers, bullet lists, inline links. Optimized for
chatbot UIs that render markdown (Claude Desktop, Cursor, ChatGPT, web
portals). Works fine in a terminal — markdown is still plain text.

Use when:
- The response is semantic text: a list of search results, a summary, a
  status report.
- The consumer renders markdown inline.

### `json` — machines and debugging

Structured, exact, unambiguous. `{ data, meta }` envelope — every
relationship traversed, every field typed, no prose. Callers parse the
JSON and pick what they need.

Use when:
- Another tool is chaining off this result.
- You're debugging and want to see everything the skill returned.
- Building UI from the structured data rather than rendering markdown.

### `text` — monospace visual artifacts

Pre-rendered output where **whitespace is load-bearing**: ASCII diagrams,
tree printers, box-drawing tables, seat maps, flame graphs, dumped
spreadsheets.

When a skill returns a pre-rendered block (typically in an `ascii`,
`diagram`, `output`, or `text` field on the response dict), the engine:

1. Pulls that string off the response.
2. Wraps it in a fenced ```` ```text ```` markdown block.
3. Prefixes with `Reproduce verbatim:\n\n` — an explicit instruction to
   the LLM that receives the response.
4. Appends any companion prose (`legend`, `summary`, `caption`, `note`
   fields) after the fence as plain text.

Why this shape survives every downstream path:

- **Raw terminals** (Claude Code CLI, `agentos call`, tmux): triple
  backticks are three visible characters — no effect on rendering.
- **Markdown-rendering chat UIs** (Claude Desktop, Cursor, ChatGPT,
  Zed): the fence signals "code block, preserve whitespace and
  monospace font" — alignment survives.
- **LLM token echo-back** (small models relaying to a chat UI that
  hides MCP responses): "Reproduce verbatim:" plus a fence is the most
  reliable prompt pattern for "emit this exactly as-is." Token costs
  are linear and predictable.

Use when:
- The response IS the visual artifact (a `render_*` tool, a chart, a
  cabin map, a tree view).
- Losing alignment would break the meaning.

### What `view.format` is NOT for

There is no `view.format=image` or `view.format=binary`. The MCP protocol
supports `image` content blocks, but returning an image **breaks the
echo-back path**: an LLM cannot reproduce a PNG by emitting tokens, and
chat UIs that hide MCP responses from users would silently swallow the
image. For universal reach across terminals (no Kitty/Sixel/iTerm2 graphics
assumption), chat UIs (no image rendering guarantees), and token-relay
paths (LLM can't emit PNGs), `view.format=text` is the right primitive.

## Writing skills that support `view.format=text`

The contract is tiny: **put the pre-rendered block under a key named
`ascii`, `diagram`, `output`, or `text` on your response dict.** The
engine handles the wrapping + prefix.

```python
@returns({"ascii": "string", "legend": "string"})
@connection("web")
@timeout(30)
async def render_seatmap(*, cart_id: str, ...) -> dict:
    """Render an ASCII cabin chart."""
    sm = await get_seatmap(cart_id=cart_id, ...)
    ascii_art = build_ascii_diagram(sm)   # you own the layout
    legend = "Legend: ○ free · $N paid · ✕ occupied"
    return {"ascii": ascii_art, "legend": legend}
```

Caller:

```bash
agentos call run '{
  "skill": "united",
  "tool": "render_seatmap",
  "params": {...},
  "view": {"format": "text"}
}'
```

Response (truncated):

```
Reproduce verbatim:

​```text
┌─────────────────────────────────┐
│         United Economy          │
│    A   B   C       D   E   F    │
│    ✕   ✕   ✕   7  ███ ███  ✕    │
│    ...
└─────────────────────────────────┘
​```

Legend: ○ free · $N paid · ✕ occupied
```

### Fallback behavior

If the caller passes `view.format=text` but the response has no `ascii`
/ `diagram` / `output` / `text` field, the engine falls back to
pretty-printed JSON. A safe degrade — you never get nothing.

### Field search order

| Priority | Key        | Typical use                                   |
| -------- | ---------- | --------------------------------------------- |
| 1        | `ascii`    | ASCII / Unicode box-drawing diagrams.         |
| 2        | `diagram`  | Generic "a diagram lives here" field name.    |
| 3        | `output`   | CLI-style dumps, formatted log tails.         |
| 4        | `text`     | Generic fallback — plain multiline strings.   |

Companion prose (appended after the fence):

- `legend`, `summary`, `caption`, `note`

## Aliases

Short forms are accepted for `view.format`:

| Canonical | Aliases              |
| --------- | -------------------- |
| `markdown`| `md`                 |
| `json`    | —                    |
| `text`    | `txt`, `ascii`       |

## Default

When `view.format` is omitted, the format defaults to `markdown` for the
`run` tool (and most others). This is a deliberate choice — markdown is
the right format for the median response. Skills that produce visual
artifacts should document in their readme that callers should pass
`view.format=text`.
