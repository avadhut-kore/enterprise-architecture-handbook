# Modernization Prioritization Model

A multi-criteria decision formula to rank application modernization initiatives across an enterprise portfolio.

---

## 1. The Prioritization Scoring Formula

$$\text{Priority Score} = \frac{(\text{Business Urgency} \times 0.30) + (\text{Risk Severity} \times 0.30) + (\text{Financial TCO ROI} \times 0.25)}{(\text{Execution Complexity} \times 0.15)}$$

* **Business Urgency (1–10)**: Executive priority, market expansion dependency, customer impact.
* **Risk Severity (1–10)**: Compliance deadlines (e.g., DORA, PCI-DSS 4.0), hardware/OS EOL date, CVE count.
* **Financial TCO ROI (1–10)**: License cost elimination, cloud efficiency gain, operational headcount savings.
* **Execution Complexity (1–10)**: Inter-system coupling, data migration size, third-party vendor lock-in.

---

## 2. Enterprise Initiative Ranking Table

| Rank | Application Name | Business Urgency (0.30) | Risk Severity (0.30) | TCO ROI (0.25) | Complexity (0.15) | Priority Score | Target Action |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | Core Payment Router | 9.5 | 9.0 | 8.5 | 6.0 | **8.85** | Re-architect to Cloud Event Mesh |
| **2** | Legacy Claims Database | 8.0 | 9.5 | 8.0 | 5.5 | **8.55** | Migrate to Managed Cloud Postgres |
| **3** | Regional B2B Portal | 7.5 | 6.0 | 9.0 | 4.0 | **7.80** | Consolidate onto Global SaaS |
| **4** | Internal Timesheet Tool | 2.0 | 2.0 | 4.0 | 2.0 | **3.20** | Eliminate / Replace with Workday |
