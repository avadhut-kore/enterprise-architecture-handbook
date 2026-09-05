# System Design & Capacity Engineering Calculators

Precise mathematical modeling and capacity sizing differentiate amateur technology guesses from production-grade enterprise architecture.

This directory provides standardized computational formulas, reference sizing worksheets, headroom multipliers, and capacity estimation models for production systems.

---

## Catalog of Architectural Calculators

| Calculator | Sizing Focus | Mathematical Model |
| :--- | :--- | :--- |
| [Traffic Calculator](traffic-calculator.md) | Request Rates & Concurrency | Peak-to-average multipliers & Little's Law |
| [Storage Calculator](storage-calculator.md) | Multi-Year Data Growth | Record serialization, replication factor & indexing |
| [Bandwidth Calculator](bandwidth-calculator.md) | Network Ingress/Egress | Bitrate, concurrent streams & CDN offload ratios |
| [Cache Capacity Calculator](cache-calculator.md) | In-Memory Working Set | Pareto 80/20 principle & memory metadata overhead |
| [Database Sizing Calculator](database-sizing-calculator.md) | IOPS, CPU & Shard Sizing | Read/Write IOPS, B-Tree overhead & connection pools |
| [Availability Calculator](availability-calculator.md) | Uptime, MTBF & MTTR | Series/parallel availability modeling & composite SLAs |
| [Latency Budget Calculator](latency-budget-calculator.md) | P99 SLA Decomposition | Per-hop network, gateway, DB & processing budgets |
| [Cost Estimator](cost-estimator.md) | TCO Cloud Infrastructure | Compute, storage, egress bandwidth & licensing models |
