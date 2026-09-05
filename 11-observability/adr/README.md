# Observability Architecture Decision Records (ADRs)

## Executive Summary

This directory documents the foundational architectural decisions governing enterprise telemetry collection, processing, storage, alerting, and incident governance.

Every ADR follows the canonical enterprise template established in [`../../16-architecture-deliverables/01-adr/template.md`](../../16-architecture-deliverables/01-adr/template.md), ensuring clear traceability between business drivers, technical trade-offs, positive impacts, and accepted liabilities.

---

## ADR Registry

| ADR ID | Decision Title | Status | Primary Decision Driver |
| :--- | :--- | :--- | :--- |
| **[`ADR-0001`](ADR-0001-opentelemetry-as-universal-telemetry-standard.md)** | Standardizing on OpenTelemetry as the Universal Telemetry Standard | **Accepted** | Eradicate proprietary vendor lock-in; establish polyglot instrumentation parity. |
| **[`ADR-0002`](ADR-0002-node-daemonset-vs-sidecar-collector-topology.md)** | OpenTelemetry Collector Deployment: Node DaemonSet vs Sidecar | **Accepted** | Optimize memory footprint; reduce cluster resource consumption by 85%. |
| **[`ADR-0003`](ADR-0003-promql-multi-burn-rate-alerting-over-thresholds.md)** | Adopting Multi-Window Multi-Burn-Rate Alerting over Static Thresholds | **Accepted** | Eliminate alert fatigue; align alerting directly with customer SLO impact. |
| **[`ADR-0004`](ADR-0004-tail-sampling-over-head-sampling-for-traces.md)** | Standardizing on OpenTelemetry Tail Sampling for Distributed Tracing | **Accepted** | Capture 100% of errors and latency outliers while reducing trace storage by 90%. |
| **[`ADR-0005`](ADR-0005-tiered-storage-and-downsampling-for-metrics.md)** | Multi-Tiered Storage & Automated Downsampling for Time-Series Data | **Accepted** | Mitigate exponential cloud storage growth; enable multi-year analytical querying. |
| **[`ADR-0006`](ADR-0006-structured-json-logging-with-ecs-schema.md)** | Enforcing Structured JSON Logging with Elastic Common Schema (ECS) | **Accepted** | Eliminate expensive regex log parsing; ensure uniform log indexing across fleet. |
| **[`ADR-0007`](ADR-0007-ebpf-continuous-profiling-for-production.md)** | Continuous Production Profiling via Zero-Overhead eBPF | **Accepted** | Identify hidden CPU/memory micro-bottlenecks without runtime code modification. |
| **[`ADR-0008`](ADR-0008-error-budget-policy-and-release-gating.md)** | Implementing Automated Error Budget Policies in CI/CD Delivery Gates | **Accepted** | Provide objective mathematical arbitration between feature velocity and platform stability. |
| **[`ADR-0009`](ADR-0009-pre-ingestion-pii-masking-in-otel-collectors.md)** | Pre-Ingestion PII & Sensitive Data Redaction in Collector Memory | **Accepted** | Guarantee zero GDPR/PCI-DSS/HIPAA violations prior to network transmission. |
| **[`ADR-0010`](ADR-0010-synthetic-canary-journeys-for-critical-paths.md)** | Multi-Region Headless Synthetic Probing for Critical Revenue Paths | **Accepted** | Catch off-peak and regional routing outages before end-users are impacted. |
