# Reference Architecture: Multi-Year Hybrid Coexistence Architecture

## 1. Architectural Vision & Context
Operating legacy on-premises core systems concurrently with modern cloud services for 3 to 5 years.

---

## 2. Current State vs. Target State Blueprint

```
CURRENT STATE: Monolithic Tightly Coupled Architecture
[Legacy Clients] ──► [Monolithic System / SOAP / Batch] ──► [Monolithic Shared Database]

TARGET STATE: Modernized Architecture
[Modern Clients] ──► [API Gateway / Facade]
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
     [Domain Service A]          [Domain Service B]
             │                           │
             ▼                           ▼
       [Database A]                [Database B]
             │                           │
             └───────────► [Event Mesh] ◄┘
```

---

## 3. Transition Architecture & Migration Sequence
1. **Foundation Phase**: Establish networking, landing zone, security baselines, and ingress facades.
2. **Data Hydration Phase**: Replicate database tables asynchronously using Change Data Capture (CDC).
3. **Shadow Traffic Phase**: Verify query equivalence under live production load without customer side effects.
4. **Canary Cutover Phase**: Shift 1% $\rightarrow$ 10% $\rightarrow$ 100% of traffic using weighted routing.
5. **Decommissioning Phase**: Isolate and prune legacy code and database tables.

---

## 4. Key Architectural Building Blocks
Bidirectional CDC synchronization, automated daily reconciliation engines, mTLS transit encryption, unified observability.

## 5. Cross-References
- Diagrams: Refer to [17-diagrams/examples/core-banking.md](../../17-diagrams/examples/core-banking.md) and [17-diagrams/sequence/saga.md](../../17-diagrams/sequence/saga.md).
- Integration: Refer to [14-enterprise-integration/README.md](../../14-enterprise-integration/README.md).
