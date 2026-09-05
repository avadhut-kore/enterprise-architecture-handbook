# Database DevOps & Continuous Schema Evolution

Deploying database schema changes requires fundamentally different architecture than deploying stateless code. A bad application deployment can be rolled back in 30 seconds; a corrupted database migration can destroy multi-million-dollar datasets.

## 1. The Expand/Contract (Parallel Run) Pattern

To achieve zero-downtime database migrations without table locks:

```
PHASE 1: EXPAND
- Add new column `full_name` (Nullable) alongside old `first_name`, `last_name`.
- Application writes to BOTH old and new columns; reads from old.

PHASE 2: BACKFILL
- Run background batch job to populate `full_name` for historical rows.

PHASE 3: SWITCH READS
- Deploy new application version reading from `full_name`.

PHASE 4: CONTRACT
- Drop old columns `first_name`, `last_name` in a subsequent release.
```

## 2. Database CI/CD Pipeline Standards
1. **Migration Tooling as Code**: Track migrations via declarative or versioned SQL files (Flyway / Liquibase / Prisma).
2. **Automated Schema Linting**: Run CI checks (e.g., `pg-roll`, `squawk`) to block non-backward-compatible DDL (e.g., adding a non-nullable column without default).
3. **Lock Timeout Enforcement**: Mandate `SET lock_timeout = '2s';` in all production migration scripts to prevent queue lock contention on active tables.

## Related Resources
- [Data Architecture](../../06-data/README.md)
- [Enterprise Failure Modes Post-Mortems](../../24-architect-mastery/failure-analysis/enterprise-failure-modes-post-mortems.md)
