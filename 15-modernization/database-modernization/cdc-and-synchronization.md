# Log-Based Change Data Capture (CDC) Architecture

## 1. The Non-Intrusive Replication Engine
Avoid polling databases with periodic `SELECT * WHERE updated_at > ?` queries, which causes severe table locks. Use **log-based Change Data Capture (Debezium)** reading the database transaction log directly:

```
[Legacy Monolithic DB (PostgreSQL / Oracle)]
       │
       ▼ (Transaction Log: WAL / Redo Log)
[Debezium CDC Connector]
       │
       ▼ (CloudEvents Stream: schema + before + after)
[Kafka Topic: cdc.orders]
       │
       ▼
[Kafka Connect JDBC Sink]
       │
       ▼ (Writes to Target Independent Database)
[Modern Orders Microservice DB]
```
