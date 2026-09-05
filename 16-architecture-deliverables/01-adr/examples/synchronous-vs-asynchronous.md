# ADR-0004: Asynchronous Event Choreography vs Synchronous REST

---
**Metadata**:
* **ADR ID**: ADR-0004
* **Title**: Inter-Service Communication — Asynchronous Event Choreography
* **Status**: Accepted
* **Date**: 2026-02-18
* **Decision Owners**: Principal Architect, Systems Engineering Lead
---

## 1. Context & Problem Statement
When an enterprise customer submits an order, five subsystems must act: Inventory Reservation, Payment Capture, Fraud Scoring, Notification Dispatch, and ERP Ledger Posting. Synchronous chained REST calls create tight temporal coupling, cascading latency, and fragile failure domains.

## 2. Decision & Rationale
Adopt **Asynchronous Event Choreography** via Kafka for order processing.
The Order Service immediately persists the order in `PENDING` state and emits an `OrderPlacedEvent`. Downstream consumers process the event asynchronously. If a non-critical downstream service (e.g., Notification Dispatch) experiences downtime, the core order transaction completes uninterrupted.

## 3. Consequences & Trade-offs
* User interfaces must embrace eventual consistency (polling, WebSockets, or Server-Sent Events to show status).
* Distributed tracing with W3C TraceContext correlation IDs is mandatory across all producers and consumers.
