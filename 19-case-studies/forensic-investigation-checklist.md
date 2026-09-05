# Architectural Forensic Investigation Checklist

Use this 50-point diagnostic checklist when investigating complex production outages, data corruptions, and architectural failures.

---

## 1. Trigger & Initial Symptoms
- [ ] What was the exact timestamp ($T_0$) of the first anomalous metric deviation?
- [ ] Was the event preceded by a code deployment, configuration change, or infrastructure update?
- [ ] Was there an abnormal external traffic surge, bot activity, or third-party outage?
- [ ] Did automated health checks detect the failure, or was it reported by customers?

## 2. Request Flow & Ingress Path
- [ ] Did the API Gateway or Load Balancer reject requests (HTTP 429, 502, 503, 504)?
- [ ] Were connection timeouts, socket read timeouts, or keep-alive limits reached?
- [ ] Did DNS resolution fail or suffer latency degradation?
- [ ] Was there any regional network partition or packet loss between availability zones?

## 3. Application & Microservices Tier
- [ ] Were CPU or memory utilization levels saturated (> 90%) on application pods?
- [ ] Did the JVM or runtime encounter Stop-The-World (STW) garbage collection pauses?
- [ ] Were worker threads or event-loop ticks blocked on synchronous I/O calls?
- [ ] Did downstream timeouts trigger aggressive, unbounded retry loops (retry storms)?
- [ ] Were circuit breakers configured, and did they trip as expected?

## 4. Database & Persistence Tier
- [ ] Did application connection pools (e.g., HikariCP) exhaust available connections?
- [ ] Were there long-running unindexed queries holding table or row-level locks?
- [ ] Did a distributed transaction (2PC / Saga) freeze in a partially committed state?
- [ ] Was database disk I/O (IOPS / write latency) saturated on primary or read replicas?
- [ ] Did replication lag between primary and secondary replicas exceed recovery thresholds?

## 5. Messaging & Event Streaming
- [ ] Did message queue depths or Kafka consumer group lag grow uncontrollably?
- [ ] Were any unparseable poison pill messages blocking event partition processing?
- [ ] Were message deduplication keys and idempotency checks functioning correctly?
- [ ] Did consumer group rebalances stall event delivery across the cluster?

## 6. Data Integrity & Drift
- [ ] Was any committed data lost, overwritten, or corrupted during the incident?
- [ ] Did dual writes create inconsistencies between primary and secondary stores?
- [ ] Was an automated reconciliation script executed to quantify drift?
- [ ] Can data be reconstructed from immutable audit logs or event streams?

## 7. Security & Access Boundaries
- [ ] Was there any evidence of unauthorized credential use or privilege escalation?
- [ ] Were rate limits bypassed via distributed IP rotation?
- [ ] Did cross-tenant data leakage occur in multi-tenant shared tables?
- [ ] Were cryptographic keys, certificates, or tokens expired?

## 8. Rollback & Remediation
- [ ] Was a rollback initiated, and did it succeed cleanly without data loss?
- [ ] Did feature flags allow instantaneous kill-switch isolation?
- [ ] Was failover to a secondary availability zone or region attempted?
- [ ] Did failover exacerbate the issue due to cold caches or unprovisioned capacity?

## 9. Observability & Telemetry
- [ ] Did distributed tracing (OpenTelemetry) pinpoint the exact failing service hop?
- [ ] Were logs truncated, dropped, or throttled due to logging pipeline saturation?
- [ ] Were SLO error budget burn alerts triggered before business impact escalated?
- [ ] Was the incident timeline reconstructible with sub-second precision?

## 10. Organization & Governance
- [ ] Who was the designated Incident Commander, and was communication clear?
- [ ] Were emergency runbooks accurate, accessible, and up-to-date?
- [ ] Did team silos impede cross-functional diagnosis during the bridge?
- [ ] What architectural trade-off or technical debt directly enabled this failure?
