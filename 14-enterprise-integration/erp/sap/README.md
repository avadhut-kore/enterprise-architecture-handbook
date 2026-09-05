# SAP S/4HANA & ECC Enterprise Integration Library

## 1. Overview
SAP powers over 70% of the world's transactional revenue. Integrating with SAP requires deep knowledge of both legacy protocols (BAPI, RFC, IDoc) and modern cloud interfaces (OData v2/v4, SAP Event Mesh, Cloud SDK).

## 2. Directory Structure
- [sap-architecture.md](sap-architecture.md): SAP technical landscape: NetWeaver, ABAP stack, S/4HANA in-memory DB.
- [sap-s4hana.md](sap-s4hana.md): S/4HANA integration paradigms, Core Data Services (CDS), and Fiori.
- [sap-erp.md](sap-erp.md): Legacy ECC 6.0 integration challenges and coexistence.
- [api-integration.md](api-integration.md): RESTful SAP APIs, Business Accelerator Hub, and SDKs.
- [odata.md](odata.md): OData v2 vs. v4, batch requests (`$batch`), and CSRF token handling.
- [idoc.md](idoc.md): Intermediate Document (IDoc) architecture: ALE, EDI, and tRFC.
- [events.md](events.md): SAP Event Mesh, Enterprise Messaging, and CloudEvents.
- [batch.md](batch.md): High-volume batch loading, LSMW, BAPI bulk loaders, and SLT.
- [master-data.md](master-data.md): SAP Master Data Governance (MDG) and Business Partner model.
- [finance.md](finance.md): FI/CO sub-ledger and Universal Journal (`ACDOCA`) integration.
- [procurement.md](procurement.md): MM (Materials Management) and Ariba Cloud Integration Gateway.
- [order-management.md](order-management.md): SD (Sales & Distribution) and Commerce Cloud integrations.
- [integration-platform.md](integration-platform.md): SAP Integration Suite (Cloud Integration / CPI) vs. Kafka.
- [security.md](security.md): SAP Principal Propagation, SNC, OAuth 2.0, and authorizations.
- [monitoring.md](monitoring.md): Solution Manager, SAP Cloud ALM, and OpenTelemetry monitoring.
- [migration.md](migration.md): ECC to S/4HANA integration migration: Brownfield vs. Greenfield.
- [reference-architecture.md](reference-architecture.md): End-to-end modern SAP integration blueprint.
