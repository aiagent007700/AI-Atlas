# Public navigation and network module refresh

This package replaces the short network-module pages with a deeper tutorial and provides an idempotent navigation cleanup.

## Apply

Copy the package contents into the root of the existing `AI-Atlas` repository, then run:

```bash
python scripts/apply_networks_upgrade.py
python scripts/apply_networks_upgrade.py --check
npm install
npm run build
```

The script:

- adds a visible `Autonomous networks, telecom and IT` category to `sidebars.ts`;
- removes the old release-labelled update entries from the sidebar;
- removes visible release terminology from tutorial titles and prose;
- leaves the existing content structure intact;
- is safe to run more than once.

Then commit:

```bash
git add docs/networks sidebars.ts scripts/apply_networks_upgrade.py NETWORKS-REFRESH-INTEGRATION.md
 git commit -m "Expand networks tutorial and clean public navigation"
git push origin main
```

If the build reports a pre-existing broken link outside `docs/networks`, fix that separately; this package does not rewrite unrelated content.
