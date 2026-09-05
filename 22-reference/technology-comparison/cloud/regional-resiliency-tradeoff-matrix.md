# Technology Comparison: Regional Resiliency Trade-Off Matrix

## Executive Summary
This reference matrix evaluates the architectural trade-offs between single region multi-az vs multi-region.

---

## Architectural Comparison Matrix

| Dimension | Single Region Multi-AZ | Multi-Region Active-Passive | Multi-Region Active-Active |
| :--- | :--- | :--- | :--- |
| **Uptime SLA** | 99.99% (52 mins/yr) | 99.995% (26 mins/yr) | 99.999% (5 mins/yr) |
| **Target RTO** | Sub-minute | 5–15 minutes | Near-zero (< 1 min) |
| **Target RPO** | Zero (Synchronous quorum)| Seconds (Async replication) | Near-zero |
| **Cost Multiplier** | 1.0x (Baseline) | 1.6x | 2.3x–2.5x |
| **Distributed Complexity**| Low | Moderate | Extreme (Split-brain risk) |
