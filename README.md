# Awesome 3D Scene Understanding and Interaction

An illustrated survey of 3D scene perception, reconstruction, generation, and embodied interaction, with papers, official project pages, code, and benchmarks.

**[Browse topics](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/#reading-routes) · [Full survey](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/survey.html) · [Search papers](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/library.html)**

Read the website in [English](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/) or [中文](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/zh/).

[![Four research areas illustrated on a RoboCasa kitchen scene: perception identifies objects and parts, reconstruction builds a 3D scene from images and scans, generation creates layouts and environments, and robots navigate and manipulate. Numbered labels and arrows connect each task to the scene.](assets/survey-teaser.svg)](assets/survey-teaser.png)

## Contents

[Survey chapters](#survey-chapters) · [Reading routes](#reading-routes) · [Research map](#research-map) · [Benchmarks](#benchmarks) · [Contributing](#contributing)

| Reading routes | Topic collections |
| --- | --- |
| [🏙️ Recognize objects in a 3D scene](#route-scene-perception)<br>[🗣️ Find objects and parts using language](#route-language-and-function)<br>[🏗️ Reconstruct a room from photos or video](#route-scene-reconstruction)<br>[🌍 Generate a 3D environment](#route-scene-generation)<br>[⚙️ Work out how doors and drawers move](#route-articulated-perception)<br>[🧩 Rebuild an object with moving parts](#route-reconstruction)<br>[🛠️ Generate objects with joints](#route-generation)<br>[🧭 Help an agent find its way](#route-spatial-navigation)<br>[💡 Let an agent explore and answer questions](#route-embodied-reasoning)<br>[🦾 Get a robot to grasp, push, or open](#route-manipulation)<br>[🤖 Understand general-purpose robot policies](#route-policies-and-agents)<br>[📊 Pick a dataset and decide what to measure](#route-data-and-evaluation) | [Scene and functional perception](topics/perception.md)<br>[Scene reconstruction and digital twins](topics/reconstruction.md)<br>[Scene generation and asset authoring](topics/generation.md)<br>[Embodied agents and robotic interaction](topics/robotics.md)<br>[Datasets, simulators, and benchmarks](topics/datasets.md)<br><br>**Resources**<br>[Survey chapters](#survey-chapters)<br>[Research map](#research-map)<br>[Paper index](PAPERS.md)<br>[Benchmark guide](BENCHMARKS.md)<br>[Contributing](CONTRIBUTING.md) |

## Survey chapters

The survey explains the methods with figures and videos from the original projects. Read it in order, or open a chapter below. Both English and Chinese editions are available.

| Chapter | What it covers | Read |
| --- | --- | --- |
| **01. Scope and overview** | How scene perception, reconstruction, generation, and interaction fit together. | [English](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/overview.html) · [中文](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/zh/overview.html) |
| **02. Scene perception** | Point-cloud features, segmentation, language grounding, parts, and motion. | [English](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/perception.html) · [中文](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/zh/perception.html) |
| **03. Scene reconstruction** | Reconstructing 3D scenes from images and scans, including appearance, camera poses, and changing geometry. | [English](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/reconstruction.html) · [中文](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/zh/reconstruction.html) |
| **04. Scene generation** | Layouts, visual worlds, procedural environments, and articulated assets. | [English](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/generation.html) · [中文](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/zh/generation.html) |
| **05. Robots & embodied agents** | Spatial memory, navigation, planning, manipulation, touch, and generalist policies. | [English](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/robotics.html) · [中文](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/zh/robotics.html) |
| **06. Datasets and evaluation** | Scene datasets, functional annotations, simulators, and robot task evaluation. | [English](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/datasets.html) · [中文](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/zh/datasets.html) |
| **07. Research directions** | Dynamic environments, active perception, generated training data, and world models. | [English](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/outlook.html) · [中文](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/zh/outlook.html) |

## Reading routes

Each step links to an explanation in the survey, followed by papers that develop the idea. Read the explanation first, or go straight to the papers if you already know the background.

<a id="route-scene-perception"></a>

### 🏙️ Recognize objects in a 3D scene

*Point features → semantic labels → separate object instances*

Labeling points as 'chair' doesn't tell you how many chairs there are. Start with point-cloud features, then look at the methods that separate individual objects.

| Stage | Suggested reading | What to look for |
| --- | --- | --- |
| **1. Start with what a point feature remembers** | [Perception §1](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/perception.html?route=scene-perception&step=1#section-1)<br>[PointNet](PAPERS.md#pointnet) · [PointNet++](PAPERS.md#pointnet-plus-plus) | PointNet summarizes a whole set; PointNet++ brings local neighborhoods back into the representation. |
| **2. See how the backbone scales up** | [Perception §1](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/perception.html?route=scene-perception&step=2#section-1)<br>[PTv3](PAPERS.md#ptv3) · [Volt](PAPERS.md#volume-transformer) | Compare Point Transformer V3's serialized points with volumetric patch tokens and global attention. |
| **3. Turn labels into individual objects** | [Perception §2](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/perception.html?route=scene-perception&step=3#section-2)<br>[Mask3D](PAPERS.md#mask3d) · [OneFormer3D](PAPERS.md#oneformer3d) | Watch point features become semantic, instance, and panoptic predictions rather than one class label per point. |
| **4. Ask what survives a new dataset** | [Perception §1](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/perception.html?route=scene-perception&step=4#section-1) · [Datasets §6](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/datasets.html?route=scene-perception&step=4#section-6)<br>[DITR](PAPERS.md#ditr) · [PPT](PAPERS.md#multi-dataset-point-prompt-training) | Contrast transferred 2D features with training across multiple 3D datasets, then ask what was actually held out. |

**Try it:** Take a kitchen scan and mark what a semantic map, an instance map, and a panoptic map would each preserve.

**Explore more:** [Scene and functional perception](topics/perception.md) · [Datasets, simulators, and benchmarks](topics/datasets.md) · [Back to contents](#contents)

<a id="route-language-and-function"></a>

### 🗣️ Find objects and parts using language

*Open vocabulary → scene relations → actionable parts*

Finding a fridge and opening it are different jobs. Start with text queries, then see how methods locate doors, handles, and other parts a robot can use.

| Stage | Suggested reading | What to look for |
| --- | --- | --- |
| **1. Query a map with text** | [Perception §3](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/perception.html?route=language-and-function&step=1#section-3)<br>[OpenScene](PAPERS.md#openscene) · [ConceptFusion](PAPERS.md#conceptfusion) | See how visual-language features answer queries that a fixed category list cannot anticipate. |
| **2. Find the particular object being described** | [Perception §3](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/perception.html?route=language-and-function&step=2#section-3) · [Perception §2](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/perception.html?route=language-and-function&step=2#section-2)<br>[OpenMask3D](PAPERS.md#openmask3d) · [Open3DIS](PAPERS.md#open3dis) | Compare how 2D observations and 3D proposals turn an open-vocabulary query into an object mask. |
| **3. Understand descriptions such as “the one on the left”** | [Perception §3](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/perception.html?route=language-and-function&step=3#section-3)<br>[ScanRefer](PAPERS.md#scanrefer) · [ConceptGraphs](PAPERS.md#conceptgraphs) | Put referring-expression localization beside a scene graph: one finds an object, the other keeps relations available for planning. |
| **4. Find the door or handle needed for the task** | [Perception §4](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/perception.html?route=language-and-function&step=4#section-4)<br>[SceneFun3D](PAPERS.md#scenefun3d) · [GAPartNet](PAPERS.md#gapartnet) | Follow task descriptions and affordances down to actionable parts, part poses, and candidate interaction regions. |

**Try it:** Compare the regions needed for 'find the refrigerator' and 'open the refrigerator': object, door, handle, and action space.

**Explore more:** [Scene and functional perception](topics/perception.md) · [Embodied agents and robotic interaction](topics/robotics.md) · [Back to contents](#contents)

<a id="route-scene-reconstruction"></a>

### 🏗️ Reconstruct a room from photos or video

*Camera geometry → neural representations → learned geometry → online mapping*

Do you need a new camera view, a surface model, or a map that updates as you move? That choice matters when you pick a reconstruction method.

| Stage | Suggested reading | What to look for |
| --- | --- | --- |
| **1. Recover cameras and geometry** | [Reconstruction §1](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/reconstruction.html?route=scene-reconstruction&step=1#section-1)<br>[COLMAP](PAPERS.md#colmap-sfm) · [BundleFusion](PAPERS.md#bundlefusion) | Compare camera-and-sparse-structure recovery from images with globally consistent RGB-D surface fusion. |
| **2. Represent scene appearance** | [Reconstruction §2](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/reconstruction.html?route=scene-reconstruction&step=2#section-2)<br>[NeRF](PAPERS.md#nerf) · [3D Gaussian Splatting](PAPERS.md#gaussian-splatting) | Contrast a continuous radiance field with explicit Gaussians, keeping rendering quality separate from surface geometry. |
| **3. Predict geometry directly** | [Reconstruction §3](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/reconstruction.html?route=scene-reconstruction&step=3#section-3)<br>[DUSt3R](PAPERS.md#dust3r) · [VGGT](PAPERS.md#vggt) | Study feed-forward point maps, camera recovery, depth, and how much multi-view consistency is built in. |
| **4. Map an ongoing observation stream** | [Reconstruction §4](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/reconstruction.html?route=scene-reconstruction&step=4#section-4)<br>[NICE-SLAM](PAPERS.md#nice-slam) · [SplaTAM](PAPERS.md#splatam) | Compare implicit and Gaussian maps as both map and camera pose are updated during a stream. |
| **5. Handle a changing scene** | [Reconstruction §5](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/reconstruction.html?route=scene-reconstruction&step=5#section-5)<br>[MonST3R](PAPERS.md#monst3r) · [4D Gaussian Splatting](PAPERS.md#four-d-gaussian-splatting) | Separate estimating changing geometry and cameras from merely rendering a dynamic scene. |

**Try it:** For one captured room, list which methods need depth, camera poses, multiple views, or scene-specific optimization, and which outputs support rendering or geometry queries.

**Explore more:** [Scene reconstruction and digital twins](topics/reconstruction.md) · [Scene and functional perception](topics/perception.md) · [Back to contents](#contents)

<a id="route-scene-generation"></a>

### 🌍 Generate a 3D environment

*Layouts → visual worlds → procedural environments → simulation tasks*

Start by arranging furniture, then look at how methods build whole rooms and worlds. If a robot needs to use the result, there's more to check than how it looks.

| Stage | Suggested reading | What to look for |
| --- | --- | --- |
| **1. Place objects before rendering them** | [Generation §2](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/generation.html?route=scene-generation&step=1#section-2)<br>[ATISS](PAPERS.md#atiss) · [DiffuScene](PAPERS.md#diffuscene) | Compare autoregressive layout prediction with diffusion over scene configurations. |
| **2. Turn a room request into spatial constraints** | [Generation §2](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/generation.html?route=scene-generation&step=2#section-2)<br>[LayoutGPT](PAPERS.md#layoutgpt) · [InstructScene](PAPERS.md#instructscene) | Ask whether the text becomes explicit object relations and layout constraints, or only a loose conditioning signal. |
| **3. Build a world from a prompt or image** | [Generation §3](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/generation.html?route=scene-generation&step=3#section-3) · [Generation §4](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/generation.html?route=scene-generation&step=3#section-4)<br>[Text2Room](PAPERS.md#text2room) · [WonderWorld](PAPERS.md#wonderworld) | Contrast a generated textured room mesh with interactive scene expansion from an image. |
| **4. Sample a training world procedurally** | [Generation §5](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/generation.html?route=scene-generation&step=4#section-5)<br>[ProcTHOR](PAPERS.md#procthor) · [Infinigen](PAPERS.md#infinigen) | Compare interactive indoor-house sampling with procedural natural-world geometry and materials. |
| **5. Give generation a task and a simulator** | [Generation §5](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/generation.html?route=scene-generation&step=5#section-5) · [Generation §7](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/generation.html?route=scene-generation&step=5#section-7)<br>[Holodeck](PAPERS.md#holodeck) · [RoboGen](PAPERS.md#robogen) | Read for task-driven scene construction and the interface between generated environments and agent training. |

**Try it:** Give one room description to a layout generator, a visual scene generator, and a simulator generator. Write down what each returns and what a robot would still be missing.

**Explore more:** [Scene generation and asset authoring](topics/generation.md) · [Datasets, simulators, and benchmarks](topics/datasets.md) · [Back to contents](#contents)

<a id="route-articulated-perception"></a>

### ⚙️ Work out how doors and drawers move

*Parts → joints and pose → tracking → scene articulation*

A robot needs to know which side a door hinges on and which way a drawer slides. Read about finding movable parts, estimating motion, and tracking their state.

| Stage | Suggested reading | What to look for |
| --- | --- | --- |
| **1. Separate a moving part from its motion** | [Perception §5](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/perception.html?route=articulated-perception&step=1#section-5) · [Perception §4](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/perception.html?route=articulated-perception&step=1#section-4)<br>[Shape2Motion](PAPERS.md#shape2motion) · [ANCSH](PAPERS.md#ancsh) | Compare a motion-part decomposition with category-level pose and canonical part coordinates: which variables make the joint explicit? |
| **2. Keep track of a moving joint over time** | [Perception §5](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/perception.html?route=articulated-perception&step=2#section-5)<br>[CAPTRA](PAPERS.md#captra) | Study how previous-frame estimates support online per-part pose tracking. |
| **3. Infer opening parts from one image** | [Perception §4](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/perception.html?route=articulated-perception&step=3#section-4)<br>[OPD](PAPERS.md#opd) · [OPDMulti](PAPERS.md#opdmulti) | Follow openable-part detection and axis estimation from single-object to multi-object images. |
| **4. Carry articulation into a cluttered room** | [Perception §4](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/perception.html?route=articulated-perception&step=4#section-4) · [Perception §5](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/perception.html?route=articulated-perception&step=4#section-5)<br>[Articulate3D](PAPERS.md#articulate3d) · [Segment–Snap](PAPERS.md#segment-snap) | Examine scene-level parts, handles, connectivity, and articulation predictions. |

**Try it:** For one door and one drawer, write the part mask, joint type, axis, origin, and state a robot would need before acting.

**Explore more:** [Scene and functional perception](topics/perception.md) · [Scene reconstruction and digital twins](topics/reconstruction.md) · [Back to contents](#contents)

<a id="route-reconstruction"></a>

### 🧩 Rebuild an object with moving parts

*Observations → geometry and motion → executable models*

A reconstructed cabinet may look right but still have no doors that open. Here's how methods recover parts and joints so the model can move in a simulator.

| Stage | Suggested reading | What to look for |
| --- | --- | --- |
| **1. Use state changes as evidence** | [Reconstruction §5](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/reconstruction.html?route=reconstruction&step=1#section-5)<br>[Ditto](PAPERS.md#ditto) · [PARIS](PAPERS.md#paris) | Compare before/after interaction observations with multi-view capture in two states: what becomes observable only after motion? |
| **2. Recover parts and joints from video** | [Reconstruction §5](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/reconstruction.html?route=reconstruction&step=2#section-5)<br>[Articulat3D](PAPERS.md#articulat3d) · [VideoArtGS](PAPERS.md#videoartgs) | Compare how the methods recover shape, separate moving parts, and estimate joints from a monocular video. |
| **3. Write the result into an executable model** | [Reconstruction §7](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/reconstruction.html?route=reconstruction&step=3#section-7)<br>[Real2Code](PAPERS.md#real2code) · [URDFormer](PAPERS.md#urdformer) | Compare reconstructed parts and articulation code with single-image, mesh-based URDF prediction. |
| **4. Add motion to a static asset** | [Reconstruction §7](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/reconstruction.html?route=reconstruction&step=4#section-7) · [Reconstruction §6](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/reconstruction.html?route=reconstruction&step=4#section-6)<br>[S2O](PAPERS.md#s2o) · [REACT3D](PAPERS.md#react3d) | Inspect part detection, motion inference, hidden-geometry completion, and scene assembly. |

**Try it:** Make a small input/output table: single image, two states, video, or static mesh in; geometry, joints, and executable assets out.

**Explore more:** [Scene reconstruction and digital twins](topics/reconstruction.md) · [Scene generation and asset authoring](topics/generation.md) · [Back to contents](#contents)

<a id="route-generation"></a>

### 🛠️ Generate objects with joints

*Part graphs → conditional generation → asset programs*

Generating a cabinet with working doors means producing more than its shape. Look at how models generate parts, connections, and motion parameters together.

| Stage | Suggested reading | What to look for |
| --- | --- | --- |
| **1. Write down the part graph first** | [Generation §6](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/generation.html?route=generation&step=1#section-6)<br>[NAP](PAPERS.md#nap) · [CAGE](PAPERS.md#cage) | Read for graph representations, part geometry, motion parameters, and structural constraints. |
| **2. Condition the graph on evidence or language** | [Generation §6](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/generation.html?route=generation&step=2#section-6)<br>[PhysNAP](PAPERS.md#physnap) · [ArtFormer](PAPERS.md#artformer) | Compare physical guidance and partial observations with text-conditioned tree generation; note which constraint fixes which ambiguity. |
| **3. Infer a movable asset from one view** | [Generation §6](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/generation.html?route=generation&step=3#section-6)<br>[SINGAPO](PAPERS.md#singapo) · [PAct](PAPERS.md#pact) | Compare plausible geometry and kinematics inferred from one image. |
| **4. Generate the program behind the asset** | [Generation §6](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/generation.html?route=generation&step=4#section-6) · [Generation §7](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/generation.html?route=generation&step=4#section-7)<br>[Articulate-Anything](PAPERS.md#articulate-anything) · [Articraft](PAPERS.md#articraft) | Trace how language/vision models produce programs defining parts, joints, and simulator assets. |

**Try it:** Draw two plausible models of the same closed cabinet. What does the image settle, and what must the generator invent?

**Explore more:** [Scene generation and asset authoring](topics/generation.md) · [Scene reconstruction and digital twins](topics/reconstruction.md) · [Back to contents](#contents)

<a id="route-spatial-navigation"></a>

### 🧭 Help an agent find its way

*Spatial maps → semantic goals → language instructions → lifelong navigation*

The target may be out of sight, and the instruction may be vague. See how maps, exploration, and memory help an agent decide where to go.

| Stage | Suggested reading | What to look for |
| --- | --- | --- |
| **1. Put language features on a map** | [Robotics §2](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/robotics.html?route=spatial-navigation&step=1#section-2)<br>[VLMaps](PAPERS.md#vlmaps) | See how visual-language features are fused into a spatial map that can name both a goal and an obstacle. |
| **2. Choose where to look next** | [Robotics §2](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/robotics.html?route=spatial-navigation&step=2#section-2)<br>[VLFM](PAPERS.md#vlfm) | Ask how frontier exploration changes once the robot can recognize a semantic goal from its current view. |
| **3. Turn route language into landmarks** | [Robotics §2](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/robotics.html?route=spatial-navigation&step=3#section-2) · [Robotics §3](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/robotics.html?route=spatial-navigation&step=3#section-3)<br>[LM-Nav](PAPERS.md#lm-nav) | Trace a named landmark from language to visual grounding and then to the navigation controller. |
| **4. Test whether memory helps after the first goal** | [Datasets §5](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/datasets.html?route=spatial-navigation&step=4#section-5)<br>[R2R](PAPERS.md#r2r) · [GOAT-Bench](PAPERS.md#goat-bench) | Compare one-off route following with repeated category, image, and language goals that reward retaining scene memory. |

**Try it:** For “find the mug near the sofa,” separate the target description, map state, next exploration move, and memory carried over from earlier goals.

**Explore more:** [Embodied agents and robotic interaction](topics/robotics.md) · [Datasets, simulators, and benchmarks](topics/datasets.md) · [Back to contents](#contents)

<a id="route-embodied-reasoning"></a>

### 💡 Let an agent explore and answer questions

*Gather observations → ground questions → reason → plan*

To answer 'what is on the table?', an agent may need to go and look. This route covers gathering observations, reasoning about the scene, and planning what to do next.

| Stage | Suggested reading | What to look for |
| --- | --- | --- |
| **1. Decide what evidence the question needs** | [Datasets §5](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/datasets.html?route=embodied-reasoning&step=1#section-5) · [Robotics §2](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/robotics.html?route=embodied-reasoning&step=1#section-2)<br>[EmbodiedQA](PAPERS.md#embodiedqa) · [OpenEQA](PAPERS.md#openeqa) | Compare navigating to gather fresh evidence with answering from episodic memory and active exploration. |
| **2. Give a language model a scene to reason over** | [Robotics §3](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/robotics.html?route=embodied-reasoning&step=2#section-3)<br>[3D-LLM](PAPERS.md#3d-llm) | Study the interface between 3D scene features and language-based questions, dialogue, and plans. |
| **3. Reuse scene features across tasks** | [Robotics §3](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/robotics.html?route=embodied-reasoning&step=3#section-3) · [Robotics §6](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/robotics.html?route=embodied-reasoning&step=3#section-6)<br>[LEO](PAPERS.md#leo) · [PaLM-E](PAPERS.md#palm-e) | Compare 3D vision-language-action instruction tuning with language models that receive continuous visual and robot-state inputs. |
| **4. Reject a plan that cannot be executed** | [Robotics §3](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/robotics.html?route=embodied-reasoning&step=4#section-3)<br>[LLM-Planner](PAPERS.md#llm-planner) · [SayCan](PAPERS.md#saycan) | Contrast controller-grounded plans with skill selection constrained by learned feasibility; where can each stop a bad action? |

**Try it:** Ask “what is on the kitchen table?” from remembered images, then decide what missing evidence would justify one more action.

**Explore more:** [Embodied agents and robotic interaction](topics/robotics.md) · [Datasets, simulators, and benchmarks](topics/datasets.md) · [Back to contents](#contents)

<a id="route-manipulation"></a>

### 🦾 Get a robot to grasp, push, or open

*Affordances → motion planning → feedback → mobile manipulation*

Where should the robot make contact, which way should it move, and what should it do if that fails? Read about affordances, motion estimates, and feedback from touch.

| Stage | Suggested reading | What to look for |
| --- | --- | --- |
| **1. Choose a contact region** | [Robotics §4](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/robotics.html?route=manipulation&step=1#section-4)<br>[Where2Act](PAPERS.md#where2act) · [EnvAwareAfford](PAPERS.md#env-aware-affordance) | Compare actionability predictions with affordances that explicitly account for occlusion and robot position. |
| **2. Represent how the object can move** | [Robotics §4](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/robotics.html?route=manipulation&step=2#section-4)<br>[FlowBot3D](PAPERS.md#flowbot3d) · [GAMMA](PAPERS.md#gamma) | Contrast dense motion fields with articulation models and adaptive joint estimation before choosing a trajectory. |
| **3. Let contact revise the motion hypothesis** | [Robotics §5](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/robotics.html?route=manipulation&step=3#section-5)<br>[FlowBotHD](PAPERS.md#flowbothd) · [Tac-Man](PAPERS.md#tacman) | Use observation history for uncertain motion hypotheses, then see how tactile feedback changes the controller. |
| **4. Move the base as well as the arm** | [Robotics §4](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/robotics.html?route=manipulation&step=4#section-4) · [Robotics §2](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/robotics.html?route=manipulation&step=4#section-2)<br>[MOSART](PAPERS.md#mosart) | See how perception, base navigation, whole-body planning, grasping, and adaptation have to agree at a real site. |

**Try it:** Trace one failed door-opening attempt: what would a new camera view, contact measurement, or base move change?

**Explore more:** [Embodied agents and robotic interaction](topics/robotics.md) · [Scene and functional perception](topics/perception.md) · [Back to contents](#contents)

<a id="route-policies-and-agents"></a>

### 🤖 Understand general-purpose robot policies

*Action learning → vision-language-action → planning and recovery*

Some models predict actions directly; others make a language plan first. Compare these approaches and the scene information they need during a task.

| Stage | Suggested reading | What to look for |
| --- | --- | --- |
| **1. Sample actions from demonstrations** | [Robotics §6](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/robotics.html?route=policies-and-agents&step=1#section-6)<br>[Diffusion Policy](PAPERS.md#diffusion-policy) | See how conditional action diffusion uses visual input and receding-horizon execution rather than one fixed trajectory. |
| **2. Add language to the action model** | [Robotics §6](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/robotics.html?route=policies-and-agents&step=2#section-6)<br>[π0](PAPERS.md#pi-zero) · [π0.5](PAPERS.md#pi-zero-point-five) | Compare flow-matching action experts with co-training across robot and semantic data. |
| **3. Compare two open policy families** | [Robotics §6](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/robotics.html?route=policies-and-agents&step=3#section-6)<br>[OpenVLA](PAPERS.md#openvla) · [Octo](PAPERS.md#octo) | Contrast a vision-language-action model with a transformer diffusion policy across embodiments and adaptation settings. |
| **4. Check language plans against the scene** | [Robotics §3](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/robotics.html?route=policies-and-agents&step=4#section-3)<br>[SayCan](PAPERS.md#saycan) · [VoxPoser](PAPERS.md#voxposer) | Compare affordance-value-guided skill selection with programs that build spatial 3D value maps. |
| **5. Recover after a failed interaction** | [Robotics §3](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/robotics.html?route=policies-and-agents&step=5#section-3) · [Robotics §7](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/robotics.html?route=policies-and-agents&step=5#section-7)<br>[SAGE](PAPERS.md#sage) | Track how semantic, actionable parts become an executable policy and a feedback-driven retry. |

**Try it:** For “put the cup in the cabinet,” separate task planning, scene grounding, contact selection, and action execution.

**Explore more:** [Embodied agents and robotic interaction](topics/robotics.md) · [Datasets, simulators, and benchmarks](topics/datasets.md) · [Back to contents](#contents)

<a id="route-data-and-evaluation"></a>

### 📊 Pick a dataset and decide what to measure

*Scene labels → functional annotations → simulation → household tasks*

Scene segmentation and opening a cabinet need different data and different tests. Start with the ability you want to measure, then choose a benchmark that can test it.

| Stage | Suggested reading | What to look for |
| --- | --- | --- |
| **1. Choose the scene evidence you need** | [Datasets §1](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/datasets.html?route=data-and-evaluation&step=1#section-1)<br>[ScanNet++](PAPERS.md#scannetpp) · [ScanNet200 / LanguageGroundedSemseg](PAPERS.md#scannet200) | Compare high-fidelity scene capture with long-tail semantic and instance-label coverage; neither one alone defines the task. |
| **2. Add labels for function and motion** | [Datasets §2](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/datasets.html?route=data-and-evaluation&step=2#section-2)<br>[MultiScan](PAPERS.md#multiscan) · [SceneFun3D](PAPERS.md#scenefun3d) · [Articulate3D](PAPERS.md#articulate3d) | Compare mobility annotations, task-grounded functional regions, and executable articulated scene structure. |
| **3. Move from annotations to interactive assets** | [Datasets §4](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/datasets.html?route=data-and-evaluation&step=3#section-4)<br>[SAPIEN](PAPERS.md#sapien) · [Arti-PG](PAPERS.md#arti-pg) | Compare physics-based part interaction with procedurally generated articulated-object data. |
| **4. Check what a manipulation score really measures** | [Datasets §4](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/datasets.html?route=data-and-evaluation&step=4#section-4) · [Datasets §6](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/datasets.html?route=data-and-evaluation&step=4#section-6)<br>[ManiSkill2](PAPERS.md#maniskill2) · [RLBench](PAPERS.md#rlbench) | Read the robot interface, observations, demonstrations, and split before comparing a manipulation score. |
| **5. Test long-horizon household behavior** | [Datasets §4](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/datasets.html?route=data-and-evaluation&step=5#section-4) · [Datasets §6](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/datasets.html?route=data-and-evaluation&step=5#section-6)<br>[RoboCasa365](PAPERS.md#robocasa365) · [BEHAVIOR-1K](PAPERS.md#behavior1k) | Compare compositional kitchen-task generalization with long-horizon activity that changes object state. |
| **6. Separate answering, doing, and asking** | [Datasets §5](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/datasets.html?route=data-and-evaluation&step=6#section-5) · [Datasets §6](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/datasets.html?route=data-and-evaluation&step=6#section-6)<br>[OpenEQA](PAPERS.md#openeqa) · [ALFRED](PAPERS.md#alfred) · [TEACh](PAPERS.md#teach) | Keep question-answering accuracy, household task completion, and dialogue-conditioned interaction as separate evidence. |

**Try it:** Choose one segmentation benchmark and one cabinet-opening benchmark; write down their inputs, success metric, and withheld split.

**Explore more:** [Datasets, simulators, and benchmarks](topics/datasets.md) · [Embodied agents and robotic interaction](topics/robotics.md) · [Back to contents](#contents)

## Research map

The four areas in the teaser are expanded in the [detailed roadmap](assets/survey-roadmap.svg). The collections below group papers by method and task, with official project and code links where available.

| Area | What it covers | Paper collection |
| --- | --- | --- |
| [Scene perception](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/perception.html) | Objects, parts, motion, open-vocabulary representations, scene graphs, and language grounding. | [Papers](topics/perception.md) |
| [Scene reconstruction](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/reconstruction.html) | 3D scenes from images and scans: geometry, appearance, camera motion, SLAM, and dynamic structure. | [Papers](topics/reconstruction.md) |
| [Scene generation](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/generation.html) | Scene layouts, 3D environments, procedural worlds, and interactive assets. | [Papers](topics/generation.md) |
| [Robots & embodied agents](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/robotics.html) | Spatial memory, navigation, embodied reasoning, task planning, policies, and manipulation. | [Papers](topics/robotics.md) |

## Benchmarks

Use the [website benchmark guide](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/benchmarks.html) or the [repository guide](BENCHMARKS.md) to find datasets, simulators, evaluation protocols, and related papers.

Scene data and functional understanding include [ScanNet++](PAPERS.md#scannetpp), [MultiScan](PAPERS.md#multiscan), [SceneFun3D](PAPERS.md#scenefun3d), and [Articulate3D](PAPERS.md#articulate3d). For robot interaction, see [SAPIEN](PAPERS.md#sapien), [ManiSkill2](PAPERS.md#maniskill2), [RLBench](PAPERS.md#rlbench), [RoboCasa365](PAPERS.md#robocasa365), and [BEHAVIOR-1K](PAPERS.md#behavior1k).

[Datasets and evaluation chapter](https://hyokong.github.io/Awesome-3D-Scene-Understanding-and-Interaction/datasets.html) · [Dataset and simulator papers](topics/datasets.md)

## Contributing

Contributions are welcome: suggest papers, add official project or code links, correct entries, or improve the organization. See the [contribution guide](CONTRIBUTING.md).

[Figure and video credits](assets/ATTRIBUTION.md) · [Complete paper index](PAPERS.md)
