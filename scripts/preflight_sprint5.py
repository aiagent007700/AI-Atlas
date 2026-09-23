"""Static preflight checks for Sprint 5 content.

Run from the repository root with:
    python scripts/preflight_sprint5.py
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
TARGETS = [
    ROOT / "docs" / "engineering",
    ROOT / "docs" / "visuals" / "production-ai-system-map.md",
    ROOT / "docs" / "updates" / "sprint-05.md",
]

errors = []
checked = []


def iter_markdown(target):
    if target.is_dir():
        yield from sorted(target.rglob("*.md"))
    elif target.is_file():
        yield target


def front_matter(text, path):
    if not text.startswith("---\n"):
        errors.append(f"{path}: missing front matter opening")
        return
    end = text.find("\n---", 4)
    if end < 0:
        errors.append(f"{path}: missing front matter closing")
        return
    block = text[4:end]
    if not re.search(r"^title:\s+.+$", block, re.M):
        errors.append(f"{path}: missing title")
    for line in block.splitlines():
        if line.startswith("title:") and ":" in line[len("title:"):]:
            value = line.split(":", 1)[1].strip()
            if not (value.startswith('"') and value.endswith('"')):
                errors.append(f"{path}: title contains colon but is not quoted")


def body_outside_fences(text, path):
    in_code = False
    body = []
    for line in text.splitlines(keepends=True):
        if line.startswith("```"):
            in_code = not in_code
            body.append("")
        elif in_code:
            body.append("")
        else:
            body.append(line)
    if in_code:
        errors.append(f"{path}: unclosed fenced code block")
    return "".join(body)


def check_links(text, path):
    for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        clean = target.split("#", 1)[0]
        candidate = (path.parent / clean).resolve()
        candidates = [candidate, candidate.with_suffix(".md"), candidate / "index.md"]
        if not any(c.exists() for c in candidates):
            errors.append(f"{path}: unresolved local link {target}")


for target in TARGETS:
    for path in iter_markdown(target):
        checked.append(path)
        text = path.read_text(encoding="utf-8")
        front_matter(text, path)
        body = body_outside_fences(text, path)
        if "$$" in body:
            errors.append(f"{path}: raw math delimiter outside code fence")
        if re.search(r"(?<![\w])\{[^\n{}]+\}(?![\w])", body):
            errors.append(f"{path}: possible unescaped MDX expression")
        if "className={styles." in body:
            errors.append(f"{path}: possible invalid CSS module expression")
        check_links(text, path)

if errors:
    print("Sprint 5 preflight failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"Sprint 5 preflight passed for {len(checked)} Markdown files.")
