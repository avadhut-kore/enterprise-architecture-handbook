# Architectural Calculator: Bandwidth & Network Egress

## 1. Mathematical Formulation

```
Ingress Throughput (Mbps) = (Write QPS * Average Inbound Payload Bytes * 8 bits/Byte) / 1,000,000
Egress Throughput (Mbps)  = (Read QPS * Average Outbound Payload Bytes * 8 bits/Byte) / 1,000,000
CDN Offload Egress = Total Egress * (1 - CDN Cache Hit Ratio)
```

$$\text{Network Transit Cost} = \text{Monthly Egress (TB)} \cdot \text{Cost per TB}$$

---

## 2. Reference Worksheet

```
Scenario: Video/Image Platform
- Peak Read QPS: 20,000 QPS
- Average Response Payload: 150 KB (Images/Thumbnails)
- Gross Egress: 20,000 * 150 KB * 8 = 24,000,000 kbps = 24 Gbps
- CDN Cache Hit Ratio: 92%
- Cloud Origin Egress: 24 Gbps * (1 - 0.92) = 1.92 Gbps
- Monthly Origin Data Transfer: (1.92 Gbps / 8) * 86,400 * 30 days = 622 TB / Month
```

---

## 3. Architectural Rules

- Design for asymmetric networks: Egress typically exceeds ingress by a factor of $10:1$ to $50:1$.
- Multi-CDN routing avoids single-provider egress bandwidth quotas.
