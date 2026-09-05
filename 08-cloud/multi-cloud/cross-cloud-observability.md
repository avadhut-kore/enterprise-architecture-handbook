# Cross-Cloud Observability Architecture

## Executive Summary

Operating a multi-cloud environment without centralized telemetry creates operational blind spots. When an incident occurs, SREs cannot correlate traces and metrics across fragmented, cloud-proprietary monitoring silos (CloudWatch vs Azure Monitor vs Google Cloud Operations).

---

## 1. Unified Telemetry Architecture

```mermaid
graph TD
    subgraph Workloads
        AWSApp[AWS Microservices] -->|OTel Traces/Metrics| OTel1[OpenTelemetry Collector Agent]
        AzureApp[Azure Microservices] -->|OTel Traces/Metrics| OTel2[OpenTelemetry Collector Agent]
        GCPApp[GCP Microservices] -->|OTel Traces/Metrics| OTel3[OpenTelemetry Collector Agent]
    end

    subgraph Central Observability Platform [Neutral SaaS or Dedicated Cluster]
        Collector[Central Telemetry Gateway]
        Mimir[(Grafana Mimir / Prometheus: Metrics)]
        Loki[(Grafana Loki: Structured Logs)]
        Tempo[(Grafana Tempo: Distributed Traces)]
        Dashboards[Unified Grafana Dashboards & PagerDuty Alerting]
    end

    OTel1 ==> Collector
    OTel2 ==> Collector
    OTel3 ==> Collector
    Collector --> Mimir
    Collector --> Loki
    Collector --> Tempo
    Mimir --> Dashboards
    Loki --> Dashboards
    Tempo --> Dashboards
```

---

## 2. Architectural Requirements

1. **Standardized Correlation IDs**:
   - Enforce W3C Trace Context headers (`traceparent`, `tracestate`) across all HTTP, gRPC, and messaging payloads. When a transaction traverses from AWS to Azure, the trace must remain continuous.
2. **Cardinality Management**:
   - In multi-cloud environments, resource labels must include `cloud.provider`, `cloud.region`, `cloud.account.id`, and `service.name`. Enforce strict metric relabeling rules at the collector level to prevent exploding time-series cardinality.
