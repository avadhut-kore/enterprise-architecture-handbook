# Payment Gateway Infrastructure and Availability

## 1. High Availability Gateway SLA (99.999%)
A downtime of 10 minutes on major retail events (e.g., Black Friday) costs millions of dollars in lost volume. Enterprise payment gateways require:
- Multi-region active-active deployments with automatic DNS health checks.
- Sub-50ms in-memory cache lookups for merchant routing profiles.
- Circuit breaker trip thresholds with automated failover to alternate payment rails.

## 2. Gateway Infrastructure Topology

```
                       [Global Anycast DNS / CDN]
                                    │
            ┌───────────────────────┴───────────────────────┐
            ▼                                               ▼
   [Region A Gateway Pods]                         [Region B Gateway Pods]
   ├── Envoy mTLS Proxy                            ├── Envoy mTLS Proxy
   ├── Tokenization Service                        ├── Tokenization Service
   └── Redis Cluster (Local)                       └── Redis Cluster (Local)
            │                                               │
            └─────────────── (Cross-Region Sync) ───────────┘
```
