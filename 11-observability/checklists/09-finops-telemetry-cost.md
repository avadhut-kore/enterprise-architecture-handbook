# Checklist 09: Observability FinOps & Telemetry Cost Audit

## 1. Overview
Quarterly financial audit checklist to identify telemetry waste, optimize storage tiers, and ensure monitoring costs remain within budget limits ($< 15\%$ of total cloud spend).

---

## 2. Verification Rubric

| FinOps Dimension | Audit Action | Target Standard | Pass/Fail |
| :--- | :--- | :--- | :--- |
| **Cost Attribution** | Review billing by squad tags (`owner_team`). | 100% of telemetry spend attributed to squads. | [ ] |
| **Tiered Storage** | Verify log/trace lifecycle policies. | Hot SSD retention $\le 7$ days; Cold object storage for rest. | [ ] |
| **Metrics Downsampling**| Confirm Thanos/Cortex downsampling active. | Raw $\le 14$d; 5m downsample $\le 90$d; 1h downsample $\le 365$d. | [ ] |
| **Log Volume Review**| Identify top 5 logging services. | Services emitting $> 100\text{GB/day}$ audited for log-to-metric conversion. | [ ] |
| **Trace Tail Sampling**| Verify nominal trace sampling ratios. | Nominal successes sampled at $\le 1.0\%$. | [ ] |
| **Cross-AZ Egress** | Inspect inter-zone telemetry network traffic. | OpenTelemetry Collectors deployed as local Node DaemonSets. | [ ] |
