# Secrets Management in Kubernetes (External Secrets Operator)

## Executive Summary

Storing raw secrets in native Kubernetes `Secret` manifests committed to Git is a critical anti-pattern (Kubernetes secrets are merely Base64-encoded, not encrypted).

---

## 1. External Secrets Operator (ESO) Architecture

```mermaid
sequenceDiagram
    autonumber
    participant Git as Git Repository (GitOps)
    participant K8s as Kubernetes Cluster
    participant ESO as External Secrets Operator
    participant KMS as AWS Secrets Manager / Vault
    participant Pod as Application Pod

    Git->>K8s: Deploys `ExternalSecret` manifest (No secrets in Git!)
    K8s->>ESO: Triggers controller reconciliation
    ESO->>KMS: Fetches encrypted secret via Workload Identity (IAM)
    KMS-->>ESO: Returns secret payload
    ESO->>K8s: Creates in-memory native `Secret` object
    K8s->>Pod: Mounts secret as volume or environment variable
```
