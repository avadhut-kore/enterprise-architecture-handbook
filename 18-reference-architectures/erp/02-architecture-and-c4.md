# C4 Architecture Model & Cloud Mapping: Enterprise ERP

## 1. C4 Level 1: System Context Diagram

```mermaid
C4Context
title System Context: Enterprise ERP Platform
Person(accountant, "Corporate Accountant", "Performs journal postings and month-end close")
Person(buyer, "Procurement Officer", "Creates purchase orders and approves vendor invoices")
System(erp, "Enterprise ERP Core", "General Ledger, Procure-to-Pay, Order-to-Cash")
System_Ext(bank, "Corporate Banking Rails", "ISO 20022 pain.001 payment dispatch & camt.053 statements")
System_Ext(crm, "Salesforce CRM", "Syncs closed deals to generate sales orders")
System_Ext(wms, "Warehouse Management", "Pushes goods receipt inventory confirmations")

Rel(accountant, erp, "Reviews balance sheets", "HTTPS")
Rel(buyer, erp, "Approves purchase orders", "HTTPS")
Rel(erp, bank, "Transmits automated vendor payment batches", "mTLS SFTP / API")
Rel(crm, erp, "Pushes sales orders", "Kafka / OData v4")
Rel(wms, erp, "Confirms material receipt", "Kafka")
```

---

## 2. Technology-Neutral to Cloud Provider Mapping

| Component | Technology-Neutral | AWS Implementation | Azure Implementation | GCP Implementation |
| :--- | :--- | :--- | :--- | :--- |
| **In-Memory Ledger DB**| SAP HANA / Aurora In-Memory| Amazon EC2 Memory-Optimized | Azure M-Series Memory VMs | Google Cloud M2 Memory VMs |
| **ERP Sidecar Platform**| Cloud Foundry / K8s | AWS App Runner / EKS | Azure App Service / AKS | Cloud Run / GKE |
| **Financial Document Store**| WORM Object Storage | Amazon S3 Glacier Vault Lock | Azure Immutable Blob Storage | Google Cloud Storage Bucket Lock |
| **Integration Broker** | Apache Kafka | Amazon MSK | Azure Event Hubs | Google Cloud Pub/Sub |
