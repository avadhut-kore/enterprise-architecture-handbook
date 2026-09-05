# System Design Checklist: Scale & Capacity Estimation

## 1. Request & Throughput Estimation
- [ ] DAU and MAU metrics documented with 1-year and 3-year growth projections?
- [ ] Average QPS and Peak QPS calculated using justified multipliers (2x–5x)?
- [ ] Read-to-Write ratio explicitly defined (e.g., 100:1 read-heavy vs 1:1)?
- [ ] Little's Law applied to compute concurrent in-flight requests ($L = \lambda W$)?

## 2. Storage & Bandwidth Estimation
- [ ] Entity schema size calculated at the raw byte level?
- [ ] Indexing and replication multipliers included in storage sizing (typically 3x–4x)?
- [ ] 5-year storage growth projected including retention and compaction headroom?
- [ ] Ingress and Egress network bandwidth calculated in Gbps?
- [ ] Cache working set sized using Pareto 80/20 principle with 40% memory headroom?
