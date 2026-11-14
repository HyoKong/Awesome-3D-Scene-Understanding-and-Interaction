#!/usr/bin/env python3
"""Generate public survey pages from the checked catalog records."""

from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse
import json
import re

ROOT = Path(__file__).resolve().parents[1]
TOPICS = [
    ("perception", "Scene and functional perception", "from 3D observations to parts, semantics, affordances, state, and language-grounded scene structure"),
    ("reconstruction", "Scene reconstruction and digital twins", "recovering scene geometry, appearance, camera motion, dynamic structure, and interactive digital twins"),
    ("generation", "Scene generation and asset authoring", "generating scene layouts, 3D environments, procedural worlds, and interactive assets"),
    ("robotics", "Embodied agents and robotic interaction", "connecting spatial memory, navigation, embodied reasoning, task planning, and manipulation"),
    ("datasets", "Datasets, simulators, and benchmarks", "the data, environments, and evaluation protocols that make comparisons meaningful"),
]
TOPIC_MAP = {key: (title, description) for key, title, description in TOPICS}


def cell(value):
    return str(value).replace("|", "&#124;").replace("\n", " ")


def write(path, lines):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n")


def resources(paper):
    project = f"[Project]({paper['project_url']})" if paper.get("project_url") else "Project: —"
    if not paper.get("code_url"):
        code = "Code: announced" if paper.get("code_status") == "placeholder" else "Code: —"
    elif paper.get("code_status") == "placeholder":
        code = f"[Code (announced)]({paper['code_url']})"
    else:
        label = "Toolkit" if paper.get("code_kind") == "dataset-toolkit" else "Code"
        code = f"[{label}]({paper['code_url']})"
    return project + " · " + code


def verify(catalog, benchmark_data):
    papers = catalog["papers"]
    assert len({p["id"] for p in papers}) == len(papers), "Duplicate paper IDs"
    normalized = [re.sub(r"\W", "", p["title"].lower()) for p in papers]
    assert len(set(normalized)) == len(normalized), "Duplicate paper titles"
    for paper in papers:
        for key in ("id", "short", "title", "year", "venue", "url", "evidence", "category", "section", "scope", "project_url", "code_url", "code_status", "link_sources", "last_verified"):
            assert key in paper, f"Missing {key}: {paper.get('id', '<unknown>')}"
        assert paper["category"] in TOPIC_MAP, paper["id"]
        additional = paper.get("additional_topics", {})
        assert isinstance(additional, dict), paper["id"]
        assert set(additional) <= set(TOPIC_MAP), paper["id"]
        assert paper["category"] not in additional, f"Redundant primary topic: {paper['id']}"
        assert all(isinstance(section, str) and section.strip() for section in additional.values()), paper["id"]
        resource_roles = {"dataset", "method-and-dataset", "scene-dataset", "simulator", "benchmark", "simulator-and-assets", "benchmark-and-demos"}
        if resource_roles.intersection(paper.get("roles", [])):
            assert paper["category"] == "datasets" or "datasets" in additional, f"Resource missing from datasets topic: {paper['id']}"
        if "dataset_summary" in paper:
            assert isinstance(paper["dataset_summary"], str) and paper["dataset_summary"].strip(), paper["id"]
        assert paper["scope"] in {"core", "enabling"}, paper["id"]
        assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", paper["id"]), paper["id"]
        assert paper["code_status"] in {"released", "placeholder", "not-located"}, paper["id"]
        assert paper["code_status"] != "released" or paper["code_url"], paper["id"]
        assert paper["link_sources"], f"Missing source provenance: {paper['id']}"
        for key in ("url", "project_url", "code_url"):
            if paper[key]:
                assert urlparse(paper[key]).scheme in {"https", "http"}, (paper["id"], key)
        if paper["code_url"]:
            assert paper.get("code_status") in {"released", "placeholder"}, paper["id"]
    paper_map = {p["id"]: p for p in papers}
    assert len({b["id"] for b in benchmark_data["benchmarks"]}) == len(benchmark_data["benchmarks"]), "Duplicate benchmark IDs"
    for benchmark in benchmark_data["benchmarks"]:
        assert benchmark["id"] and benchmark["url"] and benchmark["task"], benchmark
        assert set(benchmark.get("paper_ids", [])) <= set(paper_map), benchmark["id"]
    return paper_map


