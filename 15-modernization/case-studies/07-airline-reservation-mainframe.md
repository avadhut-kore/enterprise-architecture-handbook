# Case Study: International Airline: Passenger Service Strangler

## 1. Executive Summary & Business Context
An airline extracted flight availability and seat booking from a legacy TPF mainframe, handling 25,000 queries/second during holiday flash sales.

---

## 2. The Legacy Architectural Dilemma
- **The Problem**: Decades of architectural debt, high licensing fees, brittle point-to-point connections, and deployment paralysis.
- **The Constraints**: Zero allowable downtime; strict regulatory compliance; mission-critical 24/7 operations.

---

## 3. Transition Architecture & Wave Strategy

```
Phase 1: Ingress Facade ──► Phase 2: CDC Sync ──► Phase 3: Shadow Run ──► Phase 4: Canary Cutover ──► Phase 5: Decommission
```

1. Deployed an API Gateway and Anti-Corruption Layer to insulate modern services.
2. Hydrated independent target databases via log-based Change Data Capture.
3. Validated parity using automated nightly reconciliation scripts.
4. Progressively cut over traffic using weighted DNS and feature flags.

---

## 4. Key Architectural Lessons Learned
1. **Never Attempt Big-Bang Replacement**: Incremental strangling with an active fallback is the only reliable path for mission-critical core systems.
2. **Reverse CDC Is Essential**: Always maintain reverse synchronization from the new system to the legacy system to enable instant, zero-data-loss rollback during cutover.
3. **Decommissioning Requires Discipline**: Legacy retirement must be treated as a formal program milestone with contractual sunset deadlines.
