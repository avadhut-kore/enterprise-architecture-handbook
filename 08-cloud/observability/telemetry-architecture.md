# Cloud Telemetry Architecture: Metrics, Logs, Events & Traces (MLET)

## Executive Summary

Modern observability unifies four complementary data types into an interconnected telemetry graph.

---

## 1. The MLET Quadrant

| Telemetry Type | Primary Purpose | Scaling Characteristics | Query Latency |
| :--- | :--- | :--- | :--- |
| **Metrics** | Real-time alerting, trend detection, dashboards | Highly compressible numerical time-series ($O(1)$) | Sub-second |
| **Logs** | Deep forensic debugging, auditing, contextual detail | Massive unstructured/JSON text volume; costly | Seconds to Minutes |
| **Traces** | End-to-end distributed latency waterfalls | Graph representation of request path across services | Seconds |
| **Events** | State transitions (deployments, auto-scale actions) | Low-frequency discrete occurrences | Sub-second |

---

## 2. The Correlation Rule
> **A metric alert must link directly to an exemplar distributed trace ID, which links directly to the specific JSON error log lines.** 
Without cross-telemetry correlation, MTTR increases by an order of magnitude as engineers hunt across disparate monitoring consoles.
