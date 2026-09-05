# Cloud Migration Decision Framework (The 7 Rs Scorecard)

```yaml
status: approved
decision_type: framework
scope: enterprise-cloud-migration
owners: architecture-review-board
review_cadence: semi-annual
```

## Executive Summary

This framework evaluates every candidate workload to assign the optimal migration strategy across the 7 Rs.

---

## 1. Decision Flowchart

```mermaid
graph TD
    Start[Evaluate Legacy Application] --> Q1{Is Application Obsolete or Redundant?}
    Q1 -->|Yes| R1[1. RETIRE: Decommission Immediately]
    Q1 -->|No| Q2{Mainframe Coupled or Hardware Life Remaining?}
    Q2 -->|Yes| R2[2. RETAIN: Keep On-Premises]
    Q2 -->|No| Q3{Commercial COTS with Superior SaaS Equivalent?}
    Q3 -->|Yes| R3[3. REPURCHASE: Migrate to SaaS]
    Q3 -->|No| Q4{Requires Urgent Datacenter Exit < 6 Months?}
    Q4 -->|Yes| R4[4. REHOST / RELOCATE: Lift-and-Shift to Cloud VMs]
    Q4 -->|No| Q5{Can Benefit from Managed DB & Containers with Low Code Changes?}
    Q5 -->|Yes| R5[5. REPLATFORM: Containerize + Managed RDS/CloudSQL]
    Q5 -->|No: Core Differentiating Business Engine| R6[6. REFACTOR: Cloud-Native Microservices]
```
