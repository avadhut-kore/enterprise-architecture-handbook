# Enterprise Data Classification & Handling Architecture

Data tier classification framework (Public, Internal, Confidential, Restricted) and automated compliance tagging pipelines.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph ClassTiers ["Data Classification Levels"]
        Pub["1. PUBLIC<br/>(Marketing, Public Docs)<br/>Cleartext OK, No Access Limit"]
        Int["2. INTERNAL<br/>(Internal Wiki, Org Charts)<br/>Employee Authenticated Access"]
        Conf["3. CONFIDENTIAL<br/>(Financials, Source Code)<br/>Role-Based Encryption, DLP Enforced"]
        Rest["4. RESTRICTED / REGULATED<br/>(PII, Cardholder Data, PHI)<br/>Hardware HSM Encrypted, Tokenized, WORM Logged"]
    end

    subgraph DataIngestionPipeline ["Automated Classification Pipeline"]
        IngestData["New Ingested Payload"]
        DLPScanner["Automated DLP / Macie Scanner"]
        Classifier["Regex & ML Metadata Tagger"]
        TargetStore["Encrypted Storage Bucket"]

        IngestData --> DLPScanner
        DLPScanner -->|"Detects SSN/Credit Card"| Classifier
        Classifier -->|"Apply Tag: SecurityClass=Restricted"| TargetStore
    end

    TargetStore -.-> Rest

    classDef c1 fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef c2 fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    classDef c3 fill:#fff8e1,stroke:#f57f17,stroke-width:2px;
    classDef c4 fill:#ffebee,stroke:#b71c1c,stroke-width:2px;
    class Pub c1;
    class Int c2;
    class Conf c3;
    class Rest c4;
```

## PlantUML Specification

```plantuml
@startuml
package "Data Classification Spectrum" {
  [Public] -right-> [Internal]
  [Internal] -right-> [Confidential]
  [Confidential] -right-> [Restricted / PII]
}
note bottom of [Restricted / PII]
  * Field-level encryption
  * PCI-DSS / HIPAA scoping
  * Audit logging for every read
  * Strict DLP protection
end note
@enduml
```

## Architectural Design Considerations

* **Automated Data Discovery**: Leverage automated classifiers (e.g., AWS Macie, Microsoft Purview) to continually scan S3 buckets and databases for unclassified PII.
* **Tokenization of Restricted Data**: Replace sensitive PANs or SSNs with non-reversible random tokens; store raw data only in an isolated PCI vault.
* **Retention and Deletion**: Enforce automated data lifecycle policies that permanently shred confidential and restricted data once mandatory retention periods expire.

## Related Documentation & Patterns

* [Encryption](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/encryption.md)
* [Trust Boundaries](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/trust-boundaries.md)
* [Secrets Management](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/secrets-management.md)
