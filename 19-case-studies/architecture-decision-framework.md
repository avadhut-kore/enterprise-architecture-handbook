# Enterprise Architecture Decision Framework & Pre-Mortem Guide

## 1. Purpose & Guiding Axioms
This framework operationalizes the hard-won forensic lessons from 48 enterprise failures into an actionable decision-making rubric. Enterprise Architects should apply this framework during initial design phases, major modernization initiatives, and Architectural Review Board (ARB) submissions to systematically identify and eliminate latent failure modes before writing code.

---

## 2. The 5 Architecture Pre-Mortem Inquiries

Before committing to any significant architectural design or migration, the architecture team must answer the following **5 Inquiries**:

```
                              [THE ARCHITECTURAL PRE-MORTEM]
                                            │
  ┌─────────────────┬───────────────────────┼───────────────────────┬─────────────────┐
  ▼                 ▼                       ▼                       ▼                 ▼
[INQUIRY 1]       [INQUIRY 2]             [INQUIRY 3]             [INQUIRY 4]       [INQUIRY 5]
Blast Radius      Network Reality         State & Transaction     Downstream Data   Governance &
Containment       Assumptions             Boundaries              Sizing Limits     Team Topologies
```

### Inquiry 1: Blast Radius & Cell Containment
- *Question*: If this component experiences a catastrophic out-of-memory crash or infinite loop, what is the maximum possible blast radius?
- *Failure Warning*: Can a single tenant, single misconfigured route, or single bad payload take down unrelated systems across the enterprise (`CS-CLOUD-02`, `CS-INT-05`, `CS-SCALE-02`)?
- *Mandatory Guardrail*: Partition workloads into isolated **Cells / Availability Zones**. Ensure control planes are decoupled regionally.

### Inquiry 2: Network Reality & Fallacies of Distributed Computing
- *Question*: Does the design assume the network is reliable, latency is zero, or bandwidth is infinite?
- *Failure Warning*: Are we chaining more than 3 synchronous HTTP/REST calls in a user request path (`CS-MOD-01`)? Are we executing dual writes without CDC (`CS-INT-01`)? Are we missing exponential backoff and jitter on retries (`CS-INT-03`)?
- *Mandatory Guardrail*: Enforce asynchronous event streaming for all non-essential side-effects. Mandate Circuit Breakers on all egress boundaries.

### Inquiry 3: State & Transactional Boundaries
- *Question*: How does the system maintain state consistency across multiple databases or microservices?
- *Failure Warning*: Are we attempting Distributed Two-Phase Commit / XA transactions (`CS-INT-04`) or active-active multi-region writes with Last-Write-Wins (`CS-SCALE-06`)?
- *Mandatory Guardrail*: Adopt the **Saga Pattern** with compensating transactions. Enforce **Single-Home Geographic Partitioning** for mutable state.

### Inquiry 4: Downstream Data & Connection Sizing Limits
- *Question*: If the frontend tier scales to 10x peak traffic, what happens to the database?
- *Failure Warning*: Can autoscaled pods open 100,000 direct database connections (`CS-SCALE-03`)? Are we writing to a single DynamoDB partition key (`CS-SCALE-01`)? Does an endpoint execute ORM N+1 queries (`CS-PERF-01`)?
- *Mandatory Guardrail*: Deploy connection multiplexing (PgBouncer / RDS Proxy). Enforce automated query count budgets in CI/CD.

### Inquiry 5: Governance & Team Topologies Alignment
- *Question*: Does the software architecture align with team boundaries, or does it require continuous cross-squad coordination?
- *Failure Warning*: Are 20 squads committing to a shared database (`CS-MOD-02`)? Are we attempting a multi-year big-bang rewrite (`CS-MOD-03`)? Is the ARB acting as a waterfall bottleneck (`CS-ENT-06`)?
- *Mandatory Guardrail*: Enforce strict compile-time bounded contexts (Packwerk / ArchUnit). Ban big-bang rewrites; mandate 90-day Strangler Fig production milestones.

---

## 3. Architecture Decision Matrix (Trade-Off Rubric)

| Architecture Dilemma | Anti-Pattern Choice (High Failure Risk) | Resilient Architectural Standard | Key Trade-Off Accepted |
| :--- | :--- | :--- | :--- |
| **Multi-Service Data Consistency** | Distributed 2PC (XA) / Dual-Writes | Transactional Outbox + Eventual Consistency Saga | Accepts temporary latency in cross-domain consistency in exchange for 99.999% system availability. |
| **Monolith Modernization** | Big-Bang Ground-Up Rewrite ("Project Phoenix") | Modular Monolith or Strangler Fig Pattern | Sacrifices the illusion of a "clean slate" in exchange for continuous working software and zero business-freeze risk. |
| **Public Multi-Tenant Isolation** | Logical `WHERE tenant_id = ?` in application code | Database-level Row-Level Security (PostgreSQL RLS) | Incurs minor database query parsing overhead in exchange for mathematical immunity against cross-tenant leaks. |
| **High-Throughput Ingestion** | Dynamic Reflection JSON over HTTP REST | Protocol Buffers / Avro over gRPC or Kafka | Sacrifices human-readable text payloads in exchange for 90% compute and bandwidth cost reductions. |
| **Global Multi-Region Deployment** | Multi-Master Active-Active with LWW Conflict Resolution | Single-Home Geographic Partitioning | Sacrifices multi-region write failover transparency in exchange for zero split-brain data corruption. |
| **Enterprise Edge Routing** | Custom in-house Java/Node.js reverse proxy | Battle-tested C/C++ Envoy Proxy with CDN Fallback | Sacrifices custom application code in the proxy in exchange for rock-solid memory management and sub-millisecond p99 routing. |
