# Quality Gates

## Hard Gates (block publish)

1. Structure baseline
- Exactly one H1.
- H2 count in range `[3, 5]` by default.

2. Placeholder hygiene
- No unresolved placeholders like `TODO`, `TBD`, `{{...}}`, `待补充`.

3. Checker status
- `scripts/check-article.py --strict` must exit with code `0`.

## Warning Gates (human review required)

1. Scan overload
- Any continuous bullet block longer than 5 items.

2. Heading specificity risk
- Generic headings like `问题诊断`, `问题陈述`, `方案设计`, `总结`.

3. Example absence
- No explicit example markers (`例如`, `比如`, `case`, `before`, `after`).

4. AI-tone risk phrases
- Phrases like `打稳`, `抓手`, `返工机器`, `接得住`.

## Release Rule

- Publish only when all hard gates pass.
- Warning gates can pass only with explicit human judgment recorded in `review_report.md`.
