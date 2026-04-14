---
title: "SAML 프로토콜"
created: "2026-04-14"
updated: "2026-04-14"
type: concept
sources: ["[[sources/2026-04-14-system-design-study-ch1-deep-dive]]"]
tags: ["system-design", "auth", "sso", "session", "security"]
status: active
published: false
slug: ""
description: ""
---

# SAML 프로토콜

SSO(Single Sign-On)를 구현하는 XML 기반 인증 프로토콜. 인증을 IdP에 위임하는 구조.

## 등장인물

| 역할 | 설명 | 예시 |
|------|------|------|
| **IdP** (Identity Provider) | 인증 담당 | 회사 계정 서버 |
| **SP** (Service Provider) | 접근하려는 서비스 | 사내 앱, 전자결재 |

## 인증 흐름

```
1. 유저 → SP 접근
2. SP → IdP로 리다이렉트 (SAML Request)
3. 유저 → IdP에서 로그인
4. IdP → SAML Assertion(XML 토큰) 발급
5. SP → Assertion 검증 → 자체 세션 생성
```

## 세션이 두 개 생성됨

| 세션 | 위치 | 역할 |
|------|------|------|
| **IdP 세션** | IdP 서버 | "이 유저는 이미 인증됨" |
| **SP 세션** | SP 서버 (쿠키) | "이 유저는 이 서비스 이용 중" |

IdP 세션이 살아있으면 → 다른 SP 접근 시 로그인 없이 바로 Assertion 발급 = **SSO 동작**

## 로그아웃 종류

**로컬 로그아웃** — SP 세션만 삭제, IdP 세션 유지
→ 다른 서비스는 여전히 로그인 상태

**글로벌 로그아웃 (SLO)** — IdP가 연결된 모든 SP에 로그아웃 전파
→ 모든 서비스에서 동시에 로그아웃

## 일반 세션 vs SAML 비교

| | 일반 세션 | SAML |
|--|---------|------|
| 인증 주체 | 서비스 자체 | IdP가 대신 |
| 세션 수 | 1개 | 2개 (IdP + SP) |
| SSO | ❌ | ✅ |
| 구현 복잡도 | 단순 | 복잡 |
| IdP 장애 시 | 서비스 정상 | 모든 서비스 로그인 불가 |

## 언제 쓰나

| 상황 | 선택 |
|------|------|
| 작은 서비스, 빠른 개발 | 일반 세션 |
| 사내 여러 시스템 통합 | SAML |
| 소셜 로그인 | OAuth (SAML 경량화) |

대기업 사내 시스템이 SAML 많이 쓰는 이유: 직원 퇴사 시 IdP 계정 하나만 삭제하면 모든 사내 서비스 접근 차단.

## 전자결재 시스템 SAML 오류 사례

### 흐름
```
1. 사내시스템 데이터 작성
2. 전자결재 버튼 클릭
3. SAML 세션 인증 ✅
4. 전자결재 API 호출
5. API에서 XML 생성 ❌ 오류
```

### 원인 분류

**세션 만료 시간 불일치**
- IdP 세션(2시간) vs SP 세션(30분) 불일치
- SP 세션 만료 후 재인증 타이밍에 요청 충돌
- 해결: 세션 시간 맞추기 또는 Silent Refresh

**SAML Assertion 만료**
- 문서 작성 중 Assertion 유효시간(NotOnOrAfter) 초과
- 해결: Assertion 유효시간 연장 또는 임시저장 → 세션갱신 → 최종제출

**클럭 스큐 (Clock Skew)**
- IdP/SP 서버 시간 차이로 유효한 Assertion을 만료로 판단
- 해결: NTP 시간 동기화 또는 clockSkew 허용치 설정

**XML 직렬화 버그**
- 결재선 1명일 때 단일 값 vs 배열 구조 불일치
- null/empty 필드 처리 미흡
- 해결: 단수/복수 처리 코드 확인

## 관련 페이지

- [[concepts/stateless-architecture]] — 세션 공유 저장소
- [[concepts/cache-strategies]] — 세션 캐싱 전략
- [[projects/study-system-design-interview]] — 시스템 설계 스터디
