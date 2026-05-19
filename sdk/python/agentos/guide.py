"""agent-sdk guide — points at the canonical skill docs."""

import sys
from pathlib import Path


GUIDE_URL = "https://agentos.to/skills.md"


def print_guide():
    """Print the skill development guide.

    Preference order:
    1. Local docs/skills.md in the agentos-sdk repo (walks up from cwd)
    2. Canonical URL pointer (if no local docs found)
    """
    # Walk up from cwd looking for agentos-sdk/docs/skills.md
    for parent in [Path.cwd(), *Path.cwd().parents]:
        candidate = parent / "docs" / "skills.md"
        if candidate.is_file() and (parent / "shapes").is_dir():
            print(candidate.read_text())
            return
        candidate = parent / "agentos-sdk" / "docs" / "skills.md"
        if candidate.is_file():
            print(candidate.read_text())
            return

    # No local copy — print the pointer
    print(f"The skill development guide is hosted at:\n\n  {GUIDE_URL}\n", file=sys.stderr)
    print("Or read it locally at: agentos-sdk/docs/skills.md", file=sys.stderr)
    sys.exit(1)
