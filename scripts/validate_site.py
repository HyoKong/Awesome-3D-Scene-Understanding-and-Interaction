#!/usr/bin/env python3
"""Check public website coverage, navigation, and the deployment file boundary."""

from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

from build_site import ARTICLE_ORDER, ROOT, expected_output_files, load_media, output_paths


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.papers = {}
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            assert attrs["id"] not in self.ids, f"Duplicate ID: {attrs['id']}"
            self.ids.add(attrs["id"])
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])
        if "paper-item" in attrs.get("class", "").split():
            assert attrs["data-id"] not in self.papers
            self.papers[attrs["data-id"]] = attrs


def main():
    output = ROOT / "_site"
    catalog = json.loads((ROOT / "data/catalog.json").read_text())
    papers = {paper["id"]: paper for paper in catalog["papers"]}
    media = load_media(papers)
    expected = expected_output_files(media)
    assert output_paths(output) == expected, "Website output differs from its publication allowlist"
    assert not any(p.is_symlink() for p in output.rglob("*")), "Website output must not contain symlinks"
    pages = {p.name: Page(p.read_text()) for p in output.glob("*.html")}
    for name, page in pages.items():
        source = (output / name).read_text()
        for forbidden in ("TEASER_DESIGN.md", "REPOSITORY_DESIGN.md", "/mnt/", "/home/", "vscode-resource", "in this chat"):
            assert forbidden not in source, f"Non-public reference in {name}: {forbidden}"
        assert "{{" not in source, f"Unexpanded placeholder in {name}"
        assert "library.html?topic=overview" not in source and "library.html?topic=outlook" not in source, f"Invalid library topic link in {name}"
        citation_numbers = [int(value) for value in re.findall(r'class="citation"[^>]*href="#reference-(\d+)"', source)]
        first_seen = []
        for number in citation_numbers:
            if number not in first_seen:
                first_seen.append(number)
        assert first_seen == list(range(1, len(first_seen) + 1)), f"Citation first-use order is invalid in {name}"
        for number in first_seen:
            assert f'id="reference-{number}"' in source, f"Missing reference {number} in {name}"
            assert re.search(rf'<a class="citation" id="citation-\d+" href="#reference-{number}" title="[^"]+"', source), f"Citation metadata is incomplete in {name}"
        for link in page.links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                assert parsed.scheme in ("http", "https"), f"Unsupported URL in {name}: {link}"
                continue
            assert not parsed.path.startswith("/"), f"Project-site path must be relative: {link}"
            assert not parsed.path.startswith("research/"), f"Internal research reference in {name}: {link}"
            target = (output / unquote(parsed.path)).resolve() if parsed.path else output / name
            assert target.is_relative_to(output.resolve()), f"Link escapes website output: {link}"
            assert target.is_file(), f"Missing website target from {name}: {link}"
            if parsed.fragment and target.name in pages:
                assert unquote(parsed.fragment) in pages[target.name].ids, f"Missing anchor from {name}: {link}"

    routes = json.loads((ROOT / "data/reading_routes.json").read_text())["routes"]
    benchmarks = json.loads((ROOT / "data/benchmarks.json").read_text())["benchmarks"]
    library = pages["library.html"]
    assert set(library.papers) == {p["id"] for p in catalog["papers"]}
    for paper in catalog["papers"]:
        attrs = library.papers[paper["id"]]
        assert set(attrs["data-topics"].split()) == {paper["category"], *paper.get("additional_topics", {})}
        assert attrs["data-code"] == paper["code_status"]
        for key in ("url", "project_url", "code_url"):
            if paper.get(key):
                assert paper[key] in library.links, f"Missing official resource: {paper['id']} / {key}"
    for route in routes:
        assert f"route-{route['id']}" in pages["reading-routes.html"].ids
    for benchmark in benchmarks:
        assert f"benchmark-{benchmark['id']}" in pages["benchmarks.html"].ids
    index = pages["index.html"]
    assert {f"chapter-{number}" for number in range(1, len(ARTICLE_ORDER) + 1)} <= index.ids
    assert "references" in index.ids and '#references' in (output / "index.html").read_text()
    for topic in ARTICLE_ORDER:
        article_file = ROOT / "site" / "articles" / f"{topic}.json"
        assert article_file.is_file(), f"Missing survey chapter: {topic}"
        article = json.loads(article_file.read_text())
        assert article["id"] + ".html" in pages
        for index, _ in enumerate(article["sections"], 1):
            assert f"section-{index}" in pages[article["id"] + ".html"].ids
            assert f"chapter-{ARTICLE_ORDER.index(article['id']) + 1}-section-{index}" in pages["index.html"].ids
        for section in article["sections"]:
            for paper_id in section.get("paper_ids", []):
                paper = next(item for item in catalog["papers"] if item["id"] == paper_id)
                assert paper["url"] in pages[article["id"] + ".html"].links
        assert "[cite:" not in (output / f"{article['id']}.html").read_text()
    assert "[cite:" not in (output / "index.html").read_text()
    for item in media:
        page = pages[item["chapter"] + ".html"]
        assert f"media-{item['id']}" in page.ids
        if item["type"] == "image":
            assert item["src"] in page.links and (output / item["src"]).is_file()
        elif item["type"] == "video":
            assert item["src"] in page.links
        else:
            assert item["src"] in (output / f"{item['chapter']}.html").read_text()
        assert item["source_url"] in page.links and item["license_url"] in page.links
    print(f"Validated {len(pages)} website pages, all catalog records and resources, "
          f"all routes and benchmarks, and the exact {len(expected)}-file deployment boundary.")


if __name__ == "__main__":
    main()
