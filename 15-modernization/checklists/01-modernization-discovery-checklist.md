# Modernization Discovery Checklist

## 1. Architectural & Governance Review
- [ ] Has the business justification and economic TCO model been approved by executive stakeholders?
- [ ] Is the 11 Rs strategy formally documented and aligned with organizational risk appetite?
- [ ] Has an Anti-Corruption Layer (ACL) or API Facade been established to insulate dependencies?

## 2. Technical & Data Integrity Verification
- [ ] Are all state-mutating operations idempotent with validated deduplication keys?
- [ ] Is asynchronous data replication (CDC) active with replication lag $< 2	ext{ seconds}$?
- [ ] Are cross-system transactions managed via Saga orchestration rather than blocking 2PC?

## 3. Reliability & Rollback Assurance
- [ ] Is a non-destructive, tested rollback runbook documented with explicit time limits?
- [ ] Is reverse CDC synchronization configured from target database back to source database?
- [ ] Have automated smoke tests and shadow parity diffs reached 100% agreement?

## 4. Sign-Off & Approvals
| Role | Approver Name | Status | Date |
| :--- | :--- | :--- | :--- |
| **Lead Solution Architect** | | Approved | |
| **Security Architect** | | Approved | |
| **Lead DBA / Data Architect**| | Approved | |
| **Operations / SRE Commander**| | Approved | |
