# Load Testing Architecture & Execution

## 1. Principles of Load Testing
Load testing verifies that a system fulfills its documented Service Level Objectives (SLOs) under sustained, anticipated peak operational volume.

```mermaid
flowchart LR
    Ramp[1. Ramp Up: 0 to 20,000 RPS over 15 mins] --> Steady[2. Steady State: 20,000 RPS Sustained for 2 Hours]
    Steady --> Cooldown[3. Cooldown: Ramp down to 0 over 10 mins]
```

---

## 2. Open vs. Closed Workload Models

A critical testing flaw is utilizing **Closed Workload Models** (where virtual users wait for a response before sending the next request). In the real world, users arrive independently (**Open Workload Model**):
* If the system slows down, real-world requests continue arriving at the exact same arrival rate ($\lambda$).
* Load testing frameworks must use **Arrival Rate-based testing** (e.g., k6 `constant-arrival-rate`, Gatling) to accurately reproduce server-side queue explosions.

---

## 3. Distributed Load Testing with k6
```javascript
import http from 'k6/http';
import { check } from 'k6';

export const options = {
  scenarios: {
    peak_traffic: {
      executor: 'constant-arrival-rate',
      rate: 10000, // 10,000 requests per second
      timeUnit: '1s',
      duration: '1h',
      preAllocatedVUs: 1000,
      maxVUs: 5000,
    },
  },
  thresholds: {
    http_req_duration: ['p(95)<80', 'p(99)<200'],
    http_req_failed: ['rate<0.001'], // <0.1% errors
  },
};

export default function () {
  const res = http.get('https://api.enterprise.internal/v1/catalog');
  check(res, { 'status is 200': (r) => r.status === 200 });
}
```
