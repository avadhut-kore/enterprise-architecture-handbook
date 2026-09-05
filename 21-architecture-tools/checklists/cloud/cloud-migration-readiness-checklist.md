# Cloud Migration Readiness Checklist

- [ ] Automated discovery appliance deployed; application dependency map and Move Groups established.
- [ ] Database schema compatibility assessed via AWS Schema Conversion Tool (SCT) or Azure DMA.
- [ ] Continuous Change Data Capture (CDC) replication active with replication lag consistently < 2 seconds.
- [ ] Reverse replication pipeline configured from target cloud DB back to on-premises DB for zero-risk rollback.
- [ ] Cutover hour-by-hour runbook reviewed and approved by all stakeholders including rollback triggers.
