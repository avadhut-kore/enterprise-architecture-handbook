# Distributed Design Principle: Observability-First

## 1. Core Principle Definition

Observability-First dictates that telemetry generation—metrics, structured logs, and distributed traces—is not an afterthought added post-deployment, but a **first-class architectural requirement** embedded into the core design of every distributed service.

A system is observable if its internal state can be inferred solely by examining its external outputs.

---

## 2. The Three Pillars of Observability

```
+--------------------------+----------------------------+----------------------------+
| Pillar                   | Purpose                    | Primary Tooling Standard   |
+--------------------------+----------------------------+----------------------------+
| Distributed Traces       | End-to-end request flow    | OpenTelemetry, Jaeger, W3C |
| Metrics                  | Quantitative aggregations  | Prometheus, OpenTelemetry  |
| Structured Logs          | Discrete contextual events | JSON Logs, Fluentbit, Loki |
+--------------------------+----------------------------+----------------------------+
```

---

## 3. Distributed Context Propagation

To trace requests across 30 microservices:
- Pass standard W3C `traceparent` headers (`00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01`) across all HTTP, gRPC, and Kafka boundaries.
- Inject the `trace_id` into every structured log entry, enabling instant correlation from high-level latency alerts to exact line-of-code log statements.
