# Scene reconstruction and digital twins

> Recovering scene geometry, appearance, camera motion, dynamic structure, and interactive digital twins.

[← Overview](../README.md) · [Full paper index](../PAPERS.md) · [Benchmarks](../BENCHMARKS.md) · [Contribute](../CONTRIBUTING.md)

Papers are grouped by editorial section and ordered newest first within each section. Classification expresses relevance, not a rank.

[Classical multi-view and RGB-D reconstruction](#section-1) · [Neural scene representations and surfaces](#section-2) · [Feed-forward scene reconstruction](#section-3) · [Incremental reconstruction, SLAM and mapping](#section-4) · [Dynamic scene reconstruction](#section-5) · [Multi-state and interaction-based reconstruction](#section-6) · [Visual digital twins and executable structure](#section-7) · [Articulation recovery from static assets](#section-8)

<a id="section-1"></a>

## Classical multi-view and RGB-D reconstruction

| Paper | Focus | Official resources |
| --- | --- | --- |
| [BundleFusion: Real-time Globally Consistent 3D Reconstruction Using On-the-fly Surface Re-integration](https://arxiv.org/abs/1604.01093)<br>ACM Transactions on Graphics (SIGGRAPH) 2017 · core | Jointly estimates globally optimized RGB-D camera poses and reintegrates surfaces online for globally consistent dense reconstruction. | [Project](https://graphics.stanford.edu/projects/bundlefusion/) · [Code](https://github.com/niessner/BundleFusion) · [Details](../PAPERS.md#bundlefusion) |
| [Structure-from-Motion Revisited](https://openaccess.thecvf.com/content_cvpr_2016/html/Schonberger_Structure-From-Motion_Revisited_CVPR_2016_paper.html)<br>CVPR 2016 · core | Reconstructs camera poses and sparse scene structure from image collections with incremental structure from motion; the COLMAP software also provides multi-view stereo. | [Project](https://colmap.github.io/) · [Code](https://github.com/colmap/colmap) · [Details](../PAPERS.md#colmap-sfm) |

<a id="section-2"></a>

## Neural scene representations and surfaces

| Paper | Focus | Official resources |
| --- | --- | --- |
| [3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://arxiv.org/abs/2308.04079)<br>ACM Transactions on Graphics (SIGGRAPH) 2023 · core | Represents a captured scene as optimized anisotropic 3D Gaussians with visibility-aware splatting for real-time radiance-field rendering. | [Project](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) · [Code](https://github.com/graphdeco-inria/gaussian-splatting) · [Details](../PAPERS.md#gaussian-splatting) |
| [Neuralangelo: High-Fidelity Neural Surface Reconstruction](https://openaccess.thecvf.com/content/CVPR2023/html/Li_Neuralangelo_High-Fidelity_Neural_Surface_Reconstruction_CVPR_2023_paper.html)<br>CVPR 2023 · core | Reconstructs high-fidelity surfaces from RGB images through neural volume rendering without requiring auxiliary depth or segmentation data. | Project: — · [Code](https://github.com/NVlabs/neuralangelo) · [Details](../PAPERS.md#neuralangelo) |
| [Instant Neural Graphics Primitives with a Multiresolution Hash Encoding](https://doi.org/10.1145/3528223.3530127)<br>ACM Transactions on Graphics (SIGGRAPH) 2022 · enabling | Introduces a multiresolution hash encoding that makes neural graphics primitives, including NeRF scene fitting, substantially more efficient. | [Project](https://nvlabs.github.io/instant-ngp/) · [Code](https://github.com/NVlabs/instant-ngp) · [Details](../PAPERS.md#instant-ngp) |
| [Mip-NeRF 360: Unbounded Anti-Aliased Neural Radiance Fields](https://openaccess.thecvf.com/content/CVPR2022/html/Barron_Mip-NeRF_360_Unbounded_Anti-Aliased_Neural_Radiance_Fields_CVPR_2022_paper.html)<br>CVPR 2022 · core | Extends neural radiance fields to unbounded scenes with anti-aliased rendering and an explicit distortion regularizer. | [Project](https://jonbarron.info/mipnerf360/) · [Code](https://github.com/google-research/multinerf) · [Details](../PAPERS.md#mipnerf360) |
| [NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis](https://arxiv.org/abs/2003.08934)<br>ECCV 2020 · core | Optimizes a continuous neural field of density and view-dependent radiance for novel-view synthesis of a static captured scene. | [Project](https://www.matthewtancik.com/nerf) · [Code](https://github.com/bmild/nerf) · [Details](../PAPERS.md#nerf) |

<a id="section-3"></a>

## Feed-forward scene reconstruction

| Paper | Focus | Official resources |
| --- | --- | --- |
| [VGGT: Visual Geometry Grounded Transformer](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.html)<br>CVPR 2025 · core | Uses a feed-forward transformer to infer camera parameters, point maps, depth maps, and 3D point tracks from one or many views. | [Project](https://vggt-omega.github.io/) · [Code](https://github.com/facebookresearch/vggt) · [Details](../PAPERS.md#vggt) |
| [DUSt3R: Geometric 3D Vision Made Easy](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_DUSt3R_Geometric_3D_Vision_Made_Easy_CVPR_2024_paper.html)<br>CVPR 2024 · core | Predicts dense 2D-to-3D point maps from uncalibrated image collections, supporting camera recovery and dense scene reconstruction through global alignment. | [Project](https://dust3r.europe.naverlabs.com/) · [Code](https://github.com/naver/dust3r) · [Details](../PAPERS.md#dust3r) |
| [Grounding Image Matching in 3D with MASt3R](https://arxiv.org/abs/2406.09756)<br>ECCV 2024 · core | Adds dense local matching, metric point maps, and scalable global alignment to the DUSt3R reconstruction framework. | [Project](https://europe.naverlabs.com/research/publications/grounding-image-matching-in-3d-with-mast3r/) · [Code](https://github.com/naver/mast3r) · [Details](../PAPERS.md#mast3r) |

<a id="section-4"></a>

## Incremental reconstruction, SLAM and mapping

| Paper | Focus | Official resources |
| --- | --- | --- |
| [SplaTAM: Splat, Track & Map 3D Gaussians for Dense RGB-D SLAM](https://openaccess.thecvf.com/content/CVPR2024/html/Keetha_SplaTAM_Splat_Track__Map_3D_Gaussians_for_Dense_RGB-D_CVPR_2024_paper.html)<br>CVPR 2024 · core | Uses an online RGB-D tracking-and-mapping pipeline with a 3D Gaussian scene map optimized by differentiable rendering. | [Project](https://spla-tam.github.io/) · [Code](https://github.com/spla-tam/SplaTAM) · [Details](../PAPERS.md#splatam) |
| [GO-SLAM: Global Optimization for Consistent 3D Instant Reconstruction](https://arxiv.org/abs/2309.02436)<br>ICCV 2023 · core | Combines pose estimation, loop closing, and continuous surface updates to improve global consistency in dense visual SLAM. | Project: — · [Code](https://github.com/youmi-zym/GO-SLAM) · [Details](../PAPERS.md#go-slam) |
| [NICE-SLAM: Neural Implicit Scalable Encoding for SLAM](https://openaccess.thecvf.com/content/CVPR2022/html/Zhu_NICE-SLAM_Neural_Implicit_Scalable_Encoding_for_SLAM_CVPR_2022_paper.html)<br>CVPR 2022 · core | Uses a hierarchical grid-based neural implicit representation for scalable online dense RGB-D SLAM. | Project: — · [Code](https://github.com/cvg/nice-slam) · [Details](../PAPERS.md#nice-slam) |
| [iMAP: Implicit Mapping and Positioning in Real-Time](https://openaccess.thecvf.com/content/ICCV2021/html/Sucar_iMAP_Implicit_Mapping_and_Positioning_in_Real-Time_ICCV_2021_paper.html)<br>ICCV 2021 · core | Jointly learns a scene-specific implicit map and RGB-D camera poses online from a stream of observations. | [Project](https://edgarsucar.github.io/iMAP/) · Code: — · [Details](../PAPERS.md#imap) |
| [NeuralRecon: Real-Time Coherent 3D Reconstruction from Monocular Video](https://openaccess.thecvf.com/content/CVPR2021/html/Sun_NeuralRecon_Real-Time_Coherent_3D_Reconstruction_From_Monocular_Video_CVPR_2021_paper.html)<br>CVPR 2021 · core | Fuses monocular-video features into a sparse voxel representation to reconstruct coherent scene surfaces in real time. | [Project](https://zju3dv.github.io/neuralrecon/) · [Code](https://github.com/zju3dv/NeuralRecon) · [Details](../PAPERS.md#neuralrecon) |

<a id="section-5"></a>

## Dynamic scene reconstruction

| Paper | Focus | Official resources |
| --- | --- | --- |
| [MonST3R: A Simple Approach for Estimating Geometry in the Presence of Motion](https://arxiv.org/abs/2410.03825)<br>ICLR 2025 · core | Estimates per-timestep geometry directly from dynamic scenes, extending point-map reconstruction beyond a static-scene assumption. | [Project](https://monst3r-project.github.io/) · [Code](https://github.com/Junyi42/monst3r) · [Details](../PAPERS.md#monst3r) |
| [4D Gaussian Splatting for Real-Time Dynamic Scene Rendering](https://openaccess.thecvf.com/content/CVPR2024/html/Wu_4D_Gaussian_Splatting_for_Real-Time_Dynamic_Scene_Rendering_CVPR_2024_paper.html)<br>CVPR 2024 · core | Models a dynamic scene with a canonical 3D Gaussian representation and learned temporal deformation for efficient real-time rendering. | Project: — · [Code](https://github.com/hustvl/4DGaussians) · [Details](../PAPERS.md#four-d-gaussian-splatting) |
| [D-NeRF: Neural Radiance Fields for Dynamic Scenes](https://openaccess.thecvf.com/content/CVPR2021/html/Pumarola_D-NeRF_Neural_Radiance_Fields_for_Dynamic_Scenes_CVPR_2021_paper.html)<br>CVPR 2021 · core | Extends neural radiance fields with a learned deformation field for rendering non-rigidly moving scenes over time. | [Project](https://www.albertpumarola.com/research/D-NeRF/index.html) · [Code](https://github.com/albertpumarola/D-NeRF) · [Details](../PAPERS.md#dnerf) |

<a id="section-6"></a>

## Multi-state and interaction-based reconstruction

| Paper | Focus | Official resources |
| --- | --- | --- |
| [Articulation in Motion: Prior-free Part Mobility Analysis for Articulated Objects By Dynamic-Static Disentanglement](https://arxiv.org/abs/2603.02910)<br>arXiv preprint 2026 · core | Uses an interaction video and start-state scan for part decomposition, kinematics, and an interactive digital replica. | [Project](https://haoai-1997.github.io/AiM/) · Code: — · [Details](../PAPERS.md#articulation-in-motion) |
| [ArtHOI: Articulated Human-Object Interaction Synthesis by 4D Reconstruction from Video Priors](https://arxiv.org/abs/2603.04338)<br>arXiv preprint 2026 · core | Uses monocular video priors and initial 3D assets for articulated human-object interaction synthesis by 4D reconstruction. | [Project](https://arthoi.github.io/) · Code: — · [Details](../PAPERS.md#arthoi) |
| [PartRM: Modeling Part-Level Dynamics with Large Cross-State Reconstruction Model](https://openaccess.thecvf.com/content/CVPR2025/html/Gao_PartRM_Modeling_Part-Level_Dynamics_with_Large_Cross-State_Reconstruction_Model_CVPR_2025_paper.html)<br>CVPR 2025 · core | Models appearance, geometry, and part-level motion from one image plus user-specified drags. | [Project](https://partrm.c7w.tech/) · [Code](https://github.com/GasaiYU/PartRM) · [Details](../PAPERS.md#partrm) |
| [VideoArtGS: Building Digital Twins of Articulated Objects from Monocular Video](https://arxiv.org/abs/2509.17647)<br>arXiv preprint 2025 · core | Targets geometry, part segmentation, and articulation for digital twins from monocular video. | [Project](https://videoartgs.github.io) · Code: — · [Details](../PAPERS.md#videoartgs) |
| [Neural Implicit Representation for Building Digital Twins of Unknown Articulated Objects](https://openaccess.thecvf.com/content/CVPR2024/html/Weng_Neural_Implicit_Representation_for_Building_Digital_Twins_of_Unknown_Articulated_CVPR_2024_paper.html)<br>CVPR 2024 · core | Optimizes part geometry, segmentation, and joints from two RGB-D scans in different states. | [Project](https://nvlabs.github.io/DigitalTwinArt/) · [Code](https://github.com/NVlabs/DigitalTwinArt) · [Details](../PAPERS.md#digital-twin-art) |
| [REACTO: Reconstructing Articulated Objects from a Single Video](https://openaccess.thecvf.com/content/CVPR2024/html/Song_REACTO_Reconstructing_Articulated_Objects_from_a_Single_Video_CVPR_2024_paper.html)<br>CVPR 2024 · core | Reconstructs general articulated objects from one video with rigging and motion-aware component modeling. | [Project](https://chaoyuesong.github.io/REACTO/) · Code: — · [Details](../PAPERS.md#reacto) |
| [PARIS: Part-level Reconstruction and Motion Analysis for Articulated Objects](https://openaccess.thecvf.com/content/ICCV2023/html/Liu_PARIS_Part-level_Reconstruction_and_Motion_Analysis_for_Articulated_Objects_ICCV_2023_paper.html)<br>ICCV 2023 · core | Recovers part-level shape, appearance, and motion from multi-view observations in two states. | [Project](https://3dlg-hcvc.github.io/paris/) · [Code](https://github.com/3dlg-hcvc/paris) · [Details](../PAPERS.md#paris) |
| [Ditto: Building Digital Twins of Articulated Objects From Interaction](https://openaccess.thecvf.com/content/CVPR2022/html/Jiang_Ditto_Building_Digital_Twins_of_Articulated_Objects_From_Interaction_CVPR_2022_paper.html)<br>CVPR 2022 · core | Uses visual observations before and after interaction to recover part geometry and articulation. | [Project](https://ut-austin-rpl.github.io/Ditto/) · [Code](https://github.com/UT-Austin-RPL/Ditto) · [Details](../PAPERS.md#ditto) |

<a id="section-7"></a>

## Visual digital twins and executable structure

| Paper | Focus | Official resources |
| --- | --- | --- |
| [Articulat3D: Reconstructing Articulated Digital Twins From Monocular Videos with Geometric and Motion Constraints](https://arxiv.org/abs/2603.11606)<br>arXiv preprint 2026 · core | Builds articulated digital twins from casually captured monocular video using geometric and motion constraints. | [Project](https://maxwell-zhao.github.io/Articulat3D) · Code: — · [Details](../PAPERS.md#articulat3d) |
| [DRAWER: Digital Reconstruction and Articulation With Environment Realism](https://openaccess.thecvf.com/content/CVPR2025/html/Xia_DRAWER_Digital_Reconstruction_and_Articulation_With_Environment_Realism_CVPR_2025_paper.html)<br>CVPR 2025 · core | Converts video of a static scene into an interactive environment with reconstructed objects and articulated doors. | [Project](https://xiahongchi.github.io/DRAWER/) · [Code](https://github.com/xiahongchi/DRAWER) · [Details](../PAPERS.md#drawer) |
| [Real2Code: Reconstruct Articulated Objects via Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/hash/028fcbcf85435d39a40c4d61b42c99a4-Abstract-Conference.html)<br>ICLR 2025 · core | Reconstructs parts from visual observations, including multi-view RGB, and predicts articulation code from oriented bounding boxes using an LLM. | Project: — · [Code](https://github.com/MandiZhao/real2code) · [Details](../PAPERS.md#real2code) |
| [URDFormer: A Pipeline for Constructing Articulated Simulation Environments from Real-World Images](https://urdformer.github.io/)<br>RSS 2024 · core | Predicts a URDF from a single real-world image using localized part boxes and predefined meshes; supports simulation and policy training. | [Project](https://urdformer.github.io/) · [Code](https://github.com/WEIRDLabUW/urdformer) · [Details](../PAPERS.md#urdformer) |

<a id="section-8"></a>

## Articulation recovery from static assets

| Paper | Focus | Official resources |
| --- | --- | --- |
| [REACT3D: Recovering Articulations for Interactive Physical 3D Scenes](https://doi.org/10.1109/LRA.2026.3674028)<br>IEEE Robotics and Automation Letters 2026 · core | Converts static indoor scenes into simulation-ready interactive replicas through detection, articulation inference, completion, and assembly. | [Project](https://react3d.github.io/) · [Code](https://github.com/troyehuang/REACT3D) · [Details](../PAPERS.md#react3d) |
| [S2O: Static to Openable Enhancement for Articulated 3D Objects](https://openaccess.thecvf.com/content/WACV2026/html/Iliash_S2O_Static_to_Openable_Enhancement_for_Articulated_3D_Objects_WACV_2026_paper.html)<br>WACV 2026 · core | Defines static-to-openable enhancement: part detection, motion prediction, and interior completion from static 3D assets. | [Project](https://3dlg-hcvc.github.io/s2o/) · [Code](https://github.com/3dlg-hcvc/s2o) · [Details](../PAPERS.md#s2o) |
| [MagicArticulate: Make Your 3D Models Articulation-Ready](https://openaccess.thecvf.com/content/CVPR2025/html/Song_MagicArticulate_Make_Your_3D_Models_Articulation-Ready_CVPR_2025_paper.html)<br>CVPR 2025 · core | Adds structure and motion to static 3D models and releases Articulation-XL2.0 data. | [Project](https://chaoyuesong.github.io/MagicArticulate/) · [Code](https://github.com/Seed3D/MagicArticulate) · [Details](../PAPERS.md#magicarticulate) |
