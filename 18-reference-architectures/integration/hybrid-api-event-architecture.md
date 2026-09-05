# Reference Architecture: Hybrid Synchronous API & Asynchronous Event Architecture

## 1. Architectural Vision & Context
Harmonizing synchronous REST/gRPC queries for user-facing reads with asynchronous event pub/sub for transactional side-effects and inter-service mutations.

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
