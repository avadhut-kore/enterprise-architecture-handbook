# Least Privilege Engineering & Permission Boundaries

## Executive Summary

Enforcing least privilege requires automated tooling to calculate the exact set of permissions required by workloads and prevent privilege escalation.

---

## 1. IAM Permission Boundaries Architecture

```mermaid
graph TD
    Admin[Central Cloud Security Team] --> Boundary[Permission Boundary: Max Permissible Actions]
    Dev[DevOps Engineer] -->|Creates IAM Role for Lambda| NewRole[New IAM Role]
    Dev --> Attach[Attempts to Attach 'AdministratorAccess']

    NewRole --> Eval{Effective Permissions = Role Permissions INTERSECT Permission Boundary}
    Eval --> Result[Effective Permissions Capped at Boundary: Escalation PREVENTED!]
```

---

## 2. Automated Access Pruning via Access Analyzer

- Deploy **IAM Access Analyzer**: Continuously analyzes CloudTrail logs to identify granted permissions that have never been exercised by a workload over a 90-day window.
- Automatically generate refined, right-sized IAM policies removing unused privileges before promoting services to production.
