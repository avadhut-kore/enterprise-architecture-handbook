# Contract Testing: REST & HTTP API Contract Testing

## 1. Architectural Purpose & Problem Context
Verifying HTTP status codes, headers, query parameters, and JSON payloads across service boundaries.

---

## 2. Structural Workflow & Broker Topology

```mermaid
sequenceDiagram
    autonumber
    participant Consumer as Consumer CI
    participant Broker as Central Pact Broker
    participant Provider as Provider CI

    Consumer->>Consumer: Run Unit Tests & Generate Pact File
    Consumer->>Broker: Publish Contract (v1.2.0)
    Provider->>Broker: Fetch Latest Consumer Contracts
    Provider->>Provider: Replay Requests against Provider Controller
    Provider->>Broker: Publish Verification Result (Success/Fail)
    Consumer->>Broker: can-i-deploy --to prod?
    Broker-->>Consumer: Approved (Green Gate)
```

---

## 3. Production Invariants
- Enforce the **Tolerant Reader Pattern**: Consumers should only validate fields they explicitly consume, ignoring unexpected fields.
- Never deploy a breaking schema change without verifying all consumer contracts via the Pact Broker.
