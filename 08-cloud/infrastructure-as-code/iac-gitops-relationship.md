# IaC and GitOps: Complementary Delivery Paradigms

## Executive Summary

Architects often debate "Terraform vs GitOps." In enterprise architecture, **IaC and GitOps are complementary layers of the same delivery pipeline**, operating at different abstraction tiers.

---

## 1. Separation of Concerns: IaC vs GitOps

```mermaid
graph TD
    subgraph Layer 1: Foundational Infrastructure [Terraform / OpenTofu]
        TF[Terraform Pipeline] --> VPC[VPCs & Subnets]
        TF --> IAM[Cloud IAM Roles & KMS Keys]
        TF --> Cluster[EKS / AKS Control Plane & Karpenter]
    end

    subgraph Layer 2: Application Delivery [GitOps: ArgoCD / Flux]
        Cluster --> ArgoCD[ArgoCD In-Cluster Agent]
        ArgoCD --> Deployments[Microservice Deployments]
        ArgoCD --> Config[Ingress, Services, ConfigMaps]
    end

    TF ==>|Provisions K8s Cluster| Cluster
    Cluster ==>|Executes GitOps Loop| ArgoCD
```

---

## 2. Architectural Boundary Rule
- **Use Terraform/IaC**: For foundational cloud primitives that live outside the Kubernetes API (VPCs, Transit Gateways, IAM roles, managed databases, KMS keys).
- **Use GitOps (ArgoCD/Flux)**: For application workloads, pod scheduling, and services living inside the Kubernetes cluster.
