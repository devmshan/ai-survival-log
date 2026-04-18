---
description: "위키 무결성을 검사합니다 (깨진 링크, 고아 페이지 등)"
---

# /wiki:lint — 위키 무결성 검사

위키의 건강 상태를 전반적으로 검사하고 문제를 보고합니다.

## 워크플로우

### 1단계: 전체 파일 수집

- `wiki/` 하위의 모든 `.md` 파일 목록 수집 (index.md, log.md 포함)
- `wiki/index.md` 내용 읽기

### 2단계: 링크 검사

모든 위키 페이지에서 `[[wikilink]]`를 추출하고 검사합니다:

- **깨진 링크:** `[[target]]`의 target 파일이 존재하지 않는 경우
- **고아 페이지:** 어떤 페이지에서도 링크되지 않는 페이지 (index.md 제외)

### 3단계: 인덱스 검사

- **index.md 누락:** 실제 파일이 있지만 index.md에 없는 페이지
- **유령 항목:** index.md에 있지만 실제 파일이 없는 항목

### 4단계: Frontmatter 검사

모든 위키 페이지의 frontmatter 검증:

- 필수 필드 존재 확인: `title`, `created`, `updated`, `type`, `status`
- `type` 값이 올바른지 (entity/concept/source/topic/project/synthesis)
- `status` 값이 올바른지 (draft/active/archived)
- `published: true`인 페이지에 `slug`와 `description`이 있는지

### 5단계: 구조 검사

- `## 관련 페이지` 섹션이 없는 페이지
- 파일이 올바른 하위 폴더에 있는지 (`type`과 폴더 일치)
- `wiki/tags/`와 `.obsidian/` 같은 generated/local surface는 lint 대상에서 제외
- publishable 페이지의 이미지가 있으면 `assets/blog/` 원본과 downstream served copy 규칙이 문서상 맞는지 함께 확인

### 6단계: 보고

```markdown
## Wiki Lint Report

- 총 페이지: N개
- 마지막 log 기록: YYYY-MM-DD

### CRITICAL (수정 필요)
- [ ] 깨진 링크: [[target]] in file.md
- [ ] 유령 항목: index.md에 있지만 파일 없음

### WARNING (권장 수정)
- [ ] 고아 페이지: file.md (인바운드 링크 없음)
- [ ] frontmatter 불완전: file.md (missing: tags)
- [ ] 관련 페이지 섹션 누락: file.md

### INFO
- [ ] published: true 총 N개
- [ ] draft 상태 총 N개
```

## 자동 수정 제안

각 문제에 대해 자동 수정 가능 여부를 표시합니다.
사용자 승인 후 수정을 적용합니다.
