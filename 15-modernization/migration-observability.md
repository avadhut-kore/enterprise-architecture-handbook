# Observability During System Modernization

## 1. The Four Pillars of Migration Observability

```
Technical Metrics           Business Metrics           Data Parity Metrics          Migration Progress
├── Latency (p50/p95/p99)   ├── Checkout success rate  ├── Reconciliation breaks   ├── % Traffic shifted
├── HTTP 5xx error rate     ├── Total revenue ($)      ├── CDC replication lag     ├── # Workloads cut over
└── CPU/Memory saturation   └── Order volume/hour      └── Checksum mismatch rate  └── Rollback count
```

---

## 2. Telemetry Architecture across Hybrid Boundaries

```
[Legacy Monolith] ──(Custom Interceptor)──┐
                                          ├─► [W3C traceparent] ─► [OpenTelemetry Collector]
[Modern Service]  ──(OTel Auto-Instr)─────┘                                │
                                                                           ▼
                                                             [Distributed Tracing / Tempo]
                                                             [Prometheus Metrics]
                                                             [Structured Logs / Loki]
```

### Trace Context Propagation
Every request traversing legacy and modern systems must carry the W3C `traceparent` header. When legacy platforms (e.g., COBOL or CICS) cannot parse HTTP headers, map the trace ID into transactional user fields (e.g., CICS `commarea` or IBM MQ `CorrelationId`).

---

## 3. Real-Time Parity Dashboards
During shadow running and canary cutover, operations teams monitor real-time parity dashboards:
- **Response Code Parity**: Alert if the modern service returns HTTP 4xx/5xx while the legacy service returned HTTP 200.
- **Payload Match Ratio**: Alert if JSON payload equivalence falls below 99.99%.
- **Latency Differential**: Alert if the modern service p95 latency exceeds legacy p95 latency by more than 20%.
