# Enterprise Architecture Metrics Framework

Architecture without measurement is opinion. How to measure architectural health across 8 core dimensions.

---

## 1. Master Architecture Metrics Scorecard

| Dimension | Key Performance Indicator (KPI) | Formula / Metric | Enterprise Target |
| :--- | :--- | :--- | :---: |
| **1. Business Alignment** | **Capability Modernization Rate** | $\frac{\text{Modernized Capabilities}}{\text{Total Critical Capabilities}} \times 100\%$ | > 25% / year |
| **2. Application Health** | **Legacy Application Debt Ratio** | $\frac{\text{Applications in 'Eliminate' Quadrant}}{\text{Total Application Count}} \times 100\%$ | < 5% |
| **3. Technology Health** | **Unsupported Technology Ratio** | $\frac{\text{Systems on EOL Runtimes/DBs}}{\text{Total System Count}} \times 100\%$ | < 2% |
| **4. Integration** | **Point-to-Point Coupling Ratio** | $\frac{\text{Un-governed P2P Integrations}}{\text{Total Integrations}} \times 100\%$ | < 5% |
| **5. Data Architecture** | **Golden Record Master Coverage** | $\frac{\text{Customer Entities Governed by MDM}}{\text{Total Customer Entities}} \times 100\%$ | > 95% |
| **6. Security & Risk** | **Critical CVE Dwell Time** | $\text{Mean Days from CVE Disclosure to Production Patch}$ | < 14 Days |
| **7. Cloud & FinOps** | **Cloud Unit Cost Efficiency** | $\frac{\text{Total Cloud Spend}}{\text{Total Business Transactions}}$ | Year-over-Year Reduction |
| **8. Governance** | **ARB Review Velocity & Adoption** | $\text{Average Business Days from Submission to ARB Decision}$ | < 7 Days |
