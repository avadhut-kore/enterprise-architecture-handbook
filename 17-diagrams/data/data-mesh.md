# Data Mesh Architecture (Domain-Oriented Decentralization)

Zhamak Dehghani's Data Mesh paradigm detailing the four core principles: Domain Ownership, Data as a Product, Self-Serve Data Platform, and Federated Computational Governance.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph DomainsTier ["1. Decentralized Domain Data Products"]
        subgraph CustomerDomain ["Customer Domain"]
            CustApp["Customer Microservice"]
            CustProduct[("Data Product: Customer 360<br/>(Clean Parquet on S3 + SQL API)")]
            CustApp --> CustProduct
        end

        subgraph OrderDomain ["Order & Checkout Domain"]
            OrderApp["Order Microservice"]
            OrderProduct[("Data Product: Completed Orders<br/>(Iceberg Table + Data Contract)")]
            OrderApp --> OrderProduct
        end

        subgraph LogisticsDomain ["Logistics Domain"]
            LogApp["Fleet Service"]
            LogProduct[("Data Product: Package Trajectories<br/>(Kafka Stream + Vector Index)")]
            LogApp --> LogProduct
        end
    end

    subgraph PlatformTier ["2. Self-Serve Data Infrastructure Platform"]
        Platform["Automated Platform Plane<br/>- Automated Storage & Compute Provisioning<br/>- Data Pipeline Templates (dbt / Spark)<br/>- Access Control & Encryption Engine"]
    end

    subgraph GovernanceTier ["3. Federated Computational Governance"]
        Gov["Global Governance Board<br/>- Standardized Data Contracts<br/>- Automated Policy as Code (OPA)<br/>- Enterprise Data Lineage & Quality Auditing"]
    end

    CustomerDomain -.-> Platform
    OrderDomain -.-> Platform
    LogisticsDomain -.-> Platform

    CustomerDomain -.-> Gov
    OrderDomain -.-> Gov
    LogisticsDomain -.-> Gov
```

## PlantUML Specification

```plantuml
@startuml
package "Domain Data Products" {
  node "Customer Domain" {
    [Customer App] --> [Customer 360 Data Product]
  }
  node "Order Domain" {
    [Order App] --> [Order Orders Data Product]
  }
}
package "Self-Serve Data Platform" {
  [Infrastructure Provisioner]
  [Data Product Catalog]
}
package "Federated Governance" {
  [Automated Data Contracts]
  [Policy as Code (OPA)]
}
@enduml
```

## Architectural Design Considerations

* **Domain Ownership**: Domain feature teams own analytical data pipelines and data products end-to-end, ending the central data engineering bottleneck.
* **Data as a Product**: Data products must have explicit SLAs, data contracts, documentation, and quality guarantees.
* **Federated Governance**: Standardize interoperability (e.g., Apache Iceberg, open data formats) through automated computational policies.

## Related Documentation & Patterns

* [Data Fabric](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data/data-fabric.md)
* [Data-Flow: Lakehouse](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/lakehouse.md)
* [Data-Flow: Data Lineage](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/data-lineage.md)
