# GCP Observability Architecture: Cloud Operations Suite

## Executive Summary

Google Cloud Operations Suite (formerly Stackdriver) provides integrated monitoring, logging, and application performance tracing.

---

## 1. Telemetry Pipeline Architecture

```mermaid
graph TD
    App[GKE / Cloud Run Applications] -->|Structured JSON to stdout/stderr| CloudLogging[Cloud Logging: FluentBit / Log Routers]
    App -->|OpenTelemetry OTLP| CloudTrace[Cloud Trace: Distributed Tracing]
    App -->|Prometheus Metric Exporter| ManagedProm[Managed Service for Prometheus (GMP)]

    CloudLogging --> LogSink[Log Sink: Export to BigQuery for Compliance Audit]
    ManagedProm --> CloudMonitoring[Cloud Monitoring Dashboards & Alerts]
    CloudMonitoring --> PagerDuty[SRE Incident Management]
```

---

## 2. Production SRE Standards

1. **Google Cloud Managed Service for Prometheus (GMP)**:
   - Deploy GMP on GKE clusters to eliminate self-hosting Thanos or Cortex clusters. Collect and store Prometheus metrics at planetary scale with automated cross-cluster query support.
2. **Log Routing & Exclusion Filters**:
   - Ingesting every debug log in high-throughput production environments generates massive logging charges. Implement **Log Exclusion Filters** at the root sink to drop verbose HTTP health check logs (`GET /healthz`) before ingestion, saving up to 60% on logging bills.
