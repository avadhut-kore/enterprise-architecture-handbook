# Design Authority & Decision Rights

Explicitly defining who has the authority to approve, reject, or veto architectural decisions across an organization.

---

## 1. Architectural Decision Rights Matrix

| Decision Level | Scope | Authority / Approver | Escalation Path |
| :--- | :--- | :--- | :--- |
| **Tier 1: Enterprise Mandate** | Enterprise platforms, corporate cloud vendor, master data model, security baseline. | **Chief Architect & Architecture Review Board (ARB)** | CIO / CTO |
| **Tier 2: Domain Standard** | Domain microservice topology, database engine (from approved radar), API contracts. | **Domain Architect** | Chief Architect |
| **Tier 3: Solution Design** | Project Solution Architecture Document (SAD), component decomposition, NFR allocation. | **Solution Architect** | Domain Architect |
| **Tier 4: Local Implementation** | Class hierarchies, code refactoring, package modularity, unit test frameworks. | **Technical Architect / Tech Lead** | Solution Architect |
