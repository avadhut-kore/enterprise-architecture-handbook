# Infrastructure & High-Availability: ERP Platform

## 1. Zero-Data-Loss High Availability
- In-memory database nodes run in synchronous active-passive replication across availability zones.
- Storage volumes utilize synchronous block replication with guaranteed RPO = 0.

## 2. Production Deployment & GitOps Automation
- **GitOps Reconciliation**: Declarative infrastructure managed via ArgoCD / Flux synchronizing Kubernetes manifests from source control.
- **Multi-AZ High Availability**: Workloads spread across 3 Availability Zones with PodDisruptionBudgets (`minAvailable: 2`).
- **Canary Deployments**: Automated canary rollouts (Argo Rollouts / Flagger) analyzing error rates and p99 latency before 100% traffic shift.
