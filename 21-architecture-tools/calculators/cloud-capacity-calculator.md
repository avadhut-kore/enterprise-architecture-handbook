# Cloud Compute Capacity Calculator

## Mathematical Sizing Formula
$$\text{Total vCPUs Required} = \frac{\text{Peak Requests/Sec} \times \text{Average Latency (Seconds)}}{\text{Target Utilization Threshold (e.g. 0.65)}} \times (1 + \text{Headroom Buffer})$$

### Worked Sizing Example:
- **Peak Load**: 25,000 requests/second
- **Average Latency**: $40\text{ ms} = 0.04\text{ seconds}$
- **Target CPU Utilization**: $65\%$ ($0.65$)
- **Headroom Buffer**: $20\%$ ($0.20$)
- **Calculation**:
  $$\text{Concurrency} = 25,000 \times 0.04 = 1,000 \text{ concurrent threads}$$
  $$\text{vCPUs Baseline} = 1,000 / 0.65 = 1,538.46 \text{ vCPUs}$$
  $$\text{Total Sized Fleet} = 1,538.46 \times 1.20 = 1,846 \text{ vCPUs}$$
- **Fleet Provisioning**: $231 \text{ instances of } \text{c7g.2xlarge (8 vCPUs, 16 GB RAM each)}$.
