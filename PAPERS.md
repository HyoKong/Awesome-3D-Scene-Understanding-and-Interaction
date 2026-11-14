# Complete paper index

[← Overview](README.md) · [Topic pages](#topic-directory) · [Benchmarks](BENCHMARKS.md)

Every source-checked catalog record appears here once. Links are primary publications; resource links and release status are recorded without treating missing links as evidence of absence.

## Topic directory

- [Scene and functional perception](topics/perception.md)
- [Scene reconstruction and digital twins](topics/reconstruction.md)
- [Scene generation and asset authoring](topics/generation.md)
- [Embodied agents and robotic interaction](topics/robotics.md)
- [Datasets, simulators, and benchmarks](topics/datasets.md)

## Scene and functional perception

<a id="ditr"></a>

### DITR (2026)

**[DINO in the Room: Leveraging 2D Foundation Models for 3D Segmentation](https://arxiv.org/abs/2503.18944)** — 3DV 2026 · **Enabling** · 3D backbones and representation learning.

Projects frozen 2D foundation-model features into a 3D segmentation backbone, and also studies distillation for image-free downstream inference.

[Project](https://rwthvision.github.io/ditr/) · [Code](https://github.com/RWTHVision/ditr)

Resource note: Official repository announced its code release on 2026-03-16.

Benchmark connections: scannetpp, scannet, scannet200, s3dis. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="lassm"></a>

### LaSSM (2026)

**[LaSSM: Efficient Semantic-Spatial Query Decoding via Local Aggregation and State Space Models for 3D Instance Segmentation](https://arxiv.org/abs/2602.11007)** — IEEE Transactions on Circuits and Systems for Video Technology 2026 · **Core** · Scene segmentation.

Combines superpoint-derived semantic-spatial query initialization with local aggregation and a coordinate-guided state-space decoder for 3D instance masks.

[Project](https://rayyoh.github.io/LaSSM/) · [Code](https://github.com/RayYoh/LaSSM)

Benchmark connections: scannetpp, scannet, scannet200, s3dis. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="segment-snap"></a>

### Segment–Snap (2026)

**[Geometric and Semantic Coupling for Interaction Understanding in 3D Scenes](https://arxiv.org/abs/2609.25247)** — arXiv preprint 2026 · **Core** · Functional parts, affordances and articulation.

Couples movable-part and handle predictions to estimate articulation and improve interaction-region detection in indoor scene scans.

[Project](https://hyokong.github.io/segment-snap-page/) · [Code](https://github.com/HyoKong/Segment-Snap)

Resource note: The public implementation reproduces validation experiments; competition test scores use a separate challenge entry.

Benchmark connections: Articulate3D. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="volume-transformer"></a>

### Volt (2026)

**[Volume Transformer: Revisiting Vanilla Transformers for 3D Scene Understanding](https://arxiv.org/abs/2604.19609)** — ECCV 2026 · **Enabling** · 3D backbones and representation learning.

Applies a minimally modified vanilla Transformer to volumetric patch tokens, paired with a data-efficient training recipe and multi-dataset supervision.

[Project](https://yilmazkadir.github.io/Volt/) · [Code](https://github.com/YilmazKadir/Volt)

Resource note: The author project links this official implementation. The paper is accepted to ECCV 2026 (Long Oral).

Benchmark connections: scannetpp, scannet, scannet200, scenefun3d. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-14.

<a id="articulate3d"></a>

### Articulate3D (2025)

**[Articulate3D: Holistic Understanding of 3D Scenes as Universal Scene Description](https://openaccess.thecvf.com/content/ICCV2025/html/Halacheva_Articulate3D_Holistic_Understanding_of_3D_Scenes_as_Universal_Scene_Description_ICCV_2025_paper.html)** — ICCV 2025 · **Core** · Functional parts, affordances and articulation.

Annotates indoor scenes with parts, connectivity, articulation, and executable USD structure, with scene-point-cloud prediction baselines.

[Project](https://insait-institute.github.io/articulate3d.github.io/) · [Code](https://github.com/insait-institute/USDNet)

Resource note: USDNet is the official challenge baseline, not a claimed ICCV-method release.

Checked: 2026-11-14.

<a id="sgiformer"></a>

### SGIFormer (2025)

**[SGIFormer: Semantic-guided and Geometric-enhanced Interleaving Transformer for 3D Instance Segmentation](https://arxiv.org/abs/2407.11564)** — IEEE Transactions on Circuits and Systems for Video Technology 2025 · **Core** · Scene segmentation.

Uses semantic-guided query initialization and an interleaving transformer decoder that refines queries together with scene features.

[Project](https://rayyoh.github.io/SGIFormer/) · [Code](https://github.com/RayYoh/SGIFormer)

Benchmark connections: scannetpp, scannet, scannet200, s3dis. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="sonata"></a>

### Sonata (2025)

**[Sonata: Self-Supervised Learning of Reliable Point Representations](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_Sonata_Self-Supervised_Learning_of_Reliable_Point_Representations_CVPR_2025_paper.html)** — CVPR 2025 · **Enabling** · 3D backbones and representation learning.

A self-distillation approach for point representations designed to resist geometric shortcuts and support downstream 3D perception through lightweight task heads.

[Project](https://xywu.me/sonata) · [Code](https://github.com/facebookresearch/sonata)

Benchmark connections: scannetpp, scannet, scannet200, s3dis, arkitscenes. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="conceptgraphs"></a>

### ConceptGraphs (2024)

**[ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning](https://arxiv.org/abs/2309.16650)** — ICRA 2024 · **Core** · Open-vocabulary scenes and language grounding.

Builds open-vocabulary 3D scene graphs from RGB-D observations for downstream reasoning and planning.

[Project](https://concept-graphs.github.io/) · [Code](https://github.com/concept-graphs/concept-graphs)

Benchmark connections: scannet. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="oa-cnns"></a>

### OA-CNNs (2024)

**[OA-CNNs: Omni-Adaptive Sparse CNNs for 3D Semantic Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Peng_OA-CNNs_Omni-Adaptive_Sparse_CNNs_for_3D_Semantic_Segmentation_CVPR_2024_paper.html)** — CVPR 2024 · **Enabling** · 3D backbones and representation learning.

Revisits sparse CNNs with adaptive receptive fields and adaptive relations for 3D semantic segmentation.

Project: — · [Code](https://github.com/Pointcept/Pointcept)

Resource note: The paper identifies Pointcept as its code base; no separate OA-CNNs repository was verified.

Benchmark connections: scannetpp, scannet. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="oneformer3d"></a>

### OneFormer3D (2024)

**[OneFormer3D: One Transformer for Unified Point Cloud Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Kolodiazhnyi_OneFormer3D_One_Transformer_for_Unified_Point_Cloud_Segmentation_CVPR_2024_paper.html)** — CVPR 2024 · **Core** · Scene segmentation.

Unifies semantic, instance, and panoptic point-cloud segmentation in one transformer model.

Project: — · [Code](https://github.com/filaPro/oneformer3d)

Benchmark connections: scannet, scannet200, s3dis. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="opdmulti"></a>

### OPDMulti (2024)

**[OPDMulti: Openable Part Detection for Multiple Objects](https://3dlg-hcvc.github.io/OPDMulti/)** — 3DV 2024 · **Core** · Functional parts, affordances and articulation.

Extends openable-part segmentation and motion-parameter estimation to single-view images containing multiple objects.

[Project](https://3dlg-hcvc.github.io/OPDMulti/) · [Code](https://github.com/3dlg-hcvc/OPDMulti)

Resource note: Authors' project page and release.

Checked: 2026-11-14.

<a id="open3dis"></a>

### Open3DIS (2024)

**[Open3DIS: Open-Vocabulary 3D Instance Segmentation with 2D Mask Guidance](https://openaccess.thecvf.com/content/CVPR2024/html/Nguyen_Open3DIS_Open-Vocabulary_3D_Instance_Segmentation_with_2D_Mask_Guidance_CVPR_2024_paper.html)** — CVPR 2024 · **Core** · Open-vocabulary scenes and language grounding.

Combines 2D masks with class-agnostic 3D proposals for open-vocabulary 3D instances.

[Project](https://open3dis.github.io/) · [Code](https://github.com/VinAIResearch/Open3DIS)

Benchmark connections: scannet200, s3dis, scannetpp. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="multi-dataset-point-prompt-training"></a>

### PPT (2024)

**[Towards Large-scale 3D Representation Learning with Multi-dataset Point Prompt Training](https://openaccess.thecvf.com/content/CVPR2024/papers/Wu_Towards_Large-scale_3D_Representation_Learning_with_Multi-dataset_Point_Prompt_Training_CVPR_2024_paper.pdf)** — CVPR 2024 · **Enabling** · 3D backbones and representation learning.

Trains point-cloud representations across datasets with point prompts and releases its implementation in Pointcept.

Project: — · [Code](https://github.com/Pointcept/Pointcept)

Resource note: The official CVPR PDF is live; the previously constructed HTML slug is not.

Benchmark connections: scannet, scannet200, s3dis. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="ptv3"></a>

### PTv3 (2024)

**[Point Transformer V3: Simpler, Faster, Stronger](https://openaccess.thecvf.com/content/CVPR2024/html/Wu_Point_Transformer_V3_Simpler_Faster_Stronger_CVPR_2024_paper.html)** — CVPR 2024 · **Enabling** · 3D backbones and representation learning.

A scalable point-cloud backbone with released ScanNet, ScanNet200, and S3DIS experiments.

Project: — · [Code](https://github.com/Pointcept/PointTransformerV3)

Benchmark connections: scannet, scannet200, s3dis. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="scenefun3d"></a>

### SceneFun3D (2024)

**[SceneFun3D: Fine-Grained Functionality and Affordance Understanding in 3D Scenes](https://alexdelitzas.github.io/assets/pdf/SceneFun3D.pdf)** — CVPR 2024 · **Core** · Functional parts, affordances and articulation.

Connects functional-element masks, affordance labels, task descriptions, and interaction motions in real indoor scenes.

[Project](https://scenefun3d.github.io/) · [Toolkit](https://github.com/SceneFun3D/scenefun3d)

Resource note: The official code link provides the data toolkit and evaluation utilities; it is not a claim that every proposed baseline is implemented there.

Benchmark connections: SceneFun3D. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-14.

<a id="context-aware-classifier"></a>

### CAC (2023)

**[Learning Context-Aware Classifier for Semantic Segmentation](https://arxiv.org/abs/2303.11633)** — AAAI 2023 · **Core** · Scene segmentation.

Learns a data-conditioned classifier that adapts to the latent feature distribution while remaining model-agnostic.

Project: — · [Code](https://github.com/tianzhuotao/CAC)

Resource note: The leaderboard motivates inclusion; the primary paper is a general semantic-segmentation method rather than an articulation-specific work.

Benchmark connections: scannetpp. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="conceptfusion"></a>

### ConceptFusion (2023)

**[ConceptFusion: Open-set Multimodal 3D Mapping](https://arxiv.org/abs/2302.07241)** — RSS 2023 · **Core** · Open-vocabulary scenes and language grounding.

Builds open-set multimodal 3D maps queryable by text, click, image, audio, or geometry.

[Project](https://concept-fusion.github.io/) · [Code](https://github.com/concept-fusion/concept-fusion)

Resource note: The official repository calls itself a WIP release and documents deviations from the paper; link it as released code with this caveat.

Checked: 2026-11-13.

<a id="gapartnet"></a>

### GAPartNet (2023)

**[GAPartNet: Cross-Category Domain-Generalizable Object Perception and Manipulation via Generalizable and Actionable Parts](https://openaccess.thecvf.com/content/CVPR2023/html/Geng_GAPartNet_Cross-Category_Domain-Generalizable_Object_Perception_and_Manipulation_via_Generalizable_and_CVPR_2023_paper.html)** — CVPR 2023 · **Core** · Functional parts, affordances and articulation.

Defines transferable actionable parts for cross-category part segmentation, pose estimation, and manipulation.

[Project](https://pku-epic.github.io/GAPartNet/) · [Code](https://github.com/PKU-EPIC/GAPartNet)

Resource note: Authors' project page and release.

Checked: 2026-11-14.

<a id="mask3d"></a>

### Mask3D (2023)

**[Mask3D: Mask Transformer for 3D Semantic Instance Segmentation](https://arxiv.org/abs/2210.03105)** — ICRA 2023 · **Core** · Scene segmentation.

Uses transformer instance queries to predict semantic instance masks from point clouds.

[Project](https://jonasschult.github.io/Mask3D/) · [Code](https://github.com/JonasSchult/Mask3D)

Benchmark connections: scannet, scannet200, s3dis. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="octformer"></a>

### OctFormer (2023)

**[OctFormer: Octree-based Transformers for 3D Point Clouds](https://arxiv.org/abs/2305.03045)** — SIGGRAPH (ACM TOG) 2023 · **Enabling** · 3D backbones and representation learning.

Uses octree attention with fixed-size local windows to make transformer processing scalable for point-cloud segmentation and detection.

[Project](https://wang-ps.github.io/octformer) · [Code](https://github.com/octree-nn/octformer)

Benchmark connections: scannetpp, scannet200. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="openmask3d"></a>

### OpenMask3D (2023)

**[OpenMask3D: Open-Vocabulary 3D Instance Segmentation](https://openreview.net/forum?id=ZB9KZ0JqNv)** — NeurIPS 2023 · **Core** · Open-vocabulary scenes and language grounding.

Assigns open-vocabulary labels to 3D instance masks using multi-view images and vision-language features.

[Project](https://openmask3d.github.io/) · [Code](https://github.com/OpenMask3D/openmask3d)

Benchmark connections: scannet200. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="openscene"></a>

### OpenScene (2023)

**[OpenScene: 3D Scene Understanding With Open Vocabularies](https://openaccess.thecvf.com/content/CVPR2023/html/Peng_OpenScene_3D_Scene_Understanding_With_Open_Vocabularies_CVPR_2023_paper.html)** — CVPR 2023 · **Core** · Open-vocabulary scenes and language grounding.

Transfers 2D vision-language features into 3D for open-vocabulary scene understanding.

Project: — · [Code](https://github.com/pengsongyou/openscene)

Resource note: CVPR 2023 is confirmed by the official proceedings and author repository; the historic project-page endpoint currently returns 404, so remove it rather than substituting an unverified page.

Benchmark connections: scannet. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="partslip"></a>

### PartSLIP (2023)

**[PartSLIP: Low-Shot Part Segmentation for 3D Point Clouds via Pretrained Image-Language Models](https://openaccess.thecvf.com/content/CVPR2023/html/Liu_PartSLIP_Low-Shot_Part_Segmentation_for_3D_Point_Clouds_via_Pretrained_CVPR_2023_paper.html)** — CVPR 2023 · **Core** · Functional parts, affordances and articulation.

Uses pretrained image-language models to support low-shot 3D part segmentation.

[Project](https://colin97.github.io/PartSLIP_page/) · [Code](https://drive.google.com/drive/folders/19j6PZfW8TDQ1ifHZwHIhn6X4BHjYRFCL)

Resource note: The author project labels this Google Drive release as Code. Do not replace it with the unrelated/nonexistent colin97 GitHub URL.

Checked: 2026-11-13.

<a id="spformer"></a>

### SPFormer (2023)

**[Superpoint Transformer for 3D Scene Instance Segmentation](https://arxiv.org/abs/2211.15766)** — AAAI 2023 · **Core** · Scene segmentation.

Forms superpoints and directly predicts instance masks through superpoint cross-attention and query vectors, without an intermediate aggregation stage.

Project: — · [Code](https://github.com/sunjiahao1999/SPFormer)

Resource note: Distinct from the ICCV 2023 semantic-segmentation Superpoint Transformer already in the catalogue.

Benchmark connections: scannetpp, scannet, s3dis. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="superpoint-transformer"></a>

### SPT (2023)

**[Efficient 3D Semantic Segmentation with Superpoint Transformer](https://openaccess.thecvf.com/content/ICCV2023/html/Robert_Efficient_3D_Semantic_Segmentation_with_Superpoint_Transformer_ICCV_2023_paper.html)** — ICCV 2023 · **Enabling** · 3D backbones and representation learning.

Uses a transformer over hierarchical superpoints for efficient semantic segmentation of large 3D scenes.

[Project](https://drprojects.github.io/superpoint-transformer-site/) · [Code](https://github.com/drprojects/superpoint_transformer)

Benchmark connections: s3dis. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="opd"></a>

### OPD (2022)

**[OPD: Single-view 3D Openable Part Detection](https://3dlg-hcvc.github.io/OPD/)** — ECCV 2022 · **Core** · Functional parts, affordances and articulation.

Localizes openable parts and predicts their motion type, 3D axis, and origin from a single image.

[Project](https://3dlg-hcvc.github.io/OPD/) · [Code](https://github.com/3dlg-hcvc/OPD)

Resource note: Authors' project page and release.

Checked: 2026-11-14.

<a id="pointnext"></a>

### PointNeXt (2022)

**[PointNeXt: Revisiting PointNet++ with Improved Training and Scaling Strategies](https://proceedings.neurips.cc/paper_files/paper/2022/hash/9318763d049edf9a1f2779b2a59911d3-Abstract.html)** — NeurIPS 2022 · **Enabling** · 3D backbones and representation learning.

Studies training and scaling of PointNet++-style networks for point-cloud tasks.

Project: — · [Code](https://github.com/guochengqian/pointnext)

Benchmark connections: s3dis. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="point-transformer-v2"></a>

### PTv2 (2022)

**[Point Transformer V2: Grouped Vector Attention and Partition-based Pooling](https://arxiv.org/abs/2210.05666)** — NeurIPS 2022 · **Enabling** · 3D backbones and representation learning.

Introduces grouped vector attention and partition-based pooling for scalable point-cloud understanding.

Project: — · [Code](https://github.com/Gofinge/PointTransformerV2)

Benchmark connections: scannet, s3dis. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="softgroup"></a>

### SoftGroup (2022)

**[SoftGroup for 3D Instance Segmentation on Point Clouds](https://openaccess.thecvf.com/content/CVPR2022/html/Vu_SoftGroup_for_3D_Instance_Segmentation_on_Point_Clouds_CVPR_2022_paper.html)** — CVPR 2022 · **Core** · Scene segmentation.

Uses bottom-up soft grouping followed by top-down refinement for 3D instances.

Project: — · [Code](https://github.com/thangvubk/SoftGroup)

Benchmark connections: scannet, s3dis, scannetpp. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="stratified-transformer"></a>

### Stratified Transformer (2022)

**[Stratified Transformer for 3D Point Cloud Segmentation](https://openaccess.thecvf.com/content/CVPR2022/html/Lai_Stratified_Transformer_for_3D_Point_Cloud_Segmentation_CVPR_2022_paper.html)** — CVPR 2022 · **Enabling** · 3D backbones and representation learning.

Models local and long-range point interactions for 3D semantic segmentation.

Project: — · [Code](https://github.com/dvlab-research/Stratified-Transformer)

Benchmark connections: scannet, s3dis. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="captra"></a>

### CAPTRA (2021)

**[CAPTRA: CAtegory-Level Pose Tracking for Rigid and Articulated Objects From Point Clouds](https://openaccess.thecvf.com/content/ICCV2021/html/Weng_CAPTRA_CAtegory-Level_Pose_Tracking_for_Rigid_and_Articulated_Objects_From_ICCV_2021_paper.html)** — ICCV 2021 · **Core** · Articulated pose and tracking.

Tracks per-part articulated pose online from point-cloud sequences and previous-frame estimates.

[Project](https://yijiaweng.github.io/CAPTRA/) · [Code](https://github.com/HalfSummer11/CAPTRA)

Resource note: Repository identifies itself as the official PyTorch implementation and links the author project page.

Checked: 2026-11-13.

<a id="hais"></a>

### HAIS (2021)

**[Hierarchical Aggregation for 3D Instance Segmentation](https://openaccess.thecvf.com/content/ICCV2021/html/Chen_Hierarchical_Aggregation_for_3D_Instance_Segmentation_ICCV_2021_paper.html)** — ICCV 2021 · **Core** · Scene segmentation.

A bottom-up point-cloud instance method using point and set aggregation.

Project: — · [Code](https://github.com/hustvl/HAIS)

Benchmark connections: scannet, s3dis. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="point-transformer"></a>

### PTv1 (2021)

**[Point Transformer](https://openaccess.thecvf.com/content/ICCV2021/html/Zhao_Point_Transformer_ICCV_2021_paper.html)** — ICCV 2021 · **Enabling** · 3D backbones and representation learning.

Uses vector attention for point-cloud semantic segmentation.

Project: — · [Code](https://github.com/POSTECH-CVLab/point-transformer)

Benchmark connections: s3dis. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="ancsh"></a>

### ANCSH (2020)

**[Category-Level Articulated Object Pose Estimation](https://openaccess.thecvf.com/content_CVPR_2020/html/Li_Category-Level_Articulated_Object_Pose_Estimation_CVPR_2020_paper.html)** — CVPR 2020 · **Core** · Articulated pose and tracking.

Estimates category-level articulated pose from a single depth image through part segmentation, canonical coordinates, and joint parameters.

[Project](https://articulated-pose.github.io/) · [Code](https://github.com/dragonlong/articulated-pose)

Resource note: The authors' repository calls itself the implementation of ANCSH and links its project page.

Checked: 2026-11-13.

<a id="pointgroup"></a>

### PointGroup (2020)

**[PointGroup: Dual-Set Point Grouping for 3D Instance Segmentation](https://openaccess.thecvf.com/content_CVPR_2020/html/Jiang_PointGroup_Dual-Set_Point_Grouping_for_3D_Instance_Segmentation_CVPR_2020_paper.html)** — CVPR 2020 · **Core** · Scene segmentation.

Groups points with predicted offsets and dual sets for 3D instance masks.

Project: — · [Code](https://github.com/dvlab-research/PointGroup)

Benchmark connections: scannet, s3dis. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="scanrefer"></a>

### ScanRefer (2020)

**[ScanRefer: 3D Object Localization in RGB-D Scans using Natural Language](https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/597_ECCV_2020_paper.php)** — ECCV 2020 · **Core** · Open-vocabulary scenes and language grounding.

Pairs natural-language descriptions with object localization in ScanNet RGB-D scenes.

[Project](https://daveredrum.github.io/ScanRefer/) · [Code](https://github.com/daveredrum/ScanRefer)

Benchmark connections: scannet. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-14.

<a id="shape2motion"></a>

### Shape2Motion (2019)

**[Shape2Motion: Joint Analysis of Motion Parts and Attributes From 3D Shapes](https://openaccess.thecvf.com/content_CVPR_2019/html/Wang_Shape2Motion_Joint_Analysis_of_Motion_Parts_and_Attributes_From_3D_CVPR_2019_paper.html)** — CVPR 2019 · **Core** · Functional parts, affordances and articulation.

Jointly segments movable parts and estimates their motion attributes from a single 3D point cloud.

Project: — · [Code](https://github.com/wangxiaogang866/Shape2Motion)

Resource note: Repository identifies itself as the paper's code repository and includes train/test instructions.

Checked: 2026-11-13.

<a id="superpoint-graph"></a>

### SPG (2018)

**[Large-Scale Point Cloud Semantic Segmentation With Superpoint Graphs](https://openaccess.thecvf.com/content_cvpr_2018/html/Landrieu_Large-Scale_Point_Cloud_CVPR_2018_paper.html)** — CVPR 2018 · **Enabling** · 3D backbones and representation learning.

Uses geometric partitioning and graph learning over superpoints for large 3D point clouds.

Project: — · [Code](https://github.com/loicland/superpoint_graph)

Benchmark connections: s3dis. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="pointnet"></a>

### PointNet (2017)

**[PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation](https://openaccess.thecvf.com/content_cvpr_2017/html/Qi_PointNet_Deep_Learning_CVPR_2017_paper.html)** — CVPR 2017 · **Enabling** · 3D backbones and representation learning.

Introduces a permutation-invariant point-set network for classification and segmentation.

[Project](https://stanford.edu/~rqi/pointnet/) · [Code](https://github.com/charlesq34/pointnet)

Checked: 2026-11-13.

<a id="pointnet-plus-plus"></a>

### PointNet++ (2017)

**[PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space](https://papers.nips.cc/paper_files/paper/2017/hash/d8bf84be3800d12f74d8b05e9b89836f-Abstract.html)** — NeurIPS 2017 · **Enabling** · 3D backbones and representation learning.

Extends PointNet with hierarchical local feature learning on metric-space point sets.

[Project](https://stanford.edu/~rqi/pointnet2/) · [Code](https://github.com/charlesq34/pointnet2)

Checked: 2026-11-13.


## Scene reconstruction and digital twins

<a id="articulation-in-motion"></a>

### AiM (2026)

**[Articulation in Motion: Prior-free Part Mobility Analysis for Articulated Objects By Dynamic-Static Disentanglement](https://arxiv.org/abs/2603.02910)** — arXiv preprint 2026 · **Core** · Multi-state and interaction-based reconstruction.

Uses an interaction video and start-state scan for part decomposition, kinematics, and an interactive digital replica.

[Project](https://haoai-1997.github.io/AiM/) · Code: —

Checked: 2026-11-13.

<a id="arthoi"></a>

### ArtHOI (2026)

**[ArtHOI: Articulated Human-Object Interaction Synthesis by 4D Reconstruction from Video Priors](https://arxiv.org/abs/2603.04338)** — arXiv preprint 2026 · **Core** · Multi-state and interaction-based reconstruction.

Uses monocular video priors and initial 3D assets for articulated human-object interaction synthesis by 4D reconstruction.

[Project](https://arthoi.github.io/) · Code: —

Checked: 2026-11-13.

<a id="articulat3d"></a>

### Articulat3D (2026)

**[Articulat3D: Reconstructing Articulated Digital Twins From Monocular Videos with Geometric and Motion Constraints](https://arxiv.org/abs/2603.11606)** — arXiv preprint 2026 · **Core** · Visual digital twins and executable structure.

Builds articulated digital twins from casually captured monocular video using geometric and motion constraints.

[Project](https://maxwell-zhao.github.io/Articulat3D) · Code: —

Checked: 2026-11-13.

<a id="react3d"></a>

### REACT3D (2026)

**[REACT3D: Recovering Articulations for Interactive Physical 3D Scenes](https://doi.org/10.1109/LRA.2026.3674028)** — IEEE Robotics and Automation Letters 2026 · **Core** · Articulation recovery from static assets.

Converts static indoor scenes into simulation-ready interactive replicas through detection, articulation inference, completion, and assembly.

[Project](https://react3d.github.io/) · [Code](https://github.com/troyehuang/REACT3D)

Resource note: Official project page exposes code; repository labels source release.

Checked: 2026-11-13.

<a id="s2o"></a>

### S2O (2026)

**[S2O: Static to Openable Enhancement for Articulated 3D Objects](https://openaccess.thecvf.com/content/WACV2026/html/Iliash_S2O_Static_to_Openable_Enhancement_for_Articulated_3D_Objects_WACV_2026_paper.html)** — WACV 2026 · **Core** · Articulation recovery from static assets.

Defines static-to-openable enhancement: part detection, motion prediction, and interior completion from static 3D assets.

[Project](https://3dlg-hcvc.github.io/s2o/) · [Code](https://github.com/3dlg-hcvc/s2o)

Resource note: Repository links project page and describes released code/data.

Checked: 2026-11-13.

<a id="survey-4d-spatial"></a>

### 4D Spatial Intelligence Survey (2025)

**[Reconstructing 4D Spatial Intelligence: A Survey](https://arxiv.org/abs/2507.21045)** — arXiv 2025 · **Enabling** · Surveys and perspectives.

Reviews reconstruction across spatial attributes, scene components, dynamic scenes, interaction, and physical constraints.

[Project](https://github.com/yukangcao/Awesome-4D-Spatial-Intelligence) · Code: —

Resource note: Survey reference; a resource collection is not labeled as implementation code.

Checked: 2026-11-14.

<a id="drawer"></a>

### DRAWER (2025)

**[DRAWER: Digital Reconstruction and Articulation With Environment Realism](https://openaccess.thecvf.com/content/CVPR2025/html/Xia_DRAWER_Digital_Reconstruction_and_Articulation_With_Environment_Realism_CVPR_2025_paper.html)** — CVPR 2025 · **Core** · Visual digital twins and executable structure.

Converts video of a static scene into an interactive environment with reconstructed objects and articulated doors.

[Project](https://xiahongchi.github.io/DRAWER/) · [Code](https://github.com/xiahongchi/DRAWER)

Checked: 2026-11-13.

<a id="magicarticulate"></a>

### MagicArticulate (2025)

**[MagicArticulate: Make Your 3D Models Articulation-Ready](https://openaccess.thecvf.com/content/CVPR2025/html/Song_MagicArticulate_Make_Your_3D_Models_Articulation-Ready_CVPR_2025_paper.html)** — CVPR 2025 · **Core** · Articulation recovery from static assets.

Adds structure and motion to static 3D models and releases Articulation-XL2.0 data.

[Project](https://chaoyuesong.github.io/MagicArticulate/) · [Code](https://github.com/Seed3D/MagicArticulate)

Benchmark connections: articulation-xl2. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-14.

<a id="monst3r"></a>

### MonST3R (2025)

**[MonST3R: A Simple Approach for Estimating Geometry in the Presence of Motion](https://arxiv.org/abs/2410.03825)** — ICLR 2025 · **Core** · Dynamic scene reconstruction.

Estimates per-timestep geometry directly from dynamic scenes, extending point-map reconstruction beyond a static-scene assumption.

[Project](https://monst3r-project.github.io/) · [Code](https://github.com/Junyi42/monst3r)

Resource note: The official repository identifies the ICLR 2025 paper and code.

Checked: 2026-11-14.

<a id="partrm"></a>

### PartRM (2025)

**[PartRM: Modeling Part-Level Dynamics with Large Cross-State Reconstruction Model](https://openaccess.thecvf.com/content/CVPR2025/html/Gao_PartRM_Modeling_Part-Level_Dynamics_with_Large_Cross-State_Reconstruction_Model_CVPR_2025_paper.html)** — CVPR 2025 · **Core** · Multi-state and interaction-based reconstruction.

Models appearance, geometry, and part-level motion from one image plus user-specified drags.

[Project](https://partrm.c7w.tech/) · [Code](https://github.com/GasaiYU/PartRM)

Checked: 2026-11-13.

<a id="real2code"></a>

### Real2Code (2025)

**[Real2Code: Reconstruct Articulated Objects via Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/hash/028fcbcf85435d39a40c4d61b42c99a4-Abstract-Conference.html)** — ICLR 2025 · **Core** · Visual digital twins and executable structure.

Reconstructs parts from visual observations, including multi-view RGB, and predicts articulation code from oriented bounding boxes using an LLM.

Project: — · [Code](https://github.com/MandiZhao/real2code)

Resource note: Official code repository found; no separate project page verified.

Checked: 2026-11-13.

<a id="vggt"></a>

### VGGT (2025)

**[VGGT: Visual Geometry Grounded Transformer](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.html)** — CVPR 2025 · **Core** · Feed-forward scene reconstruction.

Uses a feed-forward transformer to infer camera parameters, point maps, depth maps, and 3D point tracks from one or many views.

[Project](https://vggt-omega.github.io/) · [Code](https://github.com/facebookresearch/vggt)

Resource note: The CVPR paper and author repository release code and models.

Checked: 2026-11-14.

<a id="videoartgs"></a>

### VideoArtGS (2025)

**[VideoArtGS: Building Digital Twins of Articulated Objects from Monocular Video](https://arxiv.org/abs/2509.17647)** — arXiv preprint 2025 · **Core** · Multi-state and interaction-based reconstruction.

Targets geometry, part segmentation, and articulation for digital twins from monocular video.

[Project](https://videoartgs.github.io) · Code: —

Checked: 2026-11-13.

<a id="four-d-gaussian-splatting"></a>

### 4D Gaussian Splatting (2024)

**[4D Gaussian Splatting for Real-Time Dynamic Scene Rendering](https://openaccess.thecvf.com/content/CVPR2024/html/Wu_4D_Gaussian_Splatting_for_Real-Time_Dynamic_Scene_Rendering_CVPR_2024_paper.html)** — CVPR 2024 · **Core** · Dynamic scene reconstruction.

Models a dynamic scene with a canonical 3D Gaussian representation and learned temporal deformation for efficient real-time rendering.

Project: — · [Code](https://github.com/hustvl/4DGaussians)

Resource note: The author repository is linked from the public CVPR 2024 release.

Checked: 2026-11-14.

<a id="digital-twin-art"></a>

### DigitalTwinArt (2024)

**[Neural Implicit Representation for Building Digital Twins of Unknown Articulated Objects](https://openaccess.thecvf.com/content/CVPR2024/html/Weng_Neural_Implicit_Representation_for_Building_Digital_Twins_of_Unknown_Articulated_CVPR_2024_paper.html)** — CVPR 2024 · **Core** · Multi-state and interaction-based reconstruction.

Optimizes part geometry, segmentation, and joints from two RGB-D scans in different states.

[Project](https://nvlabs.github.io/DigitalTwinArt/) · [Code](https://github.com/NVlabs/DigitalTwinArt)

Checked: 2026-11-13.

<a id="dust3r"></a>

### DUSt3R (2024)

**[DUSt3R: Geometric 3D Vision Made Easy](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_DUSt3R_Geometric_3D_Vision_Made_Easy_CVPR_2024_paper.html)** — CVPR 2024 · **Core** · Feed-forward scene reconstruction.

Predicts dense 2D-to-3D point maps from uncalibrated image collections, supporting camera recovery and dense scene reconstruction through global alignment.

[Project](https://dust3r.europe.naverlabs.com/) · [Code](https://github.com/naver/dust3r)

Resource note: The official repository provides code and pretrained models.

Checked: 2026-11-14.

<a id="mast3r"></a>

### MASt3R (2024)

**[Grounding Image Matching in 3D with MASt3R](https://arxiv.org/abs/2406.09756)** — ECCV 2024 · **Core** · Feed-forward scene reconstruction.

Adds dense local matching, metric point maps, and scalable global alignment to the DUSt3R reconstruction framework.

[Project](https://europe.naverlabs.com/research/publications/grounding-image-matching-in-3d-with-mast3r/) · [Code](https://github.com/naver/mast3r)

Resource note: Naver Labs Europe lists the ECCV 2024 publication and official implementation.

Checked: 2026-11-14.

<a id="reacto"></a>

### REACTO (2024)

**[REACTO: Reconstructing Articulated Objects from a Single Video](https://openaccess.thecvf.com/content/CVPR2024/html/Song_REACTO_Reconstructing_Articulated_Objects_from_a_Single_Video_CVPR_2024_paper.html)** — CVPR 2024 · **Core** · Multi-state and interaction-based reconstruction.

Reconstructs general articulated objects from one video with rigging and motion-aware component modeling.

[Project](https://chaoyuesong.github.io/REACTO/) · Code: —

Checked: 2026-11-13.

<a id="splatam"></a>

### SplaTAM (2024)

**[SplaTAM: Splat, Track & Map 3D Gaussians for Dense RGB-D SLAM](https://openaccess.thecvf.com/content/CVPR2024/html/Keetha_SplaTAM_Splat_Track__Map_3D_Gaussians_for_Dense_RGB-D_CVPR_2024_paper.html)** — CVPR 2024 · **Core** · Incremental reconstruction, SLAM and mapping.

Uses an online RGB-D tracking-and-mapping pipeline with a 3D Gaussian scene map optimized by differentiable rendering.

[Project](https://spla-tam.github.io/) · [Code](https://github.com/spla-tam/SplaTAM)

Resource note: The paper and project page identify the public code release.

Checked: 2026-11-14.

<a id="urdformer"></a>

### URDFormer (2024)

**[URDFormer: A Pipeline for Constructing Articulated Simulation Environments from Real-World Images](https://urdformer.github.io/)** — RSS 2024 · **Core** · Visual digital twins and executable structure.

Predicts a URDF from a single real-world image using localized part boxes and predefined meshes; supports simulation and policy training.

[Project](https://urdformer.github.io/) · [Code](https://github.com/WEIRDLabUW/urdformer)

Resource note: Official project and code release located.

Checked: 2026-11-13.

<a id="gaussian-splatting"></a>

### 3D Gaussian Splatting (2023)

**[3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://arxiv.org/abs/2308.04079)** — ACM Transactions on Graphics (SIGGRAPH) 2023 · **Core** · Neural scene representations and surfaces.

Represents a captured scene as optimized anisotropic 3D Gaussians with visibility-aware splatting for real-time radiance-field rendering.

[Project](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) · [Code](https://github.com/graphdeco-inria/gaussian-splatting)

Resource note: A visual radiance representation; downstream semantics, topology, or collision geometry require additional modeling choices.

Checked: 2026-11-14.

<a id="go-slam"></a>

### GO-SLAM (2023)

**[GO-SLAM: Global Optimization for Consistent 3D Instant Reconstruction](https://arxiv.org/abs/2309.02436)** — ICCV 2023 · **Core** · Incremental reconstruction, SLAM and mapping.

Combines pose estimation, loop closing, and continuous surface updates to improve global consistency in dense visual SLAM.

Project: — · [Code](https://github.com/youmi-zym/GO-SLAM)

Resource note: The author repository labels itself as the ICCV 2023 implementation.

Checked: 2026-11-14.

<a id="neuralangelo"></a>

### Neuralangelo (2023)

**[Neuralangelo: High-Fidelity Neural Surface Reconstruction](https://openaccess.thecvf.com/content/CVPR2023/html/Li_Neuralangelo_High-Fidelity_Neural_Surface_Reconstruction_CVPR_2023_paper.html)** — CVPR 2023 · **Core** · Neural scene representations and surfaces.

Reconstructs high-fidelity surfaces from RGB images through neural volume rendering without requiring auxiliary depth or segmentation data.

Project: — · [Code](https://github.com/NVlabs/neuralangelo)

Resource note: The author repository identifies itself as the official CVPR 2023 implementation.

Checked: 2026-11-14.

<a id="paris"></a>

### PARIS (2023)

**[PARIS: Part-level Reconstruction and Motion Analysis for Articulated Objects](https://openaccess.thecvf.com/content/ICCV2023/html/Liu_PARIS_Part-level_Reconstruction_and_Motion_Analysis_for_Articulated_Objects_ICCV_2023_paper.html)** — ICCV 2023 · **Core** · Multi-state and interaction-based reconstruction.

Recovers part-level shape, appearance, and motion from multi-view observations in two states.

[Project](https://3dlg-hcvc.github.io/paris/) · [Code](https://github.com/3dlg-hcvc/paris)

Resource note: Author project and official implementation repository.

Checked: 2026-11-13.

<a id="ditto"></a>

### Ditto (2022)

**[Ditto: Building Digital Twins of Articulated Objects From Interaction](https://openaccess.thecvf.com/content/CVPR2022/html/Jiang_Ditto_Building_Digital_Twins_of_Articulated_Objects_From_Interaction_CVPR_2022_paper.html)** — CVPR 2022 · **Core** · Multi-state and interaction-based reconstruction.

Uses visual observations before and after interaction to recover part geometry and articulation.

[Project](https://ut-austin-rpl.github.io/Ditto/) · [Code](https://github.com/UT-Austin-RPL/Ditto)

Resource note: CVPR links the project; repository identifies released code.

Checked: 2026-11-13.

<a id="instant-ngp"></a>

### Instant-NGP (2022)

**[Instant Neural Graphics Primitives with a Multiresolution Hash Encoding](https://doi.org/10.1145/3528223.3530127)** — ACM Transactions on Graphics (SIGGRAPH) 2022 · **Enabling** · Neural scene representations and surfaces.

Introduces a multiresolution hash encoding that makes neural graphics primitives, including NeRF scene fitting, substantially more efficient.

[Project](https://nvlabs.github.io/instant-ngp/) · [Code](https://github.com/NVlabs/instant-ngp)

Resource note: A general neural-graphics primitive framework included for its canonical scene-representation implementation.

Checked: 2026-11-14.

<a id="mipnerf360"></a>

### Mip-NeRF 360 (2022)

**[Mip-NeRF 360: Unbounded Anti-Aliased Neural Radiance Fields](https://openaccess.thecvf.com/content/CVPR2022/html/Barron_Mip-NeRF_360_Unbounded_Anti-Aliased_Neural_Radiance_Fields_CVPR_2022_paper.html)** — CVPR 2022 · **Core** · Neural scene representations and surfaces.

Extends neural radiance fields to unbounded scenes with anti-aliased rendering and an explicit distortion regularizer.

[Project](https://jonbarron.info/mipnerf360/) · [Code](https://github.com/google-research/multinerf)

Resource note: The representation targets image synthesis and depth structure from captured scenes, rather than semantic or physical scene editing.

Checked: 2026-11-14.

<a id="nice-slam"></a>

### NICE-SLAM (2022)

**[NICE-SLAM: Neural Implicit Scalable Encoding for SLAM](https://openaccess.thecvf.com/content/CVPR2022/html/Zhu_NICE-SLAM_Neural_Implicit_Scalable_Encoding_for_SLAM_CVPR_2022_paper.html)** — CVPR 2022 · **Core** · Incremental reconstruction, SLAM and mapping.

Uses a hierarchical grid-based neural implicit representation for scalable online dense RGB-D SLAM.

Project: — · [Code](https://github.com/cvg/nice-slam)

Resource note: The CVPR page and repository identify the release. The historical project-page URL reported by the paper returned 404 during this validation pass, so it is intentionally omitted.

Checked: 2026-11-14.

<a id="dnerf"></a>

### D-NeRF (2021)

**[D-NeRF: Neural Radiance Fields for Dynamic Scenes](https://openaccess.thecvf.com/content/CVPR2021/html/Pumarola_D-NeRF_Neural_Radiance_Fields_for_Dynamic_Scenes_CVPR_2021_paper.html)** — CVPR 2021 · **Core** · Dynamic scene reconstruction.

Extends neural radiance fields with a learned deformation field for rendering non-rigidly moving scenes over time.

[Project](https://www.albertpumarola.com/research/D-NeRF/index.html) · [Code](https://github.com/albertpumarola/D-NeRF)

Resource note: This reconstructs a time-varying visual representation and should not be read as recovering physical articulation parameters.

Checked: 2026-11-14.

<a id="imap"></a>

### iMAP (2021)

**[iMAP: Implicit Mapping and Positioning in Real-Time](https://openaccess.thecvf.com/content/ICCV2021/html/Sucar_iMAP_Implicit_Mapping_and_Positioning_in_Real-Time_ICCV_2021_paper.html)** — ICCV 2021 · **Core** · Incremental reconstruction, SLAM and mapping.

Jointly learns a scene-specific implicit map and RGB-D camera poses online from a stream of observations.

[Project](https://edgarsucar.github.io/iMAP/) · Code: —

Resource note: The author project page remains available. A previously circulated GitHub URL under the author account returned 404 in this validation pass, so no code release is claimed here.

Checked: 2026-11-14.

<a id="neuralrecon"></a>

### NeuralRecon (2021)

**[NeuralRecon: Real-Time Coherent 3D Reconstruction from Monocular Video](https://openaccess.thecvf.com/content/CVPR2021/html/Sun_NeuralRecon_Real-Time_Coherent_3D_Reconstruction_From_Monocular_Video_CVPR_2021_paper.html)** — CVPR 2021 · **Core** · Incremental reconstruction, SLAM and mapping.

Fuses monocular-video features into a sparse voxel representation to reconstruct coherent scene surfaces in real time.

[Project](https://zju3dv.github.io/neuralrecon/) · [Code](https://github.com/zju3dv/NeuralRecon)

Resource note: The official project page links the author implementation.

Checked: 2026-11-14.

<a id="nerf"></a>

### NeRF (2020)

**[NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis](https://arxiv.org/abs/2003.08934)** — ECCV 2020 · **Core** · Neural scene representations and surfaces.

Optimizes a continuous neural field of density and view-dependent radiance for novel-view synthesis of a static captured scene.

[Project](https://www.matthewtancik.com/nerf) · [Code](https://github.com/bmild/nerf)

Resource note: The learned radiance field is a visual scene representation; it does not by itself establish an editable or simulator-ready scene model.

Checked: 2026-11-14.

<a id="bundlefusion"></a>

### BundleFusion (2017)

**[BundleFusion: Real-time Globally Consistent 3D Reconstruction Using On-the-fly Surface Re-integration](https://arxiv.org/abs/1604.01093)** — ACM Transactions on Graphics (SIGGRAPH) 2017 · **Core** · Classical multi-view and RGB-D reconstruction.

Jointly estimates globally optimized RGB-D camera poses and reintegrates surfaces online for globally consistent dense reconstruction.

[Project](https://graphics.stanford.edu/projects/bundlefusion/) · [Code](https://github.com/niessner/BundleFusion)

Resource note: The author repository and project page identify the SIGGRAPH 2017 release.

Checked: 2026-11-14.

<a id="colmap-sfm"></a>

### COLMAP (2016)

**[Structure-from-Motion Revisited](https://openaccess.thecvf.com/content_cvpr_2016/html/Schonberger_Structure-From-Motion_Revisited_CVPR_2016_paper.html)** — CVPR 2016 · **Core** · Classical multi-view and RGB-D reconstruction.

Reconstructs camera poses and sparse scene structure from image collections with incremental structure from motion; the COLMAP software also provides multi-view stereo.

[Project](https://colmap.github.io/) · [Code](https://github.com/colmap/colmap)

Resource note: The maintained COLMAP software is linked as the official implementation; the paper predates the current release line.

Checked: 2026-11-14.


## Scene generation and asset authoring

<a id="survey-generation-embodied"></a>

### 3D Generation for Embodied AI Survey (2026)

**[3D Generation for Embodied AI and Robotic Simulation: A Survey](https://arxiv.org/abs/2604.26509)** — arXiv 2026 · **Enabling** · Surveys and perspectives.

Reviews generated assets, interactive environments, and sim-to-real pipelines, distinguishing appearance, physical validity, and embodied-task evaluation.

[Project](https://3dgen4robot.github.io/) · Code: —

Resource note: Survey and associated reading resources; no method implementation is implied. Publication metadata and latest arXiv revision checked against the primary page.

Checked: 2026-11-14.

<a id="survey-scene-generation"></a>

### 3D Scene Generation Survey (2026)

**[3D Scene Generation: A Survey](https://arxiv.org/abs/2505.05474)** — IJCV 2026 · **Enabling** · Surveys and perspectives.

Organizes scene synthesis by procedural, neural 3D, image-based, and video-based methods, with evaluation and applications.

[Project](https://github.com/hzxie/Awesome-3D-Scene-Generation) · Code: —

Resource note: Survey and associated reading resources; no method implementation is implied. Publication metadata and latest arXiv revision checked against the primary page.

Checked: 2026-11-14.

<a id="articraft"></a>

### Articraft (2026)

**[Articraft: An Agentic System for Scalable Articulated 3D Asset Generation](https://arxiv.org/abs/2605.15187)** — arXiv preprint 2026 · **Core** · Language and vision-guided asset authoring.

Uses LLM-written domain-specific code to define parts, geometry, joints, and validation for articulated assets.

[Project](https://articraft3d.github.io/) · [Code](https://github.com/articraftresearch/Articraft)

Resource note: The author project explicitly redirects readers to articraftresearch/Articraft as the current repository for code and support; it supersedes the older Rook_articraft harness.

Checked: 2026-11-13.

<a id="artllm"></a>

### ArtLLM (2026)

**[ArtLLM: Generating Articulated Assets via 3D LLM](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_ArtLLM_Generating_Articulated_Assets_via_3D_LLM_CVPR_2026_paper.html)** — CVPR 2026 · **Core** · Generative part structure and motion.

Uses a 3D multimodal language model and articulation data to generate assets from complete 3D meshes.

[Project](https://authoritywang.github.io/artllm/) · [Code](https://github.com/AuthorityWang/ArtLLM)

Resource note: Official implementation and model release are available. The repository includes preprocessing and training code, but detailed training/data-preprocessing instructions are still forthcoming; no ArtLLM dataset download was located.

Checked: 2026-11-14.

<a id="lam"></a>

### LAM (2026)

**[LAM: Language Articulated Object Modelers](https://openaccess.thecvf.com/content/CVPR2026/html/Gao_LAM_Language_Articulated_Object_Modelers_CVPR_2026_paper.html)** — CVPR 2026 · **Core** · Generative part structure and motion.

Uses LLM/VLM collaboration to generate geometry and articulation code compiled into URDF.

[Project](https://gaoypeng.github.io/LAM) · [Code](https://github.com/gaoypeng/LAM)

Checked: 2026-11-13.

<a id="pact"></a>

### PAct (2026)

**[PAct: Part-Decomposed Single-View Articulated Object Generation](https://arxiv.org/abs/2602.14965)** — SIGGRAPH Asia (conditionally accepted) 2026 · **Core** · Generative part structure and motion.

A feed-forward part-centric method generates part geometry and articulation parameters from one image.

[Project](https://pact-project.github.io/) · [Code](https://github.com/Mobiuslqm/PAct)

Benchmark connections: PartNet-Mobility, ACD. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="survey-world-modeling"></a>

### 3D and 4D World Modeling Survey (2025)

**[3D and 4D World Modeling: A Survey](https://arxiv.org/abs/2509.07996)** — arXiv 2025 · **Enabling** · Surveys and perspectives.

Organizes world modeling around video, occupancy, and LiDAR representations, with definitions, evaluation settings, and applications.

[Project](https://worldbench.github.io/survey) · Code: —

Resource note: Survey reference; a resource collection is not labeled as implementation code.

Checked: 2026-11-14.

<a id="artformer"></a>

### ArtFormer (2025)

**[ArtFormer: Controllable Generation of Diverse 3D Articulated Objects](https://openaccess.thecvf.com/content/CVPR2025/html/Su_ArtFormer_Controllable_Generation_of_Diverse_3D_Articulated_Objects_CVPR_2025_paper.html)** — CVPR 2025 · **Core** · Generative part structure and motion.

Uses a tree-token representation to generate high-level geometry codes and kinematic relations under text conditions.

Project: — · [Code](https://github.com/ShuYuMo2003/ArtFormer)

Resource note: Official repository found; no separate project page verified.

Checked: 2026-11-13.

<a id="articulate-anymesh"></a>

### Articulate AnyMesh (2025)

**[Articulate AnyMesh: Open-Vocabulary 3D Articulated Objects Modeling](https://arxiv.org/abs/2502.02590)** — CoRL 2025 · **Core** · Language and vision-guided asset authoring.

Converts a rigid 3D mesh into an articulated counterpart using VLMs and visual prompts for parts and joints.

[Project](https://articulate-anymesh.github.io/) · Code: announced

Resource note: The author project explicitly labels its Code link as 'Coming Soon'; no usable official repository was linked in this check.

Checked: 2026-11-13.

<a id="articulate-anything"></a>

### Articulate-Anything (2025)

**[Articulate-Anything: Automatic Modeling of Articulated Objects via a Vision-Language Foundation Model](https://proceedings.iclr.cc/paper_files/paper/2025/hash/2c8047bf3ed8ef6905351608d641f02f-Abstract-Conference.html)** — ICLR 2025 · **Core** · Language and vision-guided asset authoring.

Uses text, images, or video plus retrieval and VLM-generated programs to create simulator-ready articulated URDF assets.

[Project](https://articulate-anything.github.io/) · [Code](https://github.com/vlongle/articulate-anything)

Resource note: Official project and implementation repository located.

Checked: 2026-11-13.

<a id="luciddreamer"></a>

### LucidDreamer (2025)

**[LucidDreamer: Domain-free Generation of 3D Gaussian Splatting Scenes](https://arxiv.org/abs/2311.13384)** — IEEE TVCG 2025 · **Core** · Text and image-conditioned scene synthesis.

Generates navigable Gaussian-splatting scenes from a single text prompt or a single image without a target scene domain.

[Project](https://luciddreamer-cvlab.github.io/) · [Code](https://github.com/luciddreamer-cvlab/LucidDreamer)

Checked: 2026-11-14.

<a id="physnap"></a>

### PhysNAP (2025)

**[Guiding Diffusion-Based Articulated Object Generation by Partial Point Cloud Alignment and Physical Plausibility Constraints](https://openaccess.thecvf.com/content/ICCV2025/html/Kreber_Guiding_Diffusion-Based_Articulated_Object_Generation_by_Partial_Point_Cloud_Alignment_ICCV_2025_paper.html)** — ICCV 2025 · **Core** · Generative part structure and motion.

Guides articulated diffusion with partial point-cloud alignment and constraints on penetration and joint mobility.

Project: — · [Code](https://github.com/EmbodiedVision/physnap)

Checked: 2026-11-13.

<a id="realmdreamer"></a>

### RealmDreamer (2025)

**[RealmDreamer: Text-Driven 3D Scene Generation with Inpainting and Depth Diffusion](https://arxiv.org/abs/2404.07199)** — 3DV 2025 · **Core** · Text and image-conditioned scene synthesis.

Optimizes a Gaussian-splatting representation through diffusion-based inpainting and depth guidance to synthesize forward-facing text-conditioned scenes.

[Project](https://realmdreamer.github.io/) · [Code](https://github.com/jaidevshriram/realmdreamer)

Checked: 2026-11-14.

<a id="scenario-dreamer"></a>

### Scenario Dreamer (2025)

**[Scenario Dreamer: Vectorized Latent Diffusion for Generating Driving Simulation Environments](https://arxiv.org/abs/2503.22496)** — CVPR 2025 · **Core** · Simulation environments and embodied training.

Generates vectorized traffic scenes and closed-loop agent behaviors for driving-planner simulation, rather than indoor manipulation.

[Project](https://princeton-computational-imaging.github.io/scenario-dreamer/) · [Code](https://github.com/princeton-computational-imaging/scenario-dreamer)

Checked: 2026-11-14.

<a id="singapo"></a>

### SINGAPO (2025)

**[SINGAPO: Single Image Controlled Generation of Articulated Parts in Objects](https://proceedings.iclr.cc/paper_files/paper/2025/hash/f2ba7d0d1394609d5ce11853cfd1c9bf-Abstract-Conference.html)** — ICLR 2025 · **Core** · Generative part structure and motion.

Generates plausible articulated assets from one resting-state RGB view while modeling geometry and kinematic ambiguity.

Project: — · [Code](https://github.com/3dlg-hcvc/singapo)

Resource note: Use the ICLR abstract page rather than the broken PDF route from the intake check.

Checked: 2026-11-13.

<a id="wonderworld"></a>

### WonderWorld (2025)

**[WonderWorld: Interactive 3D Scene Generation from a Single Image](https://arxiv.org/abs/2406.09394)** — CVPR 2025 · **Core** · Text and image-conditioned scene synthesis.

Expands a single image into connected 3D scenes while allowing users to specify new content and locations during exploration.

[Project](https://kovenyu.com/wonderworld/) · [Code](https://github.com/KovenYu/WonderWorld)

Checked: 2026-11-14.

<a id="cage"></a>

### CAGE (2024)

**[CAGE: Controllable Articulation GEneration](https://openaccess.thecvf.com/content/CVPR2024/html/Liu_CAGE_Controllable_Articulation_GEneration_CVPR_2024_paper.html)** — CVPR 2024 · **Core** · Generative part structure and motion.

Generates an articulated shape abstraction with geometry and motion parameters subject to category and graph constraints.

[Project](https://3dlg-hcvc.github.io/cage/) · [Code](https://github.com/3dlg-hcvc/cage)

Resource note: Project page links code/data; repository identifies official implementation.

Checked: 2026-11-13.

<a id="diffuscene"></a>

### DiffuScene (2024)

**[DiffuScene: Denoising Diffusion Models for Generative Indoor Scene Synthesis](https://openaccess.thecvf.com/content/CVPR2024/html/Tang_DiffuScene_Denoising_Diffusion_Models_for_Generative_Indoor_Scene_Synthesis_CVPR_2024_paper.html)** — CVPR 2024 · **Core** · Indoor layouts and scene graphs.

Uses a diffusion model over indoor scene configurations containing semantic classes, object geometry, and placements.

Project: — · [Code](https://github.com/tangjiapeng/DiffuScene)

Checked: 2026-11-14.

<a id="holodeck"></a>

### Holodeck (2024)

**[Holodeck: Language Guided Generation of 3D Embodied AI Environments](https://arxiv.org/abs/2312.09067)** — CVPR 2024 · **Core** · Simulation environments and embodied training.

Uses language-model planning and a 3D asset collection to construct embodied-AI environments from natural-language requirements.

[Project](https://yueyang.ai/holodeck/) · [Code](https://github.com/allenai/Holodeck)

Checked: 2026-11-14.

<a id="infinigen-indoors"></a>

### Infinigen Indoors (2024)

**[Infinigen Indoors: Photorealistic Indoor Scenes Using Procedural Generation](https://arxiv.org/abs/2406.11824)** — CVPR 2024 · **Core** · Procedural scene and world generation.

Extends procedural scene construction to photorealistic indoor environments and provides an export path for real-time simulator use.

[Project](https://infinigen.org/) · [Code](https://github.com/princeton-vl/infinigen)

Checked: 2026-11-14.

<a id="instructscene"></a>

### InstructScene (2024)

**[InstructScene: Instruction-Driven 3D Indoor Scene Synthesis with Semantic Graph Prior](https://arxiv.org/abs/2402.04717)** — ICLR 2024 · **Core** · Indoor layouts and scene graphs.

Combines a semantic graph prior with a layout decoder to synthesize indoor scenes from instructions.

[Project](https://chenguolin.github.io/projects/InstructScene/) · [Code](https://github.com/chenguolin/InstructScene)

Checked: 2026-11-14.

<a id="robogen"></a>

### RoboGen (2024)

**[RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation](https://arxiv.org/abs/2311.01455)** — ICML 2024 · **Core** · Simulation environments and embodied training.

Uses generative simulation to create tasks, scenes, and training supervision for automated robot-skill learning.

[Project](https://robogen-ai.github.io/) · [Code](https://github.com/Genesis-Embodied-AI/RoboGen)

Checked: 2026-11-14.

<a id="text2nerf"></a>

### Text2NeRF (2024)

**[Text2NeRF: Text-Driven 3D Scene Generation with Neural Radiance Fields](https://arxiv.org/abs/2305.11588)** — IEEE TVCG 2024 · **Core** · Text and image-conditioned scene synthesis.

Combines neural radiance fields with text-to-image diffusion to generate view-consistent indoor and outdoor scenes from language descriptions.

[Project](https://eckertzhang.github.io/Text2NeRF.github.io/) · [Code](https://github.com/eckertzhang/Text2NeRF)

Checked: 2026-11-14.

<a id="infinigen"></a>

### Infinigen (2023)

**[Infinite Photorealistic Worlds Using Procedural Generation](https://arxiv.org/abs/2306.09310)** — CVPR 2023 · **Core** · Procedural scene and world generation.

Procedurally generates diverse photorealistic natural 3D worlds, including geometry, materials, and scene composition.

[Project](https://infinigen.org/) · [Code](https://github.com/princeton-vl/infinigen)

Checked: 2026-11-14.

<a id="layoutgpt"></a>

### LayoutGPT (2023)

**[LayoutGPT: Compositional Visual Planning and Generation with Large Language Models](https://arxiv.org/abs/2305.15393)** — NeurIPS 2023 · **Core** · Indoor layouts and scene graphs.

Uses in-context LLM prompting to translate text conditions into layouts, including 3D indoor scene layouts.

[Project](https://layoutgpt.github.io/) · [Code](https://github.com/UCSB-AI/LayoutGPT)

Checked: 2026-11-14.

<a id="nap"></a>

### NAP (2023)

**[NAP: Neural 3D Articulated Object Prior](https://proceedings.neurips.cc/paper_files/paper/2023/hash/655846cc914cb7ff977a1ada40866441-Abstract-Conference.html)** — NeurIPS 2023 · **Core** · Generative part structure and motion.

Uses diffusion over an articulation graph to synthesize articulated object models and conditional variants.

[Project](https://www.jiahuilei.com/projects/nap/) · [Code](https://github.com/JiahuiLei/NAP)

Resource note: The author homepage links this current project URL and the repository. The repository is a usable preview with basic training/inference, not a full release.

Checked: 2026-11-13.

<a id="scenedreamer"></a>

### SceneDreamer (2023)

**[SceneDreamer: Unbounded 3D Scene Generation from 2D Image Collections](https://arxiv.org/abs/2302.01330)** — IEEE TPAMI 2023 · **Core** · Text and image-conditioned scene synthesis.

Learns an unbounded 3D scene generator from collections of 2D images, targeting large-scale visual worlds rather than an object layout alone.

[Project](https://scene-dreamer.github.io/) · [Code](https://github.com/FrozenBurning/SceneDreamer)

Checked: 2026-11-14.

<a id="text2room"></a>

### Text2Room (2023)

**[Text2Room: Extracting Textured 3D Meshes from 2D Text-to-Image Models](https://arxiv.org/abs/2303.11989)** — ICCV 2023 · **Core** · Text and image-conditioned scene synthesis.

Iteratively creates a room-scale textured mesh from a text prompt by lifting text-to-image outputs through depth estimation and inpainting.

[Project](https://lukashoel.github.io/text-to-room/) · [Code](https://github.com/lukasHoel/text2room)

Checked: 2026-11-14.

<a id="procthor"></a>

### ProcTHOR (2022)

**[ProcTHOR: Large-Scale Embodied AI Using Procedural Generation](https://arxiv.org/abs/2206.06994)** — NeurIPS Datasets and Benchmarks 2022 · **Core** · Procedural scene and world generation.

Procedurally samples diverse interactive 3D houses for simulated embodied-agent training and evaluation.

[Project](https://procthor.allenai.org/) · [Code](https://github.com/allenai/procthor)

Checked: 2026-11-14.

<a id="atiss"></a>

### ATISS (2021)

**[ATISS: Autoregressive Transformers for Indoor Scene Synthesis](https://arxiv.org/abs/2110.03675)** — NeurIPS 2021 · **Core** · Indoor layouts and scene graphs.

Generates indoor object layouts from a room type and floor plan, while supporting completion and object-placement constraints.

[Project](https://research.nvidia.com/labs/toronto-ai/ATISS/) · [Code](https://github.com/nv-tlabs/ATISS)

Checked: 2026-11-14.

<a id="graph-to-3d"></a>

### Graph-to-3D (2021)

**[Graph-to-3D: End-to-End Generation and Manipulation of 3D Scenes Using Scene Graphs](https://openaccess.thecvf.com/content/ICCV2021/html/Dhamo_Graph-to-3D_End-to-End_Generation_and_Manipulation_of_3D_Scenes_Using_Scene_ICCV_2021_paper.html)** — ICCV 2021 · **Core** · Indoor layouts and scene graphs.

Uses scene graphs to jointly generate scene layout and object shape, enabling graph-conditioned 3D scene manipulation.

[Project](https://he-dhamo.github.io/Graphto3D/) · [Code](https://github.com/he-dhamo/graphto3d)

Checked: 2026-11-14.

<a id="sceneformer"></a>

### SceneFormer (2021)

**[SceneFormer: Indoor Scene Generation with Transformers](https://arxiv.org/abs/2012.09793)** — 3DV 2021 · **Core** · Indoor layouts and scene graphs.

Generates sequences of indoor objects, locations, and orientations conditioned on room layout, with a separate text-conditioned setting described by the authors.

[Project](https://xinpeng-wang.github.io/sceneformer/) · [Code](https://github.com/cy94/sceneformer)

Checked: 2026-11-14.


## Embodied agents and robotic interaction

<a id="vitacman"></a>

### Vi-TacMan (2026)

**[Vi-TacMan: Articulated Object Manipulation via Vision and Touch](https://vi-tacman.github.io/)** — ICRA 2026 · **Core** · Contact and tactile feedback.

Uses vision to propose a grasp and coarse direction, then uses tactile contact feedback for precise articulated manipulation without an explicit kinematic model.

[Project](https://vi-tacman.github.io/) · [Code](https://github.com/leiyaocui/Vi-TacMan)

Resource note: Project page and public repository use the same paper title.

Checked: 2026-11-13.

<a id="survey-vla"></a>

### VLA Survey (2026)

**[A Survey on Vision-Language-Action Models for Embodied AI](https://arxiv.org/abs/2405.14093)** — TNNLS 2026 · **Enabling** · Surveys and perspectives.

Organizes vision-language-action research into model components, low-level control policies, and high-level task planning, alongside datasets and evaluation.

[Project](https://github.com/yueen-ma/Awesome-VLA) · Code: —

Resource note: Survey and associated reading resources; no method implementation is implied. Publication metadata and latest arXiv revision checked against the primary page.

Checked: 2026-11-14.

<a id="articubot"></a>

### ArticuBot (2025)

**[ArticuBot: Learning Universal Articulated Object Manipulation Policy via Large Scale Simulation](https://www.roboticsproceedings.org/rss21/p156.pdf)** — RSS 2025 · **Core** · Motion-aware control and manipulation.

Trains one policy in large-scale simulation for opening unseen articulated object categories and reports real-world experiments.

[Project](https://articubot.github.io/) · [Code](https://github.com/yufeiwang63/ArticuBot)

Benchmark connections: partnet-mobility. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="checkmanual"></a>

### CheckManual (2025)

**[CheckManual: A New Challenge and Benchmark for Manual-based Appliance Manipulation](https://openaccess.thecvf.com/content/CVPR2025/html/Long_CheckManual_A_New_Challenge_and_Benchmark_for_Manual-based_Appliance_Manipulation_CVPR_2025_paper.html)** — CVPR 2025 · **Core** · Language-guided manipulation and agents.

Introduces a manual-based appliance-manipulation benchmark and the ManualPlan baseline; the author repository provides setup, articulated-object assets, and code.

[Project](https://sites.google.com/view/checkmanual) · [Code](https://github.com/LYX0501/CheckManual)

Benchmark connections: partnet-mobility. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-14.

<a id="groot-n1"></a>

### GR00T N1 (2025)

**[GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734)** — NVIDIA technical whitepaper 2025 · **Enabling** · Generalist policies and vision-language-action models.

A dual-system vision-language-action foundation model for humanoid robots, trained with egocentric video, real and simulated robot trajectories, and synthetic data.

[Project](https://research.nvidia.com/index.php/publication/2025-03_nvidia-isaac-gr00t-n1-open-foundation-model-humanoid-robots) · [Code](https://github.com/NVIDIA/Isaac-GR00T)

Resource note: The current official repository foregrounds later N1.x releases; it is retained as the official code ecosystem for the original N1 record, not conflated with N1.5.

Benchmark connections: robocasa. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="mosart"></a>

### MOSART (2025)

**[Opening Articulated Structures in the Real World](https://arxiv.org/abs/2402.17767)** — RSS 2025 · **Core** · Motion-aware control and manipulation.

Uses opening novel articulated structures as an end-to-end mobile-manipulation testbed, integrating robot-centric perception, navigation, whole-body planning, grasping, and adaptation across real sites.

[Project](https://arjung128.github.io/opening-articulated-structures/) · [Code](https://github.com/arjung128/stretch-open)

Resource note: Official project and RSS paper link the code. The repository targets the authors' Stretch RE2/ROS setup and requires external model weights.

Checked: 2026-11-13.

<a id="tacman"></a>

### Tac-Man (2025)

**[Tac-Man: Tactile-Informed Prior-Free Manipulation of Articulated Objects](https://arxiv.org/abs/2403.01694)** — IEEE Transactions on Robotics 2025 · **Core** · Contact and tactile feedback.

Uses tactile feedback for prior-free manipulation of articulated objects, including objects with complex joints and perturbations.

[Project](https://tacman-aom.github.io/tac-man/) · [Code](https://github.com/YuyangLee/Tac-Man-Simulation)

Resource note: Author project links this repository. It releases the paper's Isaac Sim simulation studies, not the complete real-robot stack.

Checked: 2026-11-13.

<a id="uniaff"></a>

### UniAff (2025)

**[UniAff: A Unified Representation of Affordances for Tool Usage and Articulation with Vision-Language Models](https://arxiv.org/abs/2409.20551)** — ICRA 2025 · **Core** · Language-guided manipulation and agents.

Defines a unified representation for manipulation affordances covering articulated objects and tools, with a VLM-oriented formulation.

[Project](https://sites.google.com/view/uni-aff/home) · [Code](https://github.com/qiaojunyu/UniAff)

Resource note: Author project links this repository. It provides annotation/rendering utilities and points to A3VLM for fine-tuning implementation, so it is a partial rather than end-to-end release.

Checked: 2026-11-13.

<a id="pi-zero-point-five"></a>

### π0.5 (2025)

**[π0.5: a Vision-Language-Action Model with Open-World Generalization](https://arxiv.org/abs/2504.16054)** — arXiv 2025 · **Enabling** · Generalist policies and vision-language-action models.

Extends π0 with co-training across heterogeneous robot and semantic data to target open-world robot manipulation generalization.

[Project](https://www.physicalintelligence.company/blog/pi05) · [Code](https://github.com/Physical-Intelligence/openpi)

Resource note: The official Physical Intelligence announcement redirects to pi.website and may show a Vercel checkpoint to automated clients; it is retained as the official project page. Keep π0.5 separate from π0.

Benchmark connections: robocasa. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="a3vlm"></a>

### A3VLM (2024)

**[A3VLM: Actionable Articulation-Aware Vision Language Model](https://arxiv.org/abs/2406.07549)** — CoRL 2024 · **Core** · Language-guided manipulation and agents.

Uses an object-centric representation of articulation structure and affordance that can be converted to action primitives; the repository releases model and data-generation code.

Project: — · [Code](https://github.com/changhaonan/A3VLM)

Benchmark connections: partnet-mobility. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="centerart"></a>

### CenterArt (2024)

**[CenterArt: Joint Shape Reconstruction and 6-DoF Grasp Estimation of Articulated Objects](https://arxiv.org/abs/2404.14968)** — arXiv preprint 2024 · **Core** · Motion-aware control and manipulation.

Jointly predicts shape and joint codes to reconstruct articulated objects and estimate 6-DoF grasps from RGB-D scenes.

Project: — · [Code](https://github.com/Sassanmtr/CenterArt)

Resource note: First-author repository supplies data-generation, training, evaluation, and pretrained-weight instructions.

Checked: 2026-11-13.

<a id="flowbothd"></a>

### FlowBotHD (2024)

**[FlowBotHD: History-Aware Diffuser Handling Ambiguities in Articulated Objects Manipulation](https://arxiv.org/abs/2410.07078)** — CoRL 2024 · **Core** · Motion-aware control and manipulation.

Uses a history-aware diffusion model to represent multimodal articulation hypotheses under symmetry and occlusion.

[Project](https://flowbothd.github.io/) · [Code](https://github.com/liy1shu/FlowBotHD)

Benchmark connections: partnet-mobility. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="gamma"></a>

### GAMMA (2024)

**[GAMMA: Generalizable Articulation Modeling and Manipulation for Articulated Objects](https://ieeexplore.ieee.org/document/10610652/)** — ICRA 2024 · **Core** · Motion-aware control and manipulation.

Combines articulation modeling with grasp-pose affordance and adaptively updates joint estimates during manipulation.

Project: — · [Code](https://github.com/qiaojunyu/GAMMA-ICRA2024)

Resource note: Public repository documents data generation and training setup for GAMMA.

Checked: 2026-11-13.

<a id="leo"></a>

### LEO (2024)

**[LEO: An Embodied Generalist Agent in 3D World](https://arxiv.org/abs/2311.12871)** — ICML 2024 · **Core** · 3D reasoning and embodied generalists.

Trains a multimodal agent with 3D vision-language alignment and vision-language-action instruction tuning across grounding, reasoning, planning, navigation, and manipulation.

[Project](https://embodied-generalist.github.io/) · [Code](https://github.com/embodied-generalist/embodied-generalist)

Checked: 2026-11-14.

<a id="manipllm"></a>

### ManipLLM (2024)

**[ManipLLM: Embodied Multimodal Large Language Model for Object-Centric Robotic Manipulation](https://openaccess.thecvf.com/content/CVPR2024/html/Li_ManipLLM_Embodied_Multimodal_Large_Language_Model_for_Object-Centric_Robotic_Manipulation_CVPR_2024_paper.html)** — CVPR 2024 · **Core** · Language-guided manipulation and agents.

Uses RGB and text prompts for affordance reasoning and end-effector pose prediction, followed by a closed-loop impedance adaptation policy.

[Project](https://sites.google.com/view/manipllm) · [Code](https://github.com/clorislili/ManipLLM)

Resource note: Author project links the official repository. It includes data collection, training, and direct-pose inference; test code omits the paper's chain-of-thought inference and requires external foundation checkpoints.

Checked: 2026-11-13.

<a id="octo"></a>

### Octo (2024)

**[Octo: An Open-Source Generalist Robot Policy](https://arxiv.org/abs/2405.12213)** — Robotics: Science and Systems 2024 · **Enabling** · Generalist policies and vision-language-action models.

Provides a transformer diffusion policy and training code for language- or goal-image-conditioned robot control across multiple embodiments.

[Project](https://octo-models.github.io/) · [Code](https://github.com/octo-models/octo)

Checked: 2026-11-14.

<a id="openvla"></a>

### OpenVLA (2024)

**[OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246)** — CoRL 2024 · **Enabling** · Generalist policies and vision-language-action models.

Releases a vision-language-action model trained on robot demonstrations for language-conditioned visuomotor control and adaptation.

[Project](https://openvla.github.io/) · [Code](https://github.com/openvla/openvla)

Checked: 2026-11-14.

<a id="rpmart"></a>

### RPMArt (2024)

**[RPMArt: Towards Robust Perception and Manipulation for Articulated Objects](https://arxiv.org/abs/2403.16023)** — IROS 2024 · **Core** · Motion-aware control and manipulation.

Estimates articulation parameters and interaction points from noisy point clouds, then uses them to constrain grasping and articulated motion; the authors report synthetic-to-real transfer.

[Project](https://r-pmart.github.io/) · [Code](https://github.com/R-PMArt/rpmart)

Benchmark connections: partnet-mobility. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="sage"></a>

### SAGE (2024)

**[SAGE: Bridging Semantic and Actionable Parts for Generalizable Manipulation of Articulated Objects](https://www.roboticsproceedings.org/rss20/p016.pdf)** — RSS 2024 · **Core** · Language-guided manipulation and agents.

Maps language-grounded semantic parts to actionable parts, derives executable policies, and uses interactive feedback after failed action steps.

[Project](https://geometry.stanford.edu/projects/sage/) · [Code (announced)](https://github.com/geng-haoran/SAGE)

Resource note: Official repository exists, but its README says 'Benchmark & Code & Instructions Coming soon'; do not present it as a usable implementation.

Checked: 2026-11-13.

<a id="vlfm"></a>

### VLFM (2024)

**[VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation](https://arxiv.org/abs/2312.01050)** — ICRA 2024 · **Core** · Semantic maps, memory and navigation.

Combines frontier exploration with visual-language goal recognition for zero-shot semantic navigation.

[Project](https://naoki.io/vlfm/) · [Code](https://github.com/rai-opensource/vlfm)

Benchmark connections: habitat-navigation. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-14.

<a id="pi-zero"></a>

### π0 (2024)

**[π0: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164)** — arXiv 2024 · **Enabling** · Generalist policies and vision-language-action models.

Combines a pretrained vision-language model with a flow-matching action expert for cross-embodiment general robot control.

[Project](https://www.physicalintelligence.company/blog/pi0) · [Code](https://github.com/Physical-Intelligence/openpi)

Resource note: The official Physical Intelligence announcement redirects to pi.website and may show a Vercel checkpoint to automated clients; it is retained as the official project page. The linked openpi repository is published by the Physical Intelligence team.

Benchmark connections: robocasa. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="3d-llm"></a>

### 3D-LLM (2023)

**[3D-LLM: Injecting the 3D World into Large Language Models](https://arxiv.org/abs/2307.12981)** — NeurIPS 2023 · **Core** · 3D reasoning and embodied generalists.

Augments a language model with 3D scene features for 3D question answering, dialogue, planning, navigation, and manipulation tasks.

Project: — · [Code](https://github.com/UMass-Embodied-AGI/3D-LLM)

Checked: 2026-11-14.

<a id="diffusion-policy"></a>

### Diffusion Policy (2023)

**[Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://arxiv.org/abs/2303.04137)** — Robotics: Science and Systems 2023 · **Enabling** · Generalist policies and vision-language-action models.

Represents visuomotor control as conditional action diffusion, with visual conditioning and receding-horizon action execution.

[Project](https://diffusion-policy.cs.columbia.edu/) · [Code](https://github.com/real-stanford/diffusion_policy)

Benchmark connections: robocasa. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="env-aware-affordance"></a>

### EnvAwareAfford (2023)

**[Learning Environment-Aware Affordance for 3D Articulated Object Manipulation under Occlusions](https://proceedings.neurips.cc/paper_files/paper/2023/hash/bf78fc727cf882df66e6dbc826161e86-Abstract-Conference.html)** — NeurIPS 2023 · **Core** · Affordances and active exploration.

Models point-level affordance with target geometry, occluders, and robot-position constraints; its official repository includes code and data instructions.

Project: — · [Code](https://github.com/chengkaiAcademyCity/EnvAwareAfford)

Resource note: The author-labelled repository supplies code/data and points to a historic project page that currently returns 404; retain the repository and remove the dead project URL.

Benchmark connections: partnet-mobility, sapien. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="flowbot-plusplus"></a>

### FlowBot++ (2023)

**[FlowBot++: Learning Generalized Articulated Objects Manipulation via Articulation Projection](https://proceedings.mlr.press/v229/zhang23c/zhang23c.pdf)** — CoRL 2023 · **Core** · Motion-aware control and manipulation.

Combines dense articulation flow and per-point articulation parameters for zero-shot manipulation of novel articulated objects.

[Project](https://sites.google.com/view/flowbotpp/home) · [Code](https://github.com/harryzhangOG/flowbotpp)

Resource note: The author project links the repository, which calls itself the official code base; its public content is compact (part-embedding folder plus README).

Benchmark connections: partnet-mobility. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="llm-planner"></a>

### LLM-Planner (2023)

**[LLM-Planner: Few-Shot Grounded Planning for Embodied Agents with Large Language Models](https://openaccess.thecvf.com/content/ICCV2023/html/Song_LLM-Planner_Few-Shot_Grounded_Planning_for_Embodied_Agents_with_Large_Language_ICCV_2023_paper.html)** — ICCV 2023 · **Core** · Language-grounded planning and agents.

Uses few-shot language-model prompting to produce high-level plans grounded through a low-level embodied controller.

[Project](https://osu-nlp-group.github.io/LLM-Planner/) · [Code](https://github.com/OSU-NLP-Group/LLM-Planner)

Benchmark connections: alfred. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-14.

<a id="lm-nav"></a>

### LM-Nav (2023)

**[LM-Nav: Robotic Navigation with Large Pre-Trained Models of Language, Vision, and Action](https://proceedings.mlr.press/v205/shah23b.html)** — CoRL (PMLR proceedings) 2023 · **Core** · Semantic maps, memory and navigation.

Uses language models to name landmarks, image-language association to ground them, and a vision navigation model to execute long-horizon language instructions.

[Project](https://sites.google.com/view/lmnav/home) · [Code](https://github.com/blazejosinski/lm_nav)

Checked: 2026-11-14.

<a id="palm-e"></a>

### PaLM-E (2023)

**[PaLM-E: An Embodied Multimodal Language Model](https://arxiv.org/abs/2303.03378)** — ICML 2023 · **Enabling** · Generalist policies and vision-language-action models.

Incorporates continuous visual and robot-state observations into a language model for embodied reasoning and control tasks.

[Project](https://palm-e.github.io/) · Code: —

Checked: 2026-11-14.

<a id="rt-2"></a>

### RT-2 (2023)

**[RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://proceedings.mlr.press/v229/zitkovich23a.html)** — CoRL (PMLR proceedings) 2023 · **Enabling** · Generalist policies and vision-language-action models.

Represents robot actions as tokens in a vision-language-action model to transfer visual-language knowledge to robot control.

[Project](https://robotics-transformer2.github.io/) · Code: —

Checked: 2026-11-14.

<a id="sim2real2"></a>

### Sim2Real² (2023)

**[Sim2Real²: Actively Building Explicit Physics Model for Precise Articulated Object Manipulation](https://arxiv.org/abs/2302.10693)** — ICRA 2023 · **Core** · Motion-aware control and manipulation.

Uses a one-step interaction to construct an explicit object physics model, then plans a target joint-state trajectory with MPC; the released repository contains the three pipeline modules.

[Project](https://ttimelord.github.io/Sim2Real2-site/) · [Code](https://github.com/TTimelord/Sim2Real2)

Benchmark connections: partnet-mobility, sapien. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="vlmaps"></a>

### VLMaps (2023)

**[Visual Language Maps for Robot Navigation](https://arxiv.org/abs/2210.05714)** — ICRA 2023 · **Core** · Semantic maps, memory and navigation.

Fuses visual-language features into a spatial 3D map that can be queried with language for navigation goals and obstacle maps.

[Project](https://vlmaps.github.io/) · [Code](https://github.com/vlmaps/vlmaps)

Benchmark connections: habitat-navigation. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-14.

<a id="voxposer"></a>

### VoxPoser (2023)

**[VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models](https://proceedings.mlr.press/v229/huang23b.html)** — CoRL 2023 · **Core** · Language-guided manipulation and agents.

Uses language-model programs and 3D value maps to express and ground manipulation constraints in observed scenes.

[Project](https://voxposer.github.io/) · [Code](https://github.com/huangwl18/VoxPoser)

Resource note: PMLR identifies the correct proceedings identifier as huang23b, not huang23f.

Checked: 2026-11-13.

<a id="where2explore"></a>

### Where2Explore (2023)

**[Where2Explore: Few-shot Affordance Learning for Unseen Novel Categories of Articulated Objects](https://proceedings.neurips.cc/paper_files/paper/2023/hash/0e7e2af2e5ba822c9ad35a37b31b5dd4-Abstract-Conference.html)** — NeurIPS 2023 · **Core** · Affordances and active exploration.

Uses geometric similarity to choose few-shot exploration interactions and transfer affordance knowledge to unseen articulated categories.

[Project](https://tritiumr.github.io/Where2Explore/) · [Code](https://github.com/TritiumR/Where2Explore)

Resource note: Author repository provides code and data; project page is linked from that repository.

Benchmark connections: partnet-mobility. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="flowbot3d"></a>

### FlowBot3D (2022)

**[FlowBot3D: Learning 3D Articulation Flow to Manipulate Articulated Objects](https://www.roboticsproceedings.org/rss18/p018.html)** — RSS 2022 · **Core** · Motion-aware control and manipulation.

Predicts a dense point-wise motion field from a point cloud and uses it to guide analytical motion planning for articulated manipulation.

Project: — · [Code](https://github.com/r-pad/flowbot3d)

Resource note: Public repository names the RSS paper and contains package, scripts, tests, and pretrained directory.

Checked: 2026-11-13.

<a id="saycan"></a>

### SayCan (2022)

**[Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](https://arxiv.org/abs/2204.01691)** — Conference on Robot Learning 2022 · **Core** · Language-guided manipulation and agents.

Combines language-model task planning with learned skill value functions to select robot actions that are both relevant and feasible.

[Project](https://say-can.github.io/) · [Code](https://github.com/google-research/google-research/tree/master/saycan)

Resource note: Google Research provides a self-contained tabletop implementation; it is not the complete original mobile-manipulator system.

Checked: 2026-11-13.

<a id="umpnet"></a>

### UMPNet (2022)

**[UMPNet: Universal Manipulation Policy Network for Articulated Objects](https://ump-net.cs.columbia.edu/)** — RA-L / ICRA 2022 · **Core** · Affordances and active exploration.

A single image-based policy uses self-guided exploration and a per-step Arrow-of-Time attribute for closed-loop articulated manipulation and state exploration.

[Project](https://ump-net.cs.columbia.edu/) · [Code](https://github.com/real-stanford/umpnet)

Resource note: Official project and public implementation repository.

Checked: 2026-11-13.

<a id="act-the-part"></a>

### Act the Part (2021)

**[Act the Part: Learning Interaction Strategies for Articulated Object Part Discovery](https://openaccess.thecvf.com/content/ICCV2021/html/Gadre_Act_the_Part_Learning_Interaction_Strategies_for_Articulated_Object_Part_ICCV_2021_paper.html)** — ICCV 2021 · **Core** · Affordances and active exploration.

Couples learned action selection with motion segmentation to discover articulated parts without semantic part labels.

[Project](https://atp.cs.columbia.edu/) · Code: —

Resource note: Official project provides paper and browser demonstration but does not link an author code release.

Benchmark connections: partnet-mobility. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="where2act"></a>

### Where2Act (2021)

**[Where2Act: From Pixels to Actions for Articulated 3D Objects](https://openaccess.thecvf.com/content/ICCV2021/html/Mo_Where2Act_From_Pixels_to_Actions_for_Articulated_3D_Objects_ICCV_2021_paper.html)** — ICCV 2021 · **Core** · Affordances and active exploration.

Predicts pixel-level actionability, interaction trajectories, and success likelihoods for pushing and pulling articulated objects from image and depth input.

Project: — · [Code](https://github.com/daerduoCarey/where2act)

Resource note: Author repository used by later official papers as the Where2Act implementation.

Checked: 2026-11-13.


## Datasets, simulators, and benchmarks

<a id="robocasa365"></a>

### RoboCasa365 (2026)

**[RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots](https://arxiv.org/abs/2603.04356)** — ICLR 2026 · **Enabling** · Manipulation and household-task benchmarks.

Scales kitchen tasks, scenes, and demonstrations to study multi-task policies, generalist pretraining, and compositional robot-task generalization.

[Project](https://robocasa.ai/) · [Code](https://github.com/robocasa/robocasa)

Benchmark connections: robocasa. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="arti-pg"></a>

### Arti-PG (2025)

**[Arti-PG: A Toolbox for Procedurally Synthesizing Large-Scale and Diverse Articulated Objects with Rich Annotations](https://openaccess.thecvf.com/content/ICCV2025/html/Sun_Arti-PG_A_Toolbox_for_Procedurally_Synthesizing_Large-Scale_and_Diverse_Articulated_ICCV_2025_paper.html)** — ICCV 2025 · **Core** · Articulated assets and simulators.

Procedurally synthesizes articulated objects with rich annotations for articulation-understanding data.

Project: — · [Toolkit](https://github.com/Analytic-Concept-Group/ArtiPG)

Checked: 2026-11-13.

<a id="goat-bench"></a>

### GOAT-Bench (2024)

**[GOAT-Bench: A Benchmark for Multi-Modal Lifelong Navigation](https://openaccess.thecvf.com/content/CVPR2024/html/Khanna_GOAT-Bench_A_Benchmark_for_Multi-Modal_Lifelong_Navigation_CVPR_2024_paper.html)** — CVPR 2024 · **Core** · Embodied navigation and semantic memory.

Evaluates lifelong navigation to object-category, image, and language goals, including the role of scene memory across goal modalities.

[Project](https://mukulkhanna.github.io/goat-bench/) · [Toolkit](https://github.com/Ram81/goat-bench)

Benchmark connections: goat-bench. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-14.

<a id="habitat3"></a>

### Habitat 3.0 (2024)

**[Habitat 3.0: A Co-Habitat for Humans, Avatars and Robots](https://arxiv.org/abs/2310.13724)** — ICLR 2024 · **Enabling** · Embodied simulators and household tasks.

Adds humanoid simulation, human-in-the-loop infrastructure, and collaborative social-navigation and rearrangement tasks to Habitat.

[Project](https://aihabitat.org/habitat3/) · [Toolkit](https://github.com/facebookresearch/habitat-lab)

Benchmark connections: habitat3. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-14.

<a id="openeqa"></a>

### OpenEQA (2024)

**[OpenEQA: Embodied Question Answering in the Era of Foundation Models](https://openaccess.thecvf.com/content/CVPR2024/html/Majumdar_OpenEQA_Embodied_Question_Answering_in_the_Era_of_Foundation_Models_CVPR_2024_paper.html)** — CVPR 2024 · **Core** · Embodied question answering and 3D reasoning.

Introduces open-vocabulary embodied question answering for episodic-memory and active-exploration settings in real scanned environments.

[Project](https://open-eqa.github.io/) · [Toolkit](https://github.com/facebookresearch/open-eqa)

Benchmark connections: openeqa. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-14.

<a id="robocasa"></a>

### RoboCasa (2024)

**[RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots](https://arxiv.org/abs/2406.02523)** — RSS 2024 · **Enabling** · Manipulation and household-task benchmarks.

Combines interactive kitchen environments, varied robot embodiments, articulated furniture, and human/synthetic demonstrations for everyday robot learning.

[Project](https://robocasa.ai/) · [Code](https://github.com/robocasa/robocasa)

Benchmark connections: robocasa. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="behavior1k"></a>

### BEHAVIOR-1K (2023)

**[BEHAVIOR-1K: A Benchmark for Embodied AI with 1,000 Everyday Activities and Realistic Simulation](https://proceedings.mlr.press/v205/li23a.html)** — CoRL (PMLR proceedings) 2023 · **Enabling** · Manipulation and household-task benchmarks.

Household-activity benchmark and OmniGibson environment for long-horizon embodied tasks with dynamic object states; its current challenge documentation specifies a reproducible onboard-sensing evaluation protocol.

[Project](https://behavior.stanford.edu/) · [Code](https://github.com/StanfordVL/BEHAVIOR-1K)

Resource note: Proceedings publication year is 2023; the sixth CoRL conference took place in 2022. OmniGibson is the simulation environment accompanying this benchmark.

Benchmark connections: behavior1k. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="maniskill2"></a>

### ManiSkill2 (2023)

**[ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills](https://arxiv.org/abs/2302.04659)** — ICLR 2023 · **Enabling** · Manipulation and household-task benchmarks.

Open benchmark with articulation tasks, mobile and dual-arm settings, 2D/3D observations, demonstration data, RL, imitation learning, and planning interfaces.

[Project](https://maniskill2.github.io/) · [Code](https://github.com/haosulab/ManiSkill2)

Benchmark connections: maniskill2. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="scannetpp"></a>

### ScanNet++ (2023)

**[ScanNet++: A High-Fidelity Dataset of 3D Indoor Scenes](https://openaccess.thecvf.com/content/ICCV2023/html/Yeshwanth_ScanNet_A_High-Fidelity_Dataset_of_3D_Indoor_Scenes_ICCV_2023_paper.html)** — ICCV 2023 · **Enabling** · Real indoor scenes.

Pairs high-fidelity indoor geometry with registered DSLR and mobile RGB-D observations for scene understanding and novel view synthesis.

[Project](https://scannetpp.mlsg.cit.tum.de/scannetpp/) · [Toolkit](https://github.com/scannetpp/scannetpp)

Benchmark connections: scannetpp. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="multiscan"></a>

### MultiScan (2022)

**[MultiScan: Scalable RGBD Scanning for 3D Environments with Articulated Objects](https://arxiv.org/abs/2203.16840)** — NeurIPS 2022 · **Core** · Real indoor scenes.

Provides RGB-D environments with object/part semantics and articulated-part mobility annotations.

[Project](https://multiscan3d.github.io/) · [Toolkit](https://github.com/smartscenes/multiscan)

Benchmark connections: multiscan. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="scannet200"></a>

### ScanNet200 / LanguageGroundedSemseg (2022)

**[Language-Grounded Indoor 3D Semantic Segmentation in the Wild](https://arxiv.org/abs/2204.07761)** — ECCV 2022 · **Enabling** · Real indoor scenes.

Introduces a 200-category ScanNet benchmark and language-guided feature pretraining to study long-tail indoor semantic segmentation.

[Project](https://rozdavid.github.io/scannet200) · [Code](https://github.com/RozDavid/LanguageGroundedSemseg)

Benchmark connections: scannet200. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="teach"></a>

### TEACh (2022)

**[TEACh: Task-driven Embodied Agents that Chat](https://arxiv.org/abs/2110.00534)** — AAAI 2022 · **Enabling** · Embodied instruction following and planning.

Provides dialog-guided household tasks where an embodied agent asks questions and acts in a simulated environment.

[Project](https://teachingalfred.github.io/) · [Toolkit](https://github.com/alexa/teach)

Benchmark connections: teach. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-14.

<a id="arkitscenes"></a>

### ARKitScenes (2021)

**[ARKitScenes: A Diverse Real-World Dataset for 3D Indoor Scene Understanding Using Mobile RGB-D Data](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/file/66f041e16a60928b05a7e228a89c3799-Paper-round1.pdf)** — NeurIPS Datasets and Benchmarks 2021 · **Enabling** · Real indoor scenes.

Provides mobile RGB-D indoor captures and benchmarks for scene understanding.

[Project](https://github.com/apple-aiml-research/ARKitScenes) · [Toolkit](https://github.com/apple-aiml-research/ARKitScenes)

Resource note: The Apple repository supplies accompanying data-processing and training code; its canonical owner is apple-aiml-research after the apple/ redirect.

Benchmark connections: arkitscenes. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="habitat2"></a>

### Habitat 2.0 (2021)

**[Habitat 2.0: Training Home Assistants to Rearrange their Habitat](https://proceedings.neurips.cc/paper/2021/hash/021bbc7ee20b71134d53e20206bd6feb-Abstract.html)** — NeurIPS 2021 · **Enabling** · Embodied simulators and household tasks.

Combines reconfigurable apartments, physics-enabled simulation, and home-assistant tasks for long-horizon mobile manipulation.

[Project](https://aihabitat.org/docs/habitat2/) · [Toolkit](https://github.com/facebookresearch/habitat-lab)

Benchmark connections: habitat-rearrangement. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-14.

<a id="maniskill"></a>

### ManiSkill (2021)

**[ManiSkill: Generalizable Manipulation Skill Benchmark with Large-Scale Demonstrations](https://datasets-benchmarks-proceedings.neurips.cc/paper_files/paper/2021/hash/eda80a3d5b344bc40f3bc04f65b7a357-Abstract-round2.html)** — NeurIPS Datasets and Benchmarks 2021 · **Enabling** · Manipulation and household-task benchmarks.

Benchmarks generalizable manipulation across diverse objects in physics simulation, with large-scale demonstrations.

[Project](https://maniskill.ai/) · [Code](https://github.com/mani-skill/ManiSkill)

Resource note: Current official framework and simulator repository; distinguish it from the original 2021 paper record.

Checked: 2026-11-13.

<a id="alfred"></a>

### ALFRED (2020)

**[ALFRED: A Benchmark for Interpreting Grounded Instructions for Everyday Tasks](https://openaccess.thecvf.com/content_CVPR_2020/html/Shridhar_ALFRED_A_Benchmark_for_Interpreting_Grounded_Instructions_for_Everyday_Tasks_CVPR_2020_paper.html)** — CVPR 2020 · **Enabling** · Embodied instruction following and planning.

Benchmarks language-guided household task completion through sequences of navigation and object-interaction actions in simulated environments.

[Project](https://askforalfred.com/) · [Toolkit](https://github.com/askforalfred/alfred)

Benchmark connections: alfred. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-14.

<a id="rlbench"></a>

### RLBench (2020)

**[RLBench: The Robot Learning Benchmark & Learning Environment](https://arxiv.org/abs/1909.12271)** — IEEE Robotics and Automation Letters / ICRA 2020 · **Enabling** · Manipulation and household-task benchmarks.

Open large-scale vision-guided manipulation benchmark used for RL, imitation, multi-task, and few-shot learning; some tasks involve opening or changing articulated object state.

Project: — · [Code](https://github.com/stepjam/RLBench)

Benchmark connections: rlbench. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="sapien"></a>

### SAPIEN (2020)

**[SAPIEN: A SimulAted Part-Based Interactive ENvironment](https://openaccess.thecvf.com/content_CVPR_2020/html/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.html)** — CVPR 2020 · **Enabling** · Articulated assets and simulators.

Provides a physics-based, part-interactive simulation environment for articulated-object understanding and manipulation.

[Project](https://sapien.ucsd.edu/) · [Code](https://github.com/haosulab/SAPIEN)

Resource note: Official simulator project and source.

Checked: 2026-11-13.

<a id="embodiedqa"></a>

### EmbodiedQA (2018)

**[Embodied Question Answering](https://openaccess.thecvf.com/content_cvpr_2018/html/Das_Embodied_Question_Answering_CVPR_2018_paper.html)** — CVPR 2018 · **Enabling** · Embodied question answering and 3D reasoning.

Defines an embodied question-answering setting where an agent navigates a 3D environment to gather observations before answering.

[Project](https://embodiedqa.org/) · [Toolkit](https://github.com/facebookresearch/EmbodiedQA)

Benchmark connections: embodiedqa. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-14.

<a id="r2r"></a>

### R2R (2018)

**[Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments](https://openaccess.thecvf.com/content_cvpr_2018/html/Anderson_Vision-and-Language_Navigation_Interpreting_CVPR_2018_paper.html)** — CVPR 2018 · **Enabling** · Embodied navigation and semantic memory.

Introduces navigation in real scanned environments from natural-language route instructions and paired human demonstrations.

[Project](https://bringmeaspoon.org/) · [Toolkit](https://github.com/peteanderson80/Matterport3DSimulator)

Benchmark connections: r2r. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-14.

<a id="scannet-dataset"></a>

### ScanNet (2017)

**[ScanNet: Richly-annotated 3D Reconstructions of Indoor Scenes](https://openaccess.thecvf.com/content_cvpr_2017/html/Dai_ScanNet_Richly-Annotated_3D_CVPR_2017_paper.html)** — CVPR 2017 · **Enabling** · Real indoor scenes.

Provides richly annotated RGB-D reconstructions and benchmark tasks for indoor 3D scene understanding.

[Project](https://www.scan-net.org/) · [Toolkit](https://github.com/ScanNet/ScanNet)

Benchmark connections: scannet, scannet200. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.

<a id="s3dis-dataset"></a>

### S3DIS (2016)

**[A Large-Scale 3D Point Cloud Dataset for Indoor Scene Segmentation](https://openaccess.thecvf.com/content_cvpr_2016/html/Armeni_3D_Semantic_Parsing_CVPR_2016_paper.html)** — CVPR 2016 · **Enabling** · Real indoor scenes.

Provides large indoor point clouds and semantic labels used by room-scale segmentation protocols.

[Project](http://buildingparser.stanford.edu/dataset.html) · Code: —

Benchmark connections: s3dis. This is a relevance link, not a leaderboard claim.

Checked: 2026-11-13.
