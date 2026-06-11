---
title: symbol
description: "A code symbol — one named thing in a source surface: an MCP tool/op, a"
sidebar:
  label: symbol
---

A code symbol — one named thing in a source surface: an MCP tool/op, a
Rust fn/struct/trait, a TS hook/component, a shape. The unit of the
**System Docs** volume's API reference, projected from the canonical
source (tool schemas, rustdoc JSON, ts-morph) — never authored by hand.
A symbol describes *the code*, so it carries identity (`urn`), a callable
`signature`, the `summary` line, and a source pointer back to the truth;
the full rendered docstring lives in its content `body` so it reads as a
page. The cross-language `urn` is what lets a TS hook link the Rust tool
it calls — cross-links are the product, not a flat dump.

| Metadata | Value |
|---|---|
| **Plural** | `symbols` |
| **Subtitle field** | `signature` |

## Fields

| Field | Type |
|---|---|
| `urn` | `string` |
| `kind` | `string` |
| `lang` | `string` |
| `signature` | `text` |
| `summary` | `text` |
| `sourcePath` | `string` |
| `sourceLine` | `integer` |

## Relations

| Relation | Target |
|---|---|
| `returns` | `node` |
| `calls` | [`symbol`](/shapes/reference/symbol/) |
| `called_by` | [`symbol`](/shapes/reference/symbol/) |
| `see` | [`document`](/shapes/reference/document/) |
| `documents` | `node` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[Language Server Protocol — DocumentSymbol / SymbolKind](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_documentSymbol)** — SymbolKind (Function/Struct/Interface/Method/Module…) is the canonical `kind` enum; DocumentSymbol's name + detail + range → our name + signature + sourcePath/sourceLine.
- **[LSIF — Language Server Index Format](https://microsoft.github.io/language-server-protocol/specifications/lsif/0.6.0/specification/)** — LSIF persists hover/definition/references as a graph of monikers across files — exactly our `urn` + calls/called_by trail, made queryable.
- **[rustdoc JSON output format](https://doc.rust-lang.org/rustdoc/unstable-features.html#--output-format-json-output-crate-info-in-json)** — The P3 extractor's source — Item{id, name, kind, docs, links} maps item.id → urn, kind → kind, docs → body, inner.decl → signature.
- **[schema.org/SoftwareSourceCode + ctags](https://schema.org/SoftwareSourceCode)** — codeRepository/programmingLanguage → lang; ctags' (tag, file, kind) triple is the minimal symbol-index prior art for sourcePath + kind.
