# Architecture Review Board (ARB): System Design Review Questionnaire

## 1. Purpose & Review Governance

This formal questionnaire is utilized by the Architecture Review Board (ARB), Principal Architects, and Lead Reviewers during Architecture Governance Gates to evaluate proposed system designs before engineering implementation commences.

A system design cannot pass sign-off if critical risks ("Red Flags") in sections 2 through 10 remain unresolved.

---

## 2. Requirements, Scope & Sizing Evaluation

```
+----+-----------------------------------------------------------------------+--------+
| #  | Question                                                              | Status |
+----+-----------------------------------------------------------------------+--------+
| 2.1| Are functional requirements scoped to clear, verifiable user journeys?| [ ]    |
| 2.2| What explicit capabilities are classified as OUT of scope for Phase 1?| [ ]    |
| 2.3| Is the target availability SLA justified by business cost of downtime?| [ ]    |
| 2.4| Are average QPS, peak QPS, and read/write ratios mathematically sized?| [ ]    |
| 2.5| Is 3-year cumulative data storage estimated with replication overhead?| [ ]    |
+----+-----------------------------------------------------------------------+--------+
```

---

## 3. Architecture Topology & Structural Boundaries

```
+----+-----------------------------------------------------------------------+--------+
| #  | Question                                                              | Status |
+----+-----------------------------------------------------------------------+--------+
| 3.1| Is there a clear separation between edge, compute, and data tiers?    | [ ]    |
| 3.2| Are microservice boundaries aligned with DDD Bounded Contexts?        | [ ]    |
| 3.3| Are compute nodes 100% stateless and horizontally auto-scalable?      | [ ]    |
| 3.4| Has any Single Point of Failure (SPOF) been identified in the path?   | [ ]    |
| 3.5| Are third-party dependencies isolated behind an Anti-Corruption Layer?| [ ]    |
+----+-----------------------------------------------------------------------+--------+
```

---

## 4. Data Modeling, Storage & Consistency

```
+----+-----------------------------------------------------------------------+--------+
| #  | Question                                                              | Status |
+----+-----------------------------------------------------------------------+--------+
| 4.1| Is the choice between SQL and NoSQL justified by concrete queries?    | [ ]    |
| 4.2| What is the shard key, and does it guarantee uniform traffic spread?  | [ ]    |
| 4.3| Are cross-shard distributed joins completely eliminated from OLTP?    | [ ]    |
| 4.4| If eventual consistency is used, how is replication lag handled?      | [ ]    |
| 4.5| Are write conflicts resolved via CAS, Vector Clocks, or Domain Union? | [ ]    |
+----+-----------------------------------------------------------------------+--------+
```

---

## 5. Resilience & Failure Engineering

```
+----+-----------------------------------------------------------------------+--------+
| #  | Question                                                              | Status |
+----+-----------------------------------------------------------------------+--------+
| 5.1| Are hard timeouts configured on EVERY remote network invocation?      | [ ]    |
| 5.2| Do all retries use Exponential Backoff with randomized Full Jitter?   | [ ]    |
| 5.3| Are circuit breakers and bulkheads configured for external systems?   | [ ]    |
| 5.4| How does the system handle split-brain or network partitions?         | [ ]    |
| 5.5| Is there a Dead-Letter Queue (DLQ) configured for poison messages?    | [ ]    |
+----+-----------------------------------------------------------------------+--------+
```

---

## 6. Performance, Caching & Latency Budgets

```
+----+-----------------------------------------------------------------------+--------+
| #  | Question                                                              | Status |
+----+-----------------------------------------------------------------------+--------+
| 6.1| Is the end-to-end P99 latency budget broken down across hops?          | [ ]    |
| 6.2| Is cache stampede defended against via distributed locks or XFetch?   | [ ]    |
| 6.3| Are database connection pools sized based on CPU cores and I/O?       | [ ]    |
| 6.4| Have all primary database queries been validated with EXPLAIN ANALYZE?| [ ]    |
+----+-----------------------------------------------------------------------+--------+
```

---

## 7. Security, Identity & Compliance

```
+----+-----------------------------------------------------------------------+--------+
| #  | Question                                                              | Status |
+----+-----------------------------------------------------------------------+--------+
| 7.1| Is TLS 1.3 enforced at ingress and mTLS enforced internally?          | [ ]    |
| 7.2| Are cryptographic tokens (JWT) validated statelessly at the edge?     | [ ]    |
| 7.3| Is data encrypted at rest with customer-managed keys (KMS)?           | [ ]    |
| 7.4| Does the design comply with data residency and GDPR/HIPAA mandates?   | [ ]    |
+----+-----------------------------------------------------------------------+--------+
```

---

## 8. Observability & Telemetry

```
+----+-----------------------------------------------------------------------+--------+
| #  | Question                                                              | Status |
+----+-----------------------------------------------------------------------+--------+
| 8.1| Is distributed tracing implemented with W3C traceparent propagation?  | [ ]    |
| 8.2| Are Golden Signals (Latency, Traffic, Errors, Saturation) monitored?  | [ ]    |
| 8.3| Do logs omit sensitive PII while containing correlated trace IDs?     | [ ]    |
| 8.4| Are alerting thresholds tied to user-facing SLO burn rates?           | [ ]    |
+----+-----------------------------------------------------------------------+--------+
```

---

## 9. Production Readiness & Disaster Recovery

```
+----+-----------------------------------------------------------------------+--------+
| #  | Question                                                              | Status |
+----+-----------------------------------------------------------------------+--------+
| 9.1| What are the documented RPO (Recovery Point) and RTO (Recovery Time)? | [ ]    |
| 9.2| Can the deployment be rolled back within 10 minutes without data loss?| [ ]    |
| 9.3| Has load testing been conducted at 200% peak projected traffic?       | [ ]    |
| 9.4| Are operational runbooks written for top 5 critical alerts?           | [ ]    |
+----+-----------------------------------------------------------------------+--------+
```

---

## 10. Review Sign-Off Recommendation

```
[ ] APPROVED: Design meets all enterprise standards; proceed to engineering.
[ ] CONDITIONALLY APPROVED: Proceed with engineering subject to closing minor items.
[ ] REJECTED: Critical architectural defects identified; revise and resubmit to ARB.

Lead Reviewer Signature: _______________________ Date: _________________
```
