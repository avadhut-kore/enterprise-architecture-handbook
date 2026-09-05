# Distributed Tracing Architecture & Deployment Checklist

## 1. Executive Summary
This 25-point checklist provides engineering squads and Architecture Review Boards (ARBs) with an objective verification rubric for distributed tracing instrumentation, context propagation, and tail sampling.

---

## 2. The 25-Point Checklist

### Section 1: Context Propagation & Standards
- [ ] **01.** Application propagates W3C TraceContext (`traceparent`, `tracestate`) on all outbound HTTP and gRPC network calls.
- [ ] **02.** Asynchronous message brokers (Kafka, RabbitMQ, SQS) propagate trace headers in message metadata headers.
- [ ] **03.** Composite propagators are configured to support legacy B3 or Jaeger headers during migration phases.
- [ ] **04.** Async thread pools, coroutines, and task workers explicitly carry context using context wrappers.
- [ ] **05.** Edge API Gateways generate a valid 128-bit W3C Trace ID for requests entering without an existing trace header.
- [ ] **06.** Internal proxies and load balancers pass through `traceparent` headers without stripping or mutating them.

### Section 2: Instrumentation Quality
- [ ] **07.** Spans are created only at meaningful architectural boundaries (HTTP, RPC, DB, Cache, Messaging).
- [ ] **08.** Function-level utility loops are excluded from tracing; profiling tools are used for CPU flamegraphs.
- [ ] **09.** Exceptions set the span status to `StatusCode.ERROR` and record the exception object via `span.recordException()`.
- [ ] **10.** All spans are closed deterministically in `finally` or `using` blocks to prevent span memory leaks.
- [ ] **11.** Database spans record sanitized SQL templates with parameter literals stripped.
- [ ] **12.** Span attributes strictly adhere to OpenTelemetry semantic conventions (v1.26+).

### Section 3: Asynchronous & Event-Driven Tracing
- [ ] **13.** Asynchronous fire-and-forget messaging utilizes **Span Links** rather than synchronous parent-child relationships.
- [ ] **14.** Batch message consumers create a local processing root span linked to each message's individual trace context.
- [ ] **15.** Dead Letter Queues (DLQ) preserve original trace headers in metadata when poisoning messages are quarantined.

### Section 4: Sampling & Storage Economics
- [ ] **16.** Clustered collector gateways utilize consistent trace-ID hashing to ensure related spans land on the same node.
- [ ] **17.** Tail sampling is configured to capture 100% of spans containing HTTP 5xx or gRPC errors.
- [ ] **18.** Tail sampling captures 100% of spans exceeding latency SLO thresholds (e.g., $> 1,500\text{ms}$).
- [ ] **19.** Nominal, successful 200 OK traffic is sampled down to 1% to 5% to control storage costs.
- [ ] **20.** Collector gateway memory limits are sized according to the formula: $(R_{\text{spans}} \times S_{\text{avg}} \times T_{\text{wait}}) \times 1.5$.
- [ ] **21.** Full trace retention is capped at 7 to 14 days, with aggregated latency trends stored in metrics for 30+ days.

### Section 5: Verification & Governance
- [ ] **22.** Trace-based testing is incorporated into CI/CD pipelines to assert dependency constraints and N+1 query limits.
- [ ] **23.** Automated regex redaction in the collector gateway scrubs accidental PII and credit card numbers from spans.
- [ ] **24.** Dynamic service dependency maps are generated automatically from active distributed trace graphs.
- [ ] **25.** Critical path analysis is verified on tier-1 user journeys during Production Readiness Reviews (PRRs).
