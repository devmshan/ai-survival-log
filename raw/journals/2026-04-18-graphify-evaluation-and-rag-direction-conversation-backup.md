# 대화 백업: Graphify 평가와 RAG 방향 재정리

- **날짜:** 2026-04-18
- **성격:** 전체 대화 백업
- **맥락:** `graphify`를 현재 프로젝트 구조에 도입할 가치가 있는지 점검하고, `wiki/`를 graphify 친화 구조로 바꿀 필요가 있는지 검토한 뒤, 장기 방향을 `wiki` 파생형 retrieval abstraction으로 정리한 세션
- **용도:** 추후 블로그 글 작성 시 원천 대화 기록으로 재사용
- **참고:** 구조 변경과 clipper 설계 관련 세션은 `raw/journals/2026-04-18-codex-folder-structure-execution-and-publish-conversation-backup.md`, `raw/journals/2026-04-18-clipper-template-intake-and-recommendation-conversation-backup.md`, `raw/journals/2026-04-18-web-clipper-setup-and-first-clip-conversation-backup.md`에 저장됨

---

## 대화 원문 백업

### User

`pip install graphifyy 실행해서 그래피파이를 설치해주세요`

### Assistant

설치 후 확인 결과:

- `graphifyy 0.4.23` 설치 완료
- 주요 의존성도 함께 설치됨
- 이어서 사용법 확인 또는 저장소 적용 방식을 정리할 수 있다고 안내

### User

`2번 보여주세요`

### Assistant

초기 판단:

- Graphify는 이 저장소에서 `raw/`, `wiki/` 등을 그래프처럼 탐색하는 보조 도구일 수 있음
- 다만 source of truth를 대체하는 것이 아니라 보조 탐색 레이어로 써야 한다고 정리
- 우선 `wiki/`를 대상으로 보는 것이 자연스럽다고 설명

### User

`graphify update wiki`

### Assistant

실행 결과:

- `graphify update wiki`는 실패
- 이유는 `update`가 코드 파일 재추출용이며 `wiki/`는 Markdown 중심 폴더이기 때문
- 실제 출력은 `No code files found`, `Nothing to update`

### User

`graphify wiki`

### Assistant

실행 결과:

- `graphify wiki`는 지원되지 않는 명령
- `unknown command 'wiki'`로 확인

### Assistant

추가 점검 방향 안내:

- CLI에 어떤 명령이 실제로 노출되는지 확인
- 패키지 내부에서 `ingest`, `export`, Obsidian 관련 기능이 어느 정도 구현돼 있는지 확인
- 이 저장소에서 Graphify가 `wiki` 주력 도구인지, `raw` 수집 보조인지 구분해 정리하겠다고 안내

### Assistant

로컬 패키지 확인 결과:

- CLI 주요 명령:
  - `install`
  - `add <url>`
  - `watch <path>`
  - `update <path>`
  - `query`
  - `path`
  - `explain`
- `graphify.ingest`는 URL을 받아 Markdown/PDF/이미지/유튜브 오디오 등을 `raw` 유사 폴더에 저장하는 역할
- `graphify.export`에는 Obsidian export 함수가 존재
- 따라서 현재 버전의 Graphify는 `wiki/`를 직접 운영하는 도구라기보다 `raw` 수집과 그래프 탐색 보조에 더 가깝다고 판단

### User

`graphify는 md파일들을 graph db로 만들어주고 graph db 를 쿼리하는 방식으로 진행된다고 알고 있습니다
graphify는 wiki 구조에서 md 파일이 많을때 생기는 단점들을 커버하기위해 개발된 것으로 보여집니다.

현재 우리 프로젝트를 graphify 친화적으로 변경하는것의 장단점 그리고 기존 계획인 rag 추상화 방법과는 어떻게 다른지 알고 싶습니다.`

### Assistant

응답 요지:

- 사용자의 이해는 절반만 맞다고 설명
- Graphify는 결과적으로 그래프를 만들고 쿼리하긴 하지만, 현재 버전은 `wiki/` markdown-first 운영 도구로 보기 어려움
- 이 저장소를 graphify 친화적으로 바꿀 때의 장점:
  - 허브 노드, 관계 경로, 연결 구조를 기계적으로 볼 수 있음
  - 시각화와 탐색 surface가 좋아질 수 있음
