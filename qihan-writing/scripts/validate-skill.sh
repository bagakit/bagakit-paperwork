#!/usr/bin/env bash

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"

required_paths=(
  "SKILL.md"
  "SKILL_PAYLOAD.json"
  "README.md"
  "references"
  "scripts/qihan_write_lint.py"
  "agents/openai.yaml"
)

for rel in "${required_paths[@]}"; do
  if [[ ! -e "$ROOT/$rel" ]]; then
    echo "missing required path: $rel" >&2
    exit 1
  fi
done

python3 -m py_compile "$ROOT/scripts/qihan_write_lint.py"
python3 - "$ROOT/SKILL_PAYLOAD.json" "$ROOT" <<'PY'
import json
import sys
from pathlib import Path

payload_path = Path(sys.argv[1])
root = Path(sys.argv[2])
payload = json.loads(payload_path.read_text(encoding="utf-8"))

if payload.get("version") != 1:
    raise SystemExit("SKILL_PAYLOAD.json version must be 1")

include = payload.get("include")
if not isinstance(include, list) or not include:
    raise SystemExit("SKILL_PAYLOAD.json include must be a non-empty list")

for entry in include:
    if not isinstance(entry, str) or not entry.strip():
        raise SystemExit("SKILL_PAYLOAD.json include entries must be non-empty strings")
    if not (root / entry).exists():
        raise SystemExit(f"payload entry missing: {entry}")
PY

echo "qihan-writing validation passed."
