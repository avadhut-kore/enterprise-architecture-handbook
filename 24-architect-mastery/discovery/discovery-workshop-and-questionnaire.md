# Discovery Workshop Playbook & Registers

Templates for conducting a 1-day executive architecture discovery workshop.

---

## 1. Discovery Workshop Agenda (Full Day)

* **09:00 - 10:30 | Business Strategy & Problem Framing**: What problem are we solving? What is the cost of doing nothing?
* **10:45 - 12:15 | User Journeys & Capability Mapping**: Walk through core value stream stages; identify current friction points.
* **13:00 - 14:30 | Technical Constraints & Legacy Landscape**: Audit existing systems, database schemas, and integration points.
* **14:45 - 16:00 | NFR Quantification**: Convert vague requirements into concrete latency, availability, and throughput budgets.
* **16:00 - 17:00 | Constraint & Assumption Register Sign-Off**: Review and validate discovered boundaries.

---

## 2. Master Constraint Register Template

| Constraint ID | Category | Description | Impact on Architecture | Flexibility |
| :--- | :--- | :--- | :--- | :---: |
| **CON-01** | Regulatory | All customer PII must reside physically in EU data centers (GDPR). | Mandates multi-region localized data vaults; no US egress. | **Zero** |
| **CON-02** | Legacy | Core accounting ledger runs on IBM AS/400; cannot be replaced. | Mandates an Anti-Corruption Layer and asynchronous CDC pipeline. | **Zero** |
| **CON-03** | Timeline | Must launch initial pilot within 6 months for holiday season. | Precludes full re-architecture; mandates strangler-fig canary. | **Low** |
| **CON-04** | Skills | Engineering staff has zero Kubernetes or Go experience; strong Java background. | Paved road must default to Java 21 / Spring Boot; avoid Go. | **Medium** |
