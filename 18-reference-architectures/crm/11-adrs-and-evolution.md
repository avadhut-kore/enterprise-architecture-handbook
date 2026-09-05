# Architecture Decision Records & Evolution Roadmap: CRM

## 1. Canonical Architecture Decision Records

### ADR-001: Data Virtualization over Replication for ERP Financial History
- **Status**: Accepted
- **Context**: Replicating 10 years of detailed ERP line-item invoices into the CRM database would bloat relational storage by 40TB, costing over $200k/year in database licensing.
- **Decision**: Virtualize invoice histories using live OData v4 queries executed on-demand when the sales rep views the billing tab.
- **Consequences**: Drastically reduces CRM storage footprint; requires 200ms API timeout budget to ERP.

### ADR-002: Wide-Column Store for Append-Only Activity Timelines
- **Status**: Accepted
- **Context**: Storing billions of customer emails, calls, and click events in relational PostgreSQL causes severe table bloat and locks during sales pipeline updates.
- **Decision**: Decouple activity timelines into a dedicated wide-column NoSQL store (DynamoDB / Cassandra).
- **Consequences**: Linear horizontal scaling; eliminates OLTP locking.

---

## 2. Evolution Roadmap (1x to 100x Scale)
- **Stage 1 (1x Baseline)**: Modular monolith CRM on single PostgreSQL instance with basic email sync.
- **Stage 2 (10x Scale)**: Decoupled microservices on Kubernetes; dedicated DynamoDB activity store; Kafka integration with SAP.
- **Stage 3 (100x Scale)**: Multi-region active-active deployment; automated customer churn AI scoring; global edge caching.
