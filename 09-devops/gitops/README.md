# GitOps Architecture & Continuous Deployment

GitOps extends Infrastructure as Code to modern cloud-native application delivery, establishing Git as the immutable, auditable single source of truth for both declared infrastructure and running cluster state.

## Core Architectural Principles

1. **Declarative Descriptions**: The entire system is described declaratively using declarative specifications (Kubernetes manifests, Kustomize overlays, Helm charts).
2. **Version-Controlled Single Source of Truth**: System desired state is versioned in Git, providing complete traceability, commit signatures, peer review, and instant rollback.
3. **Automated State Pull Reconciliation**: Software agents (e.g., ArgoCD, Flux) continuously compare desired state in Git against observed state in the target cluster, pulling updates rather than pushing through CI credentials.
4. **Self-Healing and Continuous Drift Mitigation**: Unapproved manual changes (kubectl edit, ad-hoc mutations) are detected and automatically reverted back to the Git-defined golden state.

## Contents

- [GitOps Architecture and Reconciliation](./gitops-architecture-and-reconciliation.md) - Deep dive into pull-based reconciliation loops, ArgoCD vs Flux architecture, automated drift mitigation, push vs pull deployment trade-offs, and multi-tenant repository layouts.
- [Cross-Reference: Deployment Strategies](../deployment-strategies/README.md) - Canary, Blue/Green, and Progressive Delivery orchestration with Argo Rollouts and Flagger.
