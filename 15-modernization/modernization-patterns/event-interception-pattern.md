# Event Interception Pattern

## 1. Problem & Context
Modern event-driven platforms need real-time updates from legacy systems that only support direct database writes.

## 2. Forces & Trade-Offs
- **Delivery Velocity vs. Stability**: How quickly the business needs the new capability vs. the risk of breaking existing behavior.
- **Data Consistency vs. Decoupling**: Maintaining ACID guarantees across systems vs. embracing eventual consistency.

## 3. Solution Architecture
Intercept database commits via transaction log scraping (CDC) or trigger events, publishing CloudEvents to Kafka.

```
[Inbound Request] ──► [Routing Boundary / Facade]
                              │
               ┌──────────────┴──────────────┐
               ▼                             ▼
       [Legacy Component]            [Modern Component]
               │                             │
               └──────────────┬──────────────┘
                              ▼
                   [Output Parity / State]
```

## 4. Implementation Steps
1. Establish baseline characterization tests capturing existing legacy behavior.
2. Introduce the abstraction layer or routing facade at the boundary.
3. Deploy the modern implementation in parallel.
4. Verify behavioral equivalence under production load.
5. Decommission the legacy pathway.

## 5. When NOT to Use
When database log access is prohibited by hosting vendors.
