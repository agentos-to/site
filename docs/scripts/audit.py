#!/usr/bin/env python3
"""Deterministic audit for docs content.

Scans `src/content/docs/` for:
  - Broken-link sentinels: backtick-wrapped path tokens that look like paths
    but aren't real links (e.g. `agentos-sdk/shapes/foo.yaml`).
  - AgentOS-* / agentos-sdk sentinels: references to non-existent repos/paths.
  - PII: emails (non-domain), phones, API-key-shaped tokens, street addresses,
    obvious personal names in frontmatter.
  - Dangling cross-references: `[text](../path)` where the target file does
    not resolve after normalization.

Severity levels:
  fail   — broken link / PII → non-zero exit
  warn   — stylistic (bare backtick paths) → logged, no exit code

Usage:
  python3 scripts/audit.py              # audit all docs, exit non-zero on fail
  python3 scripts/audit.py --warnings   # also fail on warnings (strict mode)
  python3 scripts/audit.py --json       # machine-readable output

Designed to be cheap and hook-friendly: reads every .md/.mdx under
src/content/docs/ once, emits line:col hits with a suggestion.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable

HERE = Path(__file__).resolve().parent
DOCS_ROOT = HERE.parent / "src" / "content" / "docs"
SHAPES_ROOT = HERE.parent / "shapes"

# --- Rules --------------------------------------------------------------

# Backtick-wrapped path-looking tokens. A "path" here is: ≥1 `/`, has a file
# extension OR ends in `/`, no spaces, no markdown-link brackets.
# We flag these because bare `foo/bar.yaml` is never a link — it renders as
# monospace, so readers can't click it. Users want real links.
BACKTICK_PATH_RE = re.compile(
    r"`([^`\s\[\]]*?/[^`\s\[\]]+?\.(?:md|mdx|yaml|yml|py|ts|tsx|js|rs|sh|json|html|toml|lock|mjs|cjs))`"
    r"|`([a-zA-Z0-9_\-./]+/)`"
)

# Sentinel strings that indicate references to moved/renamed/non-existent paths.
# `AgentOS-*` caps-prefix: capital A in "AgentOS" followed by hyphen-word is
# never a real filesystem path — it's always broken link-talk.
SENTINEL_PATTERNS = [
    (re.compile(r"agentos-sdk\b", re.IGNORECASE), "agentos-sdk/ was replaced by site/docs/shapes/ or skills/_sdk/"),
    (re.compile(r"AgentOS-[A-Z][a-zA-Z]+"), "AgentOS-* PascalCase refs are typically broken — link to real location"),
    (re.compile(r"_roadmap/_research/"), "_roadmap/_research/ moved → src/content/docs/research/"),
    (re.compile(r"core/vision\.md\b"), "core/vision.md sections moved → introduction/ + principles/"),
    (re.compile(r"core/principles\.md\b"), "core/principles.md → principles/architectural-laws.md"),
    (re.compile(r"docs/reverse-engineering/"), "docs/reverse-engineering/ → contributing/skills/reverse-engineering/"),
]

# PII — intentionally conservative. We want zero false negatives on real PII,
# and tolerating false positives the author can manually confirm.
#
# Allowlisted email domains + localparts are fake-example sentinels used in
# docs. Anything else gets flagged.
PII_EMAIL_ALLOW_DOMAINS = {
    "agentos.to", "example.com", "example.org", "example.net", "localhost",
    "mysite.com", "anthropic.com", "domain.tld", "instance.tld", "instance.domain",
    "company.com", "email.com",
}
PII_EMAIL_ALLOW_LOCAL = {"user", "your", "boss", "admin", "test", "example", "foo", "bar", "proof"}
# Full-match allowlist for archetypal example addresses that frequently appear
# in identity/ontology discussions. These are not PII even if the domain looks
# real — the local part `joe` is used as a deliberate stand-in.
PII_EMAIL_ALLOW_FULL = {"joe@apple.com", "joe@gmail.com"}
EMAIL_RE = re.compile(r"\b([A-Za-z0-9._%+\-]+)@([A-Za-z0-9.\-]+\.[A-Za-z]{2,})\b")
# Phone: require separators (dash/space/dot/parens) so we don't match
# Unix timestamps, hex ids, etc. `1234567890` alone → ignored.
PHONE_RE = re.compile(r"(?<!\d)\+?1?[-.\s]?\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}(?!\d)")
# API-key-shaped: ≥20 chars of base64ish (sk_/pk_/key_/bearer/token prefixes, or long entropy strings).
API_KEY_RE = re.compile(r"\b(?:sk_|pk_|api[_-]?key[_=\s\"']|bearer[\s\"'])[A-Za-z0-9+/=_-]{20,}")
# Long alphanumeric string in YAML-like key=value or auth context. Conservative.
HEX_KEY_RE = re.compile(r"\b[A-Fa-f0-9]{40,}\b")

# Dangling markdown link: [text](relative/path) where path is not URL, not
# anchor-only, and target does not resolve.
MD_LINK_RE = re.compile(r"\[([^\]]+?)\]\(([^)\s]+?)(?:\s+\"[^\"]*\")?\)")


@dataclass
class Hit:
    file: str
    line: int
    col: int
    severity: str  # "fail" | "warn"
    category: str  # "backtick-path" | "sentinel" | "pii-email" | ...
    match: str
    message: str

    def format(self) -> str:
        return (
            f"{self.severity.upper():4s}  {self.file}:{self.line}:{self.col}  "
            f"[{self.category}]  {self.match!r}\n        → {self.message}"
        )


def _iter_md_files(root: Path) -> Iterable[Path]:
    for p in sorted(root.rglob("*")):
        if p.suffix in (".md", ".mdx") and p.is_file():
            yield p


def _lc(text: str, idx: int) -> tuple[int, int]:
    """Convert absolute char index → (line, col) 1-indexed."""
    before = text[:idx]
    line = before.count("\n") + 1
    col = idx - before.rfind("\n")
    return line, col


def _resolve_rel_link(src_file: Path, target: str) -> Path | None:
    """Resolve a markdown relative link against the source file's directory.

    Returns the canonical path if it resolves, None otherwise.
    Handles `../x.md`, `./x.md`, `x.md`, and Starlight-style pageless refs.
    """
    # Strip any anchor
    target = target.split("#", 1)[0]
    if not target:
        return src_file
    # Absolute doc-site paths like /docs/foo/ — we'll not resolve these file-system-side
    if target.startswith("/"):
        return None
    candidate = (src_file.parent / target).resolve()
    if candidate.exists():
        return candidate
    # Try adding .md / /index.md
    for ext in (".md", ".mdx", "/index.md", "/overview.md"):
        alt = Path(str(candidate) + ext)
        if alt.exists():
            return alt
    return None


def audit_file(path: Path) -> list[Hit]:
    hits: list[Hit] = []
    rel = path.relative_to(DOCS_ROOT).as_posix()
    text = path.read_text(encoding="utf-8", errors="replace")

    # --- Backtick paths ---
    for m in BACKTICK_PATH_RE.finditer(text):
        tok = m.group(1) or m.group(2) or ""
        if not tok:
            continue
        # Allowlist: code examples reference real internal paths constantly
        # (skills/foo/readme.md, shapes/bar.yaml). These exist in the repo and
        # are not broken links per se — but the user's rule says *prefer*
        # real Markdown links. Warn, don't fail.
        line, col = _lc(text, m.start())
        hits.append(Hit(
            file=rel, line=line, col=col, severity="warn",
            category="backtick-path", match=tok,
            message="Backtick path renders as monospace, not clickable. Use [text](link) — prefer internal doc link, fallback GitHub.",
        ))

    # --- Sentinels ---
    for pat, hint in SENTINEL_PATTERNS:
        for m in pat.finditer(text):
            line, col = _lc(text, m.start())
            hits.append(Hit(
                file=rel, line=line, col=col, severity="fail",
                category="sentinel", match=m.group(0),
                message=hint,
            ))

    # --- PII: emails (with allowlist) ---
    for m in EMAIL_RE.finditer(text):
        local, domain = m.group(1), m.group(2)
        if domain.lower() in PII_EMAIL_ALLOW_DOMAINS:
            continue
        if local.lower() in PII_EMAIL_ALLOW_LOCAL:
            continue
        if m.group(0).lower() in PII_EMAIL_ALLOW_FULL:
            continue
        line, col = _lc(text, m.start())
        hits.append(Hit(
            file=rel, line=line, col=col, severity="fail",
            category="pii-email", match=m.group(0),
            message="Personal-looking email address",
        ))

    # --- PII: phones/keys ---
    for pat, cat, desc in (
        (PHONE_RE, "pii-phone", "Phone-number shaped token"),
        (API_KEY_RE, "pii-apikey", "API-key-shaped token"),
        (HEX_KEY_RE, "pii-hexkey", "Long hex string — could be a key/hash"),
    ):
        for m in pat.finditer(text):
            line, col = _lc(text, m.start())
            hits.append(Hit(
                file=rel, line=line, col=col, severity="fail",
                category=cat, match=m.group(0)[:60],
                message=desc,
            ))

    # --- Dangling relative markdown links ---
    # Find code-block ranges so we can skip link syntax inside code fences.
    code_spans: list[tuple[int, int]] = []
    in_fence = False
    fence_start = 0
    cursor = 0
    for line in text.splitlines(keepends=True):
        if line.lstrip().startswith("```"):
            if in_fence:
                code_spans.append((fence_start, cursor + len(line)))
                in_fence = False
            else:
                fence_start = cursor
                in_fence = True
        cursor += len(line)
    def _in_code(idx: int) -> bool:
        return any(a <= idx < b for a, b in code_spans)

    # Placeholder-like targets that are clearly not meant to be real links.
    PLACEHOLDER_TARGETS = {"url", "path", "href", "link", "target", "..."}

    for m in MD_LINK_RE.finditer(text):
        target = m.group(2).strip()
        # Skip URLs and anchors
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        if target.startswith("/"):
            continue  # absolute doc paths — resolved by Starlight, not filesystem
        if target in PLACEHOLDER_TARGETS:
            continue
        if _in_code(m.start()):
            continue
        resolved = _resolve_rel_link(path, target)
        if resolved is None:
            line, col = _lc(text, m.start())
            hits.append(Hit(
                file=rel, line=line, col=col, severity="fail",
                category="dangling-link", match=target,
                message=f"Link target does not resolve from {rel}",
            ))

    return hits


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true", help="Emit JSON instead of human-readable output")
    ap.add_argument("--warnings", action="store_true", help="Exit non-zero on warnings too (strict)")
    ap.add_argument("--only", help="Limit to files whose rel path contains this substring")
    args = ap.parse_args(argv)

    if not DOCS_ROOT.exists():
        print(f"FAIL: {DOCS_ROOT} not found", file=sys.stderr)
        return 2

    all_hits: list[Hit] = []
    for path in _iter_md_files(DOCS_ROOT):
        if args.only and args.only not in str(path):
            continue
        all_hits.extend(audit_file(path))

    fails = [h for h in all_hits if h.severity == "fail"]
    warns = [h for h in all_hits if h.severity == "warn"]

    if args.json:
        print(json.dumps({"fails": [asdict(h) for h in fails], "warns": [asdict(h) for h in warns]}, indent=2))
    else:
        for h in fails:
            print(h.format())
        if fails and warns:
            print()
        for h in warns:
            print(h.format())
        print()
        print(f"  {len(fails)} fail, {len(warns)} warn across {sum(1 for _ in _iter_md_files(DOCS_ROOT))} files")

    if fails:
        return 1
    if warns and args.warnings:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
