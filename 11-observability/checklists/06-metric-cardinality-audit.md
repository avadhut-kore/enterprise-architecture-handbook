# Checklist 06: Metric Cardinality & TSDB Capacity Audit

## 1. Overview
Audits Prometheus and time-series metrics to identify runaway cardinality, high-entropy label abuse, and prevent cluster memory exhaustion.

---

## 2. Verification Rubric

| Audit Step | Diagnostic Metric / Query | Threshold / Target | Pass/Fail |
| :--- | :--- | :--- | :--- |
| **Top Metric Series** | `topk(10, count by (__name__)({__name__=~".+"}))` | Any single metric generating $> 50,000$ active series must be investigated. | [ ] |
| **High Entropy Labels**| Prometheus TSDB status page (`/api/v1/status/tsdb`) | Top label names must not exceed 10,000 unique values. | [ ] |
| **UUIDs in Labels** | Regex scan of label values for `[a-f0-9\-]{36}` | **ZERO tolerance**: Dynamic IDs in metric labels are strictly prohibited. | [ ] |
| **Scrape Sample Limit** | `sample_limit` configured on all Prometheus scrape jobs. | Hard cap set (e.g., 10,000 series per pod target). | [ ] |
| **Label Pruning** | Relabel configs drop un-needed default labels (`pod_template_hash`, `uid`). | Verified in Prometheus config. | [ ] |
| **Scrape Frequency** | Scrape interval matches operational necessity. | Infrastructure: 30-60s; Application SLIs: 15s. | [ ] |
