# Infrastructure & Kubernetes Tenant Isolation

## 1. Network Segmentation via Kubernetes NetworkPolicies
- Worker pods serving standard pooled tenants communicate over shared ingress.
- Enterprise silo tenants are deployed to dedicated node pools using Kubernetes taints and tolerations (`tenant=enterprise-wayne-corp:NoSchedule`) with isolated egress IPs.

## 2. Production Deployment & GitOps Automation
- **GitOps Reconciliation**: Declarative infrastructure managed via ArgoCD / Flux synchronizing Kubernetes manifests from source control.
- **Multi-AZ High Availability**: Workloads spread across 3 Availability Zones with PodDisruptionBudgets (`minAvailable: 2`).
- **Canary Deployments**: Automated canary rollouts (Argo Rollouts / Flagger) analyzing error rates and p99 latency before 100% traffic shift.
