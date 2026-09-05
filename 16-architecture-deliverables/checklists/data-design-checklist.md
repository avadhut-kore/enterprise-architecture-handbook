# Data Design Checklist
- [ ] Primary keys use collision-resistant identifiers (UUIDv7 or BigInt).
- [ ] Financial amounts strictly use `NUMERIC(18, 4)` (no floats).
- [ ] Foreign key columns have supporting B-Tree indexes.
- [ ] PII data classified, encrypted, and masked in non-prod.
