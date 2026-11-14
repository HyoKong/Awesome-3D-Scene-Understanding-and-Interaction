# Embodied agents and robotic interaction

> Connecting spatial memory, navigation, embodied reasoning, task planning, and manipulation.

[← Overview](../README.md) · [Full paper index](../PAPERS.md) · [Benchmarks](../BENCHMARKS.md) · [Contribute](../CONTRIBUTING.md)

Papers are grouped by editorial section and ordered newest first within each section. Classification expresses relevance, not a rank.

[Semantic maps, memory and navigation](#section-1) · [3D reasoning and embodied generalists](#section-2) · [Language-grounded planning and agents](#section-3) · [Generalist policies and vision-language-action models](#section-4) · [Language-guided manipulation and agents](#section-5) · [Affordances and active exploration](#section-6) · [Motion-aware control and manipulation](#section-7) · [Contact and tactile feedback](#section-8) · [Surveys and perspectives](#section-9)

<a id="section-1"></a>

## Semantic maps, memory and navigation

| Paper | Focus | Official resources |
| --- | --- | --- |
| [VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation](https://arxiv.org/abs/2312.01050)<br>ICRA 2024 · core | Combines frontier exploration with visual-language goal recognition for zero-shot semantic navigation. | [Project](https://naoki.io/vlfm/) · [Code](https://github.com/rai-opensource/vlfm) · [Details](../PAPERS.md#vlfm) |
| [LM-Nav: Robotic Navigation with Large Pre-Trained Models of Language, Vision, and Action](https://proceedings.mlr.press/v205/shah23b.html)<br>CoRL (PMLR proceedings) 2023 · core | Uses language models to name landmarks, image-language association to ground them, and a vision navigation model to execute long-horizon language instructions. | [Project](https://sites.google.com/view/lmnav/home) · [Code](https://github.com/blazejosinski/lm_nav) · [Details](../PAPERS.md#lm-nav) |
| [Visual Language Maps for Robot Navigation](https://arxiv.org/abs/2210.05714)<br>ICRA 2023 · core | Fuses visual-language features into a spatial 3D map that can be queried with language for navigation goals and obstacle maps. | [Project](https://vlmaps.github.io/) · [Code](https://github.com/vlmaps/vlmaps) · [Details](../PAPERS.md#vlmaps) |

<a id="section-2"></a>

## 3D reasoning and embodied generalists

| Paper | Focus | Official resources |
| --- | --- | --- |
| [LEO: An Embodied Generalist Agent in 3D World](https://arxiv.org/abs/2311.12871)<br>ICML 2024 · core | Trains a multimodal agent with 3D vision-language alignment and vision-language-action instruction tuning across grounding, reasoning, planning, navigation, and manipulation. | [Project](https://embodied-generalist.github.io/) · [Code](https://github.com/embodied-generalist/embodied-generalist) · [Details](../PAPERS.md#leo) |
| [3D-LLM: Injecting the 3D World into Large Language Models](https://arxiv.org/abs/2307.12981)<br>NeurIPS 2023 · core | Augments a language model with 3D scene features for 3D question answering, dialogue, planning, navigation, and manipulation tasks. | Project: — · [Code](https://github.com/UMass-Embodied-AGI/3D-LLM) · [Details](../PAPERS.md#3d-llm) |

<a id="section-3"></a>

## Language-grounded planning and agents

| Paper | Focus | Official resources |
| --- | --- | --- |
| [LLM-Planner: Few-Shot Grounded Planning for Embodied Agents with Large Language Models](https://openaccess.thecvf.com/content/ICCV2023/html/Song_LLM-Planner_Few-Shot_Grounded_Planning_for_Embodied_Agents_with_Large_Language_ICCV_2023_paper.html)<br>ICCV 2023 · core | Uses few-shot language-model prompting to produce high-level plans grounded through a low-level embodied controller. | [Project](https://osu-nlp-group.github.io/LLM-Planner/) · [Code](https://github.com/OSU-NLP-Group/LLM-Planner) · [Details](../PAPERS.md#llm-planner) |

<a id="section-4"></a>

## Generalist policies and vision-language-action models

| Paper | Focus | Official resources |
| --- | --- | --- |
| [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734)<br>NVIDIA technical whitepaper 2025 · enabling | A dual-system vision-language-action foundation model for humanoid robots, trained with egocentric video, real and simulated robot trajectories, and synthetic data. | [Project](https://research.nvidia.com/index.php/publication/2025-03_nvidia-isaac-gr00t-n1-open-foundation-model-humanoid-robots) · [Code](https://github.com/NVIDIA/Isaac-GR00T) · [Details](../PAPERS.md#groot-n1) |
| [π0.5: a Vision-Language-Action Model with Open-World Generalization](https://arxiv.org/abs/2504.16054)<br>arXiv 2025 · enabling | Extends π0 with co-training across heterogeneous robot and semantic data to target open-world robot manipulation generalization. | [Project](https://www.physicalintelligence.company/blog/pi05) · [Code](https://github.com/Physical-Intelligence/openpi) · [Details](../PAPERS.md#pi-zero-point-five) |
| [Octo: An Open-Source Generalist Robot Policy](https://arxiv.org/abs/2405.12213)<br>Robotics: Science and Systems 2024 · enabling | Provides a transformer diffusion policy and training code for language- or goal-image-conditioned robot control across multiple embodiments. | [Project](https://octo-models.github.io/) · [Code](https://github.com/octo-models/octo) · [Details](../PAPERS.md#octo) |
| [OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246)<br>CoRL 2024 · enabling | Releases a vision-language-action model trained on robot demonstrations for language-conditioned visuomotor control and adaptation. | [Project](https://openvla.github.io/) · [Code](https://github.com/openvla/openvla) · [Details](../PAPERS.md#openvla) |
| [π0: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164)<br>arXiv 2024 · enabling | Combines a pretrained vision-language model with a flow-matching action expert for cross-embodiment general robot control. | [Project](https://www.physicalintelligence.company/blog/pi0) · [Code](https://github.com/Physical-Intelligence/openpi) · [Details](../PAPERS.md#pi-zero) |
| [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://arxiv.org/abs/2303.04137)<br>Robotics: Science and Systems 2023 · enabling | Represents visuomotor control as conditional action diffusion, with visual conditioning and receding-horizon action execution. | [Project](https://diffusion-policy.cs.columbia.edu/) · [Code](https://github.com/real-stanford/diffusion_policy) · [Details](../PAPERS.md#diffusion-policy) |
| [PaLM-E: An Embodied Multimodal Language Model](https://arxiv.org/abs/2303.03378)<br>ICML 2023 · enabling | Incorporates continuous visual and robot-state observations into a language model for embodied reasoning and control tasks. | [Project](https://palm-e.github.io/) · Code: — · [Details](../PAPERS.md#palm-e) |
| [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://proceedings.mlr.press/v229/zitkovich23a.html)<br>CoRL (PMLR proceedings) 2023 · enabling | Represents robot actions as tokens in a vision-language-action model to transfer visual-language knowledge to robot control. | [Project](https://robotics-transformer2.github.io/) · Code: — · [Details](../PAPERS.md#rt-2) |

<a id="section-5"></a>

## Language-guided manipulation and agents

| Paper | Focus | Official resources |
| --- | --- | --- |
| [CheckManual: A New Challenge and Benchmark for Manual-based Appliance Manipulation](https://openaccess.thecvf.com/content/CVPR2025/html/Long_CheckManual_A_New_Challenge_and_Benchmark_for_Manual-based_Appliance_Manipulation_CVPR_2025_paper.html)<br>CVPR 2025 · core | Introduces a manual-based appliance-manipulation benchmark and the ManualPlan baseline; the author repository provides setup, articulated-object assets, and code. | [Project](https://sites.google.com/view/checkmanual) · [Code](https://github.com/LYX0501/CheckManual) · [Details](../PAPERS.md#checkmanual) |
| [UniAff: A Unified Representation of Affordances for Tool Usage and Articulation with Vision-Language Models](https://arxiv.org/abs/2409.20551)<br>ICRA 2025 · core | Defines a unified representation for manipulation affordances covering articulated objects and tools, with a VLM-oriented formulation. | [Project](https://sites.google.com/view/uni-aff/home) · [Code](https://github.com/qiaojunyu/UniAff) · [Details](../PAPERS.md#uniaff) |
| [A3VLM: Actionable Articulation-Aware Vision Language Model](https://arxiv.org/abs/2406.07549)<br>CoRL 2024 · core | Uses an object-centric representation of articulation structure and affordance that can be converted to action primitives; the repository releases model and data-generation code. | Project: — · [Code](https://github.com/changhaonan/A3VLM) · [Details](../PAPERS.md#a3vlm) |
| [ManipLLM: Embodied Multimodal Large Language Model for Object-Centric Robotic Manipulation](https://openaccess.thecvf.com/content/CVPR2024/html/Li_ManipLLM_Embodied_Multimodal_Large_Language_Model_for_Object-Centric_Robotic_Manipulation_CVPR_2024_paper.html)<br>CVPR 2024 · core | Uses RGB and text prompts for affordance reasoning and end-effector pose prediction, followed by a closed-loop impedance adaptation policy. | [Project](https://sites.google.com/view/manipllm) · [Code](https://github.com/clorislili/ManipLLM) · [Details](../PAPERS.md#manipllm) |
| [SAGE: Bridging Semantic and Actionable Parts for Generalizable Manipulation of Articulated Objects](https://www.roboticsproceedings.org/rss20/p016.pdf)<br>RSS 2024 · core | Maps language-grounded semantic parts to actionable parts, derives executable policies, and uses interactive feedback after failed action steps. | [Project](https://geometry.stanford.edu/projects/sage/) · [Code (announced)](https://github.com/geng-haoran/SAGE) · [Details](../PAPERS.md#sage) |
| [VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models](https://proceedings.mlr.press/v229/huang23b.html)<br>CoRL 2023 · core | Uses language-model programs and 3D value maps to express and ground manipulation constraints in observed scenes. | [Project](https://voxposer.github.io/) · [Code](https://github.com/huangwl18/VoxPoser) · [Details](../PAPERS.md#voxposer) |
| [Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](https://arxiv.org/abs/2204.01691)<br>Conference on Robot Learning 2022 · core | Combines language-model task planning with learned skill value functions to select robot actions that are both relevant and feasible. | [Project](https://say-can.github.io/) · [Code](https://github.com/google-research/google-research/tree/master/saycan) · [Details](../PAPERS.md#saycan) |

<a id="section-6"></a>

## Affordances and active exploration

| Paper | Focus | Official resources |
| --- | --- | --- |
| [Learning Environment-Aware Affordance for 3D Articulated Object Manipulation under Occlusions](https://proceedings.neurips.cc/paper_files/paper/2023/hash/bf78fc727cf882df66e6dbc826161e86-Abstract-Conference.html)<br>NeurIPS 2023 · core | Models point-level affordance with target geometry, occluders, and robot-position constraints; its official repository includes code and data instructions. | Project: — · [Code](https://github.com/chengkaiAcademyCity/EnvAwareAfford) · [Details](../PAPERS.md#env-aware-affordance) |
| [Where2Explore: Few-shot Affordance Learning for Unseen Novel Categories of Articulated Objects](https://proceedings.neurips.cc/paper_files/paper/2023/hash/0e7e2af2e5ba822c9ad35a37b31b5dd4-Abstract-Conference.html)<br>NeurIPS 2023 · core | Uses geometric similarity to choose few-shot exploration interactions and transfer affordance knowledge to unseen articulated categories. | [Project](https://tritiumr.github.io/Where2Explore/) · [Code](https://github.com/TritiumR/Where2Explore) · [Details](../PAPERS.md#where2explore) |
| [UMPNet: Universal Manipulation Policy Network for Articulated Objects](https://ump-net.cs.columbia.edu/)<br>RA-L / ICRA 2022 · core | A single image-based policy uses self-guided exploration and a per-step Arrow-of-Time attribute for closed-loop articulated manipulation and state exploration. | [Project](https://ump-net.cs.columbia.edu/) · [Code](https://github.com/real-stanford/umpnet) · [Details](../PAPERS.md#umpnet) |
| [Act the Part: Learning Interaction Strategies for Articulated Object Part Discovery](https://openaccess.thecvf.com/content/ICCV2021/html/Gadre_Act_the_Part_Learning_Interaction_Strategies_for_Articulated_Object_Part_ICCV_2021_paper.html)<br>ICCV 2021 · core | Couples learned action selection with motion segmentation to discover articulated parts without semantic part labels. | [Project](https://atp.cs.columbia.edu/) · Code: — · [Details](../PAPERS.md#act-the-part) |
| [Where2Act: From Pixels to Actions for Articulated 3D Objects](https://openaccess.thecvf.com/content/ICCV2021/html/Mo_Where2Act_From_Pixels_to_Actions_for_Articulated_3D_Objects_ICCV_2021_paper.html)<br>ICCV 2021 · core | Predicts pixel-level actionability, interaction trajectories, and success likelihoods for pushing and pulling articulated objects from image and depth input. | Project: — · [Code](https://github.com/daerduoCarey/where2act) · [Details](../PAPERS.md#where2act) |

<a id="section-7"></a>

## Motion-aware control and manipulation

| Paper | Focus | Official resources |
| --- | --- | --- |
| [ArticuBot: Learning Universal Articulated Object Manipulation Policy via Large Scale Simulation](https://www.roboticsproceedings.org/rss21/p156.pdf)<br>RSS 2025 · core | Trains one policy in large-scale simulation for opening unseen articulated object categories and reports real-world experiments. | [Project](https://articubot.github.io/) · [Code](https://github.com/yufeiwang63/ArticuBot) · [Details](../PAPERS.md#articubot) |
| [Opening Articulated Structures in the Real World](https://arxiv.org/abs/2402.17767)<br>RSS 2025 · core | Uses opening novel articulated structures as an end-to-end mobile-manipulation testbed, integrating robot-centric perception, navigation, whole-body planning, grasping, and adaptation across real sites. | [Project](https://arjung128.github.io/opening-articulated-structures/) · [Code](https://github.com/arjung128/stretch-open) · [Details](../PAPERS.md#mosart) |
| [CenterArt: Joint Shape Reconstruction and 6-DoF Grasp Estimation of Articulated Objects](https://arxiv.org/abs/2404.14968)<br>arXiv preprint 2024 · core | Jointly predicts shape and joint codes to reconstruct articulated objects and estimate 6-DoF grasps from RGB-D scenes. | Project: — · [Code](https://github.com/Sassanmtr/CenterArt) · [Details](../PAPERS.md#centerart) |
| [FlowBotHD: History-Aware Diffuser Handling Ambiguities in Articulated Objects Manipulation](https://arxiv.org/abs/2410.07078)<br>CoRL 2024 · core | Uses a history-aware diffusion model to represent multimodal articulation hypotheses under symmetry and occlusion. | [Project](https://flowbothd.github.io/) · [Code](https://github.com/liy1shu/FlowBotHD) · [Details](../PAPERS.md#flowbothd) |
| [GAMMA: Generalizable Articulation Modeling and Manipulation for Articulated Objects](https://ieeexplore.ieee.org/document/10610652/)<br>ICRA 2024 · core | Combines articulation modeling with grasp-pose affordance and adaptively updates joint estimates during manipulation. | Project: — · [Code](https://github.com/qiaojunyu/GAMMA-ICRA2024) · [Details](../PAPERS.md#gamma) |
| [RPMArt: Towards Robust Perception and Manipulation for Articulated Objects](https://arxiv.org/abs/2403.16023)<br>IROS 2024 · core | Estimates articulation parameters and interaction points from noisy point clouds, then uses them to constrain grasping and articulated motion; the authors report synthetic-to-real transfer. | [Project](https://r-pmart.github.io/) · [Code](https://github.com/R-PMArt/rpmart) · [Details](../PAPERS.md#rpmart) |
| [FlowBot++: Learning Generalized Articulated Objects Manipulation via Articulation Projection](https://proceedings.mlr.press/v229/zhang23c/zhang23c.pdf)<br>CoRL 2023 · core | Combines dense articulation flow and per-point articulation parameters for zero-shot manipulation of novel articulated objects. | [Project](https://sites.google.com/view/flowbotpp/home) · [Code](https://github.com/harryzhangOG/flowbotpp) · [Details](../PAPERS.md#flowbot-plusplus) |
| [Sim2Real²: Actively Building Explicit Physics Model for Precise Articulated Object Manipulation](https://arxiv.org/abs/2302.10693)<br>ICRA 2023 · core | Uses a one-step interaction to construct an explicit object physics model, then plans a target joint-state trajectory with MPC; the released repository contains the three pipeline modules. | [Project](https://ttimelord.github.io/Sim2Real2-site/) · [Code](https://github.com/TTimelord/Sim2Real2) · [Details](../PAPERS.md#sim2real2) |
| [FlowBot3D: Learning 3D Articulation Flow to Manipulate Articulated Objects](https://www.roboticsproceedings.org/rss18/p018.html)<br>RSS 2022 · core | Predicts a dense point-wise motion field from a point cloud and uses it to guide analytical motion planning for articulated manipulation. | Project: — · [Code](https://github.com/r-pad/flowbot3d) · [Details](../PAPERS.md#flowbot3d) |

<a id="section-8"></a>

## Contact and tactile feedback

| Paper | Focus | Official resources |
| --- | --- | --- |
| [Vi-TacMan: Articulated Object Manipulation via Vision and Touch](https://vi-tacman.github.io/)<br>ICRA 2026 · core | Uses vision to propose a grasp and coarse direction, then uses tactile contact feedback for precise articulated manipulation without an explicit kinematic model. | [Project](https://vi-tacman.github.io/) · [Code](https://github.com/leiyaocui/Vi-TacMan) · [Details](../PAPERS.md#vitacman) |
| [Tac-Man: Tactile-Informed Prior-Free Manipulation of Articulated Objects](https://arxiv.org/abs/2403.01694)<br>IEEE Transactions on Robotics 2025 · core | Uses tactile feedback for prior-free manipulation of articulated objects, including objects with complex joints and perturbations. | [Project](https://tacman-aom.github.io/tac-man/) · [Code](https://github.com/YuyangLee/Tac-Man-Simulation) · [Details](../PAPERS.md#tacman) |

<a id="section-9"></a>

## Surveys and perspectives

| Paper | Focus | Official resources |
| --- | --- | --- |
| [3D Generation for Embodied AI and Robotic Simulation: A Survey](https://arxiv.org/abs/2604.26509)<br>arXiv 2026 · enabling | Reviews generated assets, interactive environments, and sim-to-real pipelines, distinguishing appearance, physical validity, and embodied-task evaluation. | [Project](https://3dgen4robot.github.io/) · Code: — · [Details](../PAPERS.md#survey-generation-embodied) |
| [A Survey on Vision-Language-Action Models for Embodied AI](https://arxiv.org/abs/2405.14093)<br>TNNLS 2026 · enabling | Organizes vision-language-action research into model components, low-level control policies, and high-level task planning, alongside datasets and evaluation. | [Project](https://github.com/yueen-ma/Awesome-VLA) · Code: — · [Details](../PAPERS.md#survey-vla) |
