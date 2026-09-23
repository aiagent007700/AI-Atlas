# Research automation

`research_pipeline.py` is a zero-cost public-feed collector. It uses only Python's standard library and writes a dated Markdown page under `docs/updates/`.

## What it does

* Reads configured RSS/Atom feeds.
* Keeps items within the configured lookback window.
* Deduplicates by source URL.
* Adds topic tags and publication metadata.
* Writes source-linked Markdown.

## What it deliberately does not do

* Invent quotes
* Copy full articles
* Treat a headline as proof
* Make unsupported industry claims
* Call a paid AI provider

Use the generated page as a discovery layer. Add deeper synthesis only when the source is available and its context is understood.
