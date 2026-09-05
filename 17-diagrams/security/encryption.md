# Data Encryption Architecture: In-Transit, At-Rest & In-Use

Comprehensive cryptographic architectural patterns covering envelope encryption, transparent database encryption (TDE), TLS 1.3, and confidential computing.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph DataInTransit ["1. Data in Transit (Network Wire)"]
        UserClient["Browser / Mobile Client"]
        ALB["Application Load Balancer"]
        AppPod["Application Container"]
        UserClient -->|"TLS 1.3 (ECDHE-RSA-AES256-GCM)"| ALB
        ALB -->|"mTLS 1.3 (Internal Mesh)"| AppPod
    end

    subgraph EnvelopeEncryption ["2. Data at Rest (Envelope Cryptography)"]
        KMS["Enterprise KMS (AWS KMS / Cloud HSM)"]
        CMK["Customer Managed Key (Root KEK)"]
        DEK["Data Encryption Key (Plaintext)"]
        EncDEK["Encrypted Data Encryption Key (Ciphertext)"]
        PlaintextDoc["Sensitive Customer PII Document"]
        EncDoc["Encrypted Document Payload"]

        KMS --- CMK
        CMK -->|"Encrypts"| DEK
        DEK --> EncDEK
        DEK -->|"AES-256-GCM Encrypt"| PlaintextDoc
        PlaintextDoc --> EncDoc
        EncDoc --- EncDEK
        note1["Discard Plaintext DEK from RAM immediately after encryption"]
    end

    subgraph DataInUse ["3. Data in Use (Confidential Computing)"]
        TEE["Hardware Trusted Execution Environment (TEE)<br/>[AMD SEV-SNP / Intel SGX Enclave]"]
        EncMemory["Encrypted Memory Bus (Hardware Key)"]
        TEE --- EncMemory
    end

    AppPod -->|"Store Encrypted Object"| EncDoc
    AppPod -->|"Run Protected Computation"| TEE

    classDef transit fill:#e1f5fe,stroke:#039be5,stroke-width:2px;
    classDef rest fill:#fbe9e7,stroke:#d84315,stroke-width:2px;
    classDef inuse fill:#ede7f6,stroke:#512da8,stroke-width:2px;
    class UserClient,ALB,AppPod transit;
    class KMS,CMK,DEK,EncDEK,PlaintextDoc,EncDoc rest;
    class TEE,EncMemory inuse;
```

## PlantUML Specification

```plantuml
@startuml
package "In Transit" {
  [Client] --> [Ingress ALB] : TLS 1.3
  [Ingress ALB] --> [Service Pod] : mTLS
}
package "At Rest (Envelope Cryptography)" {
  [KMS Key (KEK)] --> [Data Key (DEK)] : Protects
  [Data Key (DEK)] --> [PII Payload] : AES-256-GCM
}
package "In Use" {
  [Secure Enclave (Intel SGX / AMD SEV)] : Memory Encryption
}
@enduml
```

## Architectural Design Considerations

* **Envelope Encryption**: Never encrypt mass payloads directly with root KMS keys; use KMS solely to generate and encrypt ephemeral Data Encryption Keys (DEKs).
* **Cryptographic Agility**: Support cipher suite upgrades and key migration paths without necessitating massive system refactoring.
* **Confidential Computing**: Implement hardware enclaves (AMD SEV / Intel SGX) when processing unencrypted data in multi-tenant untrusted clouds.

## Related Documentation & Patterns

* [Key Management](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/key-management.md)
* [Secrets Management](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/secrets-management.md)
* [Data Classification](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/data-classification.md)
