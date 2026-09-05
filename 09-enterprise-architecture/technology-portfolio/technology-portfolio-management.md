# Technology Portfolio Management (TPM) Discipline

How Enterprise Architects systematically detect, track, and eliminate obsolete technology versions before they cause catastrophic outages or security breaches.

---

## 1. Automated Technology Discovery via Software Bill of Materials (SBOM)

```mermaid
flowchart LR
    Repo["Git Code Repositories"] --> Scanner["Dependency & SBOM Scanner (Trivy, Snyk, Dependabot)"]
    Scanner --> Inventory["Enterprise Technology Inventory Database"]
    Inventory --> Analyzer["EOL & CVE Vulnerability Engine"]
    Analyzer --> Alert["Automated Jira Tech Debt Tickets & ARB Alerts"]
```

---

## 2. Technology Health Metrics
* **Obsolescence Ratio**: $\frac{\text{Systems running on EOL Technology}}{\text{Total Active Systems}} \times 100\%$. (Target: < 2%).
* **Mean Time to Remediate (MTTR) Runtime Deprecation**: Target < 90 days from vendor EOL announcement.
