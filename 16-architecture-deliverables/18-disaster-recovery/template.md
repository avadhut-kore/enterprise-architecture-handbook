# Disaster Recovery Plan: [SYSTEM NAME]

---
**Metadata**:
```yaml
dr_id: "DR-PLAN-[PROJECT-ID]"
title: "Disaster Recovery Plan — [System Name]"
system_tier: "Tier 1 (Mission Critical)"
rto_target: "30 Seconds"
rpo_target: "0 Seconds (Zero Data Loss)"
strategy: "Multi-Region Active-Active"
lead_sre: "[Lead SRE / DR Coordinator <email>]"
created_date: "YYYY-MM-DD"
```
---

## 1. Business Impact Analysis (BIA) & Targets
* Financial cost of downtime: $25,000 per minute.
* Regulatory penalty: Severe reporting mandate after 15 minutes of continuous outage.

## 2. Disaster Recovery Strategy: Active-Active
* Primary Region: `us-east-1` (AWS Northern Virginia).
* Secondary Region: `eu-west-1` (AWS Ireland).
* Persistence: CockroachDB distributed SQL running across both regions.

## 3. Automated Failover Sequence
```mermaid
sequenceDiagram
    autonumber
    participant Mon as Route 53 Health Checks
    participant DNS as Route 53 DNS
    participant RegA as Region us-east-1
    participant RegB as Region eu-west-1
    
    Note over RegA: Catastrophic Regional Outage
    Mon->>RegA: Health Check probe fails (3 consecutive 503s)
    Mon->>DNS: Mark us-east-1 endpoint UNHEALTHY
    DNS->>DNS: Shift 100% of global traffic to eu-west-1
    Note over RegB: Absorbs full traffic; nodes auto-scale
```

## 4. Testing & Verification Schedule
* Quarterly chaos Game Day: Simulate region severance and verify automated recovery.
