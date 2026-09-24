#!/usr/bin/env python3
"""Static checks for AI Atlas Sprint 8 Markdown and integration files."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "multimodal" / "sprint-08"
EXPECTED = {
    "index.md", "multimodal-foundations.md", "computer-vision.md",
    "speech-and-audio.md", "diffusion-and-generation.md",
    "video-and-temporal-models.md", "grounding-and-evaluation.md",
    "world-models-and-embodied-ai.md", "production-patterns.md",
    "labs.md", "references.md",
}
errors = []

if not DOCS.exists():
    errors.append(f"Missing directory: {DOCS}")
else:
    actual = {p.name for p in DOCS.glob("*.md")}
    missing = EXPECTED - actual
    if missing:
        errors.append("Missing expected pages: " + ", ".join(sorted(missing)))

for path in sorted(DOCS.glob("*.md")) if DOCS.exists() else []:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{path}: missing front matter start")
        continue
    end = text.find("\n---\n", 4)
    if end < 0:
        errors.append(f"{path}: missing front matter end")
        continue
    fm = text[4:end]
    if not re.search(r"^id:\s*[A-Za-z0-9][A-Za-z0-9-]*$", fm, re.M):
        errors.append(f"{path}: invalid or missing id")
    if not re.search(r'^title:\s*".*"$', fm, re.M):
        errors.append(f"{path}: title must be double-quoted")
    # Detect unescaped MDX-style expressions outside fenced code blocks.
    outside = []
    fenced = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            fenced = not fenced
            continue
        if not fenced:
            outside.append(line)
    if any(re.search(r"\{[^}]+\}", line) for line in outside):
        errors.append(f"{path}: possible MDX expression outside code fence")
    if text.count("```") % 2:
        errors.append(f"{path}: unbalanced code fences")
    # Sprint pages use absolute docs links to avoid fragile relative resolution.
    for target in re.findall(r"\]\(([^)]+)\)", text):
        if target.startswith("./") and not target.startswith("./"):
            errors.append(f"{path}: malformed relative link {target}")

integration = ROOT / "SPRINT-08-INTEGRATION.md"
if not integration.exists():
    errors.append("Missing SPRINT-08-INTEGRATION.md")
else:
    itext = integration.read_text(encoding="utf-8")
    for token in ["multimodal/sprint-08", "preflight_sprint8.py"]:
        if token not in itext:
            errors.append(f"Integration guide missing {token}")

if errors:
    print("Sprint 8 preflight FAILED")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print(f"Sprint 8 preflight passed: {len(list(DOCS.glob('*.md')))} pages checked")
