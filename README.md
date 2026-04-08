# SCI_introduction

> 一个用于写顶刊级"国内外研究现状"的 Claude Skill——消灭报菜名写法、结构化缺口逻辑、批判认识论深度。

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE.txt)
![Skill Version](https://img.shields.io/badge/version-2.0-green.svg)
[![GitHub Repo](https://img.shields.io/badge/GitHub-sci--introduction-blue?logo=github)](https://github.com/stephenlzc/sci-introduction)

---

## 核心功能亮点

### 五步写作流水线
从文献笔记到期刊级初稿，全自动执行：
```
① 话语体系分类 → ② 主题聚类整合 → ③ 核心分歧诊断 → ④ 双重视角缺口探测 → ⑤ 学术语态缝合
```

### 批判性认识论深度
不仅罗列文献，**更揭示国内外研究在认识论层面的根本分歧**——为什么同样的概念在国际和国内语境下会被不同地理论化和经验化。

### 研究缺口逻辑链
严格遵循 **"国际研究缺乏 X → 国内研究缺乏 Y → 本文填补 Z"** 的完整链条，每一处研究缺口都有逻辑支撑。

### 双重引用格式
`(作者, 年份)^{[1]}` 双重格式，参考文献合并为单一顺序列表，符合 GB/T 7714-2015 国家标准。

### 实战验证
已成功处理 **24篇文献（8篇国际 + 16篇国内）**，输出约2,200字研究现状。

---

## 问题

写"国内外研究现状"（文献综述）是中文学术论文中最常见、也最常写砸的部分。绝大多数最终写成了一笔按时间排序的流水账：

> "国外学者A提到了什么，国内学者B又附和了什么，国外学者C也发现了什么…"

这种写法**毫无分析深度**——根本没有点透国内外学术界到底在"吵"什么。特别是在高度依赖社会语境的社科类或质性研究中，我们绝对不能简单地把西方的理论框架生搬硬套到本土的经验现实上。一篇顶刊级别的研究现状，必须在结构上精准对比国内外研究在认识论和经验关注点上的根本差异。

---

## 解决方案

`SCI_introduction` 是一个**五步写作流水线**，将杂乱的文献笔记转化为结构清晰、分析深入的文献综述：

```
① 话语体系分类     → 对比矩阵（国际 vs 国内）
② 主题聚类整合     → 3–4 个跨越国界的核心主题
③ 核心分歧诊断     → ~200字批判性分析段落
④ 双重视角缺口探测 → Gap 1 + Gap 2 + 优先切入点
⑤ 学术语态缝合     → 期刊级正文初稿（800–1200字）
```

每一步的输出是下一步的输入。最终散文遵循严格的**主题概述 → 对比摩擦 → 锁定双重缺口 → 本文切入点**叙事结构。

---

## 五步流水线详解

### 第一步 — 话语体系分类

**角色**：敏锐的学术档案管理员

在动笔之前，先将国内外文献按"话语阵营"分开，防止不同语境的文献被搅和在一起。

**输出**：对比矩阵

| 核心概念 | 国际话语包装 / 主导理论 | 国内话语包装 / 本土现实 |
|---|---|---|
| [概念X] | [国际学者的理论化路径] | [国内学者的经验关切] |

---

### 第二步 — 主题聚类整合

**角色**：精通扎根理论和主题聚类的资深质性研究员

将第一步的分类打乱，按**主题**而不是**作者**来归纳文献，提炼背后的机制或质性体验——彻底消灭报菜名写法。

**输出**：3–4 个核心主题聚类，每个包含：
- 国际立场（不点名具体作者）
- 国内立场
- 张力点

---

### 第三步 — 核心分歧诊断

**角色**：冷酷的批判理论家

**这是整篇综述的灵魂。** 揭露"舶来理论"与"本土语境"之间的摩擦力与张力。必须使用对比性转折句式：

> "尽管国际研究热衷于将 X 概念化为……，但国内研究则被牢牢锁定在 Y 的本土经验现实中……"

**输出**：~200字批判性分析段落 + 张力根源分析

---

### 第四步 — 双重视角缺口探测

**角色**：顶尖的国社科/自科基金撰写专家

同时扫描国内外两个领域的盲区，严格遵循此逻辑链：

> **"国际研究缺乏 X，而国内研究缺乏 Y，因此，本研究填补了 Z。"**

**输出**：
- Gap 1（国际前沿的盲区）
- Gap 2（国内经验的短板）
- **Prioritized Opportunity**（整合 X + Y，明确本文的优先切入点）

---

### 第五步 — 学术语态缝合

**角色**：社会科学顶刊的责任编辑

将前四步的所有分析模块，缝合成逻辑严密、行文丝滑的学术散文：

- **主题概述**（每个核心主题的核心争论是什么）
- **对比摩擦**（国际与本土之间的张力根源）
- **锁定双重缺口**（国际缺什么、国内缺什么、本文填补什么）

彻底剔除废话套话（"值得注意的是"、"多姿多彩的画卷"），保持极其客观、冷峻、严谨的学术声口。

**输出**：完整正文初稿 + 写作检查清单

---

## 快速开始

### 安装

**方式一：从 GitHub 安装**

```bash
git clone https://github.com/stephenlzc/sci-introduction.git ~/.claude/skills/SCI_introduction
```

**方式二：手动复制**

将本仓库复制到 Claude Code 的 skills 文件夹：

```bash
cp -r /path/to/SCI_introduction ~/.claude/skills/
```

> 仓库地址：`https://github.com/stephenlzc/sci-introduction`

### 使用

**第一步：准备文献笔记**

1. 下载与你研究主题相关的 PDF 文献（建议 10-24 篇）
2. 使用 `scripts/extract_literature.py` 批量提取 PDF 元数据：
   ```bash
   pip install pymupdf
   python scripts/extract_literature.py /path/to/papers/ --output literature.json
   ```
3. 参考 `references/literature-extraction-guide.md` 补充理论视角和核心发现
4. 将整理好的文献填入 `SAMPLE INPUT.md` 表格

**第二步：启动流水线**

调用本 Skill，然后提供：
1. **你的研究主题**（例如："基层治理中的形式主义现象"）
2. **文献笔记**（`SAMPLE INPUT.md` 中的表格——国内外分开）

Skill 将执行完整五步流水线并输出最终初稿。

---

## 输出示例

详见 `examples/formalism-output.md`，展示第五步"学术语态缝合"的最终输出格式。

各步骤的 Prompt 模板位于 `references/prompts/` 目录，详见下方文件结构。

---

## 写作原则（铁律）

| 原则 | 说明 |
|---|---|
| **禁止报菜名** | 永远不要"作者A发现了X，作者B发现了Y" |
| **禁止理论霸权** | 不将西方理论视为普适真理，始终警惕本土适用性 |
| **禁止废话套话** | 不出现"值得注意的是"、"多姿多彩的画卷"等 |
| **必须按主题聚类** | 以概念维度组织，而非以作者组织 |
| **逻辑链必须完整** | 每个缺口都要遵循"国际缺X → 国内缺Y → 本文填补Z" |
| **Evidence-bounding** | 每个事实声明必须有文献/证据支撑，禁止过度推断 |
| **引用格式** | （作者, 年份）^{[1]} 双重格式；参考文献合并为单一顺序列表；符合 GB/T 7714-2015 |

---

## 技能质量

基于 3 个盲测用例评估（形式主义 / 数字社区参与 / 社会企业困境）：

| 指标 | With-Skill | 无 Skill（Baseline） |
|---|---|
| 质量得分 | **30/30** | 17.3/30 |
| 报菜名写法 | **0次** | 3个用例全出现 |
| 完整缺口逻辑链 | **3/3** | 0/3 |
| 对比转折句≥2处 | **3/3** | 0/3 |

完整评测数据：[EVALUATION_REPORT.md](./EVALUATION_REPORT.md)

---

## 文件结构

```
SCI_introduction/
├── SKILL.md                      ← 核心技能（五步流水线）
├── README.md                     ← 本文件（GitHub 仓库首页）
├── EVALUATION_REPORT.md          ← 完整评测报告
├── SAMPLE INPUT.md               ← 文献笔记填写模板（用户用这个）
├── .gitignore                    ← 忽略评测产物和临时文件
├── scripts/
│   └── extract_literature.py     ← PDF 文献元数据批量提取脚本
├── references/
│   ├── literature-extraction-guide.md  ← 文献准备详细指南
│   └── prompts/                  ← 各步骤 Prompt 模板
│       ├── step1-discourse-classification.md
│       ├── step2-theme-clustering.md
│       ├── step3-gap-diagnosis.md
│       ├── step4-gap-probing.md
│       ├── step5a-writing.md
│       ├── step5b-review.md
│       └── step5c-finalize.md
└── examples/
    └── formalism-output.md       ← 最终输出示例（研究现状正文格式）
```

---

## 参考资源

- **AutoResearchClaw** (Liu et al., 2026) — Gap驱动的 Related Work 结构与字数标准（600–800词）
- **Scientific Writing Skill** — IMRAD 结构与引用规范
- **PRISMA 方法论** — 系统性文献综述框架

---

## License

MIT — 详见 [LICENSE.txt](LICENSE.txt)
