# Capability Mapping Templates: End-to-End Enterprise Traceability

Practical templates linking Business Capability to Business Process, Supporting Application, Data Entities, Technology Runtime, and Cloud Infrastructure.

---

## 1. The Enterprise Traceability Template

| Dimension | Enterprise Specification | Example Instance |
| :--- | :--- | :--- |
| **Capability ID & Name** | Unique ID + Verb-Noun Name | `CAP-01.02.01: Customer Identity Verification` |
| **Capability Level** | Level 1, 2, or 3 | Level 3 (Discrete Functional Ability) |
| **Business Value Stream Stage** | Stage in end-to-end customer journey | Customer Acquisition -> Onboarding Stage |
| **Executive Owner** | Head of Business Domain | VP of Digital Experience & Fraud Prevention |
| **Business Process (How)** | Specific workflow or policy | Workflow WF-KYC-04: Digital Identity Biometric Validation |
| **Primary Application** | Supporting software system | `APP-104: Enterprise KYC Identity Hub` |
| **Application TIME Status** | Invest, Tolerate, Migrate, Eliminate | **Invest** (Target global standard) |
| **Core Data Entities** | Data created or consumed | `CustomerProfile`, `IdentityDocument`, `BiometricHash` |
| **Data Classification** | Security & Privacy rating | Restricted / PII (GDPR, CCPA, PCI-DSS) |
| **Integration Protocols** | API & Event Contracts | REST OpenAPI 3.0, Kafka topic `events.kyc.verification` |
| **Technology Runtime** | Language & Framework standards | Java 21 / Spring Boot 3 / PostgreSQL 16 |
| **Hosting & Infrastructure** | Cloud / On-Prem deployment | AWS EKS (eu-central-1, us-east-1 multi-region) |
| **Regulatory Drivers** | Compliance mandates | USA PATRIOT Act, EU 5AMLD, MAS Notice 626 |

---

## 2. Reverse Traceability Verification

```text
IF infrastructure failure occurs on: AWS EKS (eu-central-1)
  -> AFFECTS application: APP-104 (Enterprise KYC Identity Hub)
    -> DEGRADES capability: CAP-01.02.01 (Customer Identity Verification)
      -> HALTS value stream: Customer Acquisition -> Onboarding
        -> RISKS business outcome: 500k Digital Customer Target ($14M Revenue)
```
