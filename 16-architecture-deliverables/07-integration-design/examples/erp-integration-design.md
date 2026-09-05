# INT-ERP-001: CRM to ERP Order Settlement Integration Design

---
**Metadata**:
* **Document ID**: INT-ERP-001
* **Source**: Salesforce CRM (Cloud)
* **Target**: SAP S/4HANA (On-Premises ERP)
* **Pattern**: Asynchronous Event Streaming via Apache Kafka
* **Status**: Approved
---

## 1. Architecture Flow
When an enterprise opportunity reaches `Closed - Won` in Salesforce, a Change Data Capture (CDC) event is published to an Apache Kafka topic. An integration microservice validates the contract, maps customer identifiers to SAP Business Partner IDs, and posts the sales order into SAP via RFC/OData.

## 2. Resilience & Error Handling
* Failed SAP postings are redirected to `sap-orders-dlq` with full payload and error code.
* Financial reconciliation runs nightly at 02:00 UTC verifying that total daily Salesforce contract value matches SAP General Ledger postings within $0.01 tolerance.
