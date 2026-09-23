#!/usr/bin/env python3
"""Zero-cost public-feed discovery for the AI Atlas.

Discovery is deliberately separated from synthesis. This script uses only the
Python standard library, preserves provenance, and never invents quotes or
claims. It writes a dated Markdown page plus a machine-readable run manifest.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ATOM = "{http://www.w3.org/2005/Atom}"
USER_AGENT = "AI-Atlas-Public-Research-Bot/0.2"


def clean_text(value: str | None) -> str:
    if not value:
        return ""
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def parse_date(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    value = value.strip()
    for fmt in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S%z", "%a, %d %b %Y %H:%M:%S %z", "%Y-%m-%d"):
        try:
            result = dt.datetime.strptime(value, fmt)
            return (result if result.tzinfo else result.replace(tzinfo=dt.timezone.utc)).astimezone(dt.timezone.utc)
        except ValueError:
            continue
    return None


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def parse_feed(source: dict, raw: bytes, cutoff: dt.datetime) -> list[dict]:
    root = ET.fromstring(raw)
    records: list[dict] = []
    entries = root.findall(f"{ATOM}entry")
    if entries:
        for entry in entries:
            title = clean_text(entry.findtext(f"{ATOM}title"))
            summary = clean_text(entry.findtext(f"{ATOM}summary") or entry.findtext(f"{ATOM}content"))
            published = parse_date(entry.findtext(f"{ATOM}published") or entry.findtext(f"{ATOM}updated"))
            links = entry.findall(f"{ATOM}link")
            url = next((x.attrib.get("href") for x in links if x.attrib.get("rel", "alternate") == "alternate"), None)
            url = url or (links[0].attrib.get("href") if links else None)
            if title and url and published and published >= cutoff:
                records.append(record(source, title, summary, url, published))
        return records
    for item in root.findall(".//item"):
        title = clean_text(item.findtext("title"))
        summary = clean_text(item.findtext("description"))
        url = clean_text(item.findtext("link"))
        published = parse_date(item.findtext("pubDate"))
        if title and url and published and published >= cutoff:
            records.append(record(source, title, summary, url, published))
    return records


def record(source: dict, title: str, summary: str, url: str, published: dt.datetime) -> dict:
    stable_id = hashlib.sha256(url.strip().encode("utf-8")).hexdigest()[:16]
    return {
        "id": stable_id,
        "status": "NEW",
        "title": title,
        "summary": summary[:1200],
        "url": url,
        "published": published,
        "source": source["name"],
        "topic": source.get("topic", "uncategorized"),
        "evidence_tier": source.get("evidence_tier", 1),
        "review": source.get("review", "required-before-synthesis"),
    }


def render(items: list[dict], run_time: dt.datetime, failures: list[str]) -> str:
    date_label = run_time.date().isoformat()
    lines = [
        "---", f'title: "Daily research — {date_label}"', "sidebar_position: 2",
        f"description: Public-web research discoveries collected on {date_label}.", "---", "",
        f"# Daily research — {date_label}", "",
        "> Discovery layer only: open the original source before turning an item into a tutorial claim or quote.", "",
    ]
    if failures:
        lines += ["> Some configured feeds failed. See `last-run-warnings.txt` in the repository for details.", ""]
    if not items:
        lines += ["No new feed items were found in the configured lookback window.", ""]
        return "\n".join(lines)
    for item in items:
        lines += [
            f"## {item['status']} — {item['title']}", "",
            f"- **Topic:** `{item['topic']}`",
            f"- **Evidence tier:** `{item['evidence_tier']}`",
            f"- **Review:** `{item['review']}`",
            f"- **Source:** [{item['source']}]({item['url']})",
            f"- **Published:** {item['published'].strftime('%Y-%m-%d %H:%M UTC')}", "",
            item["summary"] or "Source summary unavailable; open the original source for context.", "",
            "**Editorial next step:** verify the original source, add context, and link this item to the relevant durable chapter.", "",
        ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config/sources.json")
    parser.add_argument("--output", default="docs/updates")
    parser.add_argument("--state", default="config/research-state.json")
    parser.add_argument("--lookback-days", type=int, default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    config = json.loads(Path(args.config).read_text(encoding="utf-8"))
    now = dt.datetime.now(dt.timezone.utc)
    lookback = args.lookback_days if args.lookback_days is not None else int(config.get("lookback_days", 2))
    cutoff = now - dt.timedelta(days=lookback)
    items: list[dict] = []
    failures: list[str] = []

    for source in config.get("feeds", []):
        try:
            items.extend(parse_feed(source, fetch(source["url"]), cutoff))
        except Exception as exc:
            failures.append(f"{source['name']}: {exc}")

    unique: dict[str, dict] = {}
    for item in sorted(items, key=lambda x: x["published"], reverse=True):
        unique.setdefault(item["id"], item)
    selected = list(unique.values())[: int(config.get("max_total_items", 24))]

    output = Path(args.output)
    manifest = {
        "generated_at": now.isoformat(),
        "lookback_days": lookback,
        "item_count": len(selected),
        "failure_count": len(failures),
        "items": [{**item, "published": item["published"].isoformat()} for item in selected],
    }
    if args.dry_run:
        print(json.dumps(manifest, indent=2))
        return

    output.mkdir(parents=True, exist_ok=True)
    (output / f"{now.date().isoformat()}.md").write_text(render(selected, now, failures), encoding="utf-8")
    (output / "latest-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    warnings = output / "last-run-warnings.txt"
    if failures:
        warnings.write_text("\n".join(failures) + "\n", encoding="utf-8")
    elif warnings.exists():
        warnings.unlink()
    print(f"Wrote {output / f'{now.date().isoformat()}.md'} with {len(selected)} item(s).")
    if failures:
        print(f"{len(failures)} feed failure(s) recorded.")


if __name__ == "__main__":
    main()
