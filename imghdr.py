"""Minimal imghdr shim to satisfy environments missing the stdlib module.

This implements a tiny subset of the stdlib `imghdr.what` used by Streamlit
to detect common image types. It avoids adding a non-existent package to
`requirements.txt` and is safe to include in the repo.
"""
from __future__ import annotations

from typing import Optional


def what(h_or_filename, h: bytes | None = None) -> Optional[str]:
    """Return a string describing the image type based on header bytes.

    Accepts either a filename (str / Path) or header bytes. Returns one of
    'jpeg', 'png', 'gif', 'bmp', 'svg' or None.
    """
    # If a filename was passed, read a small header from the file
    if h is None and isinstance(h_or_filename, (str, bytes)):
        try:
            with open(h_or_filename, 'rb') as f:
                h = f.read(64)
        except Exception:
            return None
    elif h is None:
        return None

    header = h
    if header.startswith(b"\xff\xd8\xff"):
        return 'jpeg'
    if header.startswith(b"\x89PNG\r\n\x1a\n"):
        return 'png'
    if header[:6] in (b'GIF87a', b'GIF89a'):
        return 'gif'
    if header.startswith(b'BM'):
        return 'bmp'
    # A very small check for SVG (text-based)
    low = header.lstrip().lower()
    if b'<svg' in low or low.startswith(b'<?xml'):
        return 'svg'
    return None
