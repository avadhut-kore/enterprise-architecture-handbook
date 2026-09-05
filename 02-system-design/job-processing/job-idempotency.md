# Job Idempotency Architecture

## 1. Deduplication Keys
Every job should carry a deterministic **Idempotency Key / Job ID**:
$$\text{Job ID} = \text{SHA256}(\text{JobType} + \text{EntityID} + \text{DateWindow})$$
* For daily payroll: `Job ID = SHA256("payroll_monthly" + "emp_42" + "2026-09")`.
* If network retries enqueue the job 5 times, the queue deduplicates based on Job ID and executes only once.
