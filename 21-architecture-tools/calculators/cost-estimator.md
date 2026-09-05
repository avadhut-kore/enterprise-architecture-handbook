# Architectural Calculator: Cloud Infrastructure TCO Estimator

## 1. Total Cost of Ownership (TCO) Formulation

$$\text{Monthly TCO} = C_{\text{compute}} + C_{\text{storage}} + C_{\text{network}} + C_{\text{licensing}} + C_{\text{support}}$$

---

## 2. Cost Modeling Breakdown

```
1. Compute Tier (Kubernetes Cluster):
   - Total vCPUs needed = (Peak QPS * Core-Seconds per Request) / Target Core Utilization (60%)
   - Node Cost = Node Count * Monthly Cost per Instance (Spot/Reserved Discounts applied)

2. Storage Tier:
   - Primary Disk Cost = GB Provisioned * Storage Price per GB ($0.08/GB EBS gp3)
   - IOPS Provisioned Cost = (Provisioned IOPS - 3000 free) * $0.005/IOPS

3. Network Egress:
   - Monthly Egress TB * $0.08/GB ($80 per TB)
   - CDN Bandwidth = Monthly CDN Egress TB * $0.02/GB ($20 per TB)
```

---

## 3. Financial Optimization Rules for Architects

- **Leverage Savings Plans**: Commit to 1-year or 3-year Compute Savings Plans for steady-state workloads to reduce EC2/vCPU costs by 40%–60%.
- **Cache at the Edge**: Every gigabyte served from a CDN edge costs up to 75% less than serving directly from cloud origin egress.
