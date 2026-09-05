# Parallel Run & Dual-Running Operations

## 1. The Parallel Run Model
In mission-critical financial, core banking, and payroll systems, organizations cannot rely on synthetic testing. A **Parallel Run** executes both the legacy and the modern systems concurrently against production inputs for an extended period (typically 30 to 90 days).

## 2. Dual Ledger Comparison
Outputs from both engines (e.g., calculated employee paychecks or interest accruals) are written to staging tables and compared row-by-row daily. The legacy system remains the legal system of record until 30 consecutive days of zero variances are achieved.
