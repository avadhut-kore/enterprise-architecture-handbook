# The 4-Step System Design Interview Framework

## 1. High-Level Flow (45 Minutes)

```mermaid
flowchart LR
    Step1[Step 1: Understand Problem & Scope (5m)] --> Step2[Step 2: Capacity Estimation (5m)]
    Step2 --> Step3[Step 3: High-Level Architecture (12m)]
    Step3 --> Step4[Step 4: Deep Dive & Bottlenecks (18m)]
    Step4 --> Wrap[Wrap-up & Trade-offs (5m)]
```

---

## 2. Detailed Step Breakdown

### Step 1: Clarify Requirements & Scope (Minutes 0–5)
- Clarify functional requirements (pick top 3 core user journeys).
- Quantify non-functional requirements (Availability SLA, latency targets, consistency model).
- Establish explicit out-of-scope boundaries.

### Step 2: Back-of-the-Envelope Calculations (Minutes 5–10)
- Calculate Read/Write QPS and peak traffic multiplier ($3\times$).
- Calculate storage requirements over 5 years.
- Sizing cache working set using the 80/20 rule.

### Step 3: High-Level Design (Minutes 10–22)
- Sketch end-to-end topology: Client $\rightarrow$ Edge/CDN $\rightarrow$ Gateway $\rightarrow$ Stateless Services $\rightarrow$ Storage.
- Trace primary read and write flows step-by-step.
- Verify basic functional completeness before optimizing.

### Step 4: Deep-Dive & Resiliency (Minutes 22–40)
- Dive into component bottlenecks identified by the interviewer.
- Address distributed concurrency, caching, data partitioning, and failure modes.

### Step 5: Wrap-up & Trade-Offs (Minutes 40–45)
- Summarize architectural decisions and CAP/PACELC trade-offs.
- Highlight future scaling vectors and monitoring metrics.
