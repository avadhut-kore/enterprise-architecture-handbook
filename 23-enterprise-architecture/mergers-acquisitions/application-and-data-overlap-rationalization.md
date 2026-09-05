# M&A Application & Data Overlap Rationalization

How to eliminate duplicate software licenses and consolidate fragmented customer databases post-acquisition.

---

## 1. Post-Acquisition System Overlap Matrix

```mermaid
flowchart LR
    subgraph Acquiring Enterprise
        A1["Salesforce CRM"]
        A2["Workday HR"]
        A3["SAP S/4HANA ERP"]
    end
    subgraph Acquired Company
        B1["HubSpot CRM"]
        B2["BambooHR"]
        B3["NetSuite ERP"]
    end
    subgraph Rationalized Target
        T1["Global Standard: Salesforce CRM (Migrate Acquired Customers)"]
        T2["Global Standard: Workday HR (Absorb Acquired Headcount)"]
        T3["Two-Tier ERP: SAP for Corporate, NetSuite for Fast-Moving Subsidiary"]
    end
    A1 --> T1
    B1 --> T1
    A2 --> T2
    B2 --> T2
    A3 --> T3
    B3 --> T3
```
