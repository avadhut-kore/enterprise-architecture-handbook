# 07-INTEGRATION-DESIGN: Enterprise Application Integration (EAI) Design

## 1. Overview & Purpose
This directory provides production standards, master templates, and audit checklists for designing enterprise system-to-system integrations.

Every integration design must answer 11 foundational architecture questions:
1. Who owns each system (Team / Org / Vendor)?
2. What specific data crosses the system boundary?
3. Who initiates the interaction (Push vs Pull)?
4. Is the communication synchronous (blocking) or asynchronous (event/queue)?
5. What happens when the downstream system is degraded or down?
6. What happens when messages are duplicated (network replay)?
7. How is message ordering guaranteed across partitions?
8. How are retries, backoffs, and Dead-Letter Queues (DLQ) handled?
9. How is reconciliation performed to detect data discrepancies?
10. How is authentication and transport security enforced?
11. How is end-to-end distributed tracing monitored across boundaries?

---

## 2. Directory Contents
* **[template.md](template.md)**: Master Enterprise Integration Design template.
* **Integration Patterns**:
  - [rest.md](rest.md) — Synchronous RESTful service-to-service integration.
  - [graphql.md](graphql.md) — Federated GraphQL gateway integration.
  - [grpc.md](grpc.md) — High-throughput low-latency gRPC RPC.
  - [messaging.md](messaging.md) — Message queues (RabbitMQ, SQS, JMS).
  - [event-driven.md](event-driven.md) — Event streaming and pub/sub (Kafka, EventBridge).
  - [webhook.md](webhook.md) — Webhook ingestion and signature verification.
  - [batch.md](batch.md) — Scheduled batch processing and ETL pipelines.
  - [file-transfer.md](file-transfer.md) — Secure sFTP and managed file transfer (MFT).
  - [legacy-integration.md](legacy-integration.md) — Mainframe, AS400, and SOAP/XML bridges.
  - [saas-integration.md](saas-integration.md) — Salesforce, Workday, ServiceNow, and Stripe webhooks.
* **Resilience, Security & Operations**:
  - [integration-error-handling.md](integration-error-handling.md) — DLQ, poison pill handling, and circuit breakers.
  - [retry-and-idempotency.md](retry-and-idempotency.md) — Exponential backoff, jitter, and idempotency tables.
  - [reconciliation.md](reconciliation.md) — Automated end-of-day matching algorithms.
  - [integration-security.md](integration-security.md) — Mutual TLS, IP whitelisting, and OAuth2 client credentials.
  - [integration-observability.md](integration-observability.md) — W3C traceparent propagation and consumer lag telemetry.
* **Governance**:
  - [review-checklist.md](review-checklist.md) — 20-Point Integration Design Review Checklist.
  - [examples/erp-integration-design.md](examples/erp-integration-design.md) — Salesforce CRM to SAP S/4HANA ERP Integration Design.
