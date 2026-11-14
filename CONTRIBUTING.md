# Contributing

[Back to the survey](README.md)

We welcome missing papers, official code releases, corrected metadata, benchmark connections, and better classifications. The scope includes scene perception and reconstruction, scene generation, embodied reasoning and navigation, robotic manipulation, and articulated objects.

## Add or correct a paper

Edit `data/catalog.json`; do not edit generated paper tables directly. An entry needs:

| Field | Meaning |
| --- | --- |
| `id`, `short`, `title` | Stable unique ID, readable short name, full canonical title |
| `year`, `venue`, `url` | Publication year, venue or explicit preprint status, primary paper page |
| `category`, `section`, `subtopic` | Broad research area, browsing group, specific research question |
| `additional_topics` (optional) | Other topic pages where this paper belongs, mapped to a section name, e.g. `{"datasets": "Functional indoor scenes and annotations"}` |
| `dataset_summary` (optional) | Dataset, simulator, or benchmark contribution to describe on the datasets page when the main summary focuses on a method |
| `scope` | `core` for methods directly studying scene understanding, reconstruction, generation, or embodied interaction; `enabling` for reusable backbones, general policy foundations, datasets, and infrastructure |
| `evidence` | Brief original description of the contribution; avoid unqualified SOTA claims |
| `project_url`, `code_url` | Official links, or `null` when not located |
| `code_status` | `released`, `placeholder`, or `not-located`; an announcement is not a release |
| `link_sources`, `last_verified` | Primary sources establishing the links and the date checked |

Use `link_notes` for partial implementations, paper/code differences, or redirects. Set `code_kind` to `dataset-toolkit` for dataset/evaluation utilities. A weights download is not implementation code. Keep an arXiv preprint and its published version in one record unless they are materially different works.

A paper can appear on multiple topic pages while keeping one record in the full index. If it introduces a dataset, benchmark, simulator, or reusable environment generator, include it on the datasets page using its primary category or `additional_topics`. The datasets page also includes every resource registered in `data/benchmarks.json`.

When proposing an addition through an issue, a short submission is enough:

```text
Paper title / year / venue:
Primary paper URL:
Official project URL:
Official code URL and release status:
Research area and why it belongs:
Benchmark or task, with source if applicable:
```

## Connect a benchmark

Edit `data/benchmarks.json`. Record the task, version, split, inputs, metric, and official source before comparing scores. Resolve a submission name to its original paper; keep unresolved team names in `unresolved_entries`. A benchmark association does not imply a submitted result or rank. Preserve the distinction between semantic segmentation, instance segmentation, motion estimation, grounding, and robot task success.

For motion estimation, see the [Articulate3D challenge](https://insait-institute.github.io/articulate3d.github.io/challenge.html). Keep its evaluation protocol distinct from SceneFun3D's segmentation and grounding tasks.

## Improve a reading route

Edit `data/reading_routes.json` to add a learning path or refine its stages. Each stage names a reading goal, existing catalog paper IDs, and a short explanation of what to look for. Keep routes focused on a question, and finish with a small comparison or exercise. The README displays every route in full and automatically includes it in the contents below the teaser.

Each step also needs `chapter_sections`: one or two references such as `{"chapter": "perception", "section": 3}`, with a one-based section number. Put the section that explains the method first; use a second link for useful background. Check the actual chapter text before linking, and update it if the route introduces a method the chapter does not yet cover. The website uses these references for direct reading links and previous/next-step navigation. Write the Chinese route descriptions for Chinese readers rather than translating English phrasing word for word; preserve the learning objectives and step order.

## Regenerate and review

From this directory:

```bash
python scripts/build_catalog.py
python scripts/validate_catalog.py
```

Review the generated README, topic pages, complete index, and benchmark guide. Open changed links and check paper identity against the primary source. If changing the detailed figure, edit `data/roadmap.json` and run `scripts/render_roadmap.py` in an environment with Matplotlib. The teaser has its own renderer, `scripts/render_teaser.py`. Inspect rendered figures for legibility as well as programmatic bounds checks.

Existing surveys and awesome lists can reveal candidates. Verify those candidates against primary sources and write independent summaries. Reused figures or text require their source's attribution and license terms.

## Update the website

The website uses the same catalog, reading routes, and benchmark records as the README. The survey chapters live in `site/articles/` and generate both the continuous survey and individual chapter pages. Cite canonical paper IDs inline with `[cite:paper-id]`. Sections can include a comparison table (`caption`, `columns`, `rows`) and a short callout (`title`, `text`). Keep claims grounded in primary papers, distinguish proposed research directions from reported results, and compare methods under stated assumptions.

The homepage introduces the reading routes; `survey.html` contains the full survey. English and Chinese share the same templates. Chinese chapters live in `site/zh/articles/`, interface labels in `site/locales/zh.json`, and translated catalog, route, and benchmark descriptions in `site/zh/`. Keep canonical IDs, paper titles, resource links, section order, and citation order consistent between languages. When adding a record, include its Chinese description under the same ID; suggestions through issues can be in either language. Write Chinese explanations independently, using concrete tasks and method details rather than translating English phrasing sentence by sentence. Keep familiar technical terms such as `Gaussian primitives` and `instance mask` in English, with spaces between English and Chinese text. Avoid em dashes in authored English and Chinese prose; use a period, comma, colon, or a clearer sentence instead.

Figures and videos are declared individually in `site/media.json`, with their target chapter and section, original paper, caption, source, credit, and license information. Keep copied assets under `assets/paper-media/`, add each file to the explicit `.gitignore` allowlist, and document attribution in `assets/ATTRIBUTION.md`. Stream official videos from their source; YouTube videos load only after a reader chooses to play. The builder copies only media explicitly named in the manifest.

Each media entry includes a `zh` object translating its title, caption, credit, and license label. Explain what readers should notice in the visual, and distinguish a project's overview figure from a frame of its video when using it as a preview.

To preview the site:

```bash
python scripts/build_site.py
python scripts/validate_site.py
python -m http.server 8000 --directory _site
```

Open `http://localhost:8000` in your browser. The build needs only Python's standard library. Editing the templates, styles, or JavaScript in `site/` changes the presentation.

GitHub Actions builds and deploys the website when its inputs change on `main`. Only the explicitly allowed output files in `_site/` enter the Pages artifact. Research notes and design drafts remain outside the public repository and deployment.
