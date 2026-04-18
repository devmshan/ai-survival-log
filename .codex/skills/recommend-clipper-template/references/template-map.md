# Template Map

Current repository template set:

- `assets/clipper-templates/articles/article-deep-research.json`
  - target: `raw/articles`
  - next harness: `/wiki:ingest`
  - use for: long-form technical posts, research posts, essays, explainers, docs pages worth durable ingest
- `assets/clipper-templates/articles/article-quick-capture.json`
  - target: `raw/articles`
  - next harness: `/wiki:ingest`
  - use for: lighter saves, less certain importance, skim-first material
- `assets/clipper-templates/videos/video-transcript-notes.json`
  - target: `raw/videos`
  - next harness: `/wiki:ingest`
  - use for: YouTube, interviews, lectures, demos, recorded talks
- `assets/clipper-templates/podcasts/podcast-episode-notes.json`
  - target: `raw/podcasts`
  - next harness: `/wiki:ingest`
  - use for: podcast episode pages, show notes, audio interviews
- `assets/clipper-templates/books/book-chapter-notes.json`
  - target: `raw/books`
  - next harness: `/wiki:ingest -> /content:book-study-blog`
  - use for: chapter summaries, reading notes, structured study
- `assets/clipper-templates/books/book-quote-capture.json`
  - target: `raw/books`
  - next harness: `/wiki:ingest`
  - use for: short excerpts, quotes, isolated highlights
- `assets/clipper-templates/journals/journal-insight-capture.json`
  - target: `raw/journals`
  - next harness: `/wiki:ingest or /wiki:file-answer`
  - use for: personal insights, reflective notes, short self-authored memos
- `assets/clipper-templates/journals/conversation-backup.json`
  - target: `raw/journals`
  - next harness: `/wiki:ingest or manual backup flow`
  - use for: long chats, session logs, transcript archives
- `assets/clipper-templates/other-assets/asset-reference-note.json`
  - target: `assets/intake/reference-notes`
  - next harness: classify first, then move to a channel asset lane if needed
  - use for: images, attachments, galleries, non-text references, moodboards
- `assets/clipper-templates/generic/generic-source-capture.json`
  - target: `raw/articles`
  - next harness: classify first, then `/wiki:ingest`
  - use for: ambiguous URLs

## URL Heuristics

- Article-like:
  - blog, posts, articles, docs, engineering, Substack, Medium, Velog, Tistory
- Video-like:
  - `youtube.com/watch`, `youtu.be`, Vimeo, `watch`, `video`, `lecture`, `interview`
- Podcast-like:
  - `podcast`, `episode`, `show-notes`, Spotify episode, Apple Podcasts episode
- Book-like:
  - `chapter`, `book`, `highlights`, reading-notes, study-note pages
- Journal or conversation-like:
  - memo, recap, transcript, diary, reflection, chat export
- Asset-note-like:
  - direct image URLs, gallery pages, Figma boards, Pinterest-like collections, attachment downloads

## Ambiguity Defaults

- Article vs book note: prefer article unless the page is clearly chapter-oriented.
- Article vs journal: prefer article for public web pages and journal for self-authored/private note pages.
- Video vs podcast: use the primary medium shown by the URL platform.
- Mostly non-text media: prefer `asset-reference-note.json`.
