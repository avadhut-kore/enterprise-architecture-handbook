# Production Readiness Review (PRR) Guide

## Overview

The Production Readiness Review (PRR)—pioneered by Google Site Reliability Engineering (SRE)—is the final operational governance checkpoint conducted approximately **two weeks prior to general commercial availability (GA)**. 

While earlier reviews evaluate design blueprints and theoretical capacity, the PRR evaluates **working software, live deployment automation, telemetry dashboards, incident alerting rules, and disaster recovery runbooks**. The PRR answers one fundamental question: **"Is this system safe, operable, observable, and resilient enough to handle real customer traffic and 3:00 AM on-call emergencies without causing an enterprise disaster?"**

---

## The Production Readiness Checklist

```mermaid
mindmap
  root((PRR Verification))
    Observability & Telemetry
      Distributed Tracing Verified (W3C Headers)
      Structured JSON Logging in Central APM
      RED / USE Dashboards Configured
      SLO / SLI Alerting with Multi-Window Burn Rates
    Operational Runbooks
      Standard Operating Procedures (SOPs) Documented
      Incident Escalation Matrix Configured (PagerDuty)
      Graceful Degradation Switches Tested
    Deployment & Delivery
      Zero-Downtime Deployment Verified (Canary/Blue-Green)
      Automated Rollback Scripts Tested (< 60s rollback)
      Database Schema Migration Scripts Verified (Backward Compatible)
    Resilience & Chaos
      Simulated Node Kill / Container Crash Survived
      Primary DB Failover Drill Executed
      Third-Party Dependency Timeout Tested
    Security & Compliance
      Secret Rotation Policy Enforced
      Penetration Test Vulnerabilities Remediated
      KMS Encryption Keys Active & Verified
```

---

## 1. Zero-Downtime Deployment & Automated Rollback

Before commercial launch, the deployment pipeline must demonstrate automated zero-downtime execution in staging:
- **Canary Rollouts**: The orchestrator deploys a canary pod receiving 1% of live traffic. If error rates increase or latency breaches thresholds, the pipeline automatically halts and rolls back within **60 seconds** without human intervention.
- **Database Schema Expand-and-Contract**: All database schema migrations must be backwards-compatible:
  1. *Expand Phase*: Add new optional column; existing production code continues functioning without error.
  2. *Deploy Phase*: Deploy new application code writing to both old and new columns.
  3. *Contract Phase*: Remove old column in a subsequent deployment.

---

## 2. On-Call Runbooks & PagerDuty Integration

A system is not production-ready if the engineers who built it cannot explain how to troubleshoot it at 3:00 AM:
- **Alert Quality**: Every configured pager alert must be actionable. If an alert fires that requires no human action, it is noise and must be deleted.
- **Runbook Links**: Every alert delivered to PagerDuty or Slack must include a direct URL to a validated **Operational Runbook**:
  - What does this alert mean?
  - What is the business impact?
  - What are the first three diagnostic commands to run?
  - How do we trigger an immediate mitigation or service restart?

---

## 3. Chaos Engineering Verification Drill

The PRR mandates executing at least three live fault-injection experiments in pre-production:

| Chaos Experiment | Injected Fault | Expected System Behavior | PRR Pass Criteria |
|:---|:---|:---|:---:|
| **Pod / Node Termination** | Terminate 33% of worker pods during peak load | Remaining pods absorb traffic; Kubernetes spins up replacements within 45s | Zero dropped HTTP requests; p99 latency spike $< 100\text{ms}$ |
| **Primary DB Failover** | Force restart / crash on primary Aurora PostgreSQL node | Aurora elects standby replica; DNS flips automatically within 30s | System briefly returns cached data; writes resume within 35s |
| **Payment Partner Blackout**| Inject 10-second latency on Stripe mock API | Circuit breaker trips after 5 timeouts; checkout queues orders into offline buffer | Checkout UI returns `202 Accepted`; zero thread exhaustion |

---

## Production Readiness Review Sign-Off Template

```markdown
### Production Readiness Review (PRR) Determination: CLEARED FOR LAUNCH
- **System**: Global Digital Wallet & Ledger Service (GDW-100)
- **Lead SRE Reviewer**: Alex Rivera (Principal SRE)
- **Authoring Architect**: John Doe
- **Target Launch Date**: 2026-09-15

#### Verification Matrix
- [x] Automated Canary deployment verified in staging with automated rollback drill.
- [x] OpenTelemetry tracing verified across 100% of microservice RPC endpoints.
- [x] PagerDuty escalation policies configured and on-call rotation established.
- [x] Chaos experiments executed: Survives primary database failover with RPO = 0, RTO = 28 seconds.
- [x] All High/Critical penetration test vulnerabilities remediated and validated by SecOps.

#### Signatures
- **Lead SRE**: *Alex Rivera* (Signed: 2026-09-05)
- **Lead Solution Architect**: *John Doe* (Signed: 2026-09-05)
- **VP of Engineering**: *Michael Vance* (Signed: 2026-09-05)
```
