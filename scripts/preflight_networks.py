#!/usr/bin/env python3
"""Validate the networks module before it is copied into a Docusaurus site."""
from pathlib import Path
import re, sys

BASE = Path(__file__).resolve().parents[1]
DOCS = BASE / 'docs' / 'networks'
errors = []

if not DOCS.exists():
    errors.append('docs/networks is missing')

md_files = sorted(DOCS.rglob('*.md')) if DOCS.exists() else []
if len(md_files) < 9:
    errors.append(f'expected at least 9 module pages; found {len(md_files)}')

for p in md_files:
    text = p.read_text(encoding='utf-8')
    rel = p.relative_to(BASE)
    if not text.startswith('---\n'):
        errors.append(f'{rel}: missing front matter')
        continue
    end = text.find('\n---\n', 4)
    if end < 0:
        errors.append(f'{rel}: unterminated front matter')
        continue
    fm = text[4:end]
    if not re.search(r'^id:\s*[^\s]+\s*$', fm, re.M):
        errors.append(f'{rel}: missing id')
    title = re.search(r'^title:\s*(.+)$', fm, re.M)
    if not title:
        errors.append(f'{rel}: missing title')
    elif ':' in title.group(1) and not title.group(1).lstrip().startswith(('"', "'")):
        errors.append(f'{rel}: title with colon must be quoted')
    if re.search(r'(?i)\bsprint\b', text):
        errors.append(f'{rel}: contains forbidden public release terminology')

    # Ignore braces inside fenced code blocks; Docusaurus MDX parses braces elsewhere.
    in_fence = False
    for line_no, line in enumerate(text.splitlines(), 1):
        if line.strip().startswith('```'):
            in_fence = not in_fence
            continue
        if not in_fence and re.search(r'[{}]', line):
            errors.append(f'{rel}:{line_no}: raw brace outside code fence')

    # Check relative links resolve to a markdown page or directory index.
    in_fence = False
    for line_no, line in enumerate(text.splitlines(), 1):
        if line.strip().startswith('```'):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', line):
            target = target.split('#', 1)[0]
            if not target or target.startswith(('http://', 'https://', 'mailto:', '#')):
                continue
            candidate = (p.parent / target).resolve()
            options = [candidate]
            if candidate.suffix == '':
                options += [candidate.with_suffix('.md'), candidate / 'index.md']
            if not any(x.exists() for x in options):
                errors.append(f'{rel}:{line_no}: broken relative link {target}')

if errors:
    print('NETWORKS PREFLIGHT FAILED')
    print('\n'.join(f'- {e}' for e in errors))
    sys.exit(1)
print(f'NETWORKS PREFLIGHT PASSED: {len(md_files)} pages checked')
