# Event Sourcing Pattern

## Overview

Event Sourcing is an architectural pattern in which the state of an application or domain entity is not persisted as a mutable record (e.g., updating a row in an SQL table with current balances), but rather as an **append-only, immutable sequence of business events**. Every state change in the system is captured as an event and appended to an **Event Store**. 

To determine the current state of an entity at any point in time, the system **replays** all historical events associated with that entity from inception to the present.

---

## Traditional CRUD vs. Event Sourcing

```mermaid
flowchart TD
    subgraph TraditionalCRUD["Traditional CRUD (State Overwriting)"]
        T1["INSERT Account: balance = $100"] --> T2["UPDATE Account: balance = $150"]
        T2 --> T3["UPDATE Account: balance = $120"]
        T3 --> TState["Current Row in DB: [Account: 101, Balance: $120]<br/>The history of HOW balance reached $120 is LOST forever!"]
    end

    subgraph EventSourcingModel["Event Sourcing (Immutable Append-Only Log)"]
        E1["Event 1: AccountOpened (initial_deposit: $100, timestamp: t0)"]
        E2["Event 2: MoneyDeposited (amount: $50, timestamp: t1)"]
        E3["Event 3: MoneyWithdrawn (amount: $30, timestamp: t2)"]
        E1 --> E2 --> E3
        E3 --> EState["Current State = Replay(E1 + E2 + E3) = $120<br/>Complete audit trail and temporal history preserved!"]
    end
```

---

## Architectural Topology: Event Store & Snapshotting

```mermaid
sequenceDiagram
    autonumber
    participant App as Banking Application
    participant Snap as Snapshot Store
    participant ES as Event Store (Append-Only)

    Note over App: Client requests: Withdraw $50 from Account 101
    App->>Snap: 1. Fetch Latest Snapshot (Version 100: Balance $200)
    App->>ES: 2. Load Events after Version 100 (Events 101-105)
    App->>App: 3. Hydrate Aggregate State ($200 + $20 - $10 = $210)
    App->>App: 4. Validate Business Invariants ($210 >= $50: OK!)
    App->>ES: 5. Append New Event: MoneyWithdrawn (Amount: $50, ExpectedVersion: 105)
    ES-->>App: 6. Event Appended Successfully (New Version: 106)
```

---

## Core Capabilities of Event Sourcing

1. **Complete, Verifiable Audit Trail**: Because the Event Store is strictly append-only, no human or system error can overwrite or erase past transactions. This is the foundational model for accounting ledgers and financial systems.
2. **Temporal Querying & Time Travel**: An architect can recreate the exact state of the entire system at any given second in history (e.g., "What was Customer 42's portfolio balance at 11:15:32 AM on October 14th?").
3. **What-If Analysis & Retrospective Modeling**: New business models or fraud detection algorithms can be tested by replaying 5 years of historical events through a newly coded projection engine to observe how it would have behaved.

---

## Performance Optimization: Snapshotting

Replaying 100,000 historical events to hydrate a long-lived aggregate (e.g., an active bank account open for 10 years) introduces unacceptable latency:
- **Snapshots**: Every $N$ events (e.g., every 100 events), the system serializes the aggregate's current state into a Snapshot table.
- **Hydration**: The aggregate loads the latest snapshot ($N=100$) and replays only the events that occurred after the snapshot ($N=101, 102 \dots$).

---

## Pairing Event Sourcing with CQRS

Event Sourcing is almost universally paired with **CQRS**:
- **Write Side**: The Event Store acts as the single source of truth, accepting append-only events.
- **Read Side**: Background projection services subscribe to the Event Store log and materialize read-optimized projections in Elasticsearch, PostgreSQL, or Redis.

---

## Operational Realities & Complexities

| Operational Challenge | Root Cause | Production Mitigation Strategy |
|:---|:---|:---|
| **Schema Evolution** | Event schemas change over 5 years (fields added, renamed, or deprecated) | Implement **Upcasting** in the event deserializer: an upcaster transforms legacy v1 event schemas into modern v3 schemas in memory without modifying the immutable disk log. |
| **GDPR "Right to be Forgotten"** | GDPR mandates erasing customer PII, but event logs are strictly immutable | **Crypto-Shredding**: Encrypt each user's PII within event payloads using an individual, user-specific encryption key in a key vault. To delete the user, destroy the key; the events remain structurally intact but mathematically unreadable. |
| **Optimistic Concurrency** | Two concurrent users attempt to mutate the same aggregate simultaneously | Append operations specify `expected_version`. If a concurrent write incremented the version first, the second write fails with a concurrency exception and retries. |
