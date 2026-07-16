"""agentOS app validator — single source of truth.

Static checks on agentOS apps, consolidated from what used to be two
parallel validators (`agentos/bin/audit-apps.py` and an older, thinner
`agentos-sdk/apps-sdk/agentos/validate.py`). Lives in the SDK so it
travels with the public surface it checks against — adding an
`async def foo` to `agentos/http.py` automatically updates what apps
are allowed to call, with no registry file to keep in sync.

App layout is `apps/<group>/<name>/readme.md + *.py` (nested — the
community repo groups apps by domain). Tool discovery is AST-based:
any top-level function decorated with an SDK decorator (`@returns`,
`@provides`, `@connection`, `@timeout`) is a tool, keyed by function
name. Filenames are irrelevant to routing.

What this script checks:

  1. **Frontmatter** — required fields (id, name), no unknown keys
     (with fuzzy suggestions), valid auth types.

  2. **Sandbox — banned imports.** Keep in sync with the runtime list
     in `crates/core/src/executors/python_worker.rs`. `urllib` is not
     banned by the worker but is banned here because apps should use
     `http.build_url`/`parse_url`/`encode`/`decode` for URL work.

  3. **SDK surface existence.** Any `http.foo(...)`, `sql.bar(...)`,
     etc. where `foo`/`bar` doesn't exist on the imported SDK module
     is a static error with a closest-match suggestion. Catches
     `http.request(...)` (doesn't exist — use `http.post`) and
     similar phantom methods that used to ship to main and blow up
     at runtime.

  4. **Missing `await` on async SDK calls.** Calls to SDK async
     functions (`http.get`, `sql.query`, …) or locally-defined
     `async def` helpers that aren't wrapped in an `Await` node,
     including sync parent functions that need to become async.

  5. **Sync sleep in async.** `time.sleep(...)` inside an `async def`
     blocks the event loop — use `await asyncio.sleep(...)`.

  6. **Tool name collisions** — no two decorated functions sharing a
     name across an app's `.py` files. The tool namespace is flat
     per app.

  7. **`@returns` required** on every public (non-underscore) function.

  8. **`**params` required** on every public function (engine injects
     auth/context via `params`).

  9. **Docstrings** — warning when missing.

  10. **Shape existence** with closest-match suggestions.

  11. **Shape conformance** — AST-extract dict keys from return
      statements, diff against the declared shape's fields, warn on
      missing identity fields and unknown extra keys. Follows shape
      `also:` inheritance chains.

  12. **Shape file validation** — relation targets exist, shapes with
      `platform` relations declare an `identity`.

  13. **camelCase enforcement** on dict keys that match a shape field.

  14. **Test-block op references** — every tool named in the readme
      `test:` block must correspond to a real function.

  15. **`params.get("params")` anti-pattern** — double-nesting bug.

  16. **Connection client kind** — `connection(..., client="X")` where
      `X` isn't one of `{"browser", "fetch", "api"}` is a static error.

  17. **Session connection domain** — a no-auth connection used by
      `@account.check` must declare `domain=` explicitly (browser-driven
      session identity namespace). `base_url` alone is not enough.

Run:
    agent-sdk validate                   # audit every app under cwd
    agent-sdk validate <app-dir>       # single app
    agent-sdk validate --all             # walk apps/ tree under cwd
    agent-sdk validate --sandbox         # only the banned-import check
    python -m agentos validate           # same, via module entry point

Exits 1 on any error. Warnings don't block.
"""

from __future__ import annotations

import ast
import difflib
import glob
import json
import os
import re
import sqlite3
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml


# ═══════════════════════════════════════════════════════════════════════════════
# Source discovery — local workspace + configured paths in ~/.agentos/data/agentos.db
# ═══════════════════════════════════════════════════════════════════════════════

AGENTOS_DB_PATH = Path.home() / ".agentos" / "data" / "agentos.db"


@dataclass
class AppSource:
    """One discovered apps+shapes+engine source.

    `origin` is either "workspace" (auto-discovered from CWD) or a configured
    source path from `settings.sources` in agentos.db. `apps_dir`,
    `shapes_dir`, and `crates_dir` are the on-disk directories to scan;
    any may be None if the source doesn't have that half.

    `crates_dir` points at the Rust engine's `core/crates/` so the orphan
    classifier can see `ensure_tag(...)` and `shapes::FOO` producers. Only
    the workspace-adjacent agentos repo has one.
    """
    origin: str                 # "workspace" | "configured"
    root: Path                  # the source path we were handed
    apps_dir: Path | None
    shapes_dir: Path | None
    crates_dir: Path | None = None
    exists: bool = True         # False when the configured path is missing on disk


def _read_configured_source_paths(db_path: Path = AGENTOS_DB_PATH) -> list[str]:
    """Read `settings.sources` from the engine's SQLite. Returns the raw paths
    as stored — no expansion, no existence check. Empty list when the DB is
    missing, locked, or the key is absent."""
    if not db_path.is_file():
        return []
    try:
        conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True, timeout=0.5)
    except sqlite3.Error:
        return []
    try:
        cur = conn.execute("SELECT value FROM settings WHERE key = 'sources'")
        row = cur.fetchone()
    except sqlite3.Error:
        conn.close()
        return []
    conn.close()
    if not row or not row[0]:
        return []
    try:
        parsed = json.loads(row[0])
    except (TypeError, json.JSONDecodeError):
        return []
    if not isinstance(parsed, list):
        return []
    return [str(p) for p in parsed if isinstance(p, str)]


def _write_configured_source_paths(paths: list[str], db_path: Path = AGENTOS_DB_PATH) -> bool:
    """Overwrite `settings.sources`. Returns True on success.

    Only called from the interactive `--fix-sources` flow — never from a
    regular validate run."""
    if not db_path.is_file():
        return False
    try:
        conn = sqlite3.connect(db_path, timeout=1.0)
        conn.execute(
            "INSERT INTO settings (key, value) VALUES ('sources', ?) "
            "ON CONFLICT(key) DO UPDATE SET value = excluded.value, updated_at = CURRENT_TIMESTAMP",
            (json.dumps(paths),),
        )
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error:
        return False


#  Where a shapes dir can conventionally live under a source root. Ordered —
# first match wins. `shapes/` is the canonical public location;
# `platform/ontology/shapes` is the agentos workspace layout.
_SHAPES_CANDIDATES = (
    "shapes",
    "platform/ontology/shapes",
    # Plugins now live in commons/plugins; shapes stay in the sibling
    # platform/ repo. When the source root is commons/, reach across to its sibling.
    "../platform/ontology/shapes",
    "agentos-sdk/shapes",
)


def _iter_shape_yamls(shapes_dir: Path) -> list[Path]:
    """Yield all shape YAMLs from a shapes dir, recursing one level into
    namespacing subdirs (e.g. `agentos/`) but skipping `_`-prefixed dirs
    (`_draft/`)."""
    if not shapes_dir or not shapes_dir.is_dir():
        return []
    files = list(shapes_dir.glob("*.yaml"))
    for sub in shapes_dir.iterdir():
        if sub.is_dir() and not sub.name.startswith("_"):
            files.extend(sub.glob("*.yaml"))
    return files


def _find_shape_yaml(shapes_dir: Path, name: str) -> Path:
    """Resolve a shape name to its YAML path, checking subdirs. Returns
    the bare top-level path if not found in any subdir (caller handles
    the `is_file` check)."""
    direct = shapes_dir / f"{name}.yaml"
    if direct.is_file():
        return direct
    for sub in shapes_dir.iterdir():
        if sub.is_dir() and not sub.name.startswith("_"):
            candidate = sub / f"{name}.yaml"
            if candidate.is_file():
                return candidate
    return direct


def _probe_source_root(root: Path, origin: str) -> AppSource:
    """Turn a source root into a AppSource record.

    A source root can contribute:
      - `<root>/plugins/` as a plugins dir (or the root itself, if it looks
        like a plugins dir)
      - A shapes dir at one of `_SHAPES_CANDIDATES` (conventional locations
        like `shapes/` or `platform/ontology/shapes/`).
    """
    root = root.expanduser()
    if not root.exists():
        return AppSource(origin=origin, root=root, apps_dir=None, shapes_dir=None, exists=False)

    root = root.resolve()
    apps: Path | None = None
    shapes: Path | None = None
    crates: Path | None = None

    # Plugins (contract bundles) live in `plugins/`; `apps/` was the old
    # home before the plugin/app split. A source that keeps its bundles at
    # the root (a single-plugin repo) is detected by the heuristic.
    candidate_apps = root / "plugins"
    if candidate_apps.is_dir():
        apps = candidate_apps
    elif _looks_like_apps_dir(root):
        apps = root

    for rel in _SHAPES_CANDIDATES:
        candidate = (root / rel).resolve()
        if candidate.is_dir() and any(candidate.glob("*.yaml")):
            shapes = candidate
            break

    # The engine lives at `<workspace>/core/crates/`. Only the agentos
    # workspace root has one — apps-only sources won't.
    candidate_crates = root / "core" / "crates"
    if candidate_crates.is_dir():
        crates = candidate_crates

    return AppSource(
        origin=origin, root=root, apps_dir=apps, shapes_dir=shapes,
        crates_dir=crates, exists=True,
    )


def _looks_like_apps_dir(d: Path) -> bool:
    """Heuristic: a directory is a apps root if it has at least one child
    containing a `readme.md` (direct or nested one level)."""
    if not d.is_dir():
        return False
    for child in d.iterdir():
        if not child.is_dir() or child.name.startswith("_"):
            continue
        if (child / "readme.md").is_file():
            return True
        for grandchild in child.iterdir():
            if grandchild.is_dir() and (grandchild / "readme.md").is_file():
                return True
    return False


def _discover_sources(explicit_apps_dir: Path | None = None) -> list[AppSource]:
    """Assemble every (apps, shapes) pair we should scan.

    Order:
      1. `explicit_apps_dir` (from a CLI target) or the auto-located workspace.
      2. Every path in `settings.sources` from the engine DB.
    Duplicates (same resolved path) are dropped while preserving order.
    """
    sources: list[AppSource] = []
    seen_roots: set[Path] = set()

    def _push(src: AppSource) -> None:
        key = src.root if src.exists else src.root.expanduser()
        if key in seen_roots:
            return
        seen_roots.add(key)
        sources.append(src)

    # Workspace — infer the root from the plugins dir (one level up if
    # plugins/ is a subdir, else use the dir itself), then probe for shapes
    # under the root's conventional locations.
    workspace_apps = explicit_apps_dir or _find_apps_dir()
    if workspace_apps:
        workspace_apps = workspace_apps.resolve()
        workspace_root = (
            workspace_apps.parent
            if workspace_apps.name == "plugins"
            else workspace_apps
        )
        ws = _probe_source_root(workspace_root, origin="workspace")
        # Respect the caller-provided apps dir if they passed an explicit one.
        if explicit_apps_dir:
            ws.apps_dir = workspace_apps
        # Fallback to the original env-based finder if probing missed shapes.
        if ws.shapes_dir is None:
            ws.shapes_dir = _find_shapes_dir(workspace_apps)
        _push(ws)

    for raw in _read_configured_source_paths():
        _push(_probe_source_root(Path(raw), origin="configured"))

    return sources


def _print_sources_banner(sources: list[AppSource]) -> None:
    """Print the `Sources:` block shown at the top of every validate run."""
    print("Sources:")
    label_w = max((len(s.origin) for s in sources), default=9)
    for src in sources:
        label = f"{src.origin:<{label_w}}"
        if not src.exists:
            print(f"  {label}  {src.root}  ⚠ not found")
            continue
        apps_str = (
            f"apps={src.apps_dir.relative_to(src.root) if src.apps_dir and src.apps_dir.is_relative_to(src.root) else src.apps_dir}"
            if src.apps_dir else "apps=—"
        )
        shapes_str = (
            f"shapes={src.shapes_dir.relative_to(src.root) if src.shapes_dir and src.shapes_dir.is_relative_to(src.root) else src.shapes_dir}"
            if src.shapes_dir else "shapes=—"
        )
        engine_str = (
            f"engine={src.crates_dir.relative_to(src.root) if src.crates_dir and src.crates_dir.is_relative_to(src.root) else src.crates_dir}"
            if src.crates_dir else "engine=—"
        )
        print(f"  {label}  {src.root}")
        print(f"  {' ' * label_w}    {apps_str}    {shapes_str}    {engine_str}")


# ═══════════════════════════════════════════════════════════════════════════════
# Interactive source cleanup (--fix-sources)
# ═══════════════════════════════════════════════════════════════════════════════

