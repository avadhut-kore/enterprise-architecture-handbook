# Identity-Centric vs Data-Centric Security

## Executive Summary

Enterprise security architecture has evolved through three distinct paradigms: **Network-Centric**, **Identity-Centric**, and **Data-Centric**. A robust architecture does not choose between Identity and Data; it integrates both into a complementary defense model.

---

## 1. Comparative Architecture Paradigms

```mermaid
flowchart TD
    subgraph NetworkCentric ["1. Network-Centric (Legacy)"]
        A["Firewalls / Subnets / VPNs"] -->|Grants trust based on IP location| B["Internal Resources"]
    end
    subgraph IdentityCentric ["2. Identity-Centric (Modern Zero Trust)"]
        C["User / Workload Identity (OIDC/mTLS)"] -->|Authorizes access at API Gateway| D["Service Endpoints"]
    end
    subgraph DataCentric ["3. Data-Centric (Ultimate Defense)"]
        E["Cryptographic Data Object (AES-GCM)"] -->|Decryption requires Key Custody| F["Target Sensitive Record"]
    end
```

---

## 2. Architectural Comparison Matrix

| Evaluation Dimension | Identity-Centric Security | Data-Centric Security |
| :--- | :--- | :--- |
| **Primary Mechanism** | OAuth 2.0, OIDC, JWT, SAML, mTLS, Workload Identity | Envelope encryption, tokenization, hashing, row-level security |
| **Enforcement Point** | API Gateways, Service Mesh sidecars, Cloud IAM, IDPs | Cryptographic libraries, KMS, HSMs, Database engines |
| **Vulnerability to Bypass**| If identity token is compromised, attacker accesses data | Even if identity is compromised, key access policies can restrict decryption |
| **Performance Overhead** | Low (Cached JWT validation / mTLS handshake) | Moderate (Cryptographic operations, KMS network latency) |
| **Ideal Use Case** | Controlling access to microservice APIs and cloud compute | Protecting sensitive financial ledgers, healthcare records, PII |
