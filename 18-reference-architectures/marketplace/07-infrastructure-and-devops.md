# Infrastructure & Search Scalability: Marketplace

## 1. OpenSearch High-Volume Catalog Architecture
- Cluster topology: 3 master nodes, 6 data nodes, and dedicated ingestion coordinators.
- Real-time catalog updates stream via Kafka Connect directly to OpenSearch within 500ms of merchant price changes.

## 2. Production Deployment & GitOps Automation
- **GitOps Reconciliation**: Declarative infrastructure managed via ArgoCD / Flux synchronizing Kubernetes manifests from source control.
- **Multi-AZ High Availability**: Workloads spread across 3 Availability Zones with PodDisruptionBudgets (`minAvailable: 2`).
- **Canary Deployments**: Automated canary rollouts (Argo Rollouts / Flagger) analyzing error rates and p99 latency before 100% traffic shift.
