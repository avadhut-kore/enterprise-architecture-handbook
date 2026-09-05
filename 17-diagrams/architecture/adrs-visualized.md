# Visual Architecture Decision Records (ADRs) & Trade-off DAG

Architectural decision topology modeling decision trees, context drivers, evaluated alternatives, chosen solutions, and downstream structural consequences.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph ContextDriver ["Business Context & Drivers"]
        Driver1["Requirement: Sub-50ms Global Latency"]
        Driver2["Requirement: Multi-Region Active-Active Compliance"]
    end

    subgraph ADR004 ["ADR-004: Primary Database Selection"]
        DecisionNode{"Evaluate Distributed Database Candidates"}
        Alt1["Option A: Amazon Aurora Global Database<br/>(Pros: Fast read replicas; Cons: Single-region writes)"]
        Alt2["Option B: CockroachDB Dedicated<br/>(Pros: Multi-region writes, Raft consensus; Cons: Operational overhead)"]
        Alt3["Option C: Cassandra / DynamoDB Global<br/>(Pros: High throughput; Cons: Eventual consistency, no ACID joins)"]
        
        Chosen["DECISION: CockroachDB Dedicated<br/>Status: ACCEPTED"]

        DecisionNode --> Alt1
        DecisionNode --> Alt2
        DecisionNode --> Alt3
        Alt2 --> Chosen
    end

    subgraph DownstreamConsequences ["Consequences & Downstream ADRs"]
        Cons1["Positive: Guaranteed Serializable ACID across US & EU"]
        Cons2["Tradeoff: Higher write latency (70ms) due to cross-region Raft quorum"]
        ADR008["Downstream ADR-008: Asynchronous Order Queuing Strategy"]
        
        Chosen --> Cons1
        Chosen --> Cons2
        Cons2 --> ADR008
    end

    Driver1 --> DecisionNode
    Driver2 --> DecisionNode

    classDef drv fill:#fff8e1,stroke:#f57f17,stroke-width:2px;
    classDef opt fill:#fbe9e7,stroke:#d84315,stroke-width:2px;
    classDef acc fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    class ContextDriver drv;
    class Alt1,Alt3 opt;
    class Chosen acc;
```

## PlantUML Specification

```plantuml
@startuml
rectangle "Business Drivers: Low Latency & Active-Active" as drivers
node "ADR-004: Distributed Database Evaluation" as adr {
  [Option A: Aurora Global]
  [Option B: CockroachDB]
  [Option C: DynamoDB]
}
node "Accepted: CockroachDB" as accepted
rectangle "Consequence: Must handle cross-region write latency" as cons
rectangle "Triggers ADR-008: Async Queueing" as adr8

drivers --> adr
adr --> accepted
accepted --> cons
cons --> adr8
@enduml
```

## Architectural Design Considerations

* **Explicit Trade-off Documentation**: Document not only why an architecture option was selected, but explicitly why alternative candidates were rejected.
* **Traceable Impact**: Link subsequent decisions to the consequences created by earlier ADRs.
* **Versioned in Repository**: Store ADR Markdown files in Git (`docs/adrs/`) and review them via formal pull request discussions.

## Related Documentation & Patterns

* [Trade-off Matrix](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/architecture/tradeoff-matrix.md)
* [System Architecture Document](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/architecture/system-architecture-document.md)
* [Architecture Review Checklist](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/architecture/checklists.md)
