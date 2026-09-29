# AGENTS.md

## Project

AI Atlas — a Docusaurus static site (frontend-only). No backend, database, or external services. Content lives in `docs/` as MDX with Mermaid diagrams.

## Stack

- Docusaurus 3.7 (React 18, TypeScript), npm (no lockfile committed — `npm install` resolves latest compatible).
- Dev server: `docusaurus start --host 0.0.0.0 --port 3000 --no-open` (webpack-dev-server under the hood).
- Build: `docusaurus build` outputs to `build/`.

## Running in Base44

- `docker compose -f docker-compose.base44.yml up -d --build` starts the dev server on host port 3000.
- Dependencies install on container startup (`npm install`) since none are baked into the image; first boot takes longer.
- Live reload is enabled via bind mount + chokidar polling (`CHOKIDAR_USEPOLLING=true`).

## Notes

- `docusaurus.config.ts` derives `url`/`baseUrl` from `GITHUB_REPOSITORY` or `DOCUSAURUS_URL`/`DOCUSAURUS_BASE_URL` env vars. Defaults are placeholder values suitable for local dev.
- `scripts/` contains Python research/validation helpers (not part of the running site).
- No secrets required to boot.
