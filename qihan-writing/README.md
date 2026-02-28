# qihan-writing

Writing and rewrite skill for producing technical, research, and execution-facing
documents in a sharp, evidence-first style with low AI-smell.

## What problem this skill solves

Many drafts are structurally correct but still weak in three places:

- conclusions arrive too late
- claims are hard to verify
- the prose keeps project-specific jargon, filler, or AI-ish scaffolding

`qihan-writing` turns those problems into an explicit workflow:

- identify the writing scenario first
- force evidence and mechanism ahead of vague praise
- absorb user rewrites as reusable rules
- run a lightweight lint pass before publishing or long-term storage

## What ships in this package

- `SKILL.md`
  runtime workflow and hard style constraints
- `references/*`
  scenario router, voice rules, structure rules, rewrite loop, and casebook
- `scripts/qihan_write_lint.py`
  objective markdown checks for structure, list ratio, AI-ish wording, and local-path leakage
- `agents/openai.yaml`
  runtime metadata for agent surfaces that read agent descriptors

## Notes on examples

The rewrite examples are preserved because the sentence-level differences are the
useful part of the skill. Names and identifiable internal mechanism labels have
been de-identified so the package can be shared without carrying project-specific
identifiers into the runtime payload.

## Quick start

```bash
cd qihan-writing
bash scripts/validate-skill.sh
python3 scripts/qihan_write_lint.py SKILL.md
```

## Common usage

```bash
python3 scripts/qihan_write_lint.py article.md
```

Exit code semantics:

- `0`: no findings
- `2`: warnings or failures found

## Packaging

```bash
cd qihan-writing
make package-skill
```

Output artifact:

- `dist/qihan-writing.skill`

## Install into local runtime skills

For Bagakit-style copy install:

```bash
cd qihan-writing
make install-skill
```

For SSOT-style local runtime usage, prefer symlinking the expanded `dist_local/qihan-writing`
directory into the agent skill home instead of copying this source tree.
