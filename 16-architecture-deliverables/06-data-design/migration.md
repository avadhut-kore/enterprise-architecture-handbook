# Zero-Downtime Schema Migration Standards

## 1. Expand and Contract Pattern
1. **Expand**: Add new nullable column to table; deploy code writing to both old and new columns.
2. **Backfill**: Run background script populating historical rows in batches.
3. **Contract**: Update code to read from new column; drop old column in a subsequent release.
