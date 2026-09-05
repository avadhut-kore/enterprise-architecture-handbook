# Cloud Governance Architecture

## Executive Summary

Cloud governance provides the automated policies, resource guardrails, financial tags, and service approval workflows required to manage enterprise cloud consumption safely and economically.

---

## Governance Pillars

```mermaid
graph TD
    Gov[Enterprise Cloud Governance]
    Gov --> Tagging[1. Mandatory Resource Tagging & Metadata]
    Gov --> Policy[2. Automated Guardrails: Policy as Code]
    Gov --> ServiceApproval[3. Cloud Service Approval & Risk Tiers]
    Gov --> Framework[4. Cloud Governance Operating Framework]
```

---

## Deliverables & Guides

| Document | Focus Area | Architectural Impact |
| :--- | :--- | :--- |
| **[Resource Tagging Standards](resource-tagging-standards.md)** | Metadata taxonomy | Mandatory tags: CostCenter, Owner, Environment, Classification |
| **[Guardrails & Service Approval](guardrails-and-service-approval.md)**| Service authorization | Managing risk tiers, approved cloud services, exception handling |
| **[Cloud Governance Framework](cloud-governance-framework.md)** | Operating framework | Comprehensive enterprise governance operating framework |
