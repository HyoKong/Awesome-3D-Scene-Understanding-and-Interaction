#!/usr/bin/env python3
"""Build the public, dependency-free editorial site from curated survey records."""

from __future__ import annotations

import argparse
from html import escape
import json
from pathlib import Path
import re
import shutil
import tempfile

from build_catalog import TOPICS, verify, verify_reading_routes


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
DEFAULT_OUTPUT = ROOT / "_site"
SITE_TOPICS = [topic for topic, _, _ in TOPICS]
# The main page follows the argument of the survey rather than the database
# categories.  The last two chapters are deliberately cross-cutting.
ARTICLE_ORDER = ["overview", "perception", "reconstruction", "generation", "robotics", "datasets", "outlook"]
CHAPTER_LABELS = {
    "overview": "Scope & taxonomy", "perception": "Scene perception",
    "reconstruction": "Reconstruction", "generation": "Scene generation",
    "robotics": "Agents & interaction", "datasets": "Datasets & evaluation",
    "outlook": "Open questions",
}
OUTPUT_FILES = {
    ".nojekyll", "index.html", "library.html", "reading-routes.html", "benchmarks.html",
    "overview.html", "perception.html", "reconstruction.html", "generation.html", "robotics.html", "datasets.html", "outlook.html",
    "styles.css", "app.js", "assets/survey-teaser.svg", "assets/survey-teaser.png", "assets/survey-roadmap.svg",
    "assets/teaser-source/robocasa-kitchen-robot.png",
}
TEMPLATES = {
    "index.html": ("index.template.html", {"{{SURVEY_TOC}}", "{{SURVEY_CHAPTERS}}", "{{REFERENCES}}"}),
    "library.html": ("library.template.html", {"{{TOPIC_BUTTONS}}", "{{YEAR_OPTIONS}}", "{{PAPER_ITEMS}}", "{{TOTAL_PAPERS}}"}),
    "reading-routes.html": ("routes.template.html", {"{{ROUTE_NAV}}", "{{ROUTE_SECTIONS}}"}),
    "benchmarks.html": ("benchmarks.template.html", {"{{BENCHMARK_ITEMS}}"}),
}
ARTICLE_TOKENS = {
    "{{ARTICLE_TITLE}}", "{{ARTICLE_KICKER}}", "{{ARTICLE_DEK}}", "{{READING_MINUTES}}",
    "{{ARTICLE_INTRO}}", "{{ARTICLE_CONTENT}}", "{{ARTICLE_TOC}}", "{{ARTICLE_FOOTER}}", "{{REFERENCES}}",
}


def text(value: object) -> str:
    return escape(str(value), quote=True)


def external_link(url: str, label: str, extra_class: str = "") -> str:
    class_name = f' class="{text(extra_class)}"' if extra_class else ""
    return f'<a{class_name} href="{text(url)}" target="_blank" rel="noopener noreferrer">{text(label)}</a>'


def topic_label(key: str) -> str:
    return next(title for topic, title, _ in TOPICS if topic == key)


def paper_links(paper: dict) -> str:
    links = [external_link(paper["url"], "Paper")]
    if paper.get("project_url"):
        links.append(external_link(paper["project_url"], "Project"))
    if paper.get("code_url"):
        label = "Toolkit" if paper.get("code_kind") == "dataset-toolkit" else "Code"
        if paper.get("code_status") == "placeholder":
            label += " (announced)"
        links.append(external_link(paper["code_url"], label))
    return " ".join(links)


def paper_markup(paper: dict, benchmark_names: dict[str, list[str]]) -> str:
    topics = [paper["category"], *paper.get("additional_topics", {}).keys()]
    search = " ".join([
        paper["title"], paper["short"], paper["evidence"], paper["category"], paper["section"],
        paper["venue"], str(paper["year"]), " ".join(paper.get("roles", [])),
        " ".join(benchmark_names.get(paper["id"], [])),
    ]).lower()
    code = "released" if paper.get("code_status") == "released" else paper.get("code_status", "not-located")
    return f'''<li class="paper-item" id="paper-{text(paper['id'])}" data-id="{text(paper['id'])}" data-topics="{text(' '.join(topics))}" data-year="{text(paper['year'])}" data-title="{text(paper['title'].lower())}" data-search="{text(search)}" data-code="{text(code)}">
  <article class="paper">
    <div class="paper-meta"><span class="paper-year">{text(paper['year'])}</span><span class="paper-venue">{text(paper['venue'])}</span></div>
    <div class="paper-body">
      <p class="paper-kicker">{text(topic_label(paper['category']))} · {text(paper['section'])}</p>
      <h3 class="paper-title">{external_link(paper['url'], paper['title'])}</h3>
      <p class="paper-summary">{text(paper['evidence'])}</p>
      <div class="paper-links">{paper_links(paper)}</div>
    </div>
  </article>
</li>'''


