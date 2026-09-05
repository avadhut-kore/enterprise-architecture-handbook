# Privileged Identity Management (PIM / PAM) & Just-in-Time Access

## Executive Summary

Standing administrative privileges represent an unacceptable attack surface. Privileged Identity Management (PIM) mandates that administrative rights are **ephemeral, justification-backed, peer-approved, and automatically revoked**.

---

## 1. Just-in-Time (JIT) Elevation Workflow

```mermaid
sequenceDiagram
    autonumber
    actor SRE as On-Call Engineer
    participant Slack as ChatOps / ServiceNow
    actor Lead as SRE Team Lead
    participant PIM as Privileged Identity Provider (PIM)
    participant Cloud as Cloud Production Environment

    SRE->>Slack: Requests 2-Hour Elevation to `Prod-DB-Admin` (Incident INC-4091)
    Slack->>Lead: Pushes approval prompt with incident ticket verification
    Lead->>Slack: Approves request
    Slack->>PIM: Activates role assignment with 120-minute hard TTL
    PIM->>Cloud: Grants temporary IAM role membership
    Note over SRE,Cloud: SRE resolves production incident; all commands audited
    PIM->>Cloud: 120 minutes expire; PIM automatically revokes IAM role
```
