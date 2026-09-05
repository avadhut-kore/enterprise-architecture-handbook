# Kubernetes Observability Architecture

## Executive Summary

Observability in Kubernetes requires monitoring four distinct layers: physical worker nodes, Kubernetes control plane components, pod lifecycle metrics, and application performance telemetry.

---

## 1. The Kubernetes Observability Stack

```mermaid
graph TD
    Node[Worker Node OS: node-exporter] --> Prom[Prometheus Server / Managed Prometheus]
    Kubelet[Kubelet cAdvisor: Container CPU/Memory] --> Prom
    KubeState[kube-state-metrics: Deployment/Pod States] --> Prom
    App[Application Pods: OpenTelemetry SDK] --> OTel[OpenTelemetry Collector DaemonSet]

    OTel --> Tempo[Distributed Traces: Grafana Tempo]
    OTel --> Loki[Structured Logs: Grafana Loki / CloudWatch]
    Prom --> Grafana[Centralized Grafana SRE Dashboards]
```

---

## 2. Pod Disruption Budgets (PDB) & SLO Monitoring

- **Pod Disruption Budgets (PDB)**: Enforce PDBs (`minAvailable: 2` or `maxUnavailable: 20%`) on all critical deployments. This guarantees that voluntary disruptions (node draining during upgrades, autoscaling scale-down) never breach application availability SLAs.
