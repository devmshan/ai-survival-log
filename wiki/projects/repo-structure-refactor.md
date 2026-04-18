---
title: "레포 폴더 구조 리팩토링"
created: "2026-04-18"
updated: "2026-04-18"
type: project
sources: []
tags: [project, repository, structure, refactor, wiki, raw, output]
status: active
published: false
slug: ""
description: ""
---

# 레포 폴더 구조 리팩토링

## 배경

현재 저장소는 원본 소스, 제작 자산, 채널별 결과물이 서로 다른 계층으로 충분히 분리되어 있지 않다. `sources/`는 flat 구조라 인제스트 시 컨텍스트가 약하고, `book/`, `docs/images/`, `docs/webtoon/`는 각기 다른 목적의 파일을 흩어 보관하고 있다.

앞으로 블로그, 유튜브, 인스타그램, 웹툰까지 멀티채널 제작을 지속할 계획이므로 폴더 구조는 다음 네 가지 역할을 명확히 나눠야 한다.

- `raw/` — 불변 원본 소스
- `wiki/` — source-of-truth 문서와 지식 그래프
- `assets/` — 채널별 제작 자산 원본
- `output/` — 채널별 결과물 및 publish artifact

동시에 이 위키는 Obsidian에서 사람이 읽고 관리하기 쉬워야 하며, 미래의 RAG/vector DB 확장은 이 구조를 소비하는 파생 계층이어야 한다. 현재 구조 변경의 목적은 RAG 최적화가 아니라 human-first wiki를 더 명확하게 만드는 것이다.

## 목표 구조

```
raw/                          ← 불변 원본 소스
├── CLAUDE.md
├── articles/                 ← 웹 클리핑, 아티클
├── videos/                   ← 영상 스크립트, 트랜스크립트
├── podcasts/                 ← 팟캐스트 노트
├── books/                    ← 책 스터디 원본 메모, 챕터 정리
└── journals/                 ← 일기, 생각 메모, 인사이트

wiki/
├── entities/
├── concepts/
├── sources/
├── topics/
└── projects/

assets/                       ← 채널별 제작 자산 원본
├── CLAUDE.md
├── shared/                   ← 채널 공용 자산
├── blog/                     ← 블로그용 이미지, 다이어그램 원본
├── youtube/                  ← 썸네일, 스토리보드, 참조 이미지
├── instagram/                ← 캐러셀 원본 자산
└── webtoon/                  ← 캐릭터시트, 패널 소스, 참조 이미지

output/                       ← 채널별 결과물 / publish artifact
├── CLAUDE.md
├── blog/                     ← wiki publish 결과 MDX artifact
├── youtube/
├── instagram/
├── threads/
└── webtoon/
```

## 목표 Wiki 구조

```
wiki/
├── entities/                 ← 사람, 회사, 도구, 제품
├── concepts/                 ← 추상 개념, 패턴, 정의
├── topics/                   ← 설명/허브/클러스터 페이지
├── sources/                  ← 원본 자료 요약과 분석
├── projects/                 ← 설계 문서와 실행 계획
└── tags/                     ← 현재 자동 생성 뷰
```

## Wiki 설계 원칙

- 위키는 계속 사람이 직접 읽고 고칠 수 있는 markdown 집합으로 유지한다.
- Obsidian 친화성을 우선하며, 폴더 수는 제한하고 타입 의미는 명확하게 유지한다.
- Graphify는 이 구조를 시각화하는 소비 도구이며 구조를 지배하지 않는다.
- 미래의 RAG/vector DB는 위키 파일을 인덱싱하는 파생 계층으로 두고, 현재 구조 변경에서 선반영하지 않는다.
- `tags/`는 현재 생성 뷰로 유지하되, 장기적으로 `_generated/` 분리 여부는 RAG 확장 프로젝트에서 재검토한다.
- 비교/판단 성격의 지식은 관련 `topics/` 페이지에 통합한다.

## 변경 결정 요약

| 항목 | 변경 전 | 변경 후 |
|------|---------|---------|
| 원본 소스 | `sources/` (flat) | `raw/{type}/` (타입별 분류) |
| 책 스터디 원본 | `book/` | `raw/books/` |
| 블로그 업스트림 이미지 | `docs/images/` | `assets/blog/` |
| 웹툰 제작 자산 | `docs/webtoon/` | `assets/webtoon/` |
| wiki 카테고리 | entities/concepts/sources/topics/projects | 동일 (syntheses 미도입) |
| 블로그 publish artifact | 직접 downstream 출력 중심 | `output/blog/` 추가 |
| 콘텐츠 결과물 | 미구조화 | `output/{channel}/` |
| vestigial 폴더 | `content/posts/` | 제거 대상 검토 |

