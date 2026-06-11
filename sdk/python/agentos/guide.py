"""agent-sdk guide — points at the canonical app docs."""

import sys
from pathlib import Path


def print_guide():
    """Print the app development guide.

    The canonical guide is the `apps-overview` document on the engine's
    system volume (`read({id:"apps-overview", volume:"system"})`). Its
    authored source is `core/system-docs/apps/overview.md` — walk up
    from cwd to find the workspace and print it directly.
    """
    for parent in [Path.cwd(), *Path.cwd().parents]:
        candidate = parent / "core" / "system-docs" / "apps" / "overview.md"
        if candidate.is_file():
            print(candidate.read_text())
            return

    print(
        "The app development guide is the `apps-overview` document on the "
        "system volume:\n\n"
        '  agentos call data \'{"op":"read","params":{"id":"apps-overview","volume":"system"}}\'\n\n'
        "Authored source: core/system-docs/apps/overview.md (not found by "
        "walking up from cwd — run from inside the agentos workspace).",
        file=sys.stderr,
    )
    sys.exit(1)
