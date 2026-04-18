# 대화 백업: wiki 명령 surface와 운영 문서 정합성 보정

- **날짜:** 2026-04-18
- **성격:** 전체 대화 백업
- **맥락:** Web Clipper 템플릿과 intake 구조를 실제로 적용한 뒤, `wiki` 관련 명령/스킬과 운영 문서가 현재 프로젝트 구조(`raw/wiki/assets/output`)와 실제 운영 방식에 맞게 정렬되도록 문서 surface를 다시 조정한 세션
- **용도:** 추후 블로그 글 작성 시 원천 대화 기록으로 재사용
- **참고:** 템플릿 설계와 추천 스킬 추가는 `raw/journals/2026-04-18-clipper-template-intake-and-recommendation-conversation-backup.md`, Web Clipper 설정과 첫 실사용 검증은 `raw/journals/2026-04-18-web-clipper-setup-and-first-clip-conversation-backup.md`에 저장됨

---

## 대화 원문 백업

### User

`해결했습니다. 이제 wiki 스킬들을 현재 프로젝트 구조와 운영에맞춰 수정하고
운영방법 등이 적혀있는 wiki문서도 수정해야 될거 같습니다.

수정하고 지금까지의 대화도 0418에 맞춰 백업해주시겠어요?`

### Assistant

`현재 구조와 Web Clipper 운영까지 반영된 기준으로 wiki 관련 명령/스킬과 운영 문서를 다시 맞추겠습니다. 먼저 어떤 파일이 아직 이전 흐름을 전제하는지 확인한 뒤, 명령 문서 수정과 04-18 형식 대화 백업까지 한 번에 정리하겠습니다.`

### Assistant

점검 요약:

- `.claude/commands/wiki/*`와 `CLAUDE.md`를 재검토
- `/wiki:query`, `/wiki:file-answer`, `/wiki:lint`, `/wiki:publish` 설명이 실제 운영보다 단순하거나 일부 최신 경계를 반영하지 못하는 상태를 확인
- 특히 `syntheses/`, `output/blog`, `assets/intake/`, Web Clipper 기반 intake 루틴이 문서상 더 명확히 드러날 필요가 있다고 판단

### Assistant

수정 방향 안내:

- `/wiki:query`에 `wiki/sources/`와 대응하는 `raw/{type}` 원본 확인 흐름 추가
- 비교/판단 질문은 `wiki/syntheses/`도 함께 보도록 명시
- `/wiki:file-answer`에서 `syntheses/`와 `projects/` 선택 기준을 더 분명히 함
- `/wiki:lint`에서 `synthesis` 타입과 generated/local surface 제외 기준을 반영
- `/wiki:publish`에서 `output/blog` artifact 계층과 `assets/intake` → `assets/blog` 승격 원칙을 명시
- `CLAUDE.md`의 커맨드 워크플로우와 블로그 파이프라인 다이어그램을 현재 구조로 재정렬

### Assistant

실제 반영 파일:

- `.claude/commands/wiki/query.md`
- `.claude/commands/wiki/file-answer.md`
- `.claude/commands/wiki/lint.md`
- `.claude/commands/wiki/publish.md`
- `CLAUDE.md`

### Assistant

세부 반영 내용 요약:

#### `/wiki:query`

- `wiki/index.md`만 읽는 흐름에서 끝나지 않고, 필요 시 `wiki/sources/`에 대응하는 `raw/{type}` 원본도 확인하도록 정리
- 비교/판단 질문이면 `wiki/syntheses/`를 우선 보도록 명시
- 위키 외부 소스 추가가 필요할 때는 `assets/clipper-templates/`를 통해 `raw/{type}` 또는 `assets/intake/`로 먼저 intake하라고 안내

#### `/wiki:file-answer`

- 단순 저장이 아니라 답변 성격에 따라 `syntheses/`와 `projects/` 중 어디가 맞는지 먼저 판단하도록 정리
- 후속 source ingest 또는 publish 후보 여부를 함께 메모할 수 있게 함

#### `/wiki:lint`

- `type` 검증 목록에 `synthesis` 추가
- `wiki/tags/`, `.obsidian/` 같은 generated/local surface는 lint 대상에서 제외된다는 운영 기준을 명시
- publishable 페이지 이미지 규칙도 함께 확인 포인트로 추가

#### `/wiki:publish`

- 출력 기본 경로가 `output/blog/YYYY-MM-DD-{slug}.mdx`임을 명시
- downstream `ai-survival-log-site/content/posts/`는 동기화 대상이며 최종 계약 경로라는 점을 다시 분리
- `assets/intake/`는 채널 미정 inbox이고, publish 직전 실제 사용 블로그 이미지 원본만 `assets/blog/`에 있어야 한다고 명시

#### `CLAUDE.md`

- `/wiki:query`, `/wiki:file-answer`, `/wiki:lint`, `/wiki:publish` 워크플로우를 현재 구조 기준으로 재서술
- publish 파이프라인을 `wiki -> output/blog -> ai-survival-log-site/content/posts`로 다시 그림
- `output/blog/`와 downstream `content/posts/`가 모두 generated artifact라는 점을 명시
- 채널 미정 자산은 `assets/intake/`, 블로그 publish 직전 원본은 `assets/blog/`라는 규칙을 워크플로우에 반영

### Assistant

검증 결과:

- `python3 scripts/wiki lint --summary` → 오류 없음

### User

현재 세션에서는 Web Clipper 설정 문제를 해결한 뒤, wiki 명령과 운영 문서까지 현재 구조에 맞춰 다시 정렬해 달라고 요청

### Assistant

진행 결과:

- 문서 surface를 실제 운영에 맞게 재정렬
- 세션 내용을 `04-18` 형식 백업으로 저장

---

## 세션 핵심 결정

- `wiki` 명령 surface는 단순히 위키 파일만 보는 흐름이 아니라 `raw/{type}` source, `wiki/syntheses/`, `output/blog`, `assets/intake/`까지 포함한 현재 운영 경계를 반영해야 한다.
- `output/blog`는 publish 기본 산출물 계층이고, downstream site는 별도 동기화 대상이라는 점을 문서에 명확히 유지해야 한다.
- 채널 미정 자산은 `assets/intake/`에 두고, 블로그에 실제로 쓰기로 정한 원본만 `assets/blog/`로 승격시키는 원칙을 wiki 문서 surface에서도 일관되게 유지해야 한다.
- `syntheses/`는 단순 보조 카테고리가 아니라 비교, 통합, 판단 문서를 위한 핵심 저장 위치로 계속 드러나야 한다.

## 이번 세션에서 실제 반영된 항목

- `/wiki:query` 문서에 `raw/{type}` 확인 흐름과 `syntheses/` 우선 검토 원칙 추가
- `/wiki:file-answer` 문서에 `syntheses/` / `projects/` 선택 기준 추가
- `/wiki:lint` 문서에 `synthesis` 타입과 generated/local surface 제외 기준 추가
- `/wiki:publish` 문서에 `output/blog` artifact 경계와 `assets/intake` → `assets/blog` 승격 원칙 추가
- `CLAUDE.md` 커맨드 워크플로우와 publish 파이프라인 정렬

## 블로그 글 소재 포인트

- 구조 변경이 끝난 뒤에도 명령 surface와 운영 문서가 따라오지 않으면 실제 작업자는 오래된 모델로 행동하게 된다는 점
- Web Clipper, raw source, wiki syntheses, publish artifact, downstream site 계약이 한 흐름 안에서 연결돼야 한다는 점
- “문서 정합성”이 단순 README 문제가 아니라 실제 agent behavior를 좌우하는 운영 레이어라는 점
