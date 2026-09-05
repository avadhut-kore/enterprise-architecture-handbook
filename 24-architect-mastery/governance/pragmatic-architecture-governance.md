# Pragmatic Architecture Governance

Traditional governance fails because it relies on manual approval gates, lengthy documentation, and centralized review boards that slow teams down. Modern governance automates enforcement and provides self-service guardrails.

## 1. Gates vs Guardrails

```
TRADITIONAL GOVERNANCE (GATES):
Developer -> Submit 50-page doc -> Wait 3 weeks -> ARB Meeting -> Approved/Rejected
Result: Teams bypass governance, shadow IT flourishes, releases crawl.

MODERN GOVERNANCE (GUARDRAILS):
Developer -> Clone Golden Path Repo -> Built-in Security/CI/Linting -> Auto-Validated
Result: Velocity accelerates, architectural standards are enforced by code in CI/CD.
```

## 2. The Three Layers of Pragmatic Governance

1. **Automated CI/CD Policies**: Linter rules, dependency scanning, ArchUnit fitness functions, Terraform compliance (Checkov, tfsec), Open Policy Agent (OPA).
2. **Standardized Architecture Deliverables**: Lightweight ADRs tracked in git repositories alongside code.
3. **Architecture Review Board (Consultative)**: ARB acts as an advisory center of excellence rather than an authoritarian checkpoint.

## Related Modules
- [Architecture Review Board Operating Model](file:///d:/company/products/enterprise-architecture-handbook/24-architect-mastery/architecture-review/architecture-review-board-operating-model.md)
- [Architecture Metrics and KPIs](file:///d:/company/products/enterprise-architecture-handbook/24-architect-mastery/governance/architecture-metrics-and-kpis.md)
