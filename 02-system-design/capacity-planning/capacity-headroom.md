# Capacity Headroom & Safety Buffers

## 1. The Queueing Theory of Headroom
In computer systems, waiting times follow Queueing Theory ($M/M/c$ multi-server queue models). As resource utilization ($\rho$) approaches $1.0$ ($100\%$), queue lengths and request latencies do not scale linearly; they explode exponentially.

```mermaid
flowchart LR
    subgraph Green Zone [0% to 60% Utilization]
        G[Queue Wait Time ~ 0ms: Predictable p99 Latency]
    end

    subgraph Yellow Zone [60% to 75% Utilization]
        Y[Linear Latency Increase: Stable under controlled load]
    end

    subgraph Red Zone [>80% Utilization]
        R[Asymptotic Queue Explosion: Cascading Timeouts & Thread Starvation]
    end
```

---

## 2. Mathematical Modeling of Sizing Headroom

### Utilization Factor ($\rho$)
$$\rho = \frac{\lambda}{c \times \mu}$$
Where:
* $\lambda$ = Arrival rate (RPS)
* $c$ = Number of worker instances / threads
* $\mu$ = Service rate per worker

### Target Maximum Utilization Ceilings
To prevent entering the exponential knee of the curve:
* **Compute (CPU)**: $\rho \le 0.65$ ($65\%$ maximum sustained target).
* **Application Memory**: $\rho \le 0.70$ ($70\%$ maximum to avoid Linux OOM kill).
* **Database IOPS**: $\rho \le 0.60$ ($60\%$ to allow WAL sync bursts).
* **Storage Capacity**: $\rho \le 0.75$ ($75\%$ to allow LSM compaction and VACUUM headroom).

---

## 3. Failure Headroom: The Multi-Region 2N Model

In Tier-0 mission-critical enterprise systems, headroom must absorb complete datacenter or cloud region disasters without degrading performance.

```mermaid
flowchart TD
    subgraph Region 1 [US-East: Active]
        Fleet1[Capacity: 100% of Global Traffic]
        Util1[Normal State: Operates at 50% Utilization]
    end

    subgraph Region 2 [US-West: Active]
        Fleet2[Capacity: 100% of Global Traffic]
        Util2[Normal State: Operates at 50% Utilization]
    end

    DNS[Global Traffic Router] -->|50% Global Load| Fleet1
    DNS -->|50% Global Load| Fleet2
```

### Complete Disaster Shift
If Region 1 suffers a total power grid failure:
1. DNS shifts $100\%$ of global traffic to Region 2.
2. Region 2 utilization rises from $50\%$ to **$100\%$ capacity** (its designed physical ceiling).
3. System survives with **zero customer degradation and zero emergency autoscaling lag**.
