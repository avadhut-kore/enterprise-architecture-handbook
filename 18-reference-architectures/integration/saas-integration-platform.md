# Reference Architecture: SaaS Integration Platform Reference Architecture

## 1. Architectural Vision & Context
Centralized SaaS integration hub: OAuth token lifecycle management, sliding-window rate limiters, webhook ingestion receivers, and tenant isolation.

---

## 2. Architecture Topology Blueprint

```mermaid
flowchart LR
    Client[External Client / Partner] --> Gateway[Edge API Gateway / APIM]
    Gateway --> BFF[Backend-for-Frontend / Experience API]
    BFF --> Process[Process Orchestration API]
    Process --> SystemAPI[System APIs / Legacy Adapters]
    Process -->|Async Events| EventBus[(Enterprise Event Bus: Kafka)]
    EventBus --> AsyncWorker[Asynchronous Integration Workers]
```

---

## 3. Core Architectural Invariants & Governance
- External traffic must terminate at governed edge gateways with rate limiting and authentication.
- Distributed trace contexts must propagate across both synchronous RPC calls and asynchronous event headers.
- Service integrations must be protected by explicit circuit breakers and timeouts.
