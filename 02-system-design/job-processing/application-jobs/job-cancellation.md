# Background Processing: Job Cancellation & Cooperative Shutdown

## 1. Architectural Purpose & Problem Context
Propagating cancellation tokens on SIGTERM to allow active jobs to finish cleanly.

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
