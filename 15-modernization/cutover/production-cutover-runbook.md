# Production Cutover Runbook: T-30 Days to T+7 Days

## 1. Timeline & Execution Phases

```
T-30 Days: Rehearsal ──► T-7 Days: Code Freeze ──► T-1 Day: Go/No-Go ──► T-0: Cutover Window ──► T+1 Day: Verification ──► T+7 Days: Sign-Off
```

### T-30 Days: Full Migration Rehearsal
- Execute complete cutover simulation in staging environment using sanitized production data backup.
- Time every step down to the second; establish baseline execution durations.

### T-7 Days: Operational Freeze
- Enforce strict code and infrastructure freeze on both legacy and modern systems.
- Lower DNS TTL on all public domain records to 300 seconds (5 minutes).

### T-1 Day (Friday): Final Go/No-Go Gate
- Convene executive Architecture Review Board and Business Leads at 14:00.
- Verify zero open P1/P2 defects; verify successful staging dry-run; confirm Go decision.

### T-0 (Saturday Night): Cutover Execution Window

```
22:00 UTC - Open Cutover War Room Bridge; Incident Commander takes control.
22:15 UTC - Set Legacy Application to READ-ONLY mode; display maintenance banner.
22:30 UTC - Drain in-flight message queues and active HTTP sessions.
22:45 UTC - Take final incremental database backup; trigger CDC catch-up synchronization.
23:15 UTC - Run automated data reconciliation script; verify record counts and hash totals match 100%.
23:30 UTC - Switch DNS / API Gateway routing to Modern Cloud Target.
23:45 UTC - Execute automated smoke test suite (Smoke Test Automated Run: 250 test cases).
00:15 UTC - Business validation team executes manual checkout and verification transactions.
00:45 UTC - Formal "System Operational" declaration; lift maintenance banner.
```

### T+1 Day (Sunday): Intensive Monitoring
- Monitor real-time error rates, p99 latency, and database connection pool saturation.

### T+7 Days: Stabilization & Legacy Isolation
- Conclude hypercare period; revoke legacy write access permanently.