def _fix_sources_interactive() -> int:
    """Show dead entries in `settings.sources`, propose removals, apply on confirm.

    Read-only until the user answers 'y'. Prints the full proposed add/remove
    diff and the final list before writing. Exit codes mirror bash: 0 = clean
    or user-confirmed, 1 = nothing to fix or aborted."""
    raw = _read_configured_source_paths()
    if not raw:
        print("settings.sources is empty or not set — nothing to fix.")
        return 0

    missing: list[str] = []
    kept: list[str] = []
    for p in raw:
        if Path(p).expanduser().exists():
            kept.append(p)
        else:
            missing.append(p)

    print("settings.sources audit")
    print(f"  db: {AGENTOS_DB_PATH}")
    print(f"  current: {raw}")
    print()
    for p in raw:
        ok = p in kept
        marker = "✓" if ok else "✗"
        note = "" if ok else " (does not exist)"
        print(f"  {marker} {p}{note}")

    if not missing:
        print("\nAll sources exist — nothing to remove.")
        return 0

    print()
    print("Proposed change:")
    for p in missing:
        print(f"  - {p}")
    print()
    print(f"New value: {json.dumps(kept)}")
    print()
    try:
        answer = input("Apply this change? [y/N] ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print("\nAborted.")
        return 1
    if answer != "y":
        print("Aborted — no changes made.")
        return 1

    if _write_configured_source_paths(kept):
        print(f"✓ Updated settings.sources → {kept}")
        return 0
    print("✗ Failed to write settings.sources (is the engine holding the DB?).")
    return 1


# ═══════════════════════════════════════════════════════════════════════════════
# Paths — resolved at runtime so the validator works from multiple CWDs
# (community repo root, engine repo root, SDK repo root).
# ═══════════════════════════════════════════════════════════════════════════════

# Where this file lives — the SDK package directory. Used for the SDK
# surface registry (we walk our own siblings to enumerate the public API).
_SDK_PACKAGE_DIR = Path(__file__).resolve().parent


def _find_apps_dir(start: Path | None = None) -> Path | None:
    """Locate the apps/ directory to audit.

    Resolution order:
      1. AGENTOS_APPS_DIR env var
      2. Walk up from <start> looking for a plugins home that contains
         readme.md files — either `<base>/plugins` or `<base>/commons/plugins`
         (plugins ship under commons/ alongside themes/ + wallpapers/).
    """
    env = os.environ.get("AGENTOS_APPS_DIR")
    if env:
        p = Path(env).expanduser().resolve()
        if p.is_dir():
            return p

    start = (start or Path.cwd()).resolve()

    def _has_apps(d: Path) -> bool:
        if not d.is_dir():
            return False
        # Either a direct readme.md subdir, or a nested group/app/readme.md.
        for child in d.iterdir():
            if not child.is_dir():
                continue
            if (child / "readme.md").is_file():
                return True
            for grandchild in child.iterdir():
                if grandchild.is_dir() and (grandchild / "readme.md").is_file():
                    return True
        return False

    for base in [start, *start.parents]:
        for candidate in (base / "plugins", base / "commons" / "plugins"):
            if _has_apps(candidate):
                return candidate

    return None


def _find_shapes_dir(start: Path | None = None) -> Path | None:
    """Locate the shapes/ directory.

    Resolution order:
      1. AGENT_SHAPES_DIR / SHAPES_DIR env var
      2. Walk up from <start> for `shapes/event.yaml`
      3. Walk up for `agentos-sdk/shapes/event.yaml`
    """
    env = os.environ.get("AGENT_SHAPES_DIR") or os.environ.get("SHAPES_DIR")
    if env:
        p = Path(env).expanduser().resolve()
        if p.is_dir():
            return p

    # SDK self-location: shapes/ is two levels up from this file
    # (apps-sdk/agentos/validate.py → ../../shapes).
    sdk_shapes = _SDK_PACKAGE_DIR.parent.parent / "shapes"
    if (sdk_shapes / "event.yaml").is_file():
        return sdk_shapes

    start = (start or Path.cwd()).resolve()
    for base in [start, *start.parents]:
        candidate = base / "shapes"
        if (candidate / "event.yaml").is_file():
            return candidate
        candidate = base / "agentos-sdk" / "shapes"
        if (candidate / "event.yaml").is_file():
            return candidate

    return None


# ═══════════════════════════════════════════════════════════════════════════════
# Sandbox: banned imports
#
# Keep in sync with crates/core/src/executors/python_worker.rs. The runtime
# sandbox bans the first set; we additionally ban `urllib`/`requests`/`httpx`
# at commit time because those should route through SDK modules.
# ═══════════════════════════════════════════════════════════════════════════════

BANNED_IMPORTS: dict[str, str] = {
    # Runtime-sandboxed (mirror of python_worker.rs)
    "subprocess":      "agentos.shell.run()",
    "sqlite3":         "agentos.sql.query()",
    "httpx":           "agentos.client (client.get/post/…)",
    "requests":        "agentos.client (client.get/post/…)",
    "urllib3":         "agentos.client (client.get/post/…)",
    "aiohttp":         "agentos.client (client.get/post/…)",
    "socket":          "an SDK module (no raw sockets in apps)",
    "ctypes":          "an SDK module (no FFI in apps)",
    "multiprocessing": "the engine's own task scheduling",
    "signal":          "an SDK module (no signal handling in apps)",
    # Validator-only (not worker-banned but forbidden in app code):
    "urllib":          "agentos.url (build/parse/encode/decode) or client params=",
}


# ═══════════════════════════════════════════════════════════════════════════════
# Frontmatter schema
# ═══════════════════════════════════════════════════════════════════════════════

REQUIRED_FRONTMATTER = {"id", "name"}
KNOWN_FRONTMATTER = {
    "id", "name", "description", "color", "website",
    "privacy_url", "terms_url", "product",
    "test", "tools", "sources", "accounts",
    "services", "privileges",
}
# Frontmatter keys that used to be allowed but have moved into Python:
# - `connections` → module-level `connection("name", ...)` calls
# - `operations` → renamed to `tools` and superseded by @returns decorators
DEPRECATED_FRONTMATTER = {
    "connections": (
        "declare connections at module level in .py files via "
        "connection(\"name\", ...) — YAML connections: is no longer read"
    ),
    "operations": (
        "rename to `tools` and use @returns decorators in .py files"
    ),
}
# ═══════════════════════════════════════════════════════════════════════════════
# Shape conformance: constants
# ═══════════════════════════════════════════════════════════════════════════════

# Standard fields available on every shape without being declared.
STANDARD_FIELDS = {
    "id", "name", "text", "url", "image", "author", "published",
    "platform",
}

# The content-pipeline trio — a node's *body*, not a val. The engine
# consumes these in `prepare_node_data` and routes them to the content
# table (`extraction.rs` skips them when building vals), so they're
# universal to every shape and never declared per-shape: `content` is the
# bytes, `content_role` their role (default "body"), `content_mime` their
# declared type (default text/markdown). Any node can carry a typed body.
CONTENT_FIELDS = {"content", "content_role", "content_mime"}

# Internal fields the engine uses that aren't shape fields.
#
# `authenticated` is `check_session`'s runtime freshness signal — the
# engine consumes it to decide whether to persist + trigger auto-login,
# never lands it on the account node (per `plan.md` Decision 3).
SYSTEM_RETURN_FIELDS = {"_source", "error", "authenticated"}

# @returns values that aren't shape names — primitives, informal hints,
# or inline dicts (handled separately).
_NON_SHAPE_RETURNS = {
    "void", "null", "string", "integer", "number", "boolean", "array", "object", "any",
}

# Decorators that mark a function as a tool. The engine reads these via AST.
_TOOL_MARKER_DECORATORS = {"returns", "provides", "connection", "timeout", "claims"}

# `@account.<role>` decorator roles — the account protocol's declaration
# point. The engine resolves an app's check/login/logout/profile ops from
# these, never from literal tool names.
_ACCOUNT_ROLES = {"check", "login", "logout", "profile"}

# snake_case pattern — flagged only when camelCase version is a known shape field
_SNAKE_RE = re.compile(r"^[a-z]+_[a-z]")


# ═══════════════════════════════════════════════════════════════════════════════
# SDK surface registry — single source of truth for what apps can call
#
# We walk this very package (`agentos/`) at validation time and harvest every
# public top-level `def`, `async def`, and class from every module. Apps
# referencing `http.foo` are then statically checked: `foo` must exist on
# the `http` module. Missing → error with a closest-match suggestion.
# ═══════════════════════════════════════════════════════════════════════════════

# Modules we ignore when scanning the SDK — CLI, codegen, validators, docs,
# and any helper that isn't part of the runtime app API.
_SDK_SCAN_SKIP = {
    "cli", "scaffold", "shape_cli", "guide", "validate", "tools",
    "checkpoint", "dates", "text", "decorators", "shapes",
    "__main__", "_bridge", "_generated",
}

_sdk_surface_cache: dict[str, dict[str, set[str]]] | None = None


def _load_sdk_surface() -> dict[str, dict[str, set[str]]]:
    """Scan this SDK package and return:

        {
          module_name: {
            "all":   {every public name — def, async def, class, assignment},
            "async": {every async def name},
          },
          ...
        }

    `module_name` is the filename stem for top-level files (`http` for
    `http.py`) and for subpackage files (`keychain` for `macos/keychain.py`).
    Subpackage modules are registered by stem so `keychain.read(...)`
    matches regardless of how the app imported it.
    """
    global _sdk_surface_cache
    if _sdk_surface_cache is not None:
        return _sdk_surface_cache

    registry: dict[str, dict[str, set[str]]] = {}

    def _register(module_name: str, tree: ast.Module) -> None:
        entry = registry.setdefault(module_name, {"all": set(), "async": set()})
        for node in tree.body:  # top-level only — the public surface
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if node.name.startswith("_"):
                    continue
                entry["all"].add(node.name)
                if isinstance(node, ast.AsyncFunctionDef):
                    entry["async"].add(node.name)
            elif isinstance(node, ast.ClassDef):
                if not node.name.startswith("_"):
                    entry["all"].add(node.name)
            elif isinstance(node, ast.Assign):
                for tgt in node.targets:
                    if isinstance(tgt, ast.Name) and not tgt.id.startswith("_"):
                        entry["all"].add(tgt.id)
            elif isinstance(node, ast.AnnAssign):
                if isinstance(node.target, ast.Name) and not node.target.id.startswith("_"):
                    entry["all"].add(node.target.id)

    if not _SDK_PACKAGE_DIR.is_dir():
        _sdk_surface_cache = registry
        return registry

    for root, dirs, files in os.walk(_SDK_PACKAGE_DIR):
        # Skip private/dunder subdirectories and shape data.
        dirs[:] = [d for d in dirs if not d.startswith("_") and d not in {"shapes"}]
        for fname in files:
            if not fname.endswith(".py") or fname.startswith("_"):
                continue
            module_name = fname[:-3]
            if module_name in _SDK_SCAN_SKIP:
                continue
            try:
                with open(os.path.join(root, fname), encoding="utf-8") as f:
                    tree = ast.parse(f.read())
            except (SyntaxError, UnicodeDecodeError):
                continue
            _register(module_name, tree)

    _sdk_surface_cache = registry
    return registry


def _sdk_async_modules() -> dict[str, set[str]]:
    """Convenience view: `{module_name: {async_fn, ...}}` for the await check."""
    return {m: entry["async"] for m, entry in _load_sdk_surface().items() if entry["async"]}


# ═══════════════════════════════════════════════════════════════════════════════
# Shape registry
# ═══════════════════════════════════════════════════════════════════════════════

def _load_known_shapes(shapes_dir: Path) -> set[str]:
    """Return the set of shape names (filenames without .yaml) from shapes_dir."""
    return {p.stem for p in _iter_shape_yamls(shapes_dir)}


def _load_shape_identity(shapes_dir: Path, shape_name: str) -> list[str] | None:
    """Load identity keys for a shape, following `also` chains."""
    if not shapes_dir:
        return None
    visited: set[str] = set()
    queue = [shape_name]
    while queue:
        current = queue.pop(0)
        if current in visited:
            continue
        visited.add(current)
        path = _find_shape_yaml(shapes_dir, current)
        if not path.is_file():
            continue
        try:
            obj = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError:
            continue
        if not isinstance(obj, dict):
            continue
        body = obj.get(current, obj)
        if not isinstance(body, dict):
            continue
        identity = body.get("identity")
        if isinstance(identity, list):
            return identity
        if isinstance(identity, str):
            return [identity]
        also = body.get("also", [])
        if isinstance(also, list):
            queue.extend(also)
        elif isinstance(also, str):
            queue.append(also)
    return None



def _load_shape_fields(shapes_dir: Path, shape_name: str) -> tuple[set[str], set[str]] | None:
    """Load (fields, relations) for a shape, following `also` chains."""
    if not shapes_dir:
        return None
    fields: set[str] = set()
    relations: set[str] = set()
    visited: set[str] = set()
    queue = [shape_name]
    while queue:
        current = queue.pop(0)
        if current in visited:
            continue
        visited.add(current)
        path = _find_shape_yaml(shapes_dir, current)
        if not path.is_file():
            if current == shape_name:
                return None
            continue
        try:
            obj = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError:
            if current == shape_name:
                return None
            continue
        if not isinstance(obj, dict):
            if current == shape_name:
                return None
            continue
        body = obj.get(current, obj)
        if not isinstance(body, dict):
            if current == shape_name:
                return None
            continue
        if isinstance(body.get("fields"), dict):
            fields.update(body["fields"].keys())
        if isinstance(body.get("relations"), dict):
            relations.update(body["relations"].keys())
        also = body.get("also", [])
        if isinstance(also, list):
            queue.extend(also)
        elif isinstance(also, str):
            queue.append(also)
    return (fields, relations)


def validate_shape_file(shape_name: str, yaml_obj: dict, known_shapes: set[str]) -> tuple[list, list]:
    """Validate a single shape YAML file."""
    issues: list[str] = []
    warnings: list[str] = []
    if not isinstance(yaml_obj, dict):
        return issues, warnings
    body = yaml_obj.get(shape_name, yaml_obj)
    if not isinstance(body, dict):
        return issues, warnings
    relations = body.get("relations", {})
    if not isinstance(relations, dict):
        return issues, warnings
    for field, type_val in relations.items():
        if not isinstance(type_val, str):
            continue
        target = type_val.strip().split()[0].rstrip("[]").rstrip()
        # `node` is the universal relation target — any addressable graph node.
        # No corresponding YAML; codegen emits Any/unknown/AnyCodable in SDKs.
        if target == "node":
            continue
        if target and target not in known_shapes:
            issues.append(
                f"  relations.{field}: target shape '{target}' does not exist "
                f"in shapes/ — extraction will silently no-op"
            )
    identity = body.get("identity")
    if "platform" in relations and identity is None:
        warnings.append(
            "  has 'platform' relation but no identity — "
            "extraction can't dedup by platform. Add identity: [platform, id] or similar"
        )
    display = body.get("display") or {}
    if not isinstance(display, dict) or not display.get("icon"):
        warnings.append(
            "  missing display.icon — add a Material Symbols glyph name under display:"
        )
    return issues, warnings


def audit_shape_file(shape_path: Path, known_shapes: set[str]) -> int:
    shape_name = shape_path.stem
    try:
        yaml_obj = yaml.safe_load(shape_path.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        print(f"\n[shape:{shape_name}]")
        print(f"  ✗ parse error: {e}")
        return 1
    issues, warnings = validate_shape_file(shape_name, yaml_obj or {}, known_shapes)
    if issues or warnings:
        print(f"\n[shape:{shape_name}]")
        for issue in issues:
            print(f"  ✗ {issue}")
        for warn in warnings:
            print(f"  ⚠ {warn}")
    return len(issues)


def _collect_produced_shapes(apps_roots: list[Path]) -> set[str]:
    """Walk every app root and return the set of shape names that any
    tool function declares via `@returns("shape")` or `@returns("shape[]")`.

    Skips the `_sdk` SDK package itself and any generated helpers so the
    SDK's own decorators don't count as producers.
    """
    produced: set[str] = set()
    for root in apps_roots:
        if not root or not root.is_dir():
            continue
        for app_dir in discover_app_roots(root):
            for _rel, _py_file, _source, tree in _iter_app_py_files(app_dir):
                for node in tree.body:
                    if not _is_tool_function(node):
                        continue
                    produced.update(_tool_return_shapes(node))
    return produced


def _expand_produced_via_inheritance(
    produced: set[str],
    shapes_roots: list[Path],
) -> set[str]:
    """Given the set of directly-returned shapes, expand it across `also:`
    chains. Returning `book` means `product` is also effectively produced
    (if `book` has `also: [product]`).

    We search every shapes root in order and cache file lookups so a shape
    defined in multiple sources prefers the earliest one.
    """
    index: dict[str, Path] = {}
    for root in shapes_roots:
        for path in _iter_shape_yamls(root):
            index.setdefault(path.stem, path)

    def _also_of(shape: str) -> list[str]:
        path = index.get(shape)
        if not path:
            return []
        try:
            obj = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError:
            return []
        body = obj.get(shape, obj) if isinstance(obj, dict) else {}
        if not isinstance(body, dict):
            return []
        also = body.get("also", [])
        if isinstance(also, str):
            return [also]
        if isinstance(also, list):
            return [a for a in also if isinstance(a, str)]
        return []

    expanded = set(produced)
    queue = list(produced)
    while queue:
        current = queue.pop()
        for parent in _also_of(current):
            if parent not in expanded:
                expanded.add(parent)
                queue.append(parent)
    return expanded


def check_orphan_shapes(
    apps_roots: list[Path],
    shapes_roots: list[Path],
    crates_roots: list[Path] | None = None,
) -> int:
    """Warn for every shape that has no producer and no reference.

    A shape is an **orphan** only when *all* of these are empty:
      - app producers (`@returns("foo")` in Python)
      - engine producers (`ensure_tag("foo")` / `shapes::FOO` in Rust)
      - `relations:` targets from other shapes
      - embedded field types in other shapes
      - `also:` inheritance parents

    Uses `classify_orphans.classify(...)` as the single source of truth.
    Apps-only producer context (no engine) falls back silently if the
    Rust crates tree isn't on disk.

    Warnings only — returns 0 regardless.
    """
    try:
        from agentos.classify_orphans import classify
    except ImportError:
        from classify_orphans import classify  # type: ignore[no-redef]

    # One pass per configured shapes root — report once per shape, first-wins
    # on the source file when the same name appears in multiple roots.
    reported: set[str] = set()
    for root in shapes_roots:
        if not root or not root.is_dir():
            continue

        records = classify(
            shapes_dir=root,
            apps_roots=apps_roots,
            crates_roots=crates_roots,
        )

        # Sentinel: `_draft/__test.yaml` defines a shape called `__test`.
        # If any scanner ever starts recursing into `_`-prefixed subdirs,
        # this name will appear in the classified set and the validator
        # will surface it. Either something is loading draft YAMLs that
        # shouldn't be, or the sentinel file has been renamed — both are
        # bugs worth stopping on.
        if "__test" in records:
            print()
            print(
                f"✗ FATAL: `__test` from {root}/_draft/ leaked into the "
                "shape registry. A scanner is recursing into `_`-prefixed "
                "subdirectories — find it and switch to non-recursive glob."
            )
            return 1

        orphans = sorted(
            (r for r in records.values() if r.is_orphan),
            key=lambda r: r.name,
        )

        fresh = [r for r in orphans if r.name not in reported]
        if not fresh:
            continue

        reported.update(r.name for r in fresh)

        print()
        print(
            f"--- Orphan shapes ({len(fresh)} of {len(records)} defined in {root}) ---"
        )
        for rec in fresh:
            path = _find_shape_yaml(root, rec.name)
            print(f"\n[shape:{rec.name}]")
            print(f"  ⚠ no producer, no reference (defined in {path})")
            print(
                f"    → add @returns(\"{rec.name}\") to an app, "
                "reference it from another shape, or move to shapes/_draft/"
            )

    return 0


# ═══════════════════════════════════════════════════════════════════════════════
# AST helpers: tool discovery + return-key extraction
# ═══════════════════════════════════════════════════════════════════════════════

def _decorator_name(dec: ast.AST) -> str | None:
    """Extract the callable name from a decorator node.

    Handles @foo, @foo(...), @pkg.foo, @pkg.foo(...).
    """
    target = dec.func if isinstance(dec, ast.Call) else dec
    if isinstance(target, ast.Name):
        return target.id
    if isinstance(target, ast.Attribute):
        return target.attr
    return None


def _account_role(node: ast.FunctionDef | ast.AsyncFunctionDef) -> str | None:
    """Return the role when the function is decorated `@account.<role>`.

    Matches the bare-attribute form only (`@account.login`, not
    `@account.login(...)`) — that is the decorator's one shape. The
    `account.` qualifier is required so an unrelated `@foo.login` never
    matches.
    """
    for dec in node.decorator_list:
        if (
            isinstance(dec, ast.Attribute)
            and isinstance(dec.value, ast.Name)
            and dec.value.id == "account"
            and dec.attr in _ACCOUNT_ROLES
        ):
            return dec.attr
    return None


def _op_connection(node: ast.FunctionDef | ast.AsyncFunctionDef) -> str | None:
    """The default connection a tool binds to — the first arg of its
    `@connection(...)` decorator (a bare string, or the first of a list).
    Returns None when the tool declares no connection."""
    for dec in node.decorator_list:
        func = dec.func if isinstance(dec, ast.Call) else dec
        name = (
            func.id if isinstance(func, ast.Name)
            else func.attr if isinstance(func, ast.Attribute)
            else None
        )
        if name == "connection" and isinstance(dec, ast.Call) and dec.args:
            arg = dec.args[0]
            if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                return arg.value
            if (
                isinstance(arg, ast.List)
                and arg.elts
                and isinstance(arg.elts[0], ast.Constant)
                and isinstance(arg.elts[0].value, str)
            ):
                return arg.elts[0].value
    return None


def _is_tool_function(node: ast.AST) -> bool:
    """True if a top-level function is a tool (decorated + not underscore-prefixed)."""
    if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        return False
    if node.name.startswith("_"):
        return False
    for dec in node.decorator_list:
        if _decorator_name(dec) in _TOOL_MARKER_DECORATORS:
            return True
    return _account_role(node) is not None


def _tool_return_shapes(node: ast.FunctionDef | ast.AsyncFunctionDef) -> list[str]:
    """Extract the shape name(s) from @returns(...) on a tool function.

    Returns:
        - [shape] (brackets stripped) for `@returns("shape")`, `@returns("shape[]")`
        - one entry per arm for a union — `@returns("account | auth_challenge")`;
          the worker discriminates which arm a given call returned
        - [] if @returns is absent, uses an inline dict schema, or returns
          only non-shape primitives
    """
    for dec in node.decorator_list:
        if not isinstance(dec, ast.Call):
            continue
        if _decorator_name(dec) != "returns":
            continue
        if not dec.args:
            continue
        arg = dec.args[0]
        if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
            arms = [a.strip().rstrip("[]").rstrip() for a in arg.value.split("|")]
            return [a for a in arms if a and a not in _NON_SHAPE_RETURNS]
        # inline dict schema → not a shape reference
        return []
    return []


def _has_returns_decorator(node: ast.FunctionDef | ast.AsyncFunctionDef) -> bool:
    """True if function has any @returns decorator (shape or inline dict)."""
    for dec in node.decorator_list:
        if _decorator_name(dec) == "returns":
            return True
    return False


def _extract_dict_keys(node: ast.AST) -> set[str] | None:
    """Extract string keys from a dict literal or list-of-dicts comprehension."""
    if isinstance(node, ast.Dict):
        keys: set[str] = set()
        for key in node.keys:
            if isinstance(key, ast.Constant) and isinstance(key.value, str):
                keys.add(key.value)
        return keys if keys else None
    if isinstance(node, ast.ListComp) and isinstance(node.elt, ast.Dict):
        return _extract_dict_keys(node.elt)
    return None


def _extract_listcomp_helper_keys(node: ast.ListComp, tree: ast.AST) -> set[str] | None:
    """Follow [_helper(x) for x in items] to find the helper's return keys."""
    elt = node.elt
    if isinstance(elt, ast.Dict):
        return _extract_dict_keys(elt)
    if isinstance(elt, ast.Call) and isinstance(elt.func, ast.Name):
        return _extract_return_keys_from_function(tree, elt.func.id)
    return None


def _extract_return_keys_from_function(tree: ast.AST, function_name: str) -> set[str] | None:
    """Walk a named function's AST and collect dict keys from its return statements.

    Handles:
        return {"k": ...}                 — direct dict literal
        result = {...}; return result     — variable-assigned dict
        result["k"] = v; return result    — subscript assignment
        return [helper(x) for x in items] — follows helper function returns
    """
    func_node: ast.AST | None = None
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == function_name:
            func_node = node
            break
    if func_node is None:
        return None

    var_dicts: dict[str, set[str]] = {}
    for child in ast.walk(func_node):
        if isinstance(child, ast.Assign) and len(child.targets) == 1:
            target = child.targets[0]
            if isinstance(target, ast.Name):
                dict_keys = _extract_dict_keys(child.value)
                if dict_keys is not None:
                    var_dicts.setdefault(target.id, set()).update(dict_keys)
            if (isinstance(target, ast.Subscript) and isinstance(target.value, ast.Name)
                    and isinstance(target.slice, ast.Constant) and isinstance(target.slice.value, str)):
                var_dicts.setdefault(target.value.id, set()).add(target.slice.value)
        if isinstance(child, ast.AnnAssign) and isinstance(child.target, ast.Name) and child.value:
            dict_keys = _extract_dict_keys(child.value)
            if dict_keys is not None:
                var_dicts.setdefault(child.target.id, set()).update(dict_keys)

    keys: set[str] = set()
    for child in ast.walk(func_node):
        if isinstance(child, ast.Return) and child.value is not None:
            dict_keys = _extract_dict_keys(child.value)
            if dict_keys is not None:
                keys.update(dict_keys)
            elif isinstance(child.value, ast.Name) and child.value.id in var_dicts:
                keys.update(var_dicts[child.value.id])
            elif isinstance(child.value, ast.ListComp):
                helper_keys = _extract_listcomp_helper_keys(child.value, tree)
                if helper_keys:
                    keys.update(helper_keys)
    return keys if keys else None


def _module_nested_consts(tree: ast.AST) -> set[str]:
    """Module-level names bound to a dict/list literal (`_HN = {...}`). A return
    key whose value references one of these (`at: _HN`) is an edge child, not a
    scalar field."""
    names: set[str] = set()
    for node in getattr(tree, "body", []):
        if isinstance(node, ast.Assign) and isinstance(node.value, (ast.Dict, ast.List)):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name):
                    names.add(tgt.id)
    return names


def _is_nested_value(v: ast.AST, const_names: set[str]) -> bool:
    """True when a dict-value represents a nested entity (an edge child) or a
    json blob rather than a scalar field — a dict, a list/comprehension, a
    `<dict> if cond else <...>`, or a reference to a module-level dict/list
    const. Edges are open-world, so such keys are never flagged as undeclared
    shape fields."""
    if isinstance(v, (ast.Dict, ast.List, ast.ListComp, ast.DictComp)):
        return True
    if isinstance(v, ast.IfExp):
        return _is_nested_value(v.body, const_names) or _is_nested_value(v.orelse, const_names)
    if isinstance(v, ast.Name):
        return v.id in const_names
    return False


def _extract_nested_value_keys(tree: ast.AST, function_name: str) -> set[str]:
    """Keys in a function's return dicts whose value is a nested entity (edge)
    rather than a scalar field. Follows the same reach as
    `_extract_return_keys_from_function` — the tool fn itself plus any helper it
    returns via `[_helper(x) for x in …]` (where the dict is actually built) —
    and recognizes module-level dict/list consts (`at: _HN`)."""
    const_names = _module_nested_consts(tree)

    def _find_fn(name: str) -> ast.AST | None:
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == name:
                return node
        return None

    root = _find_fn(function_name)
    if root is None:
        return set()
    # The tool fn plus any list-comprehension helper it returns — that helper is
    # where map-style apps build the actual dict (`return [_map_hit(h) for …]`).
    fns = [root]
    for child in ast.walk(root):
        if isinstance(child, ast.Return) and isinstance(child.value, ast.ListComp):
            elt = child.value.elt
            if isinstance(elt, ast.Call) and isinstance(elt.func, ast.Name):
                helper = _find_fn(elt.func.id)
                if helper is not None:
                    fns.append(helper)

    nested: set[str] = set()
    for fn in fns:
        for child in ast.walk(fn):
            if isinstance(child, ast.Dict):
                for k, v in zip(child.keys, child.values):
                    if (isinstance(k, ast.Constant) and isinstance(k.value, str)
                            and _is_nested_value(v, const_names)):
                        nested.add(k.value)
    return nested


def _iter_app_py_files(app_dir: Path):
    """Yield (rel_path, absolute_path, source, tree) for every live .py file.

    Skips `_underscore_prefixed` trees (prototypes/scratchpads) and `vendor/`.
    """
    for py_file in sorted(glob.glob(os.path.join(str(app_dir), "**", "*.py"), recursive=True)):
        rel = os.path.relpath(py_file, app_dir)
        if rel.startswith("_") or "/_" in rel or "/vendor/" in rel:
            continue
        try:
            with open(py_file, encoding="utf-8") as f:
                source = f.read()
            tree = ast.parse(source, filename=py_file)
        except (SyntaxError, UnicodeDecodeError):
            continue
        yield rel, py_file, source, tree


# ═══════════════════════════════════════════════════════════════════════════════
# Frontmatter parsing
# ═══════════════════════════════════════════════════════════════════════════════

def _parse_frontmatter(readme_path: Path) -> tuple[dict | None, list[str]]:
    """Parse YAML frontmatter from readme.md. Returns (data, errors)."""
    errors: list[str] = []
    try:
        text = readme_path.read_text()
    except Exception as e:  # noqa: BLE001
        return None, [f"cannot read readme.md: {e}"]

    stripped = text.lstrip()
    if not stripped.startswith("---"):
        return None, ["readme.md has no YAML frontmatter (must start with ---)"]

    # Find the closing --- after the opening one.
    end_marker = text.find("\n---", text.find("---") + 3)
    if end_marker == -1:
        return None, ["readme.md frontmatter not closed (missing second ---)"]

    fm_text = text[text.find("---") + 3:end_marker]
    try:
        data = yaml.safe_load(fm_text)
    except yaml.YAMLError as e:
        return None, [f"invalid YAML in frontmatter: {e}"]

    if data is None:
        data = {}
    if not isinstance(data, dict):
        return None, ["frontmatter is not a YAML mapping"]

    return data, errors


def _check_frontmatter(data: dict) -> tuple[list[str], list[str]]:
    """Validate frontmatter fields. Returns (errors, warnings)."""
    errors: list[str] = []
    warnings: list[str] = []

    # Required fields
    for key in REQUIRED_FRONTMATTER:
        if key not in data:
            errors.append(f"missing required frontmatter field: {key}")

    # Unknown keys
    for key in data:
        if key in DEPRECATED_FRONTMATTER:
            errors.append(
                f"frontmatter field '{key}' is no longer supported — "
                f"{DEPRECATED_FRONTMATTER[key]}"
            )
        elif key not in KNOWN_FRONTMATTER:
            closest = difflib.get_close_matches(key, KNOWN_FRONTMATTER, n=1, cutoff=0.6)
            hint = f" (did you mean '{closest[0]}'?)" if closest else ""
            warnings.append(f"unknown frontmatter field: '{key}'{hint}")

    return errors, warnings


def check_readme_frontmatter(app_dir: Path) -> tuple[list[str], list[str], str | None, dict | None]:
    """Parse readme.md frontmatter. Returns (issues, warnings, app_id, fm_data)."""
    issues: list[str] = []
    warnings: list[str] = []
    readme_path = app_dir / "readme.md"
    if not readme_path.is_file():
        issues.append("missing readme.md — every app needs a readme with YAML frontmatter")
        return issues, warnings, None, None

    fm_data, fm_errors = _parse_frontmatter(readme_path)
    issues.extend(fm_errors)
    if fm_data is None:
        return issues, warnings, None, None

    fm_issues, fm_warnings = _check_frontmatter(fm_data)
    issues.extend(fm_issues)
    warnings.extend(fm_warnings)

    # Body-level warnings
    text = readme_path.read_text(encoding="utf-8")
    end_marker = text.find("\n---", text.find("---") + 3)
    body = text[end_marker + 4:] if end_marker >= 0 else ""
    if re.search(r"use\(\s*\{\s*app:", body):
        warnings.append(
            "readme body contains stale use() examples — "
            'update to: run({ app: "...", tool: "...", params: { ... } })'
        )

    return issues, warnings, fm_data.get("id"), fm_data


# ═══════════════════════════════════════════════════════════════════════════════
# Per-file Python checks
# ═══════════════════════════════════════════════════════════════════════════════

def scan_python_sandbox(app_dir: Path) -> list[tuple[str, int, str, str]]:
    """AST-scan every .py file for banned imports.

    Returns list of (relative_path, lineno, module_name, suggestion) tuples.
    """
    violations: list[tuple[str, int, str, str]] = []
    for rel, _py_file, _source, tree in _iter_app_py_files(app_dir):
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    top_level = alias.name.split(".")[0]
                    if top_level in BANNED_IMPORTS:
                        violations.append((rel, node.lineno, alias.name, BANNED_IMPORTS[top_level]))
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    top_level = node.module.split(".")[0]
                    if top_level in BANNED_IMPORTS:
                        violations.append((rel, node.lineno, node.module, BANNED_IMPORTS[top_level]))
    return violations


def check_params_double_nesting(app_dir: Path) -> list[str]:
    """Flag params.get("params") in Python files — a common anti-pattern."""
    issues: list[str] = []
    pattern = re.compile(r'params\.get\(["\']params["\']\)')
    for rel, py_file, _source, _tree in _iter_app_py_files(app_dir):
        with open(py_file, encoding="utf-8") as f:
            for lineno, line in enumerate(f, 1):
                if pattern.search(line):
                    issues.append(
                        f'{rel}:{lineno}: params.get("params") double-nesting — '
                        f'access params directly (e.g. params.get("filter"))'
                    )
    return issues


_CLIENT_KINDS = {"browser", "fetch", "api"}


def check_connection_client_value(app_dir: Path) -> list[str]:
    """Flag module-level ``connection(..., client="X")`` where X is not
    one of the sealed values (browser / fetch / api).

    The client kind selects the header bundle + jar behavior for every
    tool bound to the connection; a typo here silently disables the
    bundle and the jar. Static check keeps the sealed vocabulary
    authoritative — validator blocks commits with invalid kinds."""
    issues: list[str] = []
    for rel, _py_file, _source, tree in _iter_app_py_files(app_dir):
        for node in tree.body:
            if not (isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)):
                continue
            call = node.value
            if not (isinstance(call.func, ast.Name) and call.func.id == "connection"):
                continue
            for kw in call.keywords:
                if kw.arg != "client":
                    continue
                if not isinstance(kw.value, ast.Constant):
                    continue  # dynamic — skip; runtime will catch
                val = kw.value.value
                if val in _CLIENT_KINDS:
                    continue
                issues.append(
                    f"{rel}:{call.lineno}: connection(..., client={val!r}) — "
                    f"must be one of {sorted(_CLIENT_KINDS)}"
                )
    return issues


