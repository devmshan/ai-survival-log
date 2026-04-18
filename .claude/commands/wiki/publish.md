---
description: "위키 페이지를 블로그 포스트(MDX)로 변환합니다"
---

# /wiki:publish — 위키 → 블로그 포스트 변환

위키 페이지를 `ai-survival-log-site`에서 소비할 수 있는 MDX 파일로 변환합니다.

## 입력

위키 페이지 경로 (예: `wiki/topics/ai-era-survival.md`).
인자가 없으면 `published: true`인 모든 페이지를 목록으로 보여줍니다.

## 사전 조건 확인

대상 페이지의 frontmatter를 검증합니다:

- `published: true` 확인
- `slug` 존재 확인 (없으면 요청)
- `description` 존재 확인 (없으면 요청)
- `status: active` 확인 (draft이면 경고)

대상 페이지가 스크린샷/이미지를 포함하면 추가로 확인합니다:

- upstream source copy가 `assets/blog/`에 있는지
- downstream served copy가 `ai-survival-log-site/public/images/{slug-or-series}/`에 있는지
- 본문 이미지 경로가 `/images/{slug-or-series}/{file}.png` 형태인지
- publish-facing 파일명이 ASCII kebab-case인지

## 워크플로우

### 1단계: 위키 페이지 읽기

대상 위키 페이지의 전체 내용을 읽습니다.

### 2단계: Frontmatter 변환

위키 frontmatter를 블로그 frontmatter로 변환합니다:

```yaml
# 위키 원본
---
title: "AI 시대 생존 전략"
created: "2026-04-10"
updated: "2026-04-12"
type: topic
tags: [ai, survival]
status: active
published: true
slug: "ai-era-survival"
description: "AI 시대를 살아남기 위한 개발자의 전략"
---

# 변환 결과 (MDX)
---
title: "AI 시대 생존 전략"
date: "2026-04-12"
tags: ["ai", "survival"]
description: "AI 시대를 살아남기 위한 개발자의 전략"
draft: false
---
```

### 3단계: 본문 변환

- `[[entities/claude-code|Claude Code]]` → published 페이지면 `[Claude Code](/posts/slug)`, 아니면 **Claude Code**
- `[[concepts/some-concept]]` → published 페이지면 내부 링크, 아니면 일반 텍스트
- `## 관련 페이지` 섹션 전체 제거
- Mermaid 코드블록 보존
- 이미지 경로는 downstream site 기준 `/images/{slug-or-series}/{file}.png` 형태 유지
- 스크린샷 원본은 `assets/blog/`에 남기고, site가 읽는 복사본은 `ai-survival-log-site/public/images/{slug-or-series}/`에 둠

### 4단계: 파일 출력

- `output/blog/YYYY-MM-DD-{slug}.mdx`로 저장
- 필요 시 downstream `ai-survival-log-site/content/posts/YYYY-MM-DD-{slug}.mdx`로 동기화
- 기존 파일이 있으면 덮어쓰기 (위키가 source of truth)

최종 downstream 계약은 계속 `ai-survival-log-site/content/posts/YYYY-MM-DD-{slug}.mdx`다.

### 5단계: 로그 기록

- `wiki/log.md`에 publish 작업 기록

## 완료 보고

```
퍼블리시 완료:
- 원본: wiki/topics/ai-era-survival.md
- 산출물: output/blog/YYYY-MM-DD-ai-era-survival.mdx
- 변환된 링크: N개
```

## 일괄 퍼블리시

인자 없이 실행하면:

1. `published: true`인 모든 페이지 목록 표시
2. 전체 퍼블리시 또는 개별 선택 가능
3. 각 페이지에 대해 위 워크플로우 실행
