# Multi-Cloud Disaster Recovery Strategy

## Executive Summary

Implementing cross-cloud disaster recovery requires clear operational definitions of Recovery Time Objective (RTO) and Recovery Point Objective (RPO), balanced against the massive cost of maintaining duplicate infrastructure.

---

## 1. Strategy Comparison

| DR Pattern | RTO | RPO | Cost Multiplier | Operational Complexity |
| :--- | :--- | :--- | :---: | :--- |
| **Backup & Restore to Cloud B** | 24–48 Hours | 12–24 Hours | $1.1\times$ | Low: Daily snapshots encrypted and copied to secondary cloud object storage. |
| **Pilot Light in Cloud B** | 1–4 Hours | Minutes | $1.3\times$ | Moderate: Core database running on small instance; compute clusters provisioned on-demand via Terraform. |
| **Warm Standby in Cloud B** | 15–30 Mins | Seconds | $1.8\times$ | High: Full compute fleet running at 20% capacity; continuous automated integration testing. |
| **Hot Standby (Active-Active)** | $< 1\text{ Min}$| Near-Zero | $2.5\times$ | Extreme: Prohibitive operational overhead; distributed consensus risks. |

---

## 2. Data Hydration & Schema Drift Governance

The primary failure mode in multi-cloud DR is **Schema and Environment Drift**:
- Application engineering updates the AWS production schema from v1.4 to v1.5.
- The Terraform or migration scripts for Azure are not updated concurrently.
- When an emergency cutover is triggered, the Azure compute instances fail to start due to missing database columns or configuration mismatches.
- **Rule**: Multi-cloud DR requires automated weekly end-to-end rehearsal drills in an isolated staging environment.
