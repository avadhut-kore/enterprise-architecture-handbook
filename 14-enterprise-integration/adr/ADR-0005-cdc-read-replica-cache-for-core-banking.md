# ADR-0005: Decoupling Core Banking Balance Queries via CDC and Redis Read Caches

---
**Metadata**:
* **ADR ID**: ADR-0005
* **Title**: Decoupling Core Banking Balance Queries via CDC and Redis Read Caches
* **Status**: Accepted
* **Date**: 2026-09-05
* **Decision Owners**: Enterprise Architecture Review Board (ARB)
* **Decision Reviewers**: Chief Architect, Security Architect, Lead Integration Architect
* **Related Requirements**: [NFR-SEC-01, NFR-REL-04, NFR-PERF-02]
* **Related ADRs**: None
* **Review Date**: 2027-09-05
---

## 1. Context & Problem Statement
Mainframe MIPS costs escalating due to millions of daily mobile banking balance inquiries.

## 2. Business Drivers
* Accelerate time-to-market for digital products and partner integrations.
* Reduce operational expenditure, licensing fees, and compliance audit scope.
* Guarantee 99.999% platform availability across mission-critical customer workflows.

## 3. Technical Drivers
* Elimination of point-to-point spaghetti architecture.
* Sub-millisecond latency overhead and horizontal scalability.
* Strict fault isolation preventing cascading failures across service boundaries.

## 4. Constraints & Assumptions
* All solutions must run in containerized Kubernetes or managed multi-cloud environments.
* External partner interfaces must remain strictly backward-compatible.

## 5. Options Considered
* **Option 1**: Legacy synchronous point-to-point RPC / Two-Phase Commit.
* **Option 2**: Monolithic Centralized Enterprise Service Bus (ESB).
* **Option 3 (Selected)**: Log-Based CDC (Debezium) streaming to Redis Read Cache.

## 6. Decision Outcome
* **Selected Option**: Log-Based CDC (Debezium) streaming to Redis Read Cache.
* **Architectural Justification**: Offloads 98% of read queries from the mainframe, preserving MIPS and eliminating latency spikes.

## 7. Architecture Blueprint
```
[Client Tier] ──> [API Gateway / Facade] ──> [Log-Based CDC (Debezium) streaming to Redis Read Cache] ──> [Enterprise Systems of Record]
```

## 8. Consequences & Impact
* **Positive**: High decoupling, zero dual-write divergence, strict compliance adherence.
* **Negative**: Requires operational training, schema governance tooling, and out-of-band monitoring.

## 9. Validation & Compliance Criteria
* 100% of production traffic verified against this standard in automated CI/CD pipeline tests.
