---
title: "블룸 필터 (Bloom Filter)"
created: "2026-04-21"
updated: "2026-04-21"
type: concept
sources: ["[[sources/2026-04-21-system-design-interview-ch6]]", "[[sources/2026-04-21-system-design-interview-ch9]]"]
tags: [system-design, bloom-filter, probabilistic, distributed-systems, cache]
status: active
published: false
slug: ""
description: ""
---

# 블룸 필터 (Bloom Filter)

원소가 집합에 속하는지 확률적으로 판단하는 공간 효율적인 자료구조. Burton Howard Bloom이 1970년에 제안.

## 핵심 특성

- **False Positive 가능:** "있다"고 답했지만 실제로 없을 수 있음
- **False Negative 없음:** "없다"고 답하면 실제로 반드시 없음
- **삭제 불가 (기본):** 원소를 추가하면 제거 불가 (Counting Bloom Filter로 해결 가능)
- **공간 효율:** 수십억 원소를 수 MB~GB 수준으로 표현

## 동작 원리

1. 비트 배열(m 비트) 초기화, k개의 해시 함수 준비
2. **삽입:** 원소에 k개 해시 적용 → 해당 비트 위치를 1로 설정
3. **조회:** k개 해시 적용 → 모든 비트가 1이면 "있을 수 있음", 하나라도 0이면 "없음"

## 활용 사례

### 키-값 저장소 (읽기 경로)
SSTable이 여러 개일 때, 특정 키가 어떤 SSTable에 있는지 확인하기 위해 블룸 필터 사용. 디스크 조회 횟수를 획기적으로 줄임.

### 웹 크롤러 (URL 중복 제거)
수십억 개의 URL을 메모리에 올릴 수 없으므로 블룸 필터로 이미 방문한 URL 여부를 빠르게 확인.

### 기타
- 데이터베이스 캐시 레이어 (존재하지 않는 키에 대한 DB 조회 차단)
- 네트워크 패킷 중복 제거
- 비밀번호 유효성 검사 (이미 사용된 비밀번호 확인)

## 설계 파라미터

- m (비트 배열 크기) ↑ → False Positive 감소, 메모리 증가
- k (해시 함수 수) 최적값 존재: k = (m/n) × ln2 (n: 예상 원소 수)

## 관련 페이지

- [[concepts/key-value-store]]
- [[concepts/web-crawler]]
- [[sources/2026-04-21-system-design-interview-ch6]]
- [[sources/2026-04-21-system-design-interview-ch9]]
