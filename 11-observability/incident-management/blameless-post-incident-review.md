# Blameless Post-Incident Review (PIR) Template

```markdown
# Post-Incident Review: INC-[Number] - [Short Title]

## 1. Executive Summary
- **Incident Date**: 2026-09-05
- **Duration**: 42 minutes
- **Severity**: SEV-1
- **Customer Impact**: 14,200 checkout transactions failed (HTTP 504 Gateway Timeout).
- **Financial Impact**: ~$140,000 lost revenue.

---

## 2. Chronological Timeline (UTC)
- **14:02** - Automated canary deployment of `order-service:v2.4.1` began.
- **14:07** - Database CPU spiked to 100% due to an unindexed query in v2.4.1.
- **14:09** - Multi-window burn-rate alert paged on-call SRE.
- **14:14** - Incident Commander declared SEV-1; opened incident war room.
- **14:22** - SRE executed emergency rollback to `order-service:v2.4.0`.
- **14:31** - Database connection pool recovered; checkout error rates dropped to 0.01%.
- **14:44** - War room stood down; all systems verified healthy.

---

## 3. Contributing Systemic Factors
*(Focus on system flaws, missing safeguards, and tooling gaps — NOT human error)*
1. The integration test suite lacked automated index-check assertions on new queries.
2. The canary analysis threshold required 10 minutes of execution before evaluation, allowing unindexed queries to hit the production database cluster before tripping.

---

## 4. Corrective Preventative Action Items
| Action Item | Type | Owner | Target Date | Jira Epic |
|:---|:---:|:---|:---:|:---|
| Add automated query EXPLAIN linter in PR pipeline | Prevent | DB Team | 2026-09-19 | PLAT-401 |
| Shorten canary failure reaction window from 10m to 2m | Detect | SRE Lead | 2026-09-12 | SRE-108 |
```
