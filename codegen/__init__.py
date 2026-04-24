"""Codegen modules — one source of truth, many outputs.

Each submodule owns one codegen target. Called from `docs/generate.py`,
which stays lean and acts as the orchestrator.

Pattern: `load_<source>()` reads from the authoritative source (YAML
on disk, engine registry over CLI, etc.). `emit_<target>()` writes
files into a sibling repo (sdk-skills, sdk-apps, docs content, etc.).
No submodule writes outside its declared target tree.
"""
