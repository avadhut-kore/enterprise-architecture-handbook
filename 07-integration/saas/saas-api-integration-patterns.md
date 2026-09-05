# SaaS Integration: SaaS API Integration Patterns & Topologies

## 1. Architectural Purpose & Problem Context
Polling vs webhooks, bulk export APIs, delta synchronization, and managing vendor API maintenance windows across Salesforce, Workday, etc.

---

## 2. Resilient SaaS Integration Topology

```mermaid
flowchart LR
    App[Enterprise Service] --> Queue[Asynchronous Integration Queue]
    Queue --> Worker[SaaS Client Worker]
    Worker --> Breaker[Circuit Breaker & Rate Limiter]
    Breaker -->|HTTPS / OAuth2| SaaS[Third-Party SaaS Provider API]
    Breaker -.->|Vendor 429 / Outage| Backoff[Exponential Backoff Queue]
```

---

## 3. Production Invariants
- Never invoke external SaaS APIs synchronously within the critical customer checkout or transaction path.
- Cache external OAuth access tokens securely in memory until expiration minus a 5-minute safety threshold.
