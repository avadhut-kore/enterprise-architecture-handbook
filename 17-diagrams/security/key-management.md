# Key Management Service (KMS) & Public Key Infrastructure (PKI)

Hierarchical Public Key Infrastructure (PKI) architecture and Hardware Security Module (HSM) root key lifecycle management.

## Mermaid Architecture Diagram

```mermaid
graph TB
    subgraph RootTier ["Tier 0: Root Infrastructure (Offline)"]
        RootCA["Enterprise Offline Root CA<br/>[FIPS 140-3 Level 4 HSM]"]
    end

    subgraph IntermediateTier ["Tier 1: Policy & Issuing CAs"]
        SubCA1["Internal Workload Issuing CA<br/>[Vault PKI Engine]"]
        SubCA2["Enterprise User Identity CA<br/>[Microsoft Active Directory CS]"]
        SubCA3["External Edge / Web Ingress CA<br/>[DigiCert / Let's Encrypt]"]

        RootCA -->|"Signs Intermediate (10-year validity)"| SubCA1
        RootCA -->|"Signs Intermediate"| SubCA2
        RootCA -->|"Signs Intermediate"| SubCA3
    end

    subgraph LeafCertificates ["Tier 2: Ephemeral End-Entity Certificates"]
        Leaf1["Service Mesh mTLS Certs<br/>[TTL: 24 Hours]"]
        Leaf2["User Smartcard / YubiKey PIV<br/>[TTL: 1 Year]"]
        Leaf3["Public Ingress Wildcard TLS<br/>[TTL: 90 Days]"]

        SubCA1 --> Leaf1
        SubCA2 --> Leaf2
        SubCA3 --> Leaf3
    end

    classDef root fill:#ffebee,stroke:#b71c1c,stroke-width:2px;
    classDef intermediate fill:#fff8e1,stroke:#f57f17,stroke-width:2px;
    classDef leaf fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    class RootCA root;
    class SubCA1,SubCA2,SubCA3 intermediate;
    class Leaf1,Leaf2,Leaf3 leaf;
```

## PlantUML Specification

```plantuml
@startuml
component "Offline Root CA (FIPS 140-3 Level 4)" as root
component "Vault Intermediate CA" as vaultCA
component "Active Directory CS" as adCA
component "Ephemeral Service Pods" as pods
component "Corporate Workstations" as pcs

root --> vaultCA : Signs Intermediate Certificate
root --> adCA : Signs Intermediate Certificate
vaultCA --> pods : Issues 24h mTLS Certificates
adCA --> pcs : Issues User Identity Certificates
@enduml
```

## Architectural Design Considerations

* **Offline Root CA**: Root CAs must remain physically or logically powered down, air-gapped from internal networks, and only activated for intermediate CA signing.
* **Automated Rotation**: Implement ACME protocol or Vault agent auto-renewal; eliminate manual certificate updates to eliminate outage risks.
* **Certificate Revocation**: Distribute lightweight Online Certificate Status Protocol (OCSP) stapling or short-lived certificates rather than large CRL files.

## Related Documentation & Patterns

* [Encryption](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/encryption.md)
* [Zero Trust](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/zero-trust.md)
* [Network Security](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/network-security.md)
