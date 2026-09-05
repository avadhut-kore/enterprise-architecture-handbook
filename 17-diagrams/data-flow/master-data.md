# Master Data Management (MDM) & Golden Record Architecture

Entity resolution and master data governance architecture detailing deduplication, survivorship rules, and authoritative golden record distribution.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph InboundDuplicates ["Disparate Source Entities"]
        CRM["Salesforce CRM<br/>John Smith, 555-0199"]
        Billing["Billing App<br/>J. Smith, 555-0199, NYC"]
        Portal["Web Portal<br/>Johnathan Smith, jsmith@work.com"]
    end

    subgraph MDMPlatform ["Master Data Management (MDM Engine)"]
        MatchEngine["1. Matching & Fuzzy Deduplication Engine<br/>(Levenshtein / Jaro-Winkler Distance)"]
        RuleEngine["2. Survivorship Rules Engine<br/>(Most Recent / Most Authoritative System)"]
        GoldenStore[("3. Master Golden Record Store<br/>Golden Customer ID: CUST-88301<br/>- Legal Name: Johnathan Smith<br/>- Verified Phone: 555-0199<br/>- Verified Email: jsmith@work.com")]

        CRM --> MatchEngine
        Billing --> MatchEngine
        Portal --> MatchEngine
        MatchEngine --> RuleEngine
        RuleEngine --> GoldenStore
    end

    subgraph GoldenDistribution ["Syndication & Downstream Publishing"]
        ERP["SAP S/4HANA ERP"]
        Analytics["Enterprise Data Lakehouse"]
        CustomerPortal["Customer Mobile App"]

        GoldenStore -->|"Kafka Topic: master.customer.v1"| ERP
        GoldenStore --> Analytics
        GoldenStore --> CustomerPortal
    end

    classDef dup fill:#fbe9e7,stroke:#d84315,stroke-width:2px;
    classDef mdm fill:#fff3e0,stroke:#e65100,stroke-width:2px;
    classDef syn fill:#edf7ed,stroke:#2e7d32,stroke-width:2px;
    class CRM,Billing,Portal dup;
    class MatchEngine,RuleEngine,GoldenStore mdm;
    class ERP,Analytics,CustomerPortal syn;
```

## PlantUML Specification

```plantuml
@startuml
package "Source Feeds" {
  [CRM Contact]
  [Billing Profile]
  [E-Commerce Account]
}
package "MDM Core Engine" {
  component "Fuzzy Matching & Deduplication" as match
  component "Survivorship Logic" as rule
  database "Golden Customer Store" as golden
}
package "Downstream Distribution" {
  [Enterprise ERP]
  [Data Warehouse]
}

[CRM Contact] --> match
[Billing Profile] --> match
[E-Commerce Account] --> match
match --> rule : Candidate Cluster Identified
rule --> golden : Materialize Golden Record
golden --> [Enterprise ERP] : Push Verified Customer
golden --> [Data Warehouse] : Conformed Customer Dimension
@enduml
```

## Architectural Design Considerations

* **Deterministic vs Probabilistic Matching**: Use deterministic matching on unique keys (Tax ID, National ID) and probabilistic fuzzy matching on names and addresses.
* **Survivorship Rule Definition**: Specify field-level survivorship rules (e.g., billing address always wins from Billing; legal name always wins from Identity Verification).
* **Data Steward Exception Queue**: Route ambiguous matches (confidence scores between 70% and 85%) to human data steward review consoles.

## Related Documentation & Patterns

* [Operational Data Store](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/operational-data-store.md)
* [Data Lineage](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/data-lineage.md)
* [Data Governance Checklist](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/checklists.md)
