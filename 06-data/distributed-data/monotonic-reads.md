# Monotonic Reads Consistency

## 1. The "Time Travel" Anomaly
Monotonic reads prevent time-travel anomalies where a user observes a newer version of data, and subsequently observes an older version on a subsequent query.

```mermaid
sequenceDiagram
    autonumber
    actor User
    participant LB as Round-Robin Load Balancer
    participant R1 as Replica 1 (Up to date: Lag = 0ms)
    participant R2 as Replica 2 (Lagging: Lag = 800ms)
    
    User->>LB: Query Account Balance (Request 1)
    LB->>R1: Route to Replica 1
    R1-->>User: Balance: $500 (Timestamp: 10:00:05)
    
    User->>LB: Refresh Page (Request 2)
    LB->>R2: Route to Replica 2
    R2-->>User: Balance: $400 (Timestamp: 10:00:01) -> TIME TRAVEL ANOMALY!
```

---

## 2. Mitigation via Session Affinity
* **Hash-Based Client Routing**: Route requests using `Hash(user_id) % Total_Replicas` to pin a user session to a single replica.
* If that replica fails, failover to a new replica guaranteed to have equal or higher applied LSN.
