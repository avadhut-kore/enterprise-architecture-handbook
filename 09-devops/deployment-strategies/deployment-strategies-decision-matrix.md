# Deployment Strategies Decision Matrix

Multi-criteria evaluation for selecting deployment strategies based on business criticality, infrastructure cost, and data consistency constraints.

| Strategy | Downtime | Rollback Speed | Infra Cost Multiplier | State / Schema Complexity | Recommended Use Case |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Recreate** | Yes (Minutes) | Slow | 1.0x | Simple | Non-production environments, batch processing. |
| **Rolling** | None | Moderate (Roll forward/back) | 1.0x - 1.25x | High (Must support N and N+1 API schemas) | Standard stateless microservices on Kubernetes. |
| **Blue/Green** | None | Instant (< 5s DNS/Router flip)| 2.0x | Very High (Shared database must handle both versions) | Critical web APIs, payment gateways where rollbacks must be instant. |
| **Canary** | None | Fast (< 30s) | 1.1x - 1.2x | High | High-throughput services with clear baseline telemetry. |
| **Progressive** | None | Automated (< 15s) | 1.1x - 1.2x | High | Tier-1 services using Argo Rollouts / Flagger. |
| **Shadow** | None | Instant (Drop mirror) | 2.0x | Extreme (Must prevent duplicate DB writes/emails) | Complete rewrites of legacy core transactional engines. |
| **Feature Flags** | None | Instant (Toggle flag) | 1.0x | Moderate | User-facing UI features, multi-tenant tiered rollouts. |

## Related Resources
- [Deployment Strategies Hub](./README.md)
- [Database DevOps](../database-devops/README.md)
