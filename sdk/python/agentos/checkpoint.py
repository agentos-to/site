"""App-level checkpoint/resume for multi-phase workflows.

Save state after each completed unit of work. On restart, load the
checkpoint to skip completed phases.

    from agentos import checkpoint

    state = checkpoint.load(output)
    if state and state.get("phase") >= 2:
        sections = state["sections"]
    else:
        sections = await research_phase(topic)
        checkpoint.save(output, {"phase": 2, "sections": sections})

    checkpoint.clear(output)  # success — remove checkpoint

Checkpoints are opt-in. Apps that don't call save() have no checkpoint
file. The file is `.checkpoint.json` in the app's output directory.
"""

import json
import os


def save(output_dir: str, state: dict):
    """Save checkpoint atomically.

    Writes to a temp file, then renames — so a crash during save
    doesn't corrupt the checkpoint. Called after each completed
    unit of work.

    Args:
        output_dir: Directory for the checkpoint file.
        state: App-specific state dict (must be JSON-serializable).
    """
    path = os.path.join(output_dir, ".checkpoint.json")
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(state, f)
    os.rename(tmp, path)


def load(output_dir: str) -> dict | None:
    """Load checkpoint, or None if no checkpoint exists."""
    path = os.path.join(output_dir, ".checkpoint.json")
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)


def clear(output_dir: str):
    """Remove checkpoint after successful completion."""
    path = os.path.join(output_dir, ".checkpoint.json")
    if os.path.exists(path):
        os.remove(path)
