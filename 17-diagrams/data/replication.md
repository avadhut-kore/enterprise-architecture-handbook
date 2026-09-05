# Database Replication Strategies (Master-Slave vs Multi-Master)

Distributed database replication architectures comparing Single-Leader (Primary-Replica) with Multi-Leader and Leaderless (Dynamo-style) topologies.

## Mermaid Architecture Diagram

```mermaid
graph LR
    subgraph SingleLeader ["1. Single-Leader Replication (Active-Passive)"]
        Leader1[("Primary Node<br/>(Accepts All Writes)")]
        Follower1[("Read Replica 1<br/>(Read Only)")]
        Follower2[("Read Replica 2<br/>(Read Only)")]
        Leader1 -->|"Async Stream"| Follower1
        Leader1 -->|"Async Stream"| Follower2
    end

    subgraph MultiLeader ["2. Multi-Leader Replication (Active-Active Geo)"]
        LeaderUS[("Leader Node (US-East)<br/>Accepts Local Writes")]
        LeaderEU[("Leader Node (EU-West)<br/>Accepts Local Writes")]
        LeaderUS <-->|"Cross-Region Sync + Conflict Resolver"| LeaderEU
    end

    subgraph LeaderlessReplication ["3. Leaderless Quorum (Dynamo / Cassandra)"]
        Coord["Client Coordinator"]
        N1[("Node 1")]
        N2[("Node 2")]
        N3[("Node 3")]
        Coord -->|"Quorum Write: W=2"| N1
        Coord -->|"Quorum Write: W=2"| N2
        Coord -.-> N3
        note["Quorum Condition: R + W > N (Guarantees Strong Consistency)"]
    end
```

## PlantUML Specification

```plantuml
@startuml
package "Single-Leader" {
  [Primary (Writes)] --> [Replica 1 (Reads)]
  [Primary (Writes)] --> [Replica 2 (Reads)]
}
package "Multi-Leader" {
  [US Primary] <..> [EU Primary] : Bi-directional Replication
}
package "Leaderless Quorum" {
  [Coordinator] --> [Node A] : Write
  [Coordinator] --> [Node B] : Write
  [Coordinator] ..> [Node C] : Quorum (W=2 of 3)
}
@enduml
```

## Architectural Design Considerations

* **Read-After-Write Consistency**: In asynchronous single-leader setups, redirect clients to the primary node for 5-10 seconds after a write to prevent users from seeing stale data.
* **Conflict Resolution in Multi-Leader**: Multi-leader setups inevitably produce write conflicts; plan deterministic conflict resolution strategies (CRDTs or Last-Write-Wins).
* **Quorum Mathematics**: In leaderless systems, ensure $R + W > N$ where $N$ is replication factor, $W$ is write quorum, and $R$ is read quorum to guarantee reading the latest value.

## Related Documentation & Patterns

* [Database Clustering](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data/database-clustering.md)
* [Database Sharding](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data/sharding.md)
* [Data-Flow: Data Synchronization](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/data-synchronization.md)
