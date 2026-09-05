# 45-Minute System Design Time Management

## 1. Pacing Blueprint

```
+-----------+-----------------------------------+------------------------------------+
| Time      | Phase                             | Goal & Deliverable                 |
+-----------+-----------------------------------+------------------------------------+
| 00:00-05m | Requirements & Clarification      | Agreed functional scope & NFRs     |
| 05:00-10m | Scale & Capacity Estimation       | Sizing numbers on the whiteboard   |
| 10:00-22m | High-Level Design (HLD)           | Working end-to-end data flow       |
| 22:00-40m | Deep Dive & Failure Engineering   | Scaling, DB sharding, edge cases   |
| 40:00-45m | Wrap-Up & Trade-Off Review        | Bottleneck summary & next steps    |
+-----------+-----------------------------------+------------------------------------+
```

---

## 2. Tactical Rules for Architects

- **Do Not Stall on Calculations**: If arithmetic gets complicated, round to clean base-10 numbers ($86,400\text{s} \approx 100,000\text{s}$, $1\text{M requests} \approx 10\text{ QPS}$). Interviewers care about methodology, not precise calculator math.
- **Drive the Conversation**: Do not wait for the interviewer to prompt every step. Senior candidates actively structure the interview and state their plan.
