"""Loader + validator for `platform/ontology/links/*.yaml`.

Three file patterns, all decoded into a flat list of `Link` records
(one per storage label) for downstream consumers:

  1. **Verb-rooted** (most common):

         # offered.yaml
         verb: offered
         by:  {from: product, to: organization}      # → label `offered_by`
         for: {from: offer,   to: product}           # → label `offered_for`

     The `verb:` key names the past-participle root. Every other top-level
     key is a preposition; its value is a per-form dict carrying
     `from`/`to`/`card?`/`link_vals?`/`inverse_of?`. Storage label =
     `<verb>_<preposition>`.

  2. **Bare-preposition** (stative widened):

         # for.yaml
         preposition: for
         to: node          # multi-target; per-shape target in each shape's links: block

     One label per file. Storage label = the preposition itself
     (`for`/`in`/`at`/`on`/`with`/`under`). Multi-target widening keeps
     the registry small for stative role-noun cases where the suffix
     would have been the target shape name.

  3. **Single-form** (everything else):

         # subsidiary_of.yaml — stative role-noun (noun ≠ target shape)
         from: organization
         to: organization
         card: many_to_many                          # default; can omit

     Storage label = the file's stem. Used for canonical forward verbs
     with no group (`follows`, `treats`), stative role-nouns
     (`subsidiary_of`, `subtask_of`, `part_of`), and any one-off label.

Cardinality defaults to `many_to_many` if omitted. `link_vals` defaults
to `{}`. `inverse_of` is optional; when present, names a sibling label
to mark this form as the reverse direction (the other side is the
canonical storage label).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


@dataclass
class Link:
    """One storage label's declaration — the flattened form every
    downstream emitter consumes."""
    name: str                              # storage label (e.g. "offered_by")
    from_kind: str                         # source shape
    to_kind: str                           # target shape (or "node" for multi-target)
    cardinality: str = "many_to_many"      # one_to_one | one_to_many | many_to_many
    link_vals: dict[str, Any] = field(default_factory=dict)
    inverse_of: str | None = None          # sibling label, if this is the reverse direction
    reverse_name: str | None = None        # active-form name used as a derived
                                           # reverse-accessor (e.g. `owned_by`'s
                                           # `reverse_name` is `owns`). When unset
                                           # codegen falls back to a stem heuristic.
    # Provenance — set by the loader so downstream tooling can map back to
    # the verb/preposition file even after flattening.
    group_file: str | None = None          # YAML filename (e.g. "offered.yaml")
    verb_root: str | None = None           # the `verb:` value, if grouped under one
    preposition_root: str | None = None    # the `preposition:` value, if bare-prep file


VALID_CARDINALITIES = {"one_to_one", "one_to_many", "many_to_many"}
SPECIAL_KINDS = {"node", "actor"}

# File-level metadata keys — skip these when iterating Pattern 1 form keys.
# This set intentionally EXCLUDES `to`, `from`, `for`, etc. — those ARE valid
# preposition forms (e.g. `born_to`, `extended_to`, `posted_to`). Reserving
# them at top level would silently drop those labels.
VERB_FILE_METADATA = {"verb", "forward", "inverse"}


def derive_reverse_name(link: "Link") -> str | None:
    """Reverse-accessor name for a canonical (past-participle) link.

    Returns the link's explicit `reverse_name:` annotation, or None.

    No stem heuristic — English orthography doesn't reliably derive
    third-person-singular-present from a past-participle ("invoked" vs
    "blocked" look identical but their stems differ in whether they end
    in `e`). Wrong derivations are worse than missing ones; the registry
    annotates each pair explicitly when an active reading exists.
    """
    return link.reverse_name


def _parse_form(form: Any, label: str) -> dict[str, Any]:
    """Normalize a one-liner form dict, defaulting card/link_vals."""
    if not isinstance(form, dict):
        raise ValueError(f"link `{label}`: form must be a dict, got {type(form).__name__}")
    return {
        "from": str(form.get("from") or "node"),
        "to": str(form.get("to") or "node"),
        "cardinality": str(form.get("card") or form.get("cardinality") or "many_to_many"),
        "link_vals": dict(form.get("link_vals") or {}),
        "inverse_of": form.get("inverse_of"),
        "reverse_name": form.get("reverse_name"),
    }


def _load_file(path: Path) -> list[Link]:
    """Parse one YAML file → list of Link records (one per storage label)."""
    try:
        data = yaml.safe_load(path.read_text())
    except yaml.YAMLError as e:
        raise ValueError(f"{path.name}: parse error: {e}")
    if not isinstance(data, dict):
        return []

    out: list[Link] = []

    if "verb" in data:
        # Pattern 1 — verb-rooted, suffix-keyed prepositions
        verb = str(data["verb"]).strip()
        for key, val in data.items():
            if key in VERB_FILE_METADATA:
                continue
            label = f"{verb}_{key}"
            f = _parse_form(val, label)
            out.append(Link(
                name=label,
                from_kind=f["from"], to_kind=f["to"],
                cardinality=f["cardinality"], link_vals=f["link_vals"],
                inverse_of=f["inverse_of"], reverse_name=f["reverse_name"],
                group_file=path.name, verb_root=verb,
            ))
        return out

    if "preposition" in data:
        # Pattern 2 — bare preposition, multi-target stative.
        # YAML 1.1 implicitly resolves bare `on`/`off`/`yes`/`no` to booleans,
        # so trust the file stem rather than the parsed value. Authors should
        # still quote (`preposition: "on"`) for readability.
        prep = path.stem
        out.append(Link(
            name=prep,
            from_kind=str(data.get("from") or "node"),
            to_kind=str(data.get("to") or "node"),
            cardinality=str(data.get("card") or data.get("cardinality") or "many_to_many"),
            link_vals=dict(data.get("link_vals") or {}),
            inverse_of=data.get("inverse_of"),
            reverse_name=data.get("reverse_name"),
            group_file=path.name, preposition_root=prep,
        ))
        return out

    # Pattern 3 — single-form file (stem = label)
    out.append(Link(
        name=path.stem,
        from_kind=str(data.get("from") or "node"),
        to_kind=str(data.get("to") or "node"),
        cardinality=str(data.get("card") or data.get("cardinality") or "many_to_many"),
        link_vals=dict(data.get("link_vals") or {}),
        inverse_of=data.get("inverse_of"),
        reverse_name=data.get("reverse_name"),
        group_file=path.name,
    ))
    return out


def load(links_dir: Path) -> list[Link]:
    """Load every `links/*.yaml` and return a sorted flat list of Link
    records. Skips `_`/`.`-prefixed files."""
    out: list[Link] = []
    for f in sorted(links_dir.glob("*.yaml")):
        if f.name.startswith(("_", ".")):
            continue
        out.extend(_load_file(f))
    return sorted(out, key=lambda l: l.name)


def validate(links: list[Link], shape_names: set[str]) -> tuple[list[str], list[str]]:
    """Validate a loaded link list against the shape registry.

    Returns (errors, warnings). Errors fail codegen; warnings are
    surfaced as `lint [warn]:` lines.
    """
    errors: list[str] = []
    warnings: list[str] = []
    resolved = shape_names | SPECIAL_KINDS

    def _kind_ok(k: str) -> bool:
        return k in resolved or "|" in k  # union strings tolerated, warn separately

    seen: dict[str, str] = {}  # label -> first file that declared it
    for link in links:
        if link.name in seen:
            errors.append(
                f"link `{link.name}`: declared twice "
                f"(first in {seen[link.name]}, again in {link.group_file})"
            )
            continue
        seen[link.name] = link.group_file or "?"

        if link.cardinality not in VALID_CARDINALITIES:
            errors.append(
                f"link `{link.name}` ({link.group_file}): invalid cardinality "
                f"'{link.cardinality}' (expected one of {sorted(VALID_CARDINALITIES)})"
            )
        if not _kind_ok(link.from_kind):
            errors.append(
                f"link `{link.name}` ({link.group_file}): unknown from_kind "
                f"'{link.from_kind}'"
            )
        elif "|" in link.from_kind:
            warnings.append(
                f"link `{link.name}`: from_kind '{link.from_kind}' is a union — "
                f"widen to `actor`/`node` or pick one"
            )
        if not _kind_ok(link.to_kind):
            errors.append(
                f"link `{link.name}` ({link.group_file}): unknown to_kind "
                f"'{link.to_kind}'"
            )
        elif "|" in link.to_kind:
            warnings.append(
                f"link `{link.name}`: to_kind '{link.to_kind}' is a union"
            )

        if link.inverse_of and link.inverse_of not in {l.name for l in links}:
            warnings.append(
                f"link `{link.name}`: inverse_of=`{link.inverse_of}` "
                f"does not resolve to another link"
            )

    return errors, warnings


if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    import ir
    platform_root = Path(__file__).parent.parent
    shapes = ir.load_shapes(platform_root / "ontology" / "shapes")
    shape_names = {s.name for s in shapes}
    links = load(platform_root / "ontology" / "links")
    print(f"Loaded {len(links)} link records from platform/ontology/links")
    # Group provenance summary
    verbs: dict[str, int] = {}
    preps: dict[str, int] = {}
    singles = 0
    for l in links:
        if l.verb_root:
            verbs[l.verb_root] = verbs.get(l.verb_root, 0) + 1
        elif l.preposition_root:
            preps[l.preposition_root] = preps.get(l.preposition_root, 0) + 1
        else:
            singles += 1
    print(f"  {len(verbs)} verb groups → {sum(verbs.values())} labels")
    print(f"  {len(preps)} bare-preposition files")
    print(f"  {singles} single-form files")
    errors, warnings = validate(links, shape_names)
    if warnings:
        print(f"\n{len(warnings)} warnings:")
        for w in warnings[:10]:
            print(f"  warn: {w}")
        if len(warnings) > 10:
            print(f"  … and {len(warnings) - 10} more")
    if errors:
        print(f"\n{len(errors)} errors:")
        for e in errors:
            print(f"  err:  {e}")
        sys.exit(1)
    print("\nValidation: OK")
