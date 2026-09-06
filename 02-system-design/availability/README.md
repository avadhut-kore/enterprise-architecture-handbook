# High Availability Architecture: Mathematics, Topologies, and Error Budgets

## 1. Architectural Overview & Mathematical Formulation
**High Availability (HA)** is the characteristic of a distributed system that aims to ensure an agreed level of operational performance and uptime over a designated time period, mitigating single points of failure (SPOFs) through redundancy, automatic failover, and fault isolation.

### The Mathematical Definition of Availability
Availability ($A$) is formally defined as the ratio of operational uptime to total time:

$$A = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}}$$

Where:
* **MTBF (Mean Time Between Failures)**: The average operational duration between system outages.
* **MTTR (Mean Time To Repair / Recover)**: The average time required to detect, diagnose, failover, and restore system availability.

> **Architectural Insight**: You can increase availability either by making systems fail less frequently ($\uparrow \text{MTBF}$) or by recovering automatically and near-instantaneously when they do fail ($\downarrow \text{MTTR}$). In modern cloud architecture, **minimizing MTTR through automated self-healing is far cheaper and more realistic than attempting to prevent all failures.**

---

## 2. The Nines of Availability (Downtime Table)

Every additional "nine" of availability incurs an exponential increase in architectural complexity, operational cost, and distributed state coordination overhead:

| Availability Level | Downtime per Year | Downtime per Month | Downtime per Day | Architectural Characteristics |
|---|---|---|---|---|
| **$99\%$ (Two Nines)** | 3.65 days | 7.31 hours | 14.40 minutes | Single cloud instance, daily manual backups, manual recovery. |
| **$99.9\%$ (Three Nines)** | 8.76 hours | 43.83 minutes | 1.44 minutes | Multi-AZ deployment, load balanced stateless nodes, automated health checks. |
| **$99.95\%$** | 4.38 hours | 21.92 minutes | 43.20 seconds | Standard enterprise SaaS SLA tier. Automated failover, multi-AZ database clustering. |
| **$99.99\%$ (Four Nines)** | 52.60 minutes | 4.38 minutes | 8.64 seconds | True High Availability. Multi-AZ active-active, cross-region warm standby, automated circuit breakers. |
| **$99.999\%$ (Five Nines)** | 5.26 minutes | 26.30 seconds | 864 milliseconds | Mission-critical / Telco / Core Banking. Multi-region active-active, zero-downtime canary deployments, hardware redundancy. |

---

## 3. The SLA, SLO, SLI & Error Budget Framework

To govern availability objectively across engineering squads:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      THE RELIABILITY CONTRACT TIER                          │
├─────────────────────┬───────────────────────────────────────────────────────┤
│ SLI (Indicator)     │ The quantitative metric measured:                     │
│                     │ Good Requests / Total Valid Requests over 30 days     │
├─────────────────────┼───────────────────────────────────────────────────────┤
│ SLO (Objective)     │ Internal engineering reliability target:              │
│                     │ E.g., 99.95% successful requests over rolling 30 days │
├─────────────────────┼───────────────────────────────────────────────────────┤
│ SLA (Agreement)     │ External contractual promise with financial penalty:  │
│                     │ E.g., 99.9% uptime (leaves 0.05% safety margin)       │
├─────────────────────┼───────────────────────────────────────────────────────┤
│ Error Budget        │ Allowed downtime = 100% - SLO:                        │
│                     │ For 99.95% SLO = 0.05% = 21.6 minutes / month         │
└─────────────────────┴───────────────────────────────────────────────────────┘
```

### The Error Budget Rule:
* **Error Budget $> 0$**: Squads are cleared to ship new features and innovate rapidly.
* **Error Budget Exhausted ($\le 0$)**: Feature deployments are automatically frozen; engineering capacity is 100% redirected to reliability engineering, bug fixes, and MTTR reduction.

---

## 4. Availability Topologies Compared

```mermaid
flowchart TD
    subgraph Passive["Active-Passive (Hot Standby)"]
        LB1[Load Balancer] --> Primary1[Active Node]
        Primary1 -.->|Sync / Async State Replication| Standby1[Passive Standby Node]
        LB1 -.->|Health Check Failover| Standby1
    end

    subgraph ActiveActive["Active-Active (Symmetric Load)"]
        LB2[Global Anycast Load Balancer]
        LB2 --> NodeA[Active Node A (50% Traffic)]
        LB2 --> NodeB[Active Node B (50% Traffic)]
        NodeA <-->|Distributed State Sync / Quorum| NodeB
    end
```

| Topology | Failover Time | Resource Utilization | Split-Brain Risk | Cost |
|---|---|---|---|---|
| **Active-Passive (Cold)** | Hours (Manual spin up) | 0% on standby | None | Low ($1.1\times$) |
| **Active-Passive (Hot)** | Seconds ($10\text{s} - 60\text{s}$) | Standby sits idle ($0\%$ traffic) | Moderate (Requires fencing token) | Moderate ($2.0\times$) |
| **Active-Active** | Zero ($< 1\text{s}$) | $100\%$ active utilization | High (Requires quorum / CRDTs) | High ($2.2\times - 3.0\times$) |

---

## 5. Cascading Failures and Composite Availability Math

In distributed microservice graphs, availability does not add up—it multiplies across synchronous dependencies:

$$A_{\text{composite}} = A_1 \times A_2 \times A_3 \times \dots \times A_n$$

### The Math of Synchronous Chaining:
If a checkout transaction synchronously calls 5 microservices, each with individual $99.9\%$ availability:

$$A_{\text{composite}} = 0.999 \times 0.999 \times 0.999 \times 0.999 \times 0.999 = (0.999)^5 \approx 99.5\%$$

Your application has dropped from **Three Nines ($8.7\text{h}$ downtime)** to **Two-and-a-Half Nines ($43.8\text{h}$ downtime)** simply due to synchronous coupling!

### Architectural Mitigation:
* **Asynchronous Decoupling**: Use message queues or transactional outboxes across service boundaries.
* **Fallback Caching**: Return stale or degraded data from local cache if a dependency is offline.
* **Circuit Breakers**: Trip immediately when failure thresholds are breached to preserve caller threads.

---

## 6. High Availability Architectural Checklist
- [ ] Calculate composite availability for all critical business transaction paths.
- [ ] Distribute all compute and database tiers across a minimum of 3 Availability Zones.
- [ ] Configure deep health checks (distinguishing shallow liveness from database readiness).
- [ ] Enforce automated load-shedding and circuit breaking on all external synchronous calls.
- [ ] Implement Fencing Tokens to prevent split-brain state corruption during failovers.
- [ ] Track monthly Error Budget consumption and enforce feature freezes when exhausted.

---

## 7. Related Modules
* [02-system-design/fault-tolerance/](../fault-tolerance/README.md) — Circuit breakers, bulkheads, and load shedding mechanics.
* [02-system-design/disaster-recovery/](../disaster-recovery/README.md) — RTO/RPO metrics, regional failovers, and backup pipelines.
* [11-observability/](../../11-observability/) — SLO monitoring, alerting, and telemetry dashboards.