def topic_records(catalog, category, include_additional=False):
    records = [p for p in catalog["papers"]
               if p["category"] == category or (include_additional and category in p.get("additional_topics", {}))]
    return sorted(records, key=lambda p: (-int(p["year"]), p["short"].lower()))


def verify_reading_routes(data, paper_map):
    routes = data["routes"]
    assert routes, "No reading routes"
    assert len({route["id"] for route in routes}) == len(routes), "Duplicate route IDs"
    for route in routes:
        assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", route["id"]), route["id"]
        for field in ("title", "summary", "goal", "try_it", "steps", "topics"):
            assert route[field], f"Missing route {field}: {route['id']}"
        assert set(route["topics"]) <= set(TOPIC_MAP), route["id"]
        for step in route["steps"]:
            assert step["label"] and step["focus"] and step["paper_ids"], route["id"]
            assert set(step["paper_ids"]) <= set(paper_map), f"Unknown route paper: {route['id']}"


def build_reading_routes(data, paper_map):
    lines = [
        "## Reading routes", "",
        "Follow a route in order, or jump to the part you need. Papers grouped in one stage offer complementary approaches; each linked entry includes project and code resources where available.", "",
    ]
    for route in data["routes"]:
        lines += [
            f'<a id="route-{route["id"]}"></a>', "",
            f'### {route["title"]}', "",
            f'*{route["summary"]}*', "",
            route["goal"], "",
            "| Stage | Suggested reading | What to look for |", "| --- | --- | --- |",
        ]
        for i, step in enumerate(route["steps"], 1):
            papers = " · ".join(f"[{cell(paper_map[pid]['short'])}](PAPERS.md#{pid})" for pid in step["paper_ids"])
            lines.append(f"| **{i}. {cell(step['label'])}** | {papers} | {cell(step['focus'])} |")
        topics = " · ".join(f"[{TOPIC_MAP[category][0]}](topics/{category}.md)" for category in route["topics"])
        lines += ["", f"**Try it:** {route['try_it']}", "", f"**Explore more:** {topics} · [Back to contents](#contents)", ""]
    return lines


def build_contents(reading_routes):
    routes = "<br>".join(f"[{route['title']}](#route-{route['id']})" for route in reading_routes["routes"])
    topics = "<br>".join(f"[{title}](topics/{category}.md)" for category, title, _ in TOPICS)
    topics += "<br><br>**Resources**<br>[Research map](#research-map)<br>[Paper index](PAPERS.md)<br>[Benchmark guide](BENCHMARKS.md)<br>[Contributing](CONTRIBUTING.md)"
    return ["## Contents", "", "| Reading routes | Topic collections |", "| --- | --- |", f"| {routes} | {topics} |", ""]


