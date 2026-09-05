# Technology Comparison: Infrastructure as Code Trade-Off Matrix

## Executive Summary
This reference matrix evaluates the architectural trade-offs between terraform / opentofu vs cloud-native iac (cloudformation / bicep).

---

## Architectural Comparison Matrix

| Dimension | HashiCorp Terraform / OpenTofu | Cloud-Native IaC (Bicep / CloudFormation) |
| :--- | :--- | :--- |
| **Workflow Consistency** | Unified workflow across all cloud providers | Distinct syntax and toolchain per provider |
| **Day-0 Feature Support** | Minor lag (days/weeks for new APIs) | Immediate Day-0 support for all native APIs |
| **State Management** | External state file requiring locking | Managed internally by cloud control plane |
| **Enterprise Adoption** | Industry gold standard | Restricted to single-cloud organizations |
