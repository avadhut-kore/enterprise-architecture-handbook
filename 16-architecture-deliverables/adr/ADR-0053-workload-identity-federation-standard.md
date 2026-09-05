# ADR-0053: Elimination of Static Cloud API Keys via Workload Identity Federation

## Metadata
```yaml
id: ADR-0053
title: Elimination of Static Cloud API Keys via Workload Identity Federation
status: accepted
decision_type: architectural
scope: enterprise-cloud-infrastructure
owners: enterprise-architecture-board
date: 2026-09-05
review_cadence: annual
```

---

## 1. Context & Problem Statement
Hardcoded AWS IAM access keys and service account JSON files were repeatedly discovered in Git repositories and developer workstations.

---

## 2. Decision
We mandate Workload Identity Federation (EKS Pod Identity, Azure Workload Identity, GCP Workload Identity) for all machine authentication, prohibiting permanent access keys.

---

## 3. Positive Consequences
- Completely eliminates credential theft via leaked source code.
- Issues short-lived, ephemeral OAuth/STS tokens that expire in 1 hour.
- Automated credential rotation without application downtime.

---

## 4. Negative Consequences & Trade-offs
- Requires configuring OIDC discovery endpoints and identity trust relationships.

---

## 5. Alternatives Considered & Rejected
- **Static IAM User Access Keys with 90-Day Rotation**: Rejected because 90 days is more than enough time for an attacker to compromise a breached key.
