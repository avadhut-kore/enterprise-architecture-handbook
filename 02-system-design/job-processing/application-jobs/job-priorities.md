# Background Processing: Job Prioritization & Multiple Queues

## 1. Architectural Purpose & Problem Context
Dedicated worker queues for high-priority user transactions vs low-priority bulk reports.

---

## 2. Structural Task Queue Pattern

```mermaid
flowchart LR
    API[Web API Request] -->|Enqueue Task Payload| Queue[(Persistent Task Queue: Redis / SQL)]
    API -->> Client[Return 202 Accepted]
    Queue --> Worker[Background Worker Daemon]
    Worker -->|Execute Task & Update Status| DB[(Job Metadata DB)]
```

---

## 3. Production Invariants
- Background jobs must be completely idempotent.
- Never use volatile in-memory queues (e.g., standard C# Channels or Java queues) for critical business operations; persist jobs in Redis or Postgres so jobs survive container restarts.
