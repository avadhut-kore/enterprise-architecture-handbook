# Workload Identity Federation

## Executive Summary

Workload Identity Federation enables software running in Kubernetes, GitHub Actions, or on-premises datacenters to authenticate securely to cloud providers (AWS, Azure, GCP) **without storing long-lived API keys or credentials**.

---

## 1. Workload Identity Federation Architecture

```mermaid
sequenceDiagram
    autonumber
    participant Pod as Microservice Pod (EKS)
    participant Kube as Kubernetes OIDC Issuer
    participant Cloud as AWS STS / Cloud IAM
    participant S3 as Target Cloud Resource (S3)

    Pod->>Kube: Requests projected service account token
    Kube-->>Pod: Injects signed short-lived OIDC JWT
    Pod->>Cloud: AssumeRoleWithWebIdentity(Token, RoleARN)
    Cloud->>Kube: Verifies JWT signature against public JWKS
    Cloud-->>Pod: Issues 15-minute temporary Cloud Access Keys
    Pod->>S3: Reads objects using temporary credentials
```
