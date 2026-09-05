# Learning from Incidents: The Architecture Feedback Loop

Production incidents are the most honest feedback an architecture ever receives. A mature architecture practice treats every Sev-1 incident as a flaw in design or guardrails, not human operator error.

## 1. The Incident-to-Architecture Pipeline

```
[Sev-1 Production Incident]
             │
             ▼
[Blameless Incident Retrospective] ──► Identify Systemic Contributing Factors
             │
             ▼
[Architectural Review] ──────────────► Was this an unforeseen constraint?
             │                         A missing fitness function?
             ▼
[Remediation Action Item] ───────────► Codify fix into CI/CD Lint / ArchUnit Rule
             │
             ▼
[Permanent Prevention] ──────────────► Future code violating pattern cannot deploy
```

## 2. The 5 Whys Done Right (Systems Over Blame)
- *Why did the service crash?* Database connection pool was exhausted.
- *Why was it exhausted?* A slow query held connections for 30 seconds.
- *Why was the query slow?* A table scan occurred due to a missing index.
- *Why was the index missing?* An ad-hoc feature bypassed standard review.
- *Why did it bypass review?* Our CI/CD pipeline lacked automated EXPLAIN query plan checks.
- **Systemic Action**: Add automated query plan linting in CI to block unindexed scans.

## Related Modules
- [War Stories](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/war-stories/README.md)
- [Fitness Functions in Practice](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/evolution/fitness-functions-in-practice.md)
