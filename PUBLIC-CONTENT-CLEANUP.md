# AI Atlas public content cleanup

This package removes release-window terminology from the public tutorial. The words used to organize our working sessions are not part of the learner-facing information architecture.

## What changes

- Renames public update pages to semantic names:
  - `updates/living-intelligence`
  - `updates/ai-systems-layer`
  - `updates/production-ai-engineering`
  - `updates/trust-security-governance`
- Renames the agent-system content directory to `agents/agent-systems`.
- Renames the multimodal content directory to `multimodal/multimodal-and-generative-ai`.
- Renames the agent-system update page to `module-update`.
- Updates document IDs, internal links, sidebar paths, titles, and prose.
- Removes release-only root files and old preflight scripts whose names expose the working-session terminology.
- Includes an idempotent checker that fails if public docs still contain the term.

## Apply

Copy `scripts/public_content_cleanup.py` into the repository's `scripts/` directory, then run from the repository root:

```bash
python scripts/public_content_cleanup.py
python scripts/public_content_cleanup.py --check
npm run build
```

Review the moved paths in Git, especially if you have bookmarked old URLs. This is an intentional route cleanup; old release-numbered paths are replaced by semantic paths. The migration preserves relative links inside moved directories and updates explicit sidebar references.

Then commit:

```bash
git add .
git commit -m "Clean public tutorial terminology and routes"
git push origin main
```

## Expected public structure

```text
docs/updates/living-intelligence.md
docs/updates/ai-systems-layer.md
docs/updates/production-ai-engineering.md
docs/updates/trust-security-governance.md
docs/agents/agent-systems/
docs/multimodal/multimodal-and-generative-ai/
```

The checker is safe to rerun and should pass after the migration.
