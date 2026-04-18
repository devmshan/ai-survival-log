# 대화 백업: Obsidian Web Clipper 설정 마무리와 첫 클리핑 확인

- **날짜:** 2026-04-18
- **성격:** 전체 대화 백업
- **맥락:** Obsidian Web Clipper에 템플릿을 등록하고, 트리거 규칙과 수동 선택 전략을 정리하고, 첫 실제 클리핑 파일 `2026-04-18T193443+0900-AI 코딩 어시스턴트를 위한 지식 그래프 스킬.md`까지 확인한 세션
- **용도:** 추후 블로그 글 작성 시 원천 대화 기록으로 재사용
- **참고:** 템플릿 설계 및 intake 구조 재정의 세션은 `raw/journals/2026-04-18-clipper-template-intake-and-recommendation-conversation-backup.md`에 저장됨

---

## 대화 원문 백업

### User

`옵시디언 웹클리퍼 설정에 새로운 템플릿 등록하게 리스트 준비해주세요.`

### Assistant

응답 요지:

- Web Clipper에 `가져오기`로 등록할 템플릿 목록을 정리
- 템플릿별 파일 경로와 추천 등록 순서를 제안
- `Article Deep Research`, `Video Transcript Notes`, `Podcast Episode Notes`, `Book Chapter Notes`, `Asset Reference Note`, `Generic Source Capture`를 우선 등록 대상으로 추천

### User

스크린샷 3장을 전달하며 현재 Obsidian Web Clipper의 템플릿 편집 화면을 공유

### Assistant

응답 요지:

- 이 UI 기준으로는 JSON을 `가져오기`로 하나씩 등록하면 된다고 설명
- 등록 대상 10개 템플릿과 추천 순서를 다시 정리
- 중요 포인트로 채널 미정 자산은 `assets/intake/reference-notes` 쪽으로 받는 게 맞다고 안내

### User

`추천 규칙 문구까지 각각써서 주세요.`

### Assistant

실행 결과:

- 10개 템플릿 각각에 대해 `템플릿 트리거` 칸에 붙여 넣을 URL 패턴을 작성
- `Article Quick Capture`, `Generic Source Capture`에는 `https://*`를 넣는 fallback 방안도 함께 설명

### User

`네 더 깔끔하게 다시 정리해주세요`

### Assistant

실행 결과:

- 각 템플릿별로 복붙 가능한 형태로 다시 정리
- 템플릿 파일 경로와 트리거 블록을 깔끔한 목록으로 제시

### User

`붙인 버전까지 정리해주세요.`

### Assistant

응답 요지:

- 템플릿 이름 앞에 번호를 붙이면 Web Clipper 목록 정렬이 안정된다고 설명
- 추천 순서를 다음처럼 제안:
  - `01 Article Deep Research`
  - `02 Video Transcript Notes`
  - `03 Podcast Episode Notes`
  - `04 Book Chapter Notes`
  - `05 Book Quote Capture`
  - `06 Conversation Backup`
  - `07 Asset Reference Note`
  - `08 Journal Insight Capture`
  - `09 Article Quick Capture`
  - `10 Generic Source Capture`

### User

`일괄 수정해주세요.`

### Assistant

실행 결과:

- `assets/clipper-templates/*.json`의 `name` 값을 위 번호 체계로 일괄 변경
- JSON 유효성 확인 완료

### User

Obsidian Web Clipper 화면 스크린샷을 공유하며:
`전부 10 템플릿으로 고정됩니다.`

### Assistant

응답 요지:

- 원인은 `10 Generic Source Capture`의 트리거 `https://*`가 모든 URL을 잡아먹는 것이라고 진단
- `09 Article Quick Capture`도 `https://*`면 같은 문제가 발생한다고 설명
- 해결책으로 두 템플릿은 수동 선택용으로 두고 `템플릿 트리거`를 비우라고 안내

### User

`수동 선택용으로 두려면 트리거를 지우면 되나요?`

### Assistant

응답 요지:

- 네, 수동 선택용 템플릿은 트리거를 비우면 된다고 설명
- 수동 선택 템플릿으로 `08 Journal Insight Capture`, `09 Article Quick Capture`, `10 Generic Source Capture`를 권장

### User

`완료했습니다. 지금 대화와 옵시디언 웹클리퍼 설정 과정, 그리고 첫 클리핑 파일 2026-04-18T193443+0900-AI 코딩 어시스턴트를 위한 지식 그래프 스킬 까지를 읽고 대화를 0418에 맞춰서 백업해주세요.`

### Assistant

진행 안내:

- 첫 클리핑 파일을 찾고 읽은 뒤, `04-18` 형식의 후속 대화 백업으로 저장하겠다고 알림

---

## 첫 클리핑 파일 확인

확인한 파일:

- `wiki/raw/articles/2026-04-18T193443+0900-AI 코딩 어시스턴트를 위한 지식 그래프 스킬.md`

파일 내용 요약:

- `title`: AI 코딩 어시스턴트를 위한 지식 그래프 스킬
- `source`: `https://graphify.net/kr/`
- `source_type`: `article`
- `ingest_target`: `raw/articles`
- `recommended_harness`: `/wiki:ingest`
- `description`: Graphify를 AI 코딩 어시스턴트용 멀티모달 지식 그래프 빌더로 설명
- 본문에는 `Why This Matters`, `Summary Seed`, `Extraction Priorities`, `Raw Clip` 섹션이 포함됨
- 실제 clipped content는 Graphify 소개, 주요 기능, 설치/실행, 비교, 보안, FAQ까지 포함하는 긴 article 형식

확인 포인트:

- 템플릿 자체는 article용으로 잘 적용됨
- 다만 실제 저장 위치가 현재 `raw/articles`가 아니라 `wiki/raw/articles/`로 들어가 있음
- 즉, Obsidian Web Clipper의 보관소 기준 경로나 노트 루트 설정이 현재 vault 루트와 기대 경로 사이에서 한 단계 어긋나 있을 가능성이 높음

## 세션 핵심 결정

- Web Clipper의 fallback 템플릿은 자동 트리거를 가지면 안 된다.
- `https://*` 같은 전역 트리거는 `Generic Source Capture`와 `Article Quick Capture`에서 제거해야 한다.
- 수동 선택용 템플릿은 트리거를 비워 두는 방식이 맞다.
- 번호 붙인 템플릿 이름은 실제 UI 정렬 안정성에 유효하다.
- 첫 실제 클리핑으로 article 템플릿 구조는 유효성이 확인됐지만, 저장 위치는 추가 점검 대상이다.

## 이번 세션에서 실제 확인/반영된 항목

- Obsidian Web Clipper 템플릿 등록 리스트 정리
- 템플릿별 추천 트리거 문구 정리
- 번호 붙인 템플릿 이름 체계 적용
- 전역 fallback 트리거 문제 원인 분석
- 수동 선택 템플릿 운용 원칙 정리
- 첫 실제 클리핑 파일 내용과 저장 위치 확인

## 블로그 글 소재 포인트

- 템플릿 설계만으로 끝나지 않고, 실제 Web Clipper UI에서 fallback 템플릿이 모든 페이지를 잡아먹는 문제를 발견한 과정
- “수동 템플릿은 트리거를 비워야 한다”는 작은 운영 원칙이 실제 사용성에 큰 차이를 만든 점
- 첫 클리핑 파일이 템플릿 구조를 잘 따르면서도 저장 위치가 `wiki/raw/articles/`로 들어간 것을 통해 vault 경로 설정 문제를 발견한 점
- 설계, 실제 UI 설정, 첫 실사용 검증까지 한 흐름으로 이어졌다는 점
