# Decision Framework: Managed Database vs Self-Managed on IaaS/K8s

```yaml
status: approved
decision_type: framework
scope: enterprise-data-infrastructure
owners: architecture-review-board
review_cadence: annual
```

## 1. Total Cost of Ownership (TCO) Calculation
$$\text{TCO}_{\text{Self-Managed}} = \text{Cloud VM Infrastructure} + (2 \times \text{Senior SRE Salaries (\$500k)}) + \text{Outage Risk Premium}$$
$$\text{TCO}_{\text{Managed}} = \text{Managed Service Fee (e.g. AWS RDS / Aurora / Cloud SQL)}$$

- **Rule**: For 95% of enterprise workloads, **Managed Databases are substantially cheaper** when true engineering labor costs are factored into the decision.
- Self-managed is authorized only for extreme scale (> 100,000 IOPS sustained) or custom uncertified database extensions.