def route_nav(routes: list[dict]) -> str:
    return "\n".join(
        f'<a class="route-index-item" href="#route-{text(route["id"])}">'
        f'<span class="route-index-title">{text(route["title"])}</span>'
        f'<span class="route-index-summary">{text(route["summary"])}</span></a>' for route in routes
    )


def route_sections(routes: list[dict], papers: dict[str, dict]) -> str:
    sections = []
    for route in routes:
        steps = []
        for number, step in enumerate(route["steps"], 1):
            references = " ".join(
                f'<a href="library.html#paper-{text(pid)}" data-paper-link="{text(pid)}">{text(papers[pid]["short"])}</a>'
                for pid in step["paper_ids"]
            )
            steps.append(f'''<li><span class="step-number">{number}</span><div class="step-content">
  <div class="step-label"><h4>{text(step['label'])}</h4></div><p class="step-papers">{references}</p><p class="step-focus">{text(step['focus'])}</p>
</div></li>''')
        sections.append(f'''<section class="reading-route" id="route-{text(route['id'])}">
  <h3>{text(route['title'])}</h3><p class="route-summary">{text(route['summary'])}</p><p class="route-goal">{text(route['goal'])}</p>
  <ol class="route-steps">{' '.join(steps)}</ol><p class="route-exercise"><strong>Try it:</strong> {text(route['try_it'])}</p>
</section>''')
    return "\n".join(sections)


def benchmark_markup(benchmark: dict, papers: dict[str, dict]) -> str:
    links = [external_link(benchmark["url"], "Official protocol")]
    if benchmark.get("leaderboard_url"):
        links.append(external_link(benchmark["leaderboard_url"], "Leaderboard"))
    for paper_id in benchmark.get("paper_ids", [])[:6]:
        links.append(f'<a href="library.html#paper-{text(paper_id)}" data-paper-link="{text(paper_id)}">{text(papers[paper_id]["short"])}</a>')
    if len(benchmark.get("paper_ids", [])) > 6:
        links.append('<a href="https://github.com/HyoKong/Awesome-3D-Scene-Understanding-and-Interaction/blob/main/BENCHMARKS.md" target="_blank" rel="noopener noreferrer">Full guide</a>')
    return f'''<article class="benchmark-item" id="benchmark-{text(benchmark['id'])}">
  <h3>{external_link(benchmark['url'], benchmark['name'])}</h3><p>{text(benchmark['task'])}</p><div class="benchmark-links">{' '.join(links)}</div>
</article>'''


