# Data Architecture: Global EdTech Platform

## 1. Polyglot Storage Strategy
- **PostgreSQL**: Stores relational course hierarchies, student enrollments, gradebooks, and financial transactions.
- **Cassandra / Timestream**: Ingests high-frequency student engagement telemetry (seconds watched, quiz pause events, clickstreams).
- **Amazon S3 / Blob Storage**: Stores raw and multi-bitrate transcoded video chunks (`.m3u8` master playlists and `.ts` video fragments).

## Operational Guidelines & Reliability Architecture
- **Idempotency & Safe Retries**: All transactions and mutations carry unique correlation IDs preventing duplicate execution.
- **Circuit Breakers & Timeouts**: Strict timeout policies protect core services from downstream cascading latency.
- **Disaster Recovery**: Automated multi-AZ replication guaranteeing operational continuity.
