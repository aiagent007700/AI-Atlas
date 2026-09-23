# Sprint 5 integration guide

Sprint 5 is an additive content patch. Copy the contents of this package into the root of the existing `AI-Atlas` repository.

## Files added

* `docs/engineering/index.md`
* `docs/engineering/data-and-datasets.md`
* `docs/engineering/fine-tuning-and-adaptation.md`
* `docs/engineering/llmops.md`
* `docs/engineering/observability.md`
* `docs/engineering/quality-cost-latency.md`
* `docs/visuals/production-ai-system-map.md`
* `docs/updates/sprint-05.md`
* `scripts/preflight_sprint5.py`

## Sidebar entry

Append this category to the existing `sidebars.ts` file. Do not replace the whole file.

```ts
{
  type: 'category',
  label: 'Production AI engineering',
  items: [
    'engineering/production-ai-engineering',
    'engineering/data-and-datasets',
    'engineering/fine-tuning-and-adaptation',
    'engineering/llmops',
    'engineering/observability',
    'engineering/quality-cost-latency',
  ],
},
```

Add these individual items to the appropriate existing categories if preferred:

```ts
'visuals/production-ai-system-map',
'updates/sprint-05',
```

## Preflight sequence

Run this before committing:

```bash
python scripts/preflight_sprint5.py
npm run build
```

Only push if both commands succeed.

## Commit

```bash
git add docs scripts/preflight_sprint5.py SPRINT-05-INTEGRATION.md sprint-05-manifest.json
git commit -m "Add production AI engineering layer"
git push origin main
```
