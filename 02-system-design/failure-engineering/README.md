# Distributed Systems Failure Engineering

In large-scale distributed architectures, failures are not rare anomalies; they are continuous, guaranteed mathematical certainties. At hyperscale across thousands of nodes, disks, network switches, and cloud availability zones, components are constantly failing, degrading, or partitioning.

Failure Engineering is the discipline of architecting systems that survive partial degradations without catastrophic total system failure, avoiding cascading collapse, data corruption, and split-brain scenarios.

---

## Failure Engineering Catalog

| Document | Core Phenomenon | Primary Architectural Defense |
| :--- | :--- | :--- |
| [Failure Modes](failure-modes.md) | Taxonomy of Distributed Faults | Defense-in-Depth, Redundancy, Fail-Safe Defaults |
| [Cascading Failures](cascading-failures.md) | Chain-reaction outages across tiers | Circuit Breakers, Bulkheads, Load Shedding |
| [Split-Brain](split-brain.md) | Concurrent divergent primaries post-partition | Quorum Consensus, Fencing Tokens, STONITH |
| [Thundering Herd](thundering-herd.md) | Mass concurrent spikes hitting single resources | Distributed Mutex (Single-flight), Cache Jitter |
| [Network Partitions](network-partitions.md) | Communication severance between subnets | CAP/PACELC Alignment, Heartbeats, Vector Clocks |
| [Byzantine Faults](byzantine-faults.md) | Arbitrary or malicious corrupted nodes | BFT Consensus, Cryptographic Signature Verification |
| [Clock Drift](clock-drift.md) | Desynchronization of physical server quartz clocks | TrueTime (GPS/Atomic), Logical / Hybrid Vector Clocks |
| [Hotspots](hotspots.md) | Severe traffic skew on individual partition keys | Salted Keys, Scatter-Gather Caching, Dynamic Splitting |
| [Slow Nodes (Gray Failures)](slow-nodes.md) | Degradation without hard process crashes | Hedged Requests, Aggressive Deadlines, Outlier Eviction |
| [Deadlocks](deadlocks.md) | Circular wait conditions across distributed locks | Strict Global Lock Ordering, Leases, Deadlock Detectors |
| [Resource Exhaustion](resource-exhaustion.md) | OOM, file descriptor, and thread starvation | Strict Concurrency Caps, Worker Pools, Memory Limits |
| [Poison Pills](poison-pills.md) | Malformed payloads crashing worker threads | Dead-Letter Queues (DLQ), Payload Schema Validation |
| [Retry Storms](retry-storms.md) | Self-inflicted amplification of downstream failures | Exponential Backoff with Full Jitter, Circuit Breakers |
| [Blast Radius](blast-radius.md) | Failure containment and boundary isolation | Cell-Based Architecture, Multi-Region Failure Domains |
| [Chaos Testing](chaos-testing.md) | Proactive fault injection in staging & prod | Chaos Monkey, Latency Injection, Partition Emulation |
| [Post-Mortem Analysis](post-mortem-analysis.md) | Blameless root cause investigation (RCA) | 5 Whys, Timeline Reconstruction, Corrective Actions |
| [Failure Catalog](failure-catalog.md) | Master reference matrix of distributed failure modes | Comprehensive architectural mitigation cheat-sheet |
