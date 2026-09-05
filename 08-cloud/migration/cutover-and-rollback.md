# Migration Cutover Windows, Validation & Rollback Runbooks

## Executive Summary

The cutover window is the critical transition period where live production traffic is redirected from the legacy environment to the cloud. Flawless execution requires deterministic runbooks.

---

## 1. The Cutover Hour-by-Hour Runbook Blueprint

| Time (T-Minus) | Action Item | Responsible Role | Rollback Gate? |
| :--- | :--- | :--- | :---: |
| **T - 4 Hours** | Verify CDC database replication lag is under 2 seconds. | Lead DBA | **YES** |
| **T - 2 Hours** | Lower public DNS TTL to 60 seconds. | Network SRE | No |
| **T - 30 Mins** | Place legacy application in read-only maintenance mode. | App Lead | No |
| **T - 15 Mins** | Verify zero in-flight transactions; validate record counts. | Data Architect | **YES** |
| **T - 0 Mins** | Promote cloud database to master; point cloud apps to DB. | Cloud SRE | No |
| **T + 5 Mins** | Shift Anycast DNS / Load Balancer to cloud landing zone. | Network SRE | No |
| **T + 15 Mins** | Execute automated synthetic smoke test suite. | QA / SRE Lead | **YES** |
| **T + 30 Mins** | Open system to live customer traffic; monitor error rates. | Incident Commander| No |