## 경계 원칙

- `wiki/`가 계속 source of truth다.
- `output/blog/`는 편집 대상이 아니라 publish artifact다.
- 최종 downstream 호환 경로는 계속 `ai-survival-log-site/content/posts/YYYY-MM-DD-{slug}.mdx`다.
- `assets/blog/`는 publishable 페이지에 쓰이는 업스트림 이미지 원본이다.
- `assets/`는 문서 디렉토리인 `docs/`와 분리된 자산 계층이다.
- `wiki/` 구조는 human-first, Obsidian-first 원칙을 유지하며 RAG 구조로 선제 재편하지 않는다.

## 현재 범위와 제외 범위

이번 구조 변경에 포함:

- `sources/`, `book/`, `docs/images/`, `docs/webtoon/`를 새 상위 계층으로 재배치
- `output/blog/`를 포함한 채널별 산출물 계층 정의
- Claude/Codex/문서 계약 정합성 갱신
- `ai-survival-log-site`와의 publish 계약을 새 구조에 맞게 정리

이번 구조 변경에서 제외:

- RAG/vector DB 도입
- chunking 정책, embedding 정책, retrieval ranking
- `wiki/tags/`의 `_generated/` 분리
- Graphify 전용 구조 최적화
- downstream site 런타임 로직 변경

## 구현 범위

### Phase 1: 디렉토리 생성 + 파일 이동
- `raw/articles/` — 기존 `sources/` 11개 파일 이동
- `raw/books/` — `book/`의 책 스터디 자료 이동
- `assets/blog/` — `docs/images/` PNG 2개 이동
- `assets/webtoon/` — `docs/webtoon/` PNG 2개 이동
- `assets/shared/` — 공용 자산용 빈 디렉토리 생성
- `output/blog/` — 블로그 publish artifact 디렉토리 생성
- `wiki/syntheses/` — 신규 카테고리 생성
- `content/posts/` — 실제 사용 여부 재확인 후 제거

### Phase 2: publish 경로 재정의
- `/wiki:publish` 책임을 `wiki -> output/blog -> ai-survival-log-site/content/posts`로 명시
- `output/blog/` 산출물은 재생성 가능 artifact로 취급
- downstream 전달 시점과 파일명 규칙은 기존 계약 유지
- upstream 이미지 원본 경로는 `assets/blog/`, downstream served 경로는 `ai-survival-log-site/public/images/{slug-or-series}/`로 정의

### Phase 3: 런타임 스크립트 수정
- `scripts/wiki_lib.py` — image upstream 검사 경로를 `assets/blog/` 기준으로 갱신
- publish artifact 출력 경로를 `output/blog/`로 반영
- `scripts/pr-summary.mjs` — `sources/` → `raw/`, `assets/`, `output/` 카테고리 반영
- 관련 테스트를 새 경계 기준으로 보강

### Phase 4: 슬래시 커맨드 수정
- `/wiki:ingest` — `raw/{type}/` 경로 안내
- `/wiki:publish` — `assets/blog/`와 `output/blog/` 기준으로 갱신
- `/wiki:lint` — 5개 타입 기준
- `/content:book-study-blog` — `raw/books/` 경로
- `/content:blog-to-instagram` — `output/instagram/` 경로
- 채널 자산 참조 문구를 `assets/{channel}/` 기준으로 통일

### Phase 5: 문서 수정
- `CLAUDE.md` — 4계층 경계(`raw/wiki/assets/output`)와 publish artifact flow 반영
- `AGENTS.md`, `README.md`, `.codex/AGENTS.md`
- `docs/publishing-contract.md`, `docs/operating-playbook.md`, `docs/content-seo-guide.md`
- `raw/CLAUDE.md`, `assets/CLAUDE.md`, `output/CLAUDE.md` 신규 생성
- image 규칙 문구를 `docs/images/`에서 `assets/blog/`로 일괄 전환
- 위키 구조 원칙에 human-first, Obsidian, future-RAG-separate-project 원칙 반영