def build_readme(catalog, reading_routes, paper_map):
    hero = "survey-teaser.svg"
    lines = [
        f"# {catalog['title']}", "",
        "> Perception, reconstruction, generation, robotic manipulation, and embodied agents.", "",
        f"[![Survey map: four numbered callouts on a RoboCasa kitchen-and-robot scene match the sections on perception, functional understanding, reconstruction and generation, and manipulation and agents.](assets/{hero})](assets/survey-teaser.png)", "",
    ]
    lines += build_contents(reading_routes)
    lines += [
        "A collection of papers and resources on 3D scene understanding, reconstruction, generation, and embodied interaction. Topics span scene geometry and appearance, spatial reasoning, generated environments, navigation, manipulation, and articulated objects.", "",
        "Explore the reading routes, illustrated chapters, and searchable paper library on the website: [English](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/) · [中文](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/zh/).", "",
    ]
    lines += build_reading_routes(reading_routes, paper_map)
    lines += [
        "## Research map", "", "The [research roadmap](assets/survey-roadmap.svg) connects scene understanding, reconstruction, generation, and robotic interaction. Browse the topic collections below for more papers.", "",
        "| Topic | What it covers |", "| --- | --- |",
    ]
    for category, title, description in TOPICS:
        lines.append(f"| [{title}](topics/{category}.md) | {description} |")
    lines += [
        "", "## Benchmarks", "", "The [benchmark guide](BENCHMARKS.md) collects scene understanding and robotics benchmarks, with links to datasets, evaluation protocols, and related papers.", "",
        "## Contributing", "", "Contributions are welcome: suggest papers, add official project or code links, correct entries, or improve the organization. See the [contribution guide](CONTRIBUTING.md).", "",
        "[Survey scope](ROADMAP.md) · [Figure attribution](assets/ATTRIBUTION.md)",
    ]
    write(ROOT / "README.md", lines)


def build_topics(catalog, benchmarks):
    for category, title, description in TOPICS:
        groups = defaultdict(list)
        for paper in topic_records(catalog, category, include_additional=True):
            section = paper.get("additional_topics", {}).get(category) or paper["section"]
            groups[section].append(paper)
        lines = [f"# {title}", "", f"> {description[0].upper() + description[1:]}.", "", "[← Overview](../README.md) · [Full paper index](../PAPERS.md) · [Benchmarks](../BENCHMARKS.md) · [Contribute](../CONTRIBUTING.md)", "", "Papers are grouped by editorial section and ordered newest first within each section. Classification expresses relevance, not a rank.", ""]
        order = catalog.get("section_order", {}).get(category, [])
        sections = sorted(groups, key=lambda section: (order.index(section) if section in order else len(order), section))
        navigation = [f"[{section}](#section-{i + 1})" for i, section in enumerate(sections)]
        if category == "datasets":
            navigation.append("[Benchmark and resource directory](#resource-directory)")
        lines += [" · ".join(navigation), ""]
        for i, section in enumerate(sections):
            entries = groups[section]
            lines += [f'<a id="section-{i + 1}"></a>', ""]
            lines += [f"## {section}", "", "| Paper | Focus | Official resources |", "| --- | --- | --- |"]
            for paper in entries:
                focus = paper.get("summary", paper["evidence"])
                if category == "datasets":
                    focus = paper.get("dataset_summary", focus)
                title_link = f"[{cell(paper['title'])}]({paper['url']})"
                lines.append(f"| {title_link}<br>{cell(paper['venue'])} {paper['year']} · {paper['scope']} | {cell(focus)} | {resources(paper)} · [Details](../PAPERS.md#{paper['id']}) |")
            lines.append("")
        if category == "datasets":
            lines += [
                '<a id="resource-directory"></a>', "", "## Benchmark and resource directory", "",
                "Datasets, simulators, challenges, and evaluation resources from the [benchmark guide](../BENCHMARKS.md).", "",
            ] + benchmark_table(benchmarks["benchmarks"]) + [""]
        write(ROOT / "topics" / f"{category}.md", lines)


def build_index(catalog):
    lines = ["# Complete paper index", "", "[← Overview](README.md) · [Topic pages](#topic-directory) · [Benchmarks](BENCHMARKS.md)", "", "Every source-checked catalog record appears here once. Links are primary publications; resource links and release status are recorded without treating missing links as evidence of absence.", "", "## Topic directory", ""]
    for category, title, _ in TOPICS:
        lines.append(f"- [{title}](topics/{category}.md)")
    for category, title, _ in TOPICS:
        lines += ["", f"## {title}", ""]
        for paper in topic_records(catalog, category):
            lines += [f"<a id=\"{paper['id']}\"></a>", "", f"### {paper['short']} ({paper['year']})", "", f"**[{paper['title']}]({paper['url']})** — {paper['venue']} {paper['year']} · **{paper['scope'].capitalize()}** · {paper.get('section', paper.get('subtopic', category))}.", "", paper.get("summary", paper["evidence"]), "", resources(paper), ""]
            if paper.get("link_notes"):
                lines += [f"Resource note: {paper['link_notes']}", ""]
            if paper.get("benchmarks"):
                lines += ["Benchmark connections: " + ", ".join(paper["benchmarks"]) + ". This is a relevance link, not a leaderboard claim.", ""]
            lines += [f"Checked: {paper.get('last_verified', catalog['verified_on'])}.", ""]
    write(ROOT / "PAPERS.md", lines)


