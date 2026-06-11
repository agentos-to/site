"""agent-sdk guide — points at the canonical app docs."""

import sys
from pathlib import Path


GUIDE_URL = "https://agentos.to/apps.md"


def print_guide():
    """Print the app development guide.

    Preference order:
    1. Local docs/apps.md in the agentos-sdk repo (walks up from cwd)
    2. Canonical URL pointer (if no local docs found)
    """
    # Walk up from cwd looking for agentos-sdk/docs/apps.md
    for parent in [Path.cwd(), *Path.cwd().parents]:
        candidate = parent / "docs" / "apps.md"
        if candidate.is_file() and (parent / "shapes").is_dir():
            print(candidate.read_text())
            return
        candidate = parent / "agentos-sdk" / "docs" / "apps.md"
        if candidate.is_file():
            print(candidate.read_text())
            return

    # No local copy — print the pointer
    print(f"The app development guide is hosted at:\n\n  {GUIDE_URL}\n", file=sys.stderr)
    print("Or read it locally at: agentos-sdk/docs/apps.md", file=sys.stderr)
    sys.exit(1)
