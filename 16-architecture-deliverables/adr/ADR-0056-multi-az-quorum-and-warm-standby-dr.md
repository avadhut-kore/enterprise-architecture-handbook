# ADR-0056: Multi-AZ Primary Deployment with Cross-Region Warm Standby DR

## Metadata
```yaml
id: ADR-0056
title: Multi-AZ Primary Deployment with Cross-Region Warm Standby DR
status: accepted
decision_type: architectural
scope: enterprise-cloud-infrastructure
owners: enterprise-architecture-board
date: 2026-09-05
review_cadence: annual
```

---

## 1. Context & Problem Statement
The enterprise required a standardized high-availability and disaster recovery architecture balancing sub-15 minute RTO against infrastructure budgets.

---

## 2. Decision
We mandate 3-AZ active-active deployment as the minimum standard for all production workloads, paired with cross-region Warm Standby (Aurora Global DB + Route 53 ARC) for Tier-1 systems.

---

## 3. Positive Consequences
- Delivers 99.99% intra-region availability.
- Guarantees sub-15 minute RTO and sub-second RPO during catastrophic regional disasters.
- Avoids the catastrophic complexity and cost of active-active multi-region.

---

## 4. Negative Consequences & Trade-offs
- Standby region incurs a 60% infrastructure cost premium over single-region.
- Requires quarterly failover drills to maintain operational readiness.

---

## 5. Alternatives Considered & Rejected
- **Single-AZ Deployment**: Rejected due to high downtime risk.
- **Active-Active Multi-Region (Bi-Directional Writes)**: Rejected due to distributed consensus latency and split-brain risks.
