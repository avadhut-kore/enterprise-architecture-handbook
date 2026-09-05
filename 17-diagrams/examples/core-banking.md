# Core Banking & Real-Time Payments Architecture

This reference architecture models a next-generation core banking platform supporting real-time gross settlement (RTGS), ISO 20022 message compliance, double-entry immutable ledgers, and Hardware Security Module (HSM) transaction signing.

## 1. Business Context & Architectural Drivers
* **Throughput Target**: 5,000 settlements/second; zero tolerance for data loss (RPO = 0, RTO $\le 30$ seconds).
* **Compliance**: Strict adherence to ISO 20022 (pacs.008, pacs.002), PCI-DSS Level 1, and Central Bank regulatory frameworks.
* **Security**: FIPS 140-3 Level 3 HSM hardware cryptography for transaction signing and key generation.

## 2. C4 Level 1: System Context

```mermaid
graph TB
    subgraph Personas ["Users & Regulators"]
        RetailClient["Retail & Corporate Customers"]
        BankAdmin["Treasury & Ops Officers"]
        CentralBank["Central Bank Clearing Network (FedNow / SEPA)"]
    end

    subgraph CoreBankingSystem ["Core Banking & Payment Engine"]
        Engine["Core Banking Platform<br/>- Real-time Balance Engine<br/>- Double-Entry General Ledger<br/>- Fraud Detection Engine"]
    end

    subgraph ClearingNetworks ["Interbank Clearing & Settlement"]
        SwiftNetwork["SWIFT Messaging Network"]
        CardNetworks["Visa / Mastercard Schemes"]
    end

    RetailClient -->|"Initiates Transfers"| Engine
    BankAdmin -->|"Manages Liquidity & Positions"| Engine
    Engine <-->|"Instant Settlement (ISO 20022)"| CentralBank
    Engine <-->|"Cross-Border FX"| SwiftNetwork
    Engine <-->|"Card Clearings"| CardNetworks
```

## 3. C4 Level 2: Container Architecture & HSM Integration

```mermaid
graph TB
    subgraph PresentationTier ["Secure Ingress Tier"]
        mTLSProxy["mTLS Mutual Authentication Proxy<br/>[Container: Envoy]<br/>Enforces client certs and Zero Trust"]
    end

    subgraph CoreBankingMesh ["Core Banking Mesh (Private Restricted Subnets)"]
        PaymentRouter["ISO 20022 Payment Router<br/>[Container: Go]<br/>Parses pacs.008 messages, validates schemas"]
        
        FraudEngine["Real-time Fraud Engine<br/>[Container: C++ / Python]<br/>Sub-50ms ML behavioral scoring"]
        
        LedgerService["Double-Entry Ledger Service<br/>[Container: Java 21]<br/>Executes atomic debit/credit multi-leg transactions"]
        
        HSMBridge["HSM Cryptographic Connector<br/>[Container: C / PKCS#11]<br/>Interfaces with Hardware Security Modules"]
    end

    subgraph SecureStorageTier ["High-Assurance Persistence Tier"]
        HardwareHSM["Hardware Security Module (HSM)<br/>[Thales payShield 10K / FIPS 140-3 L3]"]
        LedgerDB[("Immutable Accounting Ledger DB<br/>[CockroachDB Dedicated - Serializable ACID]")]
        AuditStore[("Immutable Audit WORM Store<br/>[AWS S3 Object Lock Vault]")]
    end

    mTLSProxy --> PaymentRouter
    PaymentRouter --> FraudEngine
    FraudEngine --> LedgerService
    LedgerService --> HSMBridge
    HSMBridge <--> HardwareHSM
    LedgerService --> LedgerDB
    LedgerService -.->|"Stream Audit"| AuditStore
```

## 4. Real-Time Payment Settlement Sequence (ISO 20022)

```mermaid
sequenceDiagram
    autonumber
    actor Originator as Sending Bank Customer
    participant GW as Core Ingress Gateway
    participant Router as ISO 20022 Payment Engine
    participant Ledger as Ledger Engine
    participant HSM as Hardware HSM
    participant CentralBank as Central Bank Instant Network

    Originator->>GW: POST /payments/instant (pacs.008 XML)
    GW->>Router: Validate Schema & Digital Signature
    Router->>Router: Screen Sanctions (OFAC / PEP check)
    Router->>Ledger: Debit Customer Balance ($50,000)
    Ledger->>Ledger: Verify Funds Available & Lock Account
    
    Router->>HSM: Request Transaction Authorization Signature
    HSM-->>Router: Cryptographic Signature (MAC / RSA-4096)
    
    Router->>CentralBank: Dispatch pacs.008 with HSM Signature
    CentralBank-->>Router: Receive pacs.002 Confirmation (Settled)
    
    Ledger->>Ledger: Post Balanced Entry: Debit Cash / Credit Nostro
    Router-->>GW: Payment Completed
    GW-->>Originator: Transfer Confirmation (UTR Receipt)
```

## 5. Architectural Principles & Controls
* **Double-Entry Accounting Invariant**: Every debit must have an equal and offsetting credit; `SUM(Debits) - SUM(Credits) == 0` enforced at the database schema level via constraint triggers.
* **Immutable Journaling**: Ledger tables are strictly append-only; historical corrections are performed exclusively through explicit reversing entries.
* **Network Micro-segmentation**: Hardware HSMs and ledger database clusters are isolated in dedicated Tier-4 private security zones with zero external routing.
