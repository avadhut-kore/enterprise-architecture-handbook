# Checklist: Cloud Security Review Checklist

## Executive Summary
This checklist establishes the required technical and architectural controls evaluated during formal governance reviews.

---

## Verification Criteria
- [ ] Multi-account landing zone partitioning (Prod, Non-Prod, Security, Log).
- [ ] Zero databases or caches exposed to public internet IP addresses.
- [ ] Service Control Policies (SCPs) block root account usage and public S3.
- [ ] 100% of EBS and block volumes encrypted with KMS CMKs.
- [ ] Agentless CSPM actively scanning for configuration drift.
