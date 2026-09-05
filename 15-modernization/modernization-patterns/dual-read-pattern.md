# Dual-Read Pattern

## 1. Problem & Context
Validating that a migrated database returns identical query responses under production traffic.

## 2. Forces & Trade-Offs
- **Delivery Velocity vs. Stability**: How quickly the business needs the new capability vs. the risk of breaking existing behavior.
- **Data Consistency vs. Decoupling**: Maintaining ACID guarantees across systems vs. embracing eventual consistency.

## 3. Solution Architecture
Application reads primary DB and returns response; background thread reads candidate DB and alerts on divergence.

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
When database queries have destructive side effects (e.g., stored procedures mutating counters).