def _module_connection_decls(
    app_dir: Path,
) -> dict[str, tuple[str, int, dict[str, ast.AST]]]:
    """Map connection name → (rel, lineno, kwargs AST) for module-level
    ``connection("name", ...)`` declarations."""
    decls: dict[str, tuple[str, int, dict[str, ast.AST]]] = {}
    for rel, _py, _src, tree in _iter_app_py_files(app_dir):
        for node in tree.body:
            if not (isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)):
                continue
            call = node.value
            if not (isinstance(call.func, ast.Name) and call.func.id == "connection"):
                continue
            if not call.args:
                continue
            name_arg = call.args[0]
            if not (isinstance(name_arg, ast.Constant) and isinstance(name_arg.value, str)):
                continue
            kwargs = {kw.arg: kw.value for kw in call.keywords if kw.arg}
            decls[name_arg.value] = (rel, call.lineno, kwargs)
    return decls


def check_session_connection_domain(app_dir: Path) -> list[str]:
    """Require explicit ``domain=`` on no-auth connections used by
    ``@account.check``.

    Browser-driven connectors bind ``@connection("none")`` (no vault auth)
    and self-register a session identity. Domain derivation from ``base_url``
    (or falling back to the app id) made ownership brittle — Email/Messaging
    could not attribute ``efisio@gmail.com`` on ``google.com`` to
    ``gmail-cdp``. Authors must declare the platform identity namespace
    explicitly; ``base_url`` is for ``client.*`` relative URLs, not browse
    targets or silent domain derivation for sessions.
    """
    issues: list[str] = []
    decls = _module_connection_decls(app_dir)

    # Connections referenced by @account.check ops.
    check_conns: set[str | None] = set()
    check_sites: list[tuple[str, int, str, str | None]] = []
    for rel, _py, _src, tree in _iter_app_py_files(app_dir):
        for node in tree.body:
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            if _account_role(node) != "check":
                continue
            conn = _op_connection(node)
            check_conns.add(conn)
            check_sites.append((rel, node.lineno, node.name, conn))

    if not check_sites:
        return issues

    for conn_name in check_conns:
        if conn_name is None:
            # Auto-inferred sole connection — check that declaration if present.
            if len(decls) == 1:
                conn_name = next(iter(decls))
            else:
                continue
        decl = decls.get(conn_name)
        if decl is None:
            # `@connection("none")` sentinel with no module declaration is
            # still legal (session domain falls back to app id) — but warn
            # via a soft note only when it's the conventional "none" name
            # used by browser-driven connectors that SHOULD declare domain.
            if conn_name == "none":
                for rel, lineno, name, bound in check_sites:
                    if bound == "none" or bound is None:
                        issues.append(
                            f"{rel}:{lineno}: `{name}` is @account.check with "
                            f'@connection("none") but no module-level '
                            f'connection("none", domain="...") — declare the '
                            f"platform identity namespace explicitly so session "
                            f"accounts attribute to this plugin. "
                            f"See apps-browser-driven / apps-connections."
                        )
                        break
            continue
        rel, lineno, kwargs = decl
        has_auth = "auth" in kwargs
        has_domain = "domain" in kwargs
        if has_auth:
            continue  # vault-backed — domain may derive from base_url
        if not has_domain:
            issues.append(
                f"{rel}:{lineno}: connection({conn_name!r}, ...) has no auth "
                f"and is used by @account.check but omits domain= — set "
                f'domain="<platform>" (e.g. "google.com") so session identity '
                f"ownership is explicit. base_url is for client.* relative "
                f"URLs, not the browse target or silent domain derivation."
            )
    return issues


