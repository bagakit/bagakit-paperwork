#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path


def split_h2_sections(lines):
    sections = []
    current = {"title": "__lead__", "lines": []}
    for line in lines:
        if line.startswith("## "):
            sections.append(current)
            current = {"title": line[3:].strip(), "lines": []}
        else:
            current["lines"].append(line)
    sections.append(current)
    return [s for s in sections if s["title"] != "__lead__"]


def count_paragraphs(lines):
    count = 0
    in_para = False
    for line in lines:
        t = line.strip()
        if not t:
            if in_para:
                count += 1
                in_para = False
            continue
        if t.startswith("#") or t.startswith("- ") or re.match(r"^\d+\.\s", t) or t.startswith("> "):
            if in_para:
                count += 1
                in_para = False
            continue
        in_para = True
    if in_para:
        count += 1
    return count


def main():
    if len(sys.argv) != 3:
        print("usage: structure_probe.py <input.md> <output.json>")
        sys.exit(1)

    in_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2])

    text = in_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    no_frontmatter = text
    if text.startswith("---\n"):
        parts = text.split("\n---\n", 1)
        if len(parts) == 2:
            no_frontmatter = parts[1]
            lines = no_frontmatter.splitlines()

    h1_count = len(re.findall(r"(?m)^#\s", no_frontmatter))
    h2_count = len(re.findall(r"(?m)^##\s", no_frontmatter))
    h3_count = len(re.findall(r"(?m)^###\s", no_frontmatter))
    bullet_count = len(re.findall(r"(?m)^\-\s", no_frontmatter))
    numbered_count = len(re.findall(r"(?m)^\d+\.\s", no_frontmatter))

    sections = split_h2_sections(lines)
    section_stats = []
    sparse_sections = []
    list_heavy_sections = []
    no_example_sections = []

    for sec in sections:
        sec_text = "\n".join(sec["lines"])
        bullets = len(re.findall(r"(?m)^\-\s", sec_text))
        nums = len(re.findall(r"(?m)^\d+\.\s", sec_text))
        paras = count_paragraphs(sec["lines"])
        h3s = len(re.findall(r"(?m)^###\s", sec_text))
        has_example = any(k in sec_text for k in ("例如", "比如", "Before", "After", "案例"))
        chars = len(sec_text.strip())
        section_stats.append(
            {
                "title": sec["title"],
                "h3_count": h3s,
                "paragraph_count": paras,
                "bullet_count": bullets,
                "numbered_count": nums,
                "char_count": chars,
                "has_example_signal": has_example,
            }
        )
        if paras < 2 and bullets >= 4:
            list_heavy_sections.append(sec["title"])
        if chars < 380:
            sparse_sections.append(sec["title"])
        if not has_example:
            no_example_sections.append(sec["title"])

    generic_tokens = ("问题", "机制", "方案", "优化", "设计", "流程", "诊断", "总结")
    generic_heading_hits = []
    for m in re.finditer(r"(?m)^#{1,3}\s+(.+)$", no_frontmatter):
        heading = m.group(1).strip()
        if any(token == heading or heading.endswith(token) for token in generic_tokens):
            generic_heading_hits.append(heading)

    signal_words = ("验证", "信号", "可追踪", "可复现", "回填", "边界")
    signal_word_hits = sum(no_frontmatter.count(w) for w in signal_words)

    issues = []
    if h2_count < 3 or h2_count > 5:
        issues.append("H2 count is outside 3-5 range.")
    if list_heavy_sections:
        issues.append("Some sections rely heavily on lists with few explanatory paragraphs.")
    if no_example_sections:
        issues.append("Some sections have no explicit example markers.")
    if signal_word_hits < 10:
        issues.append("Signal-related language density is low.")

    result = {
        "input_file": str(in_path),
        "h1_count": h1_count,
        "h2_count": h2_count,
        "h3_count": h3_count,
        "bullet_count": bullet_count,
        "numbered_count": numbered_count,
        "signal_word_hits": signal_word_hits,
        "generic_heading_hits": generic_heading_hits,
        "section_stats": section_stats,
        "diagnostic_flags": {
            "list_heavy_sections": list_heavy_sections,
            "sparse_sections": sparse_sections,
            "no_example_sections": no_example_sections,
        },
        "issues": issues,
    }

    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
