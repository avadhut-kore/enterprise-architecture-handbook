# The 15-Stage Database Schema Splitting Playbook

## 1. End-to-End Execution Sequence

```
Phase 1: Discovery & Dependency Mapping
  1. Inventory Tables, Views, Stored Procedures, and Triggers
  2. Map Table Read/Write Access by Application
  3. Classify Shared Tables (Entity, Reference, Join)

Phase 2: Logical Isolation
  4. Break Cross-Domain Foreign Keys (Replace with Value Objects)
  5. Refactor Stored Procedures into Application Domain Code
  6. Partition Single Schema into Logical Schemas (Schema-per-Service)

Phase 3: Asynchronous Replication & Dual-Run
  7. Deploy Log-Based CDC (Debezium) on Source Database
  8. Execute Zero-Downtime Historical Backfill to Target DB
  9. Continuous CDC Replication Hydration & Sync

Phase 4: Verification & Cutover
  10. Shadow Reads: Validate Query Equivalence & Latency
  11. Continuous Automated Reconciliation & Parity Verification
  12. Switch Writes to Modern Target Database
  13. Reverse CDC: Stream Writes Back to Legacy for Safe Rollback

Phase 5: Decommissioning
  14. Disconnect Legacy Read-Replicas and Applications
  15. Drop Extracted Tables from Monolithic Database
```
