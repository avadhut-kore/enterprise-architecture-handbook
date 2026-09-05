# HLD-ORD-001: E-Commerce Real-Time Checkout Service

---
**Metadata**:
* **Document ID**: HLD-ORD-001
* **Title**: High-Level Design — E-Commerce Real-Time Checkout Service
* **Version**: 1.0.0
* **Status**: Approved
* **Owner**: Alex Chen <alex.chen@enterprise.com> (Lead Technical Architect)
* **Parent SAD**: [SAD-PAY-001](../../02-sad/examples/global-payments-platform-sad.md)
---

## 1. Subsystem Scope & Overview
The Checkout Service manages customer checkout sessions, shopping cart conversions, payment authorization coordination, and order aggregate creation. Peak design throughput is 6,000 checkout submissions per minute with a p95 response time under 300ms.

## 2. Component Architecture
* **API Controller**: Java 21 / Spring Boot 3 handling HTTPS POST `/checkout` with RFC 7807 error responses.
* **Idempotency Filter**: Redis-backed distributed lock checking `Idempotency-Key` header.
* **Checkout Orchestrator**: Executes domain validation (coupon application, tax calculation, stock hold).
* **Transactional Outbox Worker**: Background processor reading pending events from PostgreSQL and publishing to Kafka.

## 3. Storage Design
* **Primary DB**: Amazon Aurora PostgreSQL (db.r6g.2xlarge).
* **Caching**: Amazon ElastiCache Redis Cluster for idempotency tokens and session caches.

## 4. Failure Handling
* Payment gateway calls capped at 1,500ms timeout with Resilience4j circuit breakers.
* If inventory reservation fails, state transitions to `FAILED_OUT_OF_STOCK` and order is cleanly rejected.
