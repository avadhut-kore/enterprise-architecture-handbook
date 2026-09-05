# Resource Sizing Methodology: CPU, Memory, IOPS & Bandwidth

## Executive Summary

Sizing infrastructure requires translating business user metrics into hardware primitives.

---

## 1. Compute Sizing Formula

$$\text{vCPUs Required} = \frac{\text{Peak Requests per Second} \times \text{Average Latency in Seconds}}{\text{Target CPU Utilization Threshold (e.g., 0.65)}} + \text{Headroom}$$

### Worked Example:
- Peak load = $10,000 \text{ req/sec}$
- Average execution duration = $50\text{ ms} = 0.05\text{ seconds}$
- Target CPU utilization = $65\%$ ($0.65$)
- Concurrency = $10,000 \times 0.05 = 500 \text{ concurrent threads}$
- Cores required = $500 / 0.65 \approx 770 \text{ vCPUs}$
- Fleet sizing = $96 \text{ instances of } \text{c7g.2xlarge (8 vCPUs each)}$.

---

## 2. Storage IOPS Sizing
$$\text{Total IOPS} = \text{Read IOPS} + (\text{Write IOPS} \times \text{Write Penalty})$$
- Traditional RAID 5 has a write penalty of 4; cloud SSDs (EBS gp3) provision IOPS independently of storage capacity. Size baseline IOPS to absorb peak write transaction spikes without disk queuing.
