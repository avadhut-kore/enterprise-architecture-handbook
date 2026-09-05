# Decision Framework: Rehost vs Replatform vs Refactor

```yaml
status: approved
decision_type: framework
scope: enterprise-modernization
owners: architecture-review-board
review_cadence: semi-annual
```

## 1. Modernization Trade-Off Matrix

```mermaid
graph LR
    Rehost[Rehost: Lift & Shift] -->|Fastest Timeline / Zero Agility Gain| Speed[Speed Priority: Datacenter Eviction]
    Replatform[Replatform: Move to Managed PaaS/Containers] -->|Moderate Effort / High Agility ROI| SweetSpot[ENTERPRISE SWEET SPOT]
    Refactor[Refactor: Cloud-Native Microservices] -->|Highest Effort & Risk / Maximum Scalability| Strategic[Core Business Differentiator]
```
