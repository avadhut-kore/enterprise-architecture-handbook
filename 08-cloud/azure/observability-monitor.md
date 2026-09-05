# Azure Observability Architecture: Azure Monitor & Application Insights

## Executive Summary

Azure Monitor is the comprehensive observability platform for collecting, analyzing, and acting on telemetry from cloud and on-premises environments.

---

## 1. Unified Telemetry Architecture

```mermaid
graph TD
    Apps[App Services / AKS / VMs] -->|App Insights SDK / OTel| LogAnalytics[Log Analytics Workspace]
    AzureInfra[Activity Logs / Diagnostic Settings] --> LogAnalytics
    LogAnalytics --> KQL[Kusto Query Language (KQL) Engine]
    KQL --> Dashboards[Azure Workbooks & Grafana]
    KQL --> Alerts[Metric & Log Search Alerts]
    Alerts --> ActionGroups[Action Groups: PagerDuty / Webhooks]
```

---

## 2. Kusto Query Language (KQL) for Production SRE

Enterprise SREs query telemetry using KQL. Example: Detecting 5xx error spikes with distributed trace correlation:

```kql
requests
| where timestamp > ago(1h)
| where success == false
| summarize FailCount = count(), SampleTrace = any(operation_Id) by resultCode, bin(timestamp, 5m)
| render timechart
```

### Critical Logging Standards
- **Dedicated Log Analytics Workspaces**: Deploy one central workspace per region per environment to manage data retention policies (e.g., 365-day retention for production compliance, 30 days for dev).
- **Commitment Tiers**: For ingestion volumes exceeding $100\text{ GB/day}$, switch from Pay-As-You-Go to Log Analytics Commitment Tiers to reduce data ingestion costs by up to 30%.