class CitationRegistry:
    """Assign stable per-page reference numbers while rendering escaped prose."""

    def __init__(self, papers: dict[str, dict]):
        self.papers = papers
        self.ids: list[str] = []
        self.included_ids: list[str] = []
        self.citation_count = 0
        self.first_citation: dict[int, str] = {}

    def add(self, paper_id: str) -> int:
        assert paper_id in self.papers, f"Unknown citation ID: {paper_id}"
        if paper_id not in self.ids:
            self.ids.append(paper_id)
        return self.ids.index(paper_id) + 1

    def prose(self, value: str) -> str:
        """Escape prose and turn [cite:paper-id] into an accessible inline link."""
        import re
        pieces: list[str] = []
        cursor = 0
        for match in re.finditer(r"\[cite:([a-z0-9][a-z0-9-]*)\]", value):
            pieces.append(text(value[cursor:match.start()]))
            number = self.add(match.group(1))
            paper_id = match.group(1)
            self.citation_count += 1
            citation_id = f"citation-{self.citation_count}"
            self.first_citation.setdefault(number, citation_id)
            pieces.append(
                f'<a class="citation" id="{citation_id}" href="#reference-{number}" title="{text(self.papers[paper_id]["title"])}" aria-label="Reference {number}: {text(self.papers[paper_id]["short"])}">[{number}]</a>'
            )
            cursor = match.end()
        pieces.append(text(value[cursor:]))
        assert "[cite:" not in "".join(pieces), f"Malformed citation marker: {value}"
        return "".join(pieces)

    def include(self, paper_ids: list[str]) -> None:
        for paper_id in paper_ids:
            assert paper_id in self.papers, f"Unknown citation ID: {paper_id}"
            if paper_id not in self.included_ids:
                self.included_ids.append(paper_id)

    def bibliography(self) -> str:
        for paper_id in self.included_ids:
            self.add(paper_id)
        if not self.ids:
            return ""
        entries = []
        for number, paper_id in enumerate(self.ids, 1):
            paper = self.papers[paper_id]
            backlink = f' <a class="reference-backlink" href="#{self.first_citation[number]}">↩</a>' if number in self.first_citation else ""
            entries.append(
                f'<li id="reference-{number}"><span class="reference-number">[{number}]</span> '
                f'<span>{external_link(paper["url"], paper["title"])}. {text(paper["venue"])} ({text(paper["year"])}).</span> '
                f'<span class="reference-links">{paper_links(paper)}</span>{backlink}</li>'
            )
        return '<section class="references" id="references"><p class="eyebrow">References</p><h2>Original papers and resources</h2><ol>' + "".join(entries) + "</ol></section>"


def paragraphs(values: list[str], citations: CitationRegistry, class_name: str = "") -> str:
    class_attr = f' class="{text(class_name)}"' if class_name else ""
    return "\n".join(f"<p{class_attr}>{citations.prose(value)}</p>" for value in values)


def validate_article(article: dict, papers: dict[str, dict]) -> None:
    for field in ("id", "title", "kicker", "dek", "reading_minutes", "intro", "sections", "takeaway", "next_topic"):
        assert article.get(field), f"Article missing {field}: {article.get('id', '<unknown>')}"
    assert article["id"] in ARTICLE_ORDER, article["id"]
    assert isinstance(article["reading_minutes"], int) and article["reading_minutes"] > 0, article["id"]
    assert isinstance(article["intro"], list) and all(isinstance(p, str) and p for p in article["intro"]), article["id"]
    assert isinstance(article["sections"], list) and article["sections"], article["id"]
    assert article["next_topic"] in ARTICLE_ORDER and article["next_topic"] != article["id"], article["id"]
    for section in article["sections"]:
        assert section.get("heading") and isinstance(section.get("paragraphs"), list), article["id"]
        assert all(isinstance(p, str) and p for p in section["paragraphs"]), article["id"]
        assert set(section.get("paper_ids", [])) <= set(papers), article["id"]
        table = section.get("table")
        if table is not None:
            assert set(table) == {"caption", "columns", "rows"}, f"Invalid table in {article['id']}"
            assert table["caption"] and table["columns"] and table["rows"], f"Empty table in {article['id']}"
            assert all(len(row) == len(table["columns"]) for row in table["rows"]), f"Uneven table in {article['id']}"
        callout = section.get("callout")
        if callout is not None:
            assert set(callout) == {"title", "text"} and callout["title"] and callout["text"], f"Invalid callout in {article['id']}"


def reading_minutes(article: dict) -> int:
    """Use visible prose for a transparent estimate (220 words per minute)."""
    import re
    strings = [article["title"], article["dek"], *article["intro"], article["takeaway"]]
    for section in article["sections"]:
        strings.extend([section["heading"], *section["paragraphs"]])
        if section.get("table"):
            strings.extend(section["table"]["columns"])
            strings.extend(cell for row in section["table"]["rows"] for cell in row)
        if section.get("callout"):
            strings.extend(section["callout"].values())
    words = re.findall(r"[A-Za-z0-9][A-Za-z0-9'-]*", " ".join(strings))
    return max(1, round(len(words) / 220))


def table_markup(table: dict, citations: CitationRegistry) -> str:
    caption = citations.prose(table["caption"])
    heading = "".join(f"<th scope=\"col\">{citations.prose(value)}</th>" for value in table["columns"])
    rows = "".join("<tr>" + "".join(f"<td>{citations.prose(value)}</td>" for value in row) + "</tr>" for row in table["rows"])
    return f'<figure class="comparison-table"><figcaption>{caption}</figcaption><div tabindex="0" role="region" aria-label="{text(table["caption"])}"><table><thead><tr>{heading}</tr></thead><tbody>{rows}</tbody></table></div></figure>'


