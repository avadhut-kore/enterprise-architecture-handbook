# Cloud Disaster Recovery Checklist

- [ ] RTO and RPO mathematically modeled against business financial outage costs.
- [ ] Cross-region asynchronous database replication active (Aurora Global DB / Azure Auto-Failover Group).
- [ ] Secondary region infrastructure codified 100% in Terraform and verified via automated synthetic builds.
- [ ] Global Anycast or DNS failover routing configured with 60-second TTLs and flapping suppression.
- [ ] Unannounced DR game day drill executed in staging environment within the last 90 days.
