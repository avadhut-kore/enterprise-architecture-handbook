# PII Isolation, Tokenization & Data Redaction Flow

Compliance architecture detailing field-level encryption, tokenization gateways, and irreversible pseudonymization across enterprise data pipelines.

## Mermaid Architecture Diagram

```mermaid
graph LR
    subgraph UntrustedBoundary ["Public Ingest Zone"]
        Customer["Customer Payload<br/>(Name, SSN, Credit Card, Email)"]
        APIGW["API Gateway Ingress"]
        Customer -->|"Cleartext HTTPS"| APIGW
    end

    subgraph TokenizationZone ["PCI / PII Vault Perimeter (Restricted Zone)"]
        TokenGateway["Tokenization Gateway / Proxy"]
        VaultDB[("Secure Token Vault DB<br/>[Hardware HSM AES-256 Key]")]

        APIGW -->|"Inspect Payload"| TokenGateway
        TokenGateway <-->|"Exchange Raw SSN/PAN for Token"| VaultDB
    end

    subgraph SanitizedInternalMesh ["Internal Application & Analytics Zone"]
        AppPod["Order Microservice<br/>[Handles Tokenized ID: tok_98a72]"]
        DataLake["Analytical Lakehouse<br/>[Contains only Hashed / Tokenized IDs]"]
        
        TokenGateway -->|"Sanitized Payload (Tokens Only)"| AppPod
        AppPod -->|"Emit Events"| DataLake
    end

    subgraph RightToBeForgotten ["GDPR Erasure Pipeline (Article 17)"]
        DSR["Data Subject Request Engine"]
        DSR -->|"Delete Mapping Key from HSM Vault"| VaultDB
        note["Once key is deleted from Vault DB, downstream lakehouse records become mathematically permanently irreversibly anonymized"]
    end

    classDef pub fill:#ffebee,stroke:#c62828,stroke-width:2px;
    classDef vlt fill:#f3e5f5,stroke:#4a148c,stroke-width:2px;
    classDef app fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    class Customer,APIGW pub;
    class TokenGateway,VaultDB,DSR vlt;
    class AppPod,DataLake app;
```

## PlantUML Specification

```plantuml
@startuml
actor Customer
participant "API Gateway" as gw
participant "Tokenization Gateway" as tok
database "Secure Vault (HSM)" as vault
participant "Internal Microservice" as app
database "Analytics Data Lake" as lake

Customer -> gw : Submit SSN & Credit Card
gw -> tok : Forward Raw Payload
tok -> vault : Store PII & Generate Random Token (tok_xyz)
vault -> tok : Return Token
tok -> app : Forward Payload with tok_xyz (PII Stripped)
app -> lake : Ingest Non-PII Data
@enduml
```

## Architectural Design Considerations

* **Minimization of Scope**: Isolate raw PII storage to a single dedicated vault subnet; prevent raw identifiers from propagating into general application databases.
* **Format-Preserving Encryption (FPE)**: Use FPE or format-matching tokens to avoid breaking downstream relational schemas and validation regexes.
* **Cryptographic Erasure (Crypto-Shredding)**: Fulfill GDPR Right-to-be-Forgotten requests by deleting the encryption key for a specific subject rather than executing expensive mutations across multi-terabyte Parquet files.

## Related Documentation & Patterns

* [Data Classification](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/data-classification.md)
* [Data Lineage](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/data-lineage.md)
* [Encryption](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/encryption.md)
