# AI Survival Log — Wiki Schema

@AGENTS.md

## Operating Model

- 이 저장소는 `ai-survival-log-site`의 상위 authoring/source-of-truth 저장소다.
- 기본 흐름은 `raw -> wiki -> output/blog -> ai-survival-log-site/content/posts` 이다.
- 발산 lane는 일반 블로그, 책 스터디 시리즈, 인스타그램 캐러셀까지 포함한다.
- 구조 변경, publish 계약 변경, 로컬 agent surface 변경 전에는 짧은 계획을 먼저 작성한다.
- publishable wiki 페이지를 쓰거나 고칠 때는 `docs/content-seo-guide.md`를 따라 제목, 설명, 도입부, 시리즈 구조가 검색 우선순위도 반영하도록 한다.
- 작업 완료 전에는 변경 범위에 맞는 검증을 명시적으로 수행한다.
- ECC와 superpowers는 운영 원칙만 선택적으로 반영하며, 전체 harness surface를 그대로 복제하지 않는다.
- `README.md`, `AGENTS.md`, `.claude/*`, `.codex/*`, publish 관련 문서는 같은 저장소 역할을 설명해야 한다.
- 위키 본체는 human-first, markdown-first, Obsidian-friendly 구조를 유지한다.
- 미래의 RAG/vector DB는 위키를 소비하는 파생 계층으로 다루며, 현재 구조를 선제적으로 RAG 중심으로 바꾸지 않는다.
- 현재 구조 변경 계획은 `wiki/projects/repo-structure-refactor.md`, 미래 RAG 확장은 `wiki/projects/wiki-rag-expansion-roadmap.md`에서 관리한다.

### Local Command Surface

- `/wiki:ingest` — source를 위키에 흡수
- `/wiki:query` — 위키 검색과 인용 답변
- `/wiki:file-answer` — 답변을 위키 페이지로 저장
- `/wiki:lint` — 위키 무결성 검사
- `/wiki:publish` — downstream site용 MDX 출력 준비
- `/content:book-study-blog` — 책 스터디 대화에서 시리즈형 블로그 lane 연결
- `/content:blog-to-instagram` — 블로그 포스트에서 인스타그램 lane 연결

> 이 프로젝트는 Karpathy의 LLM Wiki 패턴을 따르는 개인 지식 위키입니다.
> "Ingest time" 컴파일 방식으로 지식을 축적합니다.

## 프로젝트 개요

- **이름:** AI Survival Log (AI시대 생존일지)
- **언어:** 한국어 (기술 용어는 영문 유지)
- **목적:** 모든 분야의 지식 축적 아카이브 + 블로그 퍼블리싱

## 아키텍처 (4 Layers)

```
Human → 소스 큐레이션, 탐험 방향 설정, 질문
  ↓
LLM Agent → 읽기, 요약, 크로스레퍼런싱, 파일 관리
  ↓
Raw Layer → 불변 원본 (articles, books, journals, videos, podcasts)
  ↓
Wiki Layer → 마크다운 + index + log (persistent, compiled, interlinked)
  ↓
Assets / Output Layer → 채널 자산 원본 + publish artifact
```

### Layer 1: `raw/` — 원본 자료

- 외부 아티클, PDF, 원본 노트, 영상 메모 등
- **불변(immutable):** 한 번 추가하면 수정하지 않음
- 파일명: `YYYY-MM-DD-간단한-설명.{md,pdf,txt}`
- 대표 하위 폴더: `articles/`, `books/`, `journals/`, `videos/`, `podcasts/`
- 이 폴더의 파일은 직접 편집하지 않음

### Layer 2: `wiki/` — 위키 페이지

- Claude가 관리하는 마크다운 지식 베이스
- 모든 페이지는 서로 `[[wikilink]]`로 연결됨
- 하위 폴더: `entities/`, `concepts/`, `sources/`, `topics/`, `projects/`, `syntheses/`

### Layer 3: `assets/` / `output/` — 자산 + 산출물

- `assets/`는 채널별 제작 자산 원본
- `output/blog/`는 재생성 가능한 publish artifact
- 최종 downstream 계약은 `ai-survival-log-site/content/posts/`

### Layer 4: `CLAUDE.md` (이 파일) — 스키마 + 운영 규칙

- 위키 구조, 규칙, 워크플로우 정의
- Claude가 위키를 어떻게 관리해야 하는지 지시

## 페이지 타입

### entities/ — 엔티티

대상: 구체적인 이름이 있는 것 (Claude Code, ECC, Next.js 등)
파일명: `kebab-case-이름.md`

### concepts/ — 개념