- 단점:
  - `wiki/`의 human-first 원칙이 흔들릴 수 있음
  - 도구에 맞춰 frontmatter, 링크, 파일 규칙을 바꾸게 될 가능성이 큼
  - `wiki`와 `graphify-out`의 이중 구조가 생김
  - 현재 CLI와 이 저장소의 구조 적합성이 높지 않음
- RAG와의 차이:
  - Graphify는 명시적 관계 그래프 중심
  - RAG는 chunk/embedding/vector retrieval 중심
- 권장안:
  - `wiki/` 구조를 graphify 친화적으로 바꾸지 말 것
  - 필요하면 나중에 `wiki/`에서 graph projection을 파생시키는 방향이 더 적절

### User

`그럼 graphify 친화방식으로 하지 않아도 괜찮다는 말이네요? 결국은 graphify를 다운로드해서 사용할 메리트가 없어보이는데 맞나요?`

### Assistant

응답 요지:

- 현재 프로젝트 기준으로는 `graphify` 친화 방식으로 바꿀 필요가 없다고 명확히 답변
- `graphify`는 지금 운영의 필수 도구도 아니고, 당장 큰 생산성 향상을 주는 도구도 아니라고 정리
- “써볼 가치는 있었지만 현재 운영의 핵심 도구로 채택할 메리트는 낮다”고 판단
- 대신 장기적으로는 `wiki/`에서 파생되는
  - vector RAG
  - graph projection
  - hybrid retrieval
  방향이 더 적절하다고 정리

### User

`네 지금 판단을 반영해주시고 graphify 는 삭제하도록 하겠습니다.`

### Assistant

실행 안내:

- 판단을 로드맵과 운영 문서에 반영
- 시스템에 설치된 `graphifyy` 패키지를 제거
- 문서 검증 후 삭제까지 처리하겠다고 설명

### Assistant

실제 반영:

- `wiki/projects/wiki-rag-expansion-roadmap.md`
  - `graphify` 친화 구조로 위키를 재편하지 않는다는 판단 추가
  - `wiki/`에서 파생되는 retrieval abstraction이 장기 방향이라는 점 추가
- `docs/operating-playbook.md`
  - `graphify`를 현재 운영 의존성으로 두지 않는다는 원칙 추가
  - graph DB 도구 때문에 저장소 구조를 선제적으로 바꾸지 않는다는 규칙 추가

### Assistant

검증 및 삭제 결과:

- `python3 scripts/wiki lint --summary`
  - `오류 없음`
- `python3 -m pip uninstall -y graphifyy`
  - `graphifyy 0.4.23` 제거 완료
- 이후 `graphify --help`
  - `command not found`로 확인

---

## 세션 핵심 결정

- 현재 프로젝트는 `graphify` 친화 구조로 재편할 필요가 없다.
- `wiki/`는 계속 human-first markdown source of truth로 유지한다.
- graph DB가 필요하더라도 `wiki/`를 소비하는 파생 계층으로만 다룬다.
- 장기 방향은 `graphify` 종속 구조가 아니라 `wiki` 기반 retrieval abstraction이다.
- `graphify`는 현재 운영의 필수 도구가 아니므로 제거해도 무방하다.

## 이번 세션에서 실제 반영된 항목

- `wiki/projects/wiki-rag-expansion-roadmap.md`에 Graphify 비채택 판단 반영
- `docs/operating-playbook.md`에 Graphify 비의존 운영 원칙 반영
- `graphifyy` 패키지 제거

## 블로그 글 소재 포인트

- “md가 많아지면 graph DB가 정답인가?”라는 질문에 대해, 실제 도구 검증을 통해 왜 당장 채택하지 않기로 했는지 설명할 수 있는 세션
- human-first wiki와 graph-first tooling 사이의 긴장을 실제 운영 기준으로 정리한 사례
- RAG와 graph DB를 같은 범주로 뭉뚱그리지 않고, 각자의 역할을 어떻게 분리해 이해할지 보여주는 사례
