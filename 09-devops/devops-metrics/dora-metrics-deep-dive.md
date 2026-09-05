# DORA Metrics Deep Dive: Measurement & Anti-Gaming

The DevOps Research and Assessment (DORA) metrics provide an empirical, research-backed framework for measuring software delivery performance.

## 1. The Four Core DORA Metrics

```
┌─────────────────────────────────────────────────────────────┐
│                    VELOCITY & THROUGHPUT                    │
├──────────────────────────────┬──────────────────────────────┤
│ 1. DEPLOYMENT FREQUENCY      │ 2. LEAD TIME FOR CHANGES     │
│ How often code deploys to    │ Time from commit to running  │
│ production.                  │ in production.               │
│ Elite: Multiple deploys/day  │ Elite: < 1 hour              │
├──────────────────────────────┴──────────────────────────────┤
│                    STABILITY & RELIABILITY                  │
├──────────────────────────────┬──────────────────────────────┤
│ 3. CHANGE FAILURE RATE (CFR) │ 4. TIME TO RESTORE (MTTR)    │
│ % of deploys causing Sev-1   │ Time to recover from a       │
│ or production degradation.   │ production failure.          │
│ Elite: 0% - 15%              │ Elite: < 1 hour              │
└──────────────────────────────┴──────────────────────────────┘
```

## 2. Common Anti-Gaming Traps & Solutions

| Metric | How Teams Game It (Dysfunction) | Architectural Countermeasure |
| :--- | :--- | :--- |
| **Deployment Frequency** | Deploying trivial 1-character comment changes to inflate numbers. | Measure only commits tied to verified user stories or feature Jira tickets. |
| **Lead Time for Changes** | Keeping branches local for 3 weeks and only opening PR when fully finished. | Measure from first commit timestamp in the branch, not PR creation time. |
| **Change Failure Rate** | Refusing to declare Sev-1 incidents for small rollbacks. | Correlate CFR automatically with rollbacks and alert spikes via automated PagerDuty webhooks. |
| **Time to Restore** | Closing the incident ticket immediately and fixing the root cause later in silence. | Measure MTTR against SLO recovery telemetry rather than human ticket status updates. |

## Related Resources
- [DevOps Economics](../devops-economics/README.md)
- [SRE & Observability Architecture](../../11-observability/README.md)
