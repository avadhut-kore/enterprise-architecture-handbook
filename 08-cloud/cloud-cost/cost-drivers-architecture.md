# Cloud Cost Drivers & Economic Trade-Offs

## Executive Summary

Understanding the primary drivers of cloud expenditures allows architects to design cost-efficient systems from Day 0.

---

## 1. The Five Enterprise Cost Drivers

1. **Compute Sizing & Oversubscription (Typically 50–60% of Spend)**:
   - Development teams routinely over-provision compute (requesting 16 vCPUs and 64 GB RAM for applications running at 5% average utilization).
2. **Network Egress Fees (The Silent Killer: 15–25% of Spend)**:
   - Data ingress is free; outbound data transfer is heavily metered. Cross-AZ traffic costs $\$0.01/\text{GB}$, and public internet egress costs $\$0.05 - \$0.09/\text{GB}$.
3. **Managed Service Markups**:
   - Managed databases (RDS, Cosmos DB) carry a 40–100% premium over raw IaaS instances. This premium is justified only when it eliminates human SRE operational toil.
4. **Unmanaged Storage Bloat**:
   - Forgotten EBS snapshots, non-current S3 object versions, and unattached virtual disks silently compound monthly storage invoices.
5. **Commercial Licensing Penalties**:
   - Running legacy per-core licensed software (Oracle DB, Microsoft SQL Server) in hyper-threaded cloud environments triggers severe licensing audit liabilities.
