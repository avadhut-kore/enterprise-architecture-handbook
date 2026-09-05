# Poison Pills & Malformed Messages

## 1. Problem Definition

A Poison Pill is a message, event, or database record that causes any consumer or worker thread attempting to process it to crash, throw unhandled exceptions, or loop infinitely.

---

## 2. The Poison Pill Loop

```
Queue ──► Worker 1 reads Poison Pill ──► Crashes (Unacknowledged)
  ▲                                            │
  │                                            ▼
Message returns to Queue ◄────────── Redelivery timeout
  │
  ▼
Worker 2 reads Poison Pill ──► Crashes
  │
  ▼
Entire worker fleet crashes in rapid succession
```

---

## 3. Engineering Mitigations

### A. Dead-Letter Queues (DLQ) with Retry Thresholds
- Track redelivery attempt counters in message metadata headers (`X-Delivery-Count`).
- If a message fails processing $> 3$ times, the worker catches the error, acknowledges the message off the primary queue, and routes it to a **Dead-Letter Queue (DLQ)**.
- Primary queue traffic continues processing without interruption.

### B. Schema Validation at Ingress
Validate all payloads against strict schemas (JSON Schema, Protobuf, Avro) at the API Gateway or producer boundary. Malformed payloads are rejected immediately with HTTP 400 Bad Request before ever reaching internal event brokers.
