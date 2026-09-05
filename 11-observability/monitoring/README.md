# Enterprise Monitoring Architecture

> **Architectural Note**: In modern enterprise observability architecture, generic "monitoring" is decomposed into specialized, dedicated disciplines. Please refer to the corresponding subdirectories:
>
> * **[Metrics Architecture (`../metrics/`)](../metrics/README.md)**: Metric types, PromQL, TSDB architectures, OpenTelemetry metric data models, and cardinality control.
> * **[Alerting & Incident Management (`../alerting/`)](../alerting/README.md)**: Alert design, Google SRE multi-burn-rate alerting, Alertmanager architectures, on-call paging, and runbook integration.
> * **[Dashboards & Visualization (`../dashboards/`)](../dashboards/README.md)**: Visual hierarchy, Grafana dashboard standards, cognitive ergonomics, and SLI overview panels.
> * **[SLO & Error Budget Management (`../slo-management/`)](../slo-management/README.md)**: User journeys, SLI formulation, Error Budget policies, and CI/CD release gating.
> * **[Synthetic & Canary Probing (`../testing-observability/synthetic-monitoring.md`)](../testing-observability/synthetic-monitoring.md)**: Multi-region active headless synthetic probing for critical paths.
