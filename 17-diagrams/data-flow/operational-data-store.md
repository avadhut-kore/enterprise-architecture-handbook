# Operational Data Store (ODS) Integration Architecture

Near-real-time operational consolidation store bridging fragmented operational transaction engines and analytical reporting platforms.

## Mermaid Architecture Diagram

```mermaid
graph LR
    subgraph OperationalSilos ["Fragmented Operational Systems"]
        CoreBank[("Core Banking Engine<br/>(Mainframe COBOL/DB2)")]
        LoanApp[("Loan Origination<br/>(PostgreSQL)")]
        CreditCard[("Credit Card Management<br/>(Oracle RAC)")]
    end

    subgraph IntegrationStream ["Low-Latency Ingestion"]
        CDC["Log-Based CDC Sync"]
        CoreBank -->|"MQ Series / CDC"| CDC
        LoanApp -->|"Debezium"| CDC
        CreditCard -->|"GoldenGate"| CDC
    end

    subgraph OperationalDataStore ["Central ODS (MongoDB / PostgreSQL)"]
        ODS[("Unified ODS Cluster<br/>- Near-Real-Time Customer 360 View<br/>- Normalized Current Operational State<br/>- Retention: 30-90 Days Active Data")]
        CDC -->|"Near-Real-Time Updates (<2s lag)"| ODS
    end

    subgraph OperationalUsers ["Operational Workloads"]
        CSR["Customer Service Representative Portal"]
        Fraud["Real-Time Fraud Scoring Engine"]
        MobileApp["Mobile Banking Dashboard API"]

        ODS --> CSR
        ODS --> Fraud
        ODS --> MobileApp
    end

    classDef silo fill:#fbe9e7,stroke:#d84315,stroke-width:2px;
    classDef ods fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    classDef user fill:#edf7ed,stroke:#2e7d32,stroke-width:2px;
    class CoreBank,LoanApp,CreditCard silo;
    class ODS ods;
    class CSR,Fraud,MobileApp user;
```

## PlantUML Specification

```plantuml
@startuml
database "Core Banking DB2" as db1
database "Loan Postgres" as db2
database "Credit Card Oracle" as db3
queue "CDC Streaming Bus" as cdc
database "Operational Data Store (ODS)" as ods
actor "Customer Service Agent" as csr
component "Mobile Banking API" as api

db1 -> cdc : Emit Changes
db2 -> cdc : Emit Changes
db3 -> cdc : Emit Changes
cdc -> ods : Stream Updates (< 2s latency)
ods -> csr : Single Consolidated Customer Profile
ods -> api : Account Summary API Response
@enduml
```

## Architectural Design Considerations

* **Operational Focus**: An ODS is optimized for transactional lookup queries (Customer 360) rather than multi-year historical trend aggregation.
* **Low Replication Latency**: Ensure synchronization lag between core transactional databases and the ODS remains strictly under 2 seconds.
* **Read Offloading**: Direct high-volume operational queries away from legacy core transactional mainframes to preserve core transaction throughput.

## Related Documentation & Patterns

* [Change Data Capture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/cdc.md)
* [Data Lake](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/data-lake.md)
* [Master Data Management](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/master-data.md)
