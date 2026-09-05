# Vendor Evaluation & Selection Playbook

How Enterprise Architects lead technology RFPs (Requests for Proposal) to select enterprise software vendors.

---

## 1. The 6-Dimension Vendor Evaluation Scorecard

```mermaid
radar
    title Vendor Evaluation Radar (Vendor A vs Vendor B)
    "Functional Capability Match": 90
    "Architectural Fit & Open APIs": 85
    "Security & Compliance (SOC 2)": 95
    "Vendor Financial Viability": 80
    "TCO & Pricing Predictability": 70
    "Developer Experience & SDKs": 75
```

---

## 2. Red Flag Disqualifiers During Vendor Vetting
* Vendor has no native REST/GraphQL APIs; relies on proprietary database connectors.
* Vendor contract stipulates that vendor owns aggregated or derived enterprise customer data.
* Vendor refuses to provide SOC 2 Type II reports or sign a Business Associate Agreement (BAA).
* Vendor requires proprietary on-premises hardware appliances in an enterprise cloud-first organization.
