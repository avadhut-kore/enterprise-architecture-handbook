# Infrastructure & Telematics Pipelines: Logistics Platform

## 1. High-Throughput IoT Telematics Pipeline
```
[80,000 Trucks] ──(MQTT / TLS)──► [AWS IoT Core / EMQX Cluster]
                                                │
                                                ▼
                                    [Kafka Topic: fleet.telematics]
                                                │
                               ┌────────────────┴────────────────┐
                               ▼                                 ▼
                     [Real-Time Flink Worker]          [ClickHouse Cold Storage]
                     - H3 Geofence Evaluation          - 5-Year Historical GPS Log
                     - Speeding / Harsh Braking Alert  - Fleet Fuel Analytics
```