def check_tool_name_collisions(app_dir: Path) -> list[str]:
    """Flag duplicate tool (function) names across .py files in an app."""
    defs: dict[str, list[tuple[str, int]]] = {}
    for rel, _py_file, _source, tree in _iter_app_py_files(app_dir):
        for node in tree.body:  # top-level only
            if not _is_tool_function(node):
                continue
            defs.setdefault(node.name, []).append((rel, node.lineno))

    issues: list[str] = []
    for fname, locations in defs.items():
        if len(locations) > 1:
            where = ", ".join(f"{p}:{ln}" for p, ln in locations)
            issues.append(
                f"tool name collision: '{fname}' defined in multiple files ({where}) — "
                f"engine tool namespace is flat per app; rename or merge"
            )
    return issues


def check_tool_shape(app_dir: Path) -> list[str]:
    """Every public top-level function that's a tool must have @returns
    and accept **params."""
    issues: list[str] = []
    for rel, _py_file, _source, tree in _iter_app_py_files(app_dir):
        for node in tree.body:
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            if node.name.startswith("_"):
                continue
            # Only check functions with at least one tool marker decorator —
            # otherwise we'd flag every private helper.
            is_tool = any(
                _decorator_name(dec) in _TOOL_MARKER_DECORATORS
                for dec in node.decorator_list
            )
            if not is_tool:
                continue
            if not _has_returns_decorator(node):
                issues.append(
                    f"{rel}:{node.lineno}: `{node.name}` missing @returns decorator"
                )
            if not node.args.kwarg:
                issues.append(
                    f"{rel}:{node.lineno}: `{node.name}` missing **params "
                    f"(engine injects auth/context via params)"
                )
    return issues


# ── SDK surface existence check ────────────────────────────────────────────────

_REMOVED_MODULE_HINTS: dict[str, str] = {
    "http": (
        "removed — use `client.get/post/put/delete/patch/head` for "
        "network verbs and `url.build/parse/encode/decode` for URL "
        "string math."
    ),
}


def check_sdk_surface_existence(app_dir: Path) -> list[str]:
    """Flag `<sdk_module>.<attr>(...)` where attr doesn't exist on the
    module, and also flag imports of SDK modules that have been
    removed (with a migration hint).

    This is the catch that would have blocked `http.request(...)` at
    commit time. Walks every Attribute access where the value is a
    Name matching an SDK module, and looks up the attribute in the
    pre-scanned SDK surface. Offers a closest-match suggestion via
    difflib.
    """
    issues: list[str] = []
    surface = _load_sdk_surface()
    if not surface:
        return issues

    for rel, _py_file, _source, tree in _iter_app_py_files(app_dir):
        # Imported module aliases in this file. We only flag attribute access
        # on names that are clearly the SDK module (imported from agentos or
        # matching a module stem). Conservative: if a local variable shadows
        # the module name, we stop tracking it.
        sdk_names_in_file: dict[str, str] = {}  # local_name -> module_name

        for node in ast.walk(tree):
            # `from agentos import http` or `from agentos import http as h`
            if isinstance(node, ast.ImportFrom) and node.module == "agentos":
                for alias in node.names:
                    if alias.name in surface:
                        sdk_names_in_file[alias.asname or alias.name] = alias.name
                    elif alias.name in _REMOVED_MODULE_HINTS:
                        issues.append(
                            f"{rel}:{node.lineno}: `from agentos import "
                            f"{alias.name}` — {_REMOVED_MODULE_HINTS[alias.name]}"
                        )
            # `from agentos.macos import keychain`
            elif isinstance(node, ast.ImportFrom) and node.module and node.module.startswith("agentos."):
                for alias in node.names:
                    if alias.name in surface:
                        sdk_names_in_file[alias.asname or alias.name] = alias.name
            # `import agentos.http as http`
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name.startswith("agentos."):
                        leaf = alias.name.rsplit(".", 1)[-1]
                        if leaf in surface:
                            sdk_names_in_file[alias.asname or leaf] = leaf
                        elif leaf in _REMOVED_MODULE_HINTS:
                            issues.append(
                                f"{rel}:{node.lineno}: `import "
                                f"agentos.{leaf}` — {_REMOVED_MODULE_HINTS[leaf]}"
                            )

        if not sdk_names_in_file:
            continue

        for node in ast.walk(tree):
            if not isinstance(node, ast.Attribute):
                continue
            if not isinstance(node.value, ast.Name):
                continue
            local = node.value.id
            if local not in sdk_names_in_file:
                continue
            module = sdk_names_in_file[local]
            allowed = surface.get(module, {}).get("all", set())
            if not allowed:
                continue
            if node.attr.startswith("_"):
                continue  # private access — out of scope
            if node.attr in allowed:
                continue
            # Miss — build a closest-match suggestion.
            close = difflib.get_close_matches(node.attr, sorted(allowed), n=1, cutoff=0.6)
            hint = f" — did you mean `{local}.{close[0]}`?" if close else ""
            issues.append(
                f"{rel}:{node.lineno}: `{local}.{node.attr}` does not exist on "
                f"agentos.{module}{hint}"
            )

    return issues


