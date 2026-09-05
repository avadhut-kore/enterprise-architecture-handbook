# ADR-0058: Standardization on OpenTelemetry (OTel) for Distributed Observability

## Metadata
```yaml
id: ADR-0058
title: Standardization on OpenTelemetry (OTel) for Distributed Observability
status: accepted
decision_type: architectural
scope: enterprise-cloud-infrastructure
owners: enterprise-architecture-board
date: 2026-09-05
review_cadence: annual
```

---

## 1. Context & Problem Statement
Proprietary monitoring agents (Datadog, New Relic) created deep vendor lock-in and made migrating telemetry backends economically prohibitive.

---

## 2. Decision
We standardize on OpenTelemetry (OTel) SDKs and the OTel Collector daemon for all distributed tracing, metrics, and structured logs across the enterprise.

---

## 3. Positive Consequences
- Zero vendor lock-in: telemetry backends can be swapped by updating collector exporter YAML.
- End-to-end distributed trace propagation using W3C standards.
- Single in-process agent reduces memory and CPU overhead.

---

## 4. Negative Consequences & Trade-offs
- OpenTelemetry Collector fleet must be maintained and scaled.
- Tail sampling requires careful memory sizing on collector nodes.

---

## 5. Alternatives Considered & Rejected
- **Proprietary Vendor SDKs**: Rejected due to high commercial switching costs.
- **Fragmented Open Source (Prometheus + Jaeger + Fluentd independently)**: Rejected due to agent sprawl.
