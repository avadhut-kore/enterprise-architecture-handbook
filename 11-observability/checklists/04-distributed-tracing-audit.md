# Checklist 04: Distributed Tracing & Context Propagation Audit

## 1. Overview
Verifies end-to-end trace context propagation, OpenTelemetry SDK instrumentation quality, and trace sampling efficiency across distributed microservice topologies.

---

## 2. Verification Rubric

| Check Item | Target Standard | Verification Method | Pass/Fail |
| :--- | :--- | :--- | :--- |
| **Context Injection** | W3C `traceparent` injected into all outbound HTTP/gRPC client requests. | Packet capture / mock receiver inspection. | [ ] |
| **Context Extraction**| Inbound requests extract `traceparent` and establish active parent span context. | Verify continuous trace DAG in Tempo/Jaeger. | [ ] |
| **Async Messaging** | W3C trace context serialized into Kafka / MQ record headers. | Inspect Kafka record byte headers. | [ ] |
| **Span Naming** | Span names adhere to low-cardinality templates (e.g., `HTTP GET /orders/:id`). | Audit Tempo span names; zero UUIDs in names. | [ ] |
| **Error Flagging** | Failed RPC calls set `otel.status_code = ERROR` and record exception stack trace. | Trigger 500 error; verify span turns red. | [ ] |
| **Database Spans** | Database spans include `db.system`, `db.name`, and sanitized `db.statement`. | Verify SQL statements are parameterized (no PII).| [ ] |
| **Tail Sampling** | Collector tail sampling captures 100% of errors and latency outliers. | Validate error traces are never dropped. | [ ] |
