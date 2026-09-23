#!/usr/bin/env python3
"""Small zero-dependency checks for Markdown front matter and generated updates."""
from pathlib import Path
import re
import sys

errors = []
for path in sorted(Path("docs").rglob("*.md")):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{path}: missing front matter")
        continue
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        errors.append(f"{path}: malformed front matter")
        continue
    front = match.group(1)
    title = next((line for line in front.splitlines() if line.startswith("title:")), None)
    if title and ":" in title[len("title:"):].strip() and not title.split("title:", 1)[1].strip().startswith(('"', "'")):
        errors.append(f"{path}: title containing ':' must be quoted")

if errors:
    print("Content validation failed:")
    print("\n".join(f"- {item}" for item in errors))
    sys.exit(1)
print("Content validation passed.")
