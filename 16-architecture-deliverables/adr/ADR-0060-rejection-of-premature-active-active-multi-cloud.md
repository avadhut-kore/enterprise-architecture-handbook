# ADR-0060: Rejection of Active-Active Multi-Cloud for Transactional Workloads

## Metadata
```yaml
id: ADR-0060
title: Rejection of Active-Active Multi-Cloud for Transactional Workloads
status: accepted
decision_type: architectural
scope: enterprise-cloud-infrastructure
owners: enterprise-architecture-board
date: 2026-09-05
review_cadence: annual
```

---

## 1. Context & Problem Statement
Proposals were submitted to split transactional database traffic 50/50 across AWS and Azure simultaneously to eliminate cloud vendor lock-in.

---

## 2. Decision
We formally reject Active-Active Multi-Cloud for transactional, stateful systems as an enterprise anti-pattern. Stateful workloads will run in a single primary cloud with asynchronous cross-region or cross-cloud DR where legally mandated.

---

## 3. Positive Consequences
- Protects the enterprise from catastrophic WAN latency penalties (30ms+ RTT per commit).
- Prevents irreconcilable split-brain data corruption during cross-cloud network partitions.
- Eliminates millions of dollars in custom cross-cloud orchestration tooling.

---

## 4. Negative Consequences & Trade-offs
- Concentrates operational runtime within a single primary cloud provider (mitigated by asynchronous DR and container portability).

---

## 5. Alternatives Considered & Rejected
- **Active-Active Multi-Cloud across AWS and Azure**: Formally evaluated and rejected due to violation of CAP theorem latency constraints.
