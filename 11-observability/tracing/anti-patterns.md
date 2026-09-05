# Distributed Tracing Anti-Patterns Catalog

## 1. Executive Summary
This document catalogs 12 widespread enterprise anti-patterns in distributed tracing instrumentation, context propagation, and backend sampling.

---

## 2. The 12 Tracing Anti-Patterns

### 1. The Context Evaporation Bug (Async Task Thread Loss)
* **Problem**: Spawning an asynchronous thread or coroutine without copying the OpenTelemetry context.
* **Impact**: Child work executes with an empty context, creating an orphan trace with a new `trace_id`. The distributed trace is fractured in half.
* **Remediation**: Wrap thread pools and executors with `Context.taskWrapping()` or runtime-native context carriers.

### 2. Tracing Every Internal Loop and Function (Span Explosion)
* **Problem**: Adding spans to internal utility functions, getters, setters, or inside loops iterating over 5,000 items.
* **Impact**: A single transaction generates 100,000 spans; collector memory exhausts; browser freezes when attempting to render the trace waterfall.
* **Remediation**: Spans belong only at **architectural and network boundaries** (HTTP, RPC, DB, Cache, Messaging). Use continuous CPU profilers (Flamegraphs) for function-level analysis.

### 3. Missing Span Error Status on Exceptions
* **Problem**: Catching an exception, logging it, and ending the span without calling `span.setStatus(StatusCode.ERROR)`.
* **Impact**: The backend tracing UI displays the span as green/successful (`OK`), blinding SREs to error traces during automated search queries.
* **Remediation**: In exception catch blocks, always execute: `span.setStatus(StatusCode.ERROR, ex.getMessage()); span.recordException(ex);`.

### 4. Over-Relying on Head Sampling at 1%
* **Problem**: Using 1% probabilistic head sampling on high-throughput microservices.
* **Impact**: 99% of rare production bugs and transient edge cases are discarded at the edge before their spans are even recorded.
* **Remediation**: Deploy **Tail Sampling** at the collector gateway tier to retain 100% of error and high-latency traces.

### 5. Using Parent-Child Spans for Asynchronous Batch Messaging
* **Problem**: Setting a Kafka consumer batch span as a child of the original message producer.
* **Impact**: The producer trace appears active for hours until the consumer processes the batch.
* **Remediation**: Use **Span Links** to reference decoupled producer contexts.

### 6. Leaking PII into Span Attributes
* **Problem**: Setting `span.setAttribute("user.password", password)` or including credit card numbers in URL path attributes.
* **Impact**: Compliance breach (GDPR, PCI-DSS) permanently recorded in immutable trace indices.
* **Remediation**: Implement automated regex redaction on the OpenTelemetry Collector Gateway.

### 7. Unsanitized SQL Queries in DB Spans
* **Problem**: Emitting raw SQL strings with customer literal parameters (`SELECT * FROM users WHERE ssn = '123-45-6789'`).
* **Impact**: Telemetry leak and high cardinality in trace search indexes.
* **Remediation**: Use parameterized query templates (`SELECT * FROM users WHERE ssn = ?`).

### 8. The Infinite Span (Forgetting to Call `span.end()`)
* **Problem**: Starting a span without a `finally` block; when an unexpected exception is thrown, `span.end()` is never invoked.
* **Impact**: Spans leak in process memory and are never serialized or exported to the collector.
* **Remediation**: Always use `try-with-resources` (Java) or `using` (C#) blocks ensuring deterministic closure.

### 9. Broken Propagator Across Network Boundaries
* **Problem**: An internal API gateway strips unknown HTTP headers, dropping `traceparent` and `tracestate`.
* **Impact**: 100% context loss across corporate VPC or API gateway boundaries.
* **Remediation**: Configure all edge proxies and load balancers to pass through W3C TraceContext headers transparently.

### 10. Massive Span Payloads (Using Spans as Data Stores)
* **Problem**: Attaching a 2MB JSON document as a span attribute.
* **Impact**: Enormous network egress overhead; collector memory saturation; backend database rejections.
* **Remediation**: Restrict span attributes to metadata strings $< 512$ bytes.

### 11. Trace ID Duplication
* **Problem**: Reusing the same `trace_id` for periodic cron jobs or message polling loops.
* **Impact**: A single trace accumulates millions of spans across days, becoming un-renderable.
* **Remediation**: Every distinct operational invocation must generate a fresh, unique 128-bit W3C Trace ID.

### 12. Monolithic Trace Repositories Without Index Lifecycle
* **Problem**: Storing high-volume trace spans in Elasticsearch with no rollover policy.
* **Impact**: Storage disks fill up; search queries take minutes to execute; astronomical storage bills.
* **Remediation**: Enforce a 7-day retention limit on full trace spans, with downsampled trace metrics retained for 30 days.
