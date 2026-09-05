# Enterprise Failure Modes Post-Mortems: 20 Architectural Breakdowns

This reference analyzes 20 high-severity architectural failures encountered in enterprise distributed systems, providing root-cause mechanics, impact, and systemic architectural mitigations.

---

### 1. Cascading Failure Across Microservices
- **Mechanics**: Service A calls Service B synchronously; Service B experiences slow database queries. Service A's HTTP worker threads become blocked waiting on B. Service A exhausts its connection pool, toppling upstream Services C, D, and the API Gateway.
- **Root Cause**: Lack of strict HTTP timeouts, missing circuit breakers, and unconstrained synchronous coupling.
- **Architectural Mitigation**: Enforce 500ms max client timeouts, implement Resilience4j/Envoy circuit breakers, and transition inter-service communication to asynchronous event-driven messaging.

---

### 2. Split-Brain in Distributed Database
- **Mechanics**: Network partition separates 5-node cluster into two partitions (2 nodes vs 3 nodes). Both sub-clusters believe the other is dead and accept writes, creating irreconcilable diverged logs.
- **Root Cause**: Misconfigured Raft/Paxos quorum (`min_nodes` set to 2 instead of `(N/2)+1 = 3`), or disabling fencing tokens during master failover.
- **Architectural Mitigation**: Enforce strict quorum majority rules; enable automated fencing tokens (STONITH / I/O fencing).

---

### 3. Distributed Transaction / 2PC Deadlock
- **Mechanics**: Two microservices execute two-phase commit across accounts. Node 1 locks Resource X and requests Y; Node 2 locks Resource Y and requests X. The coordinator crashes mid-prepare phase, leaving both resources locked indefinitely.
- **Root Cause**: Applying synchronous two-phase commit (XA transactions) across distributed WAN boundaries.
- **Architectural Mitigation**: Eliminate 2PC in favor of Asynchronous Sagas with compensating transactions and outbox pattern.

---

### 4. Thundering Herd / Cache Stampede
- **Mechanics**: A high-traffic cache key (e.g., Homepage Promo banner, 50,000 req/sec) expires at 12:00:00. 50,000 concurrent threads miss cache simultaneously and hit the primary SQL database, causing CPU saturation and complete outage.
- **Root Cause**: Deterministic TTL expiration without probabilistic early refresh or mutex locking.
- **Architectural Mitigation**: Implement XFetch (probabilistic early expiration) and distributed mutex locking (`singleflight` pattern in Go, Redis distributed locks for cache miss refill).

---

### 5. Retry Storm / Self-Inflicted DDoS
- **Mechanics**: Downstream payment API slows by 30%. Upstream callers retry immediately 3 times. Traffic to payment API quadruples instantly, driving it to complete collapse.
- **Root Cause**: Immediate retries without exponential backoff and randomized jitter.
- **Architectural Mitigation**: Mandatory exponential backoff with Full Jitter: `t_sleep = random(0, min(max_backoff, base * 2^attempt))`.

---

### 6. Kafka Consumer Group Rebalance Storm
- **Mechanics**: A consumer thread pauses for 45 seconds due to a full JVM garbage collection cycle. Kafka coordinator marks consumer dead and initiates a partition rebalance. Other consumers pause processing to rebalance, timing out their heartbeats, triggering an endless cascading rebalance loop.
- **Root Cause**: `max.poll.interval.ms` set too low relative to processing time, and stop-the-world GC pauses.
- **Architectural Mitigation**: Tune G1GC/ZGC for sub-10ms pauses, decouple Kafka consumption from heavy processing via internal thread pools, and enable Cooperative Sticky assignor.

---

### 7. Kubernetes OOM Killer Cascade
- **Mechanics**: Container memory limit set to 512MiB. A sudden burst of traffic causes memory to exceed 512MiB. Linux kernel cgroup OOM-kills the pod. Kubernetes shifts traffic to remaining pods, which immediately exceed memory and get killed in turn.
- **Root Cause**: Misconfigured memory limits (`resources.limits.memory` equal to average usage instead of peak headroom), missing HPA based on memory.
- **Architectural Mitigation**: Set memory requests equal to limits, configure Horizontal Pod Autoscaler (HPA) with safety headroom, and implement graceful memory eviction.

---

### 8. Database Connection Pool Exhaustion
- **Mechanics**: 100 microservice replicas each configure `max-pool-size: 50`. Total potential connections = 5,000. PostgreSQL `max_connections` is configured for 1,000. Under load, services fail to establish connections and crash.
- **Root Cause**: Client-side connection pooling without an intermediate connection multiplexer.
- **Architectural Mitigation**: Deploy PgBouncer or AWS RDS Proxy between applications and database in transaction-pooling mode.

---

### 9. DNS Propagation Failure During Regional Failover
- **Mechanics**: Primary US-East region fails. Operations updates Route53 DNS record to point to US-West. 40% of global client traffic continues hitting dead US-East for 24 hours.
- **Root Cause**: Upstream ISPs, intermediate proxy servers, and mobile client OS caching ignoring TTL and caching DNS for 86,400 seconds.
- **Architectural Mitigation**: Use Anycast IP addresses (AWS Global Accelerator / Cloudflare) rather than DNS-based failover for disaster recovery.

---

### 10. TLS Certificate Expiry Sev-1
- **Mechanics**: Internal mTLS certificate for Service Mesh ingress expires on Sunday at 02:00 UTC. All microservice-to-microservice communication rejects connections with `SSL_ERROR_EXPIRED`.
- **Root Cause**: Manual certificate renewals without automated monitoring or automated ACME cert-manager workflows.
- **Architectural Mitigation**: Deploy cert-manager with Let's Encrypt / HashiCorp Vault automated rotation, with Prometheus alerts firing at 30, 14, and 7 days prior to expiry.

