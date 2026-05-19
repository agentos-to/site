"""Typed shape dicts — re-exports from the generated module.

Usage:
    from agentos.shapes import Person, Book, Post

Classes are generated from `agentos-sdk/shapes/*.yaml` by `generate.py`
at the repo root. Run it from the agentos-sdk repo to regenerate after
shape changes:

    python generate.py               # Python + TypeScript
    python generate.py --lang python # Python only
"""

from __future__ import annotations

from agentos._generated import *  # noqa: F401,F403
