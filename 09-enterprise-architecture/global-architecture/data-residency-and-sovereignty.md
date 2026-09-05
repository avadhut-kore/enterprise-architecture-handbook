# Data Residency & Sovereignty Architecture

Architectural patterns to comply with strict national data localization and cross-border privacy laws.

---

## 1. Data Residency Compliance Models

```mermaid
flowchart LR
    subgraph European Union (GDPR / DORA)
        EUDb["EU Data Vault (Frankfurt)<br/>Customer PII & Transactions Encrypted with Customer-Managed Keys (KMS)"]
    end
    subgraph United States (SEC / CCPA)
        USDb["US Data Vault (N. Virginia)<br/>US Customer PII"]
    end
    subgraph Global Analytics Tier
        GlobalAnalytics["Global Anonymized Analytics<br/>(All PII cryptographically tokenized before export)"]
    end
    EUDb -->|Tokenized / Anonymized Data Only| GlobalAnalytics
    USDb -->|Tokenized / Anonymized Data Only| GlobalAnalytics
```

---

## 2. Key National Regulatory Constraints
* **EU GDPR / Schrems II**: Personal data of EU citizens cannot leave the European Economic Area without strict adequacy safeguards.
* **China PIPL / Data Security Law**: Critical information infrastructure data must remain physically stored within mainland China.
* **Financial Data Localization (RBI India, MAS Singapore)**: Transaction data and payment records must reside in local in-country data centers.
