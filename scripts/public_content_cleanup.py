#!/usr/bin/env python3
"""Normalize public AI Atlas terminology and paths.

Run from the repository root:
  python scripts/public_content_cleanup.py
  python scripts/public_content_cleanup.py --check

The migration is intentionally idempotent. It renames public tutorial paths,
updates references and IDs, removes obsolete release-only artifacts, and then
checks that public tutorial content contains no Sprint terminology.
"""
from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PATH_RENAMES = [
    ("docs/updates/sprint-03.md", "docs/updates/living-intelligence.md"),
    ("docs/updates/sprint-04.md", "docs/updates/ai-systems-layer.md"),
    ("docs/updates/sprint-05.md", "docs/updates/production-ai-engineering.md"),
    ("docs/updates/sprint-06.md", "docs/updates/trust-security-governance.md"),
    ("docs/agents/sprint-07", "docs/agents/agent-systems"),
    ("docs/multimodal/sprint-08", "docs/multimodal/multimodal-and-generative-ai"),
]

FILE_RENAMES = [
    ("docs/agents/agent-systems/sprint-07-update.md", "docs/agents/agent-systems/module-update.md"),
]

LEGACY_ROOT_FILES = {
    "SPRINT-02.md", "SPRINT-03.md", "SPRINT-04-INTEGRATION.md",
    "SPRINT-05-INTEGRATION.md", "SPRINT-06-INTEGRATION.md",
    "SPRINT-07-INTEGRATION.md", "SPRINT-08-INTEGRATION.md",
}


def move_path(old_rel: str, new_rel: str) -> None:
    old, new = ROOT / old_rel, ROOT / new_rel
    if old.exists() and not new.exists():
        new.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(old), str(new))
    elif old.exists() and new.exists():
        if old.is_dir() and new.is_dir():
            for child in old.iterdir():
                target = new / child.name
                if not target.exists():
                    shutil.move(str(child), str(target))
            try:
                old.rmdir()
            except OSError:
                pass
        else:
            raise RuntimeError(f"Both old and new paths exist: {old} and {new}")


def public_files():
    paths = []
    docs = ROOT / "docs"
    if docs.exists():
        paths.extend(docs.rglob("*.md"))
    for rel in ("README.md", "sidebars.ts", "docusaurus.config.ts"):
        p = ROOT / rel
        if p.exists(): paths.append(p)
    return paths


def normalize_text(text: str) -> str:
    # First update path references so links and sidebar IDs point to the new routes.
    for old, new in sorted(PATH_RENAMES, key=lambda x: len(x[0]), reverse=True):
        text = text.replace(old, new)
        text = text.replace(old.replace("docs/", ""), new.replace("docs/", ""))

    # Normalize IDs used by the renamed content. IDs are internal but keeping them
    # semantic prevents stale release terminology from leaking into generated data.
    text = re.sub(r"(?m)^(\s*id:\s*)sprint-07-agent-loop\b", r"\1agent-systems-agent-loop", text)
    text = re.sub(r"(?m)^(\s*id:\s*)sprint-07-agent-or-workflow\b", r"\1agent-systems-agent-or-workflow", text)
    text = re.sub(r"(?m)^(\s*id:\s*)sprint-07-evaluation-observability\b", r"\1agent-systems-evaluation-observability", text)
    text = re.sub(r"(?m)^(\s*id:\s*)sprint-07-index\b", r"\1agent-systems-index", text)
    text = re.sub(r"(?m)^(\s*id:\s*)sprint-07-labs\b", r"\1agent-systems-labs", text)
    text = re.sub(r"(?m)^(\s*id:\s*)sprint-07-multi-agent\b", r"\1agent-systems-multi-agent", text)
    text = re.sub(r"(?m)^(\s*id:\s*)sprint-07-protocols\b", r"\1agent-systems-protocols", text)
    text = re.sub(r"(?m)^(\s*id:\s*)sprint-07-references\b", r"\1agent-systems-references", text)
    text = re.sub(r"(?m)^(\s*id:\s*)sprint-07-security-recovery\b", r"\1agent-systems-security-recovery", text)
    text = re.sub(r"(?m)^(\s*id:\s*)sprint-07-skills\b", r"\1agent-systems-skills", text)
    text = re.sub(r"(?m)^(\s*id:\s*)sprint-07-update\b", r"\1agent-systems-update", text)
    text = re.sub(r"(?m)^(\s*id:\s*)sprint-08\b", "id: multimodal-and-generative-ai", text)
    text = re.sub(r"(?m)^(\s*id:\s*)sprint-0([3-6])\b", r"\1module-0\2", text)

    # Public-facing naming. Apply specific numbered phrases before the generic rule.
    replacements = [
        (r"(?i)\bSprint\s*0?3\b", "Living intelligence layer"),
        (r"(?i)\bSprint\s*0?4\b", "AI systems layer"),
        (r"(?i)\bSprint\s*0?5\b", "Production AI engineering"),
        (r"(?i)\bSprint\s*0?6\b", "Trust, security, and governance"),
        (r"(?i)\bSprint\s*0?7\b", "Agents, skills, and protocols"),
        (r"(?i)\bSprint\s*0?8\b", "Multimodal and generative AI"),
        (r"(?i)\bthis sprint\b", "this module"),
        (r"(?i)\bthe sprint\b", "the module"),
        (r"(?i)\bthat sprint\b", "that module"),
        (r"(?i)\bsprint\b", "module"),
    ]
    for pattern, replacement in replacements:
        text = re.sub(pattern, replacement, text)
    return text


def apply() -> None:
    for old, new in PATH_RENAMES:
        move_path(old, new)
    for old, new in FILE_RENAMES:
        move_path(old, new)

    # Remove release-window-only documents from the public repository root.
    for name in LEGACY_ROOT_FILES:
        p = ROOT / name
        if p.exists(): p.unlink()
    for p in ROOT.glob("sprint-*-manifest.json"):
        p.unlink()
    for p in (ROOT / "scripts").glob("preflight_sprint*.py") if (ROOT / "scripts").exists() else []:
        p.unlink()

    for p in public_files():
        original = p.read_text(encoding="utf-8")
        updated = normalize_text(original)
        if updated != original:
            p.write_text(updated, encoding="utf-8")


def violations():
    found = []
    for p in public_files():
        text = p.read_text(encoding="utf-8")
        for i, line in enumerate(text.splitlines(), 1):
            if re.search(r"(?i)\bsprint\b", line):
                found.append(f"{p.relative_to(ROOT)}:{i}: {line.strip()}")
            if re.search(r"(?i)(agents/sprint-07|multimodal/sprint-08|updates/sprint-0[3-6])", line):
                found.append(f"{p.relative_to(ROOT)}:{i}: stale path")
    return found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="check without changing files")
    args = ap.parse_args()
    if not args.check:
        apply()
    problems = violations()
    if problems:
        print("Public terminology check failed:")
        print("\n".join(problems))
        raise SystemExit(1)
    print("Public terminology check passed: no Sprint references or stale release paths found.")

if __name__ == "__main__":
    main()
