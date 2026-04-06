#!/usr/bin/env python3
"""
Run fix-links.py on rendered media.html only when media.qmd changed or HTML
still contains links to fix (e.g. clean rebuild with unchanged qmd).

Usage (from project root, e.g. Quarto post-render):
    python files/scripts/fix-links-if-media-changed.py docs/media.html media.qmd
"""

from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

MARKER = 'class="no-external"'


def _repo_root(script_path: Path) -> Path:
    # files/scripts/thisfile.py -> repo root
    return script_path.resolve().parents[2]


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def main() -> None:
    root = _repo_root(Path(__file__))
    if len(sys.argv) >= 3:
        html = Path(sys.argv[1])
        qmd = Path(sys.argv[2])
        if not html.is_absolute():
            html = root / html
        if not qmd.is_absolute():
            qmd = root / qmd
    else:
        html = root / "docs" / "media.html"
        qmd = root / "media.qmd"

    fix_script = Path(__file__).resolve().parent / "fix-links.py"
    stamp = root / ".quarto" / "fix-links-media.sha256"

    if not html.is_file():
        return
    if not qmd.is_file():
        subprocess.run([sys.executable, str(fix_script), str(html)], check=True)
        return

    qmd_hash = _sha256_file(qmd)
    prev = stamp.read_text(encoding="utf-8").strip() if stamp.is_file() else ""

    text = html.read_text(encoding="utf-8")
    needs_fix = MARKER in text

    if prev == qmd_hash and not needs_fix:
        print("fix-links: skip (media.qmd unchanged, output already processed)")
        return

    if needs_fix:
        subprocess.run([sys.executable, str(fix_script), str(html)], check=True)

    stamp.parent.mkdir(parents=True, exist_ok=True)
    stamp.write_text(qmd_hash + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
