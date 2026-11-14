#!/usr/bin/env python3
"""Render the README research map as editable SVG and high-resolution PNG.

The left visual is an official RoboCasa simulator frame with vector annotations
that connect scene elements to the four research areas on the right.
"""

from pathlib import Path
import json
import xml.etree.ElementTree as ET

import matplotlib

matplotlib.use("Agg")
matplotlib.rcParams.update({"font.family": "DejaVu Sans", "svg.fonttype": "none", "svg.hashsalt": "articulated-survey-teaser"})
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.font_manager import FontProperties
from matplotlib.patches import Circle, FancyArrowPatch, Polygon, Rectangle
from matplotlib.textpath import TextPath


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
IMAGE = ASSETS / "teaser-source" / "robocasa-kitchen-robot.png"
W, H = 1920, 850
INK, MUTED, PALE, PAPER = "#17252D", "#65737A", "#D7DFE1", "#FFFFFF"
PERCEPTION, FUNCTION, MODEL, ACTION = "#286A99", "#208373", "#7961A0", "#B96430"
TEXT = []

fig, ax = plt.subplots(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(PAPER)
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.set(xlim=(0, W), ylim=(H, 0), aspect="equal")
ax.axis("off")


def text(x, y, value, size=18, color=INK, bold=False, align="left", **kwargs):
    vertical_align = kwargs.pop("va", "baseline")
    artist = ax.text(x, y, value, fontsize=size * .72, color=color,
                     fontweight="bold" if bold else "normal", ha=align,
                     va=vertical_align, **kwargs)
    TEXT.append(artist)
    return artist


def line(points, color=PALE, thickness=1.2, style="-", z=1):
    xs, ys = zip(*points)
    ax.plot(xs, ys, color=color, lw=thickness * .72, linestyle=style,
            solid_capstyle="round", solid_joinstyle="round", zorder=z)


def width(value, size, bold=False):
    prop = FontProperties(family="DejaVu Sans", size=size * .72,
                          weight="bold" if bold else "normal")
    return TextPath((0, 0), value, prop=prop).get_extents().width / .72


with (ROOT / "data" / "catalog.json").open() as handle:
    CATALOG = json.load(handle)
PAPER_URLS = {item["short"]: item["url"] for item in CATALOG["papers"]}


def paper_links(x, y, names, size=14):
    """Emit compact paper labels whose primary names point to catalog records."""
    cursor = x
    for index, name in enumerate(names):
        artist = text(cursor, y, name, size, MUTED, url=PAPER_URLS[name])
        cursor += width(name, size) + 10
        if index < len(names) - 1:
            text(cursor, y, "·", size, MUTED)
            cursor += width("·", size) + 10


def badge(x, y, number, accent, radius=16):
    ax.add_patch(Circle((x, y), radius, facecolor=accent, edgecolor=PAPER,
                        linewidth=1.2, zorder=8))
    text(x, y, str(number), 19, PAPER, True, align="center",
         va="center", zorder=9)


def band(y, number, label, subtopics, papers, accent):
    """A ruled branch of the taxonomy: one question, compact evidence, no card."""
    x0, x1 = 1070, 1855
    line([(x0, y), (x1, y)], accent, 1.6)
    badge(x0 + 16, y + 23, number, accent)
    text(x0 + 45, y + 32, label, 27, INK, True)
    for i, value in enumerate(subtopics):
        text(x0, y + 62 + i * 26, value, 21, MUTED)
    paper_links(x0, y + 118, papers, 20)


def scene_stroke(points, accent, dashed=False, fill=False):
    artist = Polygon(points, closed=fill, facecolor=accent if fill else "none",
                     edgecolor=accent, alpha=.12 if fill else 1,
                     linewidth=2, linestyle=(0, (4, 3)) if dashed else "-",
                     joinstyle="round", zorder=4)
    if not fill:
        artist.set_path_effects([pe.Stroke(linewidth=4, foreground="white", alpha=.9), pe.Normal()])
    ax.add_patch(artist)


def callout(x, y, w, number, label, question, accent, leader):
    """Label an actual scene element, with the same key as its taxonomy branch."""
    scene_stroke(leader, accent)
    ax.add_patch(Circle(leader[-1], 4.2, facecolor=accent, edgecolor=PAPER,
                        linewidth=1.2, zorder=5))
    ax.add_patch(Rectangle((x, y), w, 69, facecolor=PAPER, edgecolor="none",
                           alpha=.96, zorder=6))
    badge(x + 23, y + 23, number, accent, radius=15)
    text(x + 47, y + 29, label, 20, accent, True, zorder=9)
    text(x + 15, y + 55, question, 18, INK, zorder=9)


# Restrained figure header; the study title is information rather than branding.
text(62, 53, "From scene perception to robotic interaction", 34, INK, True)
text(1856, 52, "survey map", 15, MUTED, align="right")
line([(62, 74), (1856, 74)], PALE, 1.2)

# The source remains at its natural 16:9 ratio. All illustrative annotations are
# separate vector elements; they do not depict predictions from the cited papers.
photo_x, photo_y, photo_w = 62, 120, 953
photo_h = photo_w * 9 / 16
image = mpimg.imread(IMAGE)
ax.imshow(image, extent=(photo_x, photo_x + photo_w, photo_y + photo_h, photo_y), zorder=2)
line([(photo_x, photo_y), (photo_x + photo_w, photo_y),
      (photo_x + photo_w, photo_y + photo_h), (photo_x, photo_y + photo_h),
      (photo_x, photo_y)], PALE, 1, z=3)
# 1. A cabinet region illustrates scene-level object identification.
cabinet = [(138, 151), (285, 161), (287, 289), (139, 292), (138, 151)]
scene_stroke(cabinet, PERCEPTION, fill=True)
scene_stroke(cabinet, PERCEPTION)

# 2. A cabinet hinge and opening arc illustrate movable parts and their motion.
scene_stroke([(310, 376), (310, 482)], FUNCTION, dashed=True)
hinge_arc = FancyArrowPatch((318, 454), (370, 470), connectionstyle="arc3,rad=-.42",
                            arrowstyle="-|>", mutation_scale=17, color=FUNCTION,
                            linewidth=2, zorder=5)
hinge_arc.set_path_effects([pe.Stroke(linewidth=4, foreground=PAPER), pe.Normal()])
ax.add_patch(hinge_arc)

# 3. A schematic wireframe indicates an articulated asset / digital twin.
front = [(574, 230), (652, 232), (652, 287), (574, 284), (574, 230)]
back = [(587, 218), (665, 220), (665, 275)]
scene_stroke(front, MODEL)
scene_stroke(back, MODEL, dashed=True)
for first, second in [(front[0], back[0]), (front[1], back[1]), (front[2], back[2])]:
    scene_stroke([first, second], MODEL, dashed=True)

# 4. An illustrative reach trajectory connects the robot to a cabinet handle.
reach = FancyArrowPatch((500, 399), (366, 416), connectionstyle="arc3,rad=.25",
                        arrowstyle="-|>", mutation_scale=19, color=ACTION,
                        linewidth=2.6, zorder=5)
reach.set_path_effects([pe.Stroke(linewidth=5, foreground=PAPER), pe.Normal()])
ax.add_patch(reach)

callout(80, 136, 315, 1, "Scene perception", "Identify objects and scene layout", PERCEPTION,
        [(235, 205), (235, 236)])
callout(595, 136, 402, 3, "Reconstruction & generation", "Reconstruct scenes and generate assets", MODEL,
        [(791, 205), (791, 220), (665, 253)])
callout(80, 570, 390, 2, "Functional understanding", "Find movable parts, joints and state", FUNCTION,
        [(270, 570), (270, 513), (310, 443)])
callout(597, 570, 400, 4, "Manipulation & agents", "Plan actions and interact with objects", ACTION,
        [(668, 570), (610, 508), (500, 399)])

text(photo_x, 692, "RoboCasa simulation · four research areas illustrated in one scene", 19, INK, True)
text(photo_x, 722, "Image: RoboCasa, Nasiriany et al. · CC BY 4.0 · annotations added", 17, MUTED,
     url="https://robocasa.ai/")

# The research areas are a taxonomy, deliberately not connected by cross-panel arrows.
text(1070, 116, "Research areas", 18, MUTED, True)
text(1855, 116, "representative papers", 17, MUTED, align="right")
band(140, 1, "Scene perception", ["3D backbones · semantic / instance segmentation", "Open-vocabulary representations · grounding"],
     ["PTv3", "Volt", "Open3DIS"], PERCEPTION)
band(282, 2, "Functional understanding", ["Actionable parts · affordances", "Joint parameters · articulated pose and state"],
     ["SceneFun3D", "GAPartNet", "Articulate3D"], FUNCTION)
band(424, 3, "Reconstruction & generation", ["Scene geometry · neural fields · 3D Gaussians", "Scene layouts · procedural worlds · digital twins"],
     ["3D Gaussian Splatting", "DUSt3R", "Holodeck"], MODEL)
band(566, 4, "Manipulation & agents", ["Navigation · task planning · embodied reasoning", "Affordances · manipulation · generalist policies"],
     ["Where2Act", "VLMaps", "LEO"], ACTION)

# A narrow shared rail grounds the taxonomy without imposing a fifth research stage.
rail_y = 775
line([(62, rail_y), (1856, rail_y)], INK, 1.2)
text(62, rail_y + 31, "Data & evaluation", 18, INK, True)
text(300, rail_y + 31, "ScanNet++ · MultiScan", 18, MUTED)
text(640, rail_y + 31, "SceneFun3D · Articulate3D", 18, MUTED)
text(1040, rail_y + 31, "PartNet-Mobility", 18, MUTED)
text(1300, rail_y + 31, "ManiSkill · RLBench · BEHAVIOR-1K", 18, MUTED)
line([(62, rail_y + 51), (1856, rail_y + 51)], PALE, .9)

def validate():
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    boxes = [(artist, artist.get_window_extent(renderer)) for artist in TEXT]
    for artist, box in boxes:
        if box.x0 < 0 or box.y0 < 0 or box.x1 > W or box.y1 > H:
            raise ValueError(f"Text outside canvas: {artist.get_text()}")
    for i, (one, first) in enumerate(boxes):
        for two, second in boxes[i + 1:]:
            if first.overlaps(second) and abs(first.y0 - second.y0) < 9:
                raise ValueError(f"Overlapping labels: {one.get_text()} / {two.get_text()}")


if __name__ == "__main__":
    validate()
    svg = ASSETS / "survey-teaser.svg"
    fig.savefig(svg, format="svg", metadata={
        "Date": None,
        "Title": "From scene perception to robotic interaction",
        "Description": "A RoboCasa simulation frame with four numbered illustrative callouts matched to the literature branches: perception, functional understanding, reconstruction and generation, and manipulation and agents.",
        "Creator": "Awesome 3D Scene Understanding and Interaction",
    })
    value = svg.read_text()
    value = value.replace("<defs>", "<title>From scene perception to robotic interaction</title>\n<desc>A survey map of articulated 3D research. Left: official RoboCasa simulator frame with illustrative vector annotations. Callout 1 identifies scene objects; 2 marks a cabinet hinge and opening motion; 3 outlines a microwave model; 4 shows a robot reach. Matching numbers and colors connect these examples to the four research areas and representative papers on the right. Annotations illustrate research questions and are not measured predictions or robot trajectories.</desc>\n<defs>", 1)
    svg.write_text(value)
    fig.savefig(ASSETS / "survey-teaser.png", dpi=200)
    tree = ET.parse(svg)
    namespace = {"s": "http://www.w3.org/2000/svg"}
    assert tree.find("s:title", namespace) is not None and tree.find("s:desc", namespace) is not None
    print(f"Validated {len(TEXT)} labels; wrote {svg} and {ASSETS / 'survey-teaser.png'}.")
