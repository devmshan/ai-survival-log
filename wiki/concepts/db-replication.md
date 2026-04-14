---
title: "데이터베이스 다중화 (DB Replication)"
created: "2026-04-14"
updated: "2026-04-14"
type: concept
sources: ["[[sources/2026-04-14-system-design-interview-v1]]"]
tags: ["system-design", "database", "replication", "high-availability", "distributed-systems"]
status: active
published: false
slug: ""
description: ""
---

# 데이터베이스 다중화 (DB Replication)

데이터베이스를 여러 서버에 복제하여 가용성(availability)과 성능을 높이는 전략.

## 주/부(Master/Slave) 복제 구조

```
쓰기 연산(INSERT/UPDATE/DELETE) → 주 DB (Master)
                                      ↓ 복제
읽기 연산(SELECT)               → 부 DB (Slave) 1
                                → 부 DB (Slave) 2
                                → 부 DB (Slave) N
```

- **주(Master) DB:** 데이터 변경(쓰기) 연산만 처리
- **부(Slave) DB:** 주 DB 데이터를 복사해 읽기 연산만 처리
- 일반적으로 읽기 연산이 훨씬 많으므로 부 DB를 더 많이 둠

## 장점

- **성능 향상:** 읽기 쿼리를 여러 부 DB에 분산 → 병렬 처리
- **안정성:** 데이터를 여러 서버에 저장 → 자연재해 등 데이터 유실 방지
- **가용성(High Availability):** 한 DB 서버가 다운되어도 다른 서버로 운영 가능

## 장애 시나리오

### 부 DB 1개, 다운된 경우
1. 읽기 연산이 일시적으로 주 DB로 전달
2. 새로운 부 DB 서버 생성
3. (부 DB가 여러 개라면 나머지 부 DB에서 읽기 연산 분담)

### 주 DB 다운된 경우
1. 부 DB 중 하나가 새로운 주 DB로 승격(promotion)
2. 새로운 주 DB 선출 이후 새로운 부 DB 추가
3. **문제점:** 부 DB의 데이터가 최신이 아닐 수 있음 (복제 지연)
   - 복구 스크립트로 누락 데이터를 추가해야 할 수 있음
   - 다중 주(Multi-master) 복제로 해결 가능

## 동기화 방식

**동기식 (Synchronous)**
```
클라이언트 → 주 DB 쓰기
              → 부 DB 동기화 완료 확인
              → 완료 응답
```
- 주/부 DB 항상 일치 보장
- 부 DB 응답 올 때까지 대기 → 느림
- 부 DB 하나라도 죽으면 쓰기 블로킹

**비동기식 (Asynchronous) — 대부분 이 방식**
```
클라이언트 → 주 DB 쓰기 → 즉시 응답
              → 부 DB에 나중에 전파 (백그라운드)
```
- 빠름, 전파 전 주 DB 죽으면 데이터 유실 가능

## 전파 메커니즘 — 바이너리 로그 (binlog)

변경된 모든 쿼리를 시간순으로 append하는 로그 파일.

```sql
-- 이런 쿼리 실행 시
UPDATE users SET name = '민성' WHERE id = 1;
```
```
# binlog 기록
Timestamp: 2026-04-14 17:00:00
Query: UPDATE users SET name = '민성' WHERE id = 1
```

**부 DB 동기화 흐름:**
```
주 DB → 쿼리 실행 → binlog 기록
         ↓
부 DB IO Thread → binlog 구독 → Relay Log에 복사
         ↓
부 DB SQL Thread → Relay Log 읽어서 쿼리 재실행
         ↓
부 DB 데이터 반영
```

부 DB는 주 DB의 쿼리를 **그대로 다시 실행**하는 방식. MySQL, PostgreSQL 모두 이 방식 사용.

## 동기화 방식 상세

| | 비동기 | Semi-Sync | 완전 동기 |
|--|--------|-----------|---------|
| 속도 | 빠름 | 중간 | 느림 |
| 유실 위험 | 있음 | 거의 없음 | 없음 |
| 주 DB 장애 시 | 일부 유실 가능 | 최소 1개 부 DB에 보존 | 완전 보존 |

Semi-Sync: 부 DB가 binlog **받은 것**만 ack (처리 완료 아님). 완전 동기보다 빠르면서 유실 방지.

## 쿼리 라우팅

읽기는 부 DB로, 쓰기는 주 DB로 분기.

**방법 1 — 애플리케이션 코드 (Spring)**
```java
@Transactional(readOnly = true)   // 부 DB
public List<User> getUsers() { ... }

@Transactional                    // 주 DB
public User createUser(User user) { ... }
```

**방법 2 — ProxySQL (미들웨어)**
```
애플리케이션 → ProxySQL → 주 DB (INSERT/UPDATE/DELETE 자동)
                        → 부 DB (SELECT 자동)
```

애플리케이션 입장에서 DB가 하나인 것처럼 연결. 코드 변경 없이 라우팅.

ProxySQL 추가 기능:
- 커넥션 풀링 (서버 100대 → DB 커넥션 10개로 충분)
- 장애 감지 (부 DB 죽으면 자동으로 다른 부 DB로 전환)

| | 코드 레벨 | ProxySQL |
|--|---------|---------|
| 제어 세밀도 | 높음 | 중간 |
| 코드 변경 | 필요 | 불필요 |
| 적합한 경우 | 소규모 | 대규모 |

## 복제 지연 (Replication Lag)

주 DB에서 부 DB로 복제하는 데 시간이 걸림 → 읽기 직후 쓰기 결과가 안 보이는 현상.
- 일관성(Consistency) vs 가용성(Availability) 트레이드오프
- CAP 정리와 관련

## Read-Your-Writes

**문제:**
```
유저 닉네임 변경 → 주 DB 업데이트 ✅
0.05초 후 프로필 조회 → 부 DB에서 읽음 → 아직 구버전 ❌
```

**해결 방법:**

```java
// 방법 1: 쓰기 직후 같은 트랜잭션에서 읽기 → 주 DB 사용
@Transactional
public User updateAndReturn(Long id, String nickname) {
    userRepository.save(user);           // 주 DB 쓰기
    return userRepository.findById(id);  // 같은 트랜잭션 → 주 DB 읽기
}

// 방법 2: 세션에 "방금 썼음" 플래그
// last_write_at이 최근이면 → 주 DB, 충분히 지났으면 → 부 DB
```

**어떤 경우 중요한가:**
```
중요: SNS 프로필 수정 후 즉시 조회, 주문 완료 후 주문 내역 확인
덜 중요: 다른 유저 게시물 조회, 상품 목록, 통계 대시보드
```

## 관련 페이지

- [[concepts/load-balancer]] — 웹 계층 다중화
- [[concepts/database-sharding]] — DB 수평 확장
- [[concepts/cache-strategies]] — DB 부하 감소를 위한 캐시
- [[projects/study-system-design-interview]] — 시스템 설계 스터디
