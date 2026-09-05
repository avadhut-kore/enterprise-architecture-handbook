# Pipeline Governance and Quality Gates

Enterprise pipeline governance balances developer velocity with risk mitigation and regulatory compliance.

## 1. Automated Quality Gates

```
[Pull Request Initiated]
           │
           ▼
[Quality Gate 1: Code Quality & Coverage] ──► PR Blocked if Coverage < 80%
           │
           ▼
[Quality Gate 2: Security & SAST] ──────────► PR Blocked if Critical/High CVE found
           │
           ▼
[Quality Gate 3: Branch Up-to-Date] ────────► PR Blocked if behind trunk
           │
           ▼
[Merge Permitted & Continuous Delivery Initiated]
```

## 2. Policy-as-Code in Pipelines
- Enforce mandatory pipeline steps via central GitHub Action rulesets or GitLab CI compliance frameworks.
- Disallow developers from disabling security scan steps in child pipelines.

## Related Resources
- [DevSecOps Architecture](../../devsecops/README.md)
- [Compliance & Regulated DevOps](../../compliance/README.md)
