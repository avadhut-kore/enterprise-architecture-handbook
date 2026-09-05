# Small Organization Landing Zone Blueprint (3 Accounts)

## Executive Summary

Designed for startups, independent business units, or small IT departments ($< 25$ engineers).

---

## 1. Account Topology

```mermaid
graph TD
    Root[Organizations Root Account] --> CoreOU[Core Services]
    Root --> WorkloadsOU[Workloads]

    CoreOU --> SharedAcct[Shared Services & Security Account: Central Billing, Identity]
    WorkloadsOU --> NonProdAcct[Non-Production Account: Dev / Test / Staging]
    WorkloadsOU --> ProdAcct[Production Account: Strictly Isolated Production Workloads]
```

---

## 2. Core Guardrails
- Single transit VPC with environment-isolated subnets.
- Shared AWS IAM Identity Center or Entra ID directory.
- Centralized billing with automated budget threshold alarms.
