# 文献笔记整理指南

> 在使用 `SCI_introduction` Skill 写研究现状之前，请先按以下步骤整理文献。本指南帮助你高效完成文献准备工作。

---

## 准备工作流程

```
第0步：下载文献 PDF
    ↓
第1步：使用提取脚本批量处理 PDF
    ↓
第2步：人工复核并补充理论视角字段
    ↓
第3步：填入 SAMPLE INPUT.md 表格
    ↓
开始五步流水线
```

---

## 第0步：下载文献

### 建议文献数量

| 场景 | 国际文献 | 国内文献 | 合计 |
|------|---------|---------|------|
| 硕士论文 | 5-8 篇 | 5-8 篇 | 10-16 篇 |
| 顶刊发表 | 8-12 篇 | 8-12 篇 | 16-24 篇 |

### 下载渠道

**国际文献**
- Google Scholar: https://scholar.google.com
- Web of Science: https://www.webofscience.com
- Scopus: https://www.scopus.com
- 订阅数据库：JSTOR、ScienceDirect、Springer、 Wiley

**国内文献**
- CNKI（中国知网）: https://cnki.net
- 万方数据: https://wanfangdata.com.cn
- 维普: https://cqvip.com

### 文献选择标准

1. **核心概念相关**：与你的研究主题直接相关的理论/实证论文
2. **高被引/新发表**：经典文献或近3年重要期刊论文
3. **方法论代表性**：涵盖该领域主要理论视角
4. **避免堆砌**：不是越多越好，15-25篇核心文献足够

---

## 第1步：批量提取 PDF 信息

### 使用提取脚本

项目已内置 `scripts/extract_literature.py` 脚本，可以从 PDF 中自动提取：

- 标题（Title）
- 作者（Authors）
- 年份（Year）
- 摘要（Abstract）

### 安装依赖

```bash
pip install pymupdf
```

### 运行提取

```bash
# 处理单个 PDF
python scripts/extract_literature.py paper.pdf

# 批量处理目录
python scripts/extract_literature.py /path/to/papers/

# 指定输出文件
python scripts/extract_literature.py /path/to/papers/ --output literature_raw.json
```

### 输出格式

脚本输出 JSON 格式：

```json
[
  {
    "title": "Street-Level Bureaucracy: Dilemmas of the Individual in Public Services",
    "authors": "Michael Lipsky",
    "year": 1980,
    "abstract": "This book examines how public service workers..."
  },
  {
    "title": "Policy Implementation as Bureaucratic Politics",
    "authors": "Frank J. Brewer",
    "year": 1994,
    "abstract": "The article explores..."
  }
]
```

---

## 第2步：人工复核并补充

脚本提取的信息是**原材料**，你需要补充：

### 必须填写的字段

| 字段 | 说明 | 示例 |
|------|------|------|
| **核心发现** | 一句话概括这篇文献的核心论点 | "形式主义是基层工作人员在资源约束下的策略性适应行为" |
| **理论视角** | 文献使用的理论框架 | "街头官僚理论 / 一线裁量权" |
| **经验焦点** | 文献关注的问题层面 | "政策执行 / 目标-能力落差" |

### 理论视角参考词表

| 类别 | 常见理论视角 |
|------|------------|
| 制度分析 | 制度主义、新制度主义、压力型体制 |
| 行为逻辑 | 理性选择、街头官僚理论、行为公共管理 |
| 批判理论 | 公共行政批判、后结构主义 |
| 治理研究 | 治理现代化、数字治理、网络化治理 |
| 社会学 | 社会资本、结构功能主义 |
| 经济管理 | 交易成本、委托代理、资源依赖 |

---

## 第3步：填入模板

将整理好的文献填入 `SAMPLE INPUT.md` 的表格：

```markdown
### 【国际文献】

| # | 作者 | 年份 | 标题/核心发现 | 理论视角 / 经验焦点 |
|---|------|------|----------------|-------------------|
| 1 | Lipsky | 1980 | 形式主义是基层工作人员在资源约束下的策略性适应行为 | 街头官僚理论 / 一线裁量权 |
| 2 | Brewer | 1994 | 形式主义是政策目标与执行能力之间结构性落差的产物 | 政策执行视角 / 目标-能力落差 |

### 【国内文献】

| # | 作者 | 年份 | 标题/核心发现 | 理论视角 / 经验焦点 |
|---|------|------|----------------|-------------------|
| 1 | 李强 | 2015 | 形式主义源于压力型体制下的层层加码机制 | 制度分析 / 压力型体制 |
```

---

## 常见问题

### Q: 脚本提取失败怎么办？

A: 手动复制 PDF 摘要到网站 https://ar5iv.org 或 https://reader.abstracts.com

### Q: 文献太多，手动整理太慢？

A: 聚焦核心文献 15-25 篇，贪多嚼不烂。质量比数量重要。

### Q: 如何判断文献的理论视角？

A: 看文献的 Introduction 或 Theory 部分，通常作者会明确说明使用了什么理论框架。

### Q: 国内文献没有英文摘要？

A: 在 CNKI 页面找到"摘要"字段复制即可；或使用脚本处理中文 PDF。

---

## 下一步

文献整理完毕后，直接将 `SAMPLE INPUT.md` 的内容发给 Claude，Claude 会自动执行五步流水线。
