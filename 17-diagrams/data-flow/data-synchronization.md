# Multi-Region Data Synchronization & Conflict Resolution

Active-Active geo-replicated data synchronization architecture detailing Conflict-Free Replicated Data Types (CRDTs), Last-Write-Wins (LWW), and vector clocks.

## Mermaid Architecture Diagram

```mermaid
graph LR
    subgraph RegionUS ["Region 1: US-East (Primary App & Store)"]
        AppUS["App Service Pod (US)"]
        StoreUS[("CockroachDB / Cassandra Node<br/>[State: v1, Vector: {US:1, EU:0}]")]
        AppUS -->|"Write Mutation"| StoreUS
    end

    subgraph InterRegionSync ["Cross-Region Replication Bus"]
        SyncBus["Dedicated Encrypted Cloud Interconnect / DirectConnect<br/>(Async Replication Stream)"]
        StoreUS <-->|"Bidirectional Replication"| SyncBus
    end

    subgraph RegionEU ["Region 2: EU-West (Local App & Store)"]
        AppEU["App Service Pod (EU)"]
        StoreEU[("CockroachDB / Cassandra Node<br/>[State: v1, Vector: {US:0, EU:1}]")]
        AppEU -->|"Write Mutation"| StoreEU
        SyncBus <-->|"Bidirectional Replication"| StoreEU
    end

    subgraph ConflictEngine ["Distributed Conflict Resolution"]
        CRDT["State-based CRDT Merge Engine<br/>(Grow-Only Sets / Observed-Removed Sets)"]
        LWW["Timestamp Arbiter (Hybrid Logical Clocks - HLC)"]
        StoreUS -.-> CRDT
        StoreEU -.-> CRDT
        CRDT --> LWW
    end

    classDef us fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    classDef eu fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px;
    classDef con fill:#fff8e1,stroke:#f57f17,stroke-width:2px;
    class AppUS,StoreUS us;
    class AppEU,StoreEU eu;
    class SyncBus,CRDT,LWW con;
```

## PlantUML Specification

```plantuml
@startuml
package "Region US-East" {
  node "App US" as appUS
  database "DB Node US" as dbUS
}
package "Region EU-West" {
  node "App EU" as appEU
  database "DB Node EU" as dbEU
}
component "Hybrid Logical Clock (HLC) & CRDT Resolver" as resolver

appUS -> dbUS : Write(Key, Val_A)
appEU -> dbEU : Write(Key, Val_B)
dbUS <-> dbEU : Asynchronous Cross-Region Sync
dbUS --> resolver : Concurrent Write Detected
dbEU --> resolver : Concurrent Write Detected
resolver -> resolver : Apply Deterministic Resolution (HLC / CRDT)
resolver --> dbUS : Converged Value
resolver --> dbEU : Converged Value
@enduml
```

## Architectural Design Considerations

* **Hybrid Logical Clocks (HLC)**: Avoid pure physical NTP clocks for ordering distributed events; use HLCs to guarantee causality without clock skew anomalies.
* **Conflict-Free Data Types (CRDTs)**: For additive or counter metrics (e.g., shopping cart items, view counts), use CRDTs to achieve mathematically guaranteed convergence without data loss.
* **Data Sovereignty Compliance**: Ensure synchronization filters strictly exclude EU GDPR-protected fields from replicating across foreign border regions.

## Related Documentation & Patterns

* [Data Migration](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/data-migration.md)
* [Physical Data Flow](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/physical-data-flow.md)
* [PII Data Flow](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/pii-flow.md)
