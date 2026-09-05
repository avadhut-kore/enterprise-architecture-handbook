# Requirements Traceability Matrix (RTM)

| Business Requirement | Functional Req ID | NFR ID | Architecture Component | LLD Class / Module | Test Case ID | Verification Status |
|---|---|---|---|---|---|---|
| BR-01 (Instant Transfer) | REQ-001 | NFR-LAT-01 | [HLD §3.1 Order Service](../03-hld/template.md) | `OrderServiceImpl.java` | TC-PERF-042 | Passed (p95: 110ms) |
| BR-02 (Zero Data Loss) | REQ-002 | NFR-REL-01 | [SAD §8 CockroachDB](../02-sad/template.md) | `LedgerRepositoryImpl.java` | TC-CHAOS-003 | Passed (RPO=0) |
