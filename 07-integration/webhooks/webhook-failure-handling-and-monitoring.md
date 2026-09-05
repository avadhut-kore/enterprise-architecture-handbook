# Webhook Architecture: Webhook Failure Handling, DLQ & Monitoring

## 1. Architectural Purpose & Problem Context
Automated subscriber disablement after consecutive 5xx errors, subscriber self-service failure dashboards, and manual event resend APIs.

---

## 2. Webhook Outbound Pipeline

```mermaid
sequenceDiagram
    autonumber
    participant EventSource as Internal Domain Service
    participant Queue as Webhook Task Queue
    participant Dispatcher as Dispatch Worker
    participant Subscriber as External Partner Server

    EventSource->>Queue: Enqueue Webhook Event Payload
    Dispatcher->>Queue: Pull Webhook Task
    Note over Dispatcher: Compute HMAC-SHA256 Signature
    Dispatcher->>Subscriber: HTTP POST /webhook (Payload + X-Signature)
    alt Subscriber Returns 200 OK
        Subscriber-->>Dispatcher: 200 OK
        Dispatcher->>Queue: Mark Complete
    else Subscriber Times Out / 5xx
        Note over Dispatcher: Schedule Exponential Retry
        Dispatcher->>Queue: Re-enqueue with Backoff Delay
    end
```

---

## 3. Production Invariants
- All webhook payloads must be signed using HMAC-SHA256 with tenant-specific shared secrets.
- Webhook endpoints must never perform heavy processing synchronously; consumers must validate, enqueue, and return 200 OK immediately.
