# Resolving CRM vs. ERP Master Data Conflicts

## 1. Account Ownership Lifecycle
```
[Lead / Prospecting Phase] ──> Exists exclusively in CRM (Salesforce)
                                     │
                                     ▼ (Opportunity Won)
[Customer Conversion]      ──> CRM publishes account.won event
                                     │
                                     ▼
[Enterprise MDM]           ──> Validates tax ID, generates Global Cust ID
                                     │
                                     ▼
[ERP System]               ──> Creates Business Partner, assigns Payment Terms
                                     │
                                     ▼
[CRM System]               ◄── Backfills ERP Account Number onto CRM Record
```
