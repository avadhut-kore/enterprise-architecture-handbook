# Application Portfolio Management (APM) Discipline

How modern Enterprise Architecture offices manage application inventories as financial portfolios rather than static inventories.

---

## 1. Core APM Lifecycle Stages

```mermaid
stateDiagram-v2
    [*] --> Discovered: Shadow IT or New Request
    Discovered --> UnderEvaluation: Architecture Assessment
    UnderEvaluation --> ApprovedInvest: High Value Strategic
    UnderEvaluation --> ApprovedTolerate: Stable Non-Strategic
    UnderEvaluation --> Rejected: Redundant Capability
    ApprovedInvest --> ProductionActive: Deployed
    ApprovedTolerate --> ProductionActive: Deployed
    ProductionActive --> MarkedRetirement: End-of-Life / Superseded
    MarkedRetirement --> Decommissioned: Data Archived & Servers Wiped
    Decommissioned --> [*]
```

---

## 2. Mandatory Application Registry Attributes
Every application record in the APM tool (e.g., LeanIX, ServiceNow APM) must maintain:
* **Business Dimension**: Owning Business Unit, Primary Capability, Secondary Capabilities, User Count, Business Criticality.
* **Technical Dimension**: Architecture Style, Primary Language/Framework, Database Engine, Hosting Type, Open Source Licenses.
* **Financial Dimension**: Annual Software Licensing, Cloud/Infrastructure Cost, Annual Support & Maintenance, TCO.
* **Risk Dimension**: Security Classification, Disaster Recovery Plan, CVE Vulnerability Count, Vendor Contract Expiration Date.
