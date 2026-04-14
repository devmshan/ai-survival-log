---
title: "무상태 아키텍처 (Stateless Architecture)"
created: "2026-04-14"
updated: "2026-04-14"
type: concept
sources: ["[[sources/2026-04-14-system-design-interview-v1]]"]
tags: ["system-design", "stateless", "scalability", "web-tier", "distributed-systems"]
status: active
published: false
slug: ""
description: ""
---

# 무상태 아키텍처 (Stateless Architecture)

수평 확장(Scale Out)을 가능하게 하는 핵심 아키텍처 원칙. 웹 계층에서 상태 정보를 제거한다.

## 상태(State)가 있는 구조의 문제

```
사용자 A → 서버1 (세션 정보 보관)
사용자 A → 서버2 ❌ (서버2는 사용자 A의 세션 정보 없음)
```

- 특정 서버가 특정 사용자의 세션 데이터를 보관
- 같은 사용자의 요청이 반드시 같은 서버로 가야 함
- 로드밸런서에서 스티키 세션(sticky session) 설정 필요 → 로드밸런싱 효율 저하
- 서버 추가/제거 시 세션 데이터 문제 발생

## 무상태 구조 (Stateless)

```
사용자 A → 서버1
           서버2  → 공유 저장소(NoSQL/Redis) → 세션 데이터
           서버3
```

- 상태 정보를 **공유 데이터 저장소**(Shared Storage)에 분리
- 웹 서버는 상태 없이 요청만 처리
- 어떤 서버로 요청이 가든 동일한 처리 가능

## 공유 저장소 옵션

| 저장소 | 특징 |
|--------|------|
| Redis | 인메모리, 빠른 읽기/쓰기, 세션 저장에 적합 |
| Memcached | 단순 key-value, 빠름 |
| NoSQL (DynamoDB 등) | 대규모 분산 세션 저장 |
| RDBMS | 느리지만 일관성 보장 |

## 장점

- 어떤 서버로도 요청 처리 가능 → 로드밸런서가 자유롭게 분배
- 서버 추가/제거 용이 → 자동 확장(Auto Scaling) 연동 쉬움
- 단순하고 안정적인 구조

## 핵심 원칙

> 웹 서버에는 상태를 저장하지 않는다.
> 상태는 항상 공유 저장소에 있어야 한다.

이 원칙이 지켜져야 수평 확장이 자유로워진다.

## 관련 페이지

- [[concepts/load-balancer]] — 무상태 아키텍처와 함께 사용
- [[concepts/vertical-vs-horizontal-scaling]] — 수평 확장을 위한 전제 조건
- [[concepts/cache-strategies]] — 공유 저장소로 캐시 활용
- [[concepts/saml]] — SSO 환경에서의 세션 관리
- [[projects/study-system-design-interview]] — 시스템 설계 스터디
