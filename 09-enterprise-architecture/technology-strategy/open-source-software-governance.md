# Open Source Software (OSS) Governance

Policies ensuring open source libraries do not introduce legal liabilities, IP contagion, or supply chain vulnerabilities.

---

## 1. Open Source License Risk Classification

| License Tier | Risk Profile | Examples | Enterprise Architectural Stance |
| :--- | :--- | :--- | :--- |
| **Permissive** | **Zero / Low Risk** | MIT, Apache 2.0, BSD-2/3, ISC | **Pre-Approved** for all commercial software. |
| **Weak Copyleft** | **Medium Risk** | LGPL, MPL 2.0, CDDL | **Approved with Conditions**: Permitted as dynamic linked libraries; no modification of source code. |
| **Strong Copyleft (Viral)** | **High / Critical Risk** | GPL v2/v3, AGPL | **PROHIBITED** in commercial proprietary distributed applications (risks forced source code disclosure). |
| **Server Side Public** | **Commercial Risk** | SSPL, BSL | **Review Required**: May trigger mandatory licensing fees when hosted as a cloud service. |
