# Mid-Size Enterprise Landing Zone Blueprint (8-15 Accounts)

## Executive Summary

Designed for mid-market enterprises ($100 - 500$ engineers) requiring clear segregation of duties.

---

## 1. Account Topology

```mermaid
graph TD
    Root[Organization Root] --> PlatformOU[Platform Infrastructure]
    Root --> SecurityOU[Security & Audit]
    Root --> AppsOU[Application Workloads]

    PlatformOU --> NetAcct[Shared Network Transit Account: Transit Gateway]
    PlatformOU --> ToolsAcct[Shared CI/CD & Artifact Registry Account]

    SecurityOU --> LogAcct[Log Archive Account: Immutable S3]
    SecurityOU --> SecOpsAcct[Security Operations: GuardDuty, Security Hub]

    AppsOU --> ProdOU[Production OU: Dedicated Account per Major Domain]
    AppsOU --> NonProdOU[Non-Production OU: Dedicated Dev/Stage Accounts]
```
