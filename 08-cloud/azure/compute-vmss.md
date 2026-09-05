# Azure Compute: Virtual Machines & Scale Sets (VMSS)

## Executive Summary

Azure Virtual Machine Scale Sets (VMSS) provide automated deployment, load balancing, and scaling of identical groups of virtual machines.

---

## 1. VMSS Architecture & Availability Topologies

```mermaid
graph TD
    LB[Azure Standard Load Balancer] --> VMSS[VM Scale Set: Flexible Orchestration]
    VMSS --> VM1[VM Instance 1: Fault Domain 1 / AZ 1]
    VMSS --> VM2[VM Instance 2: Fault Domain 2 / AZ 2]
    VMSS --> VM3[VM Instance 3: Fault Domain 3 / AZ 3]
```

---

## 2. Flexible vs Uniform Orchestration

- **Uniform Orchestration (Legacy)**: High-scale compute clusters with identical configurations, optimized for stateless batch processing.
- **Flexible Orchestration (Modern Standard)**: Treats VMs as first-class citizens within the scale set. Allows mixing instance sizes, mixing Spot and On-Demand instances, and attaching dedicated availability guarantees across fault domains.

### Proximity Placement Groups (PPG)
For ultra-low-latency distributed systems (e.g., SAP HANA or custom cluster consensus), bind VMSS instances to a **Proximity Placement Group**. This physically collocates VMs within the same data center room, reducing network RTT to sub-0.3 milliseconds at the expense of regional resilience.
