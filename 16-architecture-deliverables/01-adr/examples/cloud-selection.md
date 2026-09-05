# ADR-0006: Cloud-Native Managed Services vs Multi-Cloud Portability

---
**Metadata**:
* **ADR ID**: ADR-0006
* **Title**: Infrastructure Strategy — Cloud-Native Managed Services on AWS
* **Status**: Accepted
* **Date**: 2026-03-15
* **Decision Owners**: Chief Cloud Architect, VP of Infrastructure
---

## 1. Context & Problem Statement
Determine whether to architect the platform using cloud-agnostic abstractions (e.g., self-hosted databases and generic Kubernetes across clouds) or fully embrace AWS-managed services (Amazon Aurora, SQS, KMS, EKS).

## 2. Decision & Rationale
Embrace **Cloud-Native AWS Managed Services**.
Theoretical multi-cloud portability introduces lowest-common-denominator compromises and triples infrastructure maintenance costs. Leveraging managed services (Aurora, KMS, Managed Kafka) allows the team to redirect 40% of platform engineering capacity toward core business capabilities. Exit strategies will be maintained at the software interface boundary rather than infrastructure layer.
