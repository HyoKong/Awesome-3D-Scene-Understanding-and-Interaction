#!/usr/bin/env python3
"""Render a linked survey taxonomy from data/roadmap.json.

Requires the existing Matplotlib environment. Produces an editable SVG and a
high-resolution PNG. Publication records come from data/catalog.json; the
roadmap selects representative records without limiting catalog coverage.
Run from the parent workspace with:
  .venv/bin/python articulated-3d-survey/scripts/render_roadmap.py
"""

from functools import lru_cache
from pathlib import Path
import json
import xml.etree.ElementTree as ET

import matplotlib

matplotlib.use("Agg")
matplotlib.rcParams.update({
    "font.family": "DejaVu Sans",
    "svg.fonttype": "none",
    "svg.hashsalt": "articulated-3d-survey-roadmap-v2",
})
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import Circle, FancyBboxPatch
from matplotlib.textpath import TextPath


ROOT = Path(__file__).resolve().parents[1]
WIDTH, MARGIN, GAP = 3000, 58, 20
COL = (WIDTH - 2 * MARGIN - 4 * GAP) / 5
PALETTE = {
    "blue": ("#27669E", "#EDF4FA"),
    "teal": ("#137B7C", "#ECF6F3"),
    "violet": ("#7150A0", "#F3EFF8"),
    "orange": ("#AA542B", "#FBF1E9"),
    "green": ("#557A3B", "#F0F6EB"),
}
INK, MUTED, LINE, PAPER = "#172D40", "#526474", "#D9E2EA", "#FBFCFE"


@lru_cache(maxsize=None)
def measured(value, size, bold=False):
    prop = FontProperties(family="DejaVu Sans", size=size * .72,
                          weight="bold" if bold else "normal")
    return TextPath((0, 0), value, prop=prop).get_extents().width / .72


def wrapped(value, width, size, bold=False):
    lines, line = [], ""
    for word in value.split():
        candidate = f"{line} {word}".strip()
        if line and measured(candidate, size, bold) > width:
            lines.append(line)
            line = word
        else:
            line = candidate
    if line:
        lines.append(line)
    return lines


def validate_data(data):
    catalog = json.loads((ROOT / "data/catalog.json").read_text())
    papers = {p["id"]: p for p in catalog["papers"]}
    assert len(papers) == len(catalog["papers"]), "Duplicate paper IDs"
    assert len(data["topics"]) == 5, "Layout expects five research lanes"
    all_nodes = [s for t in data["topics"] for s in t["subtopics"]] + data["foundations"]
    assert len({s["id"] for s in all_nodes}) == len(all_nodes), "Duplicate subtopic IDs"
    assert len(data["foundations"]) == 4, "Layout expects four shared-resource branches"
    for p in papers.values():
        for key in ["id", "short", "title", "year", "venue", "url", "evidence", "roles"]:
            assert key in p, f"Missing {key}: {p['id']}"
        assert p["url"].startswith("https://"), p["id"]
    for node in all_nodes:
        assert node["label"] and node["strategy"], node["id"]
        assert len(node["paper_ids"]) <= 2, "Keep representative nodes readable"
        for pid in node["paper_ids"]:
            assert pid in papers, f"Unresolved reference {pid}"
    used = {pid for n in all_nodes for pid in n["paper_ids"]}
    return {pid: papers[pid] for pid in sorted(used)}


def node_layout(node, papers, width):
    content_width = width - 46
    blocks = []
    cursor = 31
    for value in wrapped(node["label"], content_width, 25, True):
        blocks.append((cursor, value, "heading", None))
        cursor += 31
    cursor += 5
    for value in wrapped(node["strategy"], content_width, 20):
        blocks.append((cursor, value, "strategy", None))
        cursor += 26
    cursor += 12
    if not node["paper_ids"]:
        blocks.append((cursor, "Strategy branch · references to expand", "pending", None))
        cursor += 24
    for index, pid in enumerate(node["paper_ids"]):
        paper = papers[pid]
        for value in wrapped(paper["short"], content_width - 14, 20, True):
            blocks.append((cursor, value, "paper", pid))
            cursor += 26
        publication = f"{paper['venue']} · {paper['year']}"
        for value in wrapped(publication, content_width - 14, 16.5):
            blocks.append((cursor, value, "venue", pid))
            cursor += 22
        if index < len(node["paper_ids"]) - 1:
            cursor += 9
    return blocks, cursor + 14


