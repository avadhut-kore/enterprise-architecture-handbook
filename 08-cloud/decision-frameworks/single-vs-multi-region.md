# Decision Framework: Single-Region vs Multi-Region

```yaml
status: approved
decision_type: framework
scope: enterprise-resilience
owners: architecture-review-board
review_cadence: annual
```

## 1. Multi-Region Evaluation Matrix

```mermaid
graph TD
    Start[Evaluate Workload Resiliency Requirement] --> Q1{Is Required Uptime >= 99.999% or RTO < 15 Minutes?}
    Q1 -->|No| SingleRegion[Single-Region Multi-AZ Deployment: 99.99% Uptime]
    Q1 -->|Yes| Q2{Can Workload Tolerate Asynchronous RPO (Seconds of Data Loss)?}
    Q2 -->|Yes: Standard Enterprise| MultiActivePassive[Multi-Region Active-Passive: Warm Standby / Pilot Light]
    Q2 -->|No: Zero RPO Mandatory| MultiActiveActive[Multi-Region Active-Active: Requires Distributed Spanner/CRDTs]
```

---

## 2. Quantitative Scoring
- **Single-Region Multi-AZ**: Delivers **99.99% uptime** (less than 52 minutes of downtime per year) at baseline cost ($1.0x$).
- **Multi-Region Active-Passive**: Delivers **99.995% uptime** at $1.6x$ baseline cost.
- **Multi-Region Active-Active**: Delivers **99.999% uptime** at $2.3x - 2.5x$ baseline cost.
- **Rule**: Exhaust single-region multi-AZ capabilities before requesting multi-region funding.
