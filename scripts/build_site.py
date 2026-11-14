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
LANGUAGES = ("en", "zh")
PUBLIC_URL = "https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/"
TRANSLATIONS = json.loads((SITE / "locales" / "zh.json").read_text())
SITE_TOPICS = [topic for topic, _, _ in TOPICS]
# The full survey follows its argument rather than the database
# categories.  The last two chapters are deliberately cross-cutting.
ARTICLE_ORDER = ["overview", "perception", "reconstruction", "generation", "robotics", "datasets", "outlook"]
CHAPTER_LABELS = {
    "overview": "Scope & taxonomy", "perception": "Scene perception",
    "reconstruction": "Reconstruction", "generation": "Scene generation",
    "robotics": "Agents & interaction", "datasets": "Datasets & evaluation",
    "outlook": "Open questions",
}
OUTPUT_FILES = {
    ".nojekyll", "index.html", "survey.html", "library.html", "reading-routes.html", "benchmarks.html",
    "overview.html", "perception.html", "reconstruction.html", "generation.html", "robotics.html", "datasets.html", "outlook.html",
    "styles.css", "app.js", "assets/survey-teaser.svg", "assets/survey-teaser.png", "assets/survey-roadmap.svg",
    "assets/teaser-source/robocasa-kitchen-robot.png",
}
OUTPUT_FILES |= {"zh/" + name for name in tuple(OUTPUT_FILES) if name.endswith(".html")}
TEMPLATES = {
    "index.html": ("index.template.html", {"{{FEATURED_ROUTES}}", "{{CHAPTER_INDEX}}"}),
    "survey.html": ("survey.template.html", {"{{SURVEY_TOC}}", "{{SURVEY_CHAPTERS}}", "{{REFERENCES}}"}),
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


def ui(value: str, lang: str) -> str:
    if lang == "en":
        return value
    assert value in TRANSLATIONS, f"Missing Chinese interface translation: {value}"
    return TRANSLATIONS[value]


def asset_url(value: str, lang: str) -> str:
    return "../" + value if lang == "zh" and value.startswith("assets/") else value


def localized_directory(source: dict, translations: dict, key: str) -> dict:
    """Replace editorial text while keeping canonical identities and resources."""
    assert set(translations) == {item["id"] for item in source[key]}, f"Incomplete Chinese {key}"
    result = []
    for item in source[key]:
        translated = translations[item["id"]]
        permitted = {"evidence", "section"} if key == "papers" else ({"name", "task"} if key == "benchmarks" else {"title", "summary", "goal", "steps", "try_it"})
        assert set(translated) == permitted, f"Unexpected translation fields: {item['id']}"
        merged = {**item, **translated}
        if key == "routes":
            assert len(item["steps"]) == len(translated["steps"]), item["id"]
            merged["steps"] = []
            for original, step in zip(item["steps"], translated["steps"]):
                assert set(step) == {"label", "focus"}, item["id"]
                merged["steps"].append({**original, **step})
        result.append(merged)
    return {**source, key: result}


def external_link(url: str, label: str, extra_class: str = "") -> str:
    class_name = f' class="{text(extra_class)}"' if extra_class else ""
    return f'<a{class_name} href="{text(url)}" target="_blank" rel="noopener noreferrer">{text(label)}</a>'


def topic_label(key: str, lang: str = "en") -> str:
    return ui(next(title for topic, title, _ in TOPICS if topic == key), lang)


def paper_links(paper: dict, lang: str = "en") -> str:
    links = [external_link(paper["url"], ui("Paper", lang))]
    if paper.get("project_url"):
        links.append(external_link(paper["project_url"], ui("Project", lang)))
    if paper.get("code_url"):
        label = ui("Toolkit" if paper.get("code_kind") == "dataset-toolkit" else "Code", lang)
        if paper.get("code_status") == "placeholder":
            label += ui(" (announced)", lang)
        links.append(external_link(paper["code_url"], label))
    return " ".join(links)


def paper_markup(paper: dict, benchmark_names: dict[str, list[str]], lang: str = "en") -> str:
    topics = [paper["category"], *paper.get("additional_topics", {}).keys()]
    search = " ".join([
        paper["title"], paper["short"], paper["evidence"], paper["category"], paper["section"],
        paper["venue"], str(paper["year"]), " ".join(paper.get("roles", [])),
        " ".join(benchmark_names.get(paper["id"], [])), paper.get("search_extra", ""),
    ]).lower()
    code = "released" if paper.get("code_status") == "released" else paper.get("code_status", "not-located")
    return f'''<li class="paper-item" id="paper-{text(paper['id'])}" data-id="{text(paper['id'])}" data-topics="{text(' '.join(topics))}" data-year="{text(paper['year'])}" data-title="{text(paper['title'].lower())}" data-search="{text(search)}" data-code="{text(code)}">
  <article class="paper">
    <div class="paper-meta"><span class="paper-year">{text(paper['year'])}</span><span class="paper-venue">{text(paper['venue'])}</span></div>
    <div class="paper-body">
      <p class="paper-kicker">{text(topic_label(paper['category'], lang))} · {text(paper['section'])}</p>
      <h3 class="paper-title">{external_link(paper['url'], paper['title'])}</h3>
      <p class="paper-summary">{text(paper['evidence'])}</p>
      <div class="paper-links">{paper_links(paper, lang)}</div>
    </div>
  </article>
</li>'''


def route_nav(routes: list[dict]) -> str:
    return "\n".join(
        f'<a class="route-index-item" href="#route-{text(route["id"])}">'
        f'<span class="route-index-title">{text(route["title"])}</span>'
        f'<span class="route-index-summary">{text(route["summary"])}</span></a>' for route in routes
    )


def route_sections(routes: list[dict], papers: dict[str, dict], lang: str = "en") -> str:
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
  <ol class="route-steps">{' '.join(steps)}</ol><p class="route-exercise"><strong>{text(ui("Try it:", lang))}</strong> {text(route['try_it'])}</p>
</section>''')
    return "\n".join(sections)


def benchmark_markup(benchmark: dict, papers: dict[str, dict], lang: str = "en") -> str:
    links = [external_link(benchmark["url"], ui("Official protocol", lang))]
    if benchmark.get("leaderboard_url"):
        links.append(external_link(benchmark["leaderboard_url"], ui("Leaderboard", lang)))
    for paper_id in benchmark.get("paper_ids", [])[:6]:
        links.append(f'<a href="library.html#paper-{text(paper_id)}" data-paper-link="{text(paper_id)}">{text(papers[paper_id]["short"])}</a>')
    if len(benchmark.get("paper_ids", [])) > 6:
        links.append(external_link('https://github.com/HyoKong/Awesome-3D-Scene-Understanding-and-Interaction/blob/main/BENCHMARKS.md', ui('Full guide', lang)))
    return f'''<article class="benchmark-item" id="benchmark-{text(benchmark['id'])}">
  <h3>{external_link(benchmark['url'], benchmark['name'])}</h3><p>{text(benchmark['task'])}</p><div class="benchmark-links">{' '.join(links)}</div>
</article>'''


class CitationRegistry:
    """Assign stable per-page reference numbers while rendering escaped prose."""

    def __init__(self, papers: dict[str, dict], lang: str = "en"):
        self.papers = papers
        self.lang = lang
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
                f'<a class="citation" id="{citation_id}" href="#reference-{number}" title="{text(self.papers[paper_id]["title"])}" aria-label="{text(ui("Reference", self.lang))} {number}: {text(self.papers[paper_id]["short"])}">[{number}]</a>'
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
                f'<span class="reference-links">{paper_links(paper, self.lang)}</span>{backlink}</li>'
            )
        return f'<section class="references" id="references"><p class="eyebrow">{text(ui("References", self.lang))}</p><h2>{text(ui("Original papers and resources", self.lang))}</h2><ol>' + "".join(entries) + "</ol></section>"


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


def reading_minutes(article: dict, lang: str = "en") -> int:
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
    prose = re.sub(r"\[cite:[^\]]+\]", "", " ".join(strings))
    words = re.findall(r"[A-Za-z0-9][A-Za-z0-9'-]*", prose)
    chinese = len(re.findall(r"[\u4e00-\u9fff]", prose)) if lang == "zh" else 0
    return max(1, round(len(words) / 220 + chinese / 500))


def table_markup(table: dict, citations: CitationRegistry) -> str:
    caption = citations.prose(table["caption"])
    heading = "".join(f"<th scope=\"col\">{citations.prose(value)}</th>" for value in table["columns"])
    rows = "".join("<tr>" + "".join(f"<td>{citations.prose(value)}</td>" for value in row) + "</tr>" for row in table["rows"])
    return f'<figure class="comparison-table"><figcaption>{caption}</figcaption><div tabindex="0" role="region" aria-label="{text(table["caption"])}"><table><thead><tr>{heading}</tr></thead><tbody>{rows}</tbody></table></div></figure>'


def article_markup(article: dict, papers: dict[str, dict], articles: dict[str, dict], citations: CitationRegistry | None = None, section_prefix: str = "", media: dict[tuple[str, int], list[dict]] | None = None, section_heading: str = "h2", include_references: bool = True, lang: str = "en") -> dict[str, str]:
    citations = citations or CitationRegistry(papers, lang)
    content, toc = [], []
    intro = paragraphs(article["intro"], citations, "article-lead")
    for number, section in enumerate(article["sections"], 1):
        section_id = f"{section_prefix}section-{number}"
        toc.append(f'<a href="#{section_id}">{text(section["heading"])}</a>')
        body = paragraphs(section["paragraphs"], citations)
        table = table_markup(section["table"], citations) if section.get("table") else ""
        callout = (f'<aside class="article-callout"><strong>{text(section["callout"]["title"])}</strong><p>{citations.prose(section["callout"]["text"])}</p></aside>' if section.get("callout") else "")
        section_media = "".join(media_markup(item, lang) for item in (media or {}).get((article["id"], number), []))
        citations.include(section.get("paper_ids", []))
        content.append(f'<section id="{section_id}"><{section_heading}>{text(section["heading"])}</{section_heading}>{body}{table}{callout}{section_media}</section>')
    next_article = articles[article["next_topic"]]
    footer = (
        f'<aside class="article-takeaway"><p class="reading-label">{text(ui("Takeaway", lang))}</p><p>{text(article["takeaway"])}</p></aside>'
        f'<a class="next-essay" href="{text(next_article["id"])}.html"><span>{text(ui("Next chapter", lang))}</span><strong>{text(next_article["title"])} →</strong></a>'
        f'<a class="text-link" href="{"library.html?topic=" + text(article["id"]) if article["id"] in SITE_TOPICS else "library.html"}">{text(ui("Explore related papers ↗", lang))}</a>'
    )
    return {
        "{{ARTICLE_TITLE}}": text(article["title"]), "{{ARTICLE_KICKER}}": text(article["kicker"]),
        "{{ARTICLE_DEK}}": text(article["dek"]), "{{READING_MINUTES}}": text(article["reading_minutes"]),
        "{{ARTICLE_INTRO}}": intro, "{{ARTICLE_CONTENT}}": "\n".join(content),
        "{{ARTICLE_TOC}}": "\n".join(toc), "{{ARTICLE_FOOTER}}": footer,
        "{{REFERENCES}}": citations.bibliography() if include_references else "",
    }


def replace_template(template_name: str, replacements: dict[str, str], required: set[str], lang: str, filename: str) -> str:
    source = (SITE / template_name).read_text()
    assert all(token in source for token in required), f"Missing {template_name} placeholder"
    prefix = "../" if lang == "zh" else ""
    english = prefix + filename if lang == "zh" else filename
    chinese = filename if lang == "zh" else "zh/" + filename
    switch = '<span class="language-switch" role="group" aria-label="' + text(ui("Language", lang)) + '">'
    for code, label, href in (("en", "EN", english), ("zh", "中文", chinese)):
        current = ' aria-current="page"' if code == lang else ""
        switch += f'<a href="{text(href)}" hreflang="{code}" lang="{code}" data-language-switch{current}>{label}</a>'
    switch += '</span>'
    common = {
        "{{HTML_LANG}}": "zh-CN" if lang == "zh" else "en",
        "{{ASSET_PREFIX}}": prefix,
        "{{LANGUAGE_SWITCH}}": switch,
        "{{EN_URL}}": PUBLIC_URL + filename,
        "{{ZH_URL}}": PUBLIC_URL + "zh/" + filename,
    }
    for token, value in {**common, **replacements}.items():
        source = source.replace(token, value)
    source = re.sub(r"\{\{t:(.*?)\}\}", lambda match: text(ui(match[1], lang)), source)
    assert "{{" not in source, f"Unexpanded {template_name} placeholder"
    return source


def output_paths(directory: Path) -> set[str]:
    return {path.relative_to(directory).as_posix() for path in directory.rglob("*") if path.is_file()}


def load_media(papers: dict[str, dict]) -> list[dict]:
    """Validate an explicit collection of credited, bilingual paper visuals."""
    payload = json.loads((SITE / "media.json").read_text())
    assert set(payload) == {"items"} and isinstance(payload["items"], list), "Invalid site/media.json"
    items = payload["items"]
    required = {"id", "chapter", "section_index", "paper_id", "type", "src", "title", "caption", "source_url", "credit", "license_label", "license_url", "zh"}
    allowed = required | {"poster", "width", "height"}
    seen = set()
    for item in items:
        assert required <= set(item) <= allowed, f"Invalid media fields: {item.get('id')}"
        assert re.fullmatch(r"[a-z0-9-]+", item["id"]) and item["id"] not in seen, item.get("id")
        seen.add(item["id"])
        assert item["chapter"] in ARTICLE_ORDER and isinstance(item["section_index"], int) and item["section_index"] > 0
        assert item["paper_id"] in papers and item["type"] in {"image", "youtube", "video"}
        assert set(item["zh"]) == {"title", "caption", "credit", "license_label"} and all(item["zh"].values()), f"Missing Chinese media text: {item['id']}"
        for key in ("source_url", "license_url"):
            assert item[key].startswith("https://"), item[key]
        for key in ("src", "poster"):
            value = item.get(key)
            if not value:
                continue
            if value.startswith("https://"):
                continue
            assert (key == "poster" or item["type"] == "image") and value.startswith("assets/paper-media/") and ".." not in value, value
            assert (ROOT / value).is_file() and not (ROOT / value).is_symlink(), f"Invalid local media: {value}"
        if item["type"] == "youtube":
            assert re.fullmatch(r"https://www\.youtube-nocookie\.com/embed/[A-Za-z0-9_-]+", item["src"]), item["src"]
        for key in ("width", "height"):
            if key in item:
                assert isinstance(item[key], int) and item[key] > 0, item["id"]
        assert ("width" in item) == ("height" in item), item["id"]
    return items


def expected_output_files(media: list[dict]) -> set[str]:
    copied = {item[key] for item in media for key in ("src", "poster") if item.get(key, "").startswith("assets/")}
    return OUTPUT_FILES | copied


def media_markup(item: dict, lang: str = "en") -> str:
    labels = item if lang == "en" else item["zh"]
    caption = f'<figcaption><strong><a href="library.html#paper-{text(item["paper_id"])}">{text(labels["title"])}</a></strong><span>{text(labels["caption"])}</span><small>{text(labels["credit"])} · <a href="{text(item["license_url"])}" target="_blank" rel="noopener noreferrer">{text(labels["license_label"])}</a> · <a href="{text(item["source_url"])}" target="_blank" rel="noopener noreferrer">{text(ui("Source ↗", lang))}</a></small></figcaption>'
    source = text(asset_url(item["src"], lang))
    dimensions = f' width="{item["width"]}" height="{item["height"]}"' if item.get("width") else ""
    if item["type"] == "image":
        body = f'<a href="{source}" target="_blank" rel="noopener"><img src="{source}" alt="{text(labels["caption"])}"{dimensions} loading="lazy" decoding="async"></a>'
    elif item["type"] == "video":
        poster = f' poster="{text(asset_url(item["poster"], lang))}"' if item.get("poster") else ""
        preload = "none" if poster else "metadata"
        body = f'<video controls playsinline preload="{preload}" aria-label="{text(labels["title"])}"{poster}><source src="{source}">{text(ui("Your browser does not support this video.", lang))}</video>'
    else:
        poster = f' style="background-image:url(\'{text(asset_url(item["poster"], lang))}\')"' if item.get("poster") else ""
        body = f'<button type="button" class="media-consent" data-youtube-src="{source}"{poster}><span>{text(ui("Play official video", lang))}</span><small>{text(ui("Loads YouTube after you choose to play.", lang))}</small></button>'
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
            if not relative or not relative.startswith("assets/"):
                continue
            source = ROOT / relative
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
    (destination / ".nojekyll").touch()


HOME_ROUTES = {
    "perception": ["scene-perception", "language-and-function", "articulated-perception"],
    "reconstruction": ["scene-reconstruction", "reconstruction", "articulated-perception"],
    "generation": ["scene-generation", "generation", "reconstruction"],
    "robotics": ["spatial-navigation", "manipulation", "policies-and-agents"],
}


def featured_routes(routes: list[dict], papers: dict[str, dict], lang: str) -> str:
    cards = []
    for route in routes:
        topics = [topic for topic, ids in HOME_ROUTES.items() if route["id"] in ids]
        if not topics:
            continue
        first = route["steps"][0]
        starting_papers = " · ".join(papers[pid]["short"] for pid in first["paper_ids"])
        cards.append(
            f'<article class="home-route" data-route-topics="{text(" ".join(topics))}">'
            f'<h3><a href="reading-routes.html#route-{text(route["id"])}">{text(route["title"])}</a></h3>'
            f'<p>{text(route["goal"])}</p><p class="route-start"><span>{text(ui("Start with", lang))}</span>{text(starting_papers)}</p>'
            f'<a class="text-link" href="reading-routes.html#route-{text(route["id"])}">{text(ui("Follow this route →", lang))}</a></article>'
        )
    return "".join(cards)


def build(output: Path) -> None:
    catalog = json.loads((ROOT / "data/catalog.json").read_text())
    benchmarks = json.loads((ROOT / "data/benchmarks.json").read_text())
    routes = json.loads((ROOT / "data/reading_routes.json").read_text())
    papers = verify(catalog, benchmarks)
    verify_reading_routes(routes, papers)
    media_items = load_media(papers)
    media: dict[tuple[str, int], list[dict]] = {}
    for item in media_items:
        media.setdefault((item["chapter"], item["section_index"]), []).append(item)
    chinese_catalog = localized_directory(catalog, json.loads((SITE / "zh/catalog.json").read_text()), "papers")
    chinese_routes = localized_directory(routes, json.loads((SITE / "zh/reading_routes.json").read_text()), "routes")
    chinese_benchmarks = localized_directory(benchmarks, json.loads((SITE / "zh/benchmarks.json").read_text()), "benchmarks")
    chinese_papers = {paper["id"]: paper for paper in chinese_catalog["papers"]}
    for pid, paper in papers.items():
        bilingual_search = " ".join([paper["evidence"], paper["section"], chinese_papers[pid]["evidence"], chinese_papers[pid]["section"]])
        paper["search_extra"] = chinese_papers[pid]["search_extra"] = bilingual_search
    output = output.resolve()
    assert output.parent == ROOT.resolve(), "Output must be a direct repository child"
    with tempfile.TemporaryDirectory(prefix="survey-site-", dir=ROOT) as staging_name:
        staging = Path(staging_name)
        for lang in LANGUAGES:
            destination = staging if lang == "en" else staging / "zh"
            destination.mkdir(exist_ok=True)
            article_dir = SITE / "articles" if lang == "en" else SITE / "zh/articles"
            articles = {topic: json.loads((article_dir / f"{topic}.json").read_text()) for topic in ARTICLE_ORDER}
            localized_papers = papers if lang == "en" else chinese_papers
            local_routes = routes if lang == "en" else chinese_routes
            local_benchmarks = benchmarks if lang == "en" else chinese_benchmarks
            for topic, article in articles.items():
                assert article["id"] == topic, f"Article id mismatch: {topic}"
                validate_article(article, papers)
                article["reading_minutes"] = reading_minutes(article, lang)
            for (chapter, section_index) in media:
                assert section_index <= len(articles[chapter]["sections"]), f"Media section out of range: {chapter}/{section_index}"
            benchmark_names: dict[str, list[str]] = {pid: [] for pid in papers}
            for resource in [*benchmarks["benchmarks"], *chinese_benchmarks["benchmarks"]]:
                for pid in resource.get("paper_ids", []):
                    benchmark_names[pid].append(resource["name"])
            survey_citations = CitationRegistry(papers, lang)
            chapter_toc, chapters, chapter_index = [], [], []
            for number, topic in enumerate(ARTICLE_ORDER, 1):
                article = articles[topic]
                chapter_id = f"chapter-{number}"
                rendered = article_markup(article, papers, articles, survey_citations, f"{chapter_id}-", media, "h3", False, lang)
                chapter_toc.append(f'<a href="#{chapter_id}" title="{text(article["title"])}"><span>{number:02d}</span>{text(ui(CHAPTER_LABELS[topic], lang))}</a>')
                chapter_index.append(f'<a href="{topic}.html"><span>{number:02d}</span><div><strong>{text(ui(CHAPTER_LABELS[topic], lang))}</strong><p>{text(article["title"])}</p></div><b aria-hidden="true">↗</b></a>')
                chapter_name = f"Chapter {number:02d}" if lang == "en" else f"第 {number:02d} 章"
                chapters.append(
                    f'<section class="survey-chapter" id="{chapter_id}" data-topic="{text(topic)}">'
                    f'<header><p class="chapter-number">{chapter_name}</p><p class="eyebrow">{text(article["kicker"])} · {text(article["reading_minutes"])} {text(ui("min read", lang))}</p>'
                    f'<h2>{text(article["title"])}</h2><p class="chapter-dek">{text(article["dek"])}</p>'
                    f'<a class="chapter-link" href="{topic}.html">{text(ui("Open this chapter ↗", lang))}</a></header>'
                    f'<div class="survey-chapter-body">{rendered["{{ARTICLE_INTRO}}"]}{rendered["{{ARTICLE_CONTENT}}"]}</div></section>'
                )
            standard = {
                "{{SURVEY_TOC}}": "".join(chapter_toc), "{{SURVEY_CHAPTERS}}": "".join(chapters),
                "{{REFERENCES}}": survey_citations.bibliography(),
                "{{FEATURED_ROUTES}}": featured_routes(local_routes["routes"], papers, lang),
                "{{CHAPTER_INDEX}}": "".join(chapter_index),
                "{{TOPIC_BUTTONS}}": "".join(f'<button type="button" data-topic="{text(key)}" aria-pressed="false">{text(ui(title, lang))}</button>' for key, title, _ in TOPICS),
                "{{YEAR_OPTIONS}}": "".join(f'<option value="{year}">{year}</option>' for year in sorted({int(p["year"]) for p in papers.values()}, reverse=True)),
                "{{PAPER_ITEMS}}": "".join(paper_markup(paper, benchmark_names, lang) for paper in sorted(localized_papers.values(), key=lambda p: (-int(p["year"]), p["short"].lower()))),
                "{{TOTAL_PAPERS}}": text(len(papers)), "{{ROUTE_NAV}}": route_nav(local_routes["routes"]),
                "{{ROUTE_SECTIONS}}": route_sections(local_routes["routes"], papers, lang),
                "{{BENCHMARK_ITEMS}}": "".join(benchmark_markup(item, papers, lang) for item in local_benchmarks["benchmarks"]),
            }
            for filename, (template_name, required) in TEMPLATES.items():
                rendered = replace_template(template_name, {token: standard[token] for token in required}, required, lang, filename)
                (destination / filename).write_text(rendered)
            for topic, article in articles.items():
                filename = f"{topic}.html"
                rendered = replace_template("article.template.html", article_markup(article, papers, articles, media=media, lang=lang), ARTICLE_TOKENS, lang, filename)
                (destination / filename).write_text(rendered)
        copy_output_files(staging, media_items)
        expected = expected_output_files(media_items)
        assert output_paths(staging) == expected, "Unexpected static output"
        if output.exists():
            assert output_paths(output) <= expected, f"Refusing to replace unexpected files: {sorted(output_paths(output) - expected)}"
            backup = output.with_name(output.name + ".previous")
            assert not backup.exists(), f"Existing build backup requires review: {backup}"
            output.rename(backup)
            staging.rename(output)
            shutil.rmtree(backup)
        else:
            staging.rename(output)
    assert output_paths(output) == expected_output_files(media_items)
    print(f"Built English and Chinese survey: {len(papers)} papers, {len(routes['routes'])} routes, {len(articles)} chapters per language, {len(media_items)} credited visuals: {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    build(parser.parse_args().output)
