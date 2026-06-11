"""MDX emitter — shape + app reference pages (Starlight-compatible).

Not on the byte-identical `--check` path; verified by `generate.py
--docs` running clean. Shape pages are a projection off the IR; app
pages are discovered from the `apps/` tree.
"""

from __future__ import annotations

from pathlib import Path

from ir import STANDARD_FIELDS, Shape


# =============================================================================
# Shape docs
# =============================================================================

def _shape_link(target: str) -> str:
    """Produce a markdown link to another shape's reference page.

    `node` is the universal relation target (any addressable graph node) and
    has no reference page — render it as inline code without a link.
    """
    base = target.rstrip("[]")
    if base == "node":
        return f"`{target}`"
    return f"[`{target}`](/shapes/reference/{base}/)"


def emit_shape_docs(shapes: list[Shape], out_dir: Path, apps_index: dict[str, list[dict]]) -> None:
    """Write one MDX file per shape into `out_dir`, plus an index page.

    apps_index maps shape-name → list of {app_id, path, operations} dicts,
    so each shape page can show 'apps that produce this shape'.
    """
    out_dir.mkdir(parents=True, exist_ok=True)

    for s in shapes:
        desc = s.leading_comment.split("\n")[0] if s.leading_comment else f"Shape reference for `{s.name}`."
        # Starlight YAML-safe description: single line, no backticks, no quotes.
        desc_safe = desc.replace('"', "'").replace("`", "").strip()
        if len(desc_safe) > 160:
            desc_safe = desc_safe[:157] + "..."

        lines = [
            "---",
            f"title: {s.name}",
            f'description: "{desc_safe}"',
            "sidebar:",
            f"  label: {s.name}",
            "---",
            "",
        ]

        # Leading comment as intro prose, if present
        if s.leading_comment:
            lines.append(s.leading_comment)
            lines.append("")

        # Metadata table: plural, subtitle, identity, also chain
        meta_rows = []
        if s.plural:
            meta_rows.append(("Plural", f"`{s.plural}`"))
        if s.subtitle:
            meta_rows.append(("Subtitle field", f"`{s.subtitle}`"))
        if s.identity:
            meta_rows.append(("Identity", ", ".join(f"`{i}`" for i in s.identity)))
        if s.identity_any:
            meta_rows.append(("Identity (any)", ", ".join(f"`{i}`" for i in s.identity_any)))
        if s.also:
            chain = " · ".join(_shape_link(a) for a in s.also)
            meta_rows.append(("Also", chain))
        if meta_rows:
            lines.append("| Metadata | Value |")
            lines.append("|---|---|")
            for k, v in meta_rows:
                lines.append(f"| **{k}** | {v} |")
            lines.append("")

        # Own fields
        if s.own_fields:
            lines.append("## Fields")
            lines.append("")
            lines.append("| Field | Type |")
            lines.append("|---|---|")
            for f in s.own_fields:
                lines.append(f"| `{f.name}` | `{f.type}` |")
            lines.append("")

        # Own relations
        if s.own_relations:
            lines.append("## Relations")
            lines.append("")
            lines.append("| Relation | Target |")
            lines.append("|---|---|")
            for f in s.own_relations:
                tgt = f.target or f.type.rstrip("[]")
                arr = "[]" if f.is_array else ""
                lines.append(f"| `{f.name}` | {_shape_link(tgt + arr)} |")
            lines.append("")

        # Inherited fields (resolved - own, minus standard)
        own_names = {f.name for f in s.own_fields}
        own_rel_names = {f.name for f in s.own_relations}
        std_names = {n for n, _ in STANDARD_FIELDS}
        inherited_fields = [
            f for f in s.fields
            if not f.is_relation and f.name not in own_names and f.name not in std_names
        ]
        inherited_rels = [
            f for f in s.fields if f.is_relation and f.name not in own_rel_names
        ]
        if inherited_fields or inherited_rels:
            lines.append("## Inherited")
            lines.append("")
            if s.also:
                chain = " · ".join(_shape_link(a) for a in s.also)
                lines.append(f"From {chain}:")
                lines.append("")
            if inherited_fields:
                lines.append("| Field | Type |")
                lines.append("|---|---|")
                for f in inherited_fields:
                    lines.append(f"| `{f.name}` | `{f.type}` |")
                lines.append("")
            if inherited_rels:
                lines.append("| Relation | Target |")
                lines.append("|---|---|")
                for f in inherited_rels:
                    tgt = f.target or f.type.rstrip("[]")
                    arr = "[]" if f.is_array else ""
                    lines.append(f"| `{f.name}` | {_shape_link(tgt + arr)} |")
                lines.append("")

        # Shapes that declare THIS shape in their `also:` chain (children)
        children = sorted([c.name for c in shapes if s.name in c.also])
        if children:
            lines.append("## Used as a base by")
            lines.append("")
            for child in children:
                lines.append(f"- {_shape_link(child)}")
            lines.append("")

        # Prior art — external standards this shape aligns with
        if s.prior_art:
            lines.append("## Prior art")
            lines.append("")
            lines.append("External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.")
            lines.append("")
            for entry in s.prior_art:
                src = entry["source"]
                url = entry["url"]
                notes = entry["notes"]
                heading = f"[{src}]({url})" if url else src
                lines.append(f"- **{heading}** — {notes}" if notes else f"- **{heading}**")
            lines.append("")

        # Apps that return this shape
        producers = apps_index.get(s.name, [])
        if producers:
            lines.append("## Apps that produce this shape")
            lines.append("")
            for p in producers:
                sid = p["app_id"]
                cat = p.get("category", "")
                ops = ", ".join(f"`{op}`" for op in p["operations"])
                url = f"/apps/reference/{cat}/{sid}/" if cat else f"/apps/reference/{sid}/"
                lines.append(f"- [{sid}]({url}) — {ops}")
            lines.append("")

        (out_dir / f"{s.name}.md").write_text("\n".join(lines).rstrip() + "\n")

    # Index page — flat A-Z list with one-line descriptions
    idx = [
        "---",
        "title: Shapes",
        'description: "Every shape in the AgentOS ontology. Browse all 81, or follow a tag chain."',
        "---",
        "",
        f"The AgentOS ontology — **{len(shapes)}** shapes. Each shape defines what an entity *is* (fields, relations, display hints). Shapes can extend other shapes via `also:`, which makes that shape a **tag** on the entity — a person is also an actor; a book is also a product.",
        "",
        "See [Overview](/shapes/overview/) for the tactical reference and [Shape design principles](/shapes/shape-design-principles/) for the rules.",
        "",
        "## All shapes",
        "",
    ]
    for s in shapes:
        desc = (s.leading_comment.split("\n")[0] if s.leading_comment else "").strip().rstrip(".")
        also = ""
        if s.also:
            also = f" — also {', '.join(f'`{a}`' for a in s.also)}"
        desc_part = f" — {desc}" if desc else ""
        idx.append(f"- [`{s.name}`](/shapes/reference/{s.name}/){also}{desc_part}")
    (out_dir / "index.md").write_text("\n".join(idx) + "\n")


