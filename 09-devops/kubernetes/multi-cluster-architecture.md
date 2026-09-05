# Multi-Cluster Kubernetes Architecture

Operating a single giant shared Kubernetes cluster across an entire enterprise creates severe blast radius risks and tenancy friction.

## 1. Single Cluster vs Multi-Cluster Archetypes

| Archetype | Blast Radius | Operational Overhead | Cost Efficiency | Recommendation |
| :--- | :--- | :--- | :--- | :--- |
| **One Mega Cluster** | Catastrophic (Single etcd/CNI failure topples all apps). | Low (One cluster to upgrade). | Highest (Maximum bin-packing). | Avoid for production enterprise. |
| **Cluster per Environment** | Moderate (Staging failure cannot touch Production). | Moderate | Good | Baseline enterprise standard (Dev, Stage, Prod). |
| **Cluster per Business Unit** | Low (FinTech cluster isolated from Marketing cluster). | High | Moderate | Recommended for high-security / multi-tenant isolation. |
| **Cluster per Region** | Low (Survives AWS/Azure regional outages). | High | Moderate | Mandatory for global high-availability architectures. |

## 2. Fleet Management & GitOps
In a multi-cluster architecture, application deployments must be managed declaratively via GitOps (ArgoCD ApplicationSets / Flux). Never connect CI runners directly to 20 separate cluster API servers.

## Related Resources
- [GitOps Architecture](../gitops/README.md)
- [Production Cluster Architecture](./production-cluster-architecture.md)
