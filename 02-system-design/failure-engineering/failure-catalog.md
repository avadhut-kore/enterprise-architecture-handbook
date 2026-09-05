# Master Distributed Failure Mode Catalog

## Architectural Mitigation Matrix

```
+--------------------------+----------------------------+----------------------------+
| Failure Phenomenon       | Primary Manifestation      | Recommended Mitigation     |
+--------------------------+----------------------------+----------------------------+
| Cascading Collapse       | Chain-reaction service down| Circuit Breaker + Bulkhead |
| Split-Brain              | Conflicting master nodes   | Quorum Consensus + Fencing |
| Thundering Herd          | Mass concurrent cache miss | Distributed Lock (Singlefl)|
| Network Partition        | Lost inter-node connectivity| CAP-aligned Quorum (R+W>N) |
| Clock Drift              | LWW Silent Data Overwrite  | Hybrid Logical Clocks / GPS|
| Shard Hotspotting        | 1 saturated partition node | Salted Keys + L1 Caching   |
| Gray Node (Slow Node)    | P99 tail latency inflation | Hedged Requests + Ejection |
| Distributed Deadlock     | Indefinite thread hanging  | Strict Lock Ordering + TTL |
| Resource Starvation      | OutOfMemory / Thread Lock  | Bounded Queues + Backpress |
| Poison Pill Payload      | Worker crash loops         | Dead-Letter Queue (DLQ)    |
| Retry Storm              | Self-inflicted traffic surge| Exp Backoff + Full Jitter  |
| Regional Cloud Blackout  | Whole DC unavailable       | Multi-Region Active-Active |
+--------------------------+----------------------------+----------------------------+
```
