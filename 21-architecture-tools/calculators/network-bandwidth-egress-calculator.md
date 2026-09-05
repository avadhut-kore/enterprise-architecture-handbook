# Network Bandwidth & Egress Cost Calculator

## Formula
$$\text{Egress Bandwidth (Gbps)} = \frac{\text{Peak Requests/Sec} \times \text{Average Response Size (KB)} \times 8}{1,000,000}$$
$$\text{Monthly Egress Cost} = \text{Monthly Outbound Terabytes} \times 1,000 \times \text{Price per GB (\$0.08)}$$

### Worked Example:
- $10,000\text{ req/sec} \times 100\text{ KB payload} \times 8 / 1,000,000 = 8.0\text{ Gbps}$ egress bandwidth.
- Monthly transfer = $259.2\text{ TB} \times 1,000 \times \$0.08 = \$20,736/\text{month}$ in egress fees.