# =============================================================================
# App docs — discovered from the apps/ tree
# =============================================================================

_SKILL_IGNORE_DIRS = {"_sdk", "_prototype", "agent-sdk", "bin", "node_modules", "__pycache__"}


def _parse_readme_frontmatter(text: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from a readme. Returns (meta, body)."""
    try:
        import yaml
    except ImportError:
        return {}, text
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text
    meta = yaml.safe_load(text[3:end]) or {}
    body = text[end + 4:].lstrip("\n")
    return (meta if isinstance(meta, dict) else {}), body


def _extract_returns(py_text: str) -> list[tuple[str, str]]:
    """Find @returns('shape') decorators over def/async-def. Returns [(func_name, shape), ...]."""
    import ast
    try:
        tree = ast.parse(py_text)
    except SyntaxError:
        return []
    out = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for dec in node.decorator_list:
                if isinstance(dec, ast.Call) and isinstance(dec.func, ast.Name) and dec.func.id == "returns":
                    if dec.args and isinstance(dec.args[0], ast.Constant) and isinstance(dec.args[0].value, str):
                        out.append((node.name, dec.args[0].value))
    return out


def discover_apps(apps_root: Path) -> list[dict]:
    """Walk apps/ looking for readme.md files. Return list of app records."""
    records = []
    for readme in apps_root.rglob("readme.md"):
        rel = readme.parent.relative_to(apps_root)
        parts = rel.parts
        if any(p in _SKILL_IGNORE_DIRS or p.startswith(".") for p in parts):
            continue
        if readme.parent == apps_root:
            continue
        text = readme.read_text()
        meta, body = _parse_readme_frontmatter(text)
        app_id = meta.get("id") or rel.name
        category = parts[0] if len(parts) > 1 else "misc"
        # Scan .py files for @returns shape names
        returns = {}  # shape → [func_name, ...]
        for py in readme.parent.glob("*.py"):
            for fn, shape in _extract_returns(py.read_text()):
                returns.setdefault(shape, []).append(fn)
        records.append({
            "app_id": app_id,
            "rel_path": str(rel),
            "category": category,
            "meta": meta,
            "body": body,
            "returns": returns,
        })
    return records


def emit_app_docs(apps: list[dict], out_dir: Path, known_shapes: set[str]) -> None:
    """Write one MDX file per app under `<category>/<id>.md` + an index page.

    Apps are laid out by **category** — the same taxonomy the apps/ tree
    uses on disk (comms/, web/, finance/, …). The sidebar mirrors this,
    giving agents a fast scan path: "where are the email apps?" → `comms/`.

    `known_shapes` is the set of shape names that have their own reference page;
    return-types outside this set (e.g. `void`) are rendered as plain code without
    a link so generated pages never produce dead `/shapes/reference/void/` URLs.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    # The output dir is wholly owned by this emitter — prune pages whose
    # app no longer exists, or a deleted app keeps a live docs page
    # forever.
    live: set[Path] = set()
    for rec in apps:
        cat_dir = out_dir / rec["category"] if rec["category"] else out_dir
        live.add(cat_dir / f"{rec['app_id']}.md")
        live.add(cat_dir / "index.md")
    live.add(out_dir / "index.md")
    for page in out_dir.rglob("*.md"):
        if page not in live:
            page.unlink()
    for sub in sorted(out_dir.glob("*/"), reverse=True):
        if sub.is_dir() and not any(sub.iterdir()):
            sub.rmdir()
    # Group apps by category so we can emit per-category index pages below.
    by_cat: dict[str, list[dict]] = {}
    for rec in apps:
        by_cat.setdefault(rec["category"], []).append(rec)
    for rec in apps:
        meta = rec["meta"]
        sid = rec["app_id"]
        name = meta.get("name", sid)
        desc = (meta.get("description") or "").replace('"', "'").strip()
        if len(desc) > 160:
            desc = desc[:157] + "..."

        lines = [
            "---",
            f"title: {name}",
            f'description: "{desc}"' if desc else f'description: "App reference for {sid}."',
            "sidebar:",
            f"  label: {sid}",
            "---",
            "",
        ]

        # Metadata table: category, services, website
        meta_rows = [("Category", f"`{rec['category']}`")]
        if meta.get("services"):
            caps = ", ".join(f"`{c}`" for c in meta["services"])
            meta_rows.append(("Services", caps))
        if meta.get("website"):
            meta_rows.append(("Website", f"<{meta['website']}>"))
        lines.append("| Metadata | Value |")
        lines.append("|---|---|")
        for k, v in meta_rows:
            lines.append(f"| **{k}** | {v} |")
        lines.append("")

        # Shapes produced
        if rec["returns"]:
            lines.append("## Returns shapes")
            lines.append("")
            for shape, fns in sorted(rec["returns"].items()):
                fn_list = ", ".join(f"`{fn}`" for fn in fns)
                bare = shape.rstrip("[]")
                if bare in known_shapes:
                    rendered = f"[`{shape}`](/shapes/reference/{bare}/)"
                else:
                    rendered = f"`{shape}`"
                lines.append(f"- {rendered} — from {fn_list}")
            lines.append("")

        # Connections block — just list connection names
        if meta.get("connections"):
            lines.append("## Connections")
            lines.append("")
            for cname, cval in meta["connections"].items():
                cdesc = cval.get("description") if isinstance(cval, dict) else ""
                if cdesc:
                    lines.append(f"- **`{cname}`** — {cdesc}")
                else:
                    lines.append(f"- **`{cname}`**")
            lines.append("")

        # Body (the agent-facing readme) — strip first H1 if any (title already in frontmatter)
        body = rec["body"].strip()
        if body.startswith("# "):
            body = body.split("\n", 1)[1].lstrip("\n") if "\n" in body else ""
        if body:
            lines.append("## Readme")
            lines.append("")
            lines.append(body)
            lines.append("")

        cat_dir = out_dir / rec["category"]
        cat_dir.mkdir(parents=True, exist_ok=True)
        (cat_dir / f"{sid}.md").write_text("\n".join(lines).rstrip() + "\n")

    # Top-level index — flat listing of all apps, grouped visually by category.
    idx = [
        "---",
        "title: Apps index",
        'description: "Every app in the AgentOS catalog. Browse all or filter by category."',
        "---",
        "",
        f"The AgentOS app catalog — **{len(apps)}** apps across **{len(by_cat)}** categories. Each app is a Python adapter that connects to a service or provides a pure agent tool.",
        "",
        "See [Apps → Overview](/apps/overview/) for how to build one.",
        "",
    ]
    for cat in sorted(by_cat.keys()):
        idx.append(f"## [{cat}](/apps/reference/{cat}/)")
        idx.append("")
        for rec in sorted(by_cat[cat], key=lambda r: r["app_id"]):
            name = rec["meta"].get("name", rec["app_id"])
            desc = (rec["meta"].get("description") or "").strip().rstrip(".")
            desc_part = f" — {desc}" if desc else ""
            idx.append(f"- [**{name}**](/apps/reference/{cat}/{rec['app_id']}/){desc_part}")
        idx.append("")
    (out_dir / "index.md").write_text("\n".join(idx) + "\n")

    # Per-category index pages — each category folder gets its own landing.
    for cat, recs in sorted(by_cat.items()):
        cat_lines = [
            "---",
            f"title: {cat}",
            f'description: "Apps in the {cat} category."',
            "sidebar:",
            "  label: Overview",
            "  order: -1",
            "---",
            "",
            f"**{len(recs)}** apps in `{cat}`.",
            "",
        ]
        for rec in sorted(recs, key=lambda r: r["app_id"]):
            name = rec["meta"].get("name", rec["app_id"])
            desc = (rec["meta"].get("description") or "").strip().rstrip(".")
            desc_part = f" — {desc}" if desc else ""
            cat_lines.append(f"- [**{name}**](/apps/reference/{cat}/{rec['app_id']}/){desc_part}")
        (out_dir / cat / "index.md").write_text("\n".join(cat_lines).rstrip() + "\n")


def build_apps_index(apps: list[dict], known_shapes: set[str]) -> dict[str, list[dict]]:
    """Invert apps list into shape-name → apps that produce it (arrays stripped).

    Only keeps entries for shapes that have a reference page (`known_shapes`).
    Operations from multiple SOPs of the same app are merged and deduped, so
    a app appears at most once per shape.
    """
    # shape -> { app_id -> {category, operations: [ordered unique]} }
    tmp: dict[str, dict[str, dict]] = {}
    for rec in apps:
        for shape in rec["returns"]:
            bare = shape.rstrip("[]")
            if bare not in known_shapes:
                continue
            bucket = tmp.setdefault(bare, {})
            entry = bucket.get(rec["app_id"])
            if entry is None:
                entry = {
                    "app_id": rec["app_id"],
                    "category": rec["category"],
                    "operations": [],
                }
                bucket[rec["app_id"]] = entry
            seen = set(entry["operations"])
            for op in rec["returns"][shape]:
                if op not in seen:
                    entry["operations"].append(op)
                    seen.add(op)

    idx: dict[str, list[dict]] = {
        shape: list(bucket.values()) for shape, bucket in tmp.items()
    }
    # Invariant: each app appears at most once per shape. If this trips,
    # bucket aggregation above has regressed.
    for shape, entries in idx.items():
        seen: set[str] = set()
        for e in entries:
            if e["app_id"] in seen:
                raise AssertionError(
                    f"build_apps_index: app {e['app_id']!r} listed twice for shape {shape!r}"
                )
            seen.add(e["app_id"])
    return idx
