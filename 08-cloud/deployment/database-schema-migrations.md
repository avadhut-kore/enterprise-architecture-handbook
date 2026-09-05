# Zero-Downtime Database Schema Migrations: The Expand-Contract Pattern

## Executive Summary

While compute instances can be swapped instantly, database schemas cannot. Dropping or renaming a column while old code is running crashes the application. Zero-downtime database changes require the **Expand-Contract (Parallel-Run) Pattern**.

---

## 1. The Expand-Contract Four-Phase Migration

```mermaid
graph TD
    Phase1[Phase 1: Expand - Add New Column 'full_name' alongside Old Columns 'first_name' and 'last_name']
    Phase2[Phase 2: Dual-Write - Deploy Application v1.1 writing to BOTH old and new columns]
    Phase3[Phase 3: Backfill - Run background batch script migrating historical rows to 'full_name']
    Phase4[Phase 4: Contract - Deploy Application v1.2 reading ONLY 'full_name'; Drop old columns in DB]

    Phase1 --> Phase2 --> Phase3 --> Phase4
```

---

## 2. Invariant Database Deployment Rules
1. **Never Execute Destructive DDL Simultaneously with Code**: Never drop tables or columns in the same release that updates application queries.
2. **All Schema Migrations Must Be Backward-Compatible**: The database schema must always support the previous version of application code ($N-1$) to allow instantaneous compute rollbacks without database surgery.
