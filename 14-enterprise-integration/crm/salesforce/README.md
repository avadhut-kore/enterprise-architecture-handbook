# Salesforce Enterprise Integration Architecture Library

> A comprehensive architectural guide to integrating Salesforce with core enterprise systems, managing multitenant governor limits, real-time event streaming, and identity federation.

---

## 1. Overview & Architecture Persona

Integrating with Salesforce requires designing around its multitenant architecture, strict 24-hour API governor limits, and eventing infrastructure.

```
[Digital Apps / Portal] ──► [Salesforce CRM] ──► [Enterprise Event Mesh (Kafka)] ──► [Core ERP / Billing]
                              ├── REST & Composite (Synchronous UI / OLTP)
                              ├── Bulk API v2 (Mass Data Ingestion)
                              └── CDC / Platform Events (Asynchronous Decoupling)
```

---

## 2. API Selection Matrix

| Interface | Protocol | Latency | Volume / Limit | Preferred Architectural Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **Composite REST API** | HTTPS JSON | Sub-second ($< 300\text{ms}$) | Up to 25 dependent sub-requests | Interactive UI transactions; creating Account + Contacts in a single call. |
| **Bulk API v2** | HTTPS Batch | Minutes | Up to 100M rows / 24 hours | Nightly mass data synchronization, historical data lake backfills. |
| **Change Data Capture (CDC)**| gRPC / CometD | Real-time ($< 1\text{s}$) | High event volume (Replay IDs) | Asynchronously streaming object state changes to Kafka / data mesh. |
| **Platform Events** | gRPC / CometD | Real-time ($< 1\text{s}$) | Configurable publishing quota | Event-driven custom business notifications (e.g., `OrderApprovedEvent`). |
| **GraphQL API** | HTTPS JSON | Sub-second | Up to 250 fields / query | Single-endpoint declarative mobile & web client fetching (zero over-fetching).|

---

## 3. Directory Navigation & Technical Modules

### Core Platform & Protocols
* **[`salesforce-architecture.md`](salesforce-architecture.md)** — Multi-tenant architecture, Force.com metadata layer, and API tiers.
* **[`rest-api.md`](rest-api.md)** — Salesforce REST API, sObjects, collections, and Composite resources.
* **[`graphql.md`](graphql.md)** — Declarative field querying, pagination, and UI performance optimization.
* **[`bulk-api.md`](bulk-api.md)** — Bulk API 2.0 ingest/query, automated CSV chunking, and parallel processing.

### Event-Driven Streaming
* **[`change-data-capture.md`](change-data-capture.md)** — CDC channel subscriptions, `ChangeEventHeader`, and replay IDs.
* **[`platform-events.md`](platform-events.md)** — High-volume Platform Events, Pub/Sub API, and publish-behavior patterns.

### Inbound & Outbound Integration
* **[`inbound-integration.md`](inbound-integration.md)** — Inbound webhooks, Connected Apps, mutual TLS, and rate limiting.
* **[`outbound-integration.md`](outbound-integration.md)** — Apex HTTP callouts, Named Credentials, and Outbound Messaging.
* **[`data-synchronization.md`](data-synchronization.md)** — Bidirectional Account, Contact, and Opportunity synchronization with ERP.

### Security, Identity & Governance
* **[`identity.md`](identity.md)** — Connected Apps, OAuth 2.0 JWT Bearer Token Flow, and SSO federation.
* **[`security.md`](security.md)** — Shield Platform Encryption, IP restrictions, and least-privilege permission sets.
* **[`limits-and-governance.md`](limits-and-governance.md)** — Managing 24-hour API request pools and concurrent Long-Running API limits.
* **[`error-handling.md`](error-handling.md)** — Handling row locks (`UNABLE_TO_LOCK_ROW`), transient retries, and dead-letter queues.

### Operations, Monitoring & Reference Architecture
* **[`monitoring.md`](monitoring.md)** — Event Monitoring, Real-Time Event Logs, and APM Datadog/OpenTelemetry export.
* **[`migration.md`](migration.md)** — Org-to-Org consolidation, legacy CRM data migration, and External ID indexing.
* **[`reference-architecture.md`](reference-architecture.md)** — End-to-end Salesforce Enterprise Integration Reference Architecture.

---

## 4. Reading Roadmap: Where to Start?

1. **For Real-Time UI Integrations**: Start with [`rest-api.md`](rest-api.md) and [`identity.md`](identity.md).
2. **For High-Volume Synchronization**: Read [`bulk-api.md`](bulk-api.md), [`change-data-capture.md`](change-data-capture.md), and [`limits-and-governance.md`](limits-and-governance.md).
3. **For Enterprise Architecture Review**: Review [`reference-architecture.md`](reference-architecture.md) and [`security.md`](security.md).
