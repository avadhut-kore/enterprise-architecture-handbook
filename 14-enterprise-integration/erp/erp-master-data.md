# ERP Master Data Synchronization and MDM

## 1. Master Data Entities
ERP platforms act as the system of record or primary consumer for core enterprise master data:
- **Business Partner (BP)**: Unified customer, vendor, and counterparty records.
- **Material Master / Product Catalog**: SKU definitions, bills of materials (BOM), units of measure.
- **Chart of Accounts (COA)**: Cost centers, profit centers, general ledger accounts.

## 2. Bi-directional Synchronization Pattern
```
[Salesforce CRM] ──(New Customer Created)──> [Kafka: customer.created]
                                                      │
                                                      ▼
                                            [Enterprise MDM Hub]
                                            (Deduplication & Golden Record)
                                                      │
                                                      ▼ (OData / SOAP Service)
                                            [ERP System (SAP BP)]
```
