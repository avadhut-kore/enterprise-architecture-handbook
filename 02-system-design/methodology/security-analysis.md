# Security Analysis in System Design

## Overview

Security Analysis is the deliberate architectural process of identifying threat vectors, evaluating trust boundaries, and designing preventative, detective, and responsive safeguards into a distributed system design. In modern enterprise environments, security cannot be "bolted on" after code is written; it is an architectural property that must be engineered from the inception of system design.

---

## 1. Architectural Threat Modeling: Data Flow STRIDE

Architects conduct threat modeling by mapping data flows, identifying trust boundaries, and evaluating each interaction against the **STRIDE** model:

```mermaid
flowchart TD
    subgraph UntrustedZone["Untrusted Public Network"]
        Client["Web / Mobile Client"]
    end

    TrustBoundary1{{"=== Trust Boundary 1: Perimeter ==="}}

    subgraph DMZ["DMZ / Ingress Enclave"]
        WAF["Web Application Firewall"]
        APIGW["API Gateway (OAuth2 / OIDC Inspection)"]
    end

    TrustBoundary2{{"=== Trust Boundary 2: Microsegmentation ==="}}

    subgraph InternalVPC["Secure Private Application Subnet"]
        OrderSvc["Order Processing Service"]
        PaymentSvc["Payment Service (PCI DSS Scope)"]
    end

    subgraph StorageSubnet["Encrypted Storage Subnet"]
        CoreDB[("PostgreSQL (KMS Encrypted)")]
        Vault[("Hardware Security Module / KMS")]
    end

    Client --> TrustBoundary1 --> WAF --> APIGW
    APIGW --> TrustBoundary2 --> OrderSvc
    OrderSvc --> PaymentSvc
    OrderSvc --> CoreDB
    PaymentSvc --> Vault
```

### Threat Vector Mapping across Trust Boundaries

| Boundary Interaction | STRIDE Threat | Potential Attack Scenario | Architectural Defense |
|:---|:---|:---|:---|
| **Client to Ingress** | **Spoofing** | Attacker impersonates an authenticated customer using stolen session cookie. | Enforce short-lived JWT tokens signed via RS256 with OIDC identity verification and refresh token rotation. |
| **Client to Ingress** | **Denial of Service** | Botnet floods checkout endpoint with 50,000 requests/second. | Cloudflare WAF DDoS mitigation + Token Bucket rate limiting keyed by client IP and User ID. |
| **Gateway to Service**| **Tampering** | Man-in-the-middle attacker alters order price query parameters on internal network. | Mutual TLS (mTLS) with strict cipher suites (TLS 1.3) across all internal microservice communication. |
| **Service to Database**| **Information Disclosure** | SQL injection in user search parameter dumps the customer table. | Strict Parameterized Queries / ORM usage; Principle of Least Privilege database IAM credentials. |
| **Payment Service** | **Elevation of Privilege**| Compromised worker node attempts to read payment credit card keys from Vault. | Workload identity verification (AWS IAM Roles for Service Accounts - IRSA) ensuring only Payment pods can access KEK. |

---

## 2. Enterprise Data Classification Framework

Every data attribute stored or processed by the system must be classified into one of four tiers, dictating mandatory security controls:

```mermaid
graph TD
    DataClass["Data Classification Hierarchy"]
    DataClass --> Public["1. Public: Marketing copy, public product catalogs (Zero encryption restrictions)"]
    DataClass --> Internal["2. Internal: Operational logs, employee directories (Standard TLS + KMS encryption)"]
    DataClass --> Confidential["3. Confidential: Customer names, emails, order histories (PII / GDPR scope; masked logs)"]
    DataClass --> Restricted["4. Restricted: Credit cards, SSNs, passwords, health data (PCI/HIPAA scope; tokenized)"]
```

---

## 3. Cryptographic Key Management & Envelope Encryption

Directly encrypting millions of customer records with a single static master key in code is an enterprise anti-pattern. Architects enforce **Envelope Encryption**:

```mermaid
sequenceDiagram
    autonumber
    participant App as Application Service
    participant KMS as Key Management Service (AWS KMS / HSM)
    participant Storage as Encrypted Database

    App->>KMS: Request New Data Encryption Key (DEK)
    KMS-->>App: Return Plaintext DEK + Ciphertext DEK (Encrypted with KEK)
    App->>App: Encrypt Customer PII record using Plaintext DEK
    App->>App: MEMORY ZEROIZE: Wipe Plaintext DEK from RAM immediately!
    App->>Storage: Store Encrypted Record + Ciphertext DEK
    Note over Storage: Even if database is leaked, data is useless without KMS KEK!
```

---

## 4. Secrets Management Best Practices

1. **Zero Hardcoded Secrets**: Secrets (database passwords, API keys, private certificates) must never reside in source code, Docker images, or Git repositories.
2. **Dynamic Just-in-Time Credentials**: Applications authenticate to HashiCorp Vault or AWS Secrets Manager using workload identities to obtain short-lived credentials that rotate automatically every 60 minutes.
3. **Automated Secret Scanning**: Pre-commit hooks (TruffleHog, GitGuardian) and CI pipelines scan every commit to immediately block pull requests containing credentials.
