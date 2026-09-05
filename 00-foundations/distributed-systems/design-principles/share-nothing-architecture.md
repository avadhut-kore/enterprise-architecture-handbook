# Distributed Design Principle: Share-Nothing Architecture (SN)

## 1. Core Principle Definition

A Share-Nothing Architecture is a distributed computing paradigm where every independent node operates autonomously, possessing its own private CPU, private memory, and private storage disks.

No two nodes share a centralized bus, shared memory (SMP), or shared disk array (SAN/NAS). Nodes coordinate exclusively by exchanging structured messages across the network.

---

## 2. Architectural Comparison

```
Shared-Disk Architecture (Bottlenecked):
[ Node 1 ] ──┬──► [ Central SAN / NAS Storage Array ] ◄──┬── [ Node 2 ]
             │            (Contention Point)             │

Share-Nothing Architecture (Linearly Scalable):
[ Node 1 + Local NVMe ] ◄── Network Messages ──► [ Node 2 + Local NVMe ]
```

---

## 3. Scaling Mechanics

- **Elimination of Resource Contention**: No lock coordination over shared memory buses or disk controllers.
- **Near-Linear Scalability**: Adding $N$ nodes increases throughput by approximately $N \times \text{Capacity}$, bounded only by network switch fabric bandwidth and distributed consensus coordination.
- **Exemplary Implementations**: Apache Cassandra, CockroachDB, Elasticsearch, Google Bigtable.

---

## 4. Trade-Offs & Challenges

- **Data Partitioning (Sharding) Complexity**: Data must be partitioned across nodes using hashing or range keys. Cross-node queries (scatter-gather) introduce network overhead.
- **Data Rebalancing Overhead**: Adding or removing nodes requires rebalancing partitions across the cluster over the network.
