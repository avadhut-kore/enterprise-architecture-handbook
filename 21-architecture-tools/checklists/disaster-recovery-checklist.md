# Disaster Recovery (DR) & Business Continuity Checklist

Validate multi-region recovery strategies, backup integrity, failover mechanisms, and RPO/RTO adherence.

---

## 1. Objectives & Tiering
* [ ] **Tier Assigned**: Is the service categorized into a standard DR tier (Tier 0 Mission-Critical, Tier 1 Core, Tier 2 Supporting)?
* [ ] **RPO Defined & Agreed**: Is the Recovery Point Objective (e.g., RPO `< 1 minute`) formally agreed to by business leadership?
* [ ] **RTO Defined & Agreed**: Is the Recovery Time Objective (e.g., RTO `< 15 minutes`) formally agreed to by business leadership?

---

## 2. Backup Integrity & Restoration
* [ ] **Automated Daily Backups**: Are database and volume snapshots automated and executed daily?
* [ ] **Cross-Region Replication**: Are backup snapshots automatically replicated to a secondary, geographically isolated cloud region?
* [ ] **Immutable Backups (WORM)**: Are backups locked using S3 Object Lock / WORM to prevent deletion during a ransomware attack?
* [ ] **Restoration Drill**: Has a full database restoration from backup been successfully performed and timed within the last 90 days?

---

## 3. Network & DNS Traffic Steering
* [ ] **Global DNS Health Checks**: Are Route 53 / Cloudflare DNS health probes configured with fast interval (10s) checking origin health?
* [ ] **Automated Traffic Rerouting**: Does DNS automatically shift traffic away from the primary region if 3 consecutive health checks fail?
* [ ] **Low DNS TTL**: Is DNS TTL set to `<= 60 seconds` on customer-facing endpoints to prevent client-side DNS caching during a failover?
* [ ] **Static IP / Anycast Support**: Are ingress endpoints backed by Anycast IPs (AWS Global Accelerator / Cloudflare) to minimize BGP convergence delays?

---

## 4. Multi-Region Data Synchronization
* [ ] **Replication Lag Monitoring**: Is database replication lag between primary and secondary regions continuously tracked with alerts firing if lag exceeds 30 seconds?
* [ ] **Split-Brain Mitigation**: In active-active setups, is there a deterministic conflict resolution mechanism (Last-Write-Wins, CRDTs, or region-partitioned keys)?
* [ ] **Async Queue Replay**: Is there a runbook to replay uncommitted messages from transactional outbox tables following database promotion?

---

## 5. DR Testing & Incident Simulation
* [ ] **GameDay Schedule**: Is a full Disaster Recovery GameDay scheduled at least bi-annually?
* [ ] **Blackhole Simulation**: Has the primary cloud region been intentionally disconnected to measure actual wall-clock recovery time?
* [ ] **Fallback / Failback Plan**: Is there a documented procedure to safely restore traffic back to the primary region without data loss once normal service is restored?
* [ ] **Post-DR Drill Audit**: Are post-drill findings recorded in the Risk Register with assigned remediation owners?
