# AI Atlas complete sidebar patch

This patch makes the complete current tutorial visible in the Docusaurus sidebar.

## Install

Copy these files into the root of your existing `AI-Atlas` repository:

- `sidebars.ts` — replace the existing file
- `docs/updates/sprint-03.md` — add this new page

The sidebar includes the documented pages from the foundations, models, systems, learning, knowledge, agents, engineering, evaluation, safety, autonomous systems, evidence, visuals, and living-updates areas.

It intentionally uses `engineering/index` rather than the nonexistent `engineering/production-ai-engineering` document ID.

## Validate before pushing

```bash
npm run build
git add sidebars.ts docs/updates/sprint-03.md
git commit -m "Add complete AI Atlas sidebar"
git push origin main
```
