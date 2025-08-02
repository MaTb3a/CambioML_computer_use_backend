"""Utility helpers for working with VNC sessions.

These are simple placeholders used for testing and do not provide real VNC
functionality.
"""


def get_vnc_url(session_id: int) -> str:
    """Return a pseudo URL for a VNC connection."""
    return f"vnc://localhost/{session_id}"

