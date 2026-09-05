# Enterprise Debt Taxonomy: Technical vs Architectural vs Organizational

Understanding the three distinct layers of enterprise debt.

---

## 1. The 3 Dimensions of Enterprise Debt

```mermaid
graph TD
    A["1. Technical Debt (Code Layer)<br/>Messy code, missing unit tests, hardcoded credentials, unoptimized queries.<br/><b>Owner: Software Engineers & Tech Leads</b>"]
    B["2. Architectural Debt (Systems Layer)<br/>Monolithic coupling, point-to-point integrations, unsupported runtimes, missing DR.<br/><b>Owner: Solution & Enterprise Architects</b>"]
    C["3. Organizational Debt (Culture Layer)<br/>Siloed teams, handoff bureaucracy, misaligned KPIs, shadow IT purchasing.<br/><b>Owner: Business Leaders & Chief Architect</b>"]
    C --> B
    B --> A
```

---

## 2. Comparative Impact

| Debt Category | Scope | Cost to Remediate | Risk if Ignored |
| :--- | :--- | :---: | :--- |
| **Technical Debt** | Single repository or microservice. | Low (Days / Sprints) | Slower localized sprint velocity; minor software bugs. |
| **Architectural Debt** | Multi-system cross-cutting topology. | High (Months / Quarters) | Systemic cascading outages; inability to scale; massive security breach. |
| **Organizational Debt** | Enterprise operating model. | Very High (Years / Reorgs) | Paralysis of corporate agility; multi-million dollar capability duplication. |
