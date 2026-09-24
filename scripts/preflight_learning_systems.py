#!/usr/bin/env python3
"""Static checks for the Learning systems content package."""
from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs' / 'learning-systems'
errors = []

if not DOCS.exists():
    errors.append(f'missing directory: {DOCS}')
else:
    pages = sorted(DOCS.glob('*.md'))
    if len(pages) != 9:
        errors.append(f'expected 9 pages, found {len(pages)}')
    for path in pages:
        text = path.read_text(encoding='utf-8')
        if not text.startswith('---\n'):
            errors.append(f'{path}: missing front matter')
        else:
            end = text.find('\n---\n', 4)
            if end < 0:
                errors.append(f'{path}: unclosed front matter')
            else:
                fm = text[4:end]
                for key, value in re.findall(r'^(title|sidebar_label):\s*(.*)$', fm, re.M):
                    if ':' in value and not (value.startswith('"') or value.startswith("'")):
                        errors.append(f'{path}: unquoted colon in {key}')
        if text.count('```') % 2:
            errors.append(f'{path}: unbalanced code fences')
        if re.search(r'(?<!\\)\$\$', text):
            errors.append(f'{path}: raw display math is not allowed')
        body_without_fences = re.sub(r'```.*?```', '', text, flags=re.S)
        if re.search(r'(?<![\\`])\{[^\n{}]+\}', body_without_fences):
            errors.append(f'{path}: possible MDX expression')
        if re.search(r'(?im)^.*\bSprint\b', text):
            errors.append(f'{path}: internal release terminology found')

for path in [ROOT/'LEARNING-SYSTEMS-INTEGRATION.md']:
    if path.exists() and re.search(r'(?im)^.*\bSprint\b', path.read_text(encoding='utf-8')):
        errors.append(f'{path}: internal release terminology found')

if errors:
    print('\n'.join('ERROR: '+e for e in errors))
    sys.exit(1)
print(f'PASS: {len(list(DOCS.glob("*.md")))} learning-system pages passed preflight')
