---
title: "AI 웹툰 제작 워크플로우 탐색"
created: "2026-04-13"
updated: "2026-04-13"
type: source
sources: []
tags: ["ai-webtoon", "character-design", "midjourney", "chatgpt", "devsurvivallog", "instagram", "workflow"]
status: active
published: false
slug: ""
description: ""
---

# AI 웹툰 제작 워크플로우 탐색

> 2026-04-13 세션. devsurvivallog 인스타툰 제작을 위한 AI 도구 탐색, 레퍼런스 분석, 캐릭터 프롬프트 작성 과정 기록.

## 핵심 요약

- fal.ai 잔액 소진으로 대안 도구 탐색 시작
- 레퍼런스 계정 3곳 분석: marigold.in.bloom, darongtoon, _intotheblu
- AI 웹툰의 핵심 과제는 **캐릭터 일관성** — Midjourney `--cref` 또는 ChatGPT 같은 대화창 활용
- 민성+건승 캐릭터 시트 이미지 2종 확보
- ChatGPT / Midjourney 용 프롬프트 완성

## 레퍼런스 분석

### marigold.in.bloom — 개발자툰 방향성
- 치비 캐릭터 + Mac 목업 조합
- 실제 개발 경험 → 콘텐츠화
- 따뜻한 노란/앰버 색감

### darongtoon — 웹툰 진행 방식
- **심플 손그림 선화**, 얼굴 디테일 최소화
- 파스텔 블루 단색 배경 + 웨이브 레이어
- 슬라이드 카드 형식, 에피소드 번호 표시
- 그림 실력보다 스토리텔링 중심

### _intotheblu — 민성 인스타 무드
- 미드나잇 블루, 새벽 하늘, 골든아워 오렌지
- 저채도 필름 느낌, 사색적·조용한 분위기
- 오렌지(건승) vs 블루(민성) 대비 구조

## 도구 결론

| 우선순위 | 도구 | 이유 |
|---------|------|------|
| 1순위 | **Midjourney Niji 6** | 웹툰 품질 최상, `--cref` 일관성 |
| 2순위 | **ChatGPT GPT-4o** | 무료 시작 가능, 이미지 첨부로 일관성 |
| 보조 | **Canva** | 패널 조합, 텍스트, 말풍선 |

## 확보된 이미지 레퍼런스

### 1. `docs/소년과 고양이 감정 변화 모음.png` — 캐릭터 감정 시트

**민성 표정 8종**
- 미소 / 슬픔 / 머리 긁적(생각중) / 크게 웃음
- 눈물·감동 / 손으로 입 가리기 / 놀람·당황 / 화남·짜증

**건승 표정 6종**
- 짜증·무표정 / 화남(눈 가늘게) / 하품
- 눈 감음 / 놀람·화 / 기본 납작

**스타일 특징**
- 치비·둥글둥글, 깔끔한 선화, 흰 배경
- 민성: 짧은 검은 머리(약간 텁수룩), 둥근 안경, **회색 후드티**
- 건승: 주황 줄무늬 치즈 태비, 납작하게 늘어진 기본 자세

### 2. `docs/고양이와 함께 하는 코드 작업.png` — 코딩 장면 일러스트

**장면 구성**
- 민성 뒷모습 + 측면 — 검은 머리, 안경, 회색 후드티, 의자
- 건승 — 노트북 옆 납작하게 늘어짐, 짜증 표정
- 소품: 노트북(코드 에디터 화면), 흰 커피잔
- 배경: 흰 커튼, 자연광 분위기

**스타일 특징**
- 감정 시트보다 현실적인 애니 일러스트 퀄리티
- 세로 portrait 구도 (3:4)
- 따뜻한 자연광 톤

## 스타일 교정 사항

> 이미지 확인 후 업데이트

- 민성 후드티: ~~네이비~~ → **회색** (실제 시안 기준)
- 표정: 8종 확보로 다양한 에피소드 대응 가능
- 건승: 납작 자세가 기본형, 짜증·화남 표정이 핵심 매력

## 완성된 프롬프트

### ChatGPT — 캐릭터 시트 (이미지 첨부용)
```
소년과 고양이 감정 변화 모음.png 이미지를 참고해서
같은 캐릭터로 [상황] 장면을 그려줘.

배경: 미드나잇 블루 그라데이션
색보정: 필름 느낌, 살짝 desaturated
빛: 모니터 빛만, 새벽 분위기
```

### Midjourney — 캐릭터 시트
```
Korean webtoon character sheet, simple chibi style,
male character short black messy hair round glasses gray hoodie,
orange tabby cat lying flat multiple expressions,
white background, clean line art, flat colors,
cute anime style, emotion reference sheet
--niji 6 --ar 2:3
```

### Midjourney — 코딩 장면 (고양이와 함께 하는 코드 작업 스타일)
```
anime illustration style, young Korean male developer coding at desk,
seen from behind, short black hair, round glasses, gray hoodie,
orange tabby cat lying flat next to laptop with annoyed expression,
VS Code on screen, white coffee mug,
warm natural light, white curtain background, detailed interior
--niji 6 --ar 3:4
```

### Midjourney — 인스타 무드 버전 (_intotheblu 감성)
```
anime illustration style, young Korean male developer coding at desk,
short black hair, round glasses, gray hoodie,
orange tabby cat next to laptop annoyed expression,
midnight blue atmosphere, monitor glow only, no natural light,
desaturated film tone, quiet introspective mood, tokyo night blue
--niji 6 --ar 3:4
```

## 관련 페이지

- [[entities/minsung]]
- [[entities/gunseung]]
- [[projects/character-intro-draft]]
- [[topics/ai-webtoon-creation]]
