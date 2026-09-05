# SEC-FIN-001: Core Banking Enclave Security Design

---
**Metadata**:
* **Document ID**: SEC-FIN-001
* **Classification**: Restricted - Banking Confidential
* **Compliance**: PCI-DSS Level 1, SOC 2 Type II
* **Status**: Approved
---

## 1. Security Architecture Summary
This document defines the security controls for the Core Banking Transaction Enclave. All compute nodes run in private, isolated VPC subnets with zero direct internet access. Ingress is protected by AWS WAF and Cloudflare Magic Transit. Microservices authenticate via Istio mTLS with SPIRE X.509 certificates. Primary account numbers are tokenized via Thales HSM.
