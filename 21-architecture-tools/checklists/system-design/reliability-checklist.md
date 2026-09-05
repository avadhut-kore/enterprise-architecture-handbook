# System Design Checklist: High Availability & Reliability

## 1. Redundancy & Failover
- [ ] Every component deployed with at least $N+1$ or $2N$ redundancy?
- [ ] Multi-AZ deployment active for all compute and database nodes?
- [ ] Automated database failover configured and tested (RPO < 1 min, RTO < 2 min)?
- [ ] Health checks distinguish between liveness (process alive) and readiness (ready for traffic)?

## 2. Backup & Disaster Recovery
- [ ] Daily automated snapshots and continuous transaction log backups enabled?
- [ ] Backup restoration drills scheduled quarterly to validate recovery time objectives?
