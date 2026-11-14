#!/usr/bin/env python3
"""Check public website coverage, navigation, and the deployment file boundary."""

from html.parser import HTMLParser
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import parse_qs, unquote, urlsplit

from build_site import ARTICLE_ORDER, PUBLIC_URL, ROOT, expected_output_files, load_media, output_paths


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.papers = {}
        self.elements = []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.elements.append((tag, attrs))
        if attrs.get("id"):
            assert attrs["id"] not in self.ids, f"Duplicate ID: {attrs['id']}"
            self.ids.add(attrs["id"])
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])
        if "paper-item" in attrs.get("class", "").split():
            assert attrs["data-id"] not in self.papers
            self.papers[attrs["data-id"]] = attrs


def page_name(path: Path, output: Path) -> str:
    return path.relative_to(output).as_posix()


def citation_titles(source: str) -> list[str]:
    return re.findall(r'<a class="citation" id="citation-\d+" href="#reference-\d+" title="([^"]+)"', source)


def validate_citations(source: str, name: str) -> list[str]:
    citation_numbers = [int(value) for value in re.findall(r'class="citation"[^>]*href="#reference-(\d+)"', source)]
    first_seen = []
    for number in citation_numbers:
        if number not in first_seen:
            first_seen.append(number)
    assert first_seen == list(range(1, len(first_seen) + 1)), f"Citation first-use order is invalid in {name}"
    for number in first_seen:
        assert f'id="reference-{number}"' in source, f"Missing reference {number} in {name}"
        assert re.search(rf'<a class="citation" id="citation-\d+" href="#reference-{number}" title="[^"]+"', source), f"Citation metadata is incomplete in {name}"
    return citation_titles(source)


def language_switches(page: Page) -> dict[str, str]:
    links = {}
    for tag, attrs in page.elements:
        if tag == "a" and "data-language-switch" in attrs:
            links[attrs.get("hreflang", "")] = attrs.get("href", "")
    return links


def class_links(page: Page, class_name: str) -> list[str]:
    return [attrs["href"] for tag, attrs in page.elements
            if tag == "a" and class_name in attrs.get("class", "").split() and attrs.get("href")]


def route_contexts(source: str) -> list[tuple[str, int, str]]:
    """Return each contextual route aside and its rendered navigation markup."""
    pattern = r'<aside class="route-context" data-route-id="([^"]+)" data-route-step="(\d+)" hidden>(.*?)</aside>'
    return [(route_id, int(step), body) for route_id, step, body in re.findall(pattern, source, re.S)]


def assert_route_url(url: str, route_id: str, step: int, chapter: str, section: int) -> None:
    parsed = urlsplit(url)
    assert parsed.path == f"{chapter}.html", f"Wrong route chapter link: {url}"
    assert parse_qs(parsed.query) == {"route": [route_id], "step": [str(step)]}, f"Wrong route query: {url}"
    assert parsed.fragment == f"section-{section}", f"Wrong route section anchor: {url}"


