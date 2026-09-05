# Serverless Security & Micro-Perimeters

## Executive Summary

Serverless compute shifts security from network perimeter defense to **granular identity authorization**. Each individual function must be encapsulated within a minimal micro-perimeter.

---

## 1. The Micro-IAM Role Principle

```mermaid
graph TD
    subgraph INSECURE: Shared Monolithic Role
        SharedRole[Shared IAM Role: Admin S3 + Admin DynamoDB + Admin SQS]
        F1[Function: Image Resizer] --> SharedRole
        F2[Function: User Profile API] --> SharedRole
        F3[Function: Payment Transactor] --> SharedRole
    end

    subgraph SECURE: Dedicated Micro-IAM Roles
        F1Sec[Image Resizer] --> Role1[IAM: PutObject in 'thumbnails/*' ONLY]
        F2Sec[User Profile] --> Role2[IAM: GetItem on 'Users' table ONLY]
        F3Sec[Payment] --> Role3[IAM: PutItem on 'Ledger' + KMS Decrypt ONLY]
    end
```

### Security Guardrails
- **1 Function = 1 Dedicated IAM Role**: Never share IAM execution roles across multiple serverless functions.
- **Ephemeral Storage Security**: Sensitive decrypted memory or temporary files stored in `/tmp` persist between warm invocations. Always overwrite or purge temporary directories before the function handler returns.