# ── Missing-await check ────────────────────────────────────────────────────────

_SCHEDULER_NAMES = {"create_task", "ensure_future", "gather", "wait", "shield", "wait_for"}


def _collect_awaited_call_ids(func_node: ast.AST) -> set[int]:
    """Return Python object ids of Call nodes that don't need an explicit `await`.

    Covers two cases where a bare coroutine-returning call is legitimate:
      1. `await <call>(...)` — the classic case.
      2. `asyncio.create_task(<call>(...))` / `ensure_future` / `gather` etc. —
         scheduler functions that consume the coroutine themselves. The
         coroutine calls may be direct args (`gather(f(1), f(2))`) or buried
         in a starred comprehension/sequence (`gather(*[f(i) for i in xs])`),
         the canonical fan-out idiom.
    """
    awaited: set[int] = set()
    for node in ast.walk(func_node):
        if isinstance(node, ast.Await) and isinstance(node.value, ast.Call):
            awaited.add(id(node.value))
            continue
        if isinstance(node, ast.Call):
            callee = node.func
            scheduler = False
            if (
                isinstance(callee, ast.Attribute)
                and isinstance(callee.value, ast.Name)
                and callee.value.id == "asyncio"
                and callee.attr in _SCHEDULER_NAMES
            ):
                scheduler = True
            elif isinstance(callee, ast.Name) and callee.id in _SCHEDULER_NAMES:
                scheduler = True
            if scheduler:
                # The coroutine call may be a direct arg or nested inside a
                # starred comprehension/sequence — walk each arg and mark every
                # Call the scheduler ultimately consumes.
                for arg in node.args:
                    for sub in ast.walk(arg):
                        if isinstance(sub, ast.Call):
                            awaited.add(id(sub))
    return awaited