대상: 추상적 개념 (AI Transformation, Prompt Engineering, TDD 등)
파일명: `kebab-case-개념명.md`

### sources/ — 소스 요약

대상: `raw/` 폴더의 각 원본 자료에 대한 요약 + 분석
파일명: 원본과 대응되는 이름 `.md`

### topics/ — 토픽

대상: 여러 소스/엔티티/개념을 엮는 종합 페이지
파일명: `kebab-case-주제명.md`

### projects/ — 프로젝트

대상: 진행 중인 프로젝트의 설계 문서와 구현 계획
파일명: `kebab-case-프로젝트명.md`

### syntheses/ — 통합/판단

대상: 비교 분석, 질의 결과, 통합 판단 문서
파일명: `kebab-case-주제명.md`

## Frontmatter 스펙

모든 위키 페이지에 필수:

```yaml
---
title: "페이지 제목"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
type: entity | concept | source | topic | project | synthesis
sources: []
tags: []
status: draft | active | archived
published: false
slug: ""
description: ""
---
```

**규칙:**

- `created`: 최초 생성일, 변경하지 않음
- `updated`: 내용 수정 시 반드시 갱신
- `status`: 신규 → `draft`, 검토 후 → `active`, 더 이상 관리 안 함 → `archived`
- `published`: `true`이면 `/wiki:publish`로 블로그 포스트 변환 대상
- `slug`: `published: true`일 때 필수 — 블로그 URL 경로
- `description`: `published: true`일 때 필수 — 블로그 카드 요약
- `tags`: 소문자, 하이픈 구분 (예: `claude-code`, `ai-transformation`)
- `sources`: 해당 페이지가 참조하는 소스 위키 페이지 `[[wikilink]]` 배열
- 스크린샷/이미지를 포함한 publishable 페이지는 원본 자산을 `assets/blog/`에 보존
- downstream에서 실제 서빙할 자산은 `ai-survival-log-site/public/images/{slug-or-series}/`에 둠
- publishable 페이지 본문에서는 `/images/{slug-or-series}/{file}.png` 형태의 site 경로 사용
- publish-facing 이미지 파일명은 ASCII kebab-case 권장

## 크로스 레퍼런싱 규칙

### Wikilink 형식

Obsidian 호환 `[[wikilink]]` 사용:

```markdown
[[entities/claude-code]]
[[entities/claude-code|Claude Code]]
[[concepts/ax-ai-transformation]]
```

### 링크 관리 원칙

1. 새 페이지 생성 시: 관련 기존 페이지에 역링크(backlink) 추가
2. 본문에서 다른 위키 페이지에 해당하는 용어 → `[[wikilink]]` 처리
3. 각 페이지 하단에 `## 관련 페이지` 섹션 유지
4. 고아 페이지(orphan) 없도록 최소 1개 이상의 링크 확보

### 페이지 하단 구조 (필수)

```markdown
## 관련 페이지

- [[entities/관련-엔티티]]
- [[concepts/관련-개념]]
- [[topics/관련-토픽]]
```

## index.md 규칙

`wiki/index.md`는 위키의 중앙 카탈로그. 벡터 DB 대신 이 파일이 검색 인덱스 역할.

### 형식

```markdown
# Wiki Index

> 마지막 업데이트: YYYY-MM-DD | 총 N개 페이지

## Entities
| 페이지 | 설명 | 태그 | 상태 |
|--------|------|------|------|
| [[entities/claude-code]] | AI 코딩 CLI 도구 | claude, ai-tool | active |

## Concepts
(동일 형식)

## Sources
| 페이지 | 원본 | 태그 | 상태 |
|--------|------|------|------|

## Topics
(동일 형식)

## Projects
(동일 형식)
```

### index.md 업데이트 규칙

- 페이지 생성/삭제/상태 변경 시 반드시 업데이트
- 카테고리별 알파벳순 정렬
- 1줄 설명은 30자 이내

## log.md 규칙

`wiki/log.md`는 모든 위키 조작의 시간순 기록.

### 형식

```markdown
# Wiki Log

## YYYY-MM-DD

### HH:MM — 작업유형: 제목
- **source:** 원본 파일 (있는 경우)
- **created:** 생성된 페이지 목록
- **updated:** 갱신된 페이지 목록
- **summary:** 1-2줄 요약
```

### log.md 규칙

- 최신 항목이 위에 (역순)
- 날짜별 그룹핑 (`## YYYY-MM-DD`)
- 작업 유형: `ingest`, `query`, `file-answer`, `lint`, `publish`, `edit`, `init`

## 커맨드 워크플로우

### /wiki:ingest — 소스 자료 인제스트

