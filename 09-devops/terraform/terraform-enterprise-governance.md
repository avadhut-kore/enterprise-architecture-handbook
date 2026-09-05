# Terraform Enterprise Governance & Landing Zones

Scaling Terraform across dozens of cross-functional engineering teams requires opinionated module abstraction and automated compliance.

## 1. Multi-Tier Module Architecture

```
┌─────────────────────────────────────────────────────────────┐
│ 1. ROOT APPLICATION CONFIGURATION (Team Repositories)       │
│ - Instantiates enterprise modules with custom parameters    │
├─────────────────────────────────────────────────────────────┤
│ 2. COMPOSITE ENTERPRISE MODULES (Platform Team Registry)    │
│ - `terraform-aws-microservice` (Wraps EKS + RDS + IAM)      │
│ - Enforces standard tags, logging, and encryption defaults  │
├─────────────────────────────────────────────────────────────┤
│ 3. PRIMITIVE RESOURCE MODULES (Public / Core Registry)      │
│ - Official VPC, S3, Security Group building blocks          │
└─────────────────────────────────────────────────────────────┘
```

## 2. Automated Drift Detection
- Schedule nightly headless Terraform plans (`terraform plan -detailed-exitcode`).
- If unmanaged changes are detected (exit code 2), alert SREs via Slack/PagerDuty to prevent manual configuration drift in cloud consoles.

## Related Resources
- [Terraform State Management](./terraform-architecture-and-state-management.md)
- [Policy as Code](../policy-as-code/README.md)
