#!/usr/bin/env python3
"""Static checks for the Deep dives content package."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "deep-dive"
errors = []

if not DOCS.exists():
    errors.append("docs/deep-dive is missing")
else:
    pages = sorted(DOCS.rglob("*.md"))
    if len(pages) < 8:
        errors.append(f"expected at least 8 markdown pages, found {len(pages)}")
    for path in pages:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        if not text.startswith("---\n"):
            errors.append(f"{rel}: missing front matter")
        if text.count("```") % 2:
            errors.append(f"{rel}: unbalanced code fences")
        if re.search(r'(?m)^title: [^\"\n]*:', text):
            errors.append(f"{rel}: front-matter title with colon must be quoted")
        prose = re.sub(r"```.*?```", "", text, flags=re.S)
        if re.search(r"(?<!\\)\{[^}\n]+\}", prose):
            errors.append(f"{rel}: possible MDX expression; escape or use a code fence")
        if re.search(r"(?im)\bsprint\b", text):
            errors.append(f"{rel}: public release terminology found")
        if "<cite>" in text or "<citation>" in text:
            errors.append(f"{rel}: chat citation markup must not appear in artifact content")

if errors:
    print("FAILED")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print("PASS: deep-dive pages passed static checks")