def benchmark_table(benchmarks):
    lines = ["| Benchmark / resource | Tasks and relevance | Official entry point |", "| --- | --- | --- |"]
    for benchmark in benchmarks:
        links = f"[Website]({benchmark['url']})"
        if benchmark.get("leaderboard_url"):
            links += f" · [Evaluation / leaderboard]({benchmark['leaderboard_url']})"
        lines.append(f"| {cell(benchmark['name'])} | {cell(benchmark['task'])} | {links} |")
    return lines


def build_benchmarks(data, paper_map):
    lines = ["# Benchmarks and discovery map", "", "[← Overview](README.md) · [Topic pages](PAPERS.md#topic-directory) · [Full paper index](PAPERS.md)", "", "Datasets, tasks, and evaluation protocols for 3D scenes and embodied interaction. Catalog connections identify related literature; compare results within the relevant task and protocol.", "", "## Navigator", ""] + benchmark_table(data["benchmarks"])
    for benchmark in data["benchmarks"]:
        lines += ["", f"## {benchmark['name']}", "", f"**Task:** {benchmark['task']}", "", f"**Protocol / status:** {benchmark['protocol_notes']}", ""]
        if benchmark.get("related_challenge_url"):
            lines += [f"**Related challenge:** [Articulate3D challenge]({benchmark['related_challenge_url']}).", ""]
        if benchmark.get("relationship_provenance"):
            lines += [f"**Relationship note:** {benchmark['relationship_provenance']}", ""]
        if benchmark.get("paper_ids"):
            links = " · ".join(f"[{paper_map[pid]['short']}](PAPERS.md#{pid})" for pid in benchmark['paper_ids'])
            lines += [f"**Catalog connections:** {links}.", ""]
        if benchmark.get("unresolved_entries"):
            lines += ["**Unresolved entries / coverage gaps:**", ""]
            for entry in benchmark["unresolved_entries"]:
                lines.append("- " + (entry if isinstance(entry, str) else json.dumps(entry, ensure_ascii=False)))
            lines.append("")
        lines += [f"[Official source]({benchmark['url']})" + (f" · [Evaluation / leaderboard]({benchmark['leaderboard_url']})" if benchmark.get("leaderboard_url") else ""), ""]
    lines += ["## How records enter the catalog", "", "1. Inspect the exact benchmark task and public track.", "2. Resolve a named method to a primary publication and official resources.", "3. Record version, split, modality, and relevant protocol differences.", "4. Keep anonymous teams and unresolved links as coverage gaps rather than inferred papers.", "5. Add a task-specific summary and explicit core/enabling classification."]
    write(ROOT / "BENCHMARKS.md", lines)


if __name__ == "__main__":
    catalog = json.loads((ROOT / "data/catalog.json").read_text())
    benchmarks = json.loads((ROOT / "data/benchmarks.json").read_text())
    reading_routes = json.loads((ROOT / "data/reading_routes.json").read_text())
    paper_map = verify(catalog, benchmarks)
    verify_reading_routes(reading_routes, paper_map)
    build_readme(catalog, reading_routes, paper_map)
    build_topics(catalog, benchmarks)
    build_index(catalog)
    build_benchmarks(benchmarks, paper_map)
    print(f"Generated landing page, {len(TOPICS)} topic pages, index, and benchmark guide for {len(paper_map)} records.")
