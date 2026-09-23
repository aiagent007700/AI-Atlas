# Sprint 03 — the living intelligence layer

This sprint makes the daily layer more transparent and maintainable.

## Included

- A daily update contract with a clear discovery-to-synthesis lifecycle
- Evidence tiers and review routing
- A template for source-grounded updates
- Deterministic IDs and a machine-readable run manifest
- `--dry-run` support for safe local testing
- A content validator that catches malformed front matter and unquoted title colons
- A scheduled workflow with concurrency control and a separate pull-request content check
- Public-source-only configuration; no organization-specific data

## Local checks

```bash
python scripts/validate_content.py
python scripts/research_pipeline.py --dry-run
```

The pipeline is intentionally conservative: it collects public signals but does not invent quotes, numbers, or interpretations. Editorial synthesis remains a review step.
