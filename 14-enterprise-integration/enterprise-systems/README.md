# Enterprise Systems Integration Architecture

## 1. Overview
Large enterprises operate a complex portfolio of packaged enterprise software:
- **ERP**: SAP S/4HANA, Oracle Cloud ERP (Financials, Material Master).
- **CRM**: Salesforce, Microsoft Dynamics 365 (Opportunities, Leads).
- **HRIS / HCM**: Workday, SAP SuccessFactors (Employee Master, Payroll).
- **ITSM**: ServiceNow (Incident Management, Asset Tracking).
- **SCM**: Blue Yonder, Manhattan (Supply Chain Planning, Warehousing).

## 2. Enterprise Hub-and-Spoke vs. Decentralized Mesh

```
                     Enterprise Event Backbone (Apache Kafka)
                                         │
        ┌──────────────────┬─────────────┴──────┬──────────────────┐
        ▼                  ▼                    ▼                  ▼
[SAP S/4HANA]       [Salesforce]            [Workday]         [ServiceNow]
├── OData v4        ├── Pub/Sub API         ├── RaaS REST     ├── REST Table API
└── BTP Sidecar     └── Event Bus           └── Enterprise CI └── Mid Server
```
