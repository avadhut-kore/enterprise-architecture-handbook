# Decision Framework: Virtual Machines vs Containers vs Serverless

```yaml
status: approved
decision_type: framework
scope: enterprise-compute
owners: architecture-review-board
review_cadence: semi-annual
```

## 1. Decision Matrix

| Workload Characteristic | Virtual Machines (IaaS) | Containers (Cloud Run / ECS / EKS) | Serverless FaaS (Lambda) |
| :--- | :--- | :--- | :--- |
| **Legacy Windows / Kernel Modules**| **Recommended** | Prohibited | Prohibited |
| **Microservices / REST APIs** | Sub-optimal | **Recommended** | Sub-optimal (Cold starts) |
| **Event-Driven Webhooks / Cron** | Overkill | Sub-optimal | **Recommended** |
| **Sustained Continuous CPU Load**| **Recommended (Lowest Unit Cost)**| **Recommended** | Overpriced ($$$) |
| **Extreme Spikiness (Scale to Zero)**| Prohibited | **Recommended (Cloud Run)** | **Recommended** |
