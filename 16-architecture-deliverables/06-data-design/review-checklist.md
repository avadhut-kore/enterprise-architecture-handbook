# Data Architecture Review Checklist

Use this 25-point checklist before finalizing a database or data storage design.

---

## 1. Schemas & Integrity
- [ ] Primary keys use collision-resistant identifiers (UUIDv7 or BigInt sequence).
- [ ] Monetary columns strictly use `NUMERIC(18, 4)` (no floating point types).
- [ ] Foreign keys are indexed to prevent full table locks.
- [ ] Check constraints enforce valid domain states.

## 2. Performance & Scaling
- [ ] Critical query paths have covering composite indexes.
- [ ] Unbounded tables implement range or hash partitioning.
- [ ] Connection pool limits are sized to prevent database CPU exhaustion.

## 3. Security, Privacy & Lifecycle
- [ ] PII data is classified, encrypted, and masked in non-production environments.
- [ ] Retention schedules and automated archival procedures are defined.
- [ ] Zero-downtime migration plans follow the Expand and Contract pattern.
