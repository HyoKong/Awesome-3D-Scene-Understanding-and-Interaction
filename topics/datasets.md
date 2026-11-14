# Datasets, simulators, and benchmarks

> The data, environments, and evaluation protocols that make comparisons meaningful.

[← Overview](../README.md) · [Full paper index](../PAPERS.md) · [Benchmarks](../BENCHMARKS.md) · [Contribute](../CONTRIBUTING.md)

Papers are grouped by editorial section and ordered newest first within each section. Classification expresses relevance, not a rank.

[Functional indoor scenes and annotations](#section-1) · [Real indoor scenes](#section-2) · [Actionable parts and articulated-object data](#section-3) · [3D language and embodied instruction data](#section-4) · [Embodied navigation and semantic memory](#section-5) · [Embodied question answering and 3D reasoning](#section-6) · [Embodied instruction following and planning](#section-7) · [Embodied simulators and household tasks](#section-8) · [Generated environments and simulation resources](#section-9) · [Articulated assets and simulators](#section-10) · [Manipulation and household-task benchmarks](#section-11) · [Task-specific manipulation benchmarks](#section-12) · [Driving simulation](#section-13) · [Benchmark and resource directory](#resource-directory)

<a id="section-1"></a>

## Functional indoor scenes and annotations

| Paper | Focus | Official resources |
| --- | --- | --- |
| [Articulate3D: Holistic Understanding of 3D Scenes as Universal Scene Description](https://openaccess.thecvf.com/content/ICCV2025/html/Halacheva_Articulate3D_Holistic_Understanding_of_3D_Scenes_as_Universal_Scene_Description_ICCV_2025_paper.html)<br>ICCV 2025 · core | Articulate3D provides part masks, connectivity, articulation, and interactable-region annotations for ScanNet++ scenes, together with a scene-understanding challenge. | [Project](https://insait-institute.github.io/articulate3d.github.io/) · [Code](https://github.com/insait-institute/USDNet) · [Details](../PAPERS.md#articulate3d) |
| [SceneFun3D: Fine-Grained Functionality and Affordance Understanding in 3D Scenes](https://alexdelitzas.github.io/assets/pdf/SceneFun3D.pdf)<br>CVPR 2024 · core | SceneFun3D provides fine-grained functional-element masks, affordance labels, task descriptions, and interaction motions in real indoor scenes. | [Project](https://scenefun3d.github.io/) · [Toolkit](https://github.com/SceneFun3D/scenefun3d) · [Details](../PAPERS.md#scenefun3d) |
| [ScanRefer: 3D Object Localization in RGB-D Scans using Natural Language](https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/597_ECCV_2020_paper.php)<br>ECCV 2020 · core | ScanRefer pairs natural-language object descriptions with annotated objects in ScanNet scenes for 3D language grounding. | [Project](https://daveredrum.github.io/ScanRefer/) · [Code](https://github.com/daveredrum/ScanRefer) · [Details](../PAPERS.md#scanrefer) |

<a id="section-2"></a>

## Real indoor scenes

| Paper | Focus | Official resources |
| --- | --- | --- |
| [ScanNet++: A High-Fidelity Dataset of 3D Indoor Scenes](https://openaccess.thecvf.com/content/ICCV2023/html/Yeshwanth_ScanNet_A_High-Fidelity_Dataset_of_3D_Indoor_Scenes_ICCV_2023_paper.html)<br>ICCV 2023 · enabling | Pairs high-fidelity indoor geometry with registered DSLR and mobile RGB-D observations for scene understanding and novel view synthesis. | [Project](https://scannetpp.mlsg.cit.tum.de/scannetpp/) · [Toolkit](https://github.com/scannetpp/scannetpp) · [Details](../PAPERS.md#scannetpp) |
| [MultiScan: Scalable RGBD Scanning for 3D Environments with Articulated Objects](https://arxiv.org/abs/2203.16840)<br>NeurIPS 2022 · core | Provides RGB-D environments with object/part semantics and articulated-part mobility annotations. | [Project](https://multiscan3d.github.io/) · [Toolkit](https://github.com/smartscenes/multiscan) · [Details](../PAPERS.md#multiscan) |
| [Language-Grounded Indoor 3D Semantic Segmentation in the Wild](https://arxiv.org/abs/2204.07761)<br>ECCV 2022 · enabling | Introduces a 200-category ScanNet benchmark and language-guided feature pretraining to study long-tail indoor semantic segmentation. | [Project](https://rozdavid.github.io/scannet200) · [Code](https://github.com/RozDavid/LanguageGroundedSemseg) · [Details](../PAPERS.md#scannet200) |
| [ARKitScenes: A Diverse Real-World Dataset for 3D Indoor Scene Understanding Using Mobile RGB-D Data](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/file/66f041e16a60928b05a7e228a89c3799-Paper-round1.pdf)<br>NeurIPS Datasets and Benchmarks 2021 · enabling | Provides mobile RGB-D indoor captures and benchmarks for scene understanding. | [Project](https://github.com/apple-aiml-research/ARKitScenes) · [Toolkit](https://github.com/apple-aiml-research/ARKitScenes) · [Details](../PAPERS.md#arkitscenes) |
| [ScanNet: Richly-annotated 3D Reconstructions of Indoor Scenes](https://openaccess.thecvf.com/content_cvpr_2017/html/Dai_ScanNet_Richly-Annotated_3D_CVPR_2017_paper.html)<br>CVPR 2017 · enabling | Provides richly annotated RGB-D reconstructions and benchmark tasks for indoor 3D scene understanding. | [Project](https://www.scan-net.org/) · [Toolkit](https://github.com/ScanNet/ScanNet) · [Details](../PAPERS.md#scannet-dataset) |
| [A Large-Scale 3D Point Cloud Dataset for Indoor Scene Segmentation](https://openaccess.thecvf.com/content_cvpr_2016/html/Armeni_3D_Semantic_Parsing_CVPR_2016_paper.html)<br>CVPR 2016 · enabling | Provides large indoor point clouds and semantic labels used by room-scale segmentation protocols. | [Project](http://buildingparser.stanford.edu/dataset.html) · Code: — · [Details](../PAPERS.md#s3dis-dataset) |

<a id="section-3"></a>

## Actionable parts and articulated-object data

| Paper | Focus | Official resources |
| --- | --- | --- |
| [MagicArticulate: Make Your 3D Models Articulation-Ready](https://openaccess.thecvf.com/content/CVPR2025/html/Song_MagicArticulate_Make_Your_3D_Models_Articulation-Ready_CVPR_2025_paper.html)<br>CVPR 2025 · core | Articulation-XL2.0 provides articulated 3D asset data; MagicArticulate supplies methods for recovering structure and motion from static meshes. | [Project](https://chaoyuesong.github.io/MagicArticulate/) · [Code](https://github.com/Seed3D/MagicArticulate) · [Details](../PAPERS.md#magicarticulate) |
| [OPDMulti: Openable Part Detection for Multiple Objects](https://3dlg-hcvc.github.io/OPDMulti/)<br>3DV 2024 · core | OPDMulti provides multi-object images annotated with openable parts and their motion parameters. | [Project](https://3dlg-hcvc.github.io/OPDMulti/) · [Code](https://github.com/3dlg-hcvc/OPDMulti) · [Details](../PAPERS.md#opdmulti) |
| [GAPartNet: Cross-Category Domain-Generalizable Object Perception and Manipulation via Generalizable and Actionable Parts](https://openaccess.thecvf.com/content/CVPR2023/html/Geng_GAPartNet_Cross-Category_Domain-Generalizable_Object_Perception_and_Manipulation_via_Generalizable_and_CVPR_2023_paper.html)<br>CVPR 2023 · core | GAPartNet provides cross-category actionable-part semantics and pose annotations for interactive objects. | [Project](https://pku-epic.github.io/GAPartNet/) · [Code](https://github.com/PKU-EPIC/GAPartNet) · [Details](../PAPERS.md#gapartnet) |
| [OPD: Single-view 3D Openable Part Detection](https://3dlg-hcvc.github.io/OPD/)<br>ECCV 2022 · core | OPDSynth and OPDReal provide synthetic and real observations with openable-part masks and motion-parameter annotations. | [Project](https://3dlg-hcvc.github.io/OPD/) · [Code](https://github.com/3dlg-hcvc/OPD) · [Details](../PAPERS.md#opd) |

<a id="section-4"></a>

## 3D language and embodied instruction data

| Paper | Focus | Official resources |
| --- | --- | --- |
| [LEO: An Embodied Generalist Agent in 3D World](https://arxiv.org/abs/2311.12871)<br>ICML 2024 · core | LEO-align and LEO-instruct combine existing and synthesized multimodal examples for 3D vision-language alignment and embodied instruction tuning. | [Project](https://embodied-generalist.github.io/) · [Code](https://github.com/embodied-generalist/embodied-generalist) · [Details](../PAPERS.md#leo) |
| [3D-LLM: Injecting the 3D World into Large Language Models](https://arxiv.org/abs/2307.12981)<br>NeurIPS 2023 · core | The 3D-LLM release includes object- and scene-level 3D-language annotations and features for pretraining and downstream question-answering tasks. | Project: — · [Code](https://github.com/UMass-Embodied-AGI/3D-LLM) · [Details](../PAPERS.md#3d-llm) |

<a id="section-5"></a>

## Embodied navigation and semantic memory

| Paper | Focus | Official resources |
| --- | --- | --- |
| [GOAT-Bench: A Benchmark for Multi-Modal Lifelong Navigation](https://openaccess.thecvf.com/content/CVPR2024/html/Khanna_GOAT-Bench_A_Benchmark_for_Multi-Modal_Lifelong_Navigation_CVPR_2024_paper.html)<br>CVPR 2024 · core | Evaluates lifelong navigation to object-category, image, and language goals, including the role of scene memory across goal modalities. | [Project](https://mukulkhanna.github.io/goat-bench/) · [Toolkit](https://github.com/Ram81/goat-bench) · [Details](../PAPERS.md#goat-bench) |
| [Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments](https://openaccess.thecvf.com/content_cvpr_2018/html/Anderson_Vision-and-Language_Navigation_Interpreting_CVPR_2018_paper.html)<br>CVPR 2018 · enabling | Introduces navigation in real scanned environments from natural-language route instructions and paired human demonstrations. | [Project](https://bringmeaspoon.org/) · [Toolkit](https://github.com/peteanderson80/Matterport3DSimulator) · [Details](../PAPERS.md#r2r) |

<a id="section-6"></a>

## Embodied question answering and 3D reasoning

| Paper | Focus | Official resources |
| --- | --- | --- |
| [OpenEQA: Embodied Question Answering in the Era of Foundation Models](https://openaccess.thecvf.com/content/CVPR2024/html/Majumdar_OpenEQA_Embodied_Question_Answering_in_the_Era_of_Foundation_Models_CVPR_2024_paper.html)<br>CVPR 2024 · core | Introduces open-vocabulary embodied question answering for episodic-memory and active-exploration settings in real scanned environments. | [Project](https://open-eqa.github.io/) · [Toolkit](https://github.com/facebookresearch/open-eqa) · [Details](../PAPERS.md#openeqa) |
| [Embodied Question Answering](https://openaccess.thecvf.com/content_cvpr_2018/html/Das_Embodied_Question_Answering_CVPR_2018_paper.html)<br>CVPR 2018 · enabling | Defines an embodied question-answering setting where an agent navigates a 3D environment to gather observations before answering. | [Project](https://embodiedqa.org/) · [Toolkit](https://github.com/facebookresearch/EmbodiedQA) · [Details](../PAPERS.md#embodiedqa) |

<a id="section-7"></a>

## Embodied instruction following and planning

| Paper | Focus | Official resources |
| --- | --- | --- |
| [TEACh: Task-driven Embodied Agents that Chat](https://arxiv.org/abs/2110.00534)<br>AAAI 2022 · enabling | Provides dialog-guided household tasks where an embodied agent asks questions and acts in a simulated environment. | [Project](https://teachingalfred.github.io/) · [Toolkit](https://github.com/alexa/teach) · [Details](../PAPERS.md#teach) |
| [ALFRED: A Benchmark for Interpreting Grounded Instructions for Everyday Tasks](https://openaccess.thecvf.com/content_CVPR_2020/html/Shridhar_ALFRED_A_Benchmark_for_Interpreting_Grounded_Instructions_for_Everyday_Tasks_CVPR_2020_paper.html)<br>CVPR 2020 · enabling | Benchmarks language-guided household task completion through sequences of navigation and object-interaction actions in simulated environments. | [Project](https://askforalfred.com/) · [Toolkit](https://github.com/askforalfred/alfred) · [Details](../PAPERS.md#alfred) |

<a id="section-8"></a>

## Embodied simulators and household tasks

| Paper | Focus | Official resources |
| --- | --- | --- |
| [Habitat 3.0: A Co-Habitat for Humans, Avatars and Robots](https://arxiv.org/abs/2310.13724)<br>ICLR 2024 · enabling | Adds humanoid simulation, human-in-the-loop infrastructure, and collaborative social-navigation and rearrangement tasks to Habitat. | [Project](https://aihabitat.org/habitat3/) · [Toolkit](https://github.com/facebookresearch/habitat-lab) · [Details](../PAPERS.md#habitat3) |
| [Habitat 2.0: Training Home Assistants to Rearrange their Habitat](https://proceedings.neurips.cc/paper/2021/hash/021bbc7ee20b71134d53e20206bd6feb-Abstract.html)<br>NeurIPS 2021 · enabling | Combines reconfigurable apartments, physics-enabled simulation, and home-assistant tasks for long-horizon mobile manipulation. | [Project](https://aihabitat.org/docs/habitat2/) · [Toolkit](https://github.com/facebookresearch/habitat-lab) · [Details](../PAPERS.md#habitat2) |

<a id="section-9"></a>

## Generated environments and simulation resources

| Paper | Focus | Official resources |
| --- | --- | --- |
| [Holodeck: Language Guided Generation of 3D Embodied AI Environments](https://arxiv.org/abs/2312.09067)<br>CVPR 2024 · core | Holodeck constructs embodied-AI environments from natural-language requirements and a collection of 3D assets. | [Project](https://yueyang.ai/holodeck/) · [Code](https://github.com/allenai/Holodeck) · [Details](../PAPERS.md#holodeck) |
| [Infinigen Indoors: Photorealistic Indoor Scenes Using Procedural Generation](https://arxiv.org/abs/2406.11824)<br>CVPR 2024 · core | Infinigen Indoors generates procedural indoor scenes and provides an export path for real-time simulation. | [Project](https://infinigen.org/) · [Code](https://github.com/princeton-vl/infinigen) · [Details](../PAPERS.md#infinigen-indoors) |
| [RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation](https://arxiv.org/abs/2311.01455)<br>ICML 2024 · core | RoboGen supplies a generative simulation workflow for creating robot-learning tasks, scenes, and training supervision. | [Project](https://robogen-ai.github.io/) · [Code](https://github.com/Genesis-Embodied-AI/RoboGen) · [Details](../PAPERS.md#robogen) |
| [Infinite Photorealistic Worlds Using Procedural Generation](https://arxiv.org/abs/2306.09310)<br>CVPR 2023 · core | Infinigen generates procedural natural-world geometry, materials, and scenes for synthetic visual data. | [Project](https://infinigen.org/) · [Code](https://github.com/princeton-vl/infinigen) · [Details](../PAPERS.md#infinigen) |
| [ProcTHOR: Large-Scale Embodied AI Using Procedural Generation](https://arxiv.org/abs/2206.06994)<br>NeurIPS Datasets and Benchmarks 2022 · core | ProcTHOR procedurally samples interactive houses for embodied-agent training and evaluation. | [Project](https://procthor.allenai.org/) · [Code](https://github.com/allenai/procthor) · [Details](../PAPERS.md#procthor) |

<a id="section-10"></a>

## Articulated assets and simulators

| Paper | Focus | Official resources |
| --- | --- | --- |
| [Arti-PG: A Toolbox for Procedurally Synthesizing Large-Scale and Diverse Articulated Objects with Rich Annotations](https://openaccess.thecvf.com/content/ICCV2025/html/Sun_Arti-PG_A_Toolbox_for_Procedurally_Synthesizing_Large-Scale_and_Diverse_Articulated_ICCV_2025_paper.html)<br>ICCV 2025 · core | Procedurally synthesizes articulated objects with rich annotations for articulation-understanding data. | Project: — · [Toolkit](https://github.com/Analytic-Concept-Group/ArtiPG) · [Details](../PAPERS.md#arti-pg) |
| [SAPIEN: A SimulAted Part-Based Interactive ENvironment](https://openaccess.thecvf.com/content_CVPR_2020/html/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.html)<br>CVPR 2020 · enabling | Provides a physics-based, part-interactive simulation environment for articulated-object understanding and manipulation. | [Project](https://sapien.ucsd.edu/) · [Code](https://github.com/haosulab/SAPIEN) · [Details](../PAPERS.md#sapien) |

<a id="section-11"></a>

## Manipulation and household-task benchmarks

| Paper | Focus | Official resources |
| --- | --- | --- |
| [RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots](https://arxiv.org/abs/2603.04356)<br>ICLR 2026 · enabling | Scales kitchen tasks, scenes, and demonstrations to study multi-task policies, generalist pretraining, and compositional robot-task generalization. | [Project](https://robocasa.ai/) · [Code](https://github.com/robocasa/robocasa) · [Details](../PAPERS.md#robocasa365) |
| [RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots](https://arxiv.org/abs/2406.02523)<br>RSS 2024 · enabling | Combines interactive kitchen environments, varied robot embodiments, articulated furniture, and human/synthetic demonstrations for everyday robot learning. | [Project](https://robocasa.ai/) · [Code](https://github.com/robocasa/robocasa) · [Details](../PAPERS.md#robocasa) |
| [BEHAVIOR-1K: A Benchmark for Embodied AI with 1,000 Everyday Activities and Realistic Simulation](https://proceedings.mlr.press/v205/li23a.html)<br>CoRL (PMLR proceedings) 2023 · enabling | Household-activity benchmark and OmniGibson environment for long-horizon embodied tasks with dynamic object states; its current challenge documentation specifies a reproducible onboard-sensing evaluation protocol. | [Project](https://behavior.stanford.edu/) · [Code](https://github.com/StanfordVL/BEHAVIOR-1K) · [Details](../PAPERS.md#behavior1k) |
| [ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills](https://arxiv.org/abs/2302.04659)<br>ICLR 2023 · enabling | Open benchmark with articulation tasks, mobile and dual-arm settings, 2D/3D observations, demonstration data, RL, imitation learning, and planning interfaces. | [Project](https://maniskill2.github.io/) · [Code](https://github.com/haosulab/ManiSkill2) · [Details](../PAPERS.md#maniskill2) |
| [ManiSkill: Generalizable Manipulation Skill Benchmark with Large-Scale Demonstrations](https://datasets-benchmarks-proceedings.neurips.cc/paper_files/paper/2021/hash/eda80a3d5b344bc40f3bc04f65b7a357-Abstract-round2.html)<br>NeurIPS Datasets and Benchmarks 2021 · enabling | Benchmarks generalizable manipulation across diverse objects in physics simulation, with large-scale demonstrations. | [Project](https://maniskill.ai/) · [Code](https://github.com/mani-skill/ManiSkill) · [Details](../PAPERS.md#maniskill) |
| [RLBench: The Robot Learning Benchmark & Learning Environment](https://arxiv.org/abs/1909.12271)<br>IEEE Robotics and Automation Letters / ICRA 2020 · enabling | Open large-scale vision-guided manipulation benchmark used for RL, imitation, multi-task, and few-shot learning; some tasks involve opening or changing articulated object state. | Project: — · [Code](https://github.com/stepjam/RLBench) · [Details](../PAPERS.md#rlbench) |

<a id="section-12"></a>

## Task-specific manipulation benchmarks

| Paper | Focus | Official resources |
| --- | --- | --- |
| [CheckManual: A New Challenge and Benchmark for Manual-based Appliance Manipulation](https://openaccess.thecvf.com/content/CVPR2025/html/Long_CheckManual_A_New_Challenge_and_Benchmark_for_Manual-based_Appliance_Manipulation_CVPR_2025_paper.html)<br>CVPR 2025 · core | CheckManual provides manual-based appliance-manipulation tasks, articulated-object assets, environment setup, and the ManualPlan baseline. | [Project](https://sites.google.com/view/checkmanual) · [Code](https://github.com/LYX0501/CheckManual) · [Details](../PAPERS.md#checkmanual) |

<a id="section-13"></a>

## Driving simulation

| Paper | Focus | Official resources |
| --- | --- | --- |
| [Scenario Dreamer: Vectorized Latent Diffusion for Generating Driving Simulation Environments](https://arxiv.org/abs/2503.22496)<br>CVPR 2025 · core | Scenario Dreamer generates traffic scenes and closed-loop agent behavior for driving simulation. | [Project](https://princeton-computational-imaging.github.io/scenario-dreamer/) · [Code](https://github.com/princeton-computational-imaging/scenario-dreamer) · [Details](../PAPERS.md#scenario-dreamer) |

<a id="resource-directory"></a>

## Benchmark and resource directory

Datasets, simulators, challenges, and evaluation resources from the [benchmark guide](../BENCHMARKS.md).

| Benchmark / resource | Tasks and relevance | Official entry point |
| --- | --- | --- |
| ScanNet++ Benchmark | 3D semantic and instance segmentation on high-fidelity indoor scans. | [Website](https://scannetpp.mlsg.cit.tum.de/scannetpp/benchmark/docs) · [Evaluation / leaderboard](https://scannetpp.mlsg.cit.tum.de/scannetpp/benchmark/insseg) |
| ScanNet Benchmark | Indoor 3D semantic and instance segmentation. | [Website](https://www.scan-net.org/) · [Evaluation / leaderboard](https://kaldir.vc.in.tum.de/scannet_benchmark/semantic_instance_3d) |
| ScanNet200 | Long-tail 3D semantic and instance segmentation with 200 classes. | [Website](https://kaldir.vc.in.tum.de/scannet_benchmark/documentation) · [Evaluation / leaderboard](https://kaldir.vc.in.tum.de/scannet_benchmark/semantic_instance_3d) |
| S3DIS | Indoor point-cloud semantic, instance, and panoptic segmentation. | [Website](http://buildingparser.stanford.edu/dataset.html) |
| MultiScan Benchmark | Object instance segmentation, part instance segmentation, and mobility prediction in articulated indoor environments. | [Website](https://github.com/smartscenes/multiscan) |
| ARKitScenes | Mobile RGB-D indoor scene understanding tasks. | [Website](https://github.com/apple/ARKitScenes) |
| Articulation-XL2.0 | Static 3D assets to articulated structure and motion. | [Website](https://github.com/Seed3D/MagicArticulate) |
| PartNet-Mobility | Articulated object assets, motion annotations, rendering, and simulation. | [Website](https://huggingface.co/datasets/sapien-sim/PartNetMobility) |
| Articulated Container Dataset | Openable containers with articulation annotations. | [Website](https://huggingface.co/datasets/3dlg-hcvc/s2o) |
| ManiSkill2 | Generalizable manipulation with articulated tasks including cabinet doors/drawers, faucets, chairs, mobile-base and dual-arm settings. | [Website](https://maniskill2.github.io/) · [Evaluation / leaderboard](https://sapien.ucsd.edu/challenges/maniskill/challenges/ms2-ongoing) |
| RLBench | Vision-guided manipulation benchmark with diverse scripted tasks, including articulated-state interactions. | [Website](https://github.com/stepjam/RLBench) |
| BEHAVIOR-1K / OmniGibson | Long-horizon household tasks in realistic scenes using mobile, bimanual-capable embodied agents and dynamic object states. | [Website](https://behavior.stanford.edu/) · [Evaluation / leaderboard](https://github.com/StanfordVL/BEHAVIOR-1K/tree/main/docs/challenge) |
| SceneFun3D | Functionality segmentation, language-driven affordance grounding, and interaction-motion annotations. | [Website](https://scenefun3d.github.io/documentation/) · [Evaluation / leaderboard](https://eval.ai/web/challenges/challenge-page/2466/overview) |
| Articulate3D Challenge | Scene-level movable-part and interactable-region segmentation, with motion type, axis and origin prediction. | [Website](https://insait-institute.github.io/articulate3d.github.io/challenge.html) · [Evaluation / leaderboard](https://insait-institute.github.io/articulate3d.github.io/challenge.html#leaderboard) |
| RoboCasa / RoboCasa365 | Generalist kitchen manipulation with mobile robots, articulated appliances and composite household tasks. | [Website](https://robocasa.ai/) · [Evaluation / leaderboard](https://robocasa.ai/leaderboard.html) |
| ALFRED | Language-guided household task completion with navigation and object interaction in AI2-THOR. | [Website](https://askforalfred.com/) |
| TEACh | Dialog-guided embodied household tasks with an interactive teacher in AI2-THOR. | [Website](https://teachable-ai.org/) |
| OpenEQA | Open-vocabulary embodied question answering from episodic memory or active exploration. | [Website](https://open-eqa.github.io/) |
| EmbodiedQA | Navigation and question answering in 3D environments. | [Website](https://embodiedqa.org/) |
| Habitat 2.0 / Home Assistant Benchmark | Physics-enabled household rearrangement and home-assistant tasks in interactive 3D environments. | [Website](https://aihabitat.org/habitat2/) |
| Habitat 3.0 | Collaborative social navigation and social rearrangement with humanoid avatars or human partners. | [Website](https://aihabitat.org/habitat3/) |
| GOAT-Bench | Lifelong navigation to object-category, image, and language goals. | [Website](https://mukulkhanna.github.io/goat-bench/) |
| Room-to-Room (R2R) | Vision-and-language navigation in real scanned indoor environments. | [Website](https://bringmeaspoon.org/) |
| Habitat navigation ecosystem | Embodied navigation with simulation, scene datasets, sensors, and task configurations. | [Website](https://aihabitat.org/) |
