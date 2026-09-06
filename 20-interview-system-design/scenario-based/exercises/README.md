# Architecture Judgment Exercises: 10 Crisis Simulations

> 10 hands-on production, architectural, and organizational crisis simulations featuring incident prompts, diagnostic investigation workflows, immediate mitigations, and long-term architectural hardening.

---

## Crisis Simulation Catalog

1. [Exercise 1: Primary Database Crash During Peak Flash Sale](#exercise-1-primary-database-crash-during-peak-flash-sale)
2. [Exercise 2: Global Latency Spike Across All Services (The 1500ms Regression)](#exercise-2-global-latency-spike-across-all-services-the-1500ms-regression)
3. [Exercise 3: Uncontrolled Regional Cloud Outage (us-east-1 Black Hole)](#exercise-3-uncontrolled-regional-cloud-outage-us-east-1-black-hole)
4. [Exercise 4: The 10-Million Message Kafka Consumer Backlog](#exercise-4-the-10-million-message-kafka-consumer-backlog)
5. [Exercise 5: Distributed Cache Cluster Collapse (The Thundering Herd)](#exercise-5-distributed-cache-cluster-collapse-the-thundering-herd)
6. [Exercise 6: External Payment Gateway 5-Second Hang](#exercise-6-external-payment-gateway-5-second-hang)
7. [Exercise 7: Production SSL/TLS Certificate Expiration at Midnight](#exercise-7-production-ssltls-certificate-expiration-at-midnight)
8. [Exercise 8: Bad Deployment Corrupting 50,000 User Records](#exercise-8-bad-deployment-corrupting-50000-user-records)
9. [Exercise 9: Monolithic Shared Database Deadlocking Under Write Scale](#exercise-9-monolithic-shared-database-deadlocking-under-write-scale)
10. [Exercise 10: Runaway Cloud Cost Emergency ($150k Daily Burn Rate)](#exercise-10-runaway-cloud-cost-emergency-150k-daily-burn-rate)

---

### Exercise 1: Primary Database Crash During Peak Flash Sale

* **The Prompt**: *"It is 10:02 AM on Black Friday. Your primary AWS Aurora PostgreSQL instance hits 100% CPU, stops accepting writes, and the automated failover to the read replica hangs. What do you do?"*
* **Diagnostic Workflow**:
  1. Check incoming write RPS against historical baseline.
  2. Inspect connection pool saturation via AWS RDS Performance Insights.
  3. Identify lock contention: Look for blocking queries on the `inventory` or `orders` tables (`pg_stat_activity`).
* **Immediate Mitigation**:
  * Shed load at the API Gateway: Return HTTP 429 / 503 on new order creation while keeping read browsing active via edge CDN.
  * Force manual reboot / failover of the stalled primary instance.
  * Flush in-flight transaction locks.
* **Architectural Hardening**:
  * Decouple inventory reservation from order persistence. Introduce an in-memory Redis cluster for atomic stock decrements (`DECRBY`) during flash sales, asynchronously writing orders to Kafka.
  * Deploy RDS Proxy to cap connection surges.

---

### Exercise 2: Global Latency Spike Across All Services (The 1500ms Regression)

* **The Prompt**: *"A new frontend release went live 20 minutes ago. p95 latency across every backend microservice immediately jumped from 45ms to 1,500ms. No backend code was deployed. Why?"*
* **Diagnostic Workflow**:
  1. Correlate timing: Incident began exactly at the frontend deploy timestamp.
  2. Inspect network requests from the frontend client in Chrome DevTools: The frontend team replaced a paginated API call with an unbounded query requesting all 50,000 items in a user's history on page load.
  3. Backend service trace (OpenTelemetry) shows CPU serialization overhead and massive payload transfers.
* **Immediate Mitigation**: Roll back the frontend deployment immediately (canary abort).
* **Architectural Hardening**:
  * Enforce strict maximum pagination limits at the API Gateway level (`max_limit = 100`).
  * Add automated performance regression testing in the frontend CI/CD pipeline.

---

### Exercise 3: Uncontrolled Regional Cloud Outage (us-east-1 Black Hole)

* **The Prompt**: *"AWS us-east-1 suffers a total control plane and networking outage. 100% of your production traffic is failing. You have an active-passive standby in us-west-2. How do you execute disaster recovery?"*
* **Diagnostic Workflow**:
  1. Verify the scope of the outage via AWS Health Dashboard and synthetic global probes.
  2. Verify us-west-2 database replication status and replication lag.
* **Immediate Mitigation**:
  * Promote the us-west-2 read replica to primary writer.
  * Update Route 53 / Cloudflare GeoDNS failover records to route 100% of global traffic to us-west-2.
  * Scale up us-west-2 EKS worker node pools to absorb 100% global traffic.
* **Architectural Hardening**:
  * Transition from Active-Passive to **Multi-Region Active-Active** with automated latency routing, eliminating manual DNS cutovers.

---

### Exercise 4: The 10-Million Message Kafka Consumer Backlog

* **The Prompt**: *"Your primary Kafka topic is ingesting 20,000 events/sec, but the downstream consumer squad is only processing 2,000 events/sec. Consumer lag has reached 10 Million messages and is growing by 18,000 events every second. Downstream workers are pegged at 100% CPU."*
* **Diagnostic Workflow**:
  1. Check partition count: The topic only has 12 partitions.
  2. Check consumer group size: 12 consumer pods are running. Adding more consumer pods will do nothing because Kafka cannot assign more consumers than there are partitions.
* **Immediate Mitigation**:
  * Increase topic partitions from 12 to 64 partitions.
  * Scale consumer pod replicas from 12 to 64.
  * In the consumer code, enable **in-memory worker thread batching**: The consumer pulls 500 messages at once and dispatches them across a thread pool of 20 worker threads, increasing consumer throughput by 10x.
* **Architectural Hardening**: Establish autoscaling triggers on Kafka consumer lag metrics (`kafka_consumergroup_lag`).

---

### Exercise 5: Distributed Cache Cluster Collapse (The Thundering Herd)

* **The Prompt**: *"A network partition causes the primary Redis Cluster to fail. When the cluster recovers 3 minutes later, the instant it comes back online, the database crashes, which causes the application servers to crash in a continuous loop."*
* **Diagnostic Workflow**:
  1. Identify the cache stampede: All cache keys expired during the downtime or the cache memory was wiped.
  2. 100,000 incoming requests/sec hit the newly booted empty cache, miss, and hit the cold database simultaneously.
* **Immediate Mitigation**:
  * Throttle traffic at the edge (Cloudflare WAF / API Gateway) to 10% capacity.
  * Warm the cache using a pre-warming script for the top 1,000 hot SKUs.
  * Gradually open the traffic gate in 20% increments.
* **Architectural Hardening**:
  * Implement the **Single-Flight (Mutex Lock)** pattern in application code: only 1 thread fetches from the DB on a cache miss; all other concurrent requests wait for the cache to populate.
  * Introduce random TTL jitter to eliminate synchronized expiration.

---

### Exercise 6: External Payment Gateway 5-Second Hang

* **The Prompt**: *"Your third-party credit card processor (Stripe) is experiencing internal degradation: calls that usually take 200ms are taking 8 seconds before timing out. Your checkout service thread pool is 100% exhausted, and the entire website is freezing."*
* **Diagnostic Workflow**:
  1. Open distributed trace: 98% of latency is spent on outgoing HTTP calls to `api.stripe.com`.
* **Immediate Mitigation**:
  * Drop socket timeouts on the outgoing HTTP client from 30 seconds to 1,500ms.
  * Enable the Circuit Breaker: Automatically reject payment attempts with an informative UI message (*"Card processing temporarily unavailable; please try PayPal or Apple Pay"*).
* **Architectural Hardening**:
  * Implement multi-provider gateway routing: If Stripe error rate exceeds 5%, automatically route transactions to a secondary fallback gateway (Adyen / Braintree).

---

### Exercise 7: Production SSL/TLS Certificate Expiration at Midnight

* **The Prompt**: *"At 00:01 UTC, your public wildcard SSL certificate (`*.company.com`) expires. Millions of mobile app users and web browsers are blocked by security warning screens."*
* **Diagnostic Workflow**:
  1. Confirm TLS handshake failure: `curl -v https://api.company.com` outputs `SSL certificate problem: certificate has expired`.
* **Immediate Mitigation**:
  * Emergency DNS cutover to Cloudflare / AWS CloudFront with automated SSL provisioning (Universal SSL).
  * Rapidly issue and bind a new certificate via Let's Encrypt / AWS Certificate Manager (ACM).
* **Architectural Hardening**:
  * Automate all certificate renewals using **cert-manager** in Kubernetes.
  * Deploy automated Prometheus alerting 30, 14, and 7 days prior to any certificate expiration.

---

### Exercise 8: Bad Deployment Corrupting 50,000 User Records

* **The Prompt**: *"A flawed database migration script ran 2 hours ago. It accidentally set the `billing_status` of 50,000 active enterprise accounts to `DELETED`, revoking their access."*
* **Diagnostic Workflow**:
  1. Check database write audit logs or WAL records to determine the exact timestamp of the flawed migration script execution.
* **Immediate Mitigation**:
  * Abort any ongoing migration tasks and pause the billing background worker.
  * Execute **Point-In-Time Recovery (PITR)** on AWS Aurora to restore a clone of the database to 1 minute prior to the migration script run.
  * Extract only the corrupted 50,000 rows from the cloned database and run an emergency `UPDATE ... FROM` patch script on the live primary.
* **Architectural Hardening**:
  * Ban destructive DDL/DML scripts in production pipelines without staging shadow verification.
  * Implement soft-deletes (`is_deleted = true`) rather than hard row mutations.

---

### Exercise 9: Monolithic Shared Database Deadlocking Under Write Scale

* **The Prompt**: *"Two newly launched features—Real-Time Loyalty Points and Automated Order Invoicing—are locking the same rows on the monolithic PostgreSQL database in reverse order, causing 500 deadlock exceptions every minute."*
* **Diagnostic Workflow**:
  1. Query `pg_stat_activity` and `pg_locks` to identify conflicting lock acquisition order:
     * Transaction A locks `users`, then locks `orders`.
     * Transaction B locks `orders`, then locks `users`.
* **Immediate Mitigation**: Disable the loyalty points cron job to break the deadlock loop.
* **Architectural Hardening**:
  * Enforce strict lock ordering: All transactions must acquire locks in alphabetical table order.
  * Extract Loyalty Points into an independent microservice with its own dedicated datastore.

---

### Exercise 10: Runaway Cloud Cost Emergency ($150k Daily Burn Rate)

* **The Prompt**: *"An auto-scaling bug in an asynchronous worker fleet spawned 2,000 GPU-backed worker instances overnight to process a stuck retry loop, burning $150,000 in 12 hours. The CFO is in your office."*
* **Diagnostic Workflow**:
  1. Check AWS Cost Explorer and CloudWatch EC2 metrics.
  2. Discover that an SQS queue had a poison pill message with no DLQ. Every failed attempt re-triggered the worker autoscaler to provision more nodes.
* **Immediate Mitigation**:
  * Drain the malformed queue message to a cold S3 bucket.
  * Set hard `max_capacity` limits on all AWS Auto-Scaling Groups (ASGs).
* **Architectural Hardening**:
  * Implement AWS Budget Alarms that trigger automated Slack alerts and kill-switches when daily spend deviates by more than 25% from baseline.
  * Mandatory Dead-Letter Queues (DLQs) on all asynchronous queues.

---

## Cross-References

* **Production Incidents Guide**: [`production.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/scenario-based/production.md)
* **Incident Response Commander**: [`incident-response.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/scenario-based/incident-response.md)
* **Architectural Trade-Offs**: [`tradeoffs/README.md`](file:///d:/company/products/enterprise-architecture-handbook/20-interview-system-design/tradeoffs/README.md)
