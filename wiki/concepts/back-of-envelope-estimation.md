---
title: "개략적인 규모 추정 (Back-of-the-Envelope Estimation)"
created: "2026-04-15"
updated: "2026-04-15"
type: concept
sources: ["[[sources/2026-04-15-system-design-interview-ch2]]"]
tags: ["system-design", "estimation", "back-of-envelope", "qps", "capacity-planning"]
status: active
published: false
slug: ""
description: ""
---

# 개략적인 규모 추정 (Back-of-the-Envelope Estimation)

시스템 설계 면접에서 "QPS가 얼마야?", "저장소는 얼마나 필요해?"를 즉석에서 계산하는 능력. 정밀 계산이 아니라 올바른 규모 감각(order of magnitude)을 갖추는 게 핵심이다.

## 기본 단위 감각

### 2의 제곱수 (Powers of 2)

| 단위 | 바이트 | 규모 |
|------|--------|------|
| 1KB | 1,024 ≈ 10³ | 1 Thousand |
| 1MB | 1,048,576 ≈ 10⁶ | 1 Million |
| 1GB | ≈ 10⁹ | 1 Billion |
| 1TB | ≈ 10¹² | 1 Trillion |
| 1PB | ≈ 10¹⁵ | 1 Quadrillion |

실무 감각:
- 트윗 1개 텍스트 ≈ 140~200B
- 이미지 1장 ≈ 300KB~1MB
- HD 동영상 1분 ≈ 50~150MB

### 응답지연 기준값 (Latency Numbers)

| 연산 | 지연 |
|------|------|
| L1 캐시 참조 | 0.5ns |
| L2 캐시 참조 | 7ns |
| 주 메모리 참조 | 100ns |
| SSD 임의 읽기 (4KB) | 150µs |
| HDD 탐색 | 10ms |
| 같은 DC 내 패킷 왕복 | 0.5ms |
| 대륙 간 패킷 왕복 | 150ms |

**교훈:**
- 메모리(ns) >> SSD(µs) >> HDD(ms) — 계층별 차이가 10만 배 이상
- 같은 DC 내 통신(0.5ms) vs 대륙 간(150ms) — 300배 차이
- 디스크 탐색을 줄이는 것이 성능 최적화의 출발점

## QPS 추정 공식

```
QPS = DAU × 하루 평균 요청 수 / 86,400(초)
Peak QPS = QPS × 2
```

**DAU 추정 패턴:**
```
MAU → DAU = MAU × 일간 활성 비율 (보통 30~50%)
```

## 저장소 추정 공식

```
일간 데이터량 = 하루 건수 × 건당 크기
연간 데이터량 = 일간 × 365
N년 저장소 = 연간 × N
```

**미디어 포함 시 주의:**
- 텍스트(수십 ~수백 B) vs 이미지(수백 KB~MB) vs 영상(수십~수백 MB)
- 미디어가 있으면 텍스트는 무시해도 될 만큼 미디어가 지배적

## 실전 추정 예시 — 트위터

| 항목 | 가정 | 계산 |
|------|------|------|
| MAU | 3억 명 | - |
| DAU | MAU × 50% | 1.5억 명 |
| 하루 트윗 | DAU × 2건 | 3억 건 |
| QPS | 3억 / 86,400 | ≈ 3,500 |
| Peak QPS | QPS × 2 | ≈ 7,000 |
| 텍스트/일 | 3억 × 204B | ≈ 61.2GB |
| 미디어/일 | 3억 × 10% × 1MB | ≈ 30TB |
| 5년 저장소 | (30TB + 0.06TB) × 365 × 5 | ≈ 54.75PB |

## 추정 팁

1. **근사치 활용** — "98,673 / 9.1"은 "100,000 / 10 = 10,000"으로
2. **가정 명시** — 계산 전에 가정을 적고 면접관에게 확인
3. **단위 붙이기** — "5"가 아니라 "5MB"
4. **자주 구하는 값** — QPS, Peak QPS, 저장소, 캐시 크기, 서버 수

## 관련 페이지

- [[concepts/availability]]
- [[concepts/vertical-vs-horizontal-scaling]]
- [[sources/2026-04-15-system-design-interview-ch2]]
- [[topics/system-design-interview-02]]
