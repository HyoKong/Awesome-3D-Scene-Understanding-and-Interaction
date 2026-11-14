#!/usr/bin/env python3
"""Validate catalog coverage, local Markdown navigation, and SVG references."""

from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re
import xml.etree.ElementTree as ET

from build_catalog import TOPICS, topic_records, verify, verify_reading_routes

ROOT = Path(__file__).resolve().parents[1]


def anchors(text):
    found = set(re.findall(r'<a id="([^"]+)"', text))
    counts = {}
    for heading in re.findall(r"^#{1,6} (.+)$", text, re.M):
        heading = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", heading)
        anchor = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        suffix = counts.get(anchor, 0)
        counts[anchor] = suffix + 1
        found.add(anchor + (f"-{suffix}" if suffix else ""))
    return found


def main():
    catalog = json.loads((ROOT / "data/catalog.json").read_text())
    benchmarks = json.loads((ROOT / "data/benchmarks.json").read_text())
    papers = verify(catalog, benchmarks)
    reading_routes = json.loads((ROOT / "data/reading_routes.json").read_text())
    verify_reading_routes(reading_routes, papers)
    pages = list(ROOT.glob("*.md")) + list((ROOT / "topics").glob("*.md")) + list((ROOT / "assets").glob("*.md"))
    link_count = 0
    for page in pages:
        content = page.read_text()
        for link in re.findall(r"\]\(([^)\s]+)\)", content):
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            target = (page.parent / unquote(parsed.path)).resolve() if parsed.path else page
            assert target.exists(), f"Missing local target in {page.name}: {link}"
            if parsed.fragment and target.suffix == ".md":
                assert unquote(parsed.fragment) in anchors(target.read_text()), f"Missing anchor in {page.name}: {link}"
            link_count += 1
    index = (ROOT / "PAPERS.md").read_text()
    for paper in papers.values():
        assert index.count(f'<a id="{paper["id"]}"></a>') == 1, paper["id"]
    for category, _, _ in TOPICS:
        topic = (ROOT / "topics" / f'{category}.md').read_text()
        for paper in topic_records(catalog, category, include_additional=True):
            assert topic.count(f'[Details](../PAPERS.md#{paper["id"]})') == 1, f"Missing or duplicate topic entry: {category} / {paper['id']}"
            for field in ["url", "project_url", "code_url"]:
                if paper[field]:
                    assert f'({paper[field]})' in topic, f"Resource missing: {category} / {paper['id']} / {field}"
    datasets = (ROOT / "topics/datasets.md").read_text()
    for benchmark in benchmarks["benchmarks"]:
        assert f'({benchmark["url"]})' in datasets, f"Benchmark missing from datasets directory: {benchmark['id']}"
        if benchmark.get("leaderboard_url"):
            assert f'({benchmark["leaderboard_url"]})' in datasets, benchmark["id"]
    readme = (ROOT / "README.md").read_text()
    contents = readme.split("## Contents\n", 1)[1].split("## Reading routes\n", 1)[0]
    assert "](assets/survey-teaser.svg)](assets/survey-teaser.png)" in readme
    assert readme.index("assets/survey-teaser.svg") < readme.index("## Contents") < readme.index("## Reading routes")
    for route in reading_routes["routes"]:
        assert f'(#route-{route["id"]})' in contents, f"Route missing from contents: {route['id']}"
    for category, _, _ in TOPICS:
        assert f'(topics/{category}.md)' in contents, f"Topic missing from contents: {category}"
    for name in ["survey-roadmap.svg", "survey-teaser.svg"]:
        tree = ET.parse(ROOT / "assets" / name)
        ns = {"s": "http://www.w3.org/2000/svg"}
        assert tree.find("s:title", ns) is not None, f"Missing SVG title: {name}"
        assert tree.find("s:desc", ns) is not None, f"Missing SVG description: {name}"
    print(f"Validated {len(papers)} unique records, {len(benchmarks['benchmarks'])} benchmark resources, "
          f"{len(pages)} Markdown pages, {link_count} local links, and both SVG figures.")


if __name__ == "__main__":
    main()
