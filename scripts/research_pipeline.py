#!/usr/bin/env python3
"""Zero-cost public-feed discovery for the AI Atlas.

This script deliberately uses only Python's standard library. It discovers and
publishes source-linked items; it does not invent quotes or unsupported analysis.
"""

from __future__ import annotations

import argparse
import calendar
import datetime as dt
import html
import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ATOM = "{http://www.w3.org/2005/Atom}"


def clean_text(value: str | None) -> str:
    if not value:
        return ""
    value = re.sub(r"<[^>]+>", " ", value)
    value = html.unescape(value)
    return re.sub(r"\s+", " ", value).strip()


def parse_date(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    value = value.strip()
    for fmt in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S%z", "%a, %d %b %Y %H:%M:%S %z", "%Y-%m-%d"):
        try:
            parsed = dt.datetime.strptime(value, fmt)
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=dt.timezone.utc)
            return parsed.astimezone(dt.timezone.utc)
        except ValueError:
            pass
    return None


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "AI-Atlas-Research-Bot/0.1"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def parse_feed(source: dict, raw: bytes, cutoff: dt.datetime) -> list[dict]:
    root = ET.fromstring(raw)
    results = []

    atom_entries = root.findall(f"{ATOM}entry")
    if atom_entries:
        for entry in atom_entries:
            title = clean_text(entry.findtext(f"{ATOM}title"))
            summary = clean_text(entry.findtext(f"{ATOM}summary") or entry.findtext(f"{ATOM}content"))
            published = parse_date(entry.findtext(f"{ATOM}published") or entry.findtext(f"{ATOM}updated"))
            links = entry.findall(f"{ATOM}link")
            link = next((item.attrib.get("href") for item in links if item.attrib.get("rel", "alternate") == "alternate"), None)
            if not link and links:
                link = links[0].attrib.get("href")
            if title and link and published and published >= cutoff:
                results.append({"title": title, "summary": summary, "url": link, "published": published, "source": source["name"], "topic": source["topic"]})
        return results

    for item in root.findall(".//item"):
        title = clean_text(item.findtext("title"))
        summary = clean_text(item.findtext("description"))
        link = clean_text(item.findtext("link"))
        published = parse_date(item.findtext("pubDate"))
        if title and link and published and published >= cutoff:
            results.append({"title": title, "summary": summary, "url": link, "published": published, "source": source["name"], "topic": source["topic"]})
    return results


def item_key(item: dict) -> str:
    return re.sub(r"[^a-z0-9]+", "-", item["url"].lower()).strip("-")[-100:]


def render(items: list[dict], run_time: dt.datetime) -> str:
    date_label = run_time.date().isoformat()
    lines = [
        "---",
        f"title: Daily research — {date_label}",
        "sidebar_position: 2",
        f"description: Public-web research discoveries collected on {date_label}.",
        "---",
        "",
        f"# Daily research — {date_label}",
        "",
        "> Generated from public feeds. This page is a discovery layer; verify context before turning an item into a strong claim or quote.",
        "",
    ]
    if not items:
        lines.extend(["No new feed items were found in the configured lookback window.", ""])
        return "\n".join(lines)

    for item in items:
        lines.extend([
            f"## NEW — {item['title']}",
            "",
            f"* **Topic:** `{item['topic']}`",
            f"* **Source:** [{item['source']}]({item['url']})",
            f"* **Published:** {item['published'].strftime('%Y-%m-%d %H:%M UTC')}",
            "",
            item["summary"][:900] if item["summary"] else "Source summary unavailable; open the original source for context.",
            "",
            "**Why it may matter:** Add a source-grounded explanation and link this item to the relevant durable chapter.",
            "",
        ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config/sources.json")
    parser.add_argument("--output", default="docs/updates")
    args = parser.parse_args()

    config = json.loads(Path(args.config).read_text())
    now = dt.datetime.now(dt.timezone.utc)
    cutoff = now - dt.timedelta(days=int(config.get("lookback_days", 2)))
    items = []
    failures = []

    for source in config.get("feeds", []):
        try:
            items.extend(parse_feed(source, fetch(source["url"]), cutoff))
        except Exception as exc:  # a single source should not stop the run
            failures.append(f"{source['name']}: {exc}")

    unique = {}
    for item in sorted(items, key=lambda x: x["published"], reverse=True):
        unique.setdefault(item_key(item), item)

    selected = list(unique.values())[: int(config.get("max_total_items", 24))]
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    target = output / f"{now.date().isoformat()}.md"
    target.write_text(render(selected, now), encoding="utf-8")

    if failures:
        failure_path = output / "last-run-warnings.txt"
        failure_path.write_text("\n".join(failures) + "\n", encoding="utf-8")
    print(f"Wrote {target} with {len(selected)} items.")
    if failures:
        print(f"Warnings from {len(failures)} source(s) were written to {output / 'last-run-warnings.txt'}.")


if __name__ == "__main__":
    main()
