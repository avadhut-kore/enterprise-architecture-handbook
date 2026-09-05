# Architecture Modernization: Read-Write Splitting & Replica Routing

## 1. Architectural Objective & Context

Offload intensive read query traffic from a saturated primary database to horizontally scalable read replicas without exposing end users to dirty or stale reads immediately after submitting mutations.

---

## 2. Architectural Blueprint

```mermaid
flowchart TB
    subgraph ClientLayer [Application / ORM Tier]
        App[Application Service]
        RoutingProxy[Read-Write Connection Pool Proxy]
    end

    subgraph DatabaseTier [Replicated Database Architecture]
        PrimaryDB[(Primary Database - Writes Only)]
        Replica1[(Read Replica 1)]
        Replica2[(Read Replica 2)]
    end

    App --> RoutingProxy
    RoutingProxy -->|INSERT, UPDATE, DELETE| PrimaryDB
    PrimaryDB -->|Asynchronous WAL Replication| Replica1
    PrimaryDB -->|Asynchronous WAL Replication| Replica2

    RoutingProxy -->|SELECT (Standard Queries)| Replica1
    RoutingProxy -->|SELECT (Read-Your-Writes Window)| PrimaryDB
```

---

## 3. Solving the Replication Lag Problem: Read-Your-Writes Consistency

Under asynchronous database replication, replicas lag behind the primary by 10ms to 5000ms. If a user updates their profile and the page immediately reloads from a lagging replica, the user sees old data.

### Architectural Mitigations:
1. **Time-Based Pinning (The Grace Window)**:
   - After any write operation by a user session, set a session cookie or local token `last_write_timestamp`.
   - Any read query issued by that session within $T_{\text{grace}}$ (e.g., 5 seconds) is routed strictly to the **Primary Database**.
   - All subsequent reads after the grace window revert to Read Replicas.
2. **Replication Position Tracking (GTID / LSN)**:
   - The primary returns the Global Transaction Identifier (GTID) or Log Sequence Number (LSN) upon committing the write.
   - The read proxy checks whether a replica has caught up to the transaction's GTID; if not, it queries another replica or the primary.

---

## 4. Production Considerations

- **Health Checks & Lag Thresholds**: Replicas exceeding a configurable lag threshold (e.g., $> 2000\text{ms}$) must be automatically removed from the active read pool.
- **Connection Multiplexing**: Use connection pool proxies (e.g., PgBouncer, ProxySQL) to avoid thread exhaustion on database instances.
