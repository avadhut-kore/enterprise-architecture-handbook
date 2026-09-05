# Infrastructure & SRE: Fintech Platform

## 1. Active-Active Multi-Region Resiliency
- Deployed across two primary cloud regions using Google Cloud Spanner or CockroachDB with multi-region quorum consensus.
- Automatic transaction re-routing during cloud regional outages with zero data loss ($RPO = 0$).

## 2. Production Deployment & GitOps Automation
- **GitOps Reconciliation**: Declarative infrastructure managed via ArgoCD / Flux synchronizing Kubernetes manifests from source control.
- **Multi-AZ High Availability**: Workloads spread across 3 Availability Zones with PodDisruptionBudgets (`minAvailable: 2`).
- **Canary Deployments**: Automated canary rollouts (Argo Rollouts / Flagger) analyzing error rates and p99 latency before 100% traffic shift.
