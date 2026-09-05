# Database Backward Compatibility: Expand-Contract Pattern

## Executive Summary

Never execute breaking database schema changes (e.g., renaming a column or dropping a table) in a single deployment.

---

## The 3-Step Expand-Contract Migration Pattern
1. **Expand Phase**: Add the new column (`first_name`, `last_name`) alongside the old column (`full_name`). Application code writes to *both* columns, but reads from the old.
2. **Backfill Phase**: Asynchronously backfill historical data from old column to new column.
3. **Contract Phase**: Release updated application that reads from new column. Once stable, safely drop the old column in a subsequent release.
