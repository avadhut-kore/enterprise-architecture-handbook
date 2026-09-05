# Message Delivery Guarantees

## 1. The Three Delivery Semantics

```mermaid
quadrantChart
    title Message Delivery Guarantees
    x-axis "Low Throughput Overhead" --> "High Computational Overhead"
    y-axis "Data Loss Risk" --> "Zero Data Loss"
    quadrant-1 "Exactly-Once (Transactional Framing)"
    quadrant-2 "At-Least-Once (Industry Standard + Idempotency)"
    quadrant-3 "At-Most-Once (Fire-and-Forget)"
    quadrant-4 "Uncoordinated Messaging"
```

| Guarantee | Protocol Behavior | Failure Outcome | Production Fit |
| :--- | :--- | :--- | :--- |
| **At-Most-Once** | ACK before processing; no retries. | Messages may be permanently lost. | High-frequency sensor pings. |
| **At-Least-Once** | Process then ACK; producer retries. | Messages never lost, but duplicates occur. | Core enterprise transactions. |
| **Exactly-Once** | Atomic producer-broker-consumer transactions. | Exactly one state mutation occurs. | Financial ledger balance transfers. |
