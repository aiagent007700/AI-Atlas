#!/usr/bin/env python3
"""Static checks for Sprint 7 pages before a Docusaurus build."""
from pathlib import Path
import re
import sys

DOCS = Path(__file__).resolve().parents[1] / "docs" / "agents" / "sprint-07"
errors = []
seen_ids = set()

for path in sorted(DOCS.glob("*.md")):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{path}: missing front matter")
        continue
    end = text.find("\n---\n", 4)
    if end < 0:
        errors.append(f"{path}: unterminated front matter")
        continue
    front = text[4:end]
    body = text[end + 5:]
    m = re.search(r"^id:\s*(\S+)\s*$", front, re.M)
    if not m:
        errors.append(f"{path}: missing id")
    else:
        doc_id = m.group(1)
        if doc_id in seen_ids:
            errors.append(f"{path}: duplicate id {doc_id}")
        seen_ids.add(doc_id)
    title = re.search(r"^title:\s*(.+)$", front, re.M)
    if title and ":" in title.group(1) and not title.group(1).strip().startswith(('"', "'")):
        errors.append(f"{path}: title containing colon must be quoted")
    if body.count("```") % 2:
        errors.append(f"{path}: unmatched fenced code block")
    # Braces outside fenced code blocks can be interpreted as MDX expressions.
    outside = re.sub(r"```.*?```", "", body, flags=re.S)
    if re.search(r"\{[^\n}]+\}", outside):
        errors.append(f"{path}: possible MDX expression outside code fence")

index = DOCS / "index.md"
if not index.exists():
    errors.append("missing index.md")

if errors:
    print("Sprint 7 preflight failed:")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print(f"Sprint 7 preflight passed: {len(list(DOCS.glob('*.md')))} pages checked")
