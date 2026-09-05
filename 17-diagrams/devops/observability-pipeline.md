# Enterprise Observability Pipeline (OpenTelemetry, Prometheus & Tempo)

Unified observability telemetry architecture capturing the 3 Pillars (Metrics, Logs, Traces) via OpenTelemetry Collector and routing to specialized backend stores.

## Mermaid Architecture Diagram

```mermaid
graph TD
    subgraph InstrumentationTier ["Application & Infrastructure Workloads"]
        AppPod["Microservice Pod (OTel Auto-Instrumentation SDK)"]
        NodeExporter["Kubernetes Node Exporter (Host Metrics)"]
        Fluentbit["Fluent Bit DaemonSet (Container Logs)"]
    end

    subgraph OTelCollectorTier ["OpenTelemetry Collector Pipeline (DaemonSet + Gateway)"]
        OTelAgent["OTel Collector Agent (Local Pod)"]
        OTelGW["OTel Collector Central Gateway Cluster<br/>- Batch Processor<br/>- PII Scrubber & Redactor<br/>- Tail-Based Trace Sampler"]
        
        AppPod -->|"gRPC / OTLP (Protobuf)"| OTelAgent
        NodeExporter --> OTelAgent
        Fluentbit --> OTelAgent
        OTelAgent --> OTelGW
    end

    subgraph SpecializedBackends ["Specialized Storage Backends"]
        Mimir[("Grafana Mimir / Prometheus<br/>(Metrics Time-Series Store)")]
        Loki[("Grafana Loki / Elasticsearch<br/>(Structured Log Store)")]
        Tempo[("Grafana Tempo / Jaeger<br/>(Distributed Trace Store)")]

        OTelGW -->|"Prometheus Remote Write"| Mimir
        OTelGW -->|"Loki HTTP Push"| Loki
        OTelGW -->|"OTLP Traces"| Tempo
    end

    subgraph VisualizationLayer ["Unified Observability Dashboard"]
        Grafana["Grafana Unified Dashboard<br/>(Correlated Trace -> Log -> Metric Drill-down)"]
        Mimir --> Grafana
        Loki --> Grafana
        Tempo --> Grafana
    end
```

## PlantUML Specification

```plantuml
@startuml
package "Workload Pods" {
  [App Container (OTel SDK)]
}
package "Telemetry Pipeline" {
  component "OpenTelemetry Collector" as otel
  otel -> otel : Scrub PII & Batch
}
package "Storage Backends" {
  database "Prometheus (Metrics)" as prom
  database "Loki (Logs)" as loki
  database "Tempo (Traces)" as tempo
}
component "Grafana Dashboard" as grafana

[App Container (OTel SDK)] --> otel : OTLP over gRPC
otel --> prom : Metrics
otel --> loki : Logs
otel --> tempo : Traces
prom --> grafana
loki --> grafana
tempo --> grafana
@enduml
```

## Architectural Design Considerations

* **Standardized Protocol**: Use OpenTelemetry Protocol (OTLP) exclusively across all services to prevent vendor lock-in to proprietary monitoring agents.
* **Correlation ID / Trace Context**: Propagate W3C Trace Context headers (`traceparent`, `tracestate`) across all HTTP, gRPC, and messaging boundaries.
* **Tail-Based Sampling**: Retain 100% of error traces and slow traces (>2s) while aggressively sampling down high-volume 200 OK happy-path traces to control storage costs.

## Related Documentation & Patterns

* [Canary Deployment](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/devops/canary.md)
* [DevOps Checklist](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/devops/checklists.md)
* [Security: Security Monitoring](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/security-monitoring.md)
