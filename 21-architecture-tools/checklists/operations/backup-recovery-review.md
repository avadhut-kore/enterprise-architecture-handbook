# Checklist: Backup & Recovery Operations Checklist

## Executive Summary
This operational checklist must be validated prior to production promotion.

---

## Verification Criteria
- [ ] 3-2-1-1-0 backup rule enforced across all datastores.
- [ ] Backups locked in S3 Compliance Mode (WORM) to prevent ransomware deletion.
- [ ] Cross-region automated replication of backup snapshots active.
- [ ] Automated monthly restore drill restores database and passes integrity tests.
- [ ] Measured recovery time matches business RTO commitments.
