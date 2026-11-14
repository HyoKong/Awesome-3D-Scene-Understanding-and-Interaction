#!/usr/bin/env python3
"""Render the editable RoboCasa teaser used by the GitHub README.

The four annotations match the public survey website. They are explanatory
marks on an official RoboCasa frame, not model predictions or robot rollouts.
"""

from pathlib import Path
import xml.etree.ElementTree as ET

import matplotlib

matplotlib.use("Agg")
matplotlib.rcParams.update({
    "font.family": "DejaVu Sans",
    "svg.fonttype": "none",
    "svg.hashsalt": "3d-scene-survey-teaser",
})
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.colors import to_rgba
from matplotlib.patches import Circle, FancyArrowPatch, Polygon, Rectangle


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
IMAGE = ASSETS / "teaser-source" / "robocasa-kitchen-robot.png"
W, H = 1920, 1200
PAPER, INK, MUTED, PANEL = "#f8f5ee", "#17252d", "#64737a", "#0b1821"
AREAS = {
    "perception": ("#16718b", "#8bd8e8", "Scene perception", "Recognize objects, parts, and motion", "perception.html"),
    "reconstruction": ("#7955b5", "#cfb7ff", "Scene reconstruction", "Reconstruct 3D scenes from images and scans", "reconstruction.html"),
    "generation": ("#a15a14", "#f4cb8c", "Scene generation", "Create layouts and environments", "generation.html"),
    "robotics": ("#197758", "#9bddbd", "Robots & embodied agents", "Navigate, plan, and manipulate", "robotics.html"),
}
BASE = "https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/"
TEXT = []

