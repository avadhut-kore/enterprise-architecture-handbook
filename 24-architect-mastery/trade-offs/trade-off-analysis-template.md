# Trade-Off Analysis Template

Use this template when evaluating complex, high-consequence architectural choices where trade-offs must be transparently justified to technical and executive stakeholders.

## 1. Problem Framing
- **Decision Title**: [e.g., Cross-Region Replication Strategy for Core Payments]
- **Core Dilemma**: [e.g., Latency vs Durability across US-East and EU-West]
- **Business Driver**: [e.g., Compliance with DORA regulatory uptime mandates]

## 2. Competing Forces Matrix

| Force | Option 1: [Synchronous Active-Active] | Option 2: [Async Active-Passive with Failover] | Option 3: [Regional Sharding] |
| :--- | :--- | :--- | :--- |
| **Write Latency** | High (>120ms cross-region) | Low (<5ms local region) | Low (<5ms local region) |
| **RPO (Data Loss Window)**| Zero RPO | 1-5 seconds | Zero RPO |
| **RTO (Recovery Time)** | Immediate (<1 sec) | 2-5 minutes | Immediate (<1 sec) |
| **Operational Complexity**| Extremely High | Moderate | High (Routing layer needed) |
| **Infrastructure Cost** | 3.5x baseline | 1.8x baseline | 2.2x baseline |

## 3. Explicit Compromise Statement
> *"We consciously accept **[Compromise A: Higher operational complexity and regional routing rules]** in order to achieve **[Primary Benefit: Sub-5ms write latencies while guaranteeing zero data loss]**."*

## 4. Re-Evaluation Criteria
- Condition 1: If cross-region backbone latency drops below 20ms.
- Condition 2: If customer base shifts beyond regional sovereignty boundaries.
