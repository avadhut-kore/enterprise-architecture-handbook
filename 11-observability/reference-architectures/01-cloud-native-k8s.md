# Reference Architecture 01: Cloud-Native Kubernetes Observability

## 1. System Context & Overview
Designed for high-scale Kubernetes deployments running hundreds of microservices across multiple geographical regions. It utilizes the **OpenTelemetry (OTel) Collector DaemonSet pattern** paired with an open-source scalable storage tier (Prometheus/Thanos, Grafana Loki, Grafana Tempo, and Grafana).

See visual modeling in [`../../17-diagrams/deployment/kubernetes.md`](../../17-diagrams/deployment/kubernetes.md).

---

## 2. Architecture Diagram

```mermaid
flowchart TD
    subgraph K8s_Worker_Node ["Kubernetes Worker Node (Node DaemonSet Pattern)"]
        subgraph Pods ["Application Pods (Namespace: Production)"]
            App1["Service A (Spring Boot + OTel Agent)"]
            App2["Service B (Go Gin + OTel SDK)"]
        end
        
        Kubelet["Kubelet (cAdvisor Metrics)"]
        
        subgraph DaemonSet ["OTel Collector DaemonSet (HostNetwork: false)"]
            OTel_DS["OTel Collector Agent\n- Ingests OTLP gRPC (:4317)\n- Enriches K8s attributes (pod, ns, node)\n- Performs regex PII masking\n- Batches & compresses output"]
        end
        
        App1 -->|OTLP / localhost:4317| OTel_DS
        App2 -->|OTLP / localhost:4317| OTel_DS
        Kubelet -. Prometheus Scrape .-> OTel_DS
    end

    subgraph Central_Telemetry_Cluster ["Central Monitoring & Storage Tier (Thanos / Loki / Tempo)"]
        Thanos["Thanos / Cortex (Prometheus Metrics TSDB)"]
        Loki["Grafana Loki (Log Aggregation)"]
        Tempo["Grafana Tempo (Distributed Tracing Object Storage)"]
        Pyroscope["Pyroscope (eBPF Continuous Profiler)"]
    end

    OTel_DS -->|Metrics Remote Write| Thanos
    OTel_DS -->|OTLP HTTP Logs| Loki
    OTel_DS -->|OTLP gRPC Traces| Tempo

    subgraph Visualization ["Unified SRE Operations Console"]
        Grafana["Grafana Enterprise Dashboard & Incident Console"]
        Grafana --> Thanos
        Grafana --> Loki
        Grafana --> Tempo
        Grafana --> Pyroscope
    end
```

---

## 3. Key Architectural Decisions
1. **Node DaemonSet vs Sidecar**: Deploying the OTel Collector as a Kubernetes **DaemonSet (1 per node)** reduces memory consumption by 85% compared to injecting sidecar containers into thousands of application pods.
2. **K8s Metadata Enrichment**: The DaemonSet collector queries the local kubelet API to automatically tag all telemetry with `k8s.pod.name`, `k8s.namespace.name`, `k8s.deployment.name`, and `k8s.node.name`.
3. **Storage Efficiency**: Metrics are federated to Thanos for long-term multi-year object storage (S3) with automated downsampling.
