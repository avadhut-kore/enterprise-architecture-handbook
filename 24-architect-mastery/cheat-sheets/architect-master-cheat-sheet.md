# Architect Master Cheat Sheet

### 1. Latency Numbers Every Architect Must Know

| Operation | Typical Latency | Human-Scaled Analogy |
| :--- | :--- | :--- |
| **L1 cache reference** | 0.5 ns | 1 heart beat |
| **L2 cache reference** | 7 ns | 14 heart beats |
| **Main memory (RAM) reference** | 100 ns | 3.3 minutes |
| **Read 1 MB sequentially from memory** | 250,000 ns (250 µs) | 5.8 days |
| **Read 1 MB sequentially from SSD** | 1,000,000 ns (1 ms) | 23 days |
| **Send packet CA to Netherlands & back** | 150,000,000 ns (150 ms) | 9.5 years |
| **Reboot virtual machine** | 30,000,000,000 ns (30 s) | 1,900 years |

---

### 2. Back-of-the-Envelope Capacity Rules of Thumb

- **Requests to QPS**: 1 Million requests per day $pprox$ 12 requests per second (avg).
- **Peak Multiplier**: Peak traffic is typically $3	imes$ to $5	imes$ average QPS.
- **Storage Rules**: 1 Million rows with 1 KB payload $pprox$ 1 GB raw storage (add $2.5	imes$ for indexes, WAL, and replication).
- **Network Bandwidth**: 10,000 QPS with 2 KB payload $pprox$ 20 MB/sec $pprox$ 160 Mbps.

---

### 3. Golden Architectural Heuristics

1. **CAP / PACELC**: You cannot choose CA in distributed systems; network partitions are physical inevitabilities.
2. **End-to-End Principle**: Reliability and security must be validated end-to-end; intermediate network layers cannot guarantee correctness.
3. **Little's Law**: $L = \lambda 	imes W$ (Concurrent requests = Arrival rate $	imes$ Average latency).
4. **Amdahl's Law**: System speedup is strictly limited by the sequential fraction of the task.

## Related Modules
- [Master System Design Methodology](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/system-design/master-system-design-methodology.md)
- [Master Trade-offs Library](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/trade-offs/master-trade-offs-library.md)