def main():
    output = ROOT / "_site"
    catalog = json.loads((ROOT / "data/catalog.json").read_text())
    papers = {paper["id"]: paper for paper in catalog["papers"]}
    media = load_media(papers)
    expected = expected_output_files(media)
    assert output_paths(output) == expected, "Website output differs from its publication allowlist"
    assert not any(p.is_symlink() for p in output.rglob("*")), "Website output must not contain symlinks"
    # Font requests come from CSS rather than HTML, so validate them explicitly.
    css = (output / "styles.css").read_text()
    font_urls = re.findall(r'url\("(assets/fonts/[^"?#]+\.woff2)"\)', css)
    assert len(font_urls) == 3, "Expected three self-hosted font faces"
    for relative in font_urls:
        assert relative in expected, f"Font missing from publication allowlist: {relative}"
        assert (output / relative).read_bytes()[:4] == b"wOF2", f"Invalid WOFF2 font: {relative}"
    page_files = sorted(output.rglob("*.html"))
    pages = {page_name(p, output): Page(p.read_text()) for p in page_files}
    expected_pages = {path for path in expected if path.endswith(".html")}
    assert set(pages) == expected_pages and len(pages) == 24, "Expected exactly 24 public HTML pages"
    for name, page in pages.items():
        source_path = output / name
        source = source_path.read_text()
        expected_lang = "zh-CN" if name.startswith("zh/") else "en"
        assert re.search(rf'<html\s+lang="{expected_lang}">', source), f"Wrong document language in {name}"
        for forbidden in ("TEASER_DESIGN.md", "REPOSITORY_DESIGN.md", "ROADMAP.md", "/mnt/", "/home/", "vscode-resource", "in this chat"):
            assert forbidden not in source, f"Non-public reference in {name}: {forbidden}"
        assert 'href="research/' not in source and 'src="research/' not in source, f"Internal research link in {name}"
        assert "{{" not in source, f"Unexpanded placeholder in {name}"
        assert "library.html?topic=overview" not in source and "library.html?topic=outlook" not in source, f"Invalid library topic link in {name}"
        validate_citations(source, name)
        for asset in ("styles.css", "app.js"):
            version = hashlib.sha256((output / asset).read_bytes()).hexdigest()[:12]
            assert any(link.endswith(f"{asset}?v={version}") for link in page.links), f"Missing content version for {asset} in {name}"
        relative = name.removeprefix("zh/")
        switches = language_switches(page)
        expected_switches = {"en": f"../{relative}" if name.startswith("zh/") else relative,
                             "zh": relative if name.startswith("zh/") else f"zh/{relative}"}
        assert switches == expected_switches, f"Broken language switch in {name}: {switches}"
        assert f'hreflang="en" href="{PUBLIC_URL + relative}"' in source, f"Missing English alternate in {name}"
        assert f'hreflang="zh-CN" href="{PUBLIC_URL}zh/{relative}"' in source, f"Missing Chinese alternate in {name}"
        for link in page.links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                assert parsed.scheme in ("http", "https"), f"Unsupported URL in {name}: {link}"
                continue
            assert not parsed.path.startswith("/"), f"Project-site path must be relative: {link}"
            target = (source_path.parent / unquote(parsed.path)).resolve() if parsed.path else source_path.resolve()
            assert target.is_relative_to(output.resolve()), f"Link escapes website output: {link}"
            assert target.is_file(), f"Missing website target from {name}: {link}"
            target_name = page_name(target, output)
            if parsed.fragment and target_name in pages:
                assert unquote(parsed.fragment) in pages[target_name].ids, f"Missing anchor from {name}: {link}"

    for relative in sorted(path.removeprefix("zh/") for path in pages if not path.startswith("zh/")):
        assert citation_titles((output / relative).read_text()) == citation_titles((output / "zh" / relative).read_text()), f"English/Chinese citation-title mismatch: {relative}"

    routes = json.loads((ROOT / "data/reading_routes.json").read_text())["routes"]
    benchmarks = json.loads((ROOT / "data/benchmarks.json").read_text())["benchmarks"]
    libraries = [pages["library.html"], pages["zh/library.html"]]
    for library in libraries:
        assert set(library.papers) == {p["id"] for p in catalog["papers"]}
        for paper in catalog["papers"]:
            attrs = library.papers[paper["id"]]
            assert set(attrs["data-topics"].split()) == {paper["category"], *paper.get("additional_topics", {})}
            assert attrs["data-code"] == paper["code_status"]
            for key in ("url", "project_url", "code_url"):
                if paper.get(key):
                    assert paper[key] in library.links, f"Missing official resource: {paper['id']} / {key}"
    assert set(libraries[0].papers) == set(libraries[1].papers), "English/Chinese paper-library parity failed"
    for route in routes:
        assert f"route-{route['id']}" in pages["reading-routes.html"].ids
        assert f"route-{route['id']}" in pages["zh/reading-routes.html"].ids

    # Every reading step must take the reader to its declared survey section in
    # either language, and the contextual aside must preserve route progress.
    for prefix in ("", "zh/"):
        route_page_name = prefix + "reading-routes.html"
        route_page = pages[route_page_name]
        route_links = class_links(route_page, "step-chapter")
        expected_step_links = []
        expected_contexts = []
        for route in routes:
            total = len(route["steps"])
            for step_number, step in enumerate(route["steps"], 1):
                for reference in step["chapter_sections"]:
                    target = (route["id"], step_number, reference["chapter"], reference["section"])
                    expected_step_links.append(target)
                    expected_contexts.append(target)
        assert len(route_links) == len(expected_step_links), f"Wrong step-link count in {route_page_name}"
        for url, (route_id, step, chapter, section) in zip(route_links, expected_step_links):
            assert_route_url(url, route_id, step, chapter, section)

        rendered_contexts = []
        for chapter in ARTICLE_ORDER:
            article_name = prefix + chapter + ".html"
            rendered_contexts.extend((route_id, step, chapter, body)
                                     for route_id, step, body in route_contexts((output / article_name).read_text()))
        assert len(rendered_contexts) == len(expected_contexts), f"Wrong route-context count in {prefix or 'en'}"
        chapter_order = {chapter: index for index, chapter in enumerate(ARTICLE_ORDER)}
        expected_contexts.sort(key=lambda value: (chapter_order[value[2]], value[3]))
        for (route_id, step, chapter, body), target in zip(rendered_contexts, expected_contexts):
            expected_route, expected_step, expected_chapter, expected_section = target
            assert (route_id, step, chapter) == (expected_route, expected_step, expected_chapter), f"Route context order mismatch in {prefix or 'en'}"
            assert f'href="reading-routes.html#route-{route_id}-step-{step}"' in body, f"Missing route return in {prefix or 'en'}"
            route = next(item for item in routes if item["id"] == route_id)
            context_links = Page(body).links
            if step > 1:
                previous = route["steps"][step - 2]["chapter_sections"][0]
                expected_url = f'{previous["chapter"]}.html?route={route_id}&step={step - 1}#section-{previous["section"]}'
                assert expected_url in context_links, f"Broken previous route link in {prefix or 'en'}"
            if step < len(route["steps"]):
                following = route["steps"][step]["chapter_sections"][0]
                expected_url = f'{following["chapter"]}.html?route={route_id}&step={step + 1}#section-{following["section"]}'
                assert expected_url in context_links, f"Broken next route link in {prefix or 'en'}"
            else:
                assert f'href="reading-routes.html#route-{route_id}-exercise"' in body, f"Broken route end link in {prefix or 'en'}"

        for topic, route_ids in {"perception": ["scene-perception", "language-and-function", "articulated-perception"], "reconstruction": ["scene-reconstruction", "reconstruction", "articulated-perception"], "generation": ["scene-generation", "generation", "reconstruction"], "robotics": ["spatial-navigation", "manipulation", "policies-and-agents"]}.items():
            for route_id in route_ids:
                route = next(item for item in routes if item["id"] == route_id)
                first = route["steps"][0]["chapter_sections"][0]
                expected_url = f'{first["chapter"]}.html?route={route_id}&step=1#section-{first["section"]}'
                assert expected_url in class_links(pages[prefix + "index.html"], "text-link"), f"Missing homepage direct entry: {prefix}{route_id}"
    for benchmark in benchmarks:
        assert f"benchmark-{benchmark['id']}" in pages["benchmarks.html"].ids
        assert f"benchmark-{benchmark['id']}" in pages["zh/benchmarks.html"].ids
    index = pages["index.html"]
    survey = pages["survey.html"]
    assert {f"chapter-{number}" for number in range(1, len(ARTICLE_ORDER) + 1)} <= survey.ids
    assert {f"chapter-{number}" for number in range(1, len(ARTICLE_ORDER) + 1)} <= pages["zh/survey.html"].ids
    assert "references" in survey.ids and '#references' in (output / "survey.html").read_text()
    assert "survey-chapter" not in (output / "index.html").read_text(), "Homepage must not contain full-survey chapters"
    assert not {f"chapter-{number}" for number in range(1, len(ARTICLE_ORDER) + 1)} & index.ids, "Homepage must remain a short index"
    for topic in ARTICLE_ORDER:
        article_file = ROOT / "site" / "articles" / f"{topic}.json"
        assert article_file.is_file(), f"Missing survey chapter: {topic}"
        article = json.loads(article_file.read_text())
        assert article["id"] + ".html" in pages
        for index, _ in enumerate(article["sections"], 1):
            assert f"section-{index}" in pages[article["id"] + ".html"].ids
            assert f"section-{index}" in pages["zh/" + article["id"] + ".html"].ids
            assert f"chapter-{ARTICLE_ORDER.index(article['id']) + 1}-section-{index}" in survey.ids
        for section in article["sections"]:
            for paper_id in section.get("paper_ids", []):
                paper = next(item for item in catalog["papers"] if item["id"] == paper_id)
                assert paper["url"] in pages[article["id"] + ".html"].links
                assert paper["url"] in pages["zh/" + article["id"] + ".html"].links
        assert "[cite:" not in (output / f"{article['id']}.html").read_text()
        assert "[cite:" not in (output / "zh" / f"{article['id']}.html").read_text()
    assert "[cite:" not in (output / "index.html").read_text() and "[cite:" not in (output / "survey.html").read_text()
    media_per_chapter = {topic: [] for topic in ARTICLE_ORDER}
    for item in media:
        media_per_chapter[item["chapter"]].append(item)
    assert all(len(items) >= 2 for items in media_per_chapter.values()), "Every survey chapter needs at least two credited visuals"
    for item in media:
        for prefix in ("", "zh/"):
            page = pages[prefix + item["chapter"] + ".html"]
            source = (output / (prefix + item["chapter"] + ".html")).read_text()
            rendered_src = item["src"] if not prefix or item["src"].startswith("https://") else "../" + item["src"]
            assert f"media-{item['id']}" in page.ids
            assert rendered_src in source, f"Missing media source: {item['id']} / {prefix or 'en'}"
            assert item["source_url"] in page.links and item["license_url"] in page.links
            if item["src"].startswith("assets/"):
                target = output / item["src"]
                assert target.is_file(), f"Missing copied local media: {item['src']}"
    print(f"Validated {len(pages)} website pages, all catalog records and resources, "
          f"all routes and benchmarks, and the exact {len(expected)}-file deployment boundary.")


if __name__ == "__main__":
    main()
