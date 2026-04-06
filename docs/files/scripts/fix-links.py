#!/usr/bin/env python3
"""
fix-links.py  —  Post-render script for Quarto
Rewrites every <a class="no-external"> link in the rendered HTML so that:
  - class="no-external" is removed
  - target="_blank" and rel="noopener noreferrer" are added

Usage (run after quarto render):
    python3 fix-links.py docs/media.html

Or add to _quarto.yml as a post-render script:
    project:
      post-render:
        - python3 fix-links.py docs/media.html
"""

import re
import sys
from pathlib import Path


def fix_links(html: str) -> str:
    def replace_link(m: re.Match) -> str:
        tag = m.group(0)
        # Remove class="no-external" (with any surrounding whitespace)
        tag = re.sub(r'\s*class="no-external"', '', tag)
        # Add target and rel before the closing >
        tag = tag.rstrip('>')
        tag += ' target="_blank" rel="noopener noreferrer">'
        return tag

    return re.sub(
        r'<a\s[^>]*class="no-external"[^>]*>',
        replace_link,
        html
    )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 fix-links.py <path/to/file.html>")
        sys.exit(1)

    path = Path(sys.argv[1])
    original = path.read_text(encoding="utf-8")
    fixed = fix_links(original)
    path.write_text(fixed, encoding="utf-8")

    changed = original.count('class="no-external"')
    print(f"Fixed {changed} link(s) in {path}")
