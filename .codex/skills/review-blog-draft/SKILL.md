---
name: review-blog-draft
description: Use when a blog draft is ready for quality review before wiki:publish. Checks narrative quality issues that structural lint cannot catch.
---

# Review Blog Draft

Use this skill before publishing a wiki topic page as a blog post.

## Checklist

Run these 7 checks in order:

| # | Check | Question |
|---|-------|----------|
| 1 | Header quality | Does each `##` header contain an insight, discovery, or pivot — not just a descriptive label? |
| 2 | Opening context | Do the first 2-3 paragraphs explain WHY this topic matters now? |
| 3 | Section motivation | Does each section show WHY the action or discovery happened (cause, not just event)? |
| 4 | Technical depth | For tool/tech evaluations, does the draft explain WHY not just WHAT? |
| 5 | Noise filter | Are there implementation details irrelevant to the reader (sandbox constraints, agent internals, workarounds)? |
| 6 | Narrative completeness | Is the full story arc present? No orphaned context? |
| 7 | Post scope | Does this read as one coherent post for the reader, not forced to split or merge? |

## Output Format

For each item:

```
[#] [Check name]: PASS / WARN / FAIL
→ Reason: (specific)
→ Suggestion: (WARN/FAIL only)
```

Final verdict:
- All PASS → proceed with wiki:publish
- WARN only → fix recommended, may proceed
- Any FAIL → fix and re-review

## Header Quality Guide

Bad (label): "설치하고 돌려봤다", "부수 효과들", "시작은 Web Clipper였다"

Good (insight): "`pip install` 한 줄, 그리고 바로 막혔다", "마크다운이 이미 그 문제를 풀고 있었다"

Rule: Reading the header alone should tell the reader what they gain from the section.

## Noise Filter Guide

Remove: agent sandbox details, one-off workarounds, env details the reader cannot reproduce
Keep: CLI commands the reader can run, discoveries that directly support the conclusion, technical reasons for the WHY
