---
name: conversation-backup
description: Save the current conversation session as a raw backup file in raw/journals/ for this repository. Use when the user asks to archive or back up the current conversation, especially at the end of a session, so the exchange can later be referenced for blog writing or wiki ingestion.
---

# Conversation Backup

Use this skill when the user wants to archive the current conversation to `raw/journals/`.

## When to Use

- User explicitly asks to "백업해주세요", "대화 저장해주세요", or similar
- At the end of a work session before committing and pushing
- When the user says the conversation will be used as blog source material

## Workflow

### Step 1: Decide metadata

- **Date**: today's date in `YYYY-MM-DD`
- **Topic slug**: derive from the session's main work; convert to `kebab-case`
- **Filename**: `raw/journals/YYYY-MM-DD-{topic-slug}-conversation-backup.md`
  - Example: `2026-04-18-codex-folder-structure-execution-and-publish-conversation-backup.md`
- **Previous related backup**: check `raw/journals/` for a file from the same date or a closely related topic; if found, reference it in `참고:`

### Step 2: Summarize the conversation

Apply these rules:

- **User messages**: quote verbatim in a backtick block
- **Assistant responses**: compress to 1–3 lines of key outcomes; include result summaries if the assistant ran commands or made changes
- **Long lists or code blocks**: reduce to 3–5 bullet highlights
- **Routine acknowledgement turns**: merge into the adjacent meaningful turn

### Step 3: Write the file

Save to `raw/journals/{filename}`. Use exactly this structure:

```markdown
# 대화 백업: {title}

- **날짜:** YYYY-MM-DD
- **성격:** 전체 대화 백업
- **맥락:** {one-line context — what was done and why}
- **용도:** 추후 블로그 글 작성 시 원천 대화 기록으로 재사용
- **참고:** {path to a related prior backup — omit if none}

---

## 대화 원문 백업

### User

`{verbatim user message}`

### Assistant

{response summary or execution result}

(... repeat ...)

---

## 세션 핵심 결정

- {decisions or agreements reached in this session}

## 이번 세션에서 실제 반영된 항목

- {files, code, or docs changed}

## 블로그 글 소재 포인트

- {insights that could become blog content}
```

### Step 4: Report

After saving:

```
저장 완료:
- 파일: raw/journals/{filename}
- 주제: {topic}
- 블로그 소재: {1-2 key insights}
- 다음 단계: wiki-ingest 스킬로 위키 흡수 가능
```

## Rules

- `raw/journals/` is immutable — never edit a saved backup file
- Split into separate files only when the topics are clearly distinct
- For consecutive sessions on the same day, append `-part2`, `-part3` to the filename
- Strip any secrets (API keys, passwords) before saving
- The saved file becomes the source for `wiki-ingest`
