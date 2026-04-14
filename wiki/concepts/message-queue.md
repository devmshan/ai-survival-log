---
title: "메시지 큐 (Message Queue)"
created: "2026-04-14"
updated: "2026-04-14"
type: concept
sources: ["[[sources/2026-04-14-system-design-interview-v1]]"]
tags: ["system-design", "message-queue", "async", "decoupling", "distributed-systems"]
status: active
published: false
slug: ""
description: ""
---

# 메시지 큐 (Message Queue)

비동기 통신을 지원하고 컴포넌트 간 결합도를 낮추는 내구성 있는 컴포넌트.

## 기본 구조

```
생산자(Producer) → 메시지 큐 → 소비자(Consumer)
```

- **생산자(Publisher):** 메시지를 만들어 큐에 발행
- **메시지 큐:** 메시지를 보관하는 버퍼
- **소비자(Subscriber/Worker):** 큐에서 메시지를 꺼내 처리

## 핵심 특성

### 비동기(Asynchronous)
- 생산자는 소비자가 처리 완료될 때까지 기다리지 않음
- 생산자는 메시지를 큐에 넣고 바로 다음 작업으로 이동

### 독립적 규모 확장
- 생산자와 소비자가 **독립적으로 규모 조절** 가능
- 소비자 처리 속도가 느리면 소비자만 더 추가
- 생산 속도가 빠르면 생산자만 더 추가

### 내구성 (Durability)
- 소비자 프로세스가 죽어도 메시지는 큐에 보존
- 소비자가 복구되면 이어서 처리 가능
- 메시지 유실 방지

## 실제 활용 예시

### 사진 보정 앱
```
1. 사용자가 사진 업로드 → 생산자가 큐에 "보정 작업" 메시지 발행
2. 소비자가 큐에서 메시지 꺼냄 → 비동기로 보정 처리
3. 보정 완료 후 결과 저장
```

사용자는 보정 완료를 기다리지 않고 다른 작업 가능.

### 이메일 발송
- 주문 완료 이벤트 → 큐에 발행
- 이메일 발송 서비스가 큐에서 꺼내 발송 (실패 시 재시도 가능)

### 로그 처리
- 여러 서버에서 로그 생성 → 큐에 발행
- 로그 집계 서비스가 일괄 처리

## 소비자(Consumer)란

큐에서 메시지를 꺼내 처리하는 서버 또는 프로세스.

```
생산자 (앞단, 유저 요청 받음) → [메시지 큐] → 소비자 (뒤단, 실제 처리)
```

실제 사례:
- 유튜브: 웹 서버(생산자) → 인코딩 서버(소비자)
- 쇼핑몰: 주문 API(생산자) → 결제/재고/배송 서버(소비자)
- 전자결재: 사내시스템(생산자) → 전자결재 서버(소비자)

## 경쟁 소비자 패턴 (Competing Consumers)

소비자를 여러 개 띄워 병렬 처리.

```
[메시지 큐]
  작업1 → 소비자 1 (처리 중)
  작업2 → 소비자 2 (처리 중)
  작업3 → 소비자 3 (처리 중)
  작업4 → 대기 (소비자 끝나면 가져감)
```

트래픽 폭발 시 소비자만 늘리면 됨. 생산자는 신경 안 써도 됨.

## Java 예시 (RabbitMQ)

```java
// 생산자
channel.basicPublish("", QUEUE_NAME,
    MessageProperties.PERSISTENT_TEXT_PLAIN,
    "resize_image:user123:profile.jpg".getBytes());
// 큐에 넣고 즉시 리턴 → 소비자 기다리지 않음

// 소비자
channel.basicQos(1);  // 한 번에 1개만 처리 (과부하 방지)

DeliverCallback callback = (tag, delivery) -> {
    processTask(new String(delivery.getBody()));
    channel.basicAck(delivery.getEnvelope().getDeliveryTag(), false);
    // ack 보내야 큐에서 삭제됨
    // 소비자 죽으면 ack 없음 → 큐가 삭제 안 함 → 다른 소비자가 재처리
};
```

## ack / nack 상세

**ack — 처리 성공**
```java
channel.basicAck(deliveryTag, false);
// 큐 → 해당 메시지 삭제
```

**nack — 처리 실패**
```java
channel.basicNack(deliveryTag, false, true);  // requeue=true → 큐에 다시 넣음
channel.basicNack(deliveryTag, false, false); // requeue=false → 버림 (DLQ로)
```

**소비자가 죽으면:**
```
소비자 → 메시지 받음 → 처리 중 → 죽음 (ack 못 보냄)
큐 → ack 안 옴 → 다른 소비자에게 자동 재전달
```

**Dead Letter Queue (DLQ)**
```
처리 실패 반복 → DLQ로 이동 → 개발자가 나중에 원인 분석 + 수동 재처리
```
전자결재처럼 유실이 치명적인 시스템에서 중요.

## TCP ack vs 메시지 큐 ack

| | TCP ack | 메시지 큐 ack |
|--|---------|-------------|
| 계층 | 전송 계층 | 애플리케이션 계층 |
| 의미 | 패킷 **수신** 확인 | 메시지 **처리** 완료 확인 |
| 동작 | 자동 (OS가 처리) | 수동 (개발자가 코드로 호출) |
| 실패 시 | 재전송 | 재전달 |

> 계층만 다를 뿐 "확인 응답으로 유실 방지" 철학은 동일

## 느슨한 결합 (Loose Coupling)

메시지 큐의 가장 큰 장점:

```
강한 결합:  서버A → 서버B (B가 죽으면 A도 영향받음)
느슨한 결합: 서버A → 큐 → 서버B (B가 죽어도 A는 계속 작동)
```

서비스 간 직접 통신을 제거해 독립성 보장.

## 대표 솔루션

- **RabbitMQ:** 범용 메시지 브로커
- **Apache Kafka:** 고처리량 분산 스트리밍 플랫폼
- **Amazon SQS:** 관리형 메시지 큐 서비스
- **Google Pub/Sub:** GCP 메시지 큐

## 관련 페이지

- [[concepts/stateless-architecture]] — 무상태 설계와 함께 사용
- [[concepts/vertical-vs-horizontal-scaling]] — 독립적 규모 확장
- [[projects/study-system-design-interview]] — 시스템 설계 스터디
