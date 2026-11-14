# Scene generation and asset authoring

> Generating scene layouts, 3D environments, procedural worlds, and interactive assets.

[← Overview](../README.md) · [Full paper index](../PAPERS.md) · [Benchmarks](../BENCHMARKS.md) · [Contribute](../CONTRIBUTING.md)

Papers are grouped by editorial section and ordered newest first within each section. Classification expresses relevance, not a rank.

[Indoor layouts and scene graphs](#section-1) · [Text and image-conditioned scene synthesis](#section-2) · [Procedural scene and world generation](#section-3) · [Simulation environments and embodied training](#section-4) · [Generative part structure and motion](#section-5) · [Language and vision-guided asset authoring](#section-6) · [Surveys and perspectives](#section-7)

<a id="section-1"></a>

## Indoor layouts and scene graphs

| Paper | Focus | Official resources |
| --- | --- | --- |
| [DiffuScene: Denoising Diffusion Models for Generative Indoor Scene Synthesis](https://openaccess.thecvf.com/content/CVPR2024/html/Tang_DiffuScene_Denoising_Diffusion_Models_for_Generative_Indoor_Scene_Synthesis_CVPR_2024_paper.html)<br>CVPR 2024 · core | Uses a diffusion model over indoor scene configurations containing semantic classes, object geometry, and placements. | Project: — · [Code](https://github.com/tangjiapeng/DiffuScene) · [Details](../PAPERS.md#diffuscene) |
| [InstructScene: Instruction-Driven 3D Indoor Scene Synthesis with Semantic Graph Prior](https://arxiv.org/abs/2402.04717)<br>ICLR 2024 · core | Combines a semantic graph prior with a layout decoder to synthesize indoor scenes from instructions. | [Project](https://chenguolin.github.io/projects/InstructScene/) · [Code](https://github.com/chenguolin/InstructScene) · [Details](../PAPERS.md#instructscene) |
| [LayoutGPT: Compositional Visual Planning and Generation with Large Language Models](https://arxiv.org/abs/2305.15393)<br>NeurIPS 2023 · core | Uses in-context LLM prompting to translate text conditions into layouts, including 3D indoor scene layouts. | [Project](https://layoutgpt.github.io/) · [Code](https://github.com/UCSB-AI/LayoutGPT) · [Details](../PAPERS.md#layoutgpt) |
| [ATISS: Autoregressive Transformers for Indoor Scene Synthesis](https://arxiv.org/abs/2110.03675)<br>NeurIPS 2021 · core | Generates indoor object layouts from a room type and floor plan, while supporting completion and object-placement constraints. | [Project](https://research.nvidia.com/labs/toronto-ai/ATISS/) · [Code](https://github.com/nv-tlabs/ATISS) · [Details](../PAPERS.md#atiss) |
| [Graph-to-3D: End-to-End Generation and Manipulation of 3D Scenes Using Scene Graphs](https://openaccess.thecvf.com/content/ICCV2021/html/Dhamo_Graph-to-3D_End-to-End_Generation_and_Manipulation_of_3D_Scenes_Using_Scene_ICCV_2021_paper.html)<br>ICCV 2021 · core | Uses scene graphs to jointly generate scene layout and object shape, enabling graph-conditioned 3D scene manipulation. | [Project](https://he-dhamo.github.io/Graphto3D/) · [Code](https://github.com/he-dhamo/graphto3d) · [Details](../PAPERS.md#graph-to-3d) |
| [SceneFormer: Indoor Scene Generation with Transformers](https://arxiv.org/abs/2012.09793)<br>3DV 2021 · core | Generates sequences of indoor objects, locations, and orientations conditioned on room layout, with a separate text-conditioned setting described by the authors. | [Project](https://xinpeng-wang.github.io/sceneformer/) · [Code](https://github.com/cy94/sceneformer) · [Details](../PAPERS.md#sceneformer) |

<a id="section-2"></a>

## Text and image-conditioned scene synthesis

| Paper | Focus | Official resources |
| --- | --- | --- |
| [LucidDreamer: Domain-free Generation of 3D Gaussian Splatting Scenes](https://arxiv.org/abs/2311.13384)<br>IEEE TVCG 2025 · core | Generates navigable Gaussian-splatting scenes from a single text prompt or a single image without a target scene domain. | [Project](https://luciddreamer-cvlab.github.io/) · [Code](https://github.com/luciddreamer-cvlab/LucidDreamer) · [Details](../PAPERS.md#luciddreamer) |
| [RealmDreamer: Text-Driven 3D Scene Generation with Inpainting and Depth Diffusion](https://arxiv.org/abs/2404.07199)<br>3DV 2025 · core | Optimizes a Gaussian-splatting representation through diffusion-based inpainting and depth guidance to synthesize forward-facing text-conditioned scenes. | [Project](https://realmdreamer.github.io/) · [Code](https://github.com/jaidevshriram/realmdreamer) · [Details](../PAPERS.md#realmdreamer) |
| [WonderWorld: Interactive 3D Scene Generation from a Single Image](https://arxiv.org/abs/2406.09394)<br>CVPR 2025 · core | Expands a single image into connected 3D scenes while allowing users to specify new content and locations during exploration. | [Project](https://kovenyu.com/wonderworld/) · [Code](https://github.com/KovenYu/WonderWorld) · [Details](../PAPERS.md#wonderworld) |
| [Text2NeRF: Text-Driven 3D Scene Generation with Neural Radiance Fields](https://arxiv.org/abs/2305.11588)<br>IEEE TVCG 2024 · core | Combines neural radiance fields with text-to-image diffusion to generate view-consistent indoor and outdoor scenes from language descriptions. | [Project](https://eckertzhang.github.io/Text2NeRF.github.io/) · [Code](https://github.com/eckertzhang/Text2NeRF) · [Details](../PAPERS.md#text2nerf) |
| [SceneDreamer: Unbounded 3D Scene Generation from 2D Image Collections](https://arxiv.org/abs/2302.01330)<br>IEEE TPAMI 2023 · core | Learns an unbounded 3D scene generator from collections of 2D images, targeting large-scale visual worlds rather than an object layout alone. | [Project](https://scene-dreamer.github.io/) · [Code](https://github.com/FrozenBurning/SceneDreamer) · [Details](../PAPERS.md#scenedreamer) |
| [Text2Room: Extracting Textured 3D Meshes from 2D Text-to-Image Models](https://arxiv.org/abs/2303.11989)<br>ICCV 2023 · core | Iteratively creates a room-scale textured mesh from a text prompt by lifting text-to-image outputs through depth estimation and inpainting. | [Project](https://lukashoel.github.io/text-to-room/) · [Code](https://github.com/lukasHoel/text2room) · [Details](../PAPERS.md#text2room) |

<a id="section-3"></a>

## Procedural scene and world generation

| Paper | Focus | Official resources |
| --- | --- | --- |
| [Infinigen Indoors: Photorealistic Indoor Scenes Using Procedural Generation](https://arxiv.org/abs/2406.11824)<br>CVPR 2024 · core | Extends procedural scene construction to photorealistic indoor environments and provides an export path for real-time simulator use. | [Project](https://infinigen.org/) · [Code](https://github.com/princeton-vl/infinigen) · [Details](../PAPERS.md#infinigen-indoors) |
| [Infinite Photorealistic Worlds Using Procedural Generation](https://arxiv.org/abs/2306.09310)<br>CVPR 2023 · core | Procedurally generates diverse photorealistic natural 3D worlds, including geometry, materials, and scene composition. | [Project](https://infinigen.org/) · [Code](https://github.com/princeton-vl/infinigen) · [Details](../PAPERS.md#infinigen) |
| [ProcTHOR: Large-Scale Embodied AI Using Procedural Generation](https://arxiv.org/abs/2206.06994)<br>NeurIPS Datasets and Benchmarks 2022 · core | Procedurally samples diverse interactive 3D houses for simulated embodied-agent training and evaluation. | [Project](https://procthor.allenai.org/) · [Code](https://github.com/allenai/procthor) · [Details](../PAPERS.md#procthor) |

<a id="section-4"></a>

## Simulation environments and embodied training

| Paper | Focus | Official resources |
| --- | --- | --- |
| [Scenario Dreamer: Vectorized Latent Diffusion for Generating Driving Simulation Environments](https://arxiv.org/abs/2503.22496)<br>CVPR 2025 · core | Generates vectorized traffic scenes and closed-loop agent behaviors for driving-planner simulation, rather than indoor manipulation. | [Project](https://princeton-computational-imaging.github.io/scenario-dreamer/) · [Code](https://github.com/princeton-computational-imaging/scenario-dreamer) · [Details](../PAPERS.md#scenario-dreamer) |
| [Holodeck: Language Guided Generation of 3D Embodied AI Environments](https://arxiv.org/abs/2312.09067)<br>CVPR 2024 · core | Uses language-model planning and a 3D asset collection to construct embodied-AI environments from natural-language requirements. | [Project](https://yueyang.ai/holodeck/) · [Code](https://github.com/allenai/Holodeck) · [Details](../PAPERS.md#holodeck) |
| [RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation](https://arxiv.org/abs/2311.01455)<br>ICML 2024 · core | Uses generative simulation to create tasks, scenes, and training supervision for automated robot-skill learning. | [Project](https://robogen-ai.github.io/) · [Code](https://github.com/Genesis-Embodied-AI/RoboGen) · [Details](../PAPERS.md#robogen) |

<a id="section-5"></a>

## Generative part structure and motion

| Paper | Focus | Official resources |
| --- | --- | --- |
| [ArtLLM: Generating Articulated Assets via 3D LLM](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_ArtLLM_Generating_Articulated_Assets_via_3D_LLM_CVPR_2026_paper.html)<br>CVPR 2026 · core | Uses a 3D multimodal language model and articulation data to generate assets from complete 3D meshes. | [Project](https://authoritywang.github.io/artllm/) · [Code](https://github.com/AuthorityWang/ArtLLM) · [Details](../PAPERS.md#artllm) |
| [LAM: Language Articulated Object Modelers](https://openaccess.thecvf.com/content/CVPR2026/html/Gao_LAM_Language_Articulated_Object_Modelers_CVPR_2026_paper.html)<br>CVPR 2026 · core | Uses LLM/VLM collaboration to generate geometry and articulation code compiled into URDF. | [Project](https://gaoypeng.github.io/LAM) · [Code](https://github.com/gaoypeng/LAM) · [Details](../PAPERS.md#lam) |
| [PAct: Part-Decomposed Single-View Articulated Object Generation](https://arxiv.org/abs/2602.14965)<br>SIGGRAPH Asia (conditionally accepted) 2026 · core | A feed-forward part-centric method generates part geometry and articulation parameters from one image. | [Project](https://pact-project.github.io/) · [Code](https://github.com/Mobiuslqm/PAct) · [Details](../PAPERS.md#pact) |
| [ArtFormer: Controllable Generation of Diverse 3D Articulated Objects](https://openaccess.thecvf.com/content/CVPR2025/html/Su_ArtFormer_Controllable_Generation_of_Diverse_3D_Articulated_Objects_CVPR_2025_paper.html)<br>CVPR 2025 · core | Uses a tree-token representation to generate high-level geometry codes and kinematic relations under text conditions. | Project: — · [Code](https://github.com/ShuYuMo2003/ArtFormer) · [Details](../PAPERS.md#artformer) |
| [Guiding Diffusion-Based Articulated Object Generation by Partial Point Cloud Alignment and Physical Plausibility Constraints](https://openaccess.thecvf.com/content/ICCV2025/html/Kreber_Guiding_Diffusion-Based_Articulated_Object_Generation_by_Partial_Point_Cloud_Alignment_ICCV_2025_paper.html)<br>ICCV 2025 · core | Guides articulated diffusion with partial point-cloud alignment and constraints on penetration and joint mobility. | Project: — · [Code](https://github.com/EmbodiedVision/physnap) · [Details](../PAPERS.md#physnap) |
| [SINGAPO: Single Image Controlled Generation of Articulated Parts in Objects](https://proceedings.iclr.cc/paper_files/paper/2025/hash/f2ba7d0d1394609d5ce11853cfd1c9bf-Abstract-Conference.html)<br>ICLR 2025 · core | Generates plausible articulated assets from one resting-state RGB view while modeling geometry and kinematic ambiguity. | Project: — · [Code](https://github.com/3dlg-hcvc/singapo) · [Details](../PAPERS.md#singapo) |
| [CAGE: Controllable Articulation GEneration](https://openaccess.thecvf.com/content/CVPR2024/html/Liu_CAGE_Controllable_Articulation_GEneration_CVPR_2024_paper.html)<br>CVPR 2024 · core | Generates an articulated shape abstraction with geometry and motion parameters subject to category and graph constraints. | [Project](https://3dlg-hcvc.github.io/cage/) · [Code](https://github.com/3dlg-hcvc/cage) · [Details](../PAPERS.md#cage) |
| [NAP: Neural 3D Articulated Object Prior](https://proceedings.neurips.cc/paper_files/paper/2023/hash/655846cc914cb7ff977a1ada40866441-Abstract-Conference.html)<br>NeurIPS 2023 · core | Uses diffusion over an articulation graph to synthesize articulated object models and conditional variants. | [Project](https://www.jiahuilei.com/projects/nap/) · [Code](https://github.com/JiahuiLei/NAP) · [Details](../PAPERS.md#nap) |

<a id="section-6"></a>

## Language and vision-guided asset authoring

| Paper | Focus | Official resources |
| --- | --- | --- |
| [Articraft: An Agentic System for Scalable Articulated 3D Asset Generation](https://arxiv.org/abs/2605.15187)<br>arXiv preprint 2026 · core | Uses LLM-written domain-specific code to define parts, geometry, joints, and validation for articulated assets. | [Project](https://articraft3d.github.io/) · [Code](https://github.com/articraftresearch/Articraft) · [Details](../PAPERS.md#articraft) |
| [Articulate AnyMesh: Open-Vocabulary 3D Articulated Objects Modeling](https://arxiv.org/abs/2502.02590)<br>CoRL 2025 · core | Converts a rigid 3D mesh into an articulated counterpart using VLMs and visual prompts for parts and joints. | [Project](https://articulate-anymesh.github.io/) · Code: announced · [Details](../PAPERS.md#articulate-anymesh) |
| [Articulate-Anything: Automatic Modeling of Articulated Objects via a Vision-Language Foundation Model](https://proceedings.iclr.cc/paper_files/paper/2025/hash/2c8047bf3ed8ef6905351608d641f02f-Abstract-Conference.html)<br>ICLR 2025 · core | Uses text, images, or video plus retrieval and VLM-generated programs to create simulator-ready articulated URDF assets. | [Project](https://articulate-anything.github.io/) · [Code](https://github.com/vlongle/articulate-anything) · [Details](../PAPERS.md#articulate-anything) |

<a id="section-7"></a>

## Surveys and perspectives

| Paper | Focus | Official resources |
| --- | --- | --- |
| [3D Generation for Embodied AI and Robotic Simulation: A Survey](https://arxiv.org/abs/2604.26509)<br>arXiv 2026 · enabling | Reviews generated assets, interactive environments, and sim-to-real pipelines, distinguishing appearance, physical validity, and embodied-task evaluation. | [Project](https://3dgen4robot.github.io/) · Code: — · [Details](../PAPERS.md#survey-generation-embodied) |
| [3D Scene Generation: A Survey](https://arxiv.org/abs/2505.05474)<br>IJCV 2026 · enabling | Organizes scene synthesis by procedural, neural 3D, image-based, and video-based methods, with evaluation and applications. | [Project](https://github.com/hzxie/Awesome-3D-Scene-Generation) · Code: — · [Details](../PAPERS.md#survey-scene-generation) |
| [3D and 4D World Modeling: A Survey](https://arxiv.org/abs/2509.07996)<br>arXiv 2025 · enabling | Organizes world modeling around video, occupancy, and LiDAR representations, with definitions, evaluation settings, and applications. | [Project](https://worldbench.github.io/survey) · Code: — · [Details](../PAPERS.md#survey-world-modeling) |
