# Incident Timeline Reconstruction Forensic Guide

## 1. Forensic Principles for Timeline Construction
A post-mortem is only as valid as its timeline. Flawed timelines lead to incorrect causal conclusions. When reconstructing timelines following an enterprise outage, adhere to the following four forensic principles:

1. **Standardize on UTC**: Reconcile all system clocks, application logs, cloud provider statuses, and chat timestamps to Coordinated Universal Time (UTC).
2. **Anchor on Telemetry, Not Human Memory**: Humans under stress misremember durations. Anchor events strictly on immutable telemetry records: CloudTrail logs, TCP packet captures, database write-ahead logs, and time-series metrics.
3. **Capture the Latent Phase**: The incident almost never begins when the alert fires. Identify the **True Trigger Event** (e.g., a git commit 3 days prior, a routine cron job, or a gradual memory leak).
4. **Annotate State Transitions**: Clearly identify when the system transitioned between operational states: `Nominal` $\rightarrow$ `Degraded` $\rightarrow$ `Failed` $\rightarrow$ `Mitigating` $\rightarrow$ `Recovered`.

---

## 2. Telemetry Evidence Collection Rubric

```
                       [EVIDENCE RECONCILIATION PIPELINE]
                                       │
     ┌───────────────────┬─────────────┴─────────────┬───────────────────┐
     ▼                   ▼                           ▼                   ▼
[EDGE & INGRESS]    [APPLICATION RUNTIME]       [PERSISTENCE TIER]   [ORCHESTRATION]
 - CDN access logs   - Distributed traces (APM)  - DB slow query log  - K8s event logs
 - WAF drop logs     - JVM GC logs               - DB transaction log - CloudTrail logs
 - NLB TCP metrics   - Container stdout/stderr   - Lock wait traces   - BGP route tables
```

---

## 3. Timeline Reconstruction Template

```markdown
### Forensic Timestamp Log
- **[YYYY-MM-DD 14:02:11 UTC] - Trigger Injected**:
  - *Telemetry Source*: AWS CloudTrail `UpdateFunctionConfiguration`
  - *Observation*: Deployment of Lambda worker v2.4.1 modifying environment variable `MAX_CONCURRENCY`.

- **[YYYY-MM-DD 14:05:30 UTC] - Latent Symptom Emerges**:
  - *Telemetry Source*: Prometheus metric `container_cpu_usage_seconds_total`
  - *Observation*: Worker CPU spikes to 98%; thread queue depth begins linear climb from 10 to 450.

- **[YYYY-MM-DD 14:08:00 UTC] - Threshold Breach & Alert Fired**:
  - *Telemetry Source*: PagerDuty Incident `#84920`
  - *Observation*: Alert `High5xxErrorRate` triggers on API Gateway (5xx errors exceed 5.0%).

- **[YYYY-MM-DD 14:12:00 UTC] - Engineering Bridge Opened**:
  - *Telemetry Source*: Slack Incident Channel `#inc-2024-03-12`
  - *Observation*: On-Call SRE declares P1 incident; Incident Commander role established.

- **[YYYY-MM-DD 14:45:00 UTC] - Mitigation Executed**:
  - *Telemetry Source*: GitOps ArgoCD Sync Log
  - *Observation*: Rollback to Lambda worker v2.4.0 initiated.

- **[YYYY-MM-DD 14:52:00 UTC] - Recovery Verified**:
  - *Telemetry Source*: Datadog APM Trace Latency Dashboard
  - *Observation*: P99 latency returns to baseline (42ms); error rate drops to 0.00%.
```