def article_markup(article: dict, papers: dict[str, dict], articles: dict[str, dict], citations: CitationRegistry | None = None, section_prefix: str = "", media: dict[tuple[str, int], list[dict]] | None = None, section_heading: str = "h2", include_references: bool = True) -> dict[str, str]:
    citations = citations or CitationRegistry(papers)
    content, toc = [], []
    intro = paragraphs(article["intro"], citations, "article-lead")
    for number, section in enumerate(article["sections"], 1):
        section_id = f"{section_prefix}section-{number}"
        toc.append(f'<a href="#{section_id}">{text(section["heading"])}</a>')
        body = paragraphs(section["paragraphs"], citations)
        table = table_markup(section["table"], citations) if section.get("table") else ""
        callout = (f'<aside class="article-callout"><strong>{text(section["callout"]["title"])}</strong><p>{citations.prose(section["callout"]["text"])}</p></aside>' if section.get("callout") else "")
        section_media = "".join(media_markup(item) for item in (media or {}).get((article["id"], number), []))
        citations.include(section.get("paper_ids", []))
        content.append(f'<section id="{section_id}"><{section_heading}>{text(section["heading"])}</{section_heading}>{body}{table}{callout}{section_media}</section>')
    next_article = articles[article["next_topic"]]
    footer = (
        f'<aside class="article-takeaway"><p class="reading-label">Takeaway</p><p>{text(article["takeaway"])}</p></aside>'
        f'<a class="next-essay" href="{text(next_article["id"])}.html"><span>Next chapter</span><strong>{text(next_article["title"])} →</strong></a>'
        f'<a class="text-link" href="{"library.html?topic=" + text(article["id"]) if article["id"] in SITE_TOPICS else "library.html"}">Explore related papers ↗</a>'
    )
    return {
        "{{ARTICLE_TITLE}}": text(article["title"]), "{{ARTICLE_KICKER}}": text(article["kicker"]),
        "{{ARTICLE_DEK}}": text(article["dek"]), "{{READING_MINUTES}}": text(article["reading_minutes"]),
        "{{ARTICLE_INTRO}}": intro, "{{ARTICLE_CONTENT}}": "\n".join(content),
        "{{ARTICLE_TOC}}": "\n".join(toc), "{{ARTICLE_FOOTER}}": footer,
        "{{REFERENCES}}": citations.bibliography() if include_references else "",
    }


def replace_template(template_name: str, replacements: dict[str, str], required: set[str]) -> str:
    template_path = SITE / template_name
    assert template_path.is_file(), f"Missing site template: {template_path}"
    source = template_path.read_text()
    found = {token for token in required if token in source}
    assert found == required, f"Missing {template_name} placeholders: {sorted(required - found)}"
    for token, value in replacements.items():
        source = source.replace(token, value)
    assert not any(token in source for token in required), f"Unexpanded {template_name} placeholder"
    return source


def output_paths(directory: Path) -> set[str]:
    return {path.relative_to(directory).as_posix() for path in directory.rglob("*") if path.is_file()}


def load_media(papers: dict[str, dict]) -> list[dict]:
    """Load a small, explicit collection of credited figures and opt-in videos."""
    source = SITE / "media.json"
    if not source.exists():
        return []
    payload = json.loads(source.read_text())
    assert set(payload) == {"items"} and isinstance(payload["items"], list), "Invalid site/media.json"
    items = payload["items"]
    allowed = {"id", "chapter", "section_index", "paper_id", "type", "src", "poster", "title", "caption", "source_url", "credit", "license_label", "license_url"}
    seen = set()
    for item in items:
        assert set(item) <= allowed and {"id", "chapter", "section_index", "paper_id", "type", "src", "title", "caption", "source_url", "credit", "license_label", "license_url"} <= set(item), f"Invalid media item: {item}"
        assert re.fullmatch(r"[a-z0-9-]+", item["id"]) and item["id"] not in seen, f"Invalid media ID: {item.get('id')}"
        seen.add(item["id"])
        assert item["chapter"] in ARTICLE_ORDER and isinstance(item["section_index"], int) and item["section_index"] > 0
        assert item["paper_id"] in papers and item["type"] in {"image", "youtube", "video"}
        assert item["source_url"].startswith(("https://", "http://")) and item["license_url"].startswith(("https://", "http://"))
        if item["type"] == "image":
            assert item["src"].startswith("assets/paper-media/") and ".." not in item["src"], item["src"]
            assert (ROOT / item["src"]).is_file(), f"Missing media asset: {item['src']}"
        else:
            assert item["src"].startswith("https://"), "Remote video source must use HTTPS"
            if item.get("poster"):
                assert item["poster"].startswith("assets/paper-media/") and ".." not in item["poster"]
                assert (ROOT / item["poster"]).is_file(), f"Missing poster asset: {item['poster']}"
    return items


