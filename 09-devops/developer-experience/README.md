# Developer Experience (DevEx) & Friction Reduction

Developer Experience (DevEx) measures how easily, safely, and efficiently engineers can deliver high-quality software.

## 1. Inner Loop vs Outer Loop

```
INNER LOOP (Local Developer Workstation - Iteration speed: Seconds)
[Write Code] ──► [Save] ──► [Hot Reload] ──► [Local Unit Test]
Goal: Sub-second feedback loops; zero external network dependencies.
                                 │
                                 ▼ (Git Push)
OUTER LOOP (CI/CD Pipeline & Cloud - Iteration speed: Minutes)
[CI Build] ──► [Integration Tests] ──► [Security Scans] ──► [Deploy Staging]
Goal: Automated verification, compliance gates, and deployment confidence.
```

## 2. DevEx Metrics Framework
- **Time to First Commit / Production**: How many days does it take a newly hired engineer to ship their first code change to production? (Target: < 48 hours).
- **Local Dev Setup Friction**: Can local environments be spun up with a single command via Devcontainers (`devcontainer up`)?
- **Pipeline Waiting Time**: Average time spent by developers waiting for CI status checks.

## Related Resources
- [Platform Engineering](../platform-engineering/README.md)
- [Platform Economics](../platform-economics/README.md)