def render(data):
    papers = validate_data(data)
    topics = data["topics"]
    node_width = COL - 38
    layouts = {node["id"]: node_layout(node, papers, node_width)
               for topic in topics for node in topic["subtopics"]}
    row_count = max(len(t["subtopics"]) for t in topics)
    row_heights = [max(layouts[t["subtopics"][r]["id"]][1]
                       for t in topics if r < len(t["subtopics"]))
                   for r in range(row_count)]
    row_y = []
    cursor = 398
    for height in row_heights:
        row_y.append(cursor)
        cursor += height + 24
    foundation_y = cursor + 50
    foundation_width = (WIDTH - 2 * MARGIN - 3 * GAP) / 4
    base_layouts = {n["id"]: node_layout(n, papers, foundation_width) for n in data["foundations"]}
    base_height = max(v[1] for v in base_layouts.values())
    height = foundation_y + 73 + base_height + 90
    fig, ax = plt.subplots(figsize=(WIDTH / 100, height / 100), dpi=100)
    fig.patch.set_facecolor(PAPER)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax.set(xlim=(0, WIDTH), ylim=(height, 0), aspect="equal")
    ax.axis("off")
    text_artists, bounded = [], []

    def label(x, y, value, size=20, color=INK, bold=False, align="left", url=None):
        artist = ax.text(x, y, value, fontsize=size * .72, color=color,
                         fontweight="bold" if bold else "normal", ha=align,
                         va="baseline", url=url)
        text_artists.append(artist)
        return artist

    def line(points, color=LINE, width=2):
        xs, ys = zip(*points)
        ax.plot(xs, ys, color=color, lw=width * .72, solid_capstyle="round", zorder=1)

    def panel(x, y, w, h, fill, edge="none", radius=0, dashed=False):
        ax.add_patch(FancyBboxPatch((x, y), w, h,
            boxstyle=f"round,pad=0,rounding_size={radius}", facecolor=fill,
            edgecolor=edge, linewidth=.8, linestyle=(0, (5, 4)) if dashed else "-", zorder=0))

    def node(x, y, w, h, blocks, accent, surface):
        pending = any(kind == "pending" for _, _, kind, _ in blocks)
        panel(x, y, w, h, PAPER if pending else surface,
              edge=accent if pending else "none", dashed=pending)
        if not pending:
            line([(x, y + 18), (x, y + h - 18)], accent, 3)
        current_paper = None
        for offset, value, kind, pid in blocks:
            tx = x + 22 + (14 if kind in {"paper", "venue"} else 0)
            size = {"heading": 24, "strategy": 19, "paper": 20, "venue": 16.5, "pending": 17}[kind]
            color = INK if kind in {"heading", "paper"} else MUTED
            if kind == "paper" and current_paper != pid:
                ax.add_patch(Circle((x + 24, y + offset - 6), 3, facecolor=accent, zorder=3))
                current_paper = pid
            artist = label(tx, y + offset, value, size, color, kind in {"heading", "paper"},
                           url=papers[pid]["url"] if pid else None)
            bounded.append((artist, (x + 8, y + 4, x + w - 10, y + h - 4)))

    # The root and visible branch connectors establish a taxonomy, not a pipeline.
    label(64, 70, data["title"], 48, bold=True)
    label(64, 110, "A map of research questions, strategies, and selected papers", 25, MUTED)
    label(WIDTH - 64, 61, "SELECTED RESEARCH MAP", 17, MUTED, align="right")
    label(WIDTH / 2, 166, "How do we understand and interact with 3D scenes?", 27,
          INK, True, "center")
    line([(WIDTH / 2 - 380, 181), (WIDTH / 2 + 380, 181)], LINE, 1.5)
    centers = [MARGIN + i * (COL + GAP) + COL / 2 for i in range(5)]
    line([(WIDTH / 2, 181), (WIDTH / 2, 265)], MUTED, 2)
    line([(centers[0], 265), (centers[-1], 265)], MUTED, 2)
    for i, topic in enumerate(topics):
        x = MARGIN + i * (COL + GAP)
        accent, surface = PALETTE[topic["color"]]
        line([(centers[i], 265), (centers[i], 300)], accent, 2)
        panel(x, 300, COL, 78, accent)
        label(x + 22, 334, f"{i + 1:02d}  {topic['label']}", 25, "#FFFFFF", True)
        label(x + 22, 360, topic["role"], 16.5, "#FFFFFF")
        spine = x + 11
        line([(centers[i], 378), (centers[i], 386), (spine, 386),
              (spine, row_y[len(topic["subtopics"]) - 1] + 33)], accent, 1.8)
        for row, subtopic in enumerate(topic["subtopics"]):
            y, h = row_y[row], row_heights[row]
            line([(spine, y + 33), (x + 38, y + 33)], accent, 1.8)
            ax.add_patch(Circle((spine, y + 33), 3, facecolor=accent, zorder=3))
            node(x + 38, y, node_width, h, layouts[subtopic["id"]][0], accent, surface)

    # A common foundation spans every task branch; it is not a fifth pipeline step.
    line([(64, foundation_y - 18), (WIDTH - 64, foundation_y - 18)], width=1.5)
    label(64, foundation_y + 22, "SHARED RESOURCES", 25, bold=True)
    label(WIDTH - 64, foundation_y + 20, "Data, simulators, annotations, and task suites", 19, MUTED, align="right")
    for i, entry in enumerate(data["foundations"]):
        x = MARGIN + i * (foundation_width + GAP)
        node(x, foundation_y + 51, foundation_width, base_height,
             base_layouts[entry["id"]][0], MUTED, "#F0F3F7")
    bottom = foundation_y + 51 + base_height
    label(64, bottom + 47, "COMPARE METHODS BY", 16, MUTED, True)
    label(330, bottom + 47, "observations  ·  scene or object scale  ·  representations  ·  actions  ·  evaluation protocol", 19)

    # Validate actual font rendering, not just approximate wrapping.
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    bounds = [(artist, artist.get_window_extent(renderer)) for artist in text_artists]
    for artist, box in bounds:
        if box.x0 < 0 or box.y0 < 0 or box.x1 > WIDTH or box.y1 > height:
            raise ValueError(f"Text outside canvas: {artist.get_text()}")
    for artist, (left, top, right, bottom_y) in bounded:
        box = artist.get_window_extent(renderer)
        pts = ax.transData.inverted().transform([[box.x0, box.y0], [box.x1, box.y1]])
        if pts[0, 0] < left or pts[1, 0] > right or pts[1, 1] < top or pts[0, 1] > bottom_y:
            raise ValueError(f"Text outside branch: {artist.get_text()}")
    for i, (a, first) in enumerate(bounds):
        for b, second in bounds[i + 1:]:
            if first.overlaps(second):
                raise ValueError(f"Overlapping labels: {a.get_text()} / {b.get_text()}")
    target = ROOT / "assets"
    target.mkdir(exist_ok=True)
    svg_path = target / "survey-roadmap.svg"
    fig.savefig(svg_path, format="svg", metadata={"Date": None,
        "Title": "3D Scene Understanding and Interaction: research roadmap",
        "Description": data["description"], "Creator": "Awesome 3D Scene Understanding and Interaction"})
    svg = svg_path.read_text()
    svg = svg.replace("<defs>", "<desc>Five research lanes branch into subtopics, strategies, and linked representative papers: scene perception, articulated geometry, generation and authoring, manipulation, and embodied agents and evaluation. Shared resources cover real scenes, articulated assets and physics, functional supervision, and robot-task benchmarks.</desc>\n<defs>", 1)
    svg_path.write_text(svg)
    fig.savefig(target / "survey-roadmap.png", dpi=200)
    plt.close(fig)
    tree = ET.parse(svg_path)
    ns = {"s": "http://www.w3.org/2000/svg"}
    assert tree.find("s:title", ns) is not None
    anchors = tree.findall(".//s:a", ns)
    links = {a.attrib.get("{http://www.w3.org/1999/xlink}href") for a in anchors}
    assert {p["url"] for p in papers.values()} <= links, "Missing SVG paper hyperlinks"
    print(f"Validated {len(text_artists)} labels, {len(papers)} records and SVG links.")
    print(f"Saved {WIDTH} × {int(height)} SVG; {2 * WIDTH} × {int(2 * height)} PNG.")


if __name__ == "__main__":
    data = json.loads((ROOT / "data/roadmap.json").read_text())
    render(data)
