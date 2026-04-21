---
title: "시스템 설계 면접 8장 — URL 단축기 설계"
created: "2026-04-21"
updated: "2026-04-21"
type: topic
sources: ["[[sources/2026-04-21-system-design-interview-ch8]]"]
tags: [system-design, url-shortener, hash, base62, redirect, study, backend, interview]
status: active
published: false
slug: ""
description: ""
---

# 시스템 설계 면접 8장 — URL 단축기 설계

URL 단축기는 단순해 보이지만 리다이렉션 방식, 해시 충돌 전략, 캐시 설계, DB 스케일링까지 다양한 시스템 설계 원칙이 압축된 문제다. bit.ly를 예시로 삼아 전체 흐름을 설계한다.

## 문제 범위 확정

- 월 1억 건의 URL 단축 요청
- 단축 URL은 최대 10년 보관
- shortURL 길이는 7자리 (36^7 ≈ 3.5조, 10년치 수용)
- 읽기(리다이렉션) : 쓰기(단축) = 10:1

## 핵심 설계 결정

### 리다이렉션: 302 채택
클릭 통계 수집이 중요 → 301보다 302 선택.

### URL 단축: Base 62 인코딩 채택
해시 함수 방식 vs Base 62 인코딩:
- 해시: 구현 간단, 충돌 가능 → 재해시 로직 필요
- Base 62: 유일 ID 생성기 사용 → 충돌 없음 ✓

```
긴 URL 입력
  → ID 생성기([[concepts/unique-id-generator]])로 유일 ID 생성
  → Base 62 인코딩 → 7자리 shortURL
  → DB 저장
```

### 캐시 전략
- 자주 접근하는 shortURL 캐시 저장
- 80/20 법칙: 상위 20% URL이 80% 트래픽 처리
- 캐시 히트 → longURL 즉시 반환
- 캐시 미스 → DB 조회 → 캐시 갱신

## URL 리다이렉션 흐름

```
GET /{shortURL}
  → 캐시 확인
  → 히트: longURL 반환 (302 리다이렉션)
  → 미스: DB 조회 → 캐시 저장 → 302 리다이렉션
```

## 마무리 고려사항

- **처리율 제한:** 악의적 단축 URL 남용 방지
- **웹 서버 수평 확장:** stateless 구조
- **DB 다중화·샤딩:** 읽기 부하 분산
- **분석:** shortURL 클릭 통계, 리다이렉션 지역 분포
- **가용성·일관성·확장성**

## 면접 포인트

- 301 vs 302 선택 이유를 "통계 수집 필요 여부"로 설명
- Base 62와 해시 방식의 차이 및 각각의 충돌 처리를 명확히 설명
- 캐시 계층을 넣을 때 히트율 추정 방법 제시

## 관련 페이지

- [[concepts/url-shortener]]
- [[concepts/unique-id-generator]]
- [[concepts/cache-strategies]]
- [[sources/2026-04-21-system-design-interview-ch8]]
- [[projects/study-system-design-interview]]
