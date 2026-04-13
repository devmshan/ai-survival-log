---
title: "AI 웹툰 제작"
created: "2026-04-13"
updated: "2026-04-13"
type: topic
sources: ["[[sources/2026-04-13-ai-webtoon-workflow]]"]
tags: ["ai-webtoon", "instagram", "character-design", "devsurvivallog", "midjourney", "workflow"]
status: active
published: false
slug: ""
description: ""
---

# AI 웹툰 제작

> devsurvivallog 인스타툰을 AI로 제작하기 위한 도구, 워크플로우, 캐릭터 설계 지식 모음.

## 핵심 과제: 캐릭터 일관성

웹툰은 패널마다 **동일한 캐릭터**가 등장해야 한다.
AI 이미지 생성의 가장 큰 약점이 바로 이 일관성 문제.

### 해결 방법별 비교

| 방법 | 일관성 | 난이도 | 비용 |
|------|--------|--------|------|
| Midjourney `--cref` | ★★★★★ | 쉬움 | $10/월 |
| ChatGPT 같은 대화창 | ★★★★☆ | 가장 쉬움 | 무료~$20 |
| SD + 캐릭터 LoRA | ★★★★★ | 어려움 | 무료(GPU) |
| 매번 상세 프롬프트 | ★★★☆☆ | 보통 | 종량제 |

## 레퍼런스 계정

### darongtoon — 웹툰 진행 방식
- 심플 손그림 선화, 얼굴 디테일 최소화
- 파스텔 블루 단색 배경
- 슬라이드 카드 형식 (①②③)
- **스토리텔링 > 그림 실력**

### marigold.in.bloom — 개발자툰 스타일
- 치비 캐릭터 + Mac 화면 목업
- 개발 경험 → 콘텐츠화
- 따뜻한 노란 계열

## 민성+건승 웹툰 방향

### 세계관
> 민성은 AI에게 해체되는 중이고, 건승이는 그 옆에서 녹아내리고 있다.

### 비주얼 정체성
- **배경**: 미드나잇 블루, 새벽 하늘 그라데이션
- **색 대비**: 블루(민성) vs 오렌지(건승) — 건승이 포인트 컬러
- **필름 톤**: 저채도, 약간 desaturated
- **빛**: 모니터 빛, 새벽 분위기

### 캐릭터 시트 이미지
- `docs/민성과 건승의 귀여운 표정들.png` — 표정 3종씩
- `docs/고양이와 함께 하는 코드 작업.png` — 코딩 장면

## 제작 워크플로우

```
1. Midjourney Niji 6 or ChatGPT로 장면 생성
   (--cref로 캐릭터 일관성 유지)
        ↓
2. 배경 제거 or 패널 크롭
        ↓
3. Canva에서 슬라이드 레이아웃
   말풍선, 텍스트, 에피소드 번호 추가
        ↓
4. Instagram 게시
```

## 프롬프트 뱅크

### 기본 캐릭터 시트 (Midjourney)
```
Korean webtoon character sheet, simple hand-drawn style,
male character short black hair round glasses navy hoodie holding phone,
orange tabby cat melting flat on ground,
midnight blue gradient background, film grain, desaturated tones,
quiet introspective mood, tokyo night blue aesthetic
--niji 6 --ar 1:1
```

### 코딩 장면 (Midjourney)
```
anime illustration style, young Korean male developer coding at desk,
seen from behind, short black hair round glasses navy blue hoodie,
orange tabby cat lying flat next to laptop with annoyed expression,
VS Code on screen, white coffee mug,
midnight blue atmosphere, monitor glow lighting only
--niji 6 --ar 3:4
```

### ChatGPT 인스타 무드 반영 버전
```
이미지 첨부 후:
"같은 캐릭터로, 배경을 미드나잇 블루로,
필름 느낌으로 desaturated하게 바꿔줘.
[상황 설명]"
```

## 관련 페이지

- [[entities/minsung]]
- [[entities/gunseung]]
- [[entities/devsurvivallog]]
- [[projects/character-intro-draft]]
- [[sources/2026-04-13-ai-webtoon-workflow]]
