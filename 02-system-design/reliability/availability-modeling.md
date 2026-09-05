# Availability Modeling & The Math of Nines

## 1. System Availability Formula
Availability ($A$) represents the fraction of time a system is fully operational:
$$A = \frac{\text{Uptime}}{\text{Uptime} + \text{Downtime}} = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}}$$

### Downtime Allowances by "The Nines"
| Target Availability | Downtime per Year | Downtime per Month | Downtime per Day |
| :--- | :--- | :--- | :--- |
| **99% (Two Nines)** | 3.65 days | 7.30 hours | 14.40 minutes |
| **99.9% (Three Nines)** | 8.76 hours | 43.8 minutes | 1.44 minutes |
| **99.99% (Four Nines)** | 52.56 minutes | 4.38 minutes | 8.64 seconds |
| **99.999% (Five Nines)** | 5.26 minutes | 26.30 seconds | 0.86 seconds |

---

## 2. Serial vs. Parallel Availability Mathematics

```mermaid
flowchart LR
    subgraph Serial Dependency: A_total = A1 * A2
        S1[Service 1: 99.9%] --> S2[Service 2: 99.9%]
    end

    subgraph Parallel Redundancy: A_total = 1 - (1 - A1)^2
        P1[Node 1: 99.0%]
        P2[Node 2: 99.0%]
    end
```

### 1. Serial Components (Dependencies Degrade Availability)
When a request requires $N$ components to succeed in series:
$$A_{\text{serial}} = \prod_{i=1}^{N} A_i$$
* If an architecture chains 5 microservices, each with $99.9\%$ availability ($0.999$):
$$A_{\text{system}} = (0.999)^5 = 0.9950 \approx \mathbf{99.5\%} \quad (\text{Downtime jumps from 8.7 hours to 43.8 hours/year!})$$

### 2. Parallel Redundancy (Redundancy Elevates Availability)
When components are redundant in parallel:
$$A_{\text{parallel}} = 1 - \prod_{i=1}^{N} (1 - A_i)$$
* Running two independent nodes each with mediocre $99.0\%$ availability:
$$A_{\text{system}} = 1 - (1 - 0.99)^2 = 1 - (0.01)^2 = 1 - 0.0001 = \mathbf{99.99\%} \quad (\text{Four Nines achieved!})$$
