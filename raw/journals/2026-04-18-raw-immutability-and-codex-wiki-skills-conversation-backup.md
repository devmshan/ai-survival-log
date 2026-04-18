# 대화 백업: raw 불변 규칙 확인과 Codex용 wiki skill 추가

- **날짜:** 2026-04-18
- **성격:** 전체 대화 백업
- **맥락:** `raw/` 폴더의 불변 원칙이 충분히 강하게 문서화돼 있는지 확인하고, `raw` 자료를 바탕으로 위키 작업을 수행하는 Codex용 skill이 있는지 점검한 뒤, wiki 핵심 루프에 대응하는 Codex skill들을 추가한 세션
- **용도:** 추후 블로그 글 작성 시 원천 대화 기록으로 재사용
- **참고:** wiki 명령 surface와 운영 문서 정렬 세션은 `raw/journals/2026-04-18-wiki-surface-and-operating-docs-alignment-conversation-backup.md`에 저장됨

---

## 대화 원문 백업

### User

`raw 폴더는 절대 수정불가 규칙이 있는지 확인해주세요. 없으면 넣어주세요.

raw 폴더 자료를 가지고 ingest하는 스킬이 구현되어 있나요? 확인해주세요.`

### Assistant

`raw/` 수정 금지 규칙과 `raw` 기반 ingest 흐름이 실제로 어디까지 문서화/구현돼 있는지 확인하겠습니다. 규칙이 약하면 바로 보강하고, ingest 쪽은 현재 명령/스킬 수준까지 정확히 분리해서 정리하겠습니다.`

### Assistant

확인 결과 요약:

- `raw/` 불변 원칙은 이미 존재
  - `raw/AGENTS.md`
  - `raw/CLAUDE.md`
  - `CLAUDE.md`
  - `.claude/commands/wiki/ingest.md`
- 다만 표현은 “직접 수정하지 않는다” 수준이라, 더 강한 운영 규칙으로 보강하는 편이 낫다고 판단

### Assistant

보강 방향 안내:

- `raw/`는 불변 원본 계층임을 더 강하게 명시
- “한 번 저장한 원본은 절대 직접 수정하지 않는다”로 표현 강화
- 요약, 재서술, 태깅, 해설은 `wiki/`에서 한다는 점 명시
- 예외는 구조 마이그레이션처럼 명시적으로 승인된 이동/이관 작업뿐이라고 명시

### Assistant

실제 수정 파일:

- `raw/AGENTS.md`
- `raw/CLAUDE.md`
- `.claude/commands/wiki/ingest.md`

### Assistant

질문 2에 대한 확인 결과:

- `raw` 자료를 가지고 ingest하는 **Claude command**는 이미 구현되어 있음
  - `.claude/commands/wiki/ingest.md`
- 하지만 `raw -> wiki` ingest 전용 **Codex skill**은 아직 없었음

### User

`command 를 skill로 만들면 command는 삭제하는 것이 나을까요? command 전체를 skill 화 하는것은 어떨까요? 장단점 알려주세요.`

### Assistant

응답 요지:

- command와 skill은 역할이 겹치지만 동일하지 않음
- Claude 쪽은 slash command UX가 강하므로 command 전체 삭제는 권하지 않음
- 권장 구조는:
  - command는 실행 절차형 작업 유지
  - skill은 판단형/재사용형 지식으로 보강
- 유지 권장 command:
  - `/wiki:ingest`
  - `/wiki:lint`
  - `/wiki:publish`
  - `/content:book-study-blog`
- skill로 옮기기 좋은 것:
  - clipper template 추천
  - raw source 분류
  - publish readiness 점검
  - file-answer 카테고리 추천
  - query 결과 저장 위치 판단

### User

`그럼 codex는 skill 을 사용하지 않나요?`

### Assistant

응답 요지:

- Codex도 skill을 사용함
- 예시로 `.codex/skills/recommend-clipper-template/`가 이미 존재한다고 설명
- 다만 Claude는 command UX가 강하고, Codex는 skill + 문서 + 스크립트 중심이라고 정리

### User

`그럼 codex는 command를 사용하지 않나요?`

### Assistant

응답 요지:

- 현재 구조에서는 Codex가 Claude식 slash command surface를 직접 쓰는 방식은 아님
- Claude는 command 중심, Codex는 skill + 문서 + 스크립트 중심이라고 설명
- 따라서 `/wiki:*` command들에 대응하는 Codex skill을 따로 두는 것이 자연스럽다고 제안

### User

`뽑아주시고 codex용 스킬도 만들어주세요`

### Assistant

진행 안내:

- `wiki-ingest`, `wiki-query-answer`, `wiki-file-answer`, `wiki-lint`, `wiki-publish` 다섯 가지를 우선 Codex용 skill로 만들겠다고 설명

### Assistant

실행 결과:

추가된 Codex skill:

- `.codex/skills/wiki-ingest/SKILL.md`
- `.codex/skills/wiki-query-answer/SKILL.md`
- `.codex/skills/wiki-file-answer/SKILL.md`
- `.codex/skills/wiki-lint/SKILL.md`
- `.codex/skills/wiki-publish/SKILL.md`

각 skill의 역할:

#### `wiki-ingest`

- `raw/{type}`에서 source를 읽어 `wiki/sources`, `entities`, `concepts`, `topics`, 필요 시 `syntheses`까지 확장
- `raw/`는 절대 수정하지 않는다는 원칙 포함
- 마지막에 `python3 scripts/wiki sync`, `python3 scripts/wiki lint --summary` 흐름 포함

#### `wiki-query-answer`

- `wiki/index.md`에서 시작
- 관련 wiki 페이지와 필요 시 대응하는 `raw/{type}` 원본까지 확인
- 비교/판단 질문이면 `wiki/syntheses/`도 우선 검토

#### `wiki-file-answer`

- 답변/분석을 `entities`, `concepts`, `topics`, `syntheses`, `projects` 중 적절한 곳에 저장
- `syntheses/`와 `projects/` 선택 기준 포함

#### `wiki-lint`

- 위키 무결성 검사와 함께 `raw/wiki/assets/output` 경계 검토
- `assets/intake/`와 `assets/blog/` 역할 분리도 함께 점검

#### `wiki-publish`

- `published: true` 페이지를 `output/blog/` artifact로 내보내는 흐름
- downstream `ai-survival-log-site/content/posts/` 호환성 유지
- 채널 미정 자산은 `assets/intake/`, 실제 블로그 원본은 `assets/blog/`라는 규칙 포함

---

## 세션 핵심 결정

- `raw/`는 단순 불변 계층이 아니라 “절대 직접 수정하지 않는다”는 강한 운영 규칙으로 문서화해야 한다.
- Claude command와 Codex skill은 대체 관계가 아니라 병행 구조가 더 적절하다.
- Codex는 Claude식 slash command 대신 skill + 문서 + 스크립트 중심으로 위키 운영을 수행하는 쪽이 자연스럽다.
- `wiki-ingest`, `wiki-query-answer`, `wiki-file-answer`, `wiki-lint`, `wiki-publish`는 Codex에서 직접 재사용할 가치가 충분한 핵심 loop다.

## 이번 세션에서 실제 반영된 항목

- `raw/AGENTS.md` 불변 규칙 강화
- `raw/CLAUDE.md` 불변 규칙 강화
- `.claude/commands/wiki/ingest.md`의 raw 불변 규칙 표현 강화
- Codex용 wiki skill 5종 추가
- 현재 `wiki` command와 Codex skill의 역할 분리 원칙 정리

## 블로그 글 소재 포인트

- “불변 원본”이라는 원칙이 문서상으로는 있었지만, 실제 운영 레벨에서 얼마나 강하게 써야 하는지 다시 다듬은 과정
- Claude command와 Codex skill이 경쟁 관계가 아니라 상호 보완 구조라는 점을 정리한 부분
- 같은 저장소에서 에이전트 surface를 나눌 때, 어떤 작업은 command로 남기고 어떤 작업은 skill로 빼야 하는지 실제 기준을 세운 과정
