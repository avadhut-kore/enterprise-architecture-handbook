# Modernization Rollback Architecture & Procedures

## 1. The Rollback Spectrum
Rollback is not simply running `git revert`. In enterprise modernization, a rollback must coordinate across four distinct tiers:
1. **Network Tier**: Reverting DNS records, load balancer listener targets, and API gateway routes.
2. **Application Tier**: Redeploying legacy container images or unpausing legacy VM services.
3. **Database Tier**: Reversing database migrations, unfreezing legacy write permissions, and syncing delta transactions.
4. **Data Synchronization Tier**: Replaying missed transactions via reverse CDC.

---

## 2. Reverse CDC for Zero-Data-Loss Rollback
When traffic is shifted to the modern system, customers create new orders and transfer money. If the modern system crashes 3 hours later and requires a rollback:
- **Catastrophic Failure**: Simply reverting to the old database loses 3 hours of customer transactions!
- **Architectural Solution**: Maintain **Reverse CDC replication** streaming all transactions committed on the modern database back to the legacy database in real-time. If rollback occurs, the legacy database is already fully up-to-date!
