# Elasticity Architecture

## 1. Scalability vs. Elasticity
While closely related, scalability and elasticity represent distinct engineering dimensions:
* **Scalability**: The structural capacity of a system to handle increased volume by adding resources. A scalable system *can* support $1,000,000\text{ RPS}$ if provisioned.
* **Elasticity**: The speed, degree, and automation with which a system adapts its capacity in real time to match fluctuating demand curves, minimizing both under-provisioning and over-provisioning waste.

```mermaid
flowchart TD
    Over[Over-provisioning: Capital Waste / High Idle Cost]
    Target[Elastic Ideal: Capacity Dynamically Mirrors Real Load Curve]
    Under[Under-provisioning: Performance Degradation & Dropped Requests]
```

---

## 2. The Elasticity Penalty Metric

### Economic Waste ($W_{\text{over}}$) vs. Service Penalty ($P_{\text{under}}$)
$$\text{Over-provisioning Waste} = \int_{0}^{T} \max\left(0, \text{Capacity}(t) - \text{Demand}(t)\right) dt$$
$$\text{Under-provisioning Deficit} = \int_{0}^{T} \max\left(0, \text{Demand}(t) - \text{Capacity}(t)\right) dt$$

---

## 3. Spot Instances & Cloud Cost Elasticity
Modern elastic architectures leverage **Spot / Preemptible Instances** (unused cloud provider capacity offered at a 70â€“90% discount):
* Workloads must be completely stateless or checkpointed background worker queues.
* Infrastructure automation must handle cloud interruption warnings (e.g., AWS 2-minute termination notice) by gracefully draining pods and rebalancing traffic.
