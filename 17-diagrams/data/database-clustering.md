# Database Clustering & High-Availability Architecture

High-availability database clustering architecture detailing leader-follower topologies, Raft/Paxos consensus, automated health probing, and transparent failover.

## Mermaid Architecture Diagram

```mermaid
graph TB
    subgraph ClientLayer ["Application Layer"]
        AppSvc["Microservice Connection Pool"]
        Proxy["Database Proxy / Load Balancer<br/>(PgBouncer / ProxySQL / HAProxy)"]
        AppSvc --> Proxy
    end

    subgraph DBCluster ["Database High-Availability Cluster (Postgres + Patroni)"]
        PrimaryNode[("Primary Node (Read-Write)<br/>[Active Leader]")]
        Replica1[("Sync Standby Node 1 (Read-Only)<br/>[Zero Data Loss]")]
        Replica2[("Async Standby Node 2 (Read-Only)<br/>[Disaster Recovery]")]

        DCS["Distributed Consensus Store (etcd / Consul)<br/>[Raft Leader Election & Health Check]"]

        PrimaryNode -->|"Synchronous WAL Stream"| Replica1
        PrimaryNode -->|"Asynchronous WAL Stream"| Replica2

        PrimaryNode <--> DCS
        Replica1 <--> DCS
        Replica2 <--> DCS
    end

    Proxy -->|"Writes & Strong Reads"| PrimaryNode
    Proxy -->|"Read-Only Offload"| Replica1
    Proxy -.->|"Auto-reroute on Failover"| DCS
```

## PlantUML Specification

```plantuml
@startuml
component "App Connection Pool" as app
component "DB Proxy (PgBouncer)" as proxy
node "Database Cluster (Patroni + etcd)" {
  database "Primary (Read-Write)" as master
  database "Standby 1 (Sync Read)" as s1
  database "Standby 2 (Async Read)" as s2
  component "etcd Consensus (Raft)" as etcd
}

app -> proxy
proxy --> master : Write Traffic
proxy --> s1 : Read Traffic
master -> s1 : Sync WAL Stream
master -> s2 : Async WAL Stream
master <-> etcd : Leader Heartbeat
s1 <-> etcd : Leader Election Candidate
@enduml
```

## Architectural Design Considerations

* **Split-Brain Mitigation**: Always use an odd number of consensus nodes (minimum 3) to achieve quorum and avoid catastrophic split-brain leader elections.
* **Synchronous vs Asynchronous Replication**: Synchronous replication guarantees zero data loss (RPO=0) at the cost of higher write latency; asynchronous minimizes latency at the risk of slight data loss during hard crashes.
* **Connection Pooling**: Always place connection pooling proxies (PgBouncer) before database clusters to protect backends from client connection spikes.

## Related Documentation & Patterns

* [Database Sharding](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data/sharding.md)
* [Database Replication](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data/replication.md)
* [Data-Flow: Physical Data Flow](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data-flow/physical-data-flow.md)
