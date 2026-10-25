'''
1. Introduction（引言）
建议 1～1.5 页，5～6 个自然段。
1. 任务背景：拼图重组的挑战、应用场景、不规则边缘侵蚀带来的困难。
2. 现有方法：传统两两碎片相容性预测，以及 Greedy、LP、GA 等求解方法。
3. 现有局限：依赖局部相容性可能忽略全图视觉上下文，尤其在 GAP 上。
4. 核心方法：介绍 GlobalPuzzle 的三个组件：Global Canvas Evaluation、Position Querying、Genetic Search。
5. 实验概述：主要数据集、指标和核心结果。
6. Contributions：总结 2～3 项主要贡献。
2. Related Work（相关工作）
建议 0.75～1 页。
2.1 Pairwise Compatibility-Based Methods
介绍传统边缘相容性与学习式两两碎片匹配方法，包括 STITCH 等。
2.2 Learning-Based Jigsaw Reassembly
介绍 JigsawGAN、DiffAssemble、JPDVT、FCViT、PuzzleFlow 等方法，重点分析它们如何利用跨碎片信息，与全图画布评价有什么区别。
2.3 Search and Optimization Methods
介绍 Greedy、Linear Programming、Genetic Algorithms 等拼图优化方式，以及不同方法如何构造目标函数。
3. Method（方法）
建议 2～2.5 页，这是你的论文重点。
3.1 Framework Overview
介绍 GlobalPuzzle 整体流程，配一张架构总图。
3.2 Position Query Network
介绍 BC 网络：部分画布编码、碎片编码、Joint Transformer、位置与碎片匹配矩阵。
3.3 Global Canvas Evaluation Network
介绍 A 网络：完整拼图画布输入、整体视觉特征、质量分数，以及监督目标。
3.4 Training Strategy
介绍 BC 的正确前缀全局监督、错误前缀相对监督、空画布采样，以及 A 网络的训练策略。
3.5 Genetic Search
介绍初始化、Stage 0 绝对位置继承、Stage 1 相对块群继承、Stage 2 BC 填充、变异、选择和局部搜索。
4. Experiments（实验）
建议 2～2.5 页。
4.1 Experimental Setup
数据集 GAP-3、GAP-5，评价指标 PA、AA、SRA，训练与搜索配置。
4.2 Comparison with State-of-the-Art
与现有方法对比，用表格展示指标，并给出典型拼图可视化。
4.3 Ablation Studies
分别移除或替换 A、BC、GA，以及比较不同监督策略，验证各模块作用。
4.4 Qualitative Analysis
展示成功与失败案例，分析边缘侵蚀时全图信息的价值及方法局限。
5. Conclusion（结论）
建议 0.2～0.4 页。
'''

