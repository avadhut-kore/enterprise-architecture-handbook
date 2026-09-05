# Database Rollback Strategies & Forward-Fix Protocols

## 1. The Asymmetric Rollback Dilemma
Application rollbacks are trivial (redeploy the previous container image). Database rollbacks are complex because new transactions have been committed to the new database that do not exist in the legacy database.

---

## 2. Reverse CDC for Zero-Data-Loss Rollback
Maintain **reverse CDC replication** from the modern database back to the legacy database for 14 to 30 days post-cutover:
- If a critical bug mandates rolling back the application to the legacy monolith, the legacy database is already fully hydrated with all post-cutover transactions.
