# ADR-0048: Adoption of Amazon EKS with Karpenter Node Autoscaling

## Metadata
```yaml
id: ADR-0048
title: Adoption of Amazon EKS with Karpenter Node Autoscaling
status: accepted
decision_type: architectural
scope: enterprise-cloud-infrastructure
owners: enterprise-architecture-board
date: 2026-09-05
review_cadence: annual
```

---

## 1. Context & Problem Statement
Existing Kubernetes clusters suffered from slow cluster autoscaling (3–5 minutes) and resource fragmentation using legacy Auto Scaling Groups.

---

## 2. Decision
We mandate Amazon EKS paired with Karpenter for high-speed, dynamic node provisioning and automated instance consolidation.

---

## 3. Positive Consequences
- Reduces node provisioning latency from minutes to sub-45 seconds.
- Automatically mixes Graviton ARM64, Spot, and On-Demand instances to optimize cost.
- Eliminates the maintenance of hundreds of static Auto Scaling Groups.

---

## 4. Negative Consequences & Trade-offs
- Requires Karpenter controller lifecycle management and fine-grained EC2 fleet IAM permissions.

---

## 5. Alternatives Considered & Rejected
- **Legacy Cluster Autoscaler**: Rejected due to rigid node group boundaries and sluggish scaling.