fig, ax = plt.subplots(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(PAPER)
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.set(xlim=(0, W), ylim=(H, 0), aspect="equal")
ax.axis("off")


def text(x, y, value, size=18, color=INK, bold=False, align="left", **kwargs):
    artist = ax.text(x, y, value, fontsize=size * .72, color=color,
                     fontweight="bold" if bold else "normal", ha=align,
                     va=kwargs.pop("va", "baseline"), **kwargs)
    TEXT.append(artist)
    return artist


def outline(points, color, dashed=False, filled=False, closed=True):
    patch = Polygon(points, closed=closed,
                    facecolor=to_rgba(color, .12) if filled else "none",
                    edgecolor=color,
                    linewidth=2.1, linestyle=(0, (5, 4)) if dashed else "-",
                    joinstyle="round", zorder=4)
    if not filled:
        patch.set_path_effects([pe.Stroke(linewidth=4, foreground="#ffffff", alpha=.8), pe.Normal()])
    ax.add_patch(patch)
    return patch


def arrow(points, color):
    path = FancyArrowPatch(points[0], points[-1], connectionstyle="arc3,rad=.12",
                           arrowstyle="-|>", mutation_scale=18, color=color,
                           linewidth=2.4, zorder=5)
    path.set_path_effects([pe.Stroke(linewidth=5, foreground="#ffffff", alpha=.8), pe.Normal()])
    ax.add_patch(path)


def leader(points, color):
    """Draw a discreet connector from a glass label to its scene marker."""
    xs, ys = zip(*points)
    (line,) = ax.plot(xs, ys, color=color, linewidth=2.2, zorder=5)
    line.set_path_effects([pe.Stroke(linewidth=4.5, foreground="#ffffff", alpha=.72), pe.Normal()])


def pin(x, y, number, color):
    ax.add_patch(Circle((x, y), 17, facecolor=color, edgecolor="#ffffff", linewidth=1.8, zorder=8))
    text(x, y, str(number), 17, "#ffffff", True, align="center", va="center", zorder=9)


def callout(x, y, width, key, number):
    color, tint, title, detail, destination = AREAS[key]
    panel = Rectangle((x, y), width, 104, facecolor=PANEL, edgecolor="#ffffff55",
                      linewidth=1, alpha=.78, zorder=6)
    panel.set_url(BASE + destination)
    ax.add_patch(panel)
    title_artist = text(x + 45, y + 42, title, 30, "#ffffff", True, zorder=9)
    detail_artist = text(x + 45, y + 78, detail, 21, "#edf4f5", zorder=9)
    key_artist = text(x + 18, y + 42, str(number), 22, tint, True, zorder=9)
    for artist in (title_artist, detail_artist, key_artist):
        artist.set_url(BASE + destination)


text(60, 58, "3D Scene Understanding & Interaction", 36, INK, True)
text(1860, 58, "open survey", 16, MUTED, align="right")
ax.plot([60, 1860], [82, 82], color="#cbd1cf", lw=1)

# The photo stays at 16:9. Coordinates below are scaled from its 1920 × 1080
# source so the semantic markers agree with the website teaser.
photo_x, photo_y, photo_w = 60, 130, 1800
photo_h = photo_w * 9 / 16
image = mpimg.imread(IMAGE)
ax.imshow(image, extent=(photo_x, photo_x + photo_w, photo_y + photo_h, photo_y), zorder=2)
ax.add_patch(Rectangle((photo_x, photo_y), photo_w, photo_h, fill=False,
                       edgecolor="#ccd4d5", linewidth=1, zorder=3))


def p(x, y):
    return photo_x + photo_w * x / 1920, photo_y + photo_h * y / 1080


perception, _, *_ = AREAS["perception"]
reconstruction, _, *_ = AREAS["reconstruction"]
generation, _, *_ = AREAS["generation"]
robotics, _, *_ = AREAS["robotics"]

# 1: cabinet and parts. 2: inferred surfaces. 3: room layout. 4: reach path.
outline([p(148, 76), p(445, 98), p(448, 347), p(151, 360)], perception, filled=True)
outline([p(148, 76), p(445, 98), p(448, 347), p(151, 360)], perception)

wire_front = [p(1155, 470), p(1593, 510), p(1593, 770), p(1155, 700)]
wire_back = [p(1190, 435), p(1612, 475), p(1612, 729)]
outline(wire_front, reconstruction)
outline(wire_back, reconstruction, dashed=True, closed=False)
for first, second in [(wire_front[0], wire_back[0]), (wire_front[1], wire_back[1]), (wire_front[2], wire_back[2])]:
    outline([first, second], reconstruction, dashed=True, closed=False)
for first, second in [(p(1301, 483), p(1301, 723)), (p(1447, 497), p(1447, 747)), (p(1155, 585), p(1593, 638))]:
    outline([first, second], reconstruction, dashed=True, closed=False)

outline([p(136, 820), p(700, 700), p(1490, 800), p(1100, 1010)], generation, dashed=True, filled=True)
arrow([p(875, 560), p(637, 582)], robotics)

# Connect each label edge to its corresponding scene marker.
leader([(p(360, 0)[0], photo_y + 138), p(360, 290)], perception)
leader([(p(1410, 0)[0], photo_y + 138), p(1410, 490)], reconstruction)
leader([p(400, 1000), p(400, 900), p(440, 830)], generation)
leader([p(1420, 1000), p(1420, 900), p(1120, 840), p(875, 560)], robotics)

pin(*p(360, 290), 1, perception)
pin(*p(1410, 490), 2, reconstruction)
pin(*p(440, 830), 3, generation)
pin(*p(875, 560), 4, robotics)

callout(photo_x + 34, photo_y + 34, 660, "perception", 1)
callout(photo_x + photo_w - 694, photo_y + 34, 660, "reconstruction", 2)
callout(photo_x + 34, photo_y + photo_h - 138, 660, "generation", 3)
callout(photo_x + photo_w - 694, photo_y + photo_h - 138, 660, "robotics", 4)

text(60, 1178, "RoboCasa simulation frame · four survey modules illustrated in one scene", 17, INK, True)
credit = text(1860, 1178, "RoboCasa, Nasiriany et al. · CC BY 4.0 · annotations schematic", 15, MUTED, align="right")
credit.set_url("https://robocasa.ai/")


def validate():
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    for artist in TEXT:
        box = artist.get_window_extent(renderer)
        if box.x0 < 0 or box.y0 < 0 or box.x1 > W or box.y1 > H:
            raise ValueError(f"Text outside canvas: {artist.get_text()}")


if __name__ == "__main__":
    validate()
    svg = ASSETS / "survey-teaser.svg"
    png = ASSETS / "survey-teaser.png"
    fig.savefig(svg, format="svg", metadata={
        "Date": None,
        "Title": "3D Scene Understanding and Interaction",
        "Description": "An official RoboCasa kitchen frame annotated with the four survey modules: scene perception, scene reconstruction, scene generation, and robots and embodied agents. The annotations are schematic research examples, not model predictions or recorded robot actions.",
        "Creator": "Awesome 3D Scene Understanding and Interaction",
    })
    value = svg.read_text()
    value = value.replace("<defs>", "<title>3D Scene Understanding and Interaction</title>\n<desc>An official RoboCasa kitchen frame annotated with four survey modules. A cabinet outline represents scene perception, a wireframe represents scene reconstruction, a room-layout outline represents scene generation, and a reach arrow represents robots and embodied agents. The annotations are schematic research examples, not model predictions or recorded robot actions.</desc>\n<defs>", 1)
    value = "\n".join(line.rstrip() for line in value.splitlines()) + "\n"
    svg.write_text(value)
    fig.savefig(png, dpi=200)
    tree = ET.parse(svg)
    namespace = {"s": "http://www.w3.org/2000/svg"}
    assert tree.find("s:title", namespace) is not None and tree.find("s:desc", namespace) is not None
    print(f"Validated {len(TEXT)} labels; wrote {svg} and {png}.")
