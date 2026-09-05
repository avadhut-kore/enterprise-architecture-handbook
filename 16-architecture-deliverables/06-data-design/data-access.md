# Data Access & Connection Pool Standards

## 1. Connection Pool Tuning (HikariCP / pgBouncer)
* Formula: `connections = ((cpu_cores * 2) + effective_spindle_count)`.
* Enforce statement timeouts on all connections (max 5,000ms) to kill runaway queries.
