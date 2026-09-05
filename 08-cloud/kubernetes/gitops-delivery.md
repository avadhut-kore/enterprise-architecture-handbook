# GitOps Delivery Architecture: ArgoCD and Flux

## Executive Summary

GitOps is the operational framework where the entire desired state of a Kubernetes cluster is declared in a version-controlled Git repository. An in-cluster reconciliation agent continuously synchronizes the cluster state with Git, **eliminating direct `kubectl` access for engineers**.

---

## 1. Push vs Pull-Based GitOps

```mermaid
graph TD
    subgraph INSECURE: Push-Based CI/CD
        Git1[Git Push] --> CI[Jenkins / GitHub Actions]
        CI -->|Requires Stored Admin Kubeconfig Credentials: HIGH RISK!| K8sCluster1[Kubernetes Cluster]
    end

    subgraph SECURE: Pull-Based GitOps
        Git2[Git Push: App Manifests] --> GitRepo[(Git Repository: Source of Truth)]
        K8sCluster2[Kubernetes Cluster] --> ArgoCD[ArgoCD / Flux In-Cluster Agent]
        ArgoCD -->|Polls / Webhook Pull over Outbound TLS| GitRepo
        ArgoCD -->|Detects Drift & Reconciles State Locally| K8sCluster2
    end
```

---

## 2. Enterprise GitOps Repository Structure

Organize GitOps repositories into two distinct tiers:
1. **Application Source Repositories**: Contains code, unit tests, and Dockerfile. CI pipeline compiles code, runs scans, builds image, and issues a pull request updating the image tag in the Config Repo.
2. **Infrastructure / Config Repositories**: Contains Kustomize/Helm manifests structured by environment (`environments/dev`, `environments/staging`, `environments/prod`). ArgoCD monitors this repository exclusively.