def expected_output_files(media: list[dict]) -> set[str]:
    copied = set()
    for item in media:
        if item["type"] == "image":
            copied.add(item["src"])
        if item.get("poster"):
            copied.add(item["poster"])
    return OUTPUT_FILES | copied


def media_markup(item: dict) -> str:
    caption = f'<figcaption><strong>{text(item["title"])}</strong><span>{text(item["caption"])}</span><small>{text(item["credit"])} · <a href="{text(item["license_url"])}" target="_blank" rel="noopener noreferrer">{text(item["license_label"])}</a> · <a href="{text(item["source_url"])}" target="_blank" rel="noopener noreferrer">Source ↗</a></small></figcaption>'
    if item["type"] == "image":
        body = f'<a href="{text(item["src"])}" target="_blank" rel="noopener"><img src="{text(item["src"])}" alt="{text(item["caption"])}" loading="lazy"></a>'
    elif item["type"] == "video":
        poster = f' poster="{text(item["poster"])}"' if item.get("poster") else ""
        body = f'<video controls preload="none"{poster}><source src="{text(item["src"])}">Your browser does not support this video.</video>'
    else:
        poster = f' style="background-image:url(\'{text(item["poster"])}\')"' if item.get("poster") else ""
        body = f'<button type="button" class="media-consent" data-youtube-src="{text(item["src"])}"{poster}><span>Play official video</span><small>Loads YouTube after you choose to play.</small></button>'
    return f'<figure class="paper-media" id="media-{text(item["id"])}">{body}{caption}</figure>'


def copy_output_files(destination: Path, media: list[dict]) -> None:
    sources = {
        "styles.css": SITE / "styles.css", "app.js": SITE / "app.js",
        "assets/survey-teaser.svg": ROOT / "assets" / "survey-teaser.svg",
        "assets/survey-teaser.png": ROOT / "assets" / "survey-teaser.png",
        "assets/survey-roadmap.svg": ROOT / "assets" / "survey-roadmap.svg",
        "assets/teaser-source/robocasa-kitchen-robot.png": ROOT / "assets" / "teaser-source" / "robocasa-kitchen-robot.png",
    }
    for relative, source in sources.items():
        assert source.is_file(), f"Missing public site asset: {source}"
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    for item in media:
        for relative in (item["src"] if item["type"] == "image" else None, item.get("poster")):
            if not relative:
                continue
            source = ROOT / relative
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
    (destination / ".nojekyll").touch()


