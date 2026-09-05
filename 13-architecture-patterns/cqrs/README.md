# Command Query Responsibility Segregation (CQRS) Pattern

## Overview

Command Query Responsibility Segregation (CQRS) is an architectural pattern that strictly segregates the data models and execution paths used to mutate state (**Commands**) from the data models and execution paths used to read state (**Queries**). Originally conceptualized by Greg Young based on Bertrand Meyer's Command-Query Separation (CQS) principle, CQRS recognizes that in complex enterprise systems, the optimal data structure for write transactions is almost never the optimal data structure for high-performance reading and reporting.

---

## Architectural Topology

```mermaid
flowchart TD
    Client["Client Application"]
    
    subgraph WriteSide["Command Side (Write Model)"]
        CmdAPI["Command API Handler"]
        CmdHandler["Command Handler & Domain Invariants"]
        WriteDB[("Write Database (OLTP)<br/>Normalized (3NF) PostgreSQL<br/>Optimized for ACID Transactions")]
        
        CmdAPI --> CmdHandler --> WriteDB
    end

    subgraph SyncChannel["Asynchronous Synchronization"]
        Outbox["Outbox / Change Data Capture (CDC)<br/>Debezium / Kafka Event Stream"]
        WriteDB -.-> Outbox
    end

    subgraph ReadSide["Query Side (Read Model)"]
        Projector["Event Projector / Materializer"]
        ReadDB[("Read Database (OLAP / Search / Cache)<br/>Denormalized Redis / Elasticsearch<br/>Optimized for Fast Queries")]
        QueryAPI["Query API Handler"]
        
        Outbox --> Projector --> ReadDB
        QueryAPI --> ReadDB
    end

    Client -->|HTTP POST/PUT: /commands/place-order| CmdAPI
    Client -->|HTTP GET: /queries/orders/{id}| QueryAPI
```

---

## The Core Duality: Commands vs. Queries

| Attribute | The Command Model (Writes) | The Query Model (Reads) |
|:---|:---|:---|
| **Intent** | Perform a business action and mutate system state | Retrieve formatted data without altering state (Side-Effect Free) |
| **Data Schema** | Highly normalized (3NF) relational tables or Event Store | Flat, denormalized, pre-joined documents or key-value structures |
| **Invariants** | Enforces deep business rules, concurrency locks, validations | Zero validation logic; pure projection and projection filters |
| **Consistency** | Immediate linearizable ACID consistency | Eventual consistency (slight milliseconds/seconds projection lag) |
| **Scaling Profile** | Scaled vertically or partitioned by entity ID (e.g. `order_id`) | Scaled horizontally with massive read-replica caching |

---

## Synchronization Mechanisms: Bridging Write to Read

The Query model must be updated whenever the Command model commits changes:

1. **Synchronous Dual-Write (Anti-Pattern)**: The Command handler writes to PostgreSQL and then immediately executes an `INSERT` into Elasticsearch in the same code block. If Elasticsearch fails, the transaction is half-committed, causing permanent data divergence.
2. **Transactional Outbox with CDC (Recommended Production Standard)**: The Command handler writes only to PostgreSQL, including an event record in an `outbox` table. A background CDC engine (Debezium) reads the transaction log and publishes an event to Kafka. A read-side **Projector service** consumes the event and updates the read model.
3. **Database Native Replication**: Some databases support automated read-replica projections or materialized views natively.

---

## When to Apply CQRS

- **High Read-to-Write Asymmetry**: Systems with a 100:1 or 1000:1 read/write ratio (e.g., e-commerce product catalogs, social media feeds, property listings).
- **Complex Screen Projections**: When rendering a single frontend dashboard requires joining 10+ relational tables across different domains. Pre-computing that screen into a single JSON document in MongoDB or Redis eliminates runtime database CPU thrashing.
- **Complex Domain Invariants on Mutation**: Systems where write business logic requires heavy validation and aggregate locking, but reads must remain instantaneous (e.g., flight seat reservations).

## When NOT to Apply CQRS (Over-Engineering Warning)

- **Standard CRUD Applications**: Simple back-office administration portals, internal employee directories, and straightforward CRUD workflows do not justify CQRS.
- **Strict Real-Time Read-Your-Own-Writes**: If a user updates their profile and immediately redirects to a page that will crash if the update hasn't propagated, eventual consistency introduces significant frontend complexity.

---

## Mitigating Eventual Consistency in the Frontend

To prevent users from thinking their update failed when querying an eventually consistent read model:
1. **Optimistic UI Updates**: The client frontend updates its local state cache (React Query, Redux) immediately upon receiving a `202 Accepted` or `200 OK` from the Command API, without waiting for the Query model to reflect the change.
2. **Versioning / ETags**: Include a `version` number or timestamp in the command response. The frontend includes this version in subsequent queries, prompting the query handler to check the write database if the read model has not yet caught up.
