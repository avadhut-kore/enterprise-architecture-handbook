# Cloud Security Posture Management (CSPM) & Automated Remediation

## Executive Summary

CSPM provides continuous, agentless visibility into multi-cloud infrastructure, detecting misconfigurations (e.g., publicly readable S3 buckets, open security groups) against CIS benchmarks.

---

## Event-Driven Automated Remediation Architecture

```mermaid
sequenceDiagram
    autonumber
    actor Dev as Misconfigured Terraform
    participant S3 as S3 Bucket (Publicly Accessible)
    participant Event as CloudTrail / EventBridge
    participant Lambda as Remediation Lambda
    participant Sec as Security Hub / Slack

    Dev->>S3: Creates S3 bucket with public read ACL
    S3->>Event: Emits API event: `PutBucketAcl`
    Event->>Lambda: Triggers automated compliance rule
    Lambda->>S3: Executes `PutPublicAccessBlock` (Enforces Block Public Access)
    Lambda->>Sec: Posts incident notification: "Auto-remediated public bucket in Account #402"
```