1. 소스 자료 읽기 (파일 경로, URL, 또는 텍스트)
2. 외부 소스인 경우 `raw/{type}/`에 원본 보존
3. `wiki/sources/`에 소스 요약 페이지 생성
4. 언급된 엔티티 → `wiki/entities/`에 페이지 생성 또는 갱신
5. 추출된 개념 → `wiki/concepts/`에 페이지 생성 또는 갱신
6. 기존 토픽/프로젝트 페이지와 관련 있으면 갱신
7. 모든 관련 페이지에 크로스 레퍼런스 추가
8. `wiki/index.md` 업데이트
9. `wiki/log.md`에 작업 기록 추가

**규칙:**

- 하나의 소스가 10-15개 페이지에 영향을 줄 수 있음
- 기존 페이지 갱신 시 기존 내용을 보존하고 새 정보를 추가
- 충돌하는 정보가 있으면 출처와 함께 병기

### /wiki:query — 위키 검색 + 인용 답변

1. `wiki/index.md` 읽기
2. 관련 페이지 식별 및 읽기
3. `[[citation]]` 포함하여 답변
4. 답변을 위키 페이지로 저장할지 제안

### /wiki:file-answer — 답변을 위키 페이지로 저장

1. 답변을 적절한 카테고리의 위키 페이지로 변환
2. frontmatter 추가
3. 크로스 레퍼런스 설정
4. `wiki/index.md` 업데이트
5. `wiki/log.md` 기록

### /wiki:lint — 위키 무결성 검사

검사 항목:

1. 깨진 `[[wikilink]]` (대상 페이지 없음)
2. 고아 페이지 (어디서도 링크되지 않음)
3. `index.md`에 누락된 페이지
4. `index.md`에 있지만 실제로 없는 페이지
5. frontmatter 누락 또는 불완전
6. `updated` 날짜가 실제 수정일과 불일치
7. `## 관련 페이지` 섹션 누락
8. `published: true`인데 `slug`/`description` 없는 페이지

### /wiki:publish — 위키 → 블로그 포스트 변환

1. 대상 위키 페이지 읽기 (`published: true` 확인)
2. frontmatter를 블로그 포맷으로 변환
3. `[[wikilink]]`를 블로그 링크 또는 일반 텍스트로 변환
4. `## 관련 페이지` 섹션 제거
5. 인라인 이미지가 있으면 downstream site 경로(`/images/{slug-or-series}/{file}.png`) 호환성 확인
6. `ai-survival-log-site/content/posts/YYYY-MM-DD-{slug}.mdx`로 출력
7. `wiki/log.md`에 publish 기록

**변환 규칙:**

- `[[wikilink]]`에 대응하는 published 페이지가 있으면 → 블로그 내부 링크 (`/posts/slug`)
- 없으면 → 일반 텍스트 (링크 제거)
- Mermaid 코드블록은 보존
- 이미지는 upstream 원본(`assets/blog/`)과 downstream served copy(`ai-survival-log-site/public/images/{slug-or-series}/`)를 함께 유지
- 이미지 링크는 site가 읽는 `/images/{slug-or-series}/...` 경로를 사용

## 블로그 연동

### 위키 → 블로그 파이프라인

```
wiki/topics/ai-era-survival.md (published: true, slug: "ai-era-survival")
    ↓ /wiki:publish
ai-survival-log-site/content/posts/YYYY-MM-DD-ai-era-survival.mdx (블로그 frontmatter)
    ↓ Next.js 빌드 (미래)
/posts/ai-era-survival (웹 페이지)
```

### 규칙

- **위키가 source of truth.** `ai-survival-log-site/content/posts/`는 생성된 출력물
- 위키 갱신 시 `/wiki:publish` 재실행
- `published: true` 페이지는 블로그 독자를 위해 standalone으로 읽힐 수 있어야 함
- 주로 `topics/` 페이지가 블로그 후보 (서사적 흐름이 있는 글)
- 스크린샷/이미지가 있으면 source copy와 site-served copy를 모두 관리

## 컨벤션

### 파일명

- kebab-case (소문자, 하이픈 구분)
- 영문 권장 (한글 가능하나 git/URL 호환성 고려)
- 날짜 prefix 없음 (frontmatter의 `created`로 관리)

### 내용 작성

- 한국어로 작성 (기술 용어는 영문 병기)
- 각 페이지는 `# 제목`으로 시작
- 섹션은 `##`부터 사용
- 코드 블록에 언어 지정 필수

### 스케일 관리

- 목표: 50-200개 페이지
- 200개 초과 시 구조 리뷰 필요 ("false coherence" 위험)
- 현재 페이지 수를 `index.md` 상단에 표시
