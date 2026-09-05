# Database Sharding & Horizontal Partitioning Architecture

Horizontal database sharding architecture detailing hash-based vs range-based partition keys, routing middleware, and re-sharding strategies.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph ClientTier ["Application Ingress"]
        App["App Pod: Insert User(id=88321)"]
        Router["Sharding Router / Query Coordinator<br/>(Vitess / Citus / App Sharding Logic)"]
        App --> Router
    end

    subgraph ShardingFunction ["Consistent Hashing & Key Routing"]
        HashCalc["HashFunction: CRC32(user_id) % 3"]
        Router --> HashCalc
    end

    subgraph ShardInstances ["Horizontal Database Shards"]
        Shard0[("Shard 0 (PostgreSQL)<br/>Range: Hash 0..0x5555<br/>[Users 0 - 33%]")]
        Shard1[("Shard 1 (PostgreSQL)<br/>Range: Hash 0x5556..0xAAAA<br/>[Users 34 - 66%]")]
        Shard2[("Shard 2 (PostgreSQL)<br/>Range: Hash 0xAAAB..0xFFFF<br/>[Users 67 - 100%]")]
    end

    HashCalc -->|"Partition 0"| Shard0
    HashCalc -->|"Partition 1"| Shard1
    HashCalc -->|"Partition 2"| Shard2
```

## PlantUML Specification

```plantuml
@startuml
component "App Service" as app
component "Sharding Router (Vitess)" as router
database "Shard 0 (Users A-H)" as s0
database "Shard 1 (Users I-P)" as s1
database "Shard 2 (Users Q-Z)" as s2

app -> router : SELECT * FROM users WHERE id=123
router -> router : Compute Hash(id) -> Shard 1
router -> s1 : Execute Targeted Query
s1 -> router : Result Set
router -> app : Return Row
@enduml
```

## Architectural Design Considerations

* **Shard Key Selection**: Choose high-cardinality shard keys (e.g., `user_id`, `tenant_id`) that distribute read and write traffic evenly across all nodes.
* **Cross-Shard Queries**: Avoid queries that do not include the shard key; cross-shard scatter-gather queries introduce massive latency and resource strain.
* **Re-sharding Complexity**: Use consistent hashing algorithms to ensure that adding new shards requires migrating only $K/N$ keys rather than reshuffling the entire database.

## Related Documentation & Patterns

* [Database Clustering](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data/database-clustering.md)
* [Database Replication](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data/replication.md)
* [Data Architecture Checklist](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/data/checklists.md)
