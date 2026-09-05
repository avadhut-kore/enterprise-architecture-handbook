# System Design Interview: Deep Dive & Specialization

## 1. Directing the Deep Dive

In senior interviews, the interviewer will say: *"Now let's zoom into component X. How does this scale to 100x traffic?"*

Common deep-dive topics:
1. **Database Sharding & Hotspotting**: How to partition data, handle resharding, and manage viral celebrity keys.
2. **Concurrency & Race Conditions**: Distributed locking (Redlock), optimistic locking (`version` column), and state machines.
3. **Real-Time Communication**: WebSocket connection management, edge gateways (Slack's Flannel pattern), and Redis pub/sub.
4. **Failure Recovery**: What happens if the cache dies? What happens if the network partitions?

---

## 2. Framework for Answering Deep Dives

```
1. Identify the Bottleneck: "At 100k QPS, single-node MySQL will exhaust IOPS."
2. Propose 2 Architectural Options:
   - Option A: Read replicas with cache-aside.
   - Option B: Horizontal sharding by user_id.
3. Compare Trade-Offs: "Option A handles read spikes, but write QPS is still bounded. Since our write QPS is high, Option B is necessary."
4. Detail the Chosen Solution: "We will shard using consistent hashing with virtual nodes."
```
