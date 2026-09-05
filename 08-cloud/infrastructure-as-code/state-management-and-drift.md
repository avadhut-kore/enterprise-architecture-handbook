# IaC State Management, Locking & Drift Detection

## Executive Summary

Declarative IaC engines (Terraform, OpenTofu) maintain a **State File** that maps declared code to real-world cloud resource IDs. Protecting state integrity and detecting out-of-band drift are foundational operational responsibilities.

---

## 1. Remote State Locking Architecture

```mermaid
graph LR
    CI1[Pipeline Run A: Applying Changes] -->|1. Acquires Distributed State Lock| LockDB[(DynamoDB / Azure Blob Lease)]
    CI1 --> StateFile[(Encrypted S3 / Storage Account)]

    CI2[Pipeline Run B: Concurrent Apply] --> LockDB
    LockDB -->|2. Lock Acquired by Run A: REJECT RUN B!| Fail[Run B Aborted: State Corruption PREVENTED!]
```

---

## 2. Automated Drift Detection Scheduling

- **The Threat of Drift**: An engineer modifies a firewall rule manually during a midnight incident; the change is forgotten and never codified in Git.
- **Continuous Reconciliation**: Schedule an automated daily or hourly pipeline running `terraform plan -detailed-exitcode`. If state drift is detected, generate an immediate alert in Slack/PagerDuty and trigger an automated reconciliation pull request.
