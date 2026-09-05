# Strangler Fig Pattern and Data Migration

The Strangler Fig pattern gradually replaces specific parts of a legacy system until the new system emerges and the old can be safely decommissioned.

## 1. The 4-Phase Strangler Migration Blueprint

```
Phase 1: Intercept -> API Gateway proxies traffic; all calls hit legacy.
Phase 2: Shadow    -> Gateway forks traffic to new microservice; compare outputs.
Phase 3: Migrate   -> New service becomes primary for writes; sync back to legacy.
Phase 4: Strangle  -> Decommission legacy route; legacy endpoint turned off.
```

## 2. Zero-Downtime Data Migration Architecture
1. **Historical Backfill**: Bulk export baseline records from legacy database to target datastore.
2. **Change Data Capture (CDC)**: Deploy Debezium to stream legacy database transaction logs (WAL) to Kafka.
3. **Consumer Replay**: Stream consumer replays CDC events to target database with upsert semantics until replication lag reaches sub-second parity.
4. **Cutover & Verification**: Flip DNS or Gateway routing rules.

## Related Modules
- [Legacy Modernization Mastery](file:///d:/company/products/enterprise-architecture-handbook/24-architect-mastery/modernization/legacy-modernization-mastery.md)
- [Enterprise Integration](../../14-enterprise-integration/README.md)
