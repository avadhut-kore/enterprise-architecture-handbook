# Observability FinOps Anti-Patterns Catalog

## 1. Executive Summary
This document catalogs 12 widespread enterprise anti-patterns in telemetry cost management, capacity provisioning, and data lifecycle governance.

---

## 2. The 12 Observability Cost Anti-Patterns

### 1. Storing Production Logs at DEBUG Level
* **Problem**: Leaving `LOG_LEVEL=DEBUG` active in production microservices indefinitely.
* **Why It Happens**: Developers forgot to revert debug flags after investigating a production incident.
* **Impact**: Increases log volume by $500\%$; saturates network buffers; inflates monthly cloud bills by tens of thousands of dollars.
* **Remediation**: Enforce `INFO` as the default production level; use dynamic runtime log-level toggling via feature flags or admin APIs with automated 30-minute timeouts.

### 2. The Unbounded UUID Metric Label (Cardinality Suicide)
* **Problem**: Adding dynamic attributes like `user_id` or `order_id` into Prometheus metric labels.
* **Why It Happens**: Developers treating metric labels like relational database foreign keys.
* **Impact**: Millions of active time series generated; crashes Prometheus servers; triggers emergency SaaS bill spikes.
* **Remediation**: Hard relabeling drop rules in collector configs; CI/CD linting of metric definitions.

### 3. Infinite Un-Tiered Log Retention
* **Problem**: Retaining 100% of raw unstructured logs in high-performance NVMe SSD Elasticsearch clusters for 180+ days.
* **Why It Happens**: Lack of data retention policies.
* **Impact**: Storage costs grow monotonically; cluster memory pressure degrades query response times for recent incidents.
* **Remediation**: Tier storage: 7 days Hot SSD, 30 days Warm, 365 days Cold object storage (S3/Glacier).

### 4. Head Sampling High-Value Traces
* **Problem**: Applying naive 5% head sampling at the edge gateway.
* **Why It Happens**: Inability to configure tail-sampling collector infrastructure.
* **Impact**: 95% of customer-impacting 500 Internal Server Errors are permanently dropped before reaching the tracing backend.
* **Remediation**: Deploy OpenTelemetry Collector **Tail Sampling** (capture 100% of errors and latency outliers).

### 5. Indexing Entire Payloads by Default
* **Problem**: Storing complete raw HTTP request/response JSON bodies into searchable log indexes.
* **Why It Happens**: Default index templates with dynamic mapping enabled.
* **Impact**: Multiplies index size; exposes sensitive customer PII; bloats storage.
* **Remediation**: Explicit field mapping; prune verbose payload blobs before indexing.

### 6. Ingesting Kubernetes Health Checks at Full Fidelity
* **Problem**: Emitting and indexing HTTP 200 logs and trace spans every 2 seconds for `/healthz` and `/ready` probes.
* **Why It Happens**: Default framework logging filters.
* **Impact**: In Kubernetes clusters with thousands of pods, kubelet health checks account for up to $40\%$ of all incoming log volume!
* **Remediation**: Configure web servers (Nginx, Envoy, Spring Boot) to silently discard or ignore `/healthz` access logs.

### 7. Cross-AZ Telemetry Egress Costs
* **Problem**: Pods in Availability Zone `us-east-1a` streaming uncompressed logs to a centralized collector running in `us-east-1b`.
* **Why It Happens**: Lack of zone-aware daemonset topology.
* **Impact**: Massive inter-AZ network egress data transfer surcharges on AWS/GCP bills.
* **Remediation**: Deploy OpenTelemetry Collector as a **Node DaemonSet** to process and compress telemetry locally within each AZ before transmission.

### 8. Logging Exceptions Inside Tight Loops
* **Problem**: Catching a database connection exception inside a 100,000-item loop and logging the complete 50-line stack trace on every iteration.
* **Why It Happens**: Missing rate limiting on logger handlers.
* **Impact**: Emits 5,000,000 log lines in 10 seconds; causes local pod disk exhaustion and pod evictions.
* **Remediation**: Implement token-bucket rate limiting on application error loggers.

### 9. Lack of Cost Attribution per Engineering Squad
* **Problem**: Central IT pays a single monolithic $100,000/month Datadog/Splunk invoice without attributing spend to specific product squads.
* **Why It Happens**: Centralized monitoring budget with no FinOps tagging.
* **Impact**: "Tragedy of the Commons": individual squads have zero financial incentive to optimize telemetry.
* **Remediation**: Tag all telemetry with `owner_team`; implement automated internal showback / chargeback reporting.

### 10. Measuring Telemetry by Raw Volume Instead of ROI
* **Problem**: Assuming that higher telemetry ingestion automatically equals superior system observability.
* **Why It Happens**: Confusing data collection with actionable insight.
* **Impact**: Massive financial spend with zero reduction in Mean Time to Resolution (MTTR).
* **Remediation**: Track the **Telemetry Utility Ratio**: how many ingested log types or trace spans were actually queried during incident investigations.

### 11. Over-Scraping Nominal Infrastructure Metrics
* **Problem**: Scraping static Kubernetes pod disk and CPU metrics every 1 second across 50,000 pods.
* **Why It Happens**: Misunderstanding resolution requirements.
* **Impact**: Wastes massive time-series storage for metrics that only change gradually.
* **Remediation**: Scrape infrastructure at 30-second or 60-second intervals; reserve 5-10 second scrapes strictly for latency-sensitive application SLIs.

### 12. Storing Sensitive Data in Log Strings (The Compliance Remediation Nightmare)
* **Problem**: Logging plaintext passwords, authorization tokens, or credit cards.
* **Why It Happens**: Missing pre-ingestion redaction.
* **Impact**: Violates PCI-DSS/GDPR; requires emergency re-indexing and deletion of multi-terabyte log stores.
* **Remediation**: Pre-ingestion redaction regex pipelines at the edge collector.
