# OpenTelemetry Architecture & Deployment Checklist

## 1. Executive Summary
This 25-point checklist provides engineering squads and Architecture Review Boards (ARBs) with an objective verification rubric for OpenTelemetry instrumentation and collector mesh deployments.

---

## 2. The 25-Point Checklist

### Section 1: SDK & Application Instrumentation
- [ ] **01.** Application imports only the OpenTelemetry API in internal domain/shared libraries; the SDK is isolated to startup bootstrap.
- [ ] **02.** Standard Resource attributes (`service.name`, `service.version`, `deployment.environment`) are attached to all telemetry.
- [ ] **03.** `BatchSpanProcessor` is configured with bounded queue capacity (default 2048) and 5-second max export batch delay.
- [ ] **04.** W3C TraceContext (`traceparent`) is propagated on 100% of outbound HTTP and gRPC network calls.
- [ ] **05.** Asynchronous messaging producers inject `traceparent` into Kafka/RabbitMQ message headers.
- [ ] **06.** Context propagation is verified across asynchronous thread pools, coroutines, or event-loop callbacks.
- [ ] **07.** Dynamic REST paths are normalized (`/users/{id}`) to eliminate high-cardinality metric label explosions.
- [ ] **08.** Trace instrumentation creates spans only at meaningful architectural boundaries; internal utility loops are excluded.
- [ ] **09.** Downstream database calls record sanitized SQL queries with parameters stripped.
- [ ] **10.** Sensitive data (passwords, auth tokens, PANs, SSNs) is excluded from span attributes at source.

### Section 2: Collector Mesh Architecture
- [ ] **11.** Deployment follows the two-tier mesh model: Node Agent (DaemonSet) + Regional Gateway Fleet.
- [ ] **12.** Applications export telemetry exclusively to localhost (`localhost:4317` gRPC or `localhost:4318` HTTP).
- [ ] **13.** OTLP protocol with gzip/zstd compression is enforced across all internal collector-to-collector connections.
- [ ] **14.** The `memory_limiter` processor is configured as the **first processor** in every collector pipeline.
- [ ] **15.** Memory limiter thresholds are set conservatively (e.g., limit 80%, spike limit 20%).
- [ ] **16.** Collector gateway fleet is configured with Horizontal Pod Autoscaling (HPA) based on CPU and memory.
- [ ] **17.** Tail sampling is configured on the gateway fleet (100% errors, 100% slow requests, 1-5% nominal).
- [ ] **18.** Node agents use trace-ID consistent hashing to route related spans to the same gateway replica.
- [ ] **19.** Collector logs and internal operational metrics (`otelcol_processor_dropped_spans`) are monitored.
- [ ] **20.** Collector gateway pods run as unprivileged users with read-only root filesystems.

### Section 3: Governance & Operational Readiness
- [ ] **21.** OpenTelemetry semantic conventions (v1.26+) are enforced across all service repositories.
- [ ] **22.** High-cardinality values (UUIDs, user IDs) are strictly prohibited in metric labels.
- [ ] **23.** Automated regex redaction is enabled on the collector gateway to scrub residual PII and credentials.
- [ ] **24.** Telemetry failover behavior is verified: collector failure drops telemetry gracefully without blocking application threads.
- [ ] **25.** CI/CD pipelines include telemetry integration tests verifying span creation and context propagation before production release.
