#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

if len(sys.argv) != 4:
    raise SystemExit("usage: check_experiment.py <source-path> <copy-path> <candidate-path>")

source = Path(sys.argv[1])
copy = Path(sys.argv[2])
candidate = Path(sys.argv[3])

s_text = source.read_text(encoding="utf-8")
c_text = copy.read_text(encoding="utf-8")
n_text = candidate.read_text(encoding="utf-8")


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def list_block_over5(text: str) -> int:
    runs = []
    run = 0
    for line in text.splitlines():
        if re.match(r"^\s*[-*]\s+", line) or re.match(r"^\s*\d+\.\s+", line):
            run += 1
        else:
            if run:
                runs.append(run)
            run = 0
    if run:
        runs.append(run)
    return sum(1 for x in runs if x > 5)

metrics = {
    "source_and_copy_identical": s_text == c_text,
    "source_hash": sha256(s_text),
    "copy_hash": sha256(c_text),
    "candidate_hash": sha256(n_text),
    "source_char_count": len(s_text),
    "candidate_char_count": len(n_text),
    "source_heading_count": sum(1 for ln in s_text.splitlines() if ln.startswith("#")),
    "candidate_heading_count": sum(1 for ln in n_text.splitlines() if ln.startswith("#")),
    "source_list_blocks_over_5": list_block_over5(s_text),
    "candidate_list_blocks_over_5": list_block_over5(n_text),
    "candidate_has_claim_phrase": ("观点是否成立" in n_text),
    "candidate_has_tool_phrase": ("工具是否可用" in n_text),
}

print(json.dumps(metrics, ensure_ascii=False, indent=2))
