# AI Atlas — Living Tutorial Starter

A zero-cost, public-web-only starter repository for a living tutorial covering the breadth of artificial intelligence and adjacent systems.

The starter is intentionally generic. It contains no company-specific material, internal sources, or proprietary content.

## What is included

This is the first content sprint: foundations, RAG, agents and agentic skills, evaluation, and evidence practices.

* Docusaurus static site with MDX support
* Initial AI atlas and learning-path structure
* Introductory chapters on foundations, reinforcement learning, RAG, agents, agentic skills, and autonomous networks
* Mermaid diagrams and a reusable visual style
* A zero-cost RSS/public-feed research workflow
* GitHub Actions workflow for daily discovery and GitHub Pages deployment
* Git-based version history and rollback

## Run locally

```bash
npm install
npm run start
```

Open the local address shown by Docusaurus.

## Build locally

```bash
npm run build
npm run serve
```

## Publish on GitHub Pages

1. Create a GitHub repository, for example `ai-living-tutorial`.
2. Push this repository to GitHub.
3. In repository settings, enable GitHub Pages using GitHub Actions.
4. The included workflow will build and deploy the site after a push to `main`.
5. The daily research workflow can be run manually or on its scheduled cadence.

The default project-site URL will be:

```text
https://YOUR_GITHUB_USER.github.io/ai-living-tutorial/
```

The Docusaurus configuration derives the repository owner and name from `GITHUB_REPOSITORY` in GitHub Actions. For local builds, replace the placeholder values in `docusaurus.config.ts` or set `DOCUSAURUS_URL` and `DOCUSAURUS_BASE_URL`.

## Daily research workflow

The included workflow uses public feeds and official public sources. It creates a dated update page containing source-linked discoveries. It does not require a paid API, database, or proprietary search service.

The workflow is deliberately evidence-first: discovery is automated, but richer synthesis, quotes, and interpretation should be added only when the source context is available and verifiable.

To add or change sources, edit:

```text
config/sources.json
```

To change the taxonomy, edit:

```text
config/topics.json
```

## Content conventions

Each substantial chapter should include:

* A motivating question
* A plain-language explanation
* A mechanism or architecture diagram
* Engineering trade-offs and failure modes
* Industry evidence with source links
* A thought experiment
* A practical exercise
* Links to related concepts

## Zero-cost principles

* Use GitHub for source control and Pages hosting.
* Use GitHub Actions within its available free limits.
* Prefer RSS, open research indexes, and official public pages.
* Generate static graphics and diagrams where possible.
* Do not add paid services until a real need is demonstrated.
* Keep research state and credentials out of the public repository.

## Scope

The tutorial aims to cover AI broadly: learning paradigms, model families, data, retrieval, reasoning, agents, skills, infrastructure, safety, governance, applications, autonomous systems, telecom, and adjacent IT. It is a living map, not a promise to reproduce every paper or news item.


## Sprint 03

Sprint 03 adds the living intelligence layer: a daily update contract, evidence tiers, review routing, deterministic feed manifests, content validation, and safer GitHub Actions workflows. The research pipeline uses public feeds only and keeps discovery separate from editorial synthesis.