### Phase 6: Wiki 콘텐츠 경로 갱신
- `wiki/sources/` 페이지 본문의 backtick 경로 참조 수정
- 기존 문서의 `sources/`, `book/`, `docs/images/`, `docs/webtoon/` 경로 표기를 새 구조로 갱신
- `wiki/log.md`는 역사적 기록 보존 원칙에 따라 기존 서술 유지
- 예시 표기에서 lint를 깨는 wikilink 패턴은 사용하지 않음

### Phase 7: 정리
- `.claude/worktrees/objective-germain/` 제거
- 제거 대상 확인 후 정리: `sources/`, `book/`, `docs/images/`, `docs/webtoon/`, `content/posts/`

## ai-survival-log-site 고려사항

- downstream site의 최종 콘텐츠 로딩 경로는 계속 `content/posts/`다.
- upstream의 `output/blog/` 도입은 site repo의 소비 계약을 대체하지 않는다.
- 이미지 이관 시 site repo의 `public/images/{slug-or-series}/` 경로와 1:1 대응을 유지해야 한다.
- publish artifact를 중간 계층으로 두더라도 frontmatter와 slug 규칙은 그대로 유지해야 한다.
- site repo 쪽에서 확인할 검증 항목은 별도 체크리스트로 묶어 함께 수행한다.

## 세부 실행 계획

1. 구조 합의
   `raw/wiki/assets/output` 4계층을 기준 구조로 확정한다.
2. 위키 원칙 고정
   위키는 human-first markdown 저장소로 유지하고, RAG 최적화는 이번 범위에서 제외한다고 명시한다.
3. upstream 자산 경계 확정
   블로그 이미지는 `assets/blog/`, 웹툰 제작 자산은 `assets/webtoon/`, 공용 자산은 `assets/shared/`로 나눈다.
4. 블로그 artifact 경계 확정
   `output/blog/`를 재생성 가능한 publish artifact 계층으로 두고 직접 편집 금지를 문서화한다.
5. 문서 계약 정리
   README, AGENTS, CLAUDE, `.codex`, `.claude`, publishing contract, operating playbook를 같은 경계로 맞춘다.
7. site 호환 계획 동시 수립
   `ai-survival-log-site`에서 유지해야 할 입력 경로, 이미지 경로, frontmatter 계약을 함께 명시한다.
8. 실제 파일 이동 전 사전 점검
   stale path 검색, hidden file 존재, `.gitkeep`/`.DS_Store` 처리 방식을 정한다.
9. 구현
   디렉토리 생성, 파일 이동, 스크립트/명령 문서 수정, 테스트 보강을 순차 적용한다.
10. 검증
   upstream wiki 검증과 downstream publish 호환 검증을 모두 수행한다.

## 안전 포인트

- `wiki/sources/`의 wikilink 체계는 유지하므로 위키 그래프는 깨지지 않는다.
- `wiki/`가 source of truth라는 원칙은 유지한다.
- `output/blog/`는 새 중간 산출물 계층이지만 최종 downstream 계약은 유지한다.
- `assets/` 도입으로 문서(`docs/`)와 자산을 분리할 수 있다.
- 블로그, 유튜브, 인스타그램, 웹툰 확장을 같은 패턴으로 수용할 수 있다.
- 위키 본체를 RAG 구조로 비틀지 않으므로 Obsidian/markdown 중심의 장점을 유지할 수 있다.

## 검증 체크리스트

- [ ] `python3 scripts/wiki sync` 오류 없음
- [ ] `python3 scripts/wiki lint` 에러 0건
- [ ] `python3 -m pytest tests/test_wiki_lib.py` 통과
- [ ] `sources/`, `book/`, `docs/images/`, `docs/webtoon/` stale 참조 grep 클린
- [ ] `assets/blog/` image upstream 규칙 문서와 코드가 일치
- [ ] publishable 페이지 1개로 `wiki -> output/blog -> ai-survival-log-site/content/posts` 테스트
- [ ] `ai-survival-log-site`에서 `content/posts/` 로딩과 `public/images/` 참조가 유지됨
- [ ] Claude/Codex/README/contract 문서가 동일한 경계를 설명함

## 관련 페이지

- [[projects/blog-ai-study-site]]
- [[projects/wiki-rag-expansion-roadmap]]
- [[projects/wiki-category-design-decision]]
- [[concepts/llm-wiki-pattern]]
