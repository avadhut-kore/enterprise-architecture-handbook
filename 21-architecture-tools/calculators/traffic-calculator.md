# Architectural Calculator: Traffic & Concurrency

## 1. Mathematical Formulation

```
Average QPS = Daily Total Requests / 86,400 seconds
Peak QPS = Average QPS * Peak Multiplier (typically 2.0x to 5.0x)
Concurrent Active Users = Daily Active Users (DAU) * (Daily Engagement Minutes / 1,440)
```

By Little's Law:
$$L = \lambda \cdot W$$
Where $L$ is concurrent in-flight requests, $\lambda$ is arrival rate (QPS), and $W$ is average request duration (seconds).

---

## 2. Reference Sizing Worksheet

```
+------------------+---------------+---------------+-------------------+-------------------+
| DAU Volume       | Actions/User  | Avg QPS       | Peak QPS (3.0x)   | In-Flight (100ms) |
+------------------+---------------+---------------+-------------------+-------------------+
| 1,000,000 (1M)   | 50            | 579 QPS       | 1,736 QPS         | 174 requests      |
| 10,000,000 (10M) | 50            | 5,787 QPS     | 17,361 QPS        | 1,736 requests    |
| 100,000,000 (100M| 50            | 57,870 QPS    | 173,611 QPS       | 17,361 requests   |
| 1,000,000,000(1B)| 50            | 578,703 QPS   | 1,736,111 QPS     | 173,611 requests  |
+------------------+---------------+---------------+-------------------+-------------------+
```

---

## 3. Production Multipliers

- **Diurnal Fluctuation**: Normal business hours experience $2\times$ the daily average.
- **Marketing / Flash Sale Spikes**: E-commerce events require a $5\times$ to $10\times$ peak headroom buffer.
