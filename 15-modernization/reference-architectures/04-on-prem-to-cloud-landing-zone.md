# Reference Architecture: On-Premises to Cloud Landing Zone Architecture

## 1. Architectural Vision & Context
Migrating an enterprise portfolio to public cloud with multi-account governance and zero-trust security.

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
Transit Gateway, Direct Connect redundant 10 Gbps, AWS Organizations SCPs, centralized egress NAT, Terraform landing zone.

## 5. Cross-References
- Diagrams: Refer to [17-diagrams/examples/core-banking.md](../../17-diagrams/examples/core-banking.md) and [17-diagrams/sequence/saga.md](../../17-diagrams/sequence/saga.md).
- Integration: Refer to [14-enterprise-integration/README.md](../../14-enterprise-integration/README.md).
