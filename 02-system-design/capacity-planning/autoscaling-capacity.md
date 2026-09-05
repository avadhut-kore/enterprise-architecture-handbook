# Autoscaling Capacity Planning

## 1. Principles of Elastic Infrastructure
Autoscaling dynamically adjusts provisioned compute resources to match fluctuating demand. While autoscaling enables cost efficiency during off-peak hours, naive implementations cause production outages due to provisioning latency, metric lag, and oscillatory flapping.

```mermaid
flowchart TD
    TrafficSpike[Sudden 5x Traffic Surge] --> MetricLag[1. Metric Collection Delay: 60-120s]
    MetricLag --> ScaleDecision[2. Horizontal Pod Autoscaler Triggers]
    ScaleDecision --> NodeProvision[3. Cluster Autoscaler Spins New Cloud VM: 2-4 mins]
    NodeProvision --> ImagePull[4. Container Image Pull & Init: 30-60s]
    ImagePull --> Warmup[5. Application JIT / Cache Warmup: 30s]
    Warmup --> Ready[Pods Ready: 5 to 7 Minutes Later!]
    
    style Ready fill:#f96,stroke:#333,stroke-width:2px
```

---

## 2. Provisioning Latency & Spin-up Math
The time elapsed between a traffic surge and effective traffic absorption is governed by:
$$T_{\text{spinup}} = T_{\text{detect}} + T_{\text{node\_launch}} + T_{\text{image\_pull}} + T_{\text{app\_warmup}}$$

### Spin-up Latency by Compute Paradigm
* **Serverless Functions (AWS Lambda / Cloud Functions)**: $T_{\text{spinup}} \approx 100\text{ ms}\text{--}2\text{ s}$. Fast, but limited execution duration and high per-invocation cost at scale.
* **Containers on Warm Kubernetes Nodes**: $T_{\text{spinup}} \approx 15\text{--}45\text{ seconds}$.
* **New Cloud Virtual Machines (EC2 / Azure VMs)**: $T_{\text{spinup}} \approx 2\text{--}5\text{ minutes}$.

*Critical Architectural Rule*: Autoscaling **cannot** absorb sudden flash crowds (e.g., ticket drops or marketing push notifications) arriving in $<15\text{ seconds}$. Flash surges must be absorbed by pre-warmed capacity headroom and queue buffering.

---

## 3. Preventing Autoscaling Flapping (Oscillation)
Flapping occurs when a cluster rapidly scales up under load, cools down immediately, scales down, and then spikes again, causing continuous container initialization churn.

```mermaid
flowchart LR
    Spike[Load > 75%] -->|Scale Up +50%| FleetLarge[Fleet: 60 Pods]
    FleetLarge -->|Load Drops to 30%| ScaleDown[Scale Down -50%]
    ScaleDown -->|Fleet: 30 Pods| Spike
```

### Flapping Mitigation Policies
1. **Asymmetric Cooldowns**:
   * Scale-up stabilization window: $0\text{ seconds}$ (scale up instantly when breached).
   * Scale-down stabilization window: $300\text{--}600\text{ seconds}$ (hold capacity for 5â€“10 minutes to verify traffic drop is real).
2. **Step Scaling Policies**:
   * If CPU $>70\%$: Add $+20\%$ pods.
   * If CPU $>85\%$: Add $+50\%$ pods.
   * If CPU $>95\%$: Add $+100\%$ pods (emergency surge).
3. **Minimum Safe Fleet Sizing**:
   $$N_{\text{min}} = \frac{\text{Projected Steady Baseline Traffic}}{\text{Safe Pod Capacity}} \times 1.25\text{ Headroom}$$
