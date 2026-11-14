# Benchmarks and discovery map

[← Overview](README.md) · [Topic pages](PAPERS.md#topic-directory) · [Full paper index](PAPERS.md)

Datasets, tasks, and evaluation protocols for 3D scenes and embodied interaction. Catalog connections identify related literature; compare results within the relevant task and protocol.

## Navigator

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

## ScanNet++ Benchmark

**Task:** 3D semantic and instance segmentation on high-fidelity indoor scans.

**Protocol / status:** Current public pages default to v2. Semantic segmentation evaluates the top 100 semantic classes, with top-1/top-3 multilabel IoU on decimated mesh vertices; instance segmentation uses the countable subset of those classes and AP/AP50/AP25. Preserve version, task, split and supervision when comparing methods.

**Catalog connections:** [ScanNet++](PAPERS.md#scannetpp) · [PTv3](PAPERS.md#ptv3) · [PTv2](PAPERS.md#point-transformer-v2) · [OneFormer3D](PAPERS.md#oneformer3d) · [SoftGroup](PAPERS.md#softgroup) · [PointGroup](PAPERS.md#pointgroup) · [DITR](PAPERS.md#ditr) · [Sonata](PAPERS.md#sonata) · [Volt](PAPERS.md#volume-transformer) · [CAC](PAPERS.md#context-aware-classifier) · [OA-CNNs](PAPERS.md#oa-cnns) · [OctFormer](PAPERS.md#octformer) · [LaSSM](PAPERS.md#lassm) · [SGIFormer](PAPERS.md#sgiformer) · [SPFormer](PAPERS.md#spformer).

**Unresolved entries / coverage gaps:**

- Beyond Context Bias: Adaptive Instance Placement for Robust 3D Instance Segmentation (Rongkun Yang et al.; leaderboard row did not supply a publication URL). A primary project page and code repository exist, but this bounded import intentionally omits it pending a canonical paper record.
- Anonymous instance-segmentation submissions have not been mapped to publications.

[Official source](https://scannetpp.mlsg.cit.tum.de/scannetpp/benchmark/docs) · [Evaluation / leaderboard](https://scannetpp.mlsg.cit.tum.de/scannetpp/benchmark/insseg)


## ScanNet Benchmark

**Task:** Indoor 3D semantic and instance segmentation.

**Protocol / status:** State semantic, instance, or panoptic task and split for every comparison.

**Catalog connections:** [ScanNet](PAPERS.md#scannet-dataset) · [PointGroup](PAPERS.md#pointgroup) · [HAIS](PAPERS.md#hais) · [SoftGroup](PAPERS.md#softgroup) · [Mask3D](PAPERS.md#mask3d) · [OneFormer3D](PAPERS.md#oneformer3d) · [PTv3](PAPERS.md#ptv3).

[Official source](https://www.scan-net.org/) · [Evaluation / leaderboard](https://kaldir.vc.in.tum.de/scannet_benchmark/semantic_instance_3d)


## ScanNet200

**Task:** Long-tail 3D semantic and instance segmentation with 200 classes.

**Protocol / status:** Scores are not interchangeable with ScanNet20; preserve label set and metric.

**Catalog connections:** [ScanNet200 / LanguageGroundedSemseg](PAPERS.md#scannet200) · [Mask3D](PAPERS.md#mask3d) · [OneFormer3D](PAPERS.md#oneformer3d) · [PTv3](PAPERS.md#ptv3) · [OpenMask3D](PAPERS.md#openmask3d) · [Open3DIS](PAPERS.md#open3dis).

[Official source](https://kaldir.vc.in.tum.de/scannet_benchmark/documentation) · [Evaluation / leaderboard](https://kaldir.vc.in.tum.de/scannet_benchmark/semantic_instance_3d)


## S3DIS

**Task:** Indoor point-cloud semantic, instance, and panoptic segmentation.

**Protocol / status:** Keep Area 5 and 6-fold protocols distinct.

**Catalog connections:** [S3DIS](PAPERS.md#s3dis-dataset) · [PointNet](PAPERS.md#pointnet) · [PointNet++](PAPERS.md#pointnet-plus-plus) · [SPG](PAPERS.md#superpoint-graph) · [SPT](PAPERS.md#superpoint-transformer) · [Stratified Transformer](PAPERS.md#stratified-transformer) · [PTv3](PAPERS.md#ptv3).

**Unresolved entries / coverage gaps:**

- No single official all-method leaderboard was confirmed in this pass.

[Official source](http://buildingparser.stanford.edu/dataset.html)


## MultiScan Benchmark

**Task:** Object instance segmentation, part instance segmentation, and mobility prediction in articulated indoor environments.

**Protocol / status:** Official repository exposes separate benchmark downloads and data preparation paths for object, part, and mobility tasks.

**Catalog connections:** [MultiScan](PAPERS.md#multiscan).

[Official source](https://github.com/smartscenes/multiscan)


## ARKitScenes

**Task:** Mobile RGB-D indoor scene understanding tasks.

**Protocol / status:** Access and download are governed by the dataset repository and its terms; do not equate its task protocols with ScanNet.

**Catalog connections:** [ARKitScenes](PAPERS.md#arkitscenes).

[Official source](https://github.com/apple/ARKitScenes)


## Articulation-XL2.0

**Task:** Static 3D assets to articulated structure and motion.

**Protocol / status:** Official MagicArticulate release links the data; no canonical public leaderboard was verified.

**Catalog connections:** [MagicArticulate](PAPERS.md#magicarticulate).

[Official source](https://github.com/Seed3D/MagicArticulate)


## PartNet-Mobility

**Task:** Articulated object assets, motion annotations, rendering, and simulation.

**Protocol / status:** Use paper-specific protocols; this is not a cross-paper leaderboard.

**Catalog connections:** [SAPIEN](PAPERS.md#sapien) · [Ditto](PAPERS.md#ditto) · [CAGE](PAPERS.md#cage) · [FlowBot3D](PAPERS.md#flowbot3d) · [PAct](PAPERS.md#pact).

[Official source](https://huggingface.co/datasets/sapien-sim/PartNetMobility)


## Articulated Container Dataset

**Task:** Openable containers with articulation annotations.

**Protocol / status:** PAct evaluates on ACD; a canonical public leaderboard was not located in this pass.

**Catalog connections:** [S2O](PAPERS.md#s2o) · [PAct](PAPERS.md#pact).

[Official source](https://huggingface.co/datasets/3dlg-hcvc/s2o)


## ManiSkill2

**Task:** Generalizable manipulation with articulated tasks including cabinet doors/drawers, faucets, chairs, mobile-base and dual-arm settings.

**Protocol / status:** Scores require task, observation modality, embodiment, controller, and split. The public ongoing leaderboard is benchmark-specific; this survey should ingest results only with those fields.

**Catalog connections:** [ManiSkill2](PAPERS.md#maniskill2).

[Official source](https://maniskill2.github.io/) · [Evaluation / leaderboard](https://sapien.ucsd.edu/challenges/maniskill/challenges/ms2-ongoing)


## RLBench

**Task:** Vision-guided manipulation benchmark with diverse scripted tasks, including articulated-state interactions.

**Protocol / status:** Treat it as an enabling benchmark: only methods evaluated on tasks explicitly involving articulated state should enter the articulation-specific comparison table.

**Catalog connections:** [RLBench](PAPERS.md#rlbench).

[Official source](https://github.com/stepjam/RLBench)


## BEHAVIOR-1K / OmniGibson

**Task:** Long-horizon household tasks in realistic scenes using mobile, bimanual-capable embodied agents and dynamic object states.

**Protocol / status:** The 2026 challenge pins an evaluation configuration and restricts policies to onboard observations; retain version, robot configuration, task subset, and partial-credit rule with any result. OmniGibson is covered as BEHAVIOR-1K software, not as a separate misattributed paper record.

**Catalog connections:** [BEHAVIOR-1K](PAPERS.md#behavior1k).

[Official source](https://behavior.stanford.edu/) · [Evaluation / leaderboard](https://github.com/StanfordVL/BEHAVIOR-1K/tree/main/docs/challenge)


## SceneFun3D

**Task:** Functionality segmentation, language-driven affordance grounding, and interaction-motion annotations.

**Protocol / status:** SceneFun3D's documented segmentation/grounding evaluation uses dataset v0.2.0 and hidden test submissions. Segmentation is ranked by AP averaged over IoU thresholds; grounding by AP50. For scene-level motion estimation, see the Articulate3D challenge. Keep the datasets, inputs, and scoring protocols distinct.

**Related challenge:** [Articulate3D challenge](https://insait-institute.github.io/articulate3d.github.io/challenge.html).

**Catalog connections:** [SceneFun3D](PAPERS.md#scenefun3d) · [Articulate3D](PAPERS.md#articulate3d) · [Volt](PAPERS.md#volume-transformer).

**Unresolved entries / coverage gaps:**

- Revisit the dynamic EvalAI table before identifying current leaders or associating submission names with papers.

[Official source](https://scenefun3d.github.io/documentation/) · [Evaluation / leaderboard](https://eval.ai/web/challenges/challenge-page/2466/overview)


## Articulate3D Challenge

**Task:** Scene-level movable-part and interactable-region segmentation, with motion type, axis and origin prediction.

**Protocol / status:** The ECCV 2026 page specifies indoor scene point clouds and reports segmentation AP50 together with motion metrics MA, MO and MAO-ST. Keep challenge editions separate, and distinguish this motion-estimation protocol from SceneFun3D segmentation and grounding evaluation.

**Catalog connections:** [Articulate3D](PAPERS.md#articulate3d) · [Segment–Snap](PAPERS.md#segment-snap).

**Unresolved entries / coverage gaps:**

- Resolve other named challenge submissions to their official papers before adding publication records.

[Official source](https://insait-institute.github.io/articulate3d.github.io/challenge.html) · [Evaluation / leaderboard](https://insait-institute.github.io/articulate3d.github.io/challenge.html#leaderboard)


## RoboCasa / RoboCasa365

**Task:** Generalist kitchen manipulation with mobile robots, articulated appliances and composite household tasks.

**Protocol / status:** The current multi-task leaderboard evaluates 50 target tasks with Atomic-Seen, Composite-Seen and Composite-Unseen splits; its specified pretraining data and versioned horizons matter. Distinguish original RoboCasa from RoboCasa365 and model versions from the publications introducing their families.

**Catalog connections:** [RoboCasa](PAPERS.md#robocasa) · [RoboCasa365](PAPERS.md#robocasa365) · [Diffusion Policy](PAPERS.md#diffusion-policy) · [π0](PAPERS.md#pi-zero) · [π0.5](PAPERS.md#pi-zero-point-five) · [GR00T N1](PAPERS.md#groot-n1).

**Unresolved entries / coverage gaps:**

- Many current policy submissions and agentic wrappers have not yet been mapped to individual canonical papers. The listed policy records are contextual references only; they do not assert an exact submitted configuration, score, or rank.

[Official source](https://robocasa.ai/) · [Evaluation / leaderboard](https://robocasa.ai/leaderboard.html)


## ALFRED

**Task:** Language-guided household task completion with navigation and object interaction in AI2-THOR.

**Protocol / status:** Record seen/unseen split, task type, observation setup, and whether language subgoals are provided.

**Catalog connections:** [ALFRED](PAPERS.md#alfred) · [LLM-Planner](PAPERS.md#llm-planner).

[Official source](https://askforalfred.com/)


## TEACh

**Task:** Dialog-guided embodied household tasks with an interactive teacher in AI2-THOR.

**Protocol / status:** Keep dialog setting, task split, and agent interaction budget alongside results.

**Catalog connections:** [TEACh](PAPERS.md#teach).

[Official source](https://teachable-ai.org/)


## OpenEQA

**Task:** Open-vocabulary embodied question answering from episodic memory or active exploration.

**Protocol / status:** Distinguish episodic-memory and active-exploration settings; natural-language answers use the benchmark evaluation protocol.

**Catalog connections:** [OpenEQA](PAPERS.md#openeqa).

[Official source](https://open-eqa.github.io/)


## EmbodiedQA

**Task:** Navigation and question answering in 3D environments.

**Protocol / status:** Treat navigation budget and answer accuracy as linked but separate aspects of the task.

**Catalog connections:** [EmbodiedQA](PAPERS.md#embodiedqa).

[Official source](https://embodiedqa.org/)


## Habitat 2.0 / Home Assistant Benchmark

**Task:** Physics-enabled household rearrangement and home-assistant tasks in interactive 3D environments.

**Protocol / status:** Preserve task, robot embodiment, controller, observations, and generalization split when comparing agents.

**Catalog connections:** [Habitat 2.0](PAPERS.md#habitat2).

[Official source](https://aihabitat.org/habitat2/)


## Habitat 3.0

**Task:** Collaborative social navigation and social rearrangement with humanoid avatars or human partners.

**Protocol / status:** State whether evaluation uses avatar policies or humans-in-the-loop, plus task and environment setting.

**Catalog connections:** [Habitat 3.0](PAPERS.md#habitat3).

[Official source](https://aihabitat.org/habitat3/)


## GOAT-Bench

**Task:** Lifelong navigation to object-category, image, and language goals.

**Protocol / status:** Preserve goal modality, memory setting, noise configuration, and lifelong episode structure.

**Catalog connections:** [GOAT-Bench](PAPERS.md#goat-bench).

[Official source](https://mukulkhanna.github.io/goat-bench/)


## Room-to-Room (R2R)

**Task:** Vision-and-language navigation in real scanned indoor environments.

**Protocol / status:** Record split, navigation metric, instruction setting, and scene dataset/version.

**Catalog connections:** [R2R](PAPERS.md#r2r).

[Official source](https://bringmeaspoon.org/)


## Habitat navigation ecosystem

**Task:** Embodied navigation with simulation, scene datasets, sensors, and task configurations.

**Protocol / status:** Navigation papers use differing scene datasets, goal specifications, maps, and sensing; do not compare them without those fields.

**Catalog connections:** [VLMaps](PAPERS.md#vlmaps) · [VLFM](PAPERS.md#vlfm).

[Official source](https://aihabitat.org/)

## How records enter the catalog

1. Inspect the exact benchmark task and public track.
2. Resolve a named method to a primary publication and official resources.
3. Record version, split, modality, and relevant protocol differences.
4. Keep anonymous teams and unresolved links as coverage gaps rather than inferred papers.
5. Add a task-specific summary and explicit core/enabling classification.
