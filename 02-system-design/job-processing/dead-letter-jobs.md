# Dead Letter Job Handling & Quarantine

## 1. Isolating Poison Tasks
When a background job exhausts its maximum configured retry attempts (e.g., 5 attempts), it is quarantined into a **Dead Letter Queue (DLQ)**.

```mermaid
flowchart LR
    Worker[Worker: Attempt 5 Fails] --> DLQ[(Dead Letter Queue / Quarantine)]
    DLQ --> Alert[SRE Slack / Pager Alert]
    DLQ --> UI[Admin Dashboard: Inspect Stack Trace & Payload]
    UI --> Replay[Manual Retry / Fix Code & Redrive]
```
