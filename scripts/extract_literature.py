#!/usr/bin/env python3
"""
文献 PDF 批量提取脚本
Extract metadata (title, authors, year, abstract) from academic PDF papers.

Usage:
    python extract_literature.py paper.pdf
    python extract_literature.py /path/to/papers/
    python extract_literature.py /path/to/papers/ --output literature_raw.json
"""

import argparse
import json
import os
import sys
import re
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    print("Error: 请先安装 pymupdf")
    print("运行: pip install pymupdf")
    sys.exit(1)


def extract_from_pdf(pdf_path: str) -> dict:
    """从单个 PDF 提取元数据"""
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        return {"error": str(e), "file": pdf_path}

    text = ""
    for page in doc:
        text += page.get_text()

    # 提取标题（通常在第一页顶部）
    title = extract_title(text, doc)

    # 提取作者
    authors = extract_authors(text)

    # 提取年份
    year = extract_year(text)

    # 提取摘要
    abstract = extract_abstract(text)

    doc.close()

    return {
        "file": os.path.basename(pdf_path),
        "title": title,
        "authors": authors,
        "year": year,
        "abstract": abstract,
    }


def extract_title(text: str, doc) -> str:
    """提取论文标题"""
    # 方法1：直接从文档元数据获取
    metadata = doc.metadata
    if metadata.get("title"):
        return metadata["title"].strip()

    # 方法2：取第一行大字体文字
    first_page = doc[0]
    blocks = first_page.get_text("dict")["blocks"]
    for block in blocks:
        if block.get("type") == 0:  # text block
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    font_size = span.get("size", 0)
                    # 标题字体通常较大
                    if font_size > 14:
                        title = span.get("text", "").strip()
                        if len(title) > 10 and len(title) < 200:
                            return title

    # 方法3：取第一行非空文字
    lines = text.strip().split("\n")
    for line in lines[:5]:
        line = line.strip()
        if len(line) > 10 and len(line) < 200:
            return line

    return "未找到标题"


def extract_authors(text: str) -> str:
    """提取作者信息"""
    # 常见作者模式
    patterns = [
        r"(?:作者|Authors?)[:：]?\s*([^\n]{10,100})",
        r"^([A-Z][a-z]+(?:\s*,\s*[A-Z][a-z]+){0,5})",
        r"by\s+([^\n]{10,100})",
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.MULTILINE | re.IGNORECASE)
        if match:
            authors = match.group(1).strip()
            # 清理一些无关字符
            authors = re.sub(r"[\*\[][^\]\*]*[\]\*]", "", authors)
            if len(authors) > 5:
                return authors

    # 取摘要前的常见作者位置
    lines = text.strip().split("\n")
    for i, line in enumerate(lines[:10]):
        if any(keyword in line.lower() for keyword in ["author", "by"]):
            return line.strip()

    return "未找到作者"


def extract_year(text: str) -> int:
    """提取发表年份"""
    # 常见年份模式
    patterns = [
        r"(?:19|20)\d{2}",  # 1900-2099
    ]

    # 优先从文末或参考文献前的位置找
    text_lower = text.lower()

    # 尝试在开头部分找
    first_part = text[:2000]
    for pattern in patterns:
        matches = re.findall(pattern, first_part)
        for match in matches:
            year = int(match)
            if 1970 <= year <= 2030:
                return year

    # 从全文找
    for pattern in patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            year = int(match)
            if 1970 <= year <= 2030:
                return year

    return 2024  # 默认值


def extract_abstract(text: str) -> str:
    """提取摘要"""
    text = text.strip()

    # 常见摘要标记
    abstract_markers = [
        r"摘要[:：]?\s*([^\n]+(?:\n[^\n]+)*)",
        r"Abstract[:：]?\s*([^\n]+(?:\n[^\n]+)*)",
        r"ABSTRACT[:：]?\s*([^\n]+(?:\n[^\n]+)*)",
        r"摘要\s*\n\s*([\s\S]{100,2000}?)(?:关键词|Keywords|1\.|一、)",
        r"Abstract\s*\n\s*([\s\S]{100,2000}?)(?:Keywords|1\.|一、)",
    ]

    for pattern in abstract_markers:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            abstract = match.group(1).strip()
            # 清理
            abstract = re.sub(r"\s+", " ", abstract)
            abstract = re.sub(r"[\n\r]+", " ", abstract)
            if len(abstract) > 50:
                return abstract[:2000]  # 限制长度

    # 如果没找到，返回空
    return "未找到摘要"


def process_path(path: str, output_file: str = None) -> list:
    """处理文件或目录"""
    results = []

    if os.path.isfile(path):
        if path.lower().endswith(".pdf"):
            print(f"处理: {path}")
            results.append(extract_from_pdf(path))
    elif os.path.isdir(path):
        pdf_files = sorted(Path(path).glob("*.pdf"))
        print(f"找到 {len(pdf_files)} 个 PDF 文件")
        for pdf_file in pdf_files:
            print(f"处理: {pdf_file}")
            results.append(extract_from_pdf(str(pdf_file)))

    # 输出
    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"\n结果已保存到: {output_file}")
    else:
        print("\n--- JSON 输出 ---")
        print(json.dumps(results, ensure_ascii=False, indent=2))

    return results


def main():
    parser = argparse.ArgumentParser(
        description="从 PDF 提取文献元数据（标题、作者、年份、摘要）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python extract_literature.py paper.pdf
  python extract_literature.py ./papers/ --output literature.json
  python extract_literature.py /path/to/papers/
        """,
    )
    parser.add_argument("path", help="PDF 文件路径或包含 PDF 的目录")
    parser.add_argument(
        "-o", "--output", help="输出 JSON 文件路径（默认输出到终端）"
    )
    parser.add_argument(
        "--format", choices=["json", "markdown"], default="json", help="输出格式"
    )

    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(f"错误: 路径不存在 - {args.path}")
        sys.exit(1)

    process_path(args.path, args.output)


if __name__ == "__main__":
    main()
