# Checklist: Disaster Recovery Readiness Checklist

## Executive Summary
This operational checklist must be validated prior to production promotion.

---

## Verification Criteria
- [ ] RTO ($< 15	ext{ mins}$) and RPO ($< 1	ext{ min}$) mathematically verified.
- [ ] Secondary region infrastructure codified 100% in Terraform.
- [ ] Cross-region database replication active with lag $< 2	ext{ secs}$.
- [ ] Automated Anycast / DNS health failover tested.
- [ ] Unannounced DR game day executed in staging within last 90 days.
