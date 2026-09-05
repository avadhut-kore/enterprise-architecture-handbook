# Enterprise Domain Gap Analysis Template

The standardized master gap-analysis table used during enterprise architecture assessments.

---

## 1. Master Gap Analysis Table

| Domain | Current State | Target State | Gap Description | Business Impact | Priority | Remediation Initiative |
| :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| **Business** | Customer onboarding takes 3 days with branch visits. | 100% digital onboarding completed in <90 seconds. | Missing real-time digital KYC & biometric verification capability. | 32% applicant drop-off ($18M lost revenue). | **P0** | Digital Identity & KYC Modernization |
| **Application** | Core underwriting logic hardcoded in monolithic COBOL. | Composable Drools/Camunda rules engine hosted on K8s. | Business rules cannot be updated without 6-month mainframe release. | Competitors launch new insurance products 4x faster. | **P0** | Underwriting Rules Extraction |
| **Data** | 4 disparate customer tables across 4 regional ERPs. | Single Customer Master (Golden Record) via Data Mesh. | Conflicting customer profiles; duplicate marketing mailings. | Regulatory non-compliance (GDPR Right to Erasure). | **P1** | Global Customer MDM Deployment |
| **Technology** | 120 bare-metal Linux servers in legacy on-prem colocation. | Automated multi-region AWS landing zone via Terraform. | High hardware maintenance, zero auto-scaling, long lead times. | Black Friday crashes cost $2.4M/hr in downtime. | **P0** | Cloud Migration & Auto-Scaling |
| **Security** | Perimeter VPN model; password-only internal auth. | Zero Trust architecture with FIDO2 MFA & SPIFFE identity. | Internal lateral movement risk; vulnerability to credential theft. | High risk of ransomware breach; insurance refusal. | **P0** | Zero Trust & Enterprise Identity |
