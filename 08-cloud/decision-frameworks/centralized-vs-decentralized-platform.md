# Decision Framework: Centralized Platform vs Decentralized Infrastructure

```yaml
status: approved
decision_type: framework
scope: enterprise-platform-governance
owners: architecture-review-board
review_cadence: annual
```

## 1. Organizational Model Comparison

| Dimension | Centralized Platform (Golden Paths) | Decentralized (Every Team Owns Everything) |
| :--- | :--- | :--- |
| **Security Posture** | Uniform; automated guardrails enforced by code | Fractured; security depends on individual developer skill |
| **Cognitive Load** | Low; developers focus on business domain code | Extreme; developers spend 40% of time debugging Terraform/K8s |
| **Innovation Velocity**| Fast for standard 80% workloads; escape hatch for 20% | High variance; frequent reinventing of the wheel |
| **Enterprise Standard**| **MANDATORY FOR ENTERPRISES > 50 DEVELOPERS** | Suitable only for early-stage startups (< 10 devs) |
