---
name: recommend-clipper-template
description: Recommend the right Obsidian Web Clipper template for this repository when the user shares a web URL, page link, or source address and wants to know which clipper template, intake path, and next harness flow to use.
---

# Recommending Clipper Templates

Use this skill when the user shares one or more URLs and wants the best Obsidian Web Clipper template for `ai-survival-log`.

## Workflow

1. Classify the URL from visible cues first.
   - Domain, path, slug, and known platform patterns are usually enough.
   - Do not browse unless the user explicitly asks you to inspect the page contents.
2. Pick one template from `assets/clipper-templates/`.
3. Return the recommendation in a compact format:
   - recommended template
   - why it fits
   - target intake path
   - next harness
   - fallback if classification is weak
4. If the URL is ambiguous, give the best default and one fallback.

## Decision Rules

- Text-heavy article, blog post, essay, documentation page:
  - default: `articles/article-deep-research.json`
  - fallback: `articles/article-quick-capture.json`
- YouTube, Vimeo, lecture replay, interview video:
  - `videos/video-transcript-notes.json`
- Podcast episode pages or audio show notes:
  - `podcasts/podcast-episode-notes.json`
- Book chapter pages, ebook highlights, reading notes:
  - default: `books/book-chapter-notes.json`
  - short excerpt or quote focus: `books/book-quote-capture.json`
- Personal reflection, memo, chat log, transcript backup:
  - default: `journals/journal-insight-capture.json`
  - long conversation or session archive: `journals/conversation-backup.json`
- Image, attachment, gallery, design reference:
  - `other-assets/asset-reference-note.json`
- Unclear:
  - `generic/generic-source-capture.json`

## Output Shape

Use this response shape unless the user asks for something else:

```md
추천 템플릿: `...`
이유: ...
저장 경로: `...`
다음 단계: `...`
보조 선택지: `...`
```

## References

- Read `references/template-map.md` for the current template inventory and URL heuristics.
