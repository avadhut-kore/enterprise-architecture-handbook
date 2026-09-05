# GCP Cloud IAM & Workload Identity Federation

## Executive Summary

Google Cloud IAM manages authorization by binding **identities** (users, groups, service accounts) to **roles** containing granular permissions. Enterprise GCP architecture leverages **Workload Identity Federation** to eliminate long-lived private keys.

---

## 1. Workload Identity Federation Architecture

```mermaid
graph LR
    GitHub[GitHub Actions / AWS / On-Prem IDP] -->|OIDC Token Exchange| STS[Google Security Token Service (STS)]
    STS --> WIF[Workload Identity Pool]
    WIF -->|Impersonates| SA[GCP Service Account: 'terraform-deployer']
    SA --> GCS[(Cloud Storage Deployment Bucket)]
```

### Eliminating Service Account Keys
Exporting service account JSON private keys (`credentials.json`) is the leading cause of security breaches in GCP. 
- **Rule**: Enforce `constraints/iam.disableServiceAccountKeyCreation` at the Organization level.
- External CI/CD pipelines (GitHub Actions, GitLab, AWS workloads) must authenticate via **Workload Identity Federation**, exchanging short-lived OIDC tokens for temporary federated GCP OAuth tokens.
