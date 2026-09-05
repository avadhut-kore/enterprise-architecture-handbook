# Enterprise Integration Strategy: API-Led & Event-Driven

Modern enterprise integration combines API-led connectivity for synchronous request-response with Event-Driven Architecture (EDA) for asynchronous real-time scalability.

---

## 1. The 3-Tier API-Led Connectivity Model

```mermaid
graph TD
    subgraph Experience APIs (Channel-Specific)
        E1["Mobile Banking BFF"]
        E2["Partner Open Banking API"]
        E3["Internal Web Admin API"]
    end
    subgraph Process APIs (Business Logic & Orchestration)
        P1["Loan Origination Process API"]
        P2["Payment Settlement Orchestrator"]
    end
    subgraph System APIs (Raw Data & Encapsulation)
        S1["Core Banking System API"]
        S2["Salesforce CRM System API"]
        S3["Credit Bureau Gateway API"]
    end
    E1 --> P1
    E2 --> P2
    P1 --> S1
    P1 --> S3
    P2 --> S1
```

* **System APIs**: Isolate legacy systems of record behind standard REST/gRPC interfaces. Prevents core systems from being exposed directly to front-end changes.
* **Process APIs**: Combine multiple system APIs into reusable business workflows.
* **Experience APIs**: Tailor data payloads to specific client devices and network constraints.
