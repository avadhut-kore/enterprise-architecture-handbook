# Salesforce Enterprise Integration Architecture Guide

## 1. Overview
Salesforce provides a rich multi-tenant cloud ecosystem with distinct integration APIs, eventing buses, and strict governor limits. 

## 2. Directory Structure
- [salesforce-architecture.md](salesforce-architecture.md): Multi-tenant architecture and Force.com platform.
- [rest-api.md](rest-api.md): REST API, Composite resources, and sObject collections.
- [graphql.md](graphql.md): GraphQL API and declarative field querying.
- [bulk-api.md](bulk-api.md): Bulk API 2.0 for high-volume ETL ingestion.
- [platform-events.md](platform-events.md): High-volume Platform Events and Pub/Sub API.
- [change-data-capture.md](change-data-capture.md): CDC streams for asynchronous replication.
- [outbound-integration.md](outbound-integration.md): Apex callouts, Outbound Messaging, and Named Credentials.
- [inbound-integration.md](inbound-integration.md): Inbound REST, Connected Apps, and Mutual TLS.
- [data-synchronization.md](data-synchronization.md): Real-time sync vs. scheduled batch patterns.
- [identity.md](identity.md): Connected Apps, JWT Bearer Flow, and OAuth scopes.
- [security.md](security.md): Shield Platform Encryption, IP whitelisting, and field security.
- [limits-and-governance.md](limits-and-governance.md): API limits, Concurrent request limits, and mitigation.
- [error-handling.md](error-handling.md): Governor limit handling, replay IDs, and DLQs.
- [monitoring.md](monitoring.md): Event Monitoring, Real-Time Event Logs, and Datadog.
- [migration.md](migration.md): Data migration strategies and external ID indexing.
- [reference-architecture.md](reference-architecture.md): Complete Salesforce enterprise integration blueprint.