---

### 11. Asynchronous Event Out-of-Order Execution
- **Mechanics**: User updates shipping address (Event A), then cancels order (Event B). Due to partition re-balancing and network retries, Event B is processed before Event A. The address update then re-activates the cancelled order.
- **Root Cause**: Missing causal versioning, monotonic sequence numbers, or idempotency keys on event payloads.
- **Architectural Mitigation**: Include entity version / monotonic sequence timestamp in event envelopes; ignore events with `event_version <= current_entity_version`.

---

### 12. Schema Migration Lock on Active Table
- **Mechanics**: Engineer runs `ALTER TABLE orders ADD COLUMN status VARCHAR(20) DEFAULT 'PENDING'` on a table with 100M rows. PostgreSQL acquires an `ACCESS EXCLUSIVE` table lock, blocking all subsequent reads and writes.
- **Root Cause**: Blocking DDL executed during business peak without non-blocking migration patterns.
- **Architectural Mitigation**: Use `lock_timeout = 2s`, add columns without default values, populate defaults asynchronously in batches, and use tools like pg-roll or gh-ost.

---

### 13. Silent Data Corruption Undetected for Months
- **Mechanics**: Floating point rounding error in a currency calculation library drops fractional cents. Over 6 months, financial ledger balances drift by $450,000 before discovered during annual audit.
- **Root Cause**: Using IEEE 754 floating-point primitives (`float`/`double`) for monetary values instead of arbitrary-precision integers or `BigDecimal`.
- **Architectural Mitigation**: Strict linting rules requiring integer cents or `BigDecimal`, combined with automated daily reconciliation batch jobs comparing debit/credit parity.

---

### 14. Cloud Runaway Cost Incident
- **Mechanics**: Developer enables an AWS Lambda function triggered by an S3 upload that writes an output file to the same S3 bucket. An infinite recursion event triggers 500M invocations over a weekend, generating a $68,000 AWS bill.
- **Root Cause**: Event feedback loop without circuit breaking or bucket prefix filters.
- **Architectural Mitigation**: AWS Budgets with automated SNS kill-switches, recursive loop detection (Lambda header `X-Amzn-Trace-Id`), and strict output bucket separation.

---

### 15. Third-Party SaaS Outage Cascading Internally
- **Mechanics**: Third-party address verification API suffers an outage and hangs for 30 seconds per request. The enterprise user registration funnel drops to 0% conversion.
- **Root Cause**: Inline synchronous dependency on external un-SLA'd third party.
- **Architectural Mitigation**: Asynchronous background address validation, or soft-failover allowing registration to proceed with unverified address marked for background reconciliation.

---

### 16. Multi-Tenant Noisy Neighbor CPU Starvation
- **Mechanics**: A massive enterprise tenant runs a complex historical export query. The shared multi-tenant database engine hits 100% CPU, starving 4,000 smaller tenants of normal transactional throughput.
- **Root Cause**: Lack of tenant resource isolation, query quotas, or compute pooling.
- **Architectural Mitigation**: Tenant-aware rate limiting, routing analytic queries to dedicated read replicas, and tiering large enterprise tenants to isolated compute instances.

---

### 17. Hot Partition in Distributed NoSQL
- **Mechanics**: DynamoDB / Cassandra table uses `country_code` as partition key. 85% of traffic hits `country_code = 'US'`, causing that specific physical partition to throttle, while other partition nodes sit idle at 2% CPU.
- **Root Cause**: Low-cardinality partition key leading to severe data skew.
- **Architectural Mitigation**: Synthetic sharding / salting: `partition_key = country_code + "_" + random(0, 10)`.

---

### 18. Memory Leak in Long-Running Container
- **Mechanics**: Node.js microservice accumulates unclosed database event listener handles on every request. Over 10 days, heap size slowly creeps from 200MB to 2GB until the process crashes.
- **Root Cause**: Uncleaned event emitters and unmanaged closures in long-lived server processes.
- **Architectural Mitigation**: Automated heap profiling in staging, setting `--max-old-space-size`, and periodic rolling restarts in container orchestrators.

---

### 19. Deadlock Under Concurrent Write Burst
- **Mechanics**: Two concurrent transactions update items in a shopping cart. Transaction 1 updates Item A then Item B. Transaction 2 updates Item B then Item A. Under peak concurrency, both transactions lock each other out.
- **Root Cause**: Non-deterministic ordering of row locks across concurrent transactions.
- **Architectural Mitigation**: Enforce deterministic locking order: sort primary keys before acquiring locks (`SELECT ... FOR UPDATE` ordered by `id ASC`).

---

### 20. Single-AZ Dependency Failure in Multi-AZ Design
- **Mechanics**: Architecture was designed with multi-AZ compute across `us-east-1a`, `1b`, and `1c`. However, the shared internal NAT Gateway was deployed in `us-east-1a` only. When AZ-1a went down, all three AZs lost external connectivity.
- **Root Cause**: Hidden single-zone dependency in shared network infrastructure.
- **Architectural Mitigation**: Full AZ-independent isolation: deploy dedicated NAT Gateways, ALB subnets, and service instances per AZ with zero cross-AZ dependencies for failure domains.

## Related Modules
- [War Stories](file:///d:/company/products/enterprise-architecture-handbook/24-architect-mastery/war-stories/README.md)
- [Incident-Driven Architecture](file:///d:/company/products/enterprise-architecture-handbook/24-architect-mastery/incident-driven-architecture/README.md)
