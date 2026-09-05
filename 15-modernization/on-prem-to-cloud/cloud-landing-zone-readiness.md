# Cloud Landing Zone Architecture & Readiness

## 1. Multi-Account Governance Blueprint
Workloads must never be deployed into a single default cloud account. Structure environments using AWS Organizations or Azure Management Groups:
- **Core Security Account**: Centralized CloudTrail, GuardDuty, Security Hub, SIEM ingestion.
- **Network Hub Account**: Transit Gateway, Direct Connect / ExpressRoute termination, centralized outbound NAT gateways.
- **Shared Services Account**: CI/CD build agents, Artifact registries, HashiCorp Vault.
- **Application Accounts**: Isolated per business domain and environment (`orders-prod`, `orders-stage`).
