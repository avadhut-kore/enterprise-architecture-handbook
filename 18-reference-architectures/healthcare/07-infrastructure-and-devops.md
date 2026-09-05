# Infrastructure & Deployment: Healthcare Platform

## 1. HIPAA Quarantined Network Architecture
- Clinical data repositories reside in private isolated subnets with zero internet ingress or egress.
- Access occurs exclusively through mutual TLS (mTLS) authenticated internal gateways with strict network security policies.

## 2. Production Deployment & GitOps Automation
- **GitOps Reconciliation**: Declarative infrastructure managed via ArgoCD / Flux synchronizing Kubernetes manifests from source control.
- **Multi-AZ High Availability**: Workloads spread across 3 Availability Zones with PodDisruptionBudgets (`minAvailable: 2`).
- **Canary Deployments**: Automated canary rollouts (Argo Rollouts / Flagger) analyzing error rates and p99 latency before 100% traffic shift.
