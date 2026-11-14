# Survey scope and research roadmap

[Overview](README.md) · [Topic collections](PAPERS.md#topic-directory) · [Benchmarks](BENCHMARKS.md)

The survey studies **how to perceive, reconstruct, generate, and interact with 3D scenes**. It covers whole-scene geometry and appearance, scene layouts and generated environments, spatial reasoning and navigation, and robotic manipulation. Articulation and affordances connect this broader scene view to objects and parts that agents can use.

The [front-page teaser](assets/survey-teaser.png) presents that scope through four numbered scene callouts, with an [editable vector version](assets/survey-teaser.svg). The [detailed topic map](assets/survey-roadmap.svg) names strategies and representative papers. The complete [catalog](PAPERS.md) grows independently of both figures.

## Research areas

| Area | Questions | Subtopics |
| --- | --- | --- |
| Scene and functional perception | What is present, what belongs together, and what can be used? | 3D backbones; semantic/instance segmentation; open-vocabulary representations; scene graphs and language grounding; actionable parts; affordances; joint parameters; articulated pose and state |
| Scene reconstruction and digital twins | How can observations recover scene geometry, appearance, motion, and structure? | Structure from motion and multi-view reconstruction; RGB-D fusion; neural fields and 3D Gaussians; feed-forward reconstruction; SLAM and dynamic mapping; articulated digital twins |
| Scene generation and asset authoring | How can models generate coherent layouts, visual scenes, and interactive environments? | Scene graphs and layouts; text/image-conditioned scene synthesis; procedural worlds; simulation environments; articulated assets and programmatic authoring |
| Embodied agents and robotic interaction | How do agents reason, navigate, plan, and act in a 3D environment? | Spatial maps and memory; object-goal and language-guided navigation; embodied question answering; task planning; generalist policies; affordances, contact, and manipulation |
| Data and evaluation | Which capabilities do the available protocols actually measure? | Scene datasets; functional annotations; articulated assets; simulators; challenge tracks; generalization and robot task success |

The map describes related research problems, not a mandatory pipeline. Some systems reconstruct an explicit model; others act from observations or use interaction to improve their representation.

## Inclusion policy

**Core:** work directly studying 3D scene understanding, scene reconstruction, scene generation, or embodied interaction. This includes static scenes, dynamic scenes, and articulated objects, as well as spatial reasoning, navigation, and manipulation.

**Enabling:** reusable point/image backbones, general policy foundations, datasets, simulators, and evaluation infrastructure. The labels describe a paper's role in the survey; scene-level research does not need an articulation result to belong.

Include agents whose perception, memory, reasoning, navigation, or actions concern a physical or simulated 3D environment. Include human-object interaction when it informs scene dynamics or interaction. Generic text-only agents and image/video generation without a concrete scene, spatial, or robotics connection are outside the present catalog.

## Benchmark-led discovery

Start from the exact task, version, and evaluation split. Follow named submissions to primary publications and official resources, and deduplicate conference/preprint records. Keep unresolved team names visible in the benchmark guide. Associations describe relevance unless a particular evaluated submission is explicitly documented.

For scene-level motion estimation, see the [Articulate3D challenge](https://insait-institute.github.io/articulate3d.github.io/challenge.html). Its evaluation and SceneFun3D's segmentation and grounding tasks require their respective dataset, input, and scoring definitions.

A broad collection can include methods from many benchmarks without presenting an invalid combined leaderboard. Protocol-aware comparison tables will be added only when the necessary evidence is recorded.

## Comparison dimensions for the report

The current catalog captures publication identity, research area, original contribution summaries, official resource links, release status, and provenance. These additional dimensions need systematic paper-level annotation before we make cross-method claims:

| Dimension | What to record |
| --- | --- |
| Input | RGB, RGB-D, point cloud, mesh, multi-view, video, language, interaction, tactile signals |
| Observation setting | One or multiple states; passive or active observation; known or unseen category/instance |
| Scale | Part, object, assembly, tabletop, room, multi-room environment |
| Output | Segmentation, features, scene graphs, camera poses, surfaces, radiance fields, 3D Gaussians, layouts, kinematics, programs, trajectories, policies |
| Supervision and priors | Labels, demonstrations, pretrained models, templates, retrieval, simulator access |
| Evaluation | Dataset version, split, embodiment, metrics, real/simulated setting, generalization protocol |
| Reproducibility | Released implementation scope, data, models, evaluator, license, date checked |

## Questions the survey should answer

1. Which scene representations preserve geometry, appearance, semantics, and the details needed for spatial reasoning and interaction?
2. When do part, affordance, and joint estimates improve action over direct visuomotor policies?
3. How do clutter, occlusion, tiny handles, nested mechanisms, and uncertain object states affect generalization?
4. How do visual scene quality, geometric consistency, layout plausibility, and physical interactivity differ as reconstruction and generation objectives?
5. Which evaluation protocols expose the gap between geometric accuracy and successful interaction?
6. How should action, tactile contact, and language update a scene or object model?
7. How do local object skills compose into mobile, bimanual, and long-horizon household tasks?
8. How do scene memory and uncertainty affect navigation, embodied question answering, and long-horizon planning?

These are questions to test against the literature, not conclusions established by the current paper list.

## From a collection to a survey report

| Stage | Current outcome or next evidence needed |
| --- | --- |
| Scope and navigation | Teaser, detailed map, reading routes, and topic pages exist; refine wording as coverage grows |
| Bibliographic coverage | Expanded from the initial seed using primary sources, related collections, and benchmark entries; unresolved candidates remain explicit |
| Comparable records | Next: annotate the comparison dimensions above, with sources for each claim |
| Topic synthesis | Next: explain method families, assumptions, and limitations beyond individual summaries |
| Cross-topic analysis | Next: connect representations and reconstruction/generation outputs to downstream task evidence |
| Report writing | Begin once the comparisons support a distinct synthesis, figures, and an evidence-backed research agenda |

A larger count helps discovery; the report becomes worthwhile when it explains connections and tradeoffs that readers cannot obtain from titles alone.

## Maintaining the repository

[data/catalog.json](data/catalog.json) is the publication source of truth. [data/benchmarks.json](data/benchmarks.json) records task protocols and unresolved submission identities. [data/roadmap.json](data/roadmap.json) selects representative catalog IDs for the detailed map.

Run `python scripts/build_catalog.py` to regenerate the README, topic pages, paper index, and benchmark guide. Figure renderers produce editable SVGs and PNGs using Matplotlib. The [contribution guide](CONTRIBUTING.md) explains the record contract.