def check_missing_await(app_dir: Path) -> list[str]:
    """Flag sync/async functions that call async functions without `await`.

    Each issue names the file, line, parent function, the async callee,
    and whether the parent was sync or async (the fix differs: sync →
    convert the whole function; async → add the await).
    """
    issues: list[str] = []
    sdk_async = _sdk_async_modules()

    for rel, _py_file, _source, tree in _iter_app_py_files(app_dir):
        local_async_names = {
            n.name for n in ast.walk(tree)
            if isinstance(n, ast.AsyncFunctionDef)
        }

        for func in ast.walk(tree):
            if not isinstance(func, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            parent_is_async = isinstance(func, ast.AsyncFunctionDef)
            awaited_ids = _collect_awaited_call_ids(func)

            for call in ast.walk(func):
                if not isinstance(call, ast.Call):
                    continue
                if id(call) in awaited_ids:
                    continue

                callee = call.func
                called_label: str | None = None

                if isinstance(callee, ast.Attribute) and isinstance(callee.value, ast.Name):
                    module_name = callee.value.id
                    if module_name in sdk_async and callee.attr in sdk_async[module_name]:
                        called_label = f"{module_name}.{callee.attr}"
                elif isinstance(callee, ast.Name):
                    if callee.id in local_async_names:
                        called_label = callee.id

                if called_label is None:
                    continue

                fix_hint = (
                    "add `await` (parent is async)"
                    if parent_is_async
                    else "convert parent to `async def` and `await` the call "
                         "(callers must also await the parent)"
                )
                issues.append(
                    f"{rel}:{call.lineno}: {func.name}() calls {called_label}() "
                    f"without `await` — {fix_hint}"
                )

    return issues


# ── Sync-sleep-in-async check ─────────────────────────────────────────────────

def check_sync_sleep_in_async(app_dir: Path) -> list[str]:
    """Flag `time.sleep(...)` inside an `async def`.

    Sync sleep inside async code blocks the event loop. Use
    `await asyncio.sleep(...)` instead.
    """
    issues: list[str] = []
    for rel, _py_file, _source, tree in _iter_app_py_files(app_dir):
        for func in ast.walk(tree):
            if not isinstance(func, ast.AsyncFunctionDef):
                continue
            for call in ast.walk(func):
                if not isinstance(call, ast.Call):
                    continue
                callee = call.func
                if (
                    isinstance(callee, ast.Attribute)
                    and isinstance(callee.value, ast.Name)
                    and callee.value.id == "time"
                    and callee.attr == "sleep"
                ):
                    issues.append(
                        f"{rel}:{call.lineno}: `time.sleep()` inside async `{func.name}()` "
                        f"blocks the event loop — use `await asyncio.sleep(...)`"
                    )
    return issues


# ── Shape conformance (returns-dict keys vs declared shape) ───────────────────

def check_shape_conformance(app_dir: Path, shapes_dir: Path | None) -> list[str]:
    """AST-check that Python return dicts match the shape declared in @returns(...)."""
    warnings: list[str] = []
    if not shapes_dir:
        return warnings
    # Edges self-register (edges-self-register): there is no link registry and
    # shapes declare no relations. A returned key whose value is a nested entity
    # is an edge — open-world, any verb is valid — so it's never flagged as an
    # undeclared field. Only scalar-valued keys are checked against the shape's
    # own fields.

    for rel, _py_file, _source, tree in _iter_app_py_files(app_dir):
        for node in tree.body:  # top-level only
            if not _is_tool_function(node):
                continue
            shape_names = _tool_return_shapes(node)
            if not shape_names:
                continue  # inline schema or primitive return

            # Union returns validate keys against the union of all arms'
            # fields — static analysis sees every return statement mixed
            # together, so per-arm attribution is impossible here; the
            # worker discriminates at runtime.
            shape_fields: set[str] = set()
            shape_relations: set[str] = set()
            missing_arm = False
            for shape_name in shape_names:
                shape_data = _load_shape_fields(shapes_dir, shape_name)
                if shape_data is None:
                    warnings.append(
                        f"{rel}:{node.lineno}: {node.name} returns shape '{shape_name}' "
                        f"— shape not found in shapes/"
                    )
                    missing_arm = True
                    continue
                arm_fields, arm_relations = shape_data
                shape_fields |= arm_fields
                shape_relations |= arm_relations
            if missing_arm and not (shape_fields or shape_relations):
                continue
            shape_label = " | ".join(shape_names)
            all_valid_keys = STANDARD_FIELDS | CONTENT_FIELDS | shape_fields | shape_relations | SYSTEM_RETURN_FIELDS

            returned_keys = _extract_return_keys_from_function(tree, node.name)
            if returned_keys is None:
                continue  # no dict-literal returns — can't analyze

            # Identity completeness is only checkable for a single-shape
            # return — with a union, no static way to tell which return
            # statements belong to which arm.
            if len(shape_names) == 1:
                identity_keys = _load_shape_identity(shapes_dir, shape_names[0])
                if identity_keys:
                    field_identity = [k for k in identity_keys if k not in shape_relations and k != "id"]
                    for key in field_identity:
                        if key not in returned_keys:
                            warnings.append(
                                f"{rel}:{node.lineno}: {node.name} returns shape '{shape_label}' "
                                f"but is missing identity field '{key}' — dedup will fall back to imported_from"
                            )

            # Extra keys advisory — ignore underscore-prefixed internals AND
            # keys whose value is a nested entity (a dict / list-of-dicts).
            # Those are edges, not fields: the verb-space is open, so the engine
            # links any shaped child regardless of the parent's declared fields.
            # Only scalar-valued keys are field-typo candidates worth flagging.
            edge_keys = _extract_nested_value_keys(tree, node.name)
            extra = {
                k for k in returned_keys - all_valid_keys
                if not k.startswith("_") and k not in edge_keys
            }
            if extra:
                warnings.append(
                    f"{rel}:{node.lineno}: {node.name} returns keys not declared on shape '{shape_label}': "
                    f"{', '.join(sorted(extra))} — the engine will union-extend on next run; "
                    f"add to platform/ontology/shapes/{shape_names[0]}.yaml to get SDK TypedDict coverage"
                )
    return warnings


# ── camelCase dict key check ──────────────────────────────────────────────────

def _to_camel(snake: str) -> str:
    """Convert snake_case to camelCase."""
    parts = snake.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


def _inline_returns_keys(node: ast.FunctionDef | ast.AsyncFunctionDef) -> set[str] | None:
    """Extract keys from `@returns({"foo": "string", ...})` inline schema."""
    for dec in node.decorator_list:
        if not isinstance(dec, ast.Call):
            continue
        if _decorator_name(dec) != "returns":
            continue
        if not dec.args:
            continue
        arg = dec.args[0]
        if isinstance(arg, ast.Dict):
            keys: set[str] = set()
            for k in arg.keys:
                if isinstance(k, ast.Constant) and isinstance(k.value, str):
                    keys.add(k.value)
            return keys
        return None
    return None


def _provides_auth_kind(node: ast.FunctionDef | ast.AsyncFunctionDef) -> str | None:
    """If this function is decorated `@provides(<X>_auth, ...)`, return `X`.

    Recognises:
      @provides(oauth_auth, ...)        → "oauth"
      @provides(cookie_auth, ...)       → "cookie"
      @provides("oauth_auth", ...)      → "oauth"
      @provides(name="cookie_auth")     → "cookie"

    Returns None for non-auth `@provides(...)` decorators (services like
    `@provides(llm)` or `@provides(file_system)`).
    """
    for dec in node.decorator_list:
        if not isinstance(dec, ast.Call):
            continue
        if _decorator_name(dec) != "provides":
            continue
        # First positional arg, OR keyword `name=`, must be `<kind>_auth`.
        cap_node = dec.args[0] if dec.args else None
        if cap_node is None:
            for kw in dec.keywords:
                if kw.arg == "name":
                    cap_node = kw.value
                    break
        if cap_node is None:
            continue
        if isinstance(cap_node, ast.Name):
            cap = cap_node.id
        elif isinstance(cap_node, ast.Constant) and isinstance(cap_node.value, str):
            cap = cap_node.value
        else:
            continue
        if cap.endswith("_auth"):
            return cap[: -len("_auth")]
    return None


def _load_auth_contracts() -> dict[str, dict] | None:
    """Load codegen'd AUTH_CONTRACTS dict; returns None if generator hasn't run."""
    try:
        from agentos._generated_auth_contracts import AUTH_CONTRACTS
    except ImportError:
        return None
    return AUTH_CONTRACTS


def check_check_session_identity(app_dir: Path) -> tuple[list[str], list[str]]:
    """Enforce the `check_session` identity contract at commit time.

    Per `_product/p1/fix-auth/credential-providers-and-identity.md` Decision 8:
      - `authenticated: True` returns MUST include an `identifier` field.
      - `identifier` MUST NOT be a pure-integer literal (the Goodreads
        `"26631647"` antipattern). Use the service's email, handle, or
        canonical userId instead.
      - `email` / `phone` literal values SHOULD be wrapped in
        `normalize_email(...)` / `normalize_phone(...)` before returning.
        Best-effort — catches literal dict constructions like
        `{"email": email_str, ...}` where `email_str` isn't a
        normalize-call result.

    Returns `(errors, warnings)`.
    """
    errors: list[str] = []
    warnings: list[str] = []

    for rel, _py_file, _source, tree in _iter_app_py_files(app_dir):
        for node in tree.body:
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            if node.name != "check_session":
                continue

            # Walk every return statement's dict literal (if any).
            for ret in ast.walk(node):
                if not isinstance(ret, ast.Return):
                    continue
                ret_dict = ret.value
                if not isinstance(ret_dict, ast.Dict):
                    continue

                # Lift key→value pairs for the (string-keyed) entries.
                pairs: dict[str, ast.expr] = {}
                for k, v in zip(ret_dict.keys, ret_dict.values):
                    if isinstance(k, ast.Constant) and isinstance(k.value, str):
                        pairs[k.value] = v

                auth_val = pairs.get("authenticated")
                is_authed = (
                    isinstance(auth_val, ast.Constant)
                    and auth_val.value is True
                )
                identifier_val = pairs.get("identifier")

                if is_authed and identifier_val is None:
                    warnings.append(
                        f"{rel}:{ret.lineno}: check_session returns "
                        f"`authenticated: True` without `identifier` — "
                        f"engine can't persist a credential row without it."
                    )

                # Integer-literal identifier — hard error.
                if isinstance(identifier_val, ast.Constant):
                    lit = identifier_val.value
                    if isinstance(lit, int) or (
                        isinstance(lit, str) and lit.isdigit()
                    ):
                        errors.append(
                            f"{rel}:{ret.lineno}: check_session `identifier` "
                            f"is a numeric literal ({lit!r}); pick the "
                            f"service's email or handle instead and store "
                            f"the numeric id under `userId`."
                        )

                # Email / phone should be normalized. Only warn when we
                # can see the assignment isn't a normalize_*() call.
                for key, normalizer in (
                    ("email", "normalize_email"),
                    ("phone", "normalize_phone"),
                ):
                    val = pairs.get(key)
                    if val is None:
                        continue
                    if _is_normalize_call(val, normalizer):
                        continue
                    # If the value is a plain Name (e.g. `email_var`), check
                    # whether that name was assigned from a normalize_*() call
                    # inside this function body. Best-effort; skip if unclear.
                    if isinstance(val, ast.Name) and _name_from_normalize(
                        node, val.id, normalizer
                    ):
                        continue
                    warnings.append(
                        f"{rel}:{ret.lineno}: check_session `{key}` not "
                        f"obviously produced by `agentos.identity."
                        f"{normalizer}(...)` — canonical form is required "
                        f"before returning."
                    )

    return errors, warnings


def _is_normalize_call(expr: ast.expr, fn_name: str) -> bool:
    """True when `expr` is `normalize_<x>(...)` or `identity.normalize_<x>(...)`."""
    if not isinstance(expr, ast.Call):
        return False
    callee = expr.func
    if isinstance(callee, ast.Name) and callee.id == fn_name:
        return True
    if (
        isinstance(callee, ast.Attribute)
        and callee.attr == fn_name
    ):
        return True
    return False


def _name_from_normalize(
    func: ast.FunctionDef | ast.AsyncFunctionDef, name: str, fn_name: str
) -> bool:
    """True when `name` is last assigned from `normalize_<x>(...)` inside `func`."""
    found = False
    for stmt in ast.walk(func):
        if isinstance(stmt, ast.Assign):
            if _is_normalize_call(stmt.value, fn_name):
                for target in stmt.targets:
                    if isinstance(target, ast.Name) and target.id == name:
                        found = True
        elif isinstance(stmt, ast.AnnAssign):
            if stmt.value is not None and _is_normalize_call(stmt.value, fn_name):
                if isinstance(stmt.target, ast.Name) and stmt.target.id == name:
                    found = True
    return found


def check_account_trio(app_dir: Path) -> list[str]:
    """Validate `@account.<role>` declarations — the account protocol.

    - `@account.login` requires a sibling `@account.logout` somewhere in
      the app. Every app that can log in must be able to log out —
      server-side revocation is what makes "logout" more than a cosmetic
      local-cache delete.
    - `login`/`logout`/`profile`: at most one op each — the app's tool
      namespace is flat and the engine resolves exactly one.
    - `check`: one op **per connection** — a multi-connection app (Claude:
      `code` subscription, `web` login, `api` key) carries a distinct identity
      per connection, and the engine resolves the check bound to the connection
      that served. Two checks on the *same* connection would shadow each other.

    Errors, not warnings: the decorators are new, so there is no installed
    base to migrate — the wrong thing is impossible from day one.
    """
    issues: list[str] = []
    sites: dict[str, list[tuple[str, int, str, str | None]]] = {}
    for rel, _py, _src, tree in _iter_app_py_files(app_dir):
        for node in tree.body:
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            role = _account_role(node)
            if role is not None:
                sites.setdefault(role, []).append(
                    (rel, node.lineno, node.name, _op_connection(node))
                )

    for role, where in sorted(sites.items()):
        if role == "check":
            # One check per connection — flag only duplicates on the SAME one.
            by_conn: dict[str | None, list[tuple[str, int, str]]] = {}
            for rel, lineno, name, conn in where:
                by_conn.setdefault(conn, []).append((rel, lineno, name))
            for conn, group in by_conn.items():
                if len(group) > 1:
                    locs = ", ".join(f"{rel}:{lineno} {name}" for rel, lineno, name in group)
                    issues.append(
                        f"@account.check declared on {len(group)} ops for the same "
                        f"connection {conn!r} ({locs}) — one check per connection; "
                        f"the engine resolves the check bound to the serving connection."
                    )
            continue
        if len(where) > 1:
            locs = ", ".join(f"{rel}:{lineno} {name}" for rel, lineno, name, _ in where)
            issues.append(
                f"@account.{role} declared on {len(where)} ops ({locs}) — "
                f"one op per role; the engine resolves exactly one."
            )

    if "login" in sites and "logout" not in sites:
        rel, lineno, name, _ = sites["login"][0]
        issues.append(
            f"{rel}:{lineno}: `{name}` is @account.login but no op is "
            f"@account.logout. Every app that can log in must be able to "
            f"log out — server-side revoke is what makes logout more than "
            f"a local-cache delete. See apps-adding-login on the system volume."
        )
    return issues


def check_auth_provider_contract(app_dir: Path) -> list[str]:
    """Enforce the OAuth / cookie provider return contract at commit time.

    Single source of truth: `platform/ontology/auth-contracts/{oauth,cookie}.yaml` →
    codegen'd into `agentos._generated_auth_contracts.AUTH_CONTRACTS`.

    For every function decorated `@provides(<kind>_auth, ...)`, this check:
      1. Confirms `@returns(...)` is an inline dict schema (not a shape name).
      2. Verifies all REQUIRED keys are declared.
      3. Flags any FORBIDDEN_CAMEL_CASE keys with an explicit
         "did you mean <snake_case>?" message.
      4. Hints when a RECOMMENDED key is missing.

    Catches the `mimestream.credential_get returned accessToken` bug (and
    every future copy of it) before commit. See
    `_product/p1/observability/panes.md` for the full incident.
    """
    issues: list[str] = []
    contracts = _load_auth_contracts()
    if contracts is None:
        return issues

    for rel, _py, _src, tree in _iter_app_py_files(app_dir):
        for node in tree.body:
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            kind = _provides_auth_kind(node)
            if kind is None or kind not in contracts:
                continue
            spec = contracts[kind]

            keys = _inline_returns_keys(node)
            if keys is None:
                # Either no @returns, or @returns is a shape name, not a
                # dict schema. Auth providers MUST declare an inline dict
                # schema so we can validate it.
                issues.append(
                    f"{rel}:{node.lineno}: {node.name} is decorated "
                    f"`@provides({kind}_auth, ...)` but `@returns(...)` is missing or "
                    f"uses a shape name. Auth providers must declare an inline "
                    f"return schema, e.g. `@returns({{\"access_token\": \"string\", ...}})`. "
                    f"See platform/ontology/auth-contracts/{kind}.yaml for the contract."
                )
                continue

            # 1. Required keys present?
            for req in spec.get("required", []):
                if req not in keys:
                    issues.append(
                        f"{rel}:{node.lineno}: {node.name} is `@provides({kind}_auth, ...)` "
                        f"but missing required field `{req}` in @returns. "
                        f"Engine reads `{req}` (snake_case) — without it, all downstream "
                        f"API calls silently 401. See platform/ontology/auth-contracts/{kind}.yaml."
                    )

            # 2. Forbidden camelCase variants?
            forbidden = spec.get("forbidden_camel_case", {})
            for camel, snake in forbidden.items():
                if camel in keys:
                    issues.append(
                        f"{rel}:{node.lineno}: {node.name} returns `{camel}` (camelCase) — "
                        f"engine expects `{snake}` (snake_case). Did you mean `{snake}`? "
                        f"This is the mimestream bug; see platform/ontology/auth-contracts/{kind}.yaml."
                    )

            # 3. Recommended keys missing — print as warning-style suggestion
            #    (still in the issues list so it shows up; but framed as advice).
            for rec in spec.get("recommended", []):
                if rec not in keys and rec not in forbidden.values():
                    # Don't yell about every missing optional; only shout
                    # about ones the engine actually depends on for refresh
                    # in the OAuth case (refresh_token, expires_in,
                    # client_id, token_url).
                    if kind == "oauth" and rec in ("refresh_token", "expires_in", "client_id", "token_url"):
                        issues.append(
                            f"{rel}:{node.lineno}: {node.name} omits recommended `{rec}` — "
                            f"without it, engine-driven token refresh is impossible. "
                            f"platform/ontology/auth-contracts/oauth.yaml."
                        )

    return issues


# @claims decorator is currently limited to a small, reviewed set of
# claimants. Keep this list tight — every addition wires new semantics into
# the engine's extraction path (see agentos_accounts::graph::ensure_claims).
_KNOWN_CLAIMANTS = {"primary_user"}


def _claims_value(node: ast.FunctionDef | ast.AsyncFunctionDef) -> str | None:
    """Extract the claimant string from @claims(...) on a tool function.

    Returns the literal string argument, or None if @claims is absent.
    Non-string / non-literal arguments return a sentinel "<dynamic>" so the
    validator can flag them instead of silently accepting.
    """
    for dec in node.decorator_list:
        if not isinstance(dec, ast.Call):
            continue
        if _decorator_name(dec) != "claims":
            continue
        if not dec.args:
            return "<empty>"
        arg = dec.args[0]
        if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
            return arg.value
        return "<dynamic>"
    return None


def check_claims(app_dir: Path) -> list[str]:
    """Validate `@claims(who)` usage:

    - **Error** if the claimant string isn't in the known set — runtime will
      skip attachment, so catch the typo at commit time.
    - **Warn** if `@claims` appears without `@returns(shape)` — the engine
      only attaches claims links to extracted top-level nodes; inline-dict
      returns and unclaimed ops don't produce a node.

    Precedent: mirrors `check_auth_provider_contract` structure.
    """
    issues: list[str] = []
    for rel, _py, _src, tree in _iter_app_py_files(app_dir):
        for node in tree.body:
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            claimant = _claims_value(node)
            if claimant is None:
                continue
            if claimant == "<empty>":
                issues.append(
                    f"{rel}:{node.lineno}: {node.name} uses `@claims()` with no argument. "
                    f"Expected `@claims(\"primary_user\")`."
                )
                continue
            if claimant == "<dynamic>":
                issues.append(
                    f"{rel}:{node.lineno}: {node.name} uses `@claims(<dynamic>)`. "
                    f"The argument must be a string literal so the engine can "
                    f"read it via AST. Known claimants: {sorted(_KNOWN_CLAIMANTS)}."
                )
                continue
            if claimant not in _KNOWN_CLAIMANTS:
                issues.append(
                    f"{rel}:{node.lineno}: {node.name} uses `@claims(\"{claimant}\")` — "
                    f"unknown claimant. Known values: {sorted(_KNOWN_CLAIMANTS)}. "
                    f"Unknown values are silently skipped at runtime."
                )
                continue
            # @claims with no @returns(shape) is a no-op — warn.
            if not _tool_return_shapes(node):
                issues.append(
                    f"{rel}:{node.lineno}: {node.name} uses `@claims(\"{claimant}\")` "
                    f"but `@returns(...)` is missing or uses an inline dict. "
                    f"Claims links attach to extracted nodes — without a typed shape "
                    f"return, no node lands on the graph and the decorator is a no-op."
                )
    return issues


def check_camelcase_dict_keys(app_dir: Path, shapes_dir: Path | None) -> list[str]:
    """Flag snake_case dict keys inside a return that should be camelCase per the declared shape.

    Shape-scoped: only flags when the function's `@returns(...)` shape (or inline
    dict schema) contains the camelCase field. This avoids false positives when
    an app uses a snake_case key like `session_id` for its own semantic that
    happens to collide with some unrelated shape's `sessionId` field.
    """
    errors: list[str] = []
    if not shapes_dir:
        return errors

    def _target_camel_fields(func: ast.FunctionDef | ast.AsyncFunctionDef) -> set[str]:
        """Return the set of camelCase field names that apply to this function's return."""
        shape_names = _tool_return_shapes(func)
        if shape_names:
            combined: set[str] = set()
            for shape_name in shape_names:
                data = _load_shape_fields(shapes_dir, shape_name)
                if not data:
                    continue
                fields, relations = data
                combined |= fields | relations
            return combined
        inline = _inline_returns_keys(func)
        return inline or set()

    def _walk_dict(node: ast.AST, rel: str, target_camel: set[str]) -> None:
        if isinstance(node, ast.Dict):
            for key in node.keys:
                if isinstance(key, ast.Constant) and isinstance(key.value, str):
                    k = key.value
                    if k.startswith("_"):
                        continue
                    if _SNAKE_RE.match(k):
                        camel = _to_camel(k)
                        if camel in target_camel:
                            errors.append(
                                f"{rel}:{key.lineno}: snake_case dict key '{k}' "
                                f"should be camelCase shape field '{camel}'"
                            )
            for val in node.values:
                if val is not None:
                    _walk_dict(val, rel, target_camel)
        elif isinstance(node, ast.List):
            for elt in node.elts:
                _walk_dict(elt, rel, target_camel)
        elif isinstance(node, ast.ListComp):
            _walk_dict(node.elt, rel, target_camel)

    for rel, _py_file, _source, tree in _iter_app_py_files(app_dir):
        for func in tree.body:  # top-level only
            if not isinstance(func, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            if func.name.startswith("_"):
                continue
            if not _is_tool_function(func):
                continue
            target_camel = _target_camel_fields(func)
            if not target_camel:
                continue
            for ret in ast.walk(func):
                if isinstance(ret, ast.Return) and ret.value is not None:
                    _walk_dict(ret.value, rel, target_camel)
    return errors


# ── Test-block tool reference check ──────────────────────────────────────────

def check_test_block_refs(app_dir: Path, fm_data: dict | None) -> list[str]:
    """Every tool named in `test:` must resolve to a real function."""
    warnings: list[str] = []
    if not fm_data or not isinstance(fm_data.get("test"), dict):
        return warnings
    all_ops: set[str] = set()
    for _rel, _py_file, _source, tree in _iter_app_py_files(app_dir):
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if not node.name.startswith("_"):
                    all_ops.add(node.name)
    for test_op in fm_data["test"]:
        if test_op not in all_ops:
            warnings.append(
                f"test block references '{test_op}' but no matching tool found in any .py file"
            )
    return warnings


# ── Docstring check ──────────────────────────────────────────────────────────

def check_docstrings(app_dir: Path) -> list[str]:
    """Warn when public tool functions have no docstring."""
    warnings: list[str] = []
    for rel, _py_file, _source, tree in _iter_app_py_files(app_dir):
        for node in tree.body:
            if not _is_tool_function(node):
                continue
            if not ast.get_docstring(node):
                warnings.append(
                    f"{rel}:{node.lineno}: `{node.name}` has no docstring "
                    f"(description will be empty in tool listings)"
                )
    return warnings


# ═══════════════════════════════════════════════════════════════════════════════
# Per-app audit
# ═══════════════════════════════════════════════════════════════════════════════

def audit_app_dir(app_dir: Path, shapes_dir: Path | None) -> tuple[int, str | None]:
    """Audit a single app directory. Returns (issue_count, app_id)."""
    all_issues: list[str] = []
    all_warnings: list[str] = []

    # readme frontmatter
    fm_issues, fm_warnings, app_id, fm_data = check_readme_frontmatter(app_dir)
    all_issues.extend(fm_issues)
    all_warnings.extend(fm_warnings)

    # Python checks — errors
    all_issues.extend(check_params_double_nesting(app_dir))
    all_issues.extend(check_connection_client_value(app_dir))
    all_issues.extend(check_session_connection_domain(app_dir))
    all_issues.extend(check_tool_name_collisions(app_dir))
    all_issues.extend(check_tool_shape(app_dir))
    all_issues.extend(check_sdk_surface_existence(app_dir))
    all_issues.extend(check_missing_await(app_dir))
    all_issues.extend(check_sync_sleep_in_async(app_dir))
    all_issues.extend(check_camelcase_dict_keys(app_dir, shapes_dir))
    all_issues.extend(check_auth_provider_contract(app_dir))
    all_issues.extend(check_account_trio(app_dir))
    all_issues.extend(check_claims(app_dir))

    check_session_errors, check_session_warnings = check_check_session_identity(app_dir)
    all_issues.extend(check_session_errors)
    all_warnings.extend(check_session_warnings)

    # Python checks — warnings
    all_warnings.extend(check_shape_conformance(app_dir, shapes_dir))
    all_warnings.extend(check_docstrings(app_dir))
    all_warnings.extend(check_test_block_refs(app_dir, fm_data))

    # Sandbox
    for rel, lineno, module, suggestion in scan_python_sandbox(app_dir):
        all_issues.append(
            f"{rel}:{lineno}: banned import '{module}' — use {suggestion} instead"
        )

    display_name = app_id or app_dir.name
    if all_issues or all_warnings:
        print(f"\n[{display_name}]")
        for issue in all_issues:
            print(f"  ✗ {issue}")
        for warn in all_warnings:
            print(f"  ⚠ {warn}")

    return len(all_issues), app_id


# ═══════════════════════════════════════════════════════════════════════════════
# App discovery
# ═══════════════════════════════════════════════════════════════════════════════

def discover_app_roots(apps_dir: Path) -> list[Path]:
    """Walk apps_dir and return every directory containing a readme.md.

    Skips underscore-prefixed directories (prototypes, scratchpads).
    """
    roots: list[Path] = []
    for root, dirs, files in os.walk(apps_dir):
        dirs[:] = [d for d in dirs if not d.startswith("_")]
        if "readme.md" in files:
            roots.append(Path(root))
    return sorted(roots)


def _app_id_from_readme(app_dir: Path) -> str | None:
    """Best-effort app id lookup for single-app targeting."""
    readme_path = app_dir / "readme.md"
    if not readme_path.is_file():
        return None
    try:
        text = readme_path.read_text(encoding="utf-8")
        if not text.lstrip().startswith("---"):
            return None
        end = text.find("\n---", text.find("---") + 3)
        if end == -1:
            return None
        fm = yaml.safe_load(text[text.find("---") + 3:end]) or {}
        if isinstance(fm, dict):
            return fm.get("id")
    except (OSError, yaml.YAMLError):
        pass
    return None


# ═══════════════════════════════════════════════════════════════════════════════
# Commons apps — the `apps/` aisle (manifest + ui/ module)
# ═══════════════════════════════════════════════════════════════════════════════

# What a Commons app's UI may import: the SDK waist, react, and its own
# files. Anything else — a shell path, another app, a bare package — is a
# contract violation (the shell provides `agentos-ui` + `react` and
# nothing more; the store's import map will pin exactly those two).
_UI_IMPORT_ALLOW = {"react", "agentos-ui"}
_UI_IMPORT_RE = re.compile(
    r"""(?m)^\s*(?:import|export)\s+(?:[^'"\n]*?\sfrom\s+)?['"]([^'"]+)['"]"""
)

# Chrome class vocabulary apps must never hand-stamp or restyle. The OS
# emits these through agentos-ui components (Toolbar/ToolButton emit
# os-toolbar/os-tool-btn; navigator-* is the shell's own) — an app that
# writes the class by hand recreates the pre-component era where every
# theme pack needed a per-app section or the bar silently fell to white.
_UI_CHROME_CLASS_RE = re.compile(
    r"\b(?:os-toolbar(?:-separator)?|os-tool-btn|os-tool-label|app-toolbar|(?<!data-)navigator-[a-z][a-z-]*)\b"
)
# TSX: chrome classes inside string literals (comments stay legal — docs
# may name the vocabulary, markup may not). `data-navigator-id` is the
# sanctioned row-addressing attribute (`ui.click {navigatorId}`), not a
# class — the lookbehind lets it through.
_UI_TSX_CHROME_RE = re.compile(
    r"""['"`][^'"`\n]*\b(os-toolbar(?:-separator)?|os-tool-btn|os-tool-label|app-toolbar|(?<!data-)navigator-[a-z][a-z-]*)\b[^'"`\n]*['"`]"""
)
_CSS_COMMENT_RE = re.compile(r"/\*.*?\*/", re.S)

# Raw interactive elements app markup may never render — the component
# contract's one law: nothing styles a raw element, so nothing may RENDER
# one either. A hand-rolled <button> inherits whatever a theme pack paints
# on bare `button` (the recurring beveled-list-rows bug); a hand-stamped
# listbox/menu role skips the primitive's keyboard model. Apps compose the
# agentos-ui primitives: Button, OptionList/Option, ContextMenu, Select.
_UI_TS_COMMENT_RE = re.compile(r"/\*.*?\*/|(?<![:\w])//[^\n]*", re.S)
_UI_RAW_INTERACTIVE_RE = re.compile(
    r"<button\b"
    r"|<select\b"
    r"|<input\b[^>]*type\s*=\s*['\"](?:button|submit|reset|image)['\"]"
    r"|<[A-Za-z][\w.]*\b[^>]*\brole\s*=\s*['\"](?:listbox|option|menu|menuitem)['\"]"
)
_UI_RAW_INTERACTIVE_HINT = {
    "<button": "render <Button variant=…> (quiet for flat/icon actions)",
    "<select": "render the SDK Select",
    "<input": "render <Button type=\"submit\"> — a command input wears theme button chrome",
    "role=": "render OptionList/Option or ContextMenu — the primitive owns the role + keyboard model",
}

# Waist names an app may NOT import — the toolbar primitives left the public
# surface when the toolbar became `<CommandBar>` fed by `useCommands`. A
# button IS a capability-command; a raw Toolbar/ToolButton is a dead-button
# primitive, so it's structurally absent from `agentos-ui` and importing it
# is caught here with the fix (not just a bare "no exported member").
_UI_AGENTOS_IMPORT_BLOCK_RE = re.compile(
    r"""(?:import|export)\s*\{([^}]*)\}\s*from\s*['"]agentos-ui['"]""", re.S
)
_UI_BANNED_WAIST_NAMES = ("Toolbar", "ToolButton", "ToolbarSeparator")


_PY_PROVIDES_RE = re.compile(r"""@provides\(\s*['"]([\w-]+)['"]""")
_RS_PROVIDES_RE = re.compile(r'tool:\s*"([\w-]+)"')


def collect_provided_services(plugin_roots: list[Path]) -> set[str]:
    """Every service name some installed provider `@provides` — the same
    registry the engine self-registers at boot, harvested statically:
    Python plugins by decorator, Rust system apps (`crates/system-apps`)
    by their `ProvidesEntry { tool: "…" }` literals. This is the universe
    a manifest command's `action.service` must land in — a command naming
    a service NOTHING provides is a dead button by construction."""
    provided: set[str] = set()
    for root in plugin_roots:
        if not root.is_dir():
            continue
        for py in root.rglob("*.py"):
            try:
                provided.update(_PY_PROVIDES_RE.findall(py.read_text(encoding="utf-8")))
            except OSError:
                continue
        # A workspace source sits beside core/ — harvest the engine's
        # Rust-native providers too so a command on `browser_session`
        # (a system app) doesn't false-fail.
        system_apps = root.parent.parent / "core" / "crates" / "system-apps" / "src"
        if system_apps.is_dir():
            for rs in system_apps.glob("*.rs"):
                try:
                    provided.update(_RS_PROVIDES_RE.findall(rs.read_text(encoding="utf-8")))
                except OSError:
                    continue
    return provided


_COMMAND_TARGETS = {"selection", "view", "none"}


def check_manifest_commands(
    data: dict, ui_dir: Path, provided_services: set[str] | None
) -> list[str]:
    """The capability-command gate — a dead button must be unconstructable.

    `layout.commands[]` is the ONLY capability vocabulary (`layout.actions`
    died with it): every entry must parse; labelled (chrome) entries need
    an id handled in ui/; headless entries (`action.service`, no `label`)
    declare broker verbs with no chrome projection — themes may move
    buttons, they never invent capabilities. Brokered `action.service`
    must resolve to a real `@provides`. UI→manifest: every
    `callService` / `services.*` call in ui/ must appear on some command.
    """
    issues: list[str] = []
    layout = data.get("layout")
    if not isinstance(layout, dict):
        return issues
    if "actions" in layout:
        issues.append(
            "layout.actions is dead vocabulary — declare layout.commands[] "
            "(id/label/icon/group/target/action); useCommands resolves them"
        )
    commands = layout.get("commands")
    if commands is None:
        return issues
    if not isinstance(commands, list):
        return ["layout.commands must be a list of command entries"]

    ui_text = ""
    if ui_dir.is_dir():
        ui_text = "\n".join(
            src.read_text(encoding="utf-8")
            for src in sorted(ui_dir.rglob("*"))
            if src.suffix in (".ts", ".tsx")
        )

    declared_services: set[str] = set()
    seen_ids: set[str] = set()
    for i, cmd in enumerate(commands):
        where = f"layout.commands[{i}]"
        if not isinstance(cmd, dict):
            issues.append(f"{where}: not a mapping")
            continue
        cid = cmd.get("id")
        if not isinstance(cid, str) or not cid:
            issues.append(f"{where}: missing `id`")
            continue
        where = f"layout.commands[{cid}]"
        if cid in seen_ids:
            issues.append(f"{where}: duplicate id")
        seen_ids.add(cid)
        reverses = cmd.get("reverses")
        if reverses is not None:
            # A REVERSIBLE verb — two faces (`apply` / `revert`), each its own
            # label + brokered action; the resolver projects the active face,
            # so there is no top-level label/action to validate. Each face's
            # service must resolve, exactly like a plain brokered verb — a
            # direction the manifest can't route is the same dead button.
            if cmd.get("action"):
                issues.append(
                    f"{where}: a `reverses` verb carries no top-level `action` — "
                    "each face names its own"
                )
            if cmd.get("label"):
                issues.append(
                    f"{where}: a `reverses` verb carries no top-level `label` — "
                    "each face labels itself"
                )
            if not isinstance(reverses, dict) or set(reverses) != {"apply", "revert"}:
                issues.append(
                    f"{where}: `reverses` must be a mapping of exactly `apply` + "
                    "`revert` faces"
                )
                reverses = {}
            for fname in ("apply", "revert"):
                face = reverses.get(fname)
                fwhere = f"{where}.{fname}"
                if not isinstance(face, dict):
                    issues.append(f"{fwhere}: missing face ({{label, action.service}})")
                    continue
                if not face.get("label"):
                    issues.append(f"{fwhere}: missing `label`")
                faction = face.get("action")
                fservice = faction.get("service") if isinstance(faction, dict) else None
                if not fservice:
                    issues.append(
                        f"{fwhere}: missing `action.service` — a reversible face "
                        "is always brokered"
                    )
                else:
                    declared_services.add(fservice)
                    if provided_services is not None and fservice not in provided_services:
                        issues.append(
                            f"{fwhere}: service `{fservice}` resolves to NO @provides "
                            "in any source — the button could never route; declare "
                            "the provider first (or fix the typo)"
                        )
        else:
            action = cmd.get("action")
            if not isinstance(action, dict):
                issues.append(f"{where}: missing `action` ({{service, account}} or {{ui}})")
                action = {}
            service = action.get("service")
            ui_action = action.get("ui")
            headless = bool(service) and not cmd.get("label") and not ui_action
            if not headless and not cmd.get("label"):
                issues.append(f"{where}: missing `label` (or omit label for a headless service-only command)")
            if bool(service) == bool(ui_action):
                issues.append(
                    f"{where}: action must carry exactly one of `service` (brokered) "
                    "or `ui` (local)"
                )
            if ui_action and action.get("account"):
                issues.append(f"{where}: `account` strategy is meaningless on a ui-only action")
            if service:
                declared_services.add(service)
                if provided_services is not None and service not in provided_services:
                    issues.append(
                        f"{where}: service `{service}` resolves to NO @provides in any "
                        "source — the button could never route; declare the provider "
                        "first (or fix the typo)"
                    )
        target = cmd.get("target")
        if target is not None and target not in _COMMAND_TARGETS:
            issues.append(f"{where}: target `{target}` — one of {sorted(_COMMAND_TARGETS)}")
        key = cmd.get("key")
        if key is not None and (not isinstance(key, str) or len(key) != 1):
            issues.append(f"{where}: `key` must be a single character")
        # Headless (service, no label) — declare-only; no chrome handler required.
        is_headless = (
            reverses is None
            and isinstance(cmd.get("action"), dict)
            and bool(cmd["action"].get("service"))
            and not cmd.get("label")
        )
        if (
            not is_headless
            and ui_text
            and f"'{cid}'" not in ui_text
            and f'"{cid}"' not in ui_text
        ):
            issues.append(
                f"{where}: id `{cid}` never appears in ui/ — every chrome command needs "
                "a handler in the app's dispatch (runCommand)"
            )

    # UI → manifest: every brokered call in ui/ must be declared on commands.
    if ui_text:
        issues.extend(
            check_ui_services_declared(ui_text, declared_services, where="ui/")
        )
    return issues


# Platform ops — not app consent surface; apps may call without declaring.
_PLATFORM_SERVICES = frozenset(
    {
        "capabilities",
    }
)

_UI_SERVICE_PATTERNS = (
    # callService('mailbox', …) / callService("mailbox", …
    re.compile(r"""\bcallService\s*\(\s*['"]([a-z][a-z0-9_]*)['"]"""),
    # callOp('services.mailbox', …)
    re.compile(r"""\bcallOp\s*\(\s*['"]services\.([a-z][a-z0-9_]*)['"]"""),
    # useLiveFanout('order_history', …) — shopping helper
    re.compile(r"""\buseLiveFanout\s*\(\s*['"]([a-z][a-z0-9_]*)['"]"""),
    # useServiceFanout({ service: 'feeds', … })
    re.compile(r"""\bservice\s*:\s*['"]([a-z][a-z0-9_]*)['"]"""),
)


def check_ui_services_declared(
    ui_text: str, declared: set[str], *, where: str = "ui/"
) -> list[str]:
    """Every broker service string in ui/ must appear on layout.commands."""
    used: set[str] = set()
    for pat in _UI_SERVICE_PATTERNS:
        for m in pat.finditer(ui_text):
            used.add(m.group(1))
    issues: list[str] = []
    for svc in sorted(used - declared - _PLATFORM_SERVICES):
        issues.append(
            f"{where}: calls service `{svc}` but layout.commands never declares it — "
            "add a command (labelled chrome or headless service-only entry)"
        )
    return issues

def audit_commons_apps(aisle: Path, provided_services: set[str] | None = None) -> int:
    """Audit one source's Commons-app aisle (`<source>/apps/<id>/`).

    Per app: the manifest parses and its `id` matches the folder (the shell
    loads `ui/index.tsx` by folder name — a mismatch is a broken launch);
    `layout.commands[]` passes the capability-command gate (parses, ids
    unique + handled, every brokered service resolves to a real
    `@provides`); the ui module default-exports; ui imports stay inside
    the contract (react + agentos-ui + the app's own files); app CSS wraps
    itself in `@layer base` so a lazily-loaded sheet never outranks theme
    packs; and neither markup nor CSS touches the OS chrome vocabulary
    (os-toolbar / os-tool-btn / navigator-*) — toolbars come from the SDK
    CommandBar, never hand-stamped classes or per-app toolbar paint.
    Returns the issue count.
    """
    issues = 0
    app_dirs = sorted(d for d in aisle.iterdir() if d.is_dir() and not d.name.startswith("_"))
    if not app_dirs:
        return 0
    print(f"\n--- Commons apps in {aisle} ---")
    for app_dir in app_dirs:
        app_issues: list[str] = []
        manifest = app_dir / "app.yaml"
        if not manifest.is_file():
            app_issues.append("missing app.yaml — the manifest IS the app's identity")
        else:
            try:
                data = yaml.safe_load(manifest.read_text(encoding="utf-8")) or {}
                if not isinstance(data, dict):
                    app_issues.append("app.yaml is not a mapping")
                else:
                    if data.get("id") != app_dir.name:
                        app_issues.append(
                            f"app.yaml id `{data.get('id')}` ≠ folder `{app_dir.name}` — "
                            "the shell resolves ui/ by folder name"
                        )
                    if not data.get("name"):
                        app_issues.append("app.yaml missing `name`")
                    app_issues.extend(
                        check_manifest_commands(data, app_dir / "ui", provided_services)
                    )
            except yaml.YAMLError as e:
                app_issues.append(f"app.yaml does not parse: {e}")

        ui_dir = app_dir / "ui"
        if ui_dir.is_dir():
            entry = ui_dir / "index.tsx"
            if not entry.is_file():
                app_issues.append("ui/ exists but ships no index.tsx — the shell loads exactly that")
            elif not re.search(r"export\s+default", entry.read_text(encoding="utf-8")):
                app_issues.append("ui/index.tsx has no default export (the AppUIProps component)")

            for src in sorted(ui_dir.rglob("*")):
                if src.suffix in (".ts", ".tsx"):
                    text = src.read_text(encoding="utf-8")
                    for spec in _UI_IMPORT_RE.findall(text):
                        if spec in _UI_IMPORT_ALLOW:
                            continue
                        if spec.startswith("."):
                            resolved = (src.parent / spec).resolve()
                            if str(resolved).startswith(str(app_dir.resolve())):
                                continue
                            app_issues.append(
                                f"{src.relative_to(app_dir)}: import `{spec}` escapes the app folder"
                            )
                            continue
                        app_issues.append(
                            f"{src.relative_to(app_dir)}: import `{spec}` — app UIs import "
                            "`agentos-ui`, `react`, and their own files ONLY"
                        )
                    for block in _UI_AGENTOS_IMPORT_BLOCK_RE.findall(text):
                        for banned in _UI_BANNED_WAIST_NAMES:
                            if re.search(rf"\b{banned}\b", block):
                                app_issues.append(
                                    f"{src.relative_to(app_dir)}: imports `{banned}` from "
                                    "agentos-ui — the toolbar is `<CommandBar commands={…}>` fed "
                                    "by `useCommands` (declare the verbs in `layout.commands[]`). "
                                    "There is no raw Toolbar/ToolButton in the waist: a button IS "
                                    "a capability-command, so a dead button is unspellable"
                                )
                    for m in _UI_TSX_CHROME_RE.finditer(text):
                        app_issues.append(
                            f"{src.relative_to(app_dir)}: chrome class `{m.group(1)}` stamped "
                            "by hand — render `<CommandBar>` (or the SDK primitives) instead; "
                            "the OS owns its chrome vocabulary"
                        )
                    uncommented = _UI_TS_COMMENT_RE.sub("", text)
                    for m in _UI_RAW_INTERACTIVE_RE.finditer(uncommented):
                        token = m.group(0)
                        hint = next(
                            v for k, v in _UI_RAW_INTERACTIVE_HINT.items() if k in token
                        )
                        app_issues.append(
                            f"{src.relative_to(app_dir)}: raw interactive element "
                            f"`{token[:40]}` — {hint}"
                        )
                elif src.suffix == ".css":
                    text = src.read_text(encoding="utf-8")
                    if not re.search(r"@layer\s+base\s*\{", text):
                        app_issues.append(
                            f"{src.relative_to(app_dir)}: app CSS must wrap its rules in "
                            "`@layer base { … }` (an unlayered sheet outranks theme packs)"
                        )
                    bare = _CSS_COMMENT_RE.sub("", text)
                    for m in _UI_CHROME_CLASS_RE.finditer(bare):
                        app_issues.append(
                            f"{src.relative_to(app_dir)}: selector touches chrome class "
                            f"`{m.group(0)}` — apps never restyle OS chrome; the floor and "
                            "packs paint the CommandBar toolbar everywhere at once"
                        )
                    for rule_m in re.finditer(r"([^{}]+)\{([^{}]*)\}", bare):
                        sel, body = rule_m.group(1), rule_m.group(2)
                        if re.search(r"\.[\w-]*-toolbar\b", sel) and "background" in body:
                            app_issues.append(
                                f"{src.relative_to(app_dir)}: `{sel.strip().splitlines()[-1].strip()}` "
                                "paints its own toolbar — render `<CommandBar>` instead; "
                                "hand-rolled toolbar chrome is exactly what packs can't theme"
                            )

        if app_issues:
            print(f"  ✗ {app_dir.name}")
            for i in app_issues:
                print(f"      {i}")
            issues += len(app_issues)
        else:
            print(f"  ✓ {app_dir.name}")
    return issues


# ═══════════════════════════════════════════════════════════════════════════════
# Public entry points
# ═══════════════════════════════════════════════════════════════════════════════

def run_validate(target: str | None = None, *, validate_all: bool = False,
                 sandbox_only: bool = False, dry_run: bool = False) -> int:
    """Main entry point — invoked by `agent-sdk validate` and the pre-commit hook.

    Args:
        target: a single app id, an app directory path, or None for auto-discovery.
        validate_all: when True (or target is None), audit every discovered app.
        sandbox_only: only run the banned-import sandbox scan (fast, for hooks).
        dry_run: unused (placeholder for future dry-run execution support).

    Returns exit code: 0 for clean, 1 if any errors found.
    """
    del dry_run  # currently unused; kept for CLI compatibility

    # If target is an explicit directory, respect it as-is. Otherwise find one.
    apps_dir: Path | None = None
    single_app_dir: Path | None = None

    if target:
        tp = Path(target).expanduser()
        if tp.is_dir():
            # Explicit directory — either an app dir or a apps-root
            if (tp / "readme.md").is_file():
                single_app_dir = tp.resolve()
                apps_dir = _find_apps_dir(tp.parent) or tp.parent.resolve()
            else:
                apps_dir = tp.resolve()

    if apps_dir is None:
        apps_dir = _find_apps_dir()
    if apps_dir is None:
        print("error: could not locate plugins/ directory", file=sys.stderr)
        print("  set AGENTOS_APPS_DIR or run from inside the workspace", file=sys.stderr)
        return 1

    # Discover all sources — local workspace + anything configured in the
    # engine's settings.sources. This powers the banner, the orphan check,
    # and (in future) multi-source app scanning.
    sources = _discover_sources(explicit_apps_dir=apps_dir)
    _print_sources_banner(sources)

    # Warn loudly when a configured path is missing. Agents running this
    # script can surface a prompt to clean it up via `--fix-sources`.
    missing_configured = [s for s in sources if s.origin == "configured" and not s.exists]
    if missing_configured:
        print()
        print(f"⚠ {len(missing_configured)} configured source path(s) do not exist on disk.")
        for s in missing_configured:
            print(f"    {s.root}")
        print(f"  Run `agent-sdk validate --fix-sources` to review and remove missing entries.")

    # Prefer the shapes dir the workspace source discovered (which knows about
    # `platform/ontology/shapes/`). Fall back to the env-based finder.
    workspace_source = next((s for s in sources if s.origin == "workspace"), None)
    shapes_dir = (workspace_source.shapes_dir if workspace_source else None) or _find_shapes_dir(apps_dir)
    known_shapes = _load_known_shapes(shapes_dir) if shapes_dir else set()

    print()
    print(f"Auditing apps in {apps_dir}")
    if shapes_dir:
        print(f"Shape registry: {len(known_shapes)} shapes from {shapes_dir}")
    else:
        print("  (shapes not found — shape conformance checks disabled)")

    app_roots = discover_app_roots(apps_dir)
    if single_app_dir:
        app_roots = [single_app_dir]

    # If target is a bare string (not a path), treat it as an app id filter.
    id_filter: str | None = None
    if target and not Path(target).expanduser().is_dir():
        id_filter = target

    total_issues = 0
    total_apps = 0

    if sandbox_only:
        print("\n--- Sandbox: banned import scan ---")
        sandbox_violations = 0
        for root in app_roots:
            app_id = _app_id_from_readme(root) or root.name
            if id_filter and app_id != id_filter:
                continue
            total_apps += 1
            violations = scan_python_sandbox(root)
            if violations:
                sandbox_violations += len(violations)
                total_issues += len(violations)
                vcount = len(violations)
                label = "banned import" if vcount == 1 else "banned imports"
                print(f"  ✗ {app_id:<20s} {vcount} {label}")
                for rel_path, lineno, module, suggestion in violations:
                    print(f"    {app_id}/{rel_path}:{lineno}  import {module}")
                    print(f"    → Use {suggestion} instead")
            else:
                print(f"  ✓ {app_id:<20s} 0 banned imports")

        print(f"\n{'=' * 50}")
        if sandbox_violations == 0:
            print(f"✓ {total_apps} apps passed sandbox check — no banned imports")
        else:
            print(f"✗ {sandbox_violations} banned imports across {total_apps} apps")
        print(f"{'=' * 50}")
        return 1 if total_issues > 0 else 0

    # Full audit — Commons-app aisles first (the `apps/` sibling of each
    # source's plugins dir: manifest + ui/ contract), then shape files,
    # then plugins.
    if not id_filter and not single_app_dir:
        provided_services = collect_provided_services(
            [s.apps_dir for s in sources if s.apps_dir]
        )
        seen_aisles: set[Path] = set()
        for s in sources:
            if not s.apps_dir:
                continue
            aisle = s.apps_dir.parent / "apps"
            if aisle in seen_aisles or not aisle.is_dir():
                continue
            seen_aisles.add(aisle)
            total_issues += audit_commons_apps(aisle, provided_services)

    if shapes_dir and not id_filter and not single_app_dir:
        for shape_path in sorted(_iter_shape_yamls(shapes_dir)):
            total_issues += audit_shape_file(shape_path, known_shapes)

        # Orphan-shape audit: warn for shapes that have no producer and
        # no reference anywhere. Producers = app `@returns(...)` + engine
        # `ensure_tag(...)` / `shapes::FOO`. References = `relations:`,
        # embedded field types, `also:` inheritance. Warnings only.
        all_apps_roots = [s.apps_dir for s in sources if s.apps_dir]
        all_shapes_roots = [s.shapes_dir for s in sources if s.shapes_dir]
        all_crates_roots = [s.crates_dir for s in sources if s.crates_dir]
        check_orphan_shapes(
            all_apps_roots, all_shapes_roots, all_crates_roots
        )

    for root in app_roots:
        app_id = _app_id_from_readme(root) or root.name
        if id_filter and app_id != id_filter:
            continue
        total_apps += 1
        issues, _ = audit_app_dir(root, shapes_dir)
        total_issues += issues

    print(f"\n{'=' * 50}")
    if total_issues == 0:
        print(f"✓ {total_apps} apps passed")
    else:
        print(f"✗ {total_issues} issues across {total_apps} apps")
    print(f"{'=' * 50}")

    return 1 if total_issues > 0 else 0


def main() -> int:
    """CLI entry point when invoked as `python -m agentos.validate`."""
    args = sys.argv[1:]
    if "--fix-sources" in args:
        return _fix_sources_interactive()
    sandbox_only = "--sandbox" in args
    if sandbox_only:
        args.remove("--sandbox")
    validate_all = "--all" in args
    if validate_all:
        args.remove("--all")
    target = args[0] if args else None
    return run_validate(target, validate_all=validate_all, sandbox_only=sandbox_only)


if __name__ == "__main__":
    sys.exit(main())
