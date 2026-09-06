# Customer Relationship Management (CRM) Integration Architecture

## 1. Overview
CRM platforms (such as Salesforce, Microsoft Dynamics 365, HubSpot) manage customer interactions, sales pipelines, service cases, and marketing automation.

Integrating CRM into the enterprise requires synchronizing customer master records across billing, ERP, and operational portals while maintaining bidirectional event flows and respecting strict SaaS governor limits.

---

## 2. Directory Contents
* **[crm-integration.md](crm-integration.md)** — Architectural principles of CRM integration.
* **[customer-360.md](customer-360.md)** — Building a unified Customer 360 data view across platforms.
* **[master-customer-data.md](master-customer-data.md)** — Identity resolution, deduplication, and golden records.
* **[salesforce/](salesforce/README.md)** — Dedicated Salesforce Architecture & Integration Suite:
  - [salesforce-architecture.md](salesforce/salesforce-architecture.md) — Multitenant SaaS architecture and API tiers.
  - [rest-api.md](salesforce/rest-api.md) — Salesforce REST API, sObjects, and Composite resources.
  - [graphql.md](salesforce/graphql.md) — Salesforce GraphQL API and query optimizations.
  - [bulk-api.md](salesforce/bulk-api.md) — Bulk API v2 for multi-million record ETL ingestion.
  - [platform-events.md](salesforce/platform-events.md) — Real-time event pub/sub via CometD / Pub/Sub API.
  - [change-data-capture.md](salesforce/change-data-capture.md) — Real-time CDC streaming for object changes.
  - [outbound-integration.md](salesforce/outbound-integration.md) — Outbound messaging, Apex callouts, and Named Credentials.
  - [inbound-integration.md](salesforce/inbound-integration.md) — Inbound webhooks, Connected Apps, and rate limiting.
  - [data-synchronization.md](salesforce/data-synchronization.md) — Bidirectional Account/Contact sync with ERP.
  - [identity.md](salesforce/identity.md) — Salesforce as Identity Provider vs Service Provider (SSO).
  - [security.md](salesforce/security.md) — Shield Platform Encryption, IP restrictions, and OAuth scopes.
  - [limits-and-governance.md](salesforce/limits-and-governance.md) — Managing 24-hour API request and event publishing limits.
  - [error-handling.md](salesforce/error-handling.md) — Handling row locks (`UNABLE_TO_LOCK_ROW`) and retries.
  - [monitoring.md](salesforce/monitoring.md) — Event Monitoring, Real-Time Event Logs, and APM tracking.
  - [migration.md](salesforce/migration.md) — Org-to-Org and legacy CRM migration patterns.
  - [reference-architecture.md](salesforce/reference-architecture.md) — Enterprise Salesforce Integration Reference Architecture.
* **[examples/salesforce-erp-sync.md](examples/salesforce-erp-sync.md)** — Bidirectional Salesforce CRM to ERP Synchronization pipeline.
