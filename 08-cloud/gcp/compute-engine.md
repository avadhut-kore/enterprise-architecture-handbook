# GCP Compute Engine: Managed Instance Groups & Spot VMs

## Executive Summary

Google Compute Engine (GCE) provides virtual machines running on Google's global infrastructure.

---

## 1. Managed Instance Groups (MIGs) Architecture

```mermaid
graph TD
    GLB[Global External HTTP(S) Load Balancer] --> MIG[Regional Managed Instance Group]
    MIG --> VM1[VM Instance: Zone A]
    MIG --> VM2[VM Instance: Zone B]
    MIG --> VM3[VM Instance: Zone C]

    Autoscaler[Predictive Autoscaler] -->|Scales Fleet based on CPU / Load Balancer Capacity| MIG
```

---

## 2. Advanced Compute Capabilities

1. **Regional Managed Instance Groups**: Distributes instances automatically across multiple availability zones within a region, providing automated instance repair, health checking, and zero-downtime rolling updates.
2. **Custom Machine Types**: Tailor exact vCPU and memory ratios (e.g., 6 vCPUs and 22 GB RAM) rather than being constrained to rigid predefined VM sizing tiers, saving 15–20% on compute spend.
3. **Spot VMs**: Run fault-tolerant batch workloads on Google's surplus compute at discounts of 60–91% compared to on-demand pricing.
