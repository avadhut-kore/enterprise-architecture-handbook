# M&A Technology Due Diligence Playbook

How to evaluate an acquisition target's technology assets, hidden liabilities, and integration feasibility before deal closing.

---

## 1. The 6-Dimension M&A Due Diligence Checklist

| Dimension | Critical Questions to Investigate | Red Flag Risk |
| :--- | :--- | :--- |
| **1. Software Architecture & Code Quality** | What percentage of the codebase is covered by automated unit/integration tests? Is the architecture modular? | Zero test automation; massive spaghetti monolith; single developer knowledge. |
| **2. Technical Debt & EOL Runtimes** | Are systems running on unsupported OS, databases, or frameworks? | Running on EOL Windows Server 2008 / Java 7 requiring $5M immediate modernization. |
| **3. Open Source License Compliance** | Are there GPL/AGPL viral copyleft licenses embedded in proprietary commercial software? | Potential legal mandate to open-source proprietary target IP. |
| **4. Cybersecurity & Breach History** | What is the historical CVE vulnerability count? Has the target experienced undisclosed breaches? | Active unpatched zero-day vulnerabilities or ongoing regulatory investigation. |
| **5. Infrastructure & Cloud Contracts** | Are cloud commitments right-sized or under punitive minimum-spend penalties? | $8M annual AWS minimum commit with only $3M actual workload usage. |
| **6. Integration Complexity & Culture** | How hard will it be to federate identity, connect networks, and integrate ERPs? | Hardcoded proprietary data models fundamentally incompatible with acquiring firm. |