def build(output: Path) -> None:
    for name in ("styles.css", "app.js"):
        assert (SITE / name).is_file(), f"Missing site source: {SITE / name}"
    catalog = json.loads((ROOT / "data" / "catalog.json").read_text())
    benchmarks = json.loads((ROOT / "data" / "benchmarks.json").read_text())
    routes = json.loads((ROOT / "data" / "reading_routes.json").read_text())
    papers = verify(catalog, benchmarks)
    verify_reading_routes(routes, papers)
    media_items = load_media(papers)
    media: dict[tuple[str, int], list[dict]] = {}
    for item in media_items:
        media.setdefault((item["chapter"], item["section_index"]), []).append(item)
    article_paths = {topic: SITE / "articles" / f"{topic}.json" for topic in ARTICLE_ORDER}
    assert all(path.is_file() for path in article_paths.values()), "Missing editorial article JSON"
    articles = {topic: json.loads(path.read_text()) for topic, path in article_paths.items()}
    for topic, article in articles.items():
        assert article["id"] == topic, f"Article id mismatch: {topic}"
        validate_article(article, papers)
        article["reading_minutes"] = reading_minutes(article)
    for (chapter, section_index), _ in media.items():
        assert section_index <= len(articles[chapter]["sections"]), f"Media section out of range: {chapter}/{section_index}"
    benchmark_names: dict[str, list[str]] = {paper_id: [] for paper_id in papers}
    for benchmark in benchmarks["benchmarks"]:
        for paper_id in benchmark.get("paper_ids", []):
            benchmark_names[paper_id].append(benchmark["name"])
    survey_citations = CitationRegistry(papers)
    chapter_toc, chapters = [], []
    for number, topic in enumerate(ARTICLE_ORDER, 1):
        article = articles[topic]
        chapter_id = f"chapter-{number}"
        rendered = article_markup(article, papers, articles, survey_citations, f"{chapter_id}-", media, "h3", False)
        chapter_toc.append(
            f'<a href="#{chapter_id}" title="{text(article["title"])}"><span>{number:02d}</span>{text(CHAPTER_LABELS[topic])}</a>'
        )
        chapters.append(
            f'<section class="survey-chapter" id="{chapter_id}" data-topic="{text(topic)}">'
            f'<header><p class="chapter-number">Chapter {number:02d}</p><p class="eyebrow">{text(article["kicker"])} · {text(article["reading_minutes"])} min read</p>'
            f'<h2>{text(article["title"])}</h2><p class="chapter-dek">{text(article["dek"])}</p>'
            f'<a class="chapter-link" href="{text(article["id"])}.html">Open this chapter ↗</a></header>'
            f'<div class="survey-chapter-body">{rendered["{{ARTICLE_INTRO}}"]}{rendered["{{ARTICLE_CONTENT}}"]}</div></section>'
        )
    standard = {
        "{{SURVEY_TOC}}": "\n".join(chapter_toc),
        "{{SURVEY_CHAPTERS}}": "\n".join(chapters),
        "{{REFERENCES}}": survey_citations.bibliography(),
        "{{TOPIC_BUTTONS}}": "\n".join(f'<button type="button" data-topic="{text(key)}" aria-pressed="false">{text(title)}</button>' for key, title, _ in TOPICS),
        "{{YEAR_OPTIONS}}": "\n".join(f'<option value="{year}">{year}</option>' for year in sorted({int(p["year"]) for p in papers.values()}, reverse=True)),
        "{{PAPER_ITEMS}}": "\n".join(paper_markup(paper, benchmark_names) for paper in sorted(papers.values(), key=lambda p: (-int(p["year"]), p["short"].lower()))),
        "{{TOTAL_PAPERS}}": text(len(papers)), "{{ROUTE_NAV}}": route_nav(routes["routes"]),
        "{{ROUTE_SECTIONS}}": route_sections(routes["routes"], papers),
        "{{BENCHMARK_ITEMS}}": "\n".join(benchmark_markup(item, papers) for item in benchmarks["benchmarks"]),
    }
    output = output.resolve()
    assert output.parent == ROOT.resolve(), "Output must be a direct repository child"
    with tempfile.TemporaryDirectory(prefix="survey-site-", dir=ROOT) as staging_name:
        staging = Path(staging_name)
        for filename, (template_name, required) in TEMPLATES.items():
            (staging / filename).write_text(replace_template(template_name, {token: standard[token] for token in required}, required))
        for topic, article in articles.items():
            (staging / f"{topic}.html").write_text(replace_template("article.template.html", article_markup(article, papers, articles, media=media), ARTICLE_TOKENS))
        copy_output_files(staging, media_items)
        actual = output_paths(staging)
        expected = expected_output_files(media_items)
        assert actual == expected, f"Unexpected static output: {sorted(actual ^ expected)}"
        if output.exists():
            existing = output_paths(output)
            assert existing <= expected, f"Refusing to replace unexpected files: {sorted(existing - expected)}"
            backup = output.with_name(output.name + ".previous")
            assert not backup.exists(), f"Existing build backup requires review: {backup}"
            output.rename(backup)
            staging.rename(output)
            shutil.rmtree(backup)
        else:
            staging.rename(output)
    assert output_paths(output) == expected_output_files(media_items)
    print(f"Built public editorial survey with {len(papers)} papers, {len(routes['routes'])} reading routes, {len(benchmarks['benchmarks'])} benchmarks, {len(articles)} chapters, and {len(media_items)} credited media items: {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    build(parser.parse_args().output)
