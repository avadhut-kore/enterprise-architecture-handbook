# Tamper-Proof Audit Logging & WORM Compliance

## Executive Summary

If an attacker compromises an administrative account, their immediate action is to delete audit logs to hide their tracks.

---

## Architectural Guarantees:
1. **S3 Object Lock (Compliance Mode)**: Logs streamed to S3 buckets configured in Compliance Mode cannot be deleted, modified, or overwritten by **ANY identity**, including the AWS Root Account, for the entire retention period (e.g., 365 days).
2. **Dedicated Log Archive Account**: Logs are shipped cross-account into a dedicated, isolated Log Archive Account where workload administrators have zero IAM permissions.
