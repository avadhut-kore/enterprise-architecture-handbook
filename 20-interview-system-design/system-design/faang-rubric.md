# FAANG / Big Tech Scoring Rubric for System Design

## Detailed Competency Dimension Scoring

```
[ Scoring Scale: 1 = Strong No-Hire | 2 = No-Hire | 3 = Lean Hire | 4 = Hire | 5 = Strong Hire ]

Dimension 1: Requirements & Scope Formulation
- [1] Ignores constraints; makes assumptions without checking.
- [3] Asks basic questions; clarifies QPS when prompted.
- [5] Proactively discovers edge cases, defines explicit boundaries, and quantifies SLAs.

Dimension 2: Scalability & Distributed Systems
- [1] Single monolithic server and DB for 100M users.
- [3] Standard horizontal scaling, basic caching, and read replicas.
- [5] Flawless sharding keys, consistent hashing, replication lag mitigation, and hot-key defense.

Dimension 3: Resilience & Fault Tolerance
- [1] Assumes infrastructure never fails.
- [3] Mentions backups and multiple servers.
- [5] Analyzes network partitions, split-brain, circuit breakers, and disaster recovery RTO/RPO.

Dimension 4: Communication & Leadership
- [1] Argumentative or completely silent.
- [3] Answers questions politely; passive.
- [5] Guides the interviewer like a peer architect; welcomes feedback; manages time efficiently.
```
