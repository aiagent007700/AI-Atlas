"""Focused static checks for Sprint 6 files.

This intentionally checks only the files introduced by Sprint 6 so it does not
change the behavior of an existing repository-wide lint setup.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
TARGETS = [
    ROOT / "docs" / "safety",
    ROOT / "docs" / "visual" / "trustworthy-ai-system-map.md",
    ROOT / "docs" / "updates" / "sprint-06.md",
]

errors = []


def files_under(target):
    if target.is_file():
        return [target]
    return sorted(target.rglob("*.md"))


def check_markdown(path):
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    rel = path.relative_to(ROOT)

    if not lines or lines[0].strip() != "---":
        errors.append(f"{rel}: missing front matter start")
        return
    try:
        end = lines.index("---", 1)
    except ValueError:
        errors.append(f"{rel}: missing front matter end")
        return

    front = "\n".join(lines[1:end])
    if not re.search(r"^id:\s*\S+", front, re.M):
        errors.append(f"{rel}: missing id")
    if not re.search(r"^title:\s*.+", front, re.M):
        errors.append(f"{rel}: missing title")

    in_fence = False
    for number, line in enumerate(lines, 1):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence and re.search(r"\{[^\n]*\}", line):
            errors.append(f"{rel}:{number}: possible MDX expression")
        if not in_fence and line.startswith("title:") and ":" in line[6:]:
            value = line[6:].strip()
            if not (value.startswith('"') or value.startswith("'")):
                errors.append(f"{rel}:{number}: unquoted colon in title")

    if in_fence:
        errors.append(f"{rel}: unclosed code fence")

    # Sprint 6 pages intentionally contain no internal Markdown links. This
    # prevents accidental route-base errors; source links are external URLs.

for target in TARGETS:
    for path in files_under(target):
        check_markdown(path)

if errors:
    print("Sprint 6 preflight failed:")
    print("\n".join(f"- {item}" for item in errors))
    sys.exit(1)

print("Sprint 6 preflight passed: front matter, MDX-sensitive text, and code fences are clean.")
